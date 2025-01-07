import nest
import numpy

nest.ResetKernel()

# Set simulation kernel
nest.SetKernelStatus({
  "local_num_threads": 1,
  "resolution": 0.1,
  "rng_seed": 1
})

# Create nodes
n1 = nest.Create("iaf_psc_alpha", 800, params={
  "V_th": -50,
  "tau_m": 20,
})
n2 = nest.Create("iaf_psc_alpha", 200, params={
  "V_th": -50,
  "tau_m": 20,
})
pg1 = nest.Create("poisson_generator", 1, params={
  "rate": 18000,
})
sr1 = nest.Create("spike_recorder", 1)
sr2 = nest.Create("spike_recorder", 1)

# Connect nodes
nest.Connect(n1, n1, conn_spec={
  "rule": "fixed_indegree",
  "indegree": 200,
}, syn_spec={ 
  "weight": 2.5,
  "delay": 1.5,
})
nest.Connect(n1, n2, conn_spec={
  "rule": "fixed_indegree",
  "indegree": 200,
}, syn_spec={ 
  "weight": 2.5,
  "delay": 1.5,
})
nest.Connect(n2, n1, conn_spec={
  "rule": "fixed_indegree",
  "indegree": 50,
}, syn_spec={ 
  "weight": -15,
  "delay": 1.5,
})
nest.Connect(n2, n2, conn_spec={
  "rule": "fixed_indegree",
  "indegree": 50,
}, syn_spec={ 
  "weight": -15,
  "delay": 1.5,
})
nest.Connect(pg1, n1, syn_spec={ 
  "weight": 2.5,
  "delay": 1.5,
})
nest.Connect(pg1, n2, syn_spec={ 
  "weight": 2.5,
  "delay": 1.5,
})
nest.Connect(n1, sr1, syn_spec={ 
  "weight": 1,
  "delay": 1.5,
})
nest.Connect(n2, sr2, syn_spec={ 
  "weight": 1,
  "delay": 1.5,
})

# Run simulation
nest.Simulate(1000)

response = {
  "events": [sr1.events, sr2.events, ]
}
