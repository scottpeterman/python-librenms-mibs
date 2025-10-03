# SNMP MIB module (EXTREME-FILETRANSFER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\extreme\EXTREME-FILETRANSFER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:28 2025
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

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
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

extremeFileTransfer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeFileTransferGroup_ObjectIdentity = ObjectIdentity
extremeFileTransferGroup = _ExtremeFileTransferGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 10, 1)
)
_ExtremeFileTransferNextAvailableIndex_Type = TestAndIncr
_ExtremeFileTransferNextAvailableIndex_Object = MibScalar
extremeFileTransferNextAvailableIndex = _ExtremeFileTransferNextAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 10, 1, 1),
    _ExtremeFileTransferNextAvailableIndex_Type()
)
extremeFileTransferNextAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeFileTransferNextAvailableIndex.setStatus("current")
_ExtremeFileTransferTable_Object = MibTable
extremeFileTransferTable = _ExtremeFileTransferTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 10, 1, 2)
)
if mibBuilder.loadTexts:
    extremeFileTransferTable.setStatus("current")
_ExtremeFileTransferEntry_Object = MibTableRow
extremeFileTransferEntry = _ExtremeFileTransferEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 10, 1, 2, 1)
)
extremeFileTransferEntry.setIndexNames(
    (0, "EXTREME-FILETRANSFER-MIB", "extremeFileTransferIndex"),
)
if mibBuilder.loadTexts:
    extremeFileTransferEntry.setStatus("current")
_ExtremeFileTransferIndex_Type = Integer32
_ExtremeFileTransferIndex_Object = MibTableColumn
extremeFileTransferIndex = _ExtremeFileTransferIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 10, 1, 2, 1, 1),
    _ExtremeFileTransferIndex_Type()
)
extremeFileTransferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeFileTransferIndex.setStatus("current")
_ExtremeFileTransferServerAddress_Type = IpAddress
_ExtremeFileTransferServerAddress_Object = MibTableColumn
extremeFileTransferServerAddress = _ExtremeFileTransferServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 10, 1, 2, 1, 2),
    _ExtremeFileTransferServerAddress_Type()
)
extremeFileTransferServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeFileTransferServerAddress.setStatus("current")


class _ExtremeFileTransferFileName_Type(DisplayString):
    """Custom type extremeFileTransferFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ExtremeFileTransferFileName_Type.__name__ = "DisplayString"
_ExtremeFileTransferFileName_Object = MibTableColumn
extremeFileTransferFileName = _ExtremeFileTransferFileName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 10, 1, 2, 1, 3),
    _ExtremeFileTransferFileName_Type()
)
extremeFileTransferFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeFileTransferFileName.setStatus("current")


class _ExtremeFileTransferOperation_Type(Integer32):
    """Custom type extremeFileTransferOperation based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("downloadImageToPrimaryImmediate", 1),
          ("downloadImageToSecondaryImmediate", 2),
          ("downloadConfigImmediate", 3),
          ("uploadConfigImmediate", 4),
          ("scheduleConfigUploadPeriodic", 5),
          ("scheduleConfigUploadOnce", 6),
          ("scheduleImageDownloadToPrimaryOnce", 7),
          ("scheduleImageDownloadToSecondaryOnce", 8),
          ("scheduleConfigDownloadOnce", 9))
    )


_ExtremeFileTransferOperation_Type.__name__ = "Integer32"
_ExtremeFileTransferOperation_Object = MibTableColumn
extremeFileTransferOperation = _ExtremeFileTransferOperation_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 10, 1, 2, 1, 4),
    _ExtremeFileTransferOperation_Type()
)
extremeFileTransferOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeFileTransferOperation.setStatus("current")


class _ExtremeFileTransferScheduledTime_Type(OctetString):
    """Custom type extremeFileTransferScheduledTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )


_ExtremeFileTransferScheduledTime_Type.__name__ = "OctetString"
_ExtremeFileTransferScheduledTime_Object = MibTableColumn
extremeFileTransferScheduledTime = _ExtremeFileTransferScheduledTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 10, 1, 2, 1, 5),
    _ExtremeFileTransferScheduledTime_Type()
)
extremeFileTransferScheduledTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeFileTransferScheduledTime.setStatus("current")


class _ExtremeFileTransferStartAdminStatus_Type(Integer32):
    """Custom type extremeFileTransferStartAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("cancel", 2))
    )


