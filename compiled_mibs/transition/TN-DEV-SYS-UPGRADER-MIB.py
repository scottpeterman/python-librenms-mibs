# SNMP MIB module (TN-DEV-SYS-UPGRADER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-DEV-SYS-UPGRADER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:05 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tnDevMgmt,) = mibBuilder.importSymbols(
    "TN-MGMT-MIB",
    "tnDevMgmt")


# MODULE-IDENTITY

tnDevSysUpgraderMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30)
)
if mibBuilder.loadTexts:
    tnDevSysUpgraderMIB.setRevisions(
        ("2012-06-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnDevSysUpgraderNotifications_ObjectIdentity = ObjectIdentity
tnDevSysUpgraderNotifications = _TnDevSysUpgraderNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 0)
)
_TnDevSysUpgrader_ObjectIdentity = ObjectIdentity
tnDevSysUpgrader = _TnDevSysUpgrader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1)
)
_TnUpgradeOpTable_Object = MibTable
tnUpgradeOpTable = _TnUpgradeOpTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 1)
)
if mibBuilder.loadTexts:
    tnUpgradeOpTable.setStatus("current")
_TnUpgradeOpEntry_Object = MibTableRow
tnUpgradeOpEntry = _TnUpgradeOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 1, 1)
)
tnUpgradeOpEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnUpgradeOpEntry.setStatus("current")


class _UpgradeOpCommand_Type(Integer32):
    """Custom type upgradeOpCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("upgrade", 2),
          ("done", 3))
    )


_UpgradeOpCommand_Type.__name__ = "Integer32"
_UpgradeOpCommand_Object = MibTableColumn
upgradeOpCommand = _UpgradeOpCommand_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 1, 1, 1),
    _UpgradeOpCommand_Type()
)
upgradeOpCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeOpCommand.setStatus("current")


class _UpgradeOpStatus_Type(Integer32):
    """Custom type upgradeOpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("inProgress", 2))
    )


_UpgradeOpStatus_Type.__name__ = "Integer32"
_UpgradeOpStatus_Object = MibTableColumn
upgradeOpStatus = _UpgradeOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 1, 1, 2),
    _UpgradeOpStatus_Type()
)
upgradeOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeOpStatus.setStatus("current")
_TnUpgradeResultTable_Object = MibTable
tnUpgradeResultTable = _TnUpgradeResultTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 2)
)
if mibBuilder.loadTexts:
    tnUpgradeResultTable.setStatus("current")
_TnUpgradeResultEntry_Object = MibTableRow
tnUpgradeResultEntry = _TnUpgradeResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 2, 1)
)
tnUpgradeResultEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TN-DEV-SYS-UPGRADER-MIB", "upgradeResultIndex"),
)
if mibBuilder.loadTexts:
    tnUpgradeResultEntry.setStatus("current")
_UpgradeResultIndex_Type = Integer32
_UpgradeResultIndex_Object = MibTableColumn
upgradeResultIndex = _UpgradeResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 2, 1, 1),
    _UpgradeResultIndex_Type()
)
upgradeResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upgradeResultIndex.setStatus("current")
_UpgradeResultModule_Type = Integer32
_UpgradeResultModule_Object = MibTableColumn
upgradeResultModule = _UpgradeResultModule_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 2, 1, 2),
    _UpgradeResultModule_Type()
)
upgradeResultModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeResultModule.setStatus("current")


class _UpgradeResultStatus_Type(Integer32):
    """Custom type upgradeResultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("inProgress", 2),
          ("failure", 3),
          ("success", 4))
    )


_UpgradeResultStatus_Type.__name__ = "Integer32"
_UpgradeResultStatus_Object = MibTableColumn
upgradeResultStatus = _UpgradeResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 2, 1, 3),
    _UpgradeResultStatus_Type()
)
upgradeResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeResultStatus.setStatus("current")


class _UpgradeResultReason_Type(DisplayString):
    """Custom type upgradeResultReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpgradeResultReason_Type.__name__ = "DisplayString"
