# SNMP MIB module (ARUBAWIRED-LOOPPROTECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-LOOPPROTECT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:11 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

arubaWiredLoopProtectMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    arubaWiredLoopProtectMIB.setRevisions(
        ("2017-11-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfigStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3))
    )



class VidList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )



class LoopProtectReceiverAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableTx", 1),
          ("noDisable", 2),
          ("disableTxRx", 3))
    )



# MIB Managed Objects in the order of their OIDs

_ArubaWiredLoopProtectObjects_ObjectIdentity = ObjectIdentity
arubaWiredLoopProtectObjects = _ArubaWiredLoopProtectObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1)
)
_ArubaWiredLoopProtect_ObjectIdentity = ObjectIdentity
arubaWiredLoopProtect = _ArubaWiredLoopProtect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5)
)
_ArubaWiredLoopProtectNotifications_ObjectIdentity = ObjectIdentity
arubaWiredLoopProtectNotifications = _ArubaWiredLoopProtectNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 0)
)
_ArubaWiredLoopProtectBase_ObjectIdentity = ObjectIdentity
arubaWiredLoopProtectBase = _ArubaWiredLoopProtectBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1)
)


class _ArubaWiredLoopProtectInterval_Type(Integer32):
    """Custom type arubaWiredLoopProtectInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ArubaWiredLoopProtectInterval_Type.__name__ = "Integer32"
_ArubaWiredLoopProtectInterval_Object = MibScalar
arubaWiredLoopProtectInterval = _ArubaWiredLoopProtectInterval_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 1),
    _ArubaWiredLoopProtectInterval_Type()
)
arubaWiredLoopProtectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectInterval.setStatus("current")
_ArubaWiredLoopProtectTrapLoopDetectEnable_Type = TruthValue
_ArubaWiredLoopProtectTrapLoopDetectEnable_Object = MibScalar
arubaWiredLoopProtectTrapLoopDetectEnable = _ArubaWiredLoopProtectTrapLoopDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 2),
    _ArubaWiredLoopProtectTrapLoopDetectEnable_Type()
)
arubaWiredLoopProtectTrapLoopDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectTrapLoopDetectEnable.setStatus("current")


class _ArubaWiredLoopProtectEnableTimer_Type(Integer32):
    """Custom type arubaWiredLoopProtectEnableTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArubaWiredLoopProtectEnableTimer_Type.__name__ = "Integer32"
_ArubaWiredLoopProtectEnableTimer_Object = MibScalar
arubaWiredLoopProtectEnableTimer = _ArubaWiredLoopProtectEnableTimer_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 3),
    _ArubaWiredLoopProtectEnableTimer_Type()
)
arubaWiredLoopProtectEnableTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectEnableTimer.setStatus("current")


