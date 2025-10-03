# SNMP MIB module (DLINKSW-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-STACK-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:52 2025
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

dlinkSwStackMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 9)
)
if mibBuilder.loadTexts:
    dlinkSwStackMIB.setRevisions(
        ("2016-03-09 00:00",
         "2013-03-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DStackMIBNotifications_ObjectIdentity = ObjectIdentity
dStackMIBNotifications = _DStackMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 0)
)
_DStackMIBObjects_ObjectIdentity = ObjectIdentity
dStackMIBObjects = _DStackMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1)
)
_DStackMgmt_ObjectIdentity = ObjectIdentity
dStackMgmt = _DStackMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1)
)


class _DStackTopology_Type(Integer32):
    """Custom type dStackTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("standAlone", 1),
          ("duplexChain", 2),
          ("duplexRing", 3))
    )


_DStackTopology_Type.__name__ = "Integer32"
_DStackTopology_Object = MibScalar
dStackTopology = _DStackTopology_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 1),
    _DStackTopology_Type()
)
dStackTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStackTopology.setStatus("current")


class _DStackMyBoxId_Type(Integer32):
    """Custom type dStackMyBoxId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DStackMyBoxId_Type.__name__ = "Integer32"
_DStackMyBoxId_Object = MibScalar
dStackMyBoxId = _DStackMyBoxId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 2),
    _DStackMyBoxId_Type()
)
dStackMyBoxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStackMyBoxId.setStatus("current")


class _DStackNumOfDevices_Type(Integer32):
    """Custom type dStackNumOfDevices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DStackNumOfDevices_Type.__name__ = "Integer32"
_DStackNumOfDevices_Object = MibScalar
dStackNumOfDevices = _DStackNumOfDevices_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 3),
    _DStackNumOfDevices_Type()
)
dStackNumOfDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStackNumOfDevices.setStatus("current")
_DStackAdminEnabled_Type = TruthValue
_DStackAdminEnabled_Object = MibScalar
dStackAdminEnabled = _DStackAdminEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 4),
    _DStackAdminEnabled_Type()
)
dStackAdminEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dStackAdminEnabled.setStatus("current")


class _DStackPreempt_Type(TruthValue):
    """Custom type dStackPreempt based on TruthValue"""
    defaultValue = 1


_DStackPreempt_Type.__name__ = "TruthValue"
_DStackPreempt_Object = MibScalar
dStackPreempt = _DStackPreempt_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 5),
    _DStackPreempt_Type()
)
dStackPreempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dStackPreempt.setStatus("current")


class _DStackTrapStateEnabled_Type(TruthValue):
    """Custom type dStackTrapStateEnabled based on TruthValue"""
    defaultValue = 2


_DStackTrapStateEnabled_Type.__name__ = "TruthValue"
_DStackTrapStateEnabled_Object = MibScalar
dStackTrapStateEnabled = _DStackTrapStateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 6),
    _DStackTrapStateEnabled_Type()
)
dStackTrapStateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dStackTrapStateEnabled.setStatus("current")


class _DStackBandwidth_Type(Integer32):
    """Custom type dStackBandwidth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twoPorts", 1),
          ("fourPorts", 2))
    )


_DStackBandwidth_Type.__name__ = "Integer32"
_DStackBandwidth_Object = MibScalar
dStackBandwidth = _DStackBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 7),
    _DStackBandwidth_Type()
)
dStackBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dStackBandwidth.setStatus("current")
_DStackUnitInfoTable_Object = MibTable
dStackUnitInfoTable = _DStackUnitInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 8)
)
if mibBuilder.loadTexts:
    dStackUnitInfoTable.setStatus("current")
_DStackUnitInfoEntry_Object = MibTableRow
dStackUnitInfoEntry = _DStackUnitInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 8, 1)
)
dStackUnitInfoEntry.setIndexNames(
    (0, "DLINKSW-STACK-MIB", "dStackInfoBoxId"),
)
if mibBuilder.loadTexts:
    dStackUnitInfoEntry.setStatus("current")


