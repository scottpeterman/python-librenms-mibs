# SNMP MIB module (FORCE10-COPY-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\FORCE10-COPY-CONFIG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:10 2025
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

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

f10CopyConfigMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5)
)
if mibBuilder.loadTexts:
    f10CopyConfigMib.setRevisions(
        ("2009-05-14 13:00",
         "2007-06-19 12:00",
         "2003-03-01 12:00")
    )


# Types definitions



class F10ConfigFileLocation(Integer32):
    """Custom type F10ConfigFileLocation based on Integer32"""
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
        *(("flash", 1),
          ("slot0", 2),
          ("tftp", 3),
          ("ftp", 4),
          ("scp", 5),
          ("usbflash", 6))
    )





class F10ConfigFileType(Integer32):
    """Custom type F10ConfigFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftosFile", 1),
          ("runningConfig", 2),
          ("startupConfig", 3))
    )





class F10ConfigCopyState(Integer32):
    """Custom type F10ConfigCopyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("successful", 2),
          ("failed", 3))
    )





class F10ConfigCopyFailCause(Integer32):
    """Custom type F10ConfigCopyFailCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("badFileName", 1),
          ("copyInProgress", 2),
          ("diskFull", 3),
          ("fileExist", 4),
          ("fileNotFound", 5),
          ("timeout", 6),
          ("unknown", 7))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F10CopyConfigObjects_ObjectIdentity = ObjectIdentity
f10CopyConfigObjects = _F10CopyConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1)
)
_F10CopyConfig_ObjectIdentity = ObjectIdentity
f10CopyConfig = _F10CopyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1)
)
_F10CopyTable_Object = MibTable
f10CopyTable = _F10CopyTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    f10CopyTable.setStatus("current")
_F10CopyEntry_Object = MibTableRow
f10CopyEntry = _F10CopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1)
)
f10CopyEntry.setIndexNames(
    (0, "FORCE10-COPY-CONFIG-MIB", "copyConfigIndex"),
)
if mibBuilder.loadTexts:
    f10CopyEntry.setStatus("current")
_CopyConfigIndex_Type = Integer32
_CopyConfigIndex_Object = MibTableColumn
copyConfigIndex = _CopyConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 1),
    _CopyConfigIndex_Type()
)
copyConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    copyConfigIndex.setStatus("current")
_CopySrcFileType_Type = F10ConfigFileType
_CopySrcFileType_Object = MibTableColumn
copySrcFileType = _CopySrcFileType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 2),
    _CopySrcFileType_Type()
)
copySrcFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copySrcFileType.setStatus("current")
_CopySrcFileLocation_Type = F10ConfigFileLocation
_CopySrcFileLocation_Object = MibTableColumn
copySrcFileLocation = _CopySrcFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 3),
    _CopySrcFileLocation_Type()
)
copySrcFileLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copySrcFileLocation.setStatus("current")
_CopySrcFileName_Type = DisplayString
_CopySrcFileName_Object = MibTableColumn
copySrcFileName = _CopySrcFileName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 4),
    _CopySrcFileName_Type()
)
copySrcFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copySrcFileName.setStatus("current")
_CopyDestFileType_Type = F10ConfigFileType
_CopyDestFileType_Object = MibTableColumn
copyDestFileType = _CopyDestFileType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 5),
    _CopyDestFileType_Type()
)
copyDestFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copyDestFileType.setStatus("current")
_CopyDestFileLocation_Type = F10ConfigFileLocation
_CopyDestFileLocation_Object = MibTableColumn
copyDestFileLocation = _CopyDestFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 6),
    _CopyDestFileLocation_Type()
)
copyDestFileLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copyDestFileLocation.setStatus("current")
_CopyDestFileName_Type = DisplayString
_CopyDestFileName_Object = MibTableColumn
copyDestFileName = _CopyDestFileName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 7),
    _CopyDestFileName_Type()
)
copyDestFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copyDestFileName.setStatus("current")
_CopyServerAddress_Type = IpAddress
_CopyServerAddress_Object = MibTableColumn
copyServerAddress = _CopyServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 8),
    _CopyServerAddress_Type()
)
copyServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copyServerAddress.setStatus("current")


class _CopyUserName_Type(DisplayString):
    """Custom type copyUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CopyUserName_Type.__name__ = "DisplayString"
_CopyUserName_Object = MibTableColumn
copyUserName = _CopyUserName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 9),
    _CopyUserName_Type()
)
copyUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copyUserName.setStatus("current")


