# SNMP MIB module (AT-QOSv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\awplus\AT-QOSv2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:36 2025
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

atQosv2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 503)
)
if mibBuilder.loadTexts:
    atQosv2.setRevisions(
        ("2015-08-31 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtQosv2Notification_ObjectIdentity = ObjectIdentity
atQosv2Notification = _AtQosv2Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 503, 0)
)
_AtQosv2NotificationVariables_ObjectIdentity = ObjectIdentity
atQosv2NotificationVariables = _AtQosv2NotificationVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 503, 1)
)
_AtQosv2IfIndex_Type = InterfaceIndex
_AtQosv2IfIndex_Object = MibScalar
atQosv2IfIndex = _AtQosv2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 503, 1, 1),
    _AtQosv2IfIndex_Type()
)
atQosv2IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atQosv2IfIndex.setStatus("current")
_AtQosv2VlanId_Type = Integer32
_AtQosv2VlanId_Object = MibScalar
atQosv2VlanId = _AtQosv2VlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 503, 1, 2),
    _AtQosv2VlanId_Type()
)
atQosv2VlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atQosv2VlanId.setStatus("current")

# Managed Objects groups


# Notification objects

atQosv2StormDetectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 503, 0, 1)
)
atQosv2StormDetectionTrap.setObjects(
      *(("AT-QOSv2-MIB", "atQosv2IfIndex"),
        ("AT-QOSv2-MIB", "atQosv2VlanId"))
)
if mibBuilder.loadTexts:
    atQosv2StormDetectionTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-QOSv2-MIB",
    **{"atQosv2": atQosv2,
       "atQosv2Notification": atQosv2Notification,
       "atQosv2StormDetectionTrap": atQosv2StormDetectionTrap,
       "atQosv2NotificationVariables": atQosv2NotificationVariables,
       "atQosv2IfIndex": atQosv2IfIndex,
       "atQosv2VlanId": atQosv2VlanId}
)
