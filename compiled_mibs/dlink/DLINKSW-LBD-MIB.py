# SNMP MIB module (DLINKSW-LBD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-LBD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:29 2025
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

(Dlink2kVlanList,) = mibBuilder.importSymbols(
    "DLINKSW-TC-MIB",
    "Dlink2kVlanList")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwLoopbackDetectMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 46)
)
if mibBuilder.loadTexts:
    dlinkSwLoopbackDetectMIB.setRevisions(
        ("2014-10-27 00:00",
         "2013-10-23 00:00",
         "2013-02-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DLbdNotifications_ObjectIdentity = ObjectIdentity
dLbdNotifications = _DLbdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 0)
)
_DLbdObjects_ObjectIdentity = ObjectIdentity
dLbdObjects = _DLbdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1)
)


class _DLbdCtrlInterval_Type(Integer32):
    """Custom type dLbdCtrlInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_DLbdCtrlInterval_Type.__name__ = "Integer32"
_DLbdCtrlInterval_Object = MibScalar
dLbdCtrlInterval = _DLbdCtrlInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1, 1),
    _DLbdCtrlInterval_Type()
)
dLbdCtrlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLbdCtrlInterval.setStatus("current")
if mibBuilder.loadTexts:
    dLbdCtrlInterval.setUnits("seconds")
_DLbdCtrlGlobalEnabled_Type = TruthValue
_DLbdCtrlGlobalEnabled_Object = MibScalar
dLbdCtrlGlobalEnabled = _DLbdCtrlGlobalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1, 2),
    _DLbdCtrlGlobalEnabled_Type()
)
dLbdCtrlGlobalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLbdCtrlGlobalEnabled.setStatus("current")


class _DLbdCtrlMode_Type(Integer32):
    """Custom type dLbdCtrlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portBased", 1),
          ("vlanBased", 2))
    )


_DLbdCtrlMode_Type.__name__ = "Integer32"
_DLbdCtrlMode_Object = MibScalar
dLbdCtrlMode = _DLbdCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1, 3),
    _DLbdCtrlMode_Type()
)
dLbdCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLbdCtrlMode.setStatus("current")
_DLbdIfCfgTable_Object = MibTable
dLbdIfCfgTable = _DLbdIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1, 4)
)
if mibBuilder.loadTexts:
    dLbdIfCfgTable.setStatus("current")
_DLbdIfCfgEntry_Object = MibTableRow
dLbdIfCfgEntry = _DLbdIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1, 4, 1)
)
dLbdIfCfgEntry.setIndexNames(
    (0, "DLINKSW-LBD-MIB", "dLbdIfCfgIndex"),
)
if mibBuilder.loadTexts:
    dLbdIfCfgEntry.setStatus("current")
_DLbdIfCfgIndex_Type = InterfaceIndex
_DLbdIfCfgIndex_Object = MibTableColumn
dLbdIfCfgIndex = _DLbdIfCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1, 4, 1, 1),
    _DLbdIfCfgIndex_Type()
)
dLbdIfCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dLbdIfCfgIndex.setStatus("current")
_DLbdIfCfgEnabled_Type = TruthValue
_DLbdIfCfgEnabled_Object = MibTableColumn
dLbdIfCfgEnabled = _DLbdIfCfgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1, 4, 1, 2),
    _DLbdIfCfgEnabled_Type()
)
dLbdIfCfgEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLbdIfCfgEnabled.setStatus("current")


class _DLbdIfLoopStatus_Type(Integer32):
    """Custom type dLbdIfLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loop", 2))
    )


_DLbdIfLoopStatus_Type.__name__ = "Integer32"
_DLbdIfLoopStatus_Object = MibTableColumn
dLbdIfLoopStatus = _DLbdIfLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1, 4, 1, 3),
    _DLbdIfLoopStatus_Type()
)
dLbdIfLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dLbdIfLoopStatus.setStatus("current")
_DLbdIfLoopVlans_Type = DisplayString
_DLbdIfLoopVlans_Object = MibTableColumn
dLbdIfLoopVlans = _DLbdIfLoopVlans_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1, 4, 1, 4),
    _DLbdIfLoopVlans_Type()
)
dLbdIfLoopVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dLbdIfLoopVlans.setStatus("current")
_DLbdVlanCtrlObjects_ObjectIdentity = ObjectIdentity
dLbdVlanCtrlObjects = _DLbdVlanCtrlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1, 5)
)
if mibBuilder.loadTexts:
    dLbdVlanCtrlObjects.setStatus("current")
_DLbdVlanCrlFirst2K_Type = Dlink2kVlanList
_DLbdVlanCrlFirst2K_Object = MibScalar
dLbdVlanCrlFirst2K = _DLbdVlanCrlFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1, 5, 1),
    _DLbdVlanCrlFirst2K_Type()
)
dLbdVlanCrlFirst2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLbdVlanCrlFirst2K.setStatus("current")
_DLbdVlanCrlSecond2K_Type = Dlink2kVlanList
_DLbdVlanCrlSecond2K_Object = MibScalar
dLbdVlanCrlSecond2K = _DLbdVlanCrlSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1, 5, 2),
    _DLbdVlanCrlSecond2K_Type()
)
dLbdVlanCrlSecond2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLbdVlanCrlSecond2K.setStatus("current")


class _DLbdActMode_Type(Integer32):
    """Custom type dLbdActMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 1),
          ("none", 2))
    )


