# SNMP MIB module (DLINKSW-ERROR-DISABLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-ERROR-DISABLE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:07 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwErrDisableMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 45)
)
if mibBuilder.loadTexts:
    dlinkSwErrDisableMIB.setRevisions(
        ("2013-05-02 00:00",
         "2013-07-08 00:00",
         "2014-04-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DErrDisReasonID(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("loopbackDetect", 1),
          ("l2ptGuard", 2),
          ("psecureViolation", 3),
          ("stormControl", 4),
          ("bpduProtect", 5),
          ("arpRateLimit", 6),
          ("dhcpRateLimit", 7),
          ("ddm", 8),
          ("scheduledShutdown", 9),
          ("scheduledHibernation", 10))
    )



# MIB Managed Objects in the order of their OIDs

_DErrDisableMIBNotifications_ObjectIdentity = ObjectIdentity
dErrDisableMIBNotifications = _DErrDisableMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 0)
)
_DErrDisableMIBObjects_ObjectIdentity = ObjectIdentity
dErrDisableMIBObjects = _DErrDisableMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1)
)
_DErrDisRecoveryTable_Object = MibTable
dErrDisRecoveryTable = _DErrDisRecoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1, 1)
)
if mibBuilder.loadTexts:
    dErrDisRecoveryTable.setStatus("current")
_DErrDisRecoveryEntry_Object = MibTableRow
dErrDisRecoveryEntry = _DErrDisRecoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1, 1, 1)
)
dErrDisRecoveryEntry.setIndexNames(
    (0, "DLINKSW-ERROR-DISABLE-MIB", "dErrDisRecoveryIndex"),
)
if mibBuilder.loadTexts:
    dErrDisRecoveryEntry.setStatus("current")
_DErrDisRecoveryIndex_Type = DErrDisReasonID
_DErrDisRecoveryIndex_Object = MibTableColumn
dErrDisRecoveryIndex = _DErrDisRecoveryIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1, 1, 1, 1),
    _DErrDisRecoveryIndex_Type()
)
dErrDisRecoveryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dErrDisRecoveryIndex.setStatus("current")


class _DErrDisRecoveryEnable_Type(TruthValue):
    """Custom type dErrDisRecoveryEnable based on TruthValue"""
    defaultValue = 2


_DErrDisRecoveryEnable_Type.__name__ = "TruthValue"
_DErrDisRecoveryEnable_Object = MibTableColumn
dErrDisRecoveryEnable = _DErrDisRecoveryEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1, 1, 1, 2),
    _DErrDisRecoveryEnable_Type()
)
dErrDisRecoveryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dErrDisRecoveryEnable.setStatus("current")