_UpgradeResultReason_Object = MibTableColumn
upgradeResultReason = _UpgradeResultReason_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 2, 1, 4),
    _UpgradeResultReason_Type()
)
upgradeResultReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeResultReason.setStatus("current")
_UpgradeResultTimeStarted_Type = TimeStamp
_UpgradeResultTimeStarted_Object = MibTableColumn
upgradeResultTimeStarted = _UpgradeResultTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 2, 1, 5),
    _UpgradeResultTimeStarted_Type()
)
upgradeResultTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeResultTimeStarted.setStatus("current")
_UpgradeResultTimeCompleted_Type = TimeStamp
_UpgradeResultTimeCompleted_Object = MibTableColumn
upgradeResultTimeCompleted = _UpgradeResultTimeCompleted_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 2, 1, 6),
    _UpgradeResultTimeCompleted_Type()
)
upgradeResultTimeCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeResultTimeCompleted.setStatus("current")
_TnUpgradeTargetTable_Object = MibTable
tnUpgradeTargetTable = _TnUpgradeTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 3)
)
if mibBuilder.loadTexts:
    tnUpgradeTargetTable.setStatus("current")
_TnUpgradeTargetEntry_Object = MibTableRow
tnUpgradeTargetEntry = _TnUpgradeTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 3, 1)
)
tnUpgradeTargetEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TN-DEV-SYS-UPGRADER-MIB", "upgradeTargetIndex"),
)
if mibBuilder.loadTexts:
    tnUpgradeTargetEntry.setStatus("current")
_UpgradeTargetIndex_Type = Integer32
_UpgradeTargetIndex_Object = MibTableColumn
upgradeTargetIndex = _UpgradeTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 3, 1, 1),
    _UpgradeTargetIndex_Type()
)
upgradeTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upgradeTargetIndex.setStatus("current")
_UpgradeTargetModule_Type = Integer32
_UpgradeTargetModule_Object = MibTableColumn
upgradeTargetModule = _UpgradeTargetModule_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 3, 1, 2),
    _UpgradeTargetModule_Type()
)
upgradeTargetModule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upgradeTargetModule.setStatus("current")
_UpgradeTargetEntryStatus_Type = RowStatus
_UpgradeTargetEntryStatus_Object = MibTableColumn
upgradeTargetEntryStatus = _UpgradeTargetEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 3, 1, 3),
    _UpgradeTargetEntryStatus_Type()
)
upgradeTargetEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upgradeTargetEntryStatus.setStatus("current")
_TnUpgradeGetIndexTable_Object = MibTable
tnUpgradeGetIndexTable = _TnUpgradeGetIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 4)
)
if mibBuilder.loadTexts:
    tnUpgradeGetIndexTable.setStatus("current")
_TnUpgradeGetIndexEntry_Object = MibTableRow
tnUpgradeGetIndexEntry = _TnUpgradeGetIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 4, 1)
)
tnUpgradeGetIndexEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnUpgradeGetIndexEntry.setStatus("current")
_NextTargetIndex_Type = Integer32
_NextTargetIndex_Object = MibTableColumn
nextTargetIndex = _NextTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 4, 1, 1),
    _NextTargetIndex_Type()
)
nextTargetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextTargetIndex.setStatus("current")
_NextFirmwareIndex_Type = Integer32
_NextFirmwareIndex_Object = MibTableColumn
nextFirmwareIndex = _NextFirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 4, 1, 2),
    _NextFirmwareIndex_Type()
)
nextFirmwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextFirmwareIndex.setStatus("current")
_TnUpgradeFirmwareTable_Object = MibTable
tnUpgradeFirmwareTable = _TnUpgradeFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 5)
)
if mibBuilder.loadTexts:
    tnUpgradeFirmwareTable.setStatus("current")
_TnUpgradeFirmwareEntry_Object = MibTableRow
tnUpgradeFirmwareEntry = _TnUpgradeFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 5, 1)
)
tnUpgradeFirmwareEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TN-DEV-SYS-UPGRADER-MIB", "upgradeFirmwareIndex"),
)
if mibBuilder.loadTexts:
    tnUpgradeFirmwareEntry.setStatus("current")