class _ArubaWiredLoopProtectMode_Type(Integer32):
    """Custom type arubaWiredLoopProtectMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("vlan", 2))
    )


_ArubaWiredLoopProtectMode_Type.__name__ = "Integer32"
_ArubaWiredLoopProtectMode_Object = MibScalar
arubaWiredLoopProtectMode = _ArubaWiredLoopProtectMode_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 4),
    _ArubaWiredLoopProtectMode_Type()
)
arubaWiredLoopProtectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectMode.setStatus("current")
_ArubaWiredLoopProtectVIDList_Type = VidList
_ArubaWiredLoopProtectVIDList_Object = MibScalar
arubaWiredLoopProtectVIDList = _ArubaWiredLoopProtectVIDList_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 5),
    _ArubaWiredLoopProtectVIDList_Type()
)
arubaWiredLoopProtectVIDList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectVIDList.setStatus("current")
_ArubaWiredLoopProtectPort_ObjectIdentity = ObjectIdentity
arubaWiredLoopProtectPort = _ArubaWiredLoopProtectPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2)
)
_ArubaWiredLoopProtectPortTable_Object = MibTable
arubaWiredLoopProtectPortTable = _ArubaWiredLoopProtectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    arubaWiredLoopProtectPortTable.setStatus("current")
_ArubaWiredLoopProtectPortEntry_Object = MibTableRow
arubaWiredLoopProtectPortEntry = _ArubaWiredLoopProtectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1)
)
arubaWiredLoopProtectPortEntry.setIndexNames(
    (0, "ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortInterfaceIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredLoopProtectPortEntry.setStatus("current")
_ArubaWiredLoopProtectPortInterfaceIndex_Type = InterfaceIndex
_ArubaWiredLoopProtectPortInterfaceIndex_Object = MibTableColumn
arubaWiredLoopProtectPortInterfaceIndex = _ArubaWiredLoopProtectPortInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 1),
    _ArubaWiredLoopProtectPortInterfaceIndex_Type()
)
arubaWiredLoopProtectPortInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectPortInterfaceIndex.setStatus("current")
_ArubaWiredLoopProtectPortEnable_Type = TruthValue
_ArubaWiredLoopProtectPortEnable_Object = MibTableColumn
arubaWiredLoopProtectPortEnable = _ArubaWiredLoopProtectPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 2),
    _ArubaWiredLoopProtectPortEnable_Type()
)
arubaWiredLoopProtectPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectPortEnable.setStatus("current")
_ArubaWiredLoopProtectPortLoopDetected_Type = TruthValue
_ArubaWiredLoopProtectPortLoopDetected_Object = MibTableColumn
arubaWiredLoopProtectPortLoopDetected = _ArubaWiredLoopProtectPortLoopDetected_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 3),
    _ArubaWiredLoopProtectPortLoopDetected_Type()
)
arubaWiredLoopProtectPortLoopDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectPortLoopDetected.setStatus("current")
_ArubaWiredLoopProtectPortLastLoopTime_Type = TimeStamp
_ArubaWiredLoopProtectPortLastLoopTime_Object = MibTableColumn
arubaWiredLoopProtectPortLastLoopTime = _ArubaWiredLoopProtectPortLastLoopTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 4),
    _ArubaWiredLoopProtectPortLastLoopTime_Type()
)
arubaWiredLoopProtectPortLastLoopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectPortLastLoopTime.setStatus("current")
_ArubaWiredLoopProtectPortLoopCount_Type = Counter32
_ArubaWiredLoopProtectPortLoopCount_Object = MibTableColumn
arubaWiredLoopProtectPortLoopCount = _ArubaWiredLoopProtectPortLoopCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 5),
    _ArubaWiredLoopProtectPortLoopCount_Type()
)
arubaWiredLoopProtectPortLoopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectPortLoopCount.setStatus("current")
_ArubaWiredLoopProtectPortReceiverAction_Type = LoopProtectReceiverAction
_ArubaWiredLoopProtectPortReceiverAction_Object = MibTableColumn
arubaWiredLoopProtectPortReceiverAction = _ArubaWiredLoopProtectPortReceiverAction_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 6),
    _ArubaWiredLoopProtectPortReceiverAction_Type()
)
arubaWiredLoopProtectPortReceiverAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectPortReceiverAction.setStatus("current")


class _ArubaWiredLoopProtectLoopDetectedVlan_Type(Integer32):
    """Custom type arubaWiredLoopProtectLoopDetectedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ArubaWiredLoopProtectLoopDetectedVlan_Type.__name__ = "Integer32"
_ArubaWiredLoopProtectLoopDetectedVlan_Object = MibTableColumn
arubaWiredLoopProtectLoopDetectedVlan = _ArubaWiredLoopProtectLoopDetectedVlan_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 7),
    _ArubaWiredLoopProtectLoopDetectedVlan_Type()
)
arubaWiredLoopProtectLoopDetectedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectLoopDetectedVlan.setStatus("current")
_ArubaWiredLoopProtectPortVlanList_Type = VidList
_ArubaWiredLoopProtectPortVlanList_Object = MibTableColumn
arubaWiredLoopProtectPortVlanList = _ArubaWiredLoopProtectPortVlanList_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 8),
    _ArubaWiredLoopProtectPortVlanList_Type()
)
arubaWiredLoopProtectPortVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectPortVlanList.setStatus("current")
_ArubaWiredLoopProtectConformance_ObjectIdentity = ObjectIdentity
arubaWiredLoopProtectConformance = _ArubaWiredLoopProtectConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3)
)
_ArubaWiredLoopProtectGroups_ObjectIdentity = ObjectIdentity
arubaWiredLoopProtectGroups = _ArubaWiredLoopProtectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 1)
)
_ArubaWiredLoopProtectCompliances_ObjectIdentity = ObjectIdentity
arubaWiredLoopProtectCompliances = _ArubaWiredLoopProtectCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 2)
)

# Managed Objects groups

arubaWiredLoopProtectBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 1, 4)
)
arubaWiredLoopProtectBaseGroup.setObjects(
      *(("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectInterval"),
        ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectEnableTimer"),
        ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectTrapLoopDetectEnable"),
        ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortEnable"),
        ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLoopDetected"),
        ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLastLoopTime"),
        ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLoopCount"),
        ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortReceiverAction"))
)
if mibBuilder.loadTexts:
    arubaWiredLoopProtectBaseGroup.setStatus("current")

arubaWiredLoopProtectVLANGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 1, 10)
)
arubaWiredLoopProtectVLANGroup.setObjects(
      *(("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectMode"),
        ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectVIDList"),
        ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectLoopDetectedVlan"),
        ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortVlanList"))
)
if mibBuilder.loadTexts:
    arubaWiredLoopProtectVLANGroup.setStatus("current")


# Notification objects

arubaWiredLoopProtectLoopDetectedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 0, 1)
)
arubaWiredLoopProtectLoopDetectedNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLoopCount"),
        ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortReceiverAction"))
)
if mibBuilder.loadTexts:
    arubaWiredLoopProtectLoopDetectedNotification.setStatus(
        "current"
    )

