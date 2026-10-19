"""Gera a pasta data_preparado/ a partir dos dados digitalizados (revisão do TCC).

Usada pelos notebooks da MM33 (painel B) e pelos notebooks *_sugestoes.ipynb.
Preparação aplicada:
  - Leitura correta: o arquivo data/all_data/data_frosberg19_fig3B_NOG_CTRL_3.csv usa ';'
    como separador e ',' como decimal. Lido corretamente, ele volta ao grupo controle da
    MM33 (painel B), que passa a ter 3 animais, como no artigo.
  - O primeiro ponto de cada série é o marcador de volume zero no dia do transplante
    (inoculação), desenhado sobre o eixo, e não uma medida. Ele é removido.
  - Volumes abaixo de 1 mm^3 estão abaixo da resolução das figuras digitalizadas
    (eixos de 200 a 800 mm^3) e correspondem a pontos desenhados sobre o eixo.
    Eles passam a valer 0.
Os arquivos originais não são alterados.
Uso: apague a pasta data_preparado/ e rode  python preparar_dados.py
"""
from pathlib import Path
import shutil

BASE = Path(__file__).resolve().parent
SRC = {"B": BASE / "data_figB", "C": BASE / "data_figC", "D": BASE / "data_figD"}
EXTRA = {"B": [BASE / "data" / "all_data" / "data_frosberg19_fig3B_NOG_CTRL_3.csv"]}
OUT = BASE / "data_preparado"
LIMIAR_ZERO = 1.0   # mm^3


def ler_estrito(fp):
    """Lê um CSV de duas colunas aceitando ',' ou ';' como separador e vírgula decimal
    quando o separador é ';'. Falha se a linha não tiver exatamente duas colunas."""
    linhas = [l.strip() for l in open(fp, encoding="utf-8") if l.strip()]
    rows = []
    for l in linhas[1:]:
        if ";" in l:
            partes = l.split(";")
            partes = [p.strip().replace(",", ".") for p in partes]
        else:
            partes = [p.strip() for p in l.split(",")]
        if len(partes) != 2:
            raise ValueError(f"{fp.name}: linha com {len(partes)} colunas: {l!r}")
        rows.append((float(partes[0]), float(partes[1])))
    return rows


def main():
    if OUT.exists():
        raise SystemExit(f"{OUT} já existe; apague-a manualmente para regenerar.")
    log = []
    for painel, pasta in SRC.items():
        destino = OUT / f"data_fig{painel}"
        destino.mkdir(parents=True)
        arquivos = sorted(pasta.glob("*.csv")) + EXTRA.get(painel, [])
        for fp in arquivos:
            rows = ler_estrito(fp)
            t0, v0 = rows[0]
            corpo = rows[1:]                       # remove o ponto de inoculação
            zerados = sum(1 for _, v in corpo if v < LIMIAR_ZERO)
            corpo = [(t, 0.0 if v < LIMIAR_ZERO else v) for t, v in corpo]
            with open(destino / fp.name, "w", encoding="utf-8") as f:
                f.write("x, y\n")
                for t, v in corpo:
                    f.write(f"{t:.6f}, {v:.6f}\n")
            log.append(f"{painel} {fp.name}: removido ({t0:.2f}, {v0:.4g}); "
                       f"{zerados} ponto(s) < {LIMIAR_ZERO} mm3 -> 0; restam {len(corpo)}")
    (OUT / "LEIAME_correcoes.txt").write_text(__doc__ + "\n\nRegistro:\n" + "\n".join(log),
                                              encoding="utf-8")
    print("\n".join(log))


if __name__ == "__main__":
    main()
