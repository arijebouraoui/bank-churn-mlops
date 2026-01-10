\# Preuve DVC - Data Versioning



\## Configuration DVC



\### Fichiers de configuration présents:

\- `.dvc/config` - Configuration DVC

\- `.dvc/.gitignore` - Ignore rules

\- `.dvcignore` - DVC ignore patterns

\- `data/bank\_churn.csv.dvc` - Fichier de tracking DVC



\### Remote DVC configuré:

```bash

C:\\Users\\erijb\\AppData\\Roaming\\Python\\Python311\\Scripts\\dvc.exe remote list

\# Output: myremote    C:\\dvc-storage  (default)

```



\## Démonstration push/pull



\### Test 1: DVC Push (effectué)

```bash

python -m dvc push

\# ✅ Données poussées vers C:\\dvc-storage

```



\### Test 2: DVC Pull - Reproductibilité (effectué)

```bash

\# 1. Supprimer le fichier local

del data\\bank\_churn.csv



\# 2. Restaurer depuis DVC

python -m dvc pull



\# 3. Vérifier la restauration

dir data

\# ✅ bank\_churn.csv est de retour! (589,233 bytes)

```



\## Contenu du fichier .dvc

```yaml

\# data/bank\_churn.csv.dvc

outs:

\- md5: \[hash\_du\_fichier]

&nbsp; size: 589233

&nbsp; path: bank\_churn.csv

```



\## Conclusion



✅ DVC configuré avec succès

✅ Remote storage fonctionnel

✅ Reproductibilité démontrée (delete + pull = restore)