arubaWiredLoopProtectVlanLoopDetectedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 0, 2)
)
arubaWiredLoopProtectVlanLoopDetectedNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLoopCount"),
        ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortReceiverAction"),
        ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectLoopDetectedVlan"))
)
if mibBuilder.loadTexts:
    arubaWiredLoopProtectVlanLoopDetectedNotification.setStatus(
        "current"
    )


# Notifications groups

arubaWiredLoopProtectNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 1, 11)
)
arubaWiredLoopProtectNotificationsGroup.setObjects(
      *(("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectLoopDetectedNotification"),
        ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectVlanLoopDetectedNotification"))
)
if mibBuilder.loadTexts:
    arubaWiredLoopProtectNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

arubaWiredLoopProtectCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 2, 5)
)
arubaWiredLoopProtectCompliance.setObjects(
      *(("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectBaseGroup"),
        ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectNotificationsGroup"),
        ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectVLANGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredLoopProtectCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-LOOPPROTECT-MIB",
    **{"ConfigStatus": ConfigStatus,
       "VidList": VidList,
       "LoopProtectReceiverAction": LoopProtectReceiverAction,
       "arubaWiredLoopProtectMIB": arubaWiredLoopProtectMIB,
       "arubaWiredLoopProtectObjects": arubaWiredLoopProtectObjects,
       "arubaWiredLoopProtect": arubaWiredLoopProtect,
       "arubaWiredLoopProtectNotifications": arubaWiredLoopProtectNotifications,
       "arubaWiredLoopProtectLoopDetectedNotification": arubaWiredLoopProtectLoopDetectedNotification,
       "arubaWiredLoopProtectVlanLoopDetectedNotification": arubaWiredLoopProtectVlanLoopDetectedNotification,
       "arubaWiredLoopProtectBase": arubaWiredLoopProtectBase,
       "arubaWiredLoopProtectInterval": arubaWiredLoopProtectInterval,
       "arubaWiredLoopProtectTrapLoopDetectEnable": arubaWiredLoopProtectTrapLoopDetectEnable,
       "arubaWiredLoopProtectEnableTimer": arubaWiredLoopProtectEnableTimer,
       "arubaWiredLoopProtectMode": arubaWiredLoopProtectMode,
       "arubaWiredLoopProtectVIDList": arubaWiredLoopProtectVIDList,
       "arubaWiredLoopProtectPort": arubaWiredLoopProtectPort,
       "arubaWiredLoopProtectPortTable": arubaWiredLoopProtectPortTable,
       "arubaWiredLoopProtectPortEntry": arubaWiredLoopProtectPortEntry,
       "arubaWiredLoopProtectPortInterfaceIndex": arubaWiredLoopProtectPortInterfaceIndex,
       "arubaWiredLoopProtectPortEnable": arubaWiredLoopProtectPortEnable,
       "arubaWiredLoopProtectPortLoopDetected": arubaWiredLoopProtectPortLoopDetected,
       "arubaWiredLoopProtectPortLastLoopTime": arubaWiredLoopProtectPortLastLoopTime,
       "arubaWiredLoopProtectPortLoopCount": arubaWiredLoopProtectPortLoopCount,
       "arubaWiredLoopProtectPortReceiverAction": arubaWiredLoopProtectPortReceiverAction,
       "arubaWiredLoopProtectLoopDetectedVlan": arubaWiredLoopProtectLoopDetectedVlan,
       "arubaWiredLoopProtectPortVlanList": arubaWiredLoopProtectPortVlanList,
       "arubaWiredLoopProtectConformance": arubaWiredLoopProtectConformance,
       "arubaWiredLoopProtectGroups": arubaWiredLoopProtectGroups,
       "arubaWiredLoopProtectBaseGroup": arubaWiredLoopProtectBaseGroup,
       "arubaWiredLoopProtectVLANGroup": arubaWiredLoopProtectVLANGroup,
       "arubaWiredLoopProtectNotificationsGroup": arubaWiredLoopProtectNotificationsGroup,
       "arubaWiredLoopProtectCompliances": arubaWiredLoopProtectCompliances,
       "arubaWiredLoopProtectCompliance": arubaWiredLoopProtectCompliance}
)
