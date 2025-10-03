# SNMP MIB module (DLINKSW-IMPB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-IMPB-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:13 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwImpbMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 22)
)
if mibBuilder.loadTexts:
    dlinkSwImpbMIB.setRevisions(
        ("2015-11-06 00:00",
         "2013-10-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DImpbNotifications_ObjectIdentity = ObjectIdentity
dImpbNotifications = _DImpbNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 0)
)
_DImpbObjects_ObjectIdentity = ObjectIdentity
dImpbObjects = _DImpbObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 1)
)
_DImpbNotifyInfo_ObjectIdentity = ObjectIdentity
dImpbNotifyInfo = _DImpbNotifyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 1, 1)
)


class _DImpbGlobalNotifyEnabled_Type(TruthValue):
    """Custom type dImpbGlobalNotifyEnabled based on TruthValue"""
    defaultValue = 2


_DImpbGlobalNotifyEnabled_Type.__name__ = "TruthValue"
_DImpbGlobalNotifyEnabled_Object = MibScalar
dImpbGlobalNotifyEnabled = _DImpbGlobalNotifyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 1, 1, 1),
    _DImpbGlobalNotifyEnabled_Type()
)
dImpbGlobalNotifyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dImpbGlobalNotifyEnabled.setStatus("current")
_DImpbViolationIpAddrType_Type = InetAddressType
_DImpbViolationIpAddrType_Object = MibScalar
dImpbViolationIpAddrType = _DImpbViolationIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 1, 1, 2),
    _DImpbViolationIpAddrType_Type()
)
dImpbViolationIpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dImpbViolationIpAddrType.setStatus("current")
_DImpbViolationIpAddress_Type = InetAddress
_DImpbViolationIpAddress_Object = MibScalar
dImpbViolationIpAddress = _DImpbViolationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 1, 1, 3),
    _DImpbViolationIpAddress_Type()
)
dImpbViolationIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dImpbViolationIpAddress.setStatus("current")
_DImpbIfConfigTable_Object = MibTable
dImpbIfConfigTable = _DImpbIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 1, 2)
)
if mibBuilder.loadTexts:
    dImpbIfConfigTable.setStatus("current")
_DImpbIfConfigEntry_Object = MibTableRow
dImpbIfConfigEntry = _DImpbIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 1, 2, 1)
)
dImpbIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dImpbIfConfigEntry.setStatus("current")


class _DImpbIfBindMode_Type(Integer32):
    """Custom type dImpbIfBindMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("strict", 2),
          ("loose", 3))
    )


_DImpbIfBindMode_Type.__name__ = "Integer32"
_DImpbIfBindMode_Object = MibTableColumn
dImpbIfBindMode = _DImpbIfBindMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 1, 2, 1, 1),
    _DImpbIfBindMode_Type()
)
dImpbIfBindMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dImpbIfBindMode.setStatus("current")
_DImpbViolationLogTable_Object = MibTable
dImpbViolationLogTable = _DImpbViolationLogTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 1, 3)
)
if mibBuilder.loadTexts:
    dImpbViolationLogTable.setStatus("current")
_DImpbViolationLogEntry_Object = MibTableRow
dImpbViolationLogEntry = _DImpbViolationLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 1, 3, 1)
)
dImpbViolationLogEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DLINKSW-IMPB-MIB", "dImpbViolationVlan"),
    (0, "DLINKSW-IMPB-MIB", "dImpbViolationMacAddress"),
)
if mibBuilder.loadTexts:
    dImpbViolationLogEntry.setStatus("current")
_DImpbViolationVlan_Type = VlanId
_DImpbViolationVlan_Object = MibTableColumn
dImpbViolationVlan = _DImpbViolationVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 1, 3, 1, 1),
    _DImpbViolationVlan_Type()
)
dImpbViolationVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dImpbViolationVlan.setStatus("current")
_DImpbViolationMacAddress_Type = MacAddress
_DImpbViolationMacAddress_Object = MibTableColumn
dImpbViolationMacAddress = _DImpbViolationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 1, 3, 1, 2),
    _DImpbViolationMacAddress_Type()
)
dImpbViolationMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dImpbViolationMacAddress.setStatus("current")


class _DImpbViolationAction_Type(Integer32):
    """Custom type dImpbViolationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DImpbViolationAction_Type.__name__ = "Integer32"
_DImpbViolationAction_Object = MibTableColumn
dImpbViolationAction = _DImpbViolationAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 1, 3, 1, 99),
    _DImpbViolationAction_Type()
)
dImpbViolationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dImpbViolationAction.setStatus("current")
_DImpbClearObjects_ObjectIdentity = ObjectIdentity
dImpbClearObjects = _DImpbClearObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 1, 4)
)