_DLbdActMode_Type.__name__ = "Integer32"
_DLbdActMode_Object = MibScalar
dLbdActMode = _DLbdActMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1, 6),
    _DLbdActMode_Type()
)
dLbdActMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLbdActMode.setStatus("current")
_DLbdNotifyEnabled_Type = TruthValue
_DLbdNotifyEnabled_Object = MibScalar
dLbdNotifyEnabled = _DLbdNotifyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1, 7),
    _DLbdNotifyEnabled_Type()
)
dLbdNotifyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLbdNotifyEnabled.setStatus("current")
_DLbdNotifyInfo_ObjectIdentity = ObjectIdentity
dLbdNotifyInfo = _DLbdNotifyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1, 8)
)
if mibBuilder.loadTexts:
    dLbdNotifyInfo.setStatus("current")
_DLbdNotifyInfoIfIndex_Type = InterfaceIndex
_DLbdNotifyInfoIfIndex_Object = MibScalar
dLbdNotifyInfoIfIndex = _DLbdNotifyInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1, 8, 1),
    _DLbdNotifyInfoIfIndex_Type()
)
dLbdNotifyInfoIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dLbdNotifyInfoIfIndex.setStatus("current")
_DLbdNotifyInfoVlanId_Type = VlanId
_DLbdNotifyInfoVlanId_Object = MibScalar
dLbdNotifyInfoVlanId = _DLbdNotifyInfoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1, 8, 2),
    _DLbdNotifyInfoVlanId_Type()
)
dLbdNotifyInfoVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dLbdNotifyInfoVlanId.setStatus("current")


