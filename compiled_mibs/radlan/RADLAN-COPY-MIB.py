# SNMP MIB module (RADLAN-COPY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\radlan\RADLAN-COPY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:22:13 2025
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

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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

(DisplayString,) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DisplayString")


# MODULE-IDENTITY

rlCopy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 87)
)
if mibBuilder.loadTexts:
    rlCopy.setRevisions(
        ("2006-02-02 00:00",
         "2003-09-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RlCopyApplicationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("mcli", 1),
          ("cli", 2),
          ("ewb", 3),
          ("nms", 4),
          ("initerm", 5),
          ("serial", 6))
    )



class RlCopyLocationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("anotherUnit", 2),
          ("tftp", 3),
          ("xmodem", 4),
          ("scp", 5),
          ("serial", 6))
    )



class RlCopyFileType(TextualConvention, Integer32):
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
        *(("other", 1),
          ("runningConfig", 2),
          ("startupConfig", 3),
          ("backupConfig", 4),
          ("runningMibConfig", 5),
          ("startupMibConfig", 6),
          ("backupMibConfig", 7),
          ("image", 8),
          ("boot", 9),
          ("null", 10))
    )



# MIB Managed Objects in the order of their OIDs

_RlCopyMibVersion_Type = Integer32
_RlCopyMibVersion_Object = MibScalar
rlCopyMibVersion = _RlCopyMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 1),
    _RlCopyMibVersion_Type()
)
rlCopyMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyMibVersion.setStatus("current")
_RlCopyTable_Object = MibTable
rlCopyTable = _RlCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2)
)
if mibBuilder.loadTexts:
    rlCopyTable.setStatus("current")
_RlCopyEntry_Object = MibTableRow
rlCopyEntry = _RlCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1)
)
rlCopyEntry.setIndexNames(
    (0, "RADLAN-COPY-MIB", "rlCopyIndex"),
)
if mibBuilder.loadTexts:
    rlCopyEntry.setStatus("current")
