# 2020-03-23 sokol@insa-toulouse.fr
# experiments with planemo for creating influx_si galaxy wrapper

# init
cd /home/sokol/dev/galaxy
planemo project_init --template=demo influx_si
cd influx_si

# test with galaxy
planemo test --galaxy_root=/usr/local/src/galaxy randomlines.xml
# failed 1 of 2

# init tool seqtk
cd ../seqtk
planemo tool_init --force \
                    --id 'seqtk_seq' \
                    --name 'Convert to FASTA (seqtk)' \
                    --requirement seqtk@1.2 \
                    --example_command 'seqtk seq -a 2.fastq > 2.fasta' \
                    --example_input 2.fastq \
                    --example_output 2.fasta \
                    --test_case \
                    --cite_url 'https://github.com/lh3/seqtk' \
                    --help_from_command 'seqtk seq'

# init influx_si
cd /home/sokol/dev/galaxy/influx_si
cp /home/sokol/dev/sysbio/ftbl2sys/test_cases/cases/e_coli.ftbl .

planemo tool_init --force \
                    --id 'influx_s' \
                    --name 'Estimate metabolic fluxes from stationary labeling' \
                    --requirement influx_si@5.0.3 \
                    --example_command 'influx_s e_coli' \
                    --example_input e_coli.ftbl \
                    --example_output e_coli_res.kvh \
                    --test_case \
                    --cite_url 'https://github.com/sgsokol/influx' \
                    --help_from_command 'influx_s -h'
# lint
planemo l
# test in galaxy
planemo t