class _DStackInfoBoxId_Type(Integer32):
    """Custom type dStackInfoBoxId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DStackInfoBoxId_Type.__name__ = "Integer32"
_DStackInfoBoxId_Object = MibTableColumn
dStackInfoBoxId = _DStackInfoBoxId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 8, 1, 1),
    _DStackInfoBoxId_Type()
)
dStackInfoBoxId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dStackInfoBoxId.setStatus("current")
_DStackInfoExist_Type = TruthValue
_DStackInfoExist_Object = MibTableColumn
dStackInfoExist = _DStackInfoExist_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 8, 1, 2),
    _DStackInfoExist_Type()
)
dStackInfoExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStackInfoExist.setStatus("current")


class _DStackInfoRole_Type(Integer32):
    """Custom type dStackInfoRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("standAlone", 3),
          ("master", 4),
          ("slave", 5),
          ("backupmaster", 6))
    )


_DStackInfoRole_Type.__name__ = "Integer32"
_DStackInfoRole_Object = MibTableColumn
dStackInfoRole = _DStackInfoRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 8, 1, 3),
    _DStackInfoRole_Type()
)
dStackInfoRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStackInfoRole.setStatus("current")


class _DStackInfoUserSetBoxId_Type(Integer32):
    """Custom type dStackInfoUserSetBoxId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DStackInfoUserSetBoxId_Type.__name__ = "Integer32"
_DStackInfoUserSetBoxId_Object = MibTableColumn
dStackInfoUserSetBoxId = _DStackInfoUserSetBoxId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 8, 1, 4),
    _DStackInfoUserSetBoxId_Type()
)
dStackInfoUserSetBoxId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dStackInfoUserSetBoxId.setStatus("current")


class _DStackInfoModuleName_Type(DisplayString):
    """Custom type dStackInfoModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DStackInfoModuleName_Type.__name__ = "DisplayString"
_DStackInfoModuleName_Object = MibTableColumn
dStackInfoModuleName = _DStackInfoModuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 8, 1, 5),
    _DStackInfoModuleName_Type()
)
dStackInfoModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStackInfoModuleName.setStatus("current")


class _DStackInfoPriority_Type(Integer32):
    """Custom type dStackInfoPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DStackInfoPriority_Type.__name__ = "Integer32"
_DStackInfoPriority_Object = MibTableColumn
dStackInfoPriority = _DStackInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 8, 1, 6),
    _DStackInfoPriority_Type()
)
dStackInfoPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dStackInfoPriority.setStatus("current")
_DStackInfoMacAddr_Type = MacAddress
_DStackInfoMacAddr_Object = MibTableColumn
dStackInfoMacAddr = _DStackInfoMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 8, 1, 7),
    _DStackInfoMacAddr_Type()
)
dStackInfoMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStackInfoMacAddr.setStatus("current")


class _DStackInfoPromVersion_Type(DisplayString):
    """Custom type dStackInfoPromVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DStackInfoPromVersion_Type.__name__ = "DisplayString"
_DStackInfoPromVersion_Object = MibTableColumn
dStackInfoPromVersion = _DStackInfoPromVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 8, 1, 8),
    _DStackInfoPromVersion_Type()
)
dStackInfoPromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStackInfoPromVersion.setStatus("current")


class _DStackInfoFirmwareVer_Type(DisplayString):
    """Custom type dStackInfoFirmwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DStackInfoFirmwareVer_Type.__name__ = "DisplayString"
_DStackInfoFirmwareVer_Object = MibTableColumn
dStackInfoFirmwareVer = _DStackInfoFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 8, 1, 9),
    _DStackInfoFirmwareVer_Type()
)
dStackInfoFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStackInfoFirmwareVer.setStatus("current")


class _DStackInfoHardwareVer_Type(DisplayString):
    """Custom type dStackInfoHardwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DStackInfoHardwareVer_Type.__name__ = "DisplayString"
_DStackInfoHardwareVer_Object = MibTableColumn
dStackInfoHardwareVer = _DStackInfoHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 8, 1, 10),
    _DStackInfoHardwareVer_Type()
)
dStackInfoHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStackInfoHardwareVer.setStatus("current")