class _DLbdAddressType_Type(Integer32):
    """Custom type dLbdAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 1),
          ("broadcast", 2))
    )


_DLbdAddressType_Type.__name__ = "Integer32"
_DLbdAddressType_Object = MibScalar
dLbdAddressType = _DLbdAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 1, 9),
    _DLbdAddressType_Type()
)
dLbdAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLbdAddressType.setStatus("current")
_DLbdConformance_ObjectIdentity = ObjectIdentity
dLbdConformance = _DLbdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 2)
)
_DLbdMIBCompliances_ObjectIdentity = ObjectIdentity
dLbdMIBCompliances = _DLbdMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 2, 1)
)
_DLbdMIBGroups_ObjectIdentity = ObjectIdentity
dLbdMIBGroups = _DLbdMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 2, 2)
)

# Managed Objects groups

dLbdCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 2, 2, 1)
)
dLbdCfgGroup.setObjects(
      *(("DLINKSW-LBD-MIB", "dLbdCtrlInterval"),
        ("DLINKSW-LBD-MIB", "dLbdCtrlGlobalEnabled"),
        ("DLINKSW-LBD-MIB", "dLbdActMode"),
        ("DLINKSW-LBD-MIB", "dLbdNotifyEnabled"),
        ("DLINKSW-LBD-MIB", "dLbdNotifyInfoIfIndex"),
        ("DLINKSW-LBD-MIB", "dLbdNotifyInfoVlanId"),
        ("DLINKSW-LBD-MIB", "dLbdAddressType"))
)
if mibBuilder.loadTexts:
    dLbdCfgGroup.setStatus("current")

dLbdIfCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 2, 2, 2)
)
dLbdIfCfgGroup.setObjects(
      *(("DLINKSW-LBD-MIB", "dLbdIfCfgEnabled"),
        ("DLINKSW-LBD-MIB", "dLbdIfLoopStatus"),
        ("DLINKSW-LBD-MIB", "dLbdIfLoopVlans"))
)
if mibBuilder.loadTexts:
    dLbdIfCfgGroup.setStatus("current")

dLbdCtrlModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 2, 2, 3)
)
dLbdCtrlModeGroup.setObjects(
    ("DLINKSW-LBD-MIB", "dLbdCtrlMode")
)
if mibBuilder.loadTexts:
    dLbdCtrlModeGroup.setStatus("current")

dLbdVlanCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 2, 2, 4)
)
dLbdVlanCtrlGroup.setObjects(
      *(("DLINKSW-LBD-MIB", "dLbdVlanCrlFirst2K"),
        ("DLINKSW-LBD-MIB", "dLbdVlanCrlSecond2K"))
)
if mibBuilder.loadTexts:
    dLbdVlanCtrlGroup.setStatus("current")


# Notification objects

dLbdLoopOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 0, 1)
)
dLbdLoopOccurred.setObjects(
    ("DLINKSW-LBD-MIB", "dLbdNotifyInfoIfIndex")
)
if mibBuilder.loadTexts:
    dLbdLoopOccurred.setStatus(
        "current"
    )

dLbdLoopRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 0, 2)
)
dLbdLoopRestart.setObjects(
    ("DLINKSW-LBD-MIB", "dLbdNotifyInfoIfIndex")
)
if mibBuilder.loadTexts:
    dLbdLoopRestart.setStatus(
        "current"
    )

dLbdVlanLoopOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 0, 3)
)
dLbdVlanLoopOccurred.setObjects(
      *(("DLINKSW-LBD-MIB", "dLbdNotifyInfoIfIndex"),
        ("DLINKSW-LBD-MIB", "dLbdNotifyInfoVlanId"))
)
if mibBuilder.loadTexts:
    dLbdVlanLoopOccurred.setStatus(
        "current"
    )

dLbdVlanLoopRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 0, 4)
)
dLbdVlanLoopRestart.setObjects(
      *(("DLINKSW-LBD-MIB", "dLbdNotifyInfoIfIndex"),
        ("DLINKSW-LBD-MIB", "dLbdNotifyInfoVlanId"))
)
if mibBuilder.loadTexts:
    dLbdVlanLoopRestart.setStatus(
        "current"
    )


# Notifications groups

dLbdNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 2, 2, 5)
)
dLbdNotificationGroup.setObjects(
      *(("DLINKSW-LBD-MIB", "dLbdLoopOccurred"),
        ("DLINKSW-LBD-MIB", "dLbdLoopRestart"),
        ("DLINKSW-LBD-MIB", "dLbdVlanLoopOccurred"),
        ("DLINKSW-LBD-MIB", "dLbdVlanLoopRestart"))
)
if mibBuilder.loadTexts:
    dLbdNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dLbdMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 46, 2, 1, 1)
)
dLbdMIBCompliance.setObjects(
      *(("DLINKSW-LBD-MIB", "dLbdCfgGroup"),
        ("DLINKSW-LBD-MIB", "dLbdIfCfgGroup"),
        ("DLINKSW-LBD-MIB", "dLbdCtrlModeGroup"),
        ("DLINKSW-LBD-MIB", "dLbdVlanCtrlGroup"))
)
if mibBuilder.loadTexts:
    dLbdMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-LBD-MIB",
    **{"dlinkSwLoopbackDetectMIB": dlinkSwLoopbackDetectMIB,
       "dLbdNotifications": dLbdNotifications,
       "dLbdLoopOccurred": dLbdLoopOccurred,
       "dLbdLoopRestart": dLbdLoopRestart,
       "dLbdVlanLoopOccurred": dLbdVlanLoopOccurred,
       "dLbdVlanLoopRestart": dLbdVlanLoopRestart,
       "dLbdObjects": dLbdObjects,
       "dLbdCtrlInterval": dLbdCtrlInterval,
       "dLbdCtrlGlobalEnabled": dLbdCtrlGlobalEnabled,
       "dLbdCtrlMode": dLbdCtrlMode,
       "dLbdIfCfgTable": dLbdIfCfgTable,
       "dLbdIfCfgEntry": dLbdIfCfgEntry,
       "dLbdIfCfgIndex": dLbdIfCfgIndex,
       "dLbdIfCfgEnabled": dLbdIfCfgEnabled,
       "dLbdIfLoopStatus": dLbdIfLoopStatus,
       "dLbdIfLoopVlans": dLbdIfLoopVlans,
       "dLbdVlanCtrlObjects": dLbdVlanCtrlObjects,
       "dLbdVlanCrlFirst2K": dLbdVlanCrlFirst2K,
       "dLbdVlanCrlSecond2K": dLbdVlanCrlSecond2K,
       "dLbdActMode": dLbdActMode,
       "dLbdNotifyEnabled": dLbdNotifyEnabled,
       "dLbdNotifyInfo": dLbdNotifyInfo,
       "dLbdNotifyInfoIfIndex": dLbdNotifyInfoIfIndex,
       "dLbdNotifyInfoVlanId": dLbdNotifyInfoVlanId,
       "dLbdAddressType": dLbdAddressType,
       "dLbdConformance": dLbdConformance,
       "dLbdMIBCompliances": dLbdMIBCompliances,
       "dLbdMIBCompliance": dLbdMIBCompliance,
       "dLbdMIBGroups": dLbdMIBGroups,
       "dLbdCfgGroup": dLbdCfgGroup,
       "dLbdIfCfgGroup": dLbdIfCfgGroup,
       "dLbdCtrlModeGroup": dLbdCtrlModeGroup,
       "dLbdVlanCtrlGroup": dLbdVlanCtrlGroup,
       "dLbdNotificationGroup": dLbdNotificationGroup}
)
