# SNMP MIB module (BROCADE-UDLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\extreme\BROCADE-UDLD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:18 2025
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

(bcsiModules,) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "bcsiModules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

brocadeUdldMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 9)
)
if mibBuilder.loadTexts:
    brocadeUdldMIB.setRevisions(
        ("2018-05-29 12:00",
         "2016-09-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BcsiUdldNotifications_ObjectIdentity = ObjectIdentity
bcsiUdldNotifications = _BcsiUdldNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 0)
)
_BcsiUdldObjects_ObjectIdentity = ObjectIdentity
bcsiUdldObjects = _BcsiUdldObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 1)
)
_BcsiUdldNotifObjects_ObjectIdentity = ObjectIdentity
bcsiUdldNotifObjects = _BcsiUdldNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 1, 1)
)


class _BcsiUdldNotifMessage_Type(SnmpAdminString):
    """Custom type bcsiUdldNotifMessage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BcsiUdldNotifMessage_Type.__name__ = "SnmpAdminString"
_BcsiUdldNotifMessage_Object = MibScalar
bcsiUdldNotifMessage = _BcsiUdldNotifMessage_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 1, 1, 1),
    _BcsiUdldNotifMessage_Type()
)
bcsiUdldNotifMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcsiUdldNotifMessage.setStatus("current")
_BcsiUdldConformance_ObjectIdentity = ObjectIdentity
bcsiUdldConformance = _BcsiUdldConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 2)
)
_BcsiUdldCompliances_ObjectIdentity = ObjectIdentity
bcsiUdldCompliances = _BcsiUdldCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 2, 1)
)
_BcsiUdldGroups_ObjectIdentity = ObjectIdentity
bcsiUdldGroups = _BcsiUdldGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 2, 2)
)

# Managed Objects groups


# Notification objects

bcsiUdldNotifLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 0, 1)
)
bcsiUdldNotifLinkDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("BROCADE-UDLD-MIB", "bcsiUdldNotifMessage"))
)
if mibBuilder.loadTexts:
    bcsiUdldNotifLinkDown.setStatus(
        "current"
    )

bcsiUdldNotifLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 0, 2)
)
bcsiUdldNotifLinkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("BROCADE-UDLD-MIB", "bcsiUdldNotifMessage"))
)
if mibBuilder.loadTexts:
    bcsiUdldNotifLinkUp.setStatus(
        "current"
    )


# Notifications groups

bcsiUdldNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 2, 2, 1)
)
bcsiUdldNotifGroup.setObjects(
      *(("BROCADE-UDLD-MIB", "bcsiUdldNotifLinkDown"),
        ("BROCADE-UDLD-MIB", "bcsiUdldNotifLinkUp"))
)
if mibBuilder.loadTexts:
    bcsiUdldNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bcsiUdldCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 2, 1, 1)
)
bcsiUdldCompliance.setObjects(
    ("BROCADE-UDLD-MIB", "bcsiUdldNotifGroup")
)
if mibBuilder.loadTexts:
    bcsiUdldCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-UDLD-MIB",
    **{"brocadeUdldMIB": brocadeUdldMIB,
       "bcsiUdldNotifications": bcsiUdldNotifications,
       "bcsiUdldNotifLinkDown": bcsiUdldNotifLinkDown,
       "bcsiUdldNotifLinkUp": bcsiUdldNotifLinkUp,
       "bcsiUdldObjects": bcsiUdldObjects,
       "bcsiUdldNotifObjects": bcsiUdldNotifObjects,
       "bcsiUdldNotifMessage": bcsiUdldNotifMessage,
       "bcsiUdldConformance": bcsiUdldConformance,
       "bcsiUdldCompliances": bcsiUdldCompliances,
       "bcsiUdldCompliance": bcsiUdldCompliance,
       "bcsiUdldGroups": bcsiUdldGroups,
       "bcsiUdldNotifGroup": bcsiUdldNotifGroup}
)
