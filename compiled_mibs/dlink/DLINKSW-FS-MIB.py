# SNMP MIB module (DLINKSW-FS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-FS-MIB
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwFsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 18)
)
if mibBuilder.loadTexts:
    dlinkSwFsMIB.setRevisions(
        ("2013-04-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DFsNotifications_ObjectIdentity = ObjectIdentity
dFsNotifications = _DFsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 0)
)
_DFsObjects_ObjectIdentity = ObjectIdentity
dFsObjects = _DFsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1)
)
_DFsBasicInfoCtrlStatus_Type = DisplayString
_DFsBasicInfoCtrlStatus_Object = MibScalar
dFsBasicInfoCtrlStatus = _DFsBasicInfoCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 1),
    _DFsBasicInfoCtrlStatus_Type()
)
dFsBasicInfoCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFsBasicInfoCtrlStatus.setStatus("current")
_DFsBasicOperation_ObjectIdentity = ObjectIdentity
dFsBasicOperation = _DFsBasicOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 2)
)


class _DFsCurrentDirUrl_Type(OctetString):
    """Custom type dFsCurrentDirUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 799),
    )


_DFsCurrentDirUrl_Type.__name__ = "OctetString"
_DFsCurrentDirUrl_Object = MibScalar
dFsCurrentDirUrl = _DFsCurrentDirUrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 2, 1),
    _DFsCurrentDirUrl_Type()
)
dFsCurrentDirUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dFsCurrentDirUrl.setStatus("current")
_DFsCurrentDirectoryTable_Object = MibTable
dFsCurrentDirectoryTable = _DFsCurrentDirectoryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dFsCurrentDirectoryTable.setStatus("current")
_DFsCurrentDirectoryEntry_Object = MibTableRow
dFsCurrentDirectoryEntry = _DFsCurrentDirectoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 2, 2, 1)
)
dFsCurrentDirectoryEntry.setIndexNames(
    (0, "DLINKSW-FS-MIB", "dFsCurrentDirItemName"),
)
if mibBuilder.loadTexts:
    dFsCurrentDirectoryEntry.setStatus("current")
_DFsCurrentDirItemName_Type = DisplayString
_DFsCurrentDirItemName_Object = MibTableColumn
dFsCurrentDirItemName = _DFsCurrentDirItemName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 2, 2, 1, 1),
    _DFsCurrentDirItemName_Type()
)
dFsCurrentDirItemName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dFsCurrentDirItemName.setStatus("current")


class _DFsCurrentDirItemMode_Type(Bits):
    """Custom type dFsCurrentDirItemMode based on Bits"""
    namedValues = NamedValues(
        *(("directory", 0),
          ("readable", 1),
          ("writeable", 2))
    )

_DFsCurrentDirItemMode_Type.__name__ = "Bits"
_DFsCurrentDirItemMode_Object = MibTableColumn
dFsCurrentDirItemMode = _DFsCurrentDirItemMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 2, 2, 1, 2),
    _DFsCurrentDirItemMode_Type()
)
dFsCurrentDirItemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFsCurrentDirItemMode.setStatus("current")
_DFsCurrentDirItemSize_Type = Unsigned32
_DFsCurrentDirItemSize_Object = MibTableColumn
dFsCurrentDirItemSize = _DFsCurrentDirItemSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 2, 2, 1, 3),
    _DFsCurrentDirItemSize_Type()
)
dFsCurrentDirItemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFsCurrentDirItemSize.setStatus("current")
if mibBuilder.loadTexts:
    dFsCurrentDirItemSize.setUnits("bytes")
_DFsCurrentDirItemTime_Type = DateAndTime
_DFsCurrentDirItemTime_Object = MibTableColumn
dFsCurrentDirItemTime = _DFsCurrentDirItemTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 2, 2, 1, 4),
    _DFsCurrentDirItemTime_Type()
)
dFsCurrentDirItemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFsCurrentDirItemTime.setStatus("current")
_DFsCurrentDirItemRawStatus_Type = RowStatus
_DFsCurrentDirItemRawStatus_Object = MibTableColumn
dFsCurrentDirItemRawStatus = _DFsCurrentDirItemRawStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 2, 2, 1, 5),
    _DFsCurrentDirItemRawStatus_Type()
)
dFsCurrentDirItemRawStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dFsCurrentDirItemRawStatus.setStatus("current")
_DFsFileRenameCtrl_ObjectIdentity = ObjectIdentity
dFsFileRenameCtrl = _DFsFileRenameCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 2, 3)
)


class _DFsFileRenameSourceUrl_Type(OctetString):
    """Custom type dFsFileRenameSourceUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 799),
    )


_DFsFileRenameSourceUrl_Type.__name__ = "OctetString"
_DFsFileRenameSourceUrl_Object = MibScalar
dFsFileRenameSourceUrl = _DFsFileRenameSourceUrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 2, 3, 1),
    _DFsFileRenameSourceUrl_Type()
)
dFsFileRenameSourceUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dFsFileRenameSourceUrl.setStatus("current")