_UpgradeFirmwareIndex_Type = Integer32
_UpgradeFirmwareIndex_Object = MibTableColumn
upgradeFirmwareIndex = _UpgradeFirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 5, 1, 1),
    _UpgradeFirmwareIndex_Type()
)
upgradeFirmwareIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upgradeFirmwareIndex.setStatus("current")


class _UpgradeFirmwareCardType_Type(DisplayString):
    """Custom type upgradeFirmwareCardType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UpgradeFirmwareCardType_Type.__name__ = "DisplayString"
_UpgradeFirmwareCardType_Object = MibTableColumn
upgradeFirmwareCardType = _UpgradeFirmwareCardType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 5, 1, 2),
    _UpgradeFirmwareCardType_Type()
)
upgradeFirmwareCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeFirmwareCardType.setStatus("current")


class _UpgradeFirmwareRevision_Type(DisplayString):
    """Custom type upgradeFirmwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UpgradeFirmwareRevision_Type.__name__ = "DisplayString"
_UpgradeFirmwareRevision_Object = MibTableColumn
upgradeFirmwareRevision = _UpgradeFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 5, 1, 3),
    _UpgradeFirmwareRevision_Type()
)
upgradeFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeFirmwareRevision.setStatus("current")


class _UpgradeFirmwareFileName_Type(DisplayString):
    """Custom type upgradeFirmwareFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UpgradeFirmwareFileName_Type.__name__ = "DisplayString"
_UpgradeFirmwareFileName_Object = MibTableColumn
upgradeFirmwareFileName = _UpgradeFirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 5, 1, 4),
    _UpgradeFirmwareFileName_Type()
)
upgradeFirmwareFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeFirmwareFileName.setStatus("current")


class _UpgradeFirmwareBuildDate_Type(DisplayString):
    """Custom type upgradeFirmwareBuildDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UpgradeFirmwareBuildDate_Type.__name__ = "DisplayString"
_UpgradeFirmwareBuildDate_Object = MibTableColumn
upgradeFirmwareBuildDate = _UpgradeFirmwareBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 5, 1, 5),
    _UpgradeFirmwareBuildDate_Type()
)
upgradeFirmwareBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeFirmwareBuildDate.setStatus("current")
_TnUpgradeFirmwareDBTable_Object = MibTable
tnUpgradeFirmwareDBTable = _TnUpgradeFirmwareDBTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 6)
)
if mibBuilder.loadTexts:
    tnUpgradeFirmwareDBTable.setStatus("current")
_TnUpgradeFirmwareDBEntry_Object = MibTableRow
tnUpgradeFirmwareDBEntry = _TnUpgradeFirmwareDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 6, 1)
)
tnUpgradeFirmwareDBEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnUpgradeFirmwareDBEntry.setStatus("current")


class _UpgradeFirmwareDBFileName_Type(DisplayString):
    """Custom type upgradeFirmwareDBFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UpgradeFirmwareDBFileName_Type.__name__ = "DisplayString"
_UpgradeFirmwareDBFileName_Object = MibTableColumn
upgradeFirmwareDBFileName = _UpgradeFirmwareDBFileName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 6, 1, 1),
    _UpgradeFirmwareDBFileName_Type()
)
upgradeFirmwareDBFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeFirmwareDBFileName.setStatus("current")


class _UpgradeFirmwareDBOpCommand_Type(Integer32):
    """Custom type upgradeFirmwareDBOpCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("update", 2))
    )


_UpgradeFirmwareDBOpCommand_Type.__name__ = "Integer32"
_UpgradeFirmwareDBOpCommand_Object = MibTableColumn
upgradeFirmwareDBOpCommand = _UpgradeFirmwareDBOpCommand_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 6, 1, 2),
    _UpgradeFirmwareDBOpCommand_Type()
)
upgradeFirmwareDBOpCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeFirmwareDBOpCommand.setStatus("current")