_RlCopyIndex_Type = Integer32
_RlCopyIndex_Object = MibTableColumn
rlCopyIndex = _RlCopyIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 1),
    _RlCopyIndex_Type()
)
rlCopyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyIndex.setStatus("current")
_RlCopyApplicationId_Type = RlCopyApplicationType
_RlCopyApplicationId_Object = MibTableColumn
rlCopyApplicationId = _RlCopyApplicationId_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 2),
    _RlCopyApplicationId_Type()
)
rlCopyApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyApplicationId.setStatus("current")
_RlCopySourceLocation_Type = RlCopyLocationType
_RlCopySourceLocation_Object = MibTableColumn
rlCopySourceLocation = _RlCopySourceLocation_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 3),
    _RlCopySourceLocation_Type()
)
rlCopySourceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopySourceLocation.setStatus("current")
_RlCopySourceIpAddress_Type = IpAddress
_RlCopySourceIpAddress_Object = MibTableColumn
rlCopySourceIpAddress = _RlCopySourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 4),
    _RlCopySourceIpAddress_Type()
)
rlCopySourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopySourceIpAddress.setStatus("current")
_RlCopySourceUnitNumber_Type = Integer32
_RlCopySourceUnitNumber_Object = MibTableColumn
rlCopySourceUnitNumber = _RlCopySourceUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 5),
    _RlCopySourceUnitNumber_Type()
)
rlCopySourceUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopySourceUnitNumber.setStatus("current")
_RlCopySourceFileName_Type = DisplayString
_RlCopySourceFileName_Object = MibTableColumn
rlCopySourceFileName = _RlCopySourceFileName_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 6),
    _RlCopySourceFileName_Type()
)
rlCopySourceFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopySourceFileName.setStatus("current")
_RlCopySourceFileType_Type = RlCopyFileType
_RlCopySourceFileType_Object = MibTableColumn
rlCopySourceFileType = _RlCopySourceFileType_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 7),
    _RlCopySourceFileType_Type()
)
rlCopySourceFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopySourceFileType.setStatus("current")
_RlCopyDestinationLocation_Type = RlCopyLocationType
_RlCopyDestinationLocation_Object = MibTableColumn
rlCopyDestinationLocation = _RlCopyDestinationLocation_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 8),
    _RlCopyDestinationLocation_Type()
)
rlCopyDestinationLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyDestinationLocation.setStatus("current")
_RlCopyDestinationIpAddress_Type = IpAddress
_RlCopyDestinationIpAddress_Object = MibTableColumn
rlCopyDestinationIpAddress = _RlCopyDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 9),
    _RlCopyDestinationIpAddress_Type()
)
rlCopyDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyDestinationIpAddress.setStatus("current")
_RlCopyDestinationUnitNumber_Type = Integer32
_RlCopyDestinationUnitNumber_Object = MibTableColumn
rlCopyDestinationUnitNumber = _RlCopyDestinationUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 10),
    _RlCopyDestinationUnitNumber_Type()
)
rlCopyDestinationUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyDestinationUnitNumber.setStatus("current")
_RlCopyDestinationFileName_Type = DisplayString
_RlCopyDestinationFileName_Object = MibTableColumn
rlCopyDestinationFileName = _RlCopyDestinationFileName_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 11),
    _RlCopyDestinationFileName_Type()
)
rlCopyDestinationFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyDestinationFileName.setStatus("current")
_RlCopyDestinationFileType_Type = RlCopyFileType
_RlCopyDestinationFileType_Object = MibTableColumn
rlCopyDestinationFileType = _RlCopyDestinationFileType_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 12),
    _RlCopyDestinationFileType_Type()
)
rlCopyDestinationFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyDestinationFileType.setStatus("current")
_RlCopyUpTime_Type = TimeTicks
_RlCopyUpTime_Object = MibTableColumn
rlCopyUpTime = _RlCopyUpTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 13),
    _RlCopyUpTime_Type()
)
rlCopyUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyUpTime.setStatus("current")


class _RlCopyOperationState_Type(Integer32):
    """Custom type rlCopyOperationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("uploadInProgress", 1),
          ("downloadInProgress", 2),
          ("copyFailed", 3),
          ("copyTimedout", 4),
          ("copyFinished", 5))
    )


_RlCopyOperationState_Type.__name__ = "Integer32"
_RlCopyOperationState_Object = MibTableColumn
rlCopyOperationState = _RlCopyOperationState_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 14),
    _RlCopyOperationState_Type()
)
rlCopyOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyOperationState.setStatus("current")
_RlCopyBytesTransferred_Type = Integer32
_RlCopyBytesTransferred_Object = MibTableColumn
rlCopyBytesTransferred = _RlCopyBytesTransferred_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 15),
    _RlCopyBytesTransferred_Type()
)
rlCopyBytesTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyBytesTransferred.setStatus("current")


class _RlCopyInBackground_Type(Integer32):
    """Custom type rlCopyInBackground based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RlCopyInBackground_Type.__name__ = "Integer32"
_RlCopyInBackground_Object = MibTableColumn
rlCopyInBackground = _RlCopyInBackground_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 16),
    _RlCopyInBackground_Type()
)
rlCopyInBackground.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyInBackground.setStatus("current")
_RlCopyRowStatus_Type = RowStatus
_RlCopyRowStatus_Object = MibTableColumn
rlCopyRowStatus = _RlCopyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 17),
    _RlCopyRowStatus_Type()
)
rlCopyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyRowStatus.setStatus("current")


class _RlCopyHistoryIndex_Type(Integer32):
    """Custom type rlCopyHistoryIndex based on Integer32"""
    defaultValue = 0


