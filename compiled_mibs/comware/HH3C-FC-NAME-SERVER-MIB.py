# SNMP MIB module (HH3C-FC-NAME-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-FC-NAME-SERVER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:31:30 2025
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

(Hh3cFcNameId,) = mibBuilder.importSymbols(
    "HH3C-FC-TC-MIB",
    "Hh3cFcNameId")

(hh3cSan,
 hh3cVsanIndex) = mibBuilder.importSymbols(
    "HH3C-VSAN-MIB",
    "hh3cSan",
    "hh3cVsanIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cFcNameServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 10)
)
if mibBuilder.loadTexts:
    hh3cFcNameServer.setRevisions(
        ("2014-03-03 10:18",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cFcNameServerMibObjects_ObjectIdentity = ObjectIdentity
hh3cFcNameServerMibObjects = _Hh3cFcNameServerMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 10, 1)
)
_Hh3cFcNsNotification_ObjectIdentity = ObjectIdentity
hh3cFcNsNotification = _Hh3cFcNsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 10, 1, 1)
)
_Hh3cFcNsNotificationPrefix_ObjectIdentity = ObjectIdentity
hh3cFcNsNotificationPrefix = _Hh3cFcNsNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 10, 1, 1, 0)
)
_Hh3cFcNsNotificationSwitch_ObjectIdentity = ObjectIdentity
hh3cFcNsNotificationSwitch = _Hh3cFcNsNotificationSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 10, 1, 1, 1)
)
_Hh3cFcNsPortLoginNotifyEnable_Type = TruthValue
_Hh3cFcNsPortLoginNotifyEnable_Object = MibScalar
hh3cFcNsPortLoginNotifyEnable = _Hh3cFcNsPortLoginNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 10, 1, 1, 1, 1),
    _Hh3cFcNsPortLoginNotifyEnable_Type()
)
hh3cFcNsPortLoginNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcNsPortLoginNotifyEnable.setStatus("current")
_Hh3cFcNsPortLogoutNotifyEnable_Type = TruthValue
_Hh3cFcNsPortLogoutNotifyEnable_Object = MibScalar
hh3cFcNsPortLogoutNotifyEnable = _Hh3cFcNsPortLogoutNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 10, 1, 1, 1, 2),
    _Hh3cFcNsPortLogoutNotifyEnable_Type()
)
hh3cFcNsPortLogoutNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcNsPortLogoutNotifyEnable.setStatus("current")
_Hh3cFcNsObjsForNotification_ObjectIdentity = ObjectIdentity
hh3cFcNsObjsForNotification = _Hh3cFcNsObjsForNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 10, 1, 1, 2)
)
_Hh3cFcNsLocalSwitchWWN_Type = Hh3cFcNameId
_Hh3cFcNsLocalSwitchWWN_Object = MibScalar
hh3cFcNsLocalSwitchWWN = _Hh3cFcNsLocalSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 10, 1, 1, 2, 1),
    _Hh3cFcNsLocalSwitchWWN_Type()
)
hh3cFcNsLocalSwitchWWN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cFcNsLocalSwitchWWN.setStatus("current")
_Hh3cFcNsFloginPortWWN_Type = Hh3cFcNameId
_Hh3cFcNsFloginPortWWN_Object = MibScalar
hh3cFcNsFloginPortWWN = _Hh3cFcNsFloginPortWWN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 10, 1, 1, 2, 2),
    _Hh3cFcNsFloginPortWWN_Type()
)
hh3cFcNsFloginPortWWN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cFcNsFloginPortWWN.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cFcNsPortLoginNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 10, 1, 1, 0, 1)
)
hh3cFcNsPortLoginNotify.setObjects(
      *(("HH3C-VSAN-MIB", "hh3cVsanIndex"),
        ("HH3C-FC-NAME-SERVER-MIB", "hh3cFcNsLocalSwitchWWN"),
        ("HH3C-FC-NAME-SERVER-MIB", "hh3cFcNsFloginPortWWN"))
)
if mibBuilder.loadTexts:
    hh3cFcNsPortLoginNotify.setStatus(
        "current"
    )

hh3cFcNsPortLogoutNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 10, 1, 1, 0, 2)
)
hh3cFcNsPortLogoutNotify.setObjects(
      *(("HH3C-VSAN-MIB", "hh3cVsanIndex"),
        ("HH3C-FC-NAME-SERVER-MIB", "hh3cFcNsLocalSwitchWWN"),
        ("HH3C-FC-NAME-SERVER-MIB", "hh3cFcNsFloginPortWWN"))
)
if mibBuilder.loadTexts:
    hh3cFcNsPortLogoutNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FC-NAME-SERVER-MIB",
    **{"hh3cFcNameServer": hh3cFcNameServer,
       "hh3cFcNameServerMibObjects": hh3cFcNameServerMibObjects,
       "hh3cFcNsNotification": hh3cFcNsNotification,
       "hh3cFcNsNotificationPrefix": hh3cFcNsNotificationPrefix,
       "hh3cFcNsPortLoginNotify": hh3cFcNsPortLoginNotify,
       "hh3cFcNsPortLogoutNotify": hh3cFcNsPortLogoutNotify,
       "hh3cFcNsNotificationSwitch": hh3cFcNsNotificationSwitch,
       "hh3cFcNsPortLoginNotifyEnable": hh3cFcNsPortLoginNotifyEnable,
       "hh3cFcNsPortLogoutNotifyEnable": hh3cFcNsPortLogoutNotifyEnable,
       "hh3cFcNsObjsForNotification": hh3cFcNsObjsForNotification,
       "hh3cFcNsLocalSwitchWWN": hh3cFcNsLocalSwitchWWN,
       "hh3cFcNsFloginPortWWN": hh3cFcNsFloginPortWWN}
)