class _DFsFileRenameTargetUrl_Type(OctetString):
    """Custom type dFsFileRenameTargetUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 799),
    )


_DFsFileRenameTargetUrl_Type.__name__ = "OctetString"
_DFsFileRenameTargetUrl_Object = MibScalar
dFsFileRenameTargetUrl = _DFsFileRenameTargetUrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 2, 3, 2),
    _DFsFileRenameTargetUrl_Type()
)
dFsFileRenameTargetUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dFsFileRenameTargetUrl.setStatus("current")


class _DFsFileRenameActivity_Type(Integer32):
    """Custom type dFsFileRenameActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rename", 1),
          ("noOp", 2))
    )


_DFsFileRenameActivity_Type.__name__ = "Integer32"
_DFsFileRenameActivity_Object = MibScalar
dFsFileRenameActivity = _DFsFileRenameActivity_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 2, 3, 3),
    _DFsFileRenameActivity_Type()
)
dFsFileRenameActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dFsFileRenameActivity.setStatus("current")
_DFsDriveCtrl_ObjectIdentity = ObjectIdentity
dFsDriveCtrl = _DFsDriveCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 3)
)
_DFsDriveInfoTable_Object = MibTable
dFsDriveInfoTable = _DFsDriveInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dFsDriveInfoTable.setStatus("current")
_DFsDriveInfoEntry_Object = MibTableRow
dFsDriveInfoEntry = _DFsDriveInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 3, 1, 1)
)
dFsDriveInfoEntry.setIndexNames(
    (0, "DLINKSW-FS-MIB", "dFsDriveInfoUnitID"),
    (0, "DLINKSW-FS-MIB", "dFsDriveInfoDriveID"),
)
if mibBuilder.loadTexts:
    dFsDriveInfoEntry.setStatus("current")


class _DFsDriveInfoUnitID_Type(Unsigned32):
    """Custom type dFsDriveInfoUnitID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DFsDriveInfoUnitID_Type.__name__ = "Unsigned32"
_DFsDriveInfoUnitID_Object = MibTableColumn
dFsDriveInfoUnitID = _DFsDriveInfoUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 3, 1, 1, 1),
    _DFsDriveInfoUnitID_Type()
)
dFsDriveInfoUnitID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dFsDriveInfoUnitID.setStatus("current")


class _DFsDriveInfoDriveID_Type(Integer32):
    """Custom type dFsDriveInfoDriveID based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2),
          ("c", 3),
          ("d", 4),
          ("e", 5),
          ("f", 6),
          ("g", 7),
          ("h", 8),
          ("i", 9),
          ("j", 10),
          ("k", 11),
          ("l", 12),
          ("m", 13),
          ("n", 14),
          ("o", 15),
          ("p", 16),
          ("q", 17),
          ("r", 18),
          ("s", 19),
          ("t", 20),
          ("u", 21),
          ("v", 22),
          ("w", 23),
          ("x", 24),
          ("y", 25),
          ("z", 26))
    )


_DFsDriveInfoDriveID_Type.__name__ = "Integer32"
_DFsDriveInfoDriveID_Object = MibTableColumn
dFsDriveInfoDriveID = _DFsDriveInfoDriveID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 3, 1, 1, 2),
    _DFsDriveInfoDriveID_Type()
)
dFsDriveInfoDriveID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dFsDriveInfoDriveID.setStatus("current")
_DFsDriveInfoMediaType_Type = DisplayString
_DFsDriveInfoMediaType_Object = MibTableColumn
dFsDriveInfoMediaType = _DFsDriveInfoMediaType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 3, 1, 1, 3),
    _DFsDriveInfoMediaType_Type()
)
dFsDriveInfoMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFsDriveInfoMediaType.setStatus("current")
_DFsDriveInfoSize_Type = Unsigned32
_DFsDriveInfoSize_Object = MibTableColumn
dFsDriveInfoSize = _DFsDriveInfoSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 3, 1, 1, 4),
    _DFsDriveInfoSize_Type()
)
dFsDriveInfoSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFsDriveInfoSize.setStatus("current")
if mibBuilder.loadTexts:
    dFsDriveInfoSize.setUnits("Mbytes")


class _DFsDriveInfoFsType_Type(Integer32):
    """Custom type dFsDriveInfoFsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("ffs", 1),
          ("fat16", 2),
          ("fat32", 3))
    )


_DFsDriveInfoFsType_Type.__name__ = "Integer32"
_DFsDriveInfoFsType_Object = MibTableColumn
dFsDriveInfoFsType = _DFsDriveInfoFsType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 3, 1, 1, 5),
    _DFsDriveInfoFsType_Type()
)
dFsDriveInfoFsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFsDriveInfoFsType.setStatus("current")


class _DFsDriveInfoLabel_Type(DisplayString):
    """Custom type dFsDriveInfoLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_DFsDriveInfoLabel_Type.__name__ = "DisplayString"
_DFsDriveInfoLabel_Object = MibTableColumn
dFsDriveInfoLabel = _DFsDriveInfoLabel_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 3, 1, 1, 6),
    _DFsDriveInfoLabel_Type()
)
dFsDriveInfoLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dFsDriveInfoLabel.setStatus("current")


