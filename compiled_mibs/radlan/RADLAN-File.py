# SNMP MIB module (RADLAN-File) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\eltexmes21xx\RADLAN-File
# Produced by pysmi-1.6.2 at Thu Oct  2 12:22:15 2025
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

(rlFile,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rlFile")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlFileMibVersion_Type = Integer32
_RlFileMibVersion_Object = MibScalar
rlFileMibVersion = _RlFileMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 1),
    _RlFileMibVersion_Type()
)
rlFileMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFileMibVersion.setStatus("current")
_RlFileTable_Object = MibTable
rlFileTable = _RlFileTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 2)
)
if mibBuilder.loadTexts:
    rlFileTable.setStatus("current")
_RlFileEntry_Object = MibTableRow
rlFileEntry = _RlFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 2, 1)
)
rlFileEntry.setIndexNames(
    (1, "RADLAN-File", "rlFileName"),
)
if mibBuilder.loadTexts:
    rlFileEntry.setStatus("current")


class _RlFileName_Type(OctetString):
    """Custom type rlFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RlFileName_Type.__name__ = "OctetString"
_RlFileName_Object = MibTableColumn
rlFileName = _RlFileName_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 1),
    _RlFileName_Type()
)
rlFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFileName.setStatus("current")


class _RlFilePermission_Type(Integer32):
    """Custom type rlFilePermission based on Integer32"""
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
        *(("read", 1),
          ("write", 2),
          ("readWrite", 3),
          ("noReadNoWrite", 4))
    )


_RlFilePermission_Type.__name__ = "Integer32"
_RlFilePermission_Object = MibTableColumn
rlFilePermission = _RlFilePermission_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 2),
    _RlFilePermission_Type()
)
rlFilePermission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFilePermission.setStatus("current")
_RlFileSize_Type = Integer32
_RlFileSize_Object = MibTableColumn
rlFileSize = _RlFileSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 3),
    _RlFileSize_Type()
)
rlFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFileSize.setStatus("current")
_RlFileModificationDate_Type = DisplayString
_RlFileModificationDate_Object = MibTableColumn
rlFileModificationDate = _RlFileModificationDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 4),
    _RlFileModificationDate_Type()
)
rlFileModificationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFileModificationDate.setStatus("current")
_RlFileModificationTime_Type = DisplayString
_RlFileModificationTime_Object = MibTableColumn
rlFileModificationTime = _RlFileModificationTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 5),
    _RlFileModificationTime_Type()
)
rlFileModificationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFileModificationTime.setStatus("current")
_RlFileRowStatus_Type = RowStatus
_RlFileRowStatus_Object = MibTableColumn
rlFileRowStatus = _RlFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 6),
    _RlFileRowStatus_Type()
)
rlFileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFileRowStatus.setStatus("current")
_RlFileFlashSize_Type = Integer32
_RlFileFlashSize_Object = MibTableColumn
rlFileFlashSize = _RlFileFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 7),
    _RlFileFlashSize_Type()
)
rlFileFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFileFlashSize.setStatus("current")
_RlFileFullNormalizedName_Type = OctetString
_RlFileFullNormalizedName_Object = MibTableColumn
rlFileFullNormalizedName = _RlFileFullNormalizedName_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 8),
    _RlFileFullNormalizedName_Type()
)
rlFileFullNormalizedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFileFullNormalizedName.setStatus("current")
_RlFileActionTable_Object = MibTable
rlFileActionTable = _RlFileActionTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 3)
)
if mibBuilder.loadTexts:
    rlFileActionTable.setStatus("current")
_RlFileActionEntry_Object = MibTableRow
rlFileActionEntry = _RlFileActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 3, 1)
)
rlFileActionEntry.setIndexNames(
    (0, "RADLAN-File", "rlFileActionName"),
)
if mibBuilder.loadTexts:
    rlFileActionEntry.setStatus("current")


class _RlFileActionName_Type(OctetString):
    """Custom type rlFileActionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RlFileActionName_Type.__name__ = "OctetString"
_RlFileActionName_Object = MibTableColumn
rlFileActionName = _RlFileActionName_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 3, 1, 1),
    _RlFileActionName_Type()
)
rlFileActionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFileActionName.setStatus("current")


class _RlFileActionNewName_Type(OctetString):
    """Custom type rlFileActionNewName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RlFileActionNewName_Type.__name__ = "OctetString"
_RlFileActionNewName_Object = MibTableColumn
rlFileActionNewName = _RlFileActionNewName_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 3, 1, 2),
    _RlFileActionNewName_Type()
)
rlFileActionNewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFileActionNewName.setStatus("current")
_RlFileActionRowStatus_Type = RowStatus
_RlFileActionRowStatus_Object = MibTableColumn
rlFileActionRowStatus = _RlFileActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 3, 1, 3),
    _RlFileActionRowStatus_Type()
)
rlFileActionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFileActionRowStatus.setStatus("current")


class _RlFileActionCommand_Type(Integer32):
    """Custom type rlFileActionCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("rename", 1)
    )


_RlFileActionCommand_Type.__name__ = "Integer32"
_RlFileActionCommand_Object = MibTableColumn
rlFileActionCommand = _RlFileActionCommand_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 3, 1, 4),
    _RlFileActionCommand_Type()
)
rlFileActionCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFileActionCommand.setStatus("current")
_RlFileTotalSizeOfFlash_Type = Integer32
_RlFileTotalSizeOfFlash_Object = MibScalar
rlFileTotalSizeOfFlash = _RlFileTotalSizeOfFlash_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 4),
    _RlFileTotalSizeOfFlash_Type()
)
rlFileTotalSizeOfFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFileTotalSizeOfFlash.setStatus("current")
_RlFileFreeSizeOfFlash_Type = Integer32
_RlFileFreeSizeOfFlash_Object = MibScalar
rlFileFreeSizeOfFlash = _RlFileFreeSizeOfFlash_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 5),
    _RlFileFreeSizeOfFlash_Type()
)
rlFileFreeSizeOfFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFileFreeSizeOfFlash.setStatus("current")


class _RlFileAuditingEnable_Type(TruthValue):
    """Custom type rlFileAuditingEnable based on TruthValue"""
    defaultValue = 1


_RlFileAuditingEnable_Type.__name__ = "TruthValue"
_RlFileAuditingEnable_Object = MibScalar
rlFileAuditingEnable = _RlFileAuditingEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 96, 6),
    _RlFileAuditingEnable_Type()
)
rlFileAuditingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFileAuditingEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-File",
    **{"rlFileMibVersion": rlFileMibVersion,
       "rlFileTable": rlFileTable,
       "rlFileEntry": rlFileEntry,
       "rlFileName": rlFileName,
       "rlFilePermission": rlFilePermission,
       "rlFileSize": rlFileSize,
       "rlFileModificationDate": rlFileModificationDate,
       "rlFileModificationTime": rlFileModificationTime,
       "rlFileRowStatus": rlFileRowStatus,
       "rlFileFlashSize": rlFileFlashSize,
       "rlFileFullNormalizedName": rlFileFullNormalizedName,
       "rlFileActionTable": rlFileActionTable,
       "rlFileActionEntry": rlFileActionEntry,
       "rlFileActionName": rlFileActionName,
       "rlFileActionNewName": rlFileActionNewName,
       "rlFileActionRowStatus": rlFileActionRowStatus,
       "rlFileActionCommand": rlFileActionCommand,
       "rlFileTotalSizeOfFlash": rlFileTotalSizeOfFlash,
       "rlFileFreeSizeOfFlash": rlFileFreeSizeOfFlash,
       "rlFileAuditingEnable": rlFileAuditingEnable}
)
