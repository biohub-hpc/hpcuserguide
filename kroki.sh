#!/bin/bash
#
export APPTAINERENV_KROKI_LISTEN=localhost:51080
export KROKI_LISTEN=localhost:51080
echo "Kroki on http://${APPTAINERENV_KROKI_LISTEN}"
# unset APPTAINERENV_KROKI_LISTEN KROKI_LISTEN
apptainer run docker://yuzutech/kroki

