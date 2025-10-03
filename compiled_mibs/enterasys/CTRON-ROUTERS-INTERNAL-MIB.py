# SNMP MIB module (CTRON-ROUTERS-INTERNAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CTRON-ROUTERS-INTERNAL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:41:17 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cabletron_ObjectIdentity = ObjectIdentity
cabletron = _Cabletron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4)
)
_Ctron_ObjectIdentity = ObjectIdentity
ctron = _Ctron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1)
)
_CtNetwork_ObjectIdentity = ObjectIdentity
ctNetwork = _CtNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3)
)
_CtronExp_ObjectIdentity = ObjectIdentity
ctronExp = _CtronExp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2)
)
_CtronRouterExp_ObjectIdentity = ObjectIdentity
ctronRouterExp = _CtronRouterExp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2)
)
_NwRouter_ObjectIdentity = ObjectIdentity
nwRouter = _NwRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2)
)
_NwRtrTemp_ObjectIdentity = ObjectIdentity
nwRtrTemp = _NwRtrTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99)
)
_NwRtrTemp1_ObjectIdentity = ObjectIdentity
nwRtrTemp1 = _NwRtrTemp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99, 2)
)
_NwRtrTemp2_ObjectIdentity = ObjectIdentity
nwRtrTemp2 = _NwRtrTemp2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99, 2, 2)
)


class _NwRtrSoftReset_Type(Integer32):
    """Custom type nwRtrSoftReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("reset", 0)
    )


_NwRtrSoftReset_Type.__name__ = "Integer32"
_NwRtrSoftReset_Object = MibScalar
nwRtrSoftReset = _NwRtrSoftReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99, 2, 2, 1),
    _NwRtrSoftReset_Type()
)
nwRtrSoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwRtrSoftReset.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-ROUTERS-INTERNAL-MIB",
    **{"cabletron": cabletron,
       "mibs": mibs,
       "ctron": ctron,
       "ctNetwork": ctNetwork,
       "ctronExp": ctronExp,
       "ctronRouterExp": ctronRouterExp,
       "nwRouter": nwRouter,
       "nwRtrTemp": nwRtrTemp,
       "nwRtrTemp1": nwRtrTemp1,
       "nwRtrTemp2": nwRtrTemp2,
       "nwRtrSoftReset": nwRtrSoftReset}
)
