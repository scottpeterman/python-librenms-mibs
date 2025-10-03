# SNMP MIB module (HH3C-FIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-FIREWALL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:31:42 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cFireWall = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 88)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cFirewallobject_ObjectIdentity = ObjectIdentity
hh3cFirewallobject = _Hh3cFirewallobject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 88, 1)
)
_Hh3cFirewallSpecs_ObjectIdentity = ObjectIdentity
hh3cFirewallSpecs = _Hh3cFirewallSpecs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 88, 1, 1)
)
_Hh3cFWMaxConnNum_Type = Unsigned32
_Hh3cFWMaxConnNum_Object = MibScalar
hh3cFWMaxConnNum = _Hh3cFWMaxConnNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 88, 1, 1, 1),
    _Hh3cFWMaxConnNum_Type()
)
hh3cFWMaxConnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFWMaxConnNum.setStatus("current")
_Hh3cFirewallGlobalStats_ObjectIdentity = ObjectIdentity
hh3cFirewallGlobalStats = _Hh3cFirewallGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 88, 1, 2)
)
_Hh3cFWConnNumCurr_Type = Gauge32
_Hh3cFWConnNumCurr_Object = MibScalar
hh3cFWConnNumCurr = _Hh3cFWConnNumCurr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 88, 1, 2, 1),
    _Hh3cFWConnNumCurr_Type()
)
hh3cFWConnNumCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFWConnNumCurr.setStatus("current")
_Hh3cFWConnRate_Type = Gauge32
_Hh3cFWConnRate_Object = MibScalar
hh3cFWConnRate = _Hh3cFWConnRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 88, 1, 2, 2),
    _Hh3cFWConnRate_Type()
)
hh3cFWConnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFWConnRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FIREWALL-MIB",
    **{"hh3cFireWall": hh3cFireWall,
       "hh3cFirewallobject": hh3cFirewallobject,
       "hh3cFirewallSpecs": hh3cFirewallSpecs,
       "hh3cFWMaxConnNum": hh3cFWMaxConnNum,
       "hh3cFirewallGlobalStats": hh3cFirewallGlobalStats,
       "hh3cFWConnNumCurr": hh3cFWConnNumCurr,
       "hh3cFWConnRate": hh3cFWConnRate}
)