class _DErrDisRecoveryInterval_Type(Integer32):
    """Custom type dErrDisRecoveryInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_DErrDisRecoveryInterval_Type.__name__ = "Integer32"
_DErrDisRecoveryInterval_Object = MibTableColumn
dErrDisRecoveryInterval = _DErrDisRecoveryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1, 1, 1, 3),
    _DErrDisRecoveryInterval_Type()
)
dErrDisRecoveryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dErrDisRecoveryInterval.setStatus("current")
if mibBuilder.loadTexts:
    dErrDisRecoveryInterval.setUnits("seconds")
_DErrDisIfStatusTableNum_Type = Unsigned32
_DErrDisIfStatusTableNum_Object = MibScalar
dErrDisIfStatusTableNum = _DErrDisIfStatusTableNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1, 2),
    _DErrDisIfStatusTableNum_Type()
)
dErrDisIfStatusTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dErrDisIfStatusTableNum.setStatus("current")
_DErrDisIfStatusTable_Object = MibTable
dErrDisIfStatusTable = _DErrDisIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1, 3)
)
if mibBuilder.loadTexts:
    dErrDisIfStatusTable.setStatus("current")
_DErrDisIfStatusEntry_Object = MibTableRow
dErrDisIfStatusEntry = _DErrDisIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1, 3, 1)
)
dErrDisIfStatusEntry.setIndexNames(
    (0, "DLINKSW-ERROR-DISABLE-MIB", "dErrDisIfStatusIfIndex"),
    (0, "DLINKSW-ERROR-DISABLE-MIB", "dErrDisIfStatusVlanIndex"),
    (0, "DLINKSW-ERROR-DISABLE-MIB", "dErrDisIfStatusDisReasonIndex"),
)
if mibBuilder.loadTexts:
    dErrDisIfStatusEntry.setStatus("current")
_DErrDisIfStatusIfIndex_Type = InterfaceIndex
_DErrDisIfStatusIfIndex_Object = MibTableColumn
dErrDisIfStatusIfIndex = _DErrDisIfStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1, 3, 1, 1),
    _DErrDisIfStatusIfIndex_Type()
)
dErrDisIfStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dErrDisIfStatusIfIndex.setStatus("current")
_DErrDisIfStatusVlanIndex_Type = VlanIdOrNone
_DErrDisIfStatusVlanIndex_Object = MibTableColumn
dErrDisIfStatusVlanIndex = _DErrDisIfStatusVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1, 3, 1, 2),
    _DErrDisIfStatusVlanIndex_Type()
)
dErrDisIfStatusVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dErrDisIfStatusVlanIndex.setStatus("current")
_DErrDisIfStatusDisReasonIndex_Type = DErrDisReasonID
_DErrDisIfStatusDisReasonIndex_Object = MibTableColumn
dErrDisIfStatusDisReasonIndex = _DErrDisIfStatusDisReasonIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1, 3, 1, 3),
    _DErrDisIfStatusDisReasonIndex_Type()
)
dErrDisIfStatusDisReasonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dErrDisIfStatusDisReasonIndex.setStatus("current")
_DErrDisIfStatusTimeLeft_Type = Unsigned32
_DErrDisIfStatusTimeLeft_Object = MibTableColumn
dErrDisIfStatusTimeLeft = _DErrDisIfStatusTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1, 3, 1, 4),
    _DErrDisIfStatusTimeLeft_Type()
)
dErrDisIfStatusTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dErrDisIfStatusTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    dErrDisIfStatusTimeLeft.setUnits("seconds")


class _DErrDisNotificationEnable_Type(Bits):
    """Custom type dErrDisNotificationEnable based on Bits"""
    namedValues = NamedValues(
        *(("errDisableAsserted", 0),
          ("errDisableCleared", 1))
    )

_DErrDisNotificationEnable_Type.__name__ = "Bits"
_DErrDisNotificationEnable_Object = MibScalar
dErrDisNotificationEnable = _DErrDisNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1, 4),
    _DErrDisNotificationEnable_Type()
)
dErrDisNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dErrDisNotificationEnable.setStatus("current")


class _DErrDisNotifRate_Type(Unsigned32):
    """Custom type dErrDisNotifRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_DErrDisNotifRate_Type.__name__ = "Unsigned32"
_DErrDisNotifRate_Object = MibScalar
dErrDisNotifRate = _DErrDisNotifRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1, 5),
    _DErrDisNotifRate_Type()
)
dErrDisNotifRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dErrDisNotifRate.setStatus("current")
if mibBuilder.loadTexts:
    dErrDisNotifRate.setUnits("notifications per minute")