_RlCopyHistoryIndex_Type.__name__ = "Integer32"
_RlCopyHistoryIndex_Object = MibTableColumn
rlCopyHistoryIndex = _RlCopyHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 18),
    _RlCopyHistoryIndex_Type()
)
rlCopyHistoryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryIndex.setStatus("current")
_RlCopyFreeHistoryIndex_Type = Integer32
_RlCopyFreeHistoryIndex_Object = MibScalar
rlCopyFreeHistoryIndex = _RlCopyFreeHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 3),
    _RlCopyFreeHistoryIndex_Type()
)
rlCopyFreeHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyFreeHistoryIndex.setStatus("current")
_RlCopyHistoryTable_Object = MibTable
rlCopyHistoryTable = _RlCopyHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4)
)
if mibBuilder.loadTexts:
    rlCopyHistoryTable.setStatus("current")
_RlCopyHistoryEntry_Object = MibTableRow
rlCopyHistoryEntry = _RlCopyHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1)
)
rlCopyHistoryEntry.setIndexNames(
    (0, "RADLAN-COPY-MIB", "rlCopyHistoryHistoryIndex"),
)
if mibBuilder.loadTexts:
    rlCopyHistoryEntry.setStatus("current")
_RlCopyHistoryHistoryIndex_Type = Integer32
_RlCopyHistoryHistoryIndex_Object = MibTableColumn
rlCopyHistoryHistoryIndex = _RlCopyHistoryHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 1),
    _RlCopyHistoryHistoryIndex_Type()
)
rlCopyHistoryHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryHistoryIndex.setStatus("current")
_RlCopyHistoryApplicationId_Type = RlCopyApplicationType
_RlCopyHistoryApplicationId_Object = MibTableColumn
rlCopyHistoryApplicationId = _RlCopyHistoryApplicationId_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 2),
    _RlCopyHistoryApplicationId_Type()
)
rlCopyHistoryApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryApplicationId.setStatus("current")
_RlCopyHistorySourceLocation_Type = RlCopyLocationType
_RlCopyHistorySourceLocation_Object = MibTableColumn
rlCopyHistorySourceLocation = _RlCopyHistorySourceLocation_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 3),
    _RlCopyHistorySourceLocation_Type()
)
rlCopyHistorySourceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistorySourceLocation.setStatus("current")
_RlCopyHistorySourceIpAddress_Type = IpAddress
_RlCopyHistorySourceIpAddress_Object = MibTableColumn
rlCopyHistorySourceIpAddress = _RlCopyHistorySourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 4),
    _RlCopyHistorySourceIpAddress_Type()
)
rlCopyHistorySourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistorySourceIpAddress.setStatus("current")
_RlCopyHistorySourceUnitNumber_Type = Integer32
_RlCopyHistorySourceUnitNumber_Object = MibTableColumn
rlCopyHistorySourceUnitNumber = _RlCopyHistorySourceUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 5),
    _RlCopyHistorySourceUnitNumber_Type()
)
rlCopyHistorySourceUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistorySourceUnitNumber.setStatus("current")
_RlCopyHistorySourceFileName_Type = DisplayString
_RlCopyHistorySourceFileName_Object = MibTableColumn
rlCopyHistorySourceFileName = _RlCopyHistorySourceFileName_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 6),
    _RlCopyHistorySourceFileName_Type()
)
rlCopyHistorySourceFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistorySourceFileName.setStatus("current")
_RlCopyHistorySourceFileType_Type = RlCopyFileType
_RlCopyHistorySourceFileType_Object = MibTableColumn
rlCopyHistorySourceFileType = _RlCopyHistorySourceFileType_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 7),
    _RlCopyHistorySourceFileType_Type()
)
rlCopyHistorySourceFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistorySourceFileType.setStatus("current")
_RlCopyHistoryDestinationLocation_Type = RlCopyLocationType
_RlCopyHistoryDestinationLocation_Object = MibTableColumn
rlCopyHistoryDestinationLocation = _RlCopyHistoryDestinationLocation_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 8),
    _RlCopyHistoryDestinationLocation_Type()
)
rlCopyHistoryDestinationLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryDestinationLocation.setStatus("current")
_RlCopyHistoryDestinationIpAddress_Type = IpAddress
_RlCopyHistoryDestinationIpAddress_Object = MibTableColumn
rlCopyHistoryDestinationIpAddress = _RlCopyHistoryDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 9),
    _RlCopyHistoryDestinationIpAddress_Type()
)
rlCopyHistoryDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryDestinationIpAddress.setStatus("current")
_RlCopyHistoryDestinationUnitNumber_Type = Integer32
_RlCopyHistoryDestinationUnitNumber_Object = MibTableColumn
rlCopyHistoryDestinationUnitNumber = _RlCopyHistoryDestinationUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 10),
    _RlCopyHistoryDestinationUnitNumber_Type()
)
rlCopyHistoryDestinationUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryDestinationUnitNumber.setStatus("current")
_RlCopyHistoryDestinationFileName_Type = DisplayString
_RlCopyHistoryDestinationFileName_Object = MibTableColumn
rlCopyHistoryDestinationFileName = _RlCopyHistoryDestinationFileName_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 11),
    _RlCopyHistoryDestinationFileName_Type()
)
rlCopyHistoryDestinationFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryDestinationFileName.setStatus("current")
_RlCopyHistoryDestinationFileType_Type = RlCopyFileType
_RlCopyHistoryDestinationFileType_Object = MibTableColumn
rlCopyHistoryDestinationFileType = _RlCopyHistoryDestinationFileType_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 12),
    _RlCopyHistoryDestinationFileType_Type()
)
rlCopyHistoryDestinationFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryDestinationFileType.setStatus("current")
_RlCopyHistoryUpTime_Type = TimeTicks
_RlCopyHistoryUpTime_Object = MibTableColumn
rlCopyHistoryUpTime = _RlCopyHistoryUpTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 13),
    _RlCopyHistoryUpTime_Type()
)
rlCopyHistoryUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryUpTime.setStatus("current")