_ExtremeFileTransferStartAdminStatus_Type.__name__ = "Integer32"
_ExtremeFileTransferStartAdminStatus_Object = MibTableColumn
extremeFileTransferStartAdminStatus = _ExtremeFileTransferStartAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 10, 1, 2, 1, 6),
    _ExtremeFileTransferStartAdminStatus_Type()
)
extremeFileTransferStartAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeFileTransferStartAdminStatus.setStatus("current")


class _ExtremeFileTransferStartOperStatus_Type(Integer32):
    """Custom type extremeFileTransferStartOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("scheduled", 2),
          ("inProgress", 3))
    )


_ExtremeFileTransferStartOperStatus_Type.__name__ = "Integer32"
_ExtremeFileTransferStartOperStatus_Object = MibTableColumn
extremeFileTransferStartOperStatus = _ExtremeFileTransferStartOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 10, 1, 2, 1, 7),
    _ExtremeFileTransferStartOperStatus_Type()
)
extremeFileTransferStartOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeFileTransferStartOperStatus.setStatus("current")


class _ExtremeFileTransferLastExecutionStatus_Type(Integer32):
    """Custom type extremeFileTransferLastExecutionStatus based on Integer32"""
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
        *(("success", 1),
          ("statusUnknown", 2),
          ("generalError", 3),
          ("noResponseFromServer", 4),
          ("checksumError", 5),
          ("incompatibleImage", 6),
          ("tftpFileNotFound", 7),
          ("tftpAccessViolation", 8),
          ("fileTooLarge", 9),
          ("downloadInProgress", 10))
    )


_ExtremeFileTransferLastExecutionStatus_Type.__name__ = "Integer32"
_ExtremeFileTransferLastExecutionStatus_Object = MibTableColumn
extremeFileTransferLastExecutionStatus = _ExtremeFileTransferLastExecutionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 10, 1, 2, 1, 8),
    _ExtremeFileTransferLastExecutionStatus_Type()
)
extremeFileTransferLastExecutionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeFileTransferLastExecutionStatus.setStatus("current")


class _ExtremeFileTransferOwner_Type(OwnerString):
    """Custom type extremeFileTransferOwner based on OwnerString"""
    subtypeSpec = OwnerString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeFileTransferOwner_Type.__name__ = "OwnerString"
_ExtremeFileTransferOwner_Object = MibTableColumn
extremeFileTransferOwner = _ExtremeFileTransferOwner_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 10, 1, 2, 1, 9),
    _ExtremeFileTransferOwner_Type()
)
extremeFileTransferOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeFileTransferOwner.setStatus("current")
_ExtremeFileTransferRowStatus_Type = RowStatus
_ExtremeFileTransferRowStatus_Object = MibTableColumn
extremeFileTransferRowStatus = _ExtremeFileTransferRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 10, 1, 2, 1, 10),
    _ExtremeFileTransferRowStatus_Type()
)
extremeFileTransferRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeFileTransferRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-FILETRANSFER-MIB",
    **{"extremeFileTransfer": extremeFileTransfer,
       "extremeFileTransferGroup": extremeFileTransferGroup,
       "extremeFileTransferNextAvailableIndex": extremeFileTransferNextAvailableIndex,
       "extremeFileTransferTable": extremeFileTransferTable,
       "extremeFileTransferEntry": extremeFileTransferEntry,
       "extremeFileTransferIndex": extremeFileTransferIndex,
       "extremeFileTransferServerAddress": extremeFileTransferServerAddress,
       "extremeFileTransferFileName": extremeFileTransferFileName,
       "extremeFileTransferOperation": extremeFileTransferOperation,
       "extremeFileTransferScheduledTime": extremeFileTransferScheduledTime,
       "extremeFileTransferStartAdminStatus": extremeFileTransferStartAdminStatus,
       "extremeFileTransferStartOperStatus": extremeFileTransferStartOperStatus,
       "extremeFileTransferLastExecutionStatus": extremeFileTransferLastExecutionStatus,
       "extremeFileTransferOwner": extremeFileTransferOwner,
       "extremeFileTransferRowStatus": extremeFileTransferRowStatus}
)
