# Install of illumiprocessor on Hydra computing cluster

Process used for installing/testing illumiprocessor for development of multiple trimmers

## `mamba` install

```bash
$ mamba create -n illumi -c conda-forge python=3.6

...

  Package              Version  Build               Channel           Size
  + ld_impl_linux-64      2.40  hf3520f5_3          conda-forge      714kB
  + _libgcc_mutex          0.1  conda_forge         conda-forge     Cached
  + libstdcxx-ng        13.2.0  hc0a3c3a_7          conda-forge     Cached
  + ca-certificates   2024.6.2  hbcca054_0          conda-forge     Cached
  + libgomp             13.2.0  h77fa898_7          conda-forge     Cached
  + _openmp_mutex          4.5  2_gnu               conda-forge     Cached
  + libgcc-ng           13.2.0  h77fa898_7          conda-forge     Cached
  + xz                   5.2.6  h166bdaf_0          conda-forge     Cached
  + openssl             1.1.1w  hd590300_0          conda-forge     Cached
  + ncurses                6.5  h59595ed_0          conda-forge     Cached
  + libzlib              1.3.1  h4ab18f5_1          conda-forge     Cached
  + libnsl               2.0.1  hd590300_0          conda-forge     Cached
  + libffi               3.4.2  h7f98852_5          conda-forge     Cached
  + readline               8.2  h8228510_1          conda-forge     Cached
  + tk                  8.6.13  noxft_h4845f30_101  conda-forge     Cached
  + libsqlite           3.46.0  hde9e2c9_0          conda-forge      865kB
  + sqlite              3.46.0  h6d4b2fc_0          conda-forge      860kB
  + python              3.6.15  hb7a2778_0_cpython  conda-forge     Cached
  + python_abi             3.6  2_cp36m             conda-forge     Cached
  + setuptools          58.0.4  py36h5fab9bb_2      conda-forge     Cached
  + wheel               0.37.1  pyhd8ed1ab_0        conda-forge     Cached
  + pip                 21.3.1  pyhd8ed1ab_0        conda-forge     Cached

...

(illumi)$ mamba activate illumi
(illumi)$ cd ~
(illumi)$ git clone https://github.com/kweskinm/illumiprocessor/
(illumi)$ cd illumiprocessor
(illumi)$ python setup.py install
```

Setup trimmomatic and a wrapper script. I will be using a system-wide java install

```bash
(illumi)$ cd $CONDA_PREFIX/share
(illumi)$ wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.39.zip
(illumi)$ unzip Trimmomatic-0.39.zip
(illumi)$ mv Trimmomatic-0.39 trimmomatic-0.39-2
(illumi)$ cd trimmomatic-0.39-2
(illumi)$ ln -s trimmomatic-0.39.jar trimmomatic.jar
(illumi)$ cp -a /share/apps/bioinformatics/phyluce/1.7.3/share/trimmomatic-0.39-2/trimmomatic $CONDA_PREFIX/share/trimmomatic-0.39-2/trimmomatic 
(illumi)$ cp -a /share/apps/bioinformatics/phyluce/1.7.3/bin/trimmomatic $CONDA_PREFIX/bin
(illumi)$ java -version
openjdk version "1.8.0_402"
OpenJDK Runtime Environment (build 1.8.0_402-b06)
OpenJDK 64-Bit Server VM (build 25.402-b06, mixed mode)
```

Test

```bash
(illumi)$ illumiprocessor 
usage: illumiprocessor [-h] --input INPUT --output OUTPUT --config CONFIG
                       [--trimmomatic TRIMMOMATIC] [--min-len MIN_LEN]
                       [--no-merge] [--cores CORES] [--r1-pattern R1_PATTERN]
                       [--r2-pattern R2_PATTERN] [--se]
                       [--phred {phred33,phred64}] [--log-path LOG_PATH]
                       [--verbosity {INFO,WARN,CRITICAL}]
illumiprocessor: error: the following arguments are required: --input, --output, --config

$ trimmomatic 
Usage: 
       PE [-version] [-threads <threads>] [-phred33|-phred64] [-trimlog <trimLogFile>] [-summary <statsSummaryFile>] [-quiet] [-validatePairs] [-basein <inputBase> | <inputFile1> <inputFile2>] [-baseout <outputBase> | <outputFile1P> <outputFile1U> <outputFile2P> <outputFile2U>] <trimmer1>...
   or: 
       SE [-version] [-threads <threads>] [-phred33|-phred64] [-trimlog <trimLogFile>] [-summary <statsSummaryFile>] [-quiet] <inputFile> <outputFile> <trimmer1>...
   or: 
       -version
(illumi)$ trimmomatic -version
0.39
```

Add trim_galore

```bash
(illumi) $ mamba install bioconda::trim-galore
```