class _DStackInfoAdminBandwidth_Type(Integer32):
    """Custom type dStackInfoAdminBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twoPorts", 1),
          ("fourPorts", 2))
    )


_DStackInfoAdminBandwidth_Type.__name__ = "Integer32"
_DStackInfoAdminBandwidth_Object = MibTableColumn
dStackInfoAdminBandwidth = _DStackInfoAdminBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 8, 1, 11),
    _DStackInfoAdminBandwidth_Type()
)
dStackInfoAdminBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStackInfoAdminBandwidth.setStatus("current")


class _DStackInfoSIO1ActiveBandwidth_Type(Integer32):
    """Custom type dStackInfoSIO1ActiveBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onePort", 1),
          ("twoPorts", 2),
          ("linkDown", 3))
    )


_DStackInfoSIO1ActiveBandwidth_Type.__name__ = "Integer32"
_DStackInfoSIO1ActiveBandwidth_Object = MibTableColumn
dStackInfoSIO1ActiveBandwidth = _DStackInfoSIO1ActiveBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 8, 1, 12),
    _DStackInfoSIO1ActiveBandwidth_Type()
)
dStackInfoSIO1ActiveBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStackInfoSIO1ActiveBandwidth.setStatus("current")


class _DStackInfoSIO2ActiveBandwidth_Type(Integer32):
    """Custom type dStackInfoSIO2ActiveBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onePort", 1),
          ("twoPorts", 2),
          ("linkDown", 3))
    )


_DStackInfoSIO2ActiveBandwidth_Type.__name__ = "Integer32"
_DStackInfoSIO2ActiveBandwidth_Object = MibTableColumn
dStackInfoSIO2ActiveBandwidth = _DStackInfoSIO2ActiveBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 8, 1, 13),
    _DStackInfoSIO2ActiveBandwidth_Type()
)
dStackInfoSIO2ActiveBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStackInfoSIO2ActiveBandwidth.setStatus("current")


class _DStackInfoStartPort_Type(Integer32):
    """Custom type dStackInfoStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DStackInfoStartPort_Type.__name__ = "Integer32"
_DStackInfoStartPort_Object = MibTableColumn
dStackInfoStartPort = _DStackInfoStartPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 8, 1, 14),
    _DStackInfoStartPort_Type()
)
dStackInfoStartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStackInfoStartPort.setStatus("current")


class _DStackInfoPortRange_Type(Integer32):
    """Custom type dStackInfoPortRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DStackInfoPortRange_Type.__name__ = "Integer32"
_DStackInfoPortRange_Object = MibTableColumn
dStackInfoPortRange = _DStackInfoPortRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 1, 8, 1, 15),
    _DStackInfoPortRange_Type()
)
dStackInfoPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStackInfoPortRange.setStatus("current")
_DStackNotificationInfo_ObjectIdentity = ObjectIdentity
dStackNotificationInfo = _DStackNotificationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 2)
)


class _DStackNotifyInfoBoxId_Type(Integer32):
    """Custom type dStackNotifyInfoBoxId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DStackNotifyInfoBoxId_Type.__name__ = "Integer32"
_DStackNotifyInfoBoxId_Object = MibScalar
dStackNotifyInfoBoxId = _DStackNotifyInfoBoxId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 2, 1),
    _DStackNotifyInfoBoxId_Type()
)
dStackNotifyInfoBoxId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dStackNotifyInfoBoxId.setStatus("current")


class _DStackNotifyInfoTopologyType_Type(Integer32):
    """Custom type dStackNotifyInfoTopologyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chain", 1),
          ("ring", 2))
    )


_DStackNotifyInfoTopologyType_Type.__name__ = "Integer32"
_DStackNotifyInfoTopologyType_Object = MibScalar
dStackNotifyInfoTopologyType = _DStackNotifyInfoTopologyType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 2, 2),
    _DStackNotifyInfoTopologyType_Type()
)
dStackNotifyInfoTopologyType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dStackNotifyInfoTopologyType.setStatus("current")


class _DStackNotifyInfoRoleChangeType_Type(Integer32):
    """Custom type dStackNotifyInfoRoleChangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backupToMaster", 1),
          ("slaveToMaster", 2))
    )


_DStackNotifyInfoRoleChangeType_Type.__name__ = "Integer32"
_DStackNotifyInfoRoleChangeType_Object = MibScalar
dStackNotifyInfoRoleChangeType = _DStackNotifyInfoRoleChangeType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 1, 2, 3),
    _DStackNotifyInfoRoleChangeType_Type()
)
dStackNotifyInfoRoleChangeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dStackNotifyInfoRoleChangeType.setStatus("current")
_DStackMIBConformance_ObjectIdentity = ObjectIdentity
dStackMIBConformance = _DStackMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 2)
)
_DStackMIBCompliances_ObjectIdentity = ObjectIdentity
dStackMIBCompliances = _DStackMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 2, 1)
)
_DStackMIBGroups_ObjectIdentity = ObjectIdentity
dStackMIBGroups = _DStackMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 2, 2)
)