class _DImpbClearAllViolation_Type(Integer32):
    """Custom type dImpbClearAllViolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DImpbClearAllViolation_Type.__name__ = "Integer32"
_DImpbClearAllViolation_Object = MibScalar
dImpbClearAllViolation = _DImpbClearAllViolation_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 1, 4, 1),
    _DImpbClearAllViolation_Type()
)
dImpbClearAllViolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dImpbClearAllViolation.setStatus("current")
_DImpbClearViolationByIf_Type = InterfaceIndexOrZero
_DImpbClearViolationByIf_Object = MibScalar
dImpbClearViolationByIf = _DImpbClearViolationByIf_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 1, 4, 2),
    _DImpbClearViolationByIf_Type()
)
dImpbClearViolationByIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dImpbClearViolationByIf.setStatus("current")
_DImpbConformance_ObjectIdentity = ObjectIdentity
dImpbConformance = _DImpbConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 2)
)
_DImpbMIBCompliances_ObjectIdentity = ObjectIdentity
dImpbMIBCompliances = _DImpbMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 2, 1)
)
_DImpbMIBGroups_ObjectIdentity = ObjectIdentity
dImpbMIBGroups = _DImpbMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 2, 2)
)

# Managed Objects groups

dImpbConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 2, 2, 1)
)
dImpbConfigGroup.setObjects(
    ("DLINKSW-IMPB-MIB", "dImpbIfBindMode")
)
if mibBuilder.loadTexts:
    dImpbConfigGroup.setStatus("current")

dImpbClearViolationLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 2, 2, 2)
)
dImpbClearViolationLogGroup.setObjects(
      *(("DLINKSW-IMPB-MIB", "dImpbViolationAction"),
        ("DLINKSW-IMPB-MIB", "dImpbClearAllViolation"),
        ("DLINKSW-IMPB-MIB", "dImpbClearViolationByIf"))
)
if mibBuilder.loadTexts:
    dImpbClearViolationLogGroup.setStatus("current")


# Notification objects

dImpbViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 0, 1)
)
dImpbViolationTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("DLINKSW-IMPB-MIB", "dImpbViolationIpAddrType"),
        ("DLINKSW-IMPB-MIB", "dImpbViolationIpAddress"),
        ("DLINKSW-IMPB-MIB", "dImpbViolationMacAddress"),
        ("DLINKSW-IMPB-MIB", "dImpbViolationVlan"))
)
if mibBuilder.loadTexts:
    dImpbViolationTrap.setStatus(
        "current"
    )


# Notifications groups

dImpbNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 2, 2, 3)
)
dImpbNotificationsGroup.setObjects(
    ("DLINKSW-IMPB-MIB", "dImpbViolationTrap")
)
if mibBuilder.loadTexts:
    dImpbNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dImpbMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 22, 2, 1, 1)
)
dImpbMIBCompliance.setObjects(
      *(("DLINKSW-IMPB-MIB", "dImpbConfigGroup"),
        ("DLINKSW-IMPB-MIB", "dImpbNotificationsGroup"),
        ("DLINKSW-IMPB-MIB", "dImpbClearViolationLogGroup"))
)
if mibBuilder.loadTexts:
    dImpbMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-IMPB-MIB",
    **{"dlinkSwImpbMIB": dlinkSwImpbMIB,
       "dImpbNotifications": dImpbNotifications,
       "dImpbViolationTrap": dImpbViolationTrap,
       "dImpbObjects": dImpbObjects,
       "dImpbNotifyInfo": dImpbNotifyInfo,
       "dImpbGlobalNotifyEnabled": dImpbGlobalNotifyEnabled,
       "dImpbViolationIpAddrType": dImpbViolationIpAddrType,
       "dImpbViolationIpAddress": dImpbViolationIpAddress,
       "dImpbIfConfigTable": dImpbIfConfigTable,
       "dImpbIfConfigEntry": dImpbIfConfigEntry,
       "dImpbIfBindMode": dImpbIfBindMode,
       "dImpbViolationLogTable": dImpbViolationLogTable,
       "dImpbViolationLogEntry": dImpbViolationLogEntry,
       "dImpbViolationVlan": dImpbViolationVlan,
       "dImpbViolationMacAddress": dImpbViolationMacAddress,
       "dImpbViolationAction": dImpbViolationAction,
       "dImpbClearObjects": dImpbClearObjects,
       "dImpbClearAllViolation": dImpbClearAllViolation,
       "dImpbClearViolationByIf": dImpbClearViolationByIf,
       "dImpbConformance": dImpbConformance,
       "dImpbMIBCompliances": dImpbMIBCompliances,
       "dImpbMIBCompliance": dImpbMIBCompliance,
       "dImpbMIBGroups": dImpbMIBGroups,
       "dImpbConfigGroup": dImpbConfigGroup,
       "dImpbClearViolationLogGroup": dImpbClearViolationLogGroup,
       "dImpbNotificationsGroup": dImpbNotificationsGroup}
)