class _RlCopyHistoryOperationState_Type(Integer32):
    """Custom type rlCopyHistoryOperationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("uploadInProgress", 1),
          ("downloadInProgress", 2),
          ("copyFailed", 3),
          ("copyTimedout", 4),
          ("copyFinished", 5))
    )


_RlCopyHistoryOperationState_Type.__name__ = "Integer32"
_RlCopyHistoryOperationState_Object = MibTableColumn
rlCopyHistoryOperationState = _RlCopyHistoryOperationState_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 14),
    _RlCopyHistoryOperationState_Type()
)
rlCopyHistoryOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryOperationState.setStatus("current")
_RlCopyHistoryBytesTransferred_Type = Integer32
_RlCopyHistoryBytesTransferred_Object = MibTableColumn
rlCopyHistoryBytesTransferred = _RlCopyHistoryBytesTransferred_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 15),
    _RlCopyHistoryBytesTransferred_Type()
)
rlCopyHistoryBytesTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryBytesTransferred.setStatus("current")


class _RlCopyHistoryInBackground_Type(Integer32):
    """Custom type rlCopyHistoryInBackground based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RlCopyHistoryInBackground_Type.__name__ = "Integer32"
_RlCopyHistoryInBackground_Object = MibTableColumn
rlCopyHistoryInBackground = _RlCopyHistoryInBackground_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 16),
    _RlCopyHistoryInBackground_Type()
)
rlCopyHistoryInBackground.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryInBackground.setStatus("current")
_RlCopyHistoryRowStatus_Type = RowStatus
_RlCopyHistoryRowStatus_Object = MibTableColumn
rlCopyHistoryRowStatus = _RlCopyHistoryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 17),
    _RlCopyHistoryRowStatus_Type()
)
rlCopyHistoryRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyHistoryRowStatus.setStatus("current")
_RlCopyHistoryErrorMessage_Type = DisplayString
_RlCopyHistoryErrorMessage_Object = MibTableColumn
rlCopyHistoryErrorMessage = _RlCopyHistoryErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 18),
    _RlCopyHistoryErrorMessage_Type()
)
rlCopyHistoryErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyHistoryErrorMessage.setStatus("current")


