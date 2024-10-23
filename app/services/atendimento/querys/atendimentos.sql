select atd.cd_atendimento
from dbamv.atendime atd
where trunc(dt_atendimento) >= sysdate  - 10