# Managed Objects groups

dStackBasicMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 2, 2, 1)
)
dStackBasicMgmtGroup.setObjects(
      *(("DLINKSW-STACK-MIB", "dStackTopology"),
        ("DLINKSW-STACK-MIB", "dStackMyBoxId"),
        ("DLINKSW-STACK-MIB", "dStackNumOfDevices"),
        ("DLINKSW-STACK-MIB", "dStackAdminEnabled"),
        ("DLINKSW-STACK-MIB", "dStackPreempt"),
        ("DLINKSW-STACK-MIB", "dStackTrapStateEnabled"),
        ("DLINKSW-STACK-MIB", "dStackInfoExist"),
        ("DLINKSW-STACK-MIB", "dStackInfoRole"),
        ("DLINKSW-STACK-MIB", "dStackInfoUserSetBoxId"),
        ("DLINKSW-STACK-MIB", "dStackInfoModuleName"),
        ("DLINKSW-STACK-MIB", "dStackInfoPriority"),
        ("DLINKSW-STACK-MIB", "dStackInfoMacAddr"),
        ("DLINKSW-STACK-MIB", "dStackInfoPromVersion"),
        ("DLINKSW-STACK-MIB", "dStackInfoFirmwareVer"),
        ("DLINKSW-STACK-MIB", "dStackInfoHardwareVer"),
        ("DLINKSW-STACK-MIB", "dStackNotifyInfoBoxId"),
        ("DLINKSW-STACK-MIB", "dStackNotifyInfoTopologyType"),
        ("DLINKSW-STACK-MIB", "dStackNotifyInfoRoleChangeType"))
)
if mibBuilder.loadTexts:
    dStackBasicMgmtGroup.setStatus("current")

dStackBandwidthMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 2, 2, 2)
)
dStackBandwidthMgmtGroup.setObjects(
      *(("DLINKSW-STACK-MIB", "dStackBandwidth"),
        ("DLINKSW-STACK-MIB", "dStackInfoAdminBandwidth"),
        ("DLINKSW-STACK-MIB", "dStackInfoSIO1ActiveBandwidth"),
        ("DLINKSW-STACK-MIB", "dStackInfoSIO2ActiveBandwidth"))
)
if mibBuilder.loadTexts:
    dStackBandwidthMgmtGroup.setStatus("current")


# Notification objects

dStackInsertNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 0, 1)
)
dStackInsertNotification.setObjects(
      *(("DLINKSW-STACK-MIB", "dStackNotifyInfoBoxId"),
        ("DLINKSW-STACK-MIB", "dStackInfoMacAddr"))
)
if mibBuilder.loadTexts:
    dStackInsertNotification.setStatus(
        "current"
    )

dStackRemoveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 0, 2)
)
dStackRemoveNotification.setObjects(
      *(("DLINKSW-STACK-MIB", "dStackNotifyInfoBoxId"),
        ("DLINKSW-STACK-MIB", "dStackInfoMacAddr"))
)
if mibBuilder.loadTexts:
    dStackRemoveNotification.setStatus(
        "current"
    )

dStackFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 0, 3)
)
dStackFailureNotification.setObjects(
    ("DLINKSW-STACK-MIB", "dStackNotifyInfoBoxId")
)
if mibBuilder.loadTexts:
    dStackFailureNotification.setStatus(
        "current"
    )

dStackTPChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 0, 4)
)
dStackTPChangeNotification.setObjects(
      *(("DLINKSW-STACK-MIB", "dStackNotifyInfoTopologyType"),
        ("DLINKSW-STACK-MIB", "dStackNotifyInfoBoxId"),
        ("DLINKSW-STACK-MIB", "dStackInfoMacAddr"))
)
if mibBuilder.loadTexts:
    dStackTPChangeNotification.setStatus(
        "current"
    )

dStackRoleChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 0, 5)
)
dStackRoleChangeNotification.setObjects(
      *(("DLINKSW-STACK-MIB", "dStackNotifyInfoRoleChangeType"),
        ("DLINKSW-STACK-MIB", "dStackNotifyInfoBoxId"))
)
if mibBuilder.loadTexts:
    dStackRoleChangeNotification.setStatus(
        "current"
    )


# Notifications groups

dStackNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 2, 2, 3)
)
dStackNotifGroup.setObjects(
      *(("DLINKSW-STACK-MIB", "dStackInsertNotification"),
        ("DLINKSW-STACK-MIB", "dStackRemoveNotification"),
        ("DLINKSW-STACK-MIB", "dStackFailureNotification"),
        ("DLINKSW-STACK-MIB", "dStackTPChangeNotification"),
        ("DLINKSW-STACK-MIB", "dStackRoleChangeNotification"))
)
if mibBuilder.loadTexts:
    dStackNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dStackCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 9, 2, 1, 1)
)
dStackCompliance.setObjects(
      *(("DLINKSW-STACK-MIB", "dStackBasicMgmtGroup"),
        ("DLINKSW-STACK-MIB", "dStackNotifGroup"),
        ("DLINKSW-STACK-MIB", "dStackBandwidthMgmtGroup"))
)
if mibBuilder.loadTexts:
    dStackCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-STACK-MIB",
    **{"dlinkSwStackMIB": dlinkSwStackMIB,
       "dStackMIBNotifications": dStackMIBNotifications,
       "dStackInsertNotification": dStackInsertNotification,
       "dStackRemoveNotification": dStackRemoveNotification,
       "dStackFailureNotification": dStackFailureNotification,
       "dStackTPChangeNotification": dStackTPChangeNotification,
       "dStackRoleChangeNotification": dStackRoleChangeNotification,
       "dStackMIBObjects": dStackMIBObjects,
       "dStackMgmt": dStackMgmt,
       "dStackTopology": dStackTopology,
       "dStackMyBoxId": dStackMyBoxId,
       "dStackNumOfDevices": dStackNumOfDevices,
       "dStackAdminEnabled": dStackAdminEnabled,
       "dStackPreempt": dStackPreempt,
       "dStackTrapStateEnabled": dStackTrapStateEnabled,
       "dStackBandwidth": dStackBandwidth,
       "dStackUnitInfoTable": dStackUnitInfoTable,
       "dStackUnitInfoEntry": dStackUnitInfoEntry,
       "dStackInfoBoxId": dStackInfoBoxId,
       "dStackInfoExist": dStackInfoExist,
       "dStackInfoRole": dStackInfoRole,
       "dStackInfoUserSetBoxId": dStackInfoUserSetBoxId,
       "dStackInfoModuleName": dStackInfoModuleName,
       "dStackInfoPriority": dStackInfoPriority,
       "dStackInfoMacAddr": dStackInfoMacAddr,
       "dStackInfoPromVersion": dStackInfoPromVersion,
       "dStackInfoFirmwareVer": dStackInfoFirmwareVer,
       "dStackInfoHardwareVer": dStackInfoHardwareVer,
       "dStackInfoAdminBandwidth": dStackInfoAdminBandwidth,
       "dStackInfoSIO1ActiveBandwidth": dStackInfoSIO1ActiveBandwidth,
       "dStackInfoSIO2ActiveBandwidth": dStackInfoSIO2ActiveBandwidth,
       "dStackInfoStartPort": dStackInfoStartPort,
       "dStackInfoPortRange": dStackInfoPortRange,
       "dStackNotificationInfo": dStackNotificationInfo,
       "dStackNotifyInfoBoxId": dStackNotifyInfoBoxId,
       "dStackNotifyInfoTopologyType": dStackNotifyInfoTopologyType,
       "dStackNotifyInfoRoleChangeType": dStackNotifyInfoRoleChangeType,
       "dStackMIBConformance": dStackMIBConformance,
       "dStackMIBCompliances": dStackMIBCompliances,
       "dStackCompliance": dStackCompliance,
       "dStackMIBGroups": dStackMIBGroups,
       "dStackBasicMgmtGroup": dStackBasicMgmtGroup,
       "dStackBandwidthMgmtGroup": dStackBandwidthMgmtGroup,
       "dStackNotifGroup": dStackNotifGroup}
)