class _CopyUserPassword_Type(DisplayString):
    """Custom type copyUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CopyUserPassword_Type.__name__ = "DisplayString"
_CopyUserPassword_Object = MibTableColumn
copyUserPassword = _CopyUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 10),
    _CopyUserPassword_Type()
)
copyUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copyUserPassword.setStatus("current")
_CopyState_Type = F10ConfigCopyState
_CopyState_Object = MibTableColumn
copyState = _CopyState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 11),
    _CopyState_Type()
)
copyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyState.setStatus("current")
_CopyTimeStarted_Type = TimeTicks
_CopyTimeStarted_Object = MibTableColumn
copyTimeStarted = _CopyTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 12),
    _CopyTimeStarted_Type()
)
copyTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyTimeStarted.setStatus("current")
_CopyTimeCompleted_Type = TimeTicks
_CopyTimeCompleted_Object = MibTableColumn
copyTimeCompleted = _CopyTimeCompleted_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 13),
    _CopyTimeCompleted_Type()
)
copyTimeCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyTimeCompleted.setStatus("current")
_CopyFailCause_Type = F10ConfigCopyFailCause
_CopyFailCause_Object = MibTableColumn
copyFailCause = _CopyFailCause_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 14),
    _CopyFailCause_Type()
)
copyFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyFailCause.setStatus("current")
_CopyEntryRowStatus_Type = RowStatus
_CopyEntryRowStatus_Object = MibTableColumn
copyEntryRowStatus = _CopyEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 15),
    _CopyEntryRowStatus_Type()
)
copyEntryRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copyEntryRowStatus.setStatus("current")
_F10CopyConfigTraps_ObjectIdentity = ObjectIdentity
f10CopyConfigTraps = _F10CopyConfigTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 2)
)
_CopyAlarmMibNotifications_ObjectIdentity = ObjectIdentity
copyAlarmMibNotifications = _CopyAlarmMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 2, 0)
)
_CopyAlarmVariable_ObjectIdentity = ObjectIdentity
copyAlarmVariable = _CopyAlarmVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 2, 1)
)
_CopyAlarmLevel_Type = Integer32
_CopyAlarmLevel_Object = MibScalar
copyAlarmLevel = _CopyAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 2, 1, 1),
    _CopyAlarmLevel_Type()
)
copyAlarmLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    copyAlarmLevel.setStatus("current")
_CopyAlarmString_Type = OctetString
_CopyAlarmString_Object = MibScalar
copyAlarmString = _CopyAlarmString_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 2, 1, 2),
    _CopyAlarmString_Type()
)
copyAlarmString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    copyAlarmString.setStatus("current")
_CopyAlarmIndex_Type = Integer32
_CopyAlarmIndex_Object = MibScalar
copyAlarmIndex = _CopyAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 2, 1, 3),
    _CopyAlarmIndex_Type()
)
copyAlarmIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    copyAlarmIndex.setStatus("current")

# Managed Objects groups


# Notification objects

copyConfigCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 2, 0, 1)
)
copyConfigCompleted.setObjects(
      *(("FORCE10-COPY-CONFIG-MIB", "copyAlarmLevel"),
        ("FORCE10-COPY-CONFIG-MIB", "copyAlarmString"),
        ("FORCE10-COPY-CONFIG-MIB", "copyAlarmIndex"))
)
if mibBuilder.loadTexts:
    copyConfigCompleted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORCE10-COPY-CONFIG-MIB",
    **{"F10ConfigFileLocation": F10ConfigFileLocation,
       "F10ConfigFileType": F10ConfigFileType,
       "F10ConfigCopyState": F10ConfigCopyState,
       "F10ConfigCopyFailCause": F10ConfigCopyFailCause,
       "f10CopyConfigMib": f10CopyConfigMib,
       "f10CopyConfigObjects": f10CopyConfigObjects,
       "f10CopyConfig": f10CopyConfig,
       "f10CopyTable": f10CopyTable,
       "f10CopyEntry": f10CopyEntry,
       "copyConfigIndex": copyConfigIndex,
       "copySrcFileType": copySrcFileType,
       "copySrcFileLocation": copySrcFileLocation,
       "copySrcFileName": copySrcFileName,
       "copyDestFileType": copyDestFileType,
       "copyDestFileLocation": copyDestFileLocation,
       "copyDestFileName": copyDestFileName,
       "copyServerAddress": copyServerAddress,
       "copyUserName": copyUserName,
       "copyUserPassword": copyUserPassword,
       "copyState": copyState,
       "copyTimeStarted": copyTimeStarted,
       "copyTimeCompleted": copyTimeCompleted,
       "copyFailCause": copyFailCause,
       "copyEntryRowStatus": copyEntryRowStatus,
       "f10CopyConfigTraps": f10CopyConfigTraps,
       "copyAlarmMibNotifications": copyAlarmMibNotifications,
       "copyConfigCompleted": copyConfigCompleted,
       "copyAlarmVariable": copyAlarmVariable,
       "copyAlarmLevel": copyAlarmLevel,
       "copyAlarmString": copyAlarmString,
       "copyAlarmIndex": copyAlarmIndex}
)