class _RlCopyAuditingEnable_Type(TruthValue):
    """Custom type rlCopyAuditingEnable based on TruthValue"""
    defaultValue = 1


_RlCopyAuditingEnable_Type.__name__ = "TruthValue"
_RlCopyAuditingEnable_Object = MibScalar
rlCopyAuditingEnable = _RlCopyAuditingEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 5),
    _RlCopyAuditingEnable_Type()
)
rlCopyAuditingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyAuditingEnable.setStatus("current")
_RlCopyMessagesTable_Object = MibTable
rlCopyMessagesTable = _RlCopyMessagesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 6)
)
if mibBuilder.loadTexts:
    rlCopyMessagesTable.setStatus("current")
_RlCopyMessagesEntry_Object = MibTableRow
rlCopyMessagesEntry = _RlCopyMessagesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 6, 1)
)
rlCopyMessagesEntry.setIndexNames(
    (0, "RADLAN-COPY-MIB", "rlCopyMessagesCopyIndex"),
    (0, "RADLAN-COPY-MIB", "rlCopyMessagesMessageIndex"),
)
if mibBuilder.loadTexts:
    rlCopyMessagesEntry.setStatus("current")


class _RlCopyMessagesCopyIndex_Type(Integer32):
    """Custom type rlCopyMessagesCopyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlCopyMessagesCopyIndex_Type.__name__ = "Integer32"
_RlCopyMessagesCopyIndex_Object = MibTableColumn
rlCopyMessagesCopyIndex = _RlCopyMessagesCopyIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 6, 1, 1),
    _RlCopyMessagesCopyIndex_Type()
)
rlCopyMessagesCopyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCopyMessagesCopyIndex.setStatus("current")


class _RlCopyMessagesMessageIndex_Type(Integer32):
    """Custom type rlCopyMessagesMessageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlCopyMessagesMessageIndex_Type.__name__ = "Integer32"
_RlCopyMessagesMessageIndex_Object = MibTableColumn
rlCopyMessagesMessageIndex = _RlCopyMessagesMessageIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 6, 1, 2),
    _RlCopyMessagesMessageIndex_Type()
)
rlCopyMessagesMessageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCopyMessagesMessageIndex.setStatus("current")