class _DFsDriveInfoFormatDrive_Type(Integer32):
    """Custom type dFsDriveInfoFormatDrive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("format", 1),
          ("noOp", 2))
    )


_DFsDriveInfoFormatDrive_Type.__name__ = "Integer32"
_DFsDriveInfoFormatDrive_Object = MibTableColumn
dFsDriveInfoFormatDrive = _DFsDriveInfoFormatDrive_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 1, 3, 1, 1, 7),
    _DFsDriveInfoFormatDrive_Type()
)
dFsDriveInfoFormatDrive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dFsDriveInfoFormatDrive.setStatus("current")
_DFsConformance_ObjectIdentity = ObjectIdentity
dFsConformance = _DFsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 2)
)
_DFsCompliances_ObjectIdentity = ObjectIdentity
dFsCompliances = _DFsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 2, 1)
)
_DFsGroups_ObjectIdentity = ObjectIdentity
dFsGroups = _DFsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 2, 2)
)

# Managed Objects groups

dFsBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 2, 2, 1)
)
dFsBasicGroup.setObjects(
      *(("DLINKSW-FS-MIB", "dFsBasicInfoCtrlStatus"),
        ("DLINKSW-FS-MIB", "dFsCurrentDirUrl"),
        ("DLINKSW-FS-MIB", "dFsCurrentDirItemMode"),
        ("DLINKSW-FS-MIB", "dFsCurrentDirItemSize"),
        ("DLINKSW-FS-MIB", "dFsCurrentDirItemTime"),
        ("DLINKSW-FS-MIB", "dFsCurrentDirItemRawStatus"),
        ("DLINKSW-FS-MIB", "dFsFileRenameSourceUrl"),
        ("DLINKSW-FS-MIB", "dFsFileRenameTargetUrl"),
        ("DLINKSW-FS-MIB", "dFsFileRenameActivity"))
)
if mibBuilder.loadTexts:
    dFsBasicGroup.setStatus("current")

dFsDriveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 2, 2, 2)
)
dFsDriveGroup.setObjects(
      *(("DLINKSW-FS-MIB", "dFsDriveInfoMediaType"),
        ("DLINKSW-FS-MIB", "dFsDriveInfoSize"),
        ("DLINKSW-FS-MIB", "dFsDriveInfoFsType"),
        ("DLINKSW-FS-MIB", "dFsDriveInfoLabel"),
        ("DLINKSW-FS-MIB", "dFsDriveInfoFormatDrive"))
)
if mibBuilder.loadTexts:
    dFsDriveGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dFsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 18, 2, 1, 1)
)
dFsMIBCompliance.setObjects(
      *(("DLINKSW-FS-MIB", "dFsBasicGroup"),
        ("DLINKSW-FS-MIB", "dFsDriveGroup"))
)
if mibBuilder.loadTexts:
    dFsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-FS-MIB",
    **{"dlinkSwFsMIB": dlinkSwFsMIB,
       "dFsNotifications": dFsNotifications,
       "dFsObjects": dFsObjects,
       "dFsBasicInfoCtrlStatus": dFsBasicInfoCtrlStatus,
       "dFsBasicOperation": dFsBasicOperation,
       "dFsCurrentDirUrl": dFsCurrentDirUrl,
       "dFsCurrentDirectoryTable": dFsCurrentDirectoryTable,
       "dFsCurrentDirectoryEntry": dFsCurrentDirectoryEntry,
       "dFsCurrentDirItemName": dFsCurrentDirItemName,
       "dFsCurrentDirItemMode": dFsCurrentDirItemMode,
       "dFsCurrentDirItemSize": dFsCurrentDirItemSize,
       "dFsCurrentDirItemTime": dFsCurrentDirItemTime,
       "dFsCurrentDirItemRawStatus": dFsCurrentDirItemRawStatus,
       "dFsFileRenameCtrl": dFsFileRenameCtrl,
       "dFsFileRenameSourceUrl": dFsFileRenameSourceUrl,
       "dFsFileRenameTargetUrl": dFsFileRenameTargetUrl,
       "dFsFileRenameActivity": dFsFileRenameActivity,
       "dFsDriveCtrl": dFsDriveCtrl,
       "dFsDriveInfoTable": dFsDriveInfoTable,
       "dFsDriveInfoEntry": dFsDriveInfoEntry,
       "dFsDriveInfoUnitID": dFsDriveInfoUnitID,
       "dFsDriveInfoDriveID": dFsDriveInfoDriveID,
       "dFsDriveInfoMediaType": dFsDriveInfoMediaType,
       "dFsDriveInfoSize": dFsDriveInfoSize,
       "dFsDriveInfoFsType": dFsDriveInfoFsType,
       "dFsDriveInfoLabel": dFsDriveInfoLabel,
       "dFsDriveInfoFormatDrive": dFsDriveInfoFormatDrive,
       "dFsConformance": dFsConformance,
       "dFsCompliances": dFsCompliances,
       "dFsMIBCompliance": dFsMIBCompliance,
       "dFsGroups": dFsGroups,
       "dFsBasicGroup": dFsBasicGroup,
       "dFsDriveGroup": dFsDriveGroup}
)