class _UpgradeFirmwareDBOpResult_Type(Integer32):
    """Custom type upgradeFirmwareDBOpResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("inProgress", 2),
          ("failure", 3),
          ("success", 4))
    )


_UpgradeFirmwareDBOpResult_Type.__name__ = "Integer32"
_UpgradeFirmwareDBOpResult_Object = MibTableColumn
upgradeFirmwareDBOpResult = _UpgradeFirmwareDBOpResult_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 6, 1, 3),
    _UpgradeFirmwareDBOpResult_Type()
)
upgradeFirmwareDBOpResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeFirmwareDBOpResult.setStatus("current")


class _UpgradeFirmwareDBResultReason_Type(DisplayString):
    """Custom type upgradeFirmwareDBResultReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpgradeFirmwareDBResultReason_Type.__name__ = "DisplayString"
_UpgradeFirmwareDBResultReason_Object = MibTableColumn
upgradeFirmwareDBResultReason = _UpgradeFirmwareDBResultReason_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 6, 1, 4),
    _UpgradeFirmwareDBResultReason_Type()
)
upgradeFirmwareDBResultReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeFirmwareDBResultReason.setStatus("current")
_TnFirmwareUpgradeTable_Object = MibTable
tnFirmwareUpgradeTable = _TnFirmwareUpgradeTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 7)
)
if mibBuilder.loadTexts:
    tnFirmwareUpgradeTable.setStatus("current")
_TnFirmwareUpgradeEntry_Object = MibTableRow
tnFirmwareUpgradeEntry = _TnFirmwareUpgradeEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 7, 1)
)
tnFirmwareUpgradeEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnFirmwareUpgradeEntry.setStatus("current")


class _FwDownloadFile_Type(DisplayString):
    """Custom type fwDownloadFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_FwDownloadFile_Type.__name__ = "DisplayString"
_FwDownloadFile_Object = MibTableColumn
fwDownloadFile = _FwDownloadFile_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 7, 1, 1),
    _FwDownloadFile_Type()
)
fwDownloadFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwDownloadFile.setStatus("current")
_FwDownloadTFTPServerType_Type = InetAddressType
_FwDownloadTFTPServerType_Object = MibTableColumn
fwDownloadTFTPServerType = _FwDownloadTFTPServerType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 7, 1, 2),
    _FwDownloadTFTPServerType_Type()
)
fwDownloadTFTPServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwDownloadTFTPServerType.setStatus("current")
_FwDownloadTFTPServer_Type = InetAddress
_FwDownloadTFTPServer_Object = MibTableColumn
fwDownloadTFTPServer = _FwDownloadTFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 7, 1, 3),
    _FwDownloadTFTPServer_Type()
)
fwDownloadTFTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwDownloadTFTPServer.setStatus("current")


class _FwDownloadAction_Type(Integer32):
    """Custom type fwDownloadAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notDownloading", 1),
          ("downloadToActive", 2),
          ("downloadToBackup", 3),
          ("swap", 4))
    )


_FwDownloadAction_Type.__name__ = "Integer32"
_FwDownloadAction_Object = MibTableColumn
fwDownloadAction = _FwDownloadAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 7, 1, 4),
    _FwDownloadAction_Type()
)
fwDownloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwDownloadAction.setStatus("current")


class _FwDownloadStatus_Type(Integer32):
    """Custom type fwDownloadStatus based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("downloadSuccess", 1),
          ("downloadStatusUnknown", 2),
          ("downloadErrorIP", 3),
          ("downloadErrorTFTP", 4),
          ("downloadErrorBusy", 5),
          ("downloadErrorMalloc", 6),
          ("downloadErrorInvalid", 7),
          ("downloadErrorFlashProgram", 8),
          ("downloadErrorSame", 9),
          ("downloadErrorCurrentUnknown", 10),
          ("downloadErrorCurrentNotFound", 11),
          ("downloadErrorUpdateNotFound", 12),
          ("downloadErrorUpdateCRC", 13),
          ("downloadErrorUpdateSize", 14),
          ("downloadErrorFlashErase", 15),
          ("downloadErrorIncorrectImageVersion", 16))
    )


_FwDownloadStatus_Type.__name__ = "Integer32"
_FwDownloadStatus_Object = MibTableColumn
fwDownloadStatus = _FwDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 7, 1, 5),
    _FwDownloadStatus_Type()
)
fwDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDownloadStatus.setStatus("current")


class _FwDownloadType_Type(Integer32):
    """Custom type fwDownloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("perph", 2))
    )


