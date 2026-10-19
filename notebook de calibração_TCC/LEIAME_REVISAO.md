# Revisão dos códigos

Os notebooks originais foram corrigidos no próprio arquivo. Cada trecho alterado tem o
comentário `# CORREÇÃO (revisão)`, e a segunda célula de cada notebook resume o que mudou e por quê.
Os notebooks já foram executados com as correções.

## Notebooks corrigidos (os mesmos de antes)

| Notebook | O que foi corrigido | Saídas |
|---|---|---|
| `calibracao_crescimento B.ipynb` | Leitura do controle 3 da MM33 (vírgula decimal); análise da MM33 refeita | `calibration_outputs_didatico/` |
| `6tratacalibracao_tratamento B.ipynb` | Crescimento lido do controle corrigido; sem o piso d_max ≥ r; MM/LS/dePR → const; funções novas | `calibration_outputs_tratamento/` |
| `calibracao_crescimento C e D.ipynb` | Leitura estrita dos CSV; aviso de parâmetro no limite (`build_diagnostics`) | `calibration_outputs_didatico/` |
| `6tratacalibracao_tratamento C.ipynb` | Leitura estrita dos CSV; `SORT_REGEX` (resultados iguais aos do TCC) | `calibration_outputs_tratamento/` |
| `6tratacalibracao_tratamento D.ipynb` | Leitura estrita dos CSV (resultados iguais aos do TCC) | `calibration_outputs_tratamento/` |

Ordem de execução: crescimento antes do tratamento da mesma linhagem.

## Sugestões (opcionais)

Nos notebooks da 92-1 e da UM121213B, as sugestões estão como comentários `# SUGESTÃO (revisão)`.
Cada uma indica o notebook em que ela já está implementada e executada:

| Notebook de sugestão | O que muda | Saídas |
|---|---|---|
| `6tratacalibracao_tratamento C_sugestao_sem_piso.ipynb` | Só o limite inferior d_max ≥ r é retirado | `calibration_outputs_sugestao_sem_piso/` |
| `6tratacalibracao_tratamento D_sugestao_sem_piso.ipynb` | Só o limite inferior d_max ≥ r é retirado | `calibration_outputs_sugestao_sem_piso/` |
| `calibracao_crescimento C e D_sugestoes.ipynb` | Dados preparados, T0 e limites únicos, mais partidas | `calibration_outputs_sugestoes/` |
| `6tratacalibracao_tratamento C_sugestoes.ipynb` | Idem, mais taxa constante e funções ED, T_atraso, T_bateman | `calibration_outputs_sugestoes/` |
| `6tratacalibracao_tratamento D_sugestoes.ipynb` | Idem | `calibration_outputs_sugestoes/` |

Os notebooks `*_sugestoes` usam os dados de `data_preparado/`, gerados por `preparar_dados.py`
(ponto de inoculação removido, volumes < 1 mm³ = 0, controle 3 da MM33 lido corretamente). Para
adotar uma sugestão, compare o trecho marcado no notebook de sugestão com o mesmo trecho do original
e substitua no TCC as tabelas e figuras pelas geradas por ele.

## Outras pastas

- `data/`, `data_figB/`, `data_figC/`, `data_figD/`: dados originais, sem alteração.