class _RlCopyMessagesMessageText_Type(DisplayString):
    """Custom type rlCopyMessagesMessageText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RlCopyMessagesMessageText_Type.__name__ = "DisplayString"
_RlCopyMessagesMessageText_Object = MibTableColumn
rlCopyMessagesMessageText = _RlCopyMessagesMessageText_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 6, 1, 3),
    _RlCopyMessagesMessageText_Type()
)
rlCopyMessagesMessageText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCopyMessagesMessageText.setStatus("current")
_RlCopyMessagesStatus_Type = RowStatus
_RlCopyMessagesStatus_Object = MibTableColumn
rlCopyMessagesStatus = _RlCopyMessagesStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 6, 1, 4),
    _RlCopyMessagesStatus_Type()
)
rlCopyMessagesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyMessagesStatus.setStatus("current")
_RlCopyMessagesTableRemoveEntries_Type = Integer32
_RlCopyMessagesTableRemoveEntries_Object = MibScalar
rlCopyMessagesTableRemoveEntries = _RlCopyMessagesTableRemoveEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 87, 7),
    _RlCopyMessagesTableRemoveEntries_Type()
)
rlCopyMessagesTableRemoveEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCopyMessagesTableRemoveEntries.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-COPY-MIB",
    **{"RlCopyApplicationType": RlCopyApplicationType,
       "RlCopyLocationType": RlCopyLocationType,
       "RlCopyFileType": RlCopyFileType,
       "rlCopy": rlCopy,
       "rlCopyMibVersion": rlCopyMibVersion,
       "rlCopyTable": rlCopyTable,
       "rlCopyEntry": rlCopyEntry,
       "rlCopyIndex": rlCopyIndex,
       "rlCopyApplicationId": rlCopyApplicationId,
       "rlCopySourceLocation": rlCopySourceLocation,
       "rlCopySourceIpAddress": rlCopySourceIpAddress,
       "rlCopySourceUnitNumber": rlCopySourceUnitNumber,
       "rlCopySourceFileName": rlCopySourceFileName,
       "rlCopySourceFileType": rlCopySourceFileType,
       "rlCopyDestinationLocation": rlCopyDestinationLocation,
       "rlCopyDestinationIpAddress": rlCopyDestinationIpAddress,
       "rlCopyDestinationUnitNumber": rlCopyDestinationUnitNumber,
       "rlCopyDestinationFileName": rlCopyDestinationFileName,
       "rlCopyDestinationFileType": rlCopyDestinationFileType,
       "rlCopyUpTime": rlCopyUpTime,
       "rlCopyOperationState": rlCopyOperationState,
       "rlCopyBytesTransferred": rlCopyBytesTransferred,
       "rlCopyInBackground": rlCopyInBackground,
       "rlCopyRowStatus": rlCopyRowStatus,
       "rlCopyHistoryIndex": rlCopyHistoryIndex,
       "rlCopyFreeHistoryIndex": rlCopyFreeHistoryIndex,
       "rlCopyHistoryTable": rlCopyHistoryTable,
       "rlCopyHistoryEntry": rlCopyHistoryEntry,
       "rlCopyHistoryHistoryIndex": rlCopyHistoryHistoryIndex,
       "rlCopyHistoryApplicationId": rlCopyHistoryApplicationId,
       "rlCopyHistorySourceLocation": rlCopyHistorySourceLocation,
       "rlCopyHistorySourceIpAddress": rlCopyHistorySourceIpAddress,
       "rlCopyHistorySourceUnitNumber": rlCopyHistorySourceUnitNumber,
       "rlCopyHistorySourceFileName": rlCopyHistorySourceFileName,
       "rlCopyHistorySourceFileType": rlCopyHistorySourceFileType,
       "rlCopyHistoryDestinationLocation": rlCopyHistoryDestinationLocation,
       "rlCopyHistoryDestinationIpAddress": rlCopyHistoryDestinationIpAddress,
       "rlCopyHistoryDestinationUnitNumber": rlCopyHistoryDestinationUnitNumber,
       "rlCopyHistoryDestinationFileName": rlCopyHistoryDestinationFileName,
       "rlCopyHistoryDestinationFileType": rlCopyHistoryDestinationFileType,
       "rlCopyHistoryUpTime": rlCopyHistoryUpTime,
       "rlCopyHistoryOperationState": rlCopyHistoryOperationState,
       "rlCopyHistoryBytesTransferred": rlCopyHistoryBytesTransferred,
       "rlCopyHistoryInBackground": rlCopyHistoryInBackground,
       "rlCopyHistoryRowStatus": rlCopyHistoryRowStatus,
       "rlCopyHistoryErrorMessage": rlCopyHistoryErrorMessage,
       "rlCopyAuditingEnable": rlCopyAuditingEnable,
       "rlCopyMessagesTable": rlCopyMessagesTable,
       "rlCopyMessagesEntry": rlCopyMessagesEntry,
       "rlCopyMessagesCopyIndex": rlCopyMessagesCopyIndex,
       "rlCopyMessagesMessageIndex": rlCopyMessagesMessageIndex,
       "rlCopyMessagesMessageText": rlCopyMessagesMessageText,
       "rlCopyMessagesStatus": rlCopyMessagesStatus,
       "rlCopyMessagesTableRemoveEntries": rlCopyMessagesTableRemoveEntries}
)
