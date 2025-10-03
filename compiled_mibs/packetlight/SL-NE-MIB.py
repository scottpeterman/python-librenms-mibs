# SNMP MIB module (SL-NE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-NE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:42 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

packetlight = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sitelight_ObjectIdentity = ObjectIdentity
sitelight = _Sitelight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1)
)
_SlService_ObjectIdentity = ObjectIdentity
slService = _SlService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1)
)
_Plproduct_ObjectIdentity = ObjectIdentity
plproduct = _Plproduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100)
)
_Plne_ObjectIdentity = ObjectIdentity
plne = _Plne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1)
)
_Pl10_ObjectIdentity = ObjectIdentity
pl10 = _Pl10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 10)
)
_Pl10H_ObjectIdentity = ObjectIdentity
pl10H = _Pl10H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 10, 1)
)
_Pl10F_ObjectIdentity = ObjectIdentity
pl10F = _Pl10F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 10, 2)
)
_Pl20_ObjectIdentity = ObjectIdentity
pl20 = _Pl20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 20)
)
_Pl20H_ObjectIdentity = ObjectIdentity
pl20H = _Pl20H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 20, 1)
)
_Pl20F_ObjectIdentity = ObjectIdentity
pl20F = _Pl20F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 20, 2)
)
_Pl100_ObjectIdentity = ObjectIdentity
pl100 = _Pl100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 100)
)
_Pl100E_ObjectIdentity = ObjectIdentity
pl100E = _Pl100E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 100, 1)
)
_Pl100F_ObjectIdentity = ObjectIdentity
pl100F = _Pl100F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 100, 2)
)
_Pl100FG_ObjectIdentity = ObjectIdentity
pl100FG = _Pl100FG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 100, 3)
)
_Pl100EF_ObjectIdentity = ObjectIdentity
pl100EF = _Pl100EF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 100, 4)
)
_Pl100EFG_ObjectIdentity = ObjectIdentity
pl100EFG = _Pl100EFG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 100, 5)
)
_Pl100FT_ObjectIdentity = ObjectIdentity
pl100FT = _Pl100FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 100, 12)
)
_Plopto_ObjectIdentity = ObjectIdentity
plopto = _Plopto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 150)
)
_PloptoXB_ObjectIdentity = ObjectIdentity
ploptoXB = _PloptoXB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 150, 1)
)
_PloptoI_ObjectIdentity = ObjectIdentity
ploptoI = _PloptoI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 150, 2)
)
_PloptoX_ObjectIdentity = ObjectIdentity
ploptoX = _PloptoX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 150, 3)
)
_Pl200_ObjectIdentity = ObjectIdentity
pl200 = _Pl200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 200)
)
_Pl400r_ObjectIdentity = ObjectIdentity
pl400r = _Pl400r_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 400)
)
_Pl400_ObjectIdentity = ObjectIdentity
pl400 = _Pl400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 400, 1)
)
_Pl404r_ObjectIdentity = ObjectIdentity
pl404r = _Pl404r_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 404)
)
_Pl400e_ObjectIdentity = ObjectIdentity
pl400e = _Pl400e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 404, 1)
)
_Pl408r_ObjectIdentity = ObjectIdentity
pl408r = _Pl408r_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 408)
)
_Pl400x_ObjectIdentity = ObjectIdentity
pl400x = _Pl400x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 408, 1)
)
_Pl1000r_ObjectIdentity = ObjectIdentity
pl1000r = _Pl1000r_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 1000)
)
_Pl1000_ObjectIdentity = ObjectIdentity
pl1000 = _Pl1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 1000, 1)
)
_Pl1000e_ObjectIdentity = ObjectIdentity
pl1000e = _Pl1000e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 1000, 2)
)
_Pl1000em_ObjectIdentity = ObjectIdentity
pl1000em = _Pl1000em_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 1000, 3)
)
_Pl1000ro_ObjectIdentity = ObjectIdentity
pl1000ro = _Pl1000ro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 1000, 4)
)
_Pl1000tn_ObjectIdentity = ObjectIdentity
pl1000tn = _Pl1000tn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 1000, 5)
)
_Pl2000r_ObjectIdentity = ObjectIdentity
pl2000r = _Pl2000r_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 2000)
)
_Pl2000_ObjectIdentity = ObjectIdentity
pl2000 = _Pl2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 2000, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-NE-MIB",
    **{"packetlight": packetlight,
       "sitelight": sitelight,
       "slService": slService,
       "plproduct": plproduct,
       "plne": plne,
       "pl10": pl10,
       "pl10H": pl10H,
       "pl10F": pl10F,
       "pl20": pl20,
       "pl20H": pl20H,
       "pl20F": pl20F,
       "pl100": pl100,
       "pl100E": pl100E,
       "pl100F": pl100F,
       "pl100FG": pl100FG,
       "pl100EF": pl100EF,
       "pl100EFG": pl100EFG,
       "pl100FT": pl100FT,
       "plopto": plopto,
       "ploptoXB": ploptoXB,
       "ploptoI": ploptoI,
       "ploptoX": ploptoX,
       "pl200": pl200,
       "pl400r": pl400r,
       "pl400": pl400,
       "pl404r": pl404r,
       "pl400e": pl400e,
       "pl408r": pl408r,
       "pl400x": pl400x,
       "pl1000r": pl1000r,
       "pl1000": pl1000,
       "pl1000e": pl1000e,
       "pl1000em": pl1000em,
       "pl1000ro": pl1000ro,
       "pl1000tn": pl1000tn,
       "pl2000r": pl2000r,
       "pl2000": pl2000}
)
