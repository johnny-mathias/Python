drop table t_vendas;
drop sequence sq_t_vendas

DELETE FROM t_vendas
WHERE id_venda BETWEEN 2 AND 21;
COMMIT;
