{
 "name":"My Finance Tracker",
 "summary":"Module for managing finances",
 "category":"Tools",
 "version":"17.0.1.0.0",
 "sequence": -100,
 "author":"QuantumBonney",
 "depends":["base",'mail'],
 "data":
 [
    "security/ir.model.access.csv",
    "views/finance_tracker_views.xml",
    "data/ir_cron.xml",
     ],


 "installable": True,
 "application": True,
 "license": "LGPL-3"
}