_FwDownloadType_Type.__name__ = "Integer32"
_FwDownloadType_Object = MibTableColumn
fwDownloadType = _FwDownloadType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 1, 7, 1, 6),
    _FwDownloadType_Type()
)
fwDownloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwDownloadType.setStatus("current")

# Managed Objects groups


# Notification objects

tnUpgradeEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 30, 0, 1)
)
tnUpgradeEvt.setObjects(
      *(("TN-DEV-SYS-UPGRADER-MIB", "upgradeResultModule"),
        ("TN-DEV-SYS-UPGRADER-MIB", "upgradeResultStatus"))
)
if mibBuilder.loadTexts:
    tnUpgradeEvt.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-DEV-SYS-UPGRADER-MIB",
    **{"tnDevSysUpgraderMIB": tnDevSysUpgraderMIB,
       "tnDevSysUpgraderNotifications": tnDevSysUpgraderNotifications,
       "tnUpgradeEvt": tnUpgradeEvt,
       "tnDevSysUpgrader": tnDevSysUpgrader,
       "tnUpgradeOpTable": tnUpgradeOpTable,
       "tnUpgradeOpEntry": tnUpgradeOpEntry,
       "upgradeOpCommand": upgradeOpCommand,
       "upgradeOpStatus": upgradeOpStatus,
       "tnUpgradeResultTable": tnUpgradeResultTable,
       "tnUpgradeResultEntry": tnUpgradeResultEntry,
       "upgradeResultIndex": upgradeResultIndex,
       "upgradeResultModule": upgradeResultModule,
       "upgradeResultStatus": upgradeResultStatus,
       "upgradeResultReason": upgradeResultReason,
       "upgradeResultTimeStarted": upgradeResultTimeStarted,
       "upgradeResultTimeCompleted": upgradeResultTimeCompleted,
       "tnUpgradeTargetTable": tnUpgradeTargetTable,
       "tnUpgradeTargetEntry": tnUpgradeTargetEntry,
       "upgradeTargetIndex": upgradeTargetIndex,
       "upgradeTargetModule": upgradeTargetModule,
       "upgradeTargetEntryStatus": upgradeTargetEntryStatus,
       "tnUpgradeGetIndexTable": tnUpgradeGetIndexTable,
       "tnUpgradeGetIndexEntry": tnUpgradeGetIndexEntry,
       "nextTargetIndex": nextTargetIndex,
       "nextFirmwareIndex": nextFirmwareIndex,
       "tnUpgradeFirmwareTable": tnUpgradeFirmwareTable,
       "tnUpgradeFirmwareEntry": tnUpgradeFirmwareEntry,
       "upgradeFirmwareIndex": upgradeFirmwareIndex,
       "upgradeFirmwareCardType": upgradeFirmwareCardType,
       "upgradeFirmwareRevision": upgradeFirmwareRevision,
       "upgradeFirmwareFileName": upgradeFirmwareFileName,
       "upgradeFirmwareBuildDate": upgradeFirmwareBuildDate,
       "tnUpgradeFirmwareDBTable": tnUpgradeFirmwareDBTable,
       "tnUpgradeFirmwareDBEntry": tnUpgradeFirmwareDBEntry,
       "upgradeFirmwareDBFileName": upgradeFirmwareDBFileName,
       "upgradeFirmwareDBOpCommand": upgradeFirmwareDBOpCommand,
       "upgradeFirmwareDBOpResult": upgradeFirmwareDBOpResult,
       "upgradeFirmwareDBResultReason": upgradeFirmwareDBResultReason,
       "tnFirmwareUpgradeTable": tnFirmwareUpgradeTable,
       "tnFirmwareUpgradeEntry": tnFirmwareUpgradeEntry,
       "fwDownloadFile": fwDownloadFile,
       "fwDownloadTFTPServerType": fwDownloadTFTPServerType,
       "fwDownloadTFTPServer": fwDownloadTFTPServer,
       "fwDownloadAction": fwDownloadAction,
       "fwDownloadStatus": fwDownloadStatus,
       "fwDownloadType": fwDownloadType}
)
