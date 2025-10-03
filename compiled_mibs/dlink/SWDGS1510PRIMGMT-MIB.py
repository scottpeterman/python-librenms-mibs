# SNMP MIB module (SWDGS1510PRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\SWDGS1510PRIMGMT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:14 2025
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

(dlink_mgmt,
 dlink_products) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-mgmt",
    "dlink-products")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dlink_Dgs1510Prod_ObjectIdentity = ObjectIdentity
dlink_Dgs1510Prod = _Dlink_Dgs1510Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 137)
)
_Dlink_Dgs1510Prod_Dgs1510_20_ObjectIdentity = ObjectIdentity
dlink_Dgs1510Prod_Dgs1510_20 = _Dlink_Dgs1510Prod_Dgs1510_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 137, 1)
)
_Dlink_Dgs1510Prod_Dgs1510_28_ObjectIdentity = ObjectIdentity
dlink_Dgs1510Prod_Dgs1510_28 = _Dlink_Dgs1510Prod_Dgs1510_28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 137, 2)
)
_Dlink_Dgs1510Prod_Dgs1510_28P_ObjectIdentity = ObjectIdentity
dlink_Dgs1510Prod_Dgs1510_28P = _Dlink_Dgs1510Prod_Dgs1510_28P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 137, 3)
)
_Dlink_Dgs1510Prod_Dgs1510_52_ObjectIdentity = ObjectIdentity
dlink_Dgs1510Prod_Dgs1510_52 = _Dlink_Dgs1510Prod_Dgs1510_52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 137, 4)
)
_Dlink_Dgs1510Prod_Dgs1510_28X_ObjectIdentity = ObjectIdentity
dlink_Dgs1510Prod_Dgs1510_28X = _Dlink_Dgs1510Prod_Dgs1510_28X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 137, 6)
)
_Dlink_Dgs1510Prod_Dgs1510_52X_ObjectIdentity = ObjectIdentity
dlink_Dgs1510Prod_Dgs1510_52X = _Dlink_Dgs1510Prod_Dgs1510_52X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 137, 8)
)
_Dlink_Dgs1510Prod_Dgs1510_28XMP_ObjectIdentity = ObjectIdentity
dlink_Dgs1510Prod_Dgs1510_28XMP = _Dlink_Dgs1510Prod_Dgs1510_28XMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 137, 9)
)
_Dlink_Dgs1510Prod_Dgs1510_52XMP_ObjectIdentity = ObjectIdentity
dlink_Dgs1510Prod_Dgs1510_52XMP = _Dlink_Dgs1510Prod_Dgs1510_52XMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 137, 10)
)
_Dlink_Dgs1510Proj_ObjectIdentity = ObjectIdentity
dlink_Dgs1510Proj = _Dlink_Dgs1510Proj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118)
)
_Dlink_Dgs1510ProjModel_ObjectIdentity = ObjectIdentity
dlink_Dgs1510ProjModel = _Dlink_Dgs1510ProjModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 1)
)
_Dlink_Dgs1510Proj_Dgs1510_20_ObjectIdentity = ObjectIdentity
dlink_Dgs1510Proj_Dgs1510_20 = _Dlink_Dgs1510Proj_Dgs1510_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 1, 1)
)
_Dlink_Dgs1510Proj_Dgs1510_28_ObjectIdentity = ObjectIdentity
dlink_Dgs1510Proj_Dgs1510_28 = _Dlink_Dgs1510Proj_Dgs1510_28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 1, 2)
)
_Dlink_Dgs1510Proj_Dgs1510_28P_ObjectIdentity = ObjectIdentity
dlink_Dgs1510Proj_Dgs1510_28P = _Dlink_Dgs1510Proj_Dgs1510_28P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 1, 3)
)
_Dlink_Dgs1510Proj_Dgs1510_52_ObjectIdentity = ObjectIdentity
dlink_Dgs1510Proj_Dgs1510_52 = _Dlink_Dgs1510Proj_Dgs1510_52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 1, 4)
)
_Dlink_Dgs1510Proj_Dgs1510_28X_ObjectIdentity = ObjectIdentity
dlink_Dgs1510Proj_Dgs1510_28X = _Dlink_Dgs1510Proj_Dgs1510_28X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 1, 6)
)
_Dlink_Dgs1510Proj_Dgs1510_52X_ObjectIdentity = ObjectIdentity
dlink_Dgs1510Proj_Dgs1510_52X = _Dlink_Dgs1510Proj_Dgs1510_52X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 1, 8)
)
_Dlink_Dgs1510Proj_Dgs1510_28XMP_ObjectIdentity = ObjectIdentity
dlink_Dgs1510Proj_Dgs1510_28XMP = _Dlink_Dgs1510Proj_Dgs1510_28XMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 1, 9)
)
_Dlink_Dgs1510Proj_Dgs1510_52XMP_ObjectIdentity = ObjectIdentity
dlink_Dgs1510Proj_Dgs1510_52XMP = _Dlink_Dgs1510Proj_Dgs1510_52XMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 1, 10)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWDGS1510PRIMGMT-MIB",
    **{"dlink-Dgs1510Prod": dlink_Dgs1510Prod,
       "dlink-Dgs1510Prod-Dgs1510-20": dlink_Dgs1510Prod_Dgs1510_20,
       "dlink-Dgs1510Prod-Dgs1510-28": dlink_Dgs1510Prod_Dgs1510_28,
       "dlink-Dgs1510Prod-Dgs1510-28P": dlink_Dgs1510Prod_Dgs1510_28P,
       "dlink-Dgs1510Prod-Dgs1510-52": dlink_Dgs1510Prod_Dgs1510_52,
       "dlink-Dgs1510Prod-Dgs1510-28X": dlink_Dgs1510Prod_Dgs1510_28X,
       "dlink-Dgs1510Prod-Dgs1510-52X": dlink_Dgs1510Prod_Dgs1510_52X,
       "dlink-Dgs1510Prod-Dgs1510-28XMP": dlink_Dgs1510Prod_Dgs1510_28XMP,
       "dlink-Dgs1510Prod-Dgs1510-52XMP": dlink_Dgs1510Prod_Dgs1510_52XMP,
       "dlink-Dgs1510Proj": dlink_Dgs1510Proj,
       "dlink-Dgs1510ProjModel": dlink_Dgs1510ProjModel,
       "dlink-Dgs1510Proj-Dgs1510-20": dlink_Dgs1510Proj_Dgs1510_20,
       "dlink-Dgs1510Proj-Dgs1510-28": dlink_Dgs1510Proj_Dgs1510_28,
       "dlink-Dgs1510Proj-Dgs1510-28P": dlink_Dgs1510Proj_Dgs1510_28P,
       "dlink-Dgs1510Proj-Dgs1510-52": dlink_Dgs1510Proj_Dgs1510_52,
       "dlink-Dgs1510Proj-Dgs1510-28X": dlink_Dgs1510Proj_Dgs1510_28X,
       "dlink-Dgs1510Proj-Dgs1510-52X": dlink_Dgs1510Proj_Dgs1510_52X,
       "dlink-Dgs1510Proj-Dgs1510-28XMP": dlink_Dgs1510Proj_Dgs1510_28XMP,
       "dlink-Dgs1510Proj-Dgs1510-52XMP": dlink_Dgs1510Proj_Dgs1510_52XMP}
)