_DErrDisNotifyInfo_ObjectIdentity = ObjectIdentity
dErrDisNotifyInfo = _DErrDisNotifyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1, 6)
)
_DErrDisNotifyInfoPortIfIndex_Type = InterfaceIndex
_DErrDisNotifyInfoPortIfIndex_Object = MibScalar
dErrDisNotifyInfoPortIfIndex = _DErrDisNotifyInfoPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1, 6, 1),
    _DErrDisNotifyInfoPortIfIndex_Type()
)
dErrDisNotifyInfoPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dErrDisNotifyInfoPortIfIndex.setStatus("current")
_DErrDisNotifyInfoLoopDetectedVID_Type = VlanId
_DErrDisNotifyInfoLoopDetectedVID_Object = MibScalar
dErrDisNotifyInfoLoopDetectedVID = _DErrDisNotifyInfoLoopDetectedVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1, 6, 2),
    _DErrDisNotifyInfoLoopDetectedVID_Type()
)
dErrDisNotifyInfoLoopDetectedVID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dErrDisNotifyInfoLoopDetectedVID.setStatus("current")
_DErrDisNotifyInfoReasonID_Type = DErrDisReasonID
_DErrDisNotifyInfoReasonID_Object = MibScalar
dErrDisNotifyInfoReasonID = _DErrDisNotifyInfoReasonID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 1, 6, 3),
    _DErrDisNotifyInfoReasonID_Type()
)
dErrDisNotifyInfoReasonID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dErrDisNotifyInfoReasonID.setStatus("current")
_DErrDisableMIBConformance_ObjectIdentity = ObjectIdentity
dErrDisableMIBConformance = _DErrDisableMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 2)
)
_DErrDisMIBCompliances_ObjectIdentity = ObjectIdentity
dErrDisMIBCompliances = _DErrDisMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 2, 1)
)
_DErrDisMIBGroups_ObjectIdentity = ObjectIdentity
dErrDisMIBGroups = _DErrDisMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 2, 2)
)

# Managed Objects groups

dErrDisRecoveryCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 2, 2, 1)
)
dErrDisRecoveryCfgGroup.setObjects(
      *(("DLINKSW-ERROR-DISABLE-MIB", "dErrDisRecoveryEnable"),
        ("DLINKSW-ERROR-DISABLE-MIB", "dErrDisRecoveryInterval"))
)
if mibBuilder.loadTexts:
    dErrDisRecoveryCfgGroup.setStatus("current")

dErrDisIfStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 2, 2, 2)
)
dErrDisIfStatusGroup.setObjects(
      *(("DLINKSW-ERROR-DISABLE-MIB", "dErrDisIfStatusTableNum"),
        ("DLINKSW-ERROR-DISABLE-MIB", "dErrDisIfStatusTimeLeft"))
)
if mibBuilder.loadTexts:
    dErrDisIfStatusGroup.setStatus("current")

dErrDisNotifyCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 2, 2, 3)
)
dErrDisNotifyCfgGroup.setObjects(
      *(("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotificationEnable"),
        ("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifRate"),
        ("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifyInfoPortIfIndex"),
        ("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifyInfoReasonID"),
        ("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifyInfoLoopDetectedVID"))
)
if mibBuilder.loadTexts:
    dErrDisNotifyCfgGroup.setStatus("current")


# Notification objects

dErrDisNotifyPortDisabledAssert = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 0, 1)
)
dErrDisNotifyPortDisabledAssert.setObjects(
      *(("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifyInfoPortIfIndex"),
        ("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifyInfoReasonID"))
)
if mibBuilder.loadTexts:
    dErrDisNotifyPortDisabledAssert.setStatus(
        "current"
    )

dErrDisNotifyPortDisabledClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 0, 2)
)
dErrDisNotifyPortDisabledClear.setObjects(
      *(("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifyInfoPortIfIndex"),
        ("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifyInfoReasonID"))
)
if mibBuilder.loadTexts:
    dErrDisNotifyPortDisabledClear.setStatus(
        "current"
    )

dErrDisNotifyVlanDisabledAssert = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 0, 3)
)
dErrDisNotifyVlanDisabledAssert.setObjects(
      *(("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifyInfoPortIfIndex"),
        ("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifyInfoReasonID"),
        ("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifyInfoLoopDetectedVID"))
)
if mibBuilder.loadTexts:
    dErrDisNotifyVlanDisabledAssert.setStatus(
        "current"
    )

dErrDisNotifyVlanDisabledClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 0, 4)
)
dErrDisNotifyVlanDisabledClear.setObjects(
      *(("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifyInfoPortIfIndex"),
        ("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifyInfoReasonID"),
        ("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifyInfoLoopDetectedVID"))
)
if mibBuilder.loadTexts:
    dErrDisNotifyVlanDisabledClear.setStatus(
        "current"
    )


