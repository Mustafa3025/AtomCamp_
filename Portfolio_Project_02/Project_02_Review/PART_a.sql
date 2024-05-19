#Part_A
#How many unique nodes are there in the data system?
select count(distinct node_id) as Unique_Nodes
from customer_nodes;

#What is the number of nodes per region.. it needs to be reprahased

SELECT c.region_id,
	region_name,
	COUNT(node_id) AS num_of_nodes
FROM customer_nodes c
INNER JOIN regions r
ON c.region_id = r.region_id
GROUP BY c.region_id, region_name
ORDER BY num_of_nodes DESC;