# Notifications groups

dErrDisNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 2, 2, 4)
)
dErrDisNotificationGroup.setObjects(
      *(("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifyPortDisabledAssert"),
        ("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifyPortDisabledClear"),
        ("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifyVlanDisabledAssert"),
        ("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifyVlanDisabledClear"))
)
if mibBuilder.loadTexts:
    dErrDisNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dErrDisMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 45, 2, 1, 1)
)
dErrDisMIBCompliance.setObjects(
      *(("DLINKSW-ERROR-DISABLE-MIB", "dErrDisRecoveryCfgGroup"),
        ("DLINKSW-ERROR-DISABLE-MIB", "dErrDisIfStatusGroup"),
        ("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotifyCfgGroup"),
        ("DLINKSW-ERROR-DISABLE-MIB", "dErrDisNotificationGroup"))
)
if mibBuilder.loadTexts:
    dErrDisMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-ERROR-DISABLE-MIB",
    **{"DErrDisReasonID": DErrDisReasonID,
       "dlinkSwErrDisableMIB": dlinkSwErrDisableMIB,
       "dErrDisableMIBNotifications": dErrDisableMIBNotifications,
       "dErrDisNotifyPortDisabledAssert": dErrDisNotifyPortDisabledAssert,
       "dErrDisNotifyPortDisabledClear": dErrDisNotifyPortDisabledClear,
       "dErrDisNotifyVlanDisabledAssert": dErrDisNotifyVlanDisabledAssert,
       "dErrDisNotifyVlanDisabledClear": dErrDisNotifyVlanDisabledClear,
       "dErrDisableMIBObjects": dErrDisableMIBObjects,
       "dErrDisRecoveryTable": dErrDisRecoveryTable,
       "dErrDisRecoveryEntry": dErrDisRecoveryEntry,
       "dErrDisRecoveryIndex": dErrDisRecoveryIndex,
       "dErrDisRecoveryEnable": dErrDisRecoveryEnable,
       "dErrDisRecoveryInterval": dErrDisRecoveryInterval,
       "dErrDisIfStatusTableNum": dErrDisIfStatusTableNum,
       "dErrDisIfStatusTable": dErrDisIfStatusTable,
       "dErrDisIfStatusEntry": dErrDisIfStatusEntry,
       "dErrDisIfStatusIfIndex": dErrDisIfStatusIfIndex,
       "dErrDisIfStatusVlanIndex": dErrDisIfStatusVlanIndex,
       "dErrDisIfStatusDisReasonIndex": dErrDisIfStatusDisReasonIndex,
       "dErrDisIfStatusTimeLeft": dErrDisIfStatusTimeLeft,
       "dErrDisNotificationEnable": dErrDisNotificationEnable,
       "dErrDisNotifRate": dErrDisNotifRate,
       "dErrDisNotifyInfo": dErrDisNotifyInfo,
       "dErrDisNotifyInfoPortIfIndex": dErrDisNotifyInfoPortIfIndex,
       "dErrDisNotifyInfoLoopDetectedVID": dErrDisNotifyInfoLoopDetectedVID,
       "dErrDisNotifyInfoReasonID": dErrDisNotifyInfoReasonID,
       "dErrDisableMIBConformance": dErrDisableMIBConformance,
       "dErrDisMIBCompliances": dErrDisMIBCompliances,
       "dErrDisMIBCompliance": dErrDisMIBCompliance,
       "dErrDisMIBGroups": dErrDisMIBGroups,
       "dErrDisRecoveryCfgGroup": dErrDisRecoveryCfgGroup,
       "dErrDisIfStatusGroup": dErrDisIfStatusGroup,
       "dErrDisNotifyCfgGroup": dErrDisNotifyCfgGroup,
       "dErrDisNotificationGroup": dErrDisNotificationGroup}
)
