# SNMP MIB module (ADVANTECH-EKI-PRONEER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\advantech\ADVANTECH-EKI-PRONEER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:04 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

advantech = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10297)
)
if mibBuilder.loadTexts:
    advantech.setRevisions(
        ("2014-12-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ASwitchMIB_ObjectIdentity = ObjectIdentity
aSwitchMIB = _ASwitchMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202)
)
_Proneer_ObjectIdentity = ObjectIdentity
proneer = _Proneer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000)
)
_Monitoring_ObjectIdentity = ObjectIdentity
monitoring = _Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1)
)
_DeviceInfo_ObjectIdentity = ObjectIdentity
deviceInfo = _DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1)
)


class _SystemName_Type(DisplayString):
    """Custom type systemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SystemName_Type.__name__ = "DisplayString"
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 1),
    _SystemName_Type()
)
systemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemName.setStatus("current")


class _SystemLocation_Type(DisplayString):
    """Custom type systemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemLocation_Type.__name__ = "DisplayString"
_SystemLocation_Object = MibScalar
systemLocation = _SystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 2),
    _SystemLocation_Type()
)
systemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLocation.setStatus("current")


class _SystemContact_Type(DisplayString):
    """Custom type systemContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemContact_Type.__name__ = "DisplayString"
_SystemContact_Object = MibScalar
systemContact = _SystemContact_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 3),
    _SystemContact_Type()
)
systemContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemContact.setStatus("current")
_MacAddress_Type = DisplayString
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 4),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_IpAddress_Type = IpAddress
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 5),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 6),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_Gateway_Type = IpAddress
_Gateway_Object = MibScalar
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 7),
    _Gateway_Type()
)
gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gateway.setStatus("current")
_LoaderVersion_Type = DisplayString
_LoaderVersion_Object = MibScalar
loaderVersion = _LoaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 8),
    _LoaderVersion_Type()
)
loaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loaderVersion.setStatus("current")
_LoaderDate_Type = DisplayString
_LoaderDate_Object = MibScalar
loaderDate = _LoaderDate_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 9),
    _LoaderDate_Type()
)
loaderDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loaderDate.setStatus("current")
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 10),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_FirmwareDate_Type = DisplayString
_FirmwareDate_Object = MibScalar
firmwareDate = _FirmwareDate_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 11),
    _FirmwareDate_Type()
)
firmwareDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareDate.setStatus("current")
_SystemObjectID_Type = ObjectIdentifier
_SystemObjectID_Object = MibScalar
systemObjectID = _SystemObjectID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 12),
    _SystemObjectID_Type()
)
systemObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemObjectID.setStatus("current")
_SystemUpTime_Type = TimeTicks
_SystemUpTime_Object = MibScalar
systemUpTime = _SystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 13),
    _SystemUpTime_Type()
)
systemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpTime.setStatus("current")
_LedStatus_ObjectIdentity = ObjectIdentity
ledStatus = _LedStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 14)
)


class _LedSYSStatus_Type(Integer32):
    """Custom type ledSYSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("up", 1),
          ("down", 2))
    )


_LedSYSStatus_Type.__name__ = "Integer32"
_LedSYSStatus_Object = MibScalar
ledSYSStatus = _LedSYSStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 14, 1),
    _LedSYSStatus_Type()
)
ledSYSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledSYSStatus.setStatus("current")


class _LedRMStatus_Type(Integer32):
    """Custom type ledRMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("up", 1),
          ("down", 2))
    )


_LedRMStatus_Type.__name__ = "Integer32"
_LedRMStatus_Object = MibScalar
ledRMStatus = _LedRMStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 14, 2),
    _LedRMStatus_Type()
)
ledRMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledRMStatus.setStatus("current")


class _LedPWR1Status_Type(Integer32):
    """Custom type ledPWR1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("up", 1),
          ("down", 2))
    )


_LedPWR1Status_Type.__name__ = "Integer32"
_LedPWR1Status_Object = MibScalar
ledPWR1Status = _LedPWR1Status_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 14, 3),
    _LedPWR1Status_Type()
)
ledPWR1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledPWR1Status.setStatus("current")


class _LedPWR2Status_Type(Integer32):
    """Custom type ledPWR2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("up", 1),
          ("down", 2))
    )


_LedPWR2Status_Type.__name__ = "Integer32"
_LedPWR2Status_Object = MibScalar
ledPWR2Status = _LedPWR2Status_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 14, 4),
    _LedPWR2Status_Type()
)
ledPWR2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledPWR2Status.setStatus("current")


class _LedAlarmStatus_Type(Integer32):
    """Custom type ledAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("up", 1),
          ("down", 2))
    )


_LedAlarmStatus_Type.__name__ = "Integer32"
_LedAlarmStatus_Object = MibScalar
ledAlarmStatus = _LedAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 14, 5),
    _LedAlarmStatus_Type()
)
ledAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledAlarmStatus.setStatus("current")


class _LedPFAILStatus_Type(Integer32):
    """Custom type ledPFAILStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("up", 1),
          ("down", 2))
    )


_LedPFAILStatus_Type.__name__ = "Integer32"
_LedPFAILStatus_Object = MibScalar
ledPFAILStatus = _LedPFAILStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 14, 6),
    _LedPFAILStatus_Type()
)
ledPFAILStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledPFAILStatus.setStatus("current")


class _LedRFAILStatus_Type(Integer32):
    """Custom type ledRFAILStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("up", 1),
          ("down", 2))
    )


_LedRFAILStatus_Type.__name__ = "Integer32"
_LedRFAILStatus_Object = MibScalar
ledRFAILStatus = _LedRFAILStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 14, 7),
    _LedRFAILStatus_Type()
)
ledRFAILStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledRFAILStatus.setStatus("current")


class _LedLOOPStatus_Type(Integer32):
    """Custom type ledLOOPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("up", 1),
          ("down", 2))
    )


_LedLOOPStatus_Type.__name__ = "Integer32"
_LedLOOPStatus_Object = MibScalar
ledLOOPStatus = _LedLOOPStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 14, 8),
    _LedLOOPStatus_Type()
)
ledLOOPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledLOOPStatus.setStatus("current")


class _LedTempStatus_Type(Integer32):
    """Custom type ledTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("up", 1),
          ("down", 2))
    )


_LedTempStatus_Type.__name__ = "Integer32"
_LedTempStatus_Object = MibScalar
ledTempStatus = _LedTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 14, 9),
    _LedTempStatus_Type()
)
ledTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledTempStatus.setStatus("current")
_BuildVersion_Type = DisplayString
_BuildVersion_Object = MibScalar
buildVersion = _BuildVersion_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 1, 15),
    _BuildVersion_Type()
)
buildVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buildVersion.setStatus("current")
_LoggingMessage_ObjectIdentity = ObjectIdentity
loggingMessage = _LoggingMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 2)
)
_LoggingBufferTable_Object = MibTable
loggingBufferTable = _LoggingBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 2, 1)
)
if mibBuilder.loadTexts:
    loggingBufferTable.setStatus("current")
_LoggingBufferEntry_Object = MibTableRow
loggingBufferEntry = _LoggingBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 2, 1, 1)
)
loggingBufferEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "loggingBufferIndex"),
)
if mibBuilder.loadTexts:
    loggingBufferEntry.setStatus("current")


class _LoggingBufferIndex_Type(Integer32):
    """Custom type loggingBufferIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LoggingBufferIndex_Type.__name__ = "Integer32"
_LoggingBufferIndex_Object = MibTableColumn
loggingBufferIndex = _LoggingBufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 2, 1, 1, 1),
    _LoggingBufferIndex_Type()
)
loggingBufferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loggingBufferIndex.setStatus("current")


class _LoggingBufferSeverity_Type(Integer32):
    """Custom type loggingBufferSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("emerg", 0),
          ("alert", 1),
          ("crit", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_LoggingBufferSeverity_Type.__name__ = "Integer32"
_LoggingBufferSeverity_Object = MibTableColumn
loggingBufferSeverity = _LoggingBufferSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 2, 1, 1, 2),
    _LoggingBufferSeverity_Type()
)
loggingBufferSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingBufferSeverity.setStatus("current")
_LoggingBufferCategory_Type = DisplayString
_LoggingBufferCategory_Object = MibTableColumn
loggingBufferCategory = _LoggingBufferCategory_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 2, 1, 1, 3),
    _LoggingBufferCategory_Type()
)
loggingBufferCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingBufferCategory.setStatus("current")
_LoggingBufferTimeStamp_Type = DisplayString
_LoggingBufferTimeStamp_Object = MibTableColumn
loggingBufferTimeStamp = _LoggingBufferTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 2, 1, 1, 4),
    _LoggingBufferTimeStamp_Type()
)
loggingBufferTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingBufferTimeStamp.setStatus("current")
_LoggingBufferMessage_Type = DisplayString
_LoggingBufferMessage_Object = MibTableColumn
loggingBufferMessage = _LoggingBufferMessage_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 2, 1, 1, 5),
    _LoggingBufferMessage_Type()
)
loggingBufferMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingBufferMessage.setStatus("current")


class _ClearBufferedMsg_Type(Integer32):
    """Custom type clearBufferedMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_ClearBufferedMsg_Type.__name__ = "Integer32"
_ClearBufferedMsg_Object = MibScalar
clearBufferedMsg = _ClearBufferedMsg_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 2, 2),
    _ClearBufferedMsg_Type()
)
clearBufferedMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearBufferedMsg.setStatus("current")
_LoggingFileTable_Object = MibTable
loggingFileTable = _LoggingFileTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 2, 3)
)
if mibBuilder.loadTexts:
    loggingFileTable.setStatus("current")
_LoggingFileEntry_Object = MibTableRow
loggingFileEntry = _LoggingFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 2, 3, 1)
)
loggingFileEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "loggingFileIndex"),
)
if mibBuilder.loadTexts:
    loggingFileEntry.setStatus("current")


class _LoggingFileIndex_Type(Integer32):
    """Custom type loggingFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LoggingFileIndex_Type.__name__ = "Integer32"
_LoggingFileIndex_Object = MibTableColumn
loggingFileIndex = _LoggingFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 2, 3, 1, 1),
    _LoggingFileIndex_Type()
)
loggingFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loggingFileIndex.setStatus("current")


class _LoggingFileSeverity_Type(Integer32):
    """Custom type loggingFileSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("emerg", 0),
          ("alert", 1),
          ("crit", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_LoggingFileSeverity_Type.__name__ = "Integer32"
_LoggingFileSeverity_Object = MibTableColumn
loggingFileSeverity = _LoggingFileSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 2, 3, 1, 2),
    _LoggingFileSeverity_Type()
)
loggingFileSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingFileSeverity.setStatus("current")
_LoggingFileCategory_Type = DisplayString
_LoggingFileCategory_Object = MibTableColumn
loggingFileCategory = _LoggingFileCategory_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 2, 3, 1, 3),
    _LoggingFileCategory_Type()
)
loggingFileCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingFileCategory.setStatus("current")
_LoggingFileTimeStamp_Type = DisplayString
_LoggingFileTimeStamp_Object = MibTableColumn
loggingFileTimeStamp = _LoggingFileTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 2, 3, 1, 4),
    _LoggingFileTimeStamp_Type()
)
loggingFileTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingFileTimeStamp.setStatus("current")
_LoggingFileMessage_Type = DisplayString
_LoggingFileMessage_Object = MibTableColumn
loggingFileMessage = _LoggingFileMessage_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 2, 3, 1, 5),
    _LoggingFileMessage_Type()
)
loggingFileMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingFileMessage.setStatus("current")


class _ClearFileMsg_Type(Integer32):
    """Custom type clearFileMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_ClearFileMsg_Type.__name__ = "Integer32"
_ClearFileMsg_Object = MibScalar
clearFileMsg = _ClearFileMsg_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 2, 4),
    _ClearFileMsg_Type()
)
clearFileMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearFileMsg.setStatus("current")
_PortMonitoring_ObjectIdentity = ObjectIdentity
portMonitoring = _PortMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3)
)
_PortStatisticTable_Object = MibTable
portStatisticTable = _PortStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1)
)
if mibBuilder.loadTexts:
    portStatisticTable.setStatus("current")
_PortStatisticEntry_Object = MibTableRow
portStatisticEntry = _PortStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1)
)
portStatisticEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "portStatisticIndex"),
)
if mibBuilder.loadTexts:
    portStatisticEntry.setStatus("current")


class _PortStatisticIndex_Type(Integer32):
    """Custom type portStatisticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortStatisticIndex_Type.__name__ = "Integer32"
_PortStatisticIndex_Object = MibTableColumn
portStatisticIndex = _PortStatisticIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 1),
    _PortStatisticIndex_Type()
)
portStatisticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatisticIndex.setStatus("current")


class _PortCounterClear_Type(Integer32):
    """Custom type portCounterClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("clear", 1))
    )


_PortCounterClear_Type.__name__ = "Integer32"
_PortCounterClear_Object = MibTableColumn
portCounterClear = _PortCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 2),
    _PortCounterClear_Type()
)
portCounterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCounterClear.setStatus("current")
_IfInOctets_Type = Integer32
_IfInOctets_Object = MibTableColumn
ifInOctets = _IfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 3),
    _IfInOctets_Type()
)
ifInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInOctets.setStatus("current")
_IfInUcastPkts_Type = Integer32
_IfInUcastPkts_Object = MibTableColumn
ifInUcastPkts = _IfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 4),
    _IfInUcastPkts_Type()
)
ifInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInUcastPkts.setStatus("current")
_IfInNUcastPkts_Type = Integer32
_IfInNUcastPkts_Object = MibTableColumn
ifInNUcastPkts = _IfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 5),
    _IfInNUcastPkts_Type()
)
ifInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInNUcastPkts.setStatus("current")
_IfInDiscards_Type = Integer32
_IfInDiscards_Object = MibTableColumn
ifInDiscards = _IfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 6),
    _IfInDiscards_Type()
)
ifInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInDiscards.setStatus("current")
_IfOutOctets_Type = Integer32
_IfOutOctets_Object = MibTableColumn
ifOutOctets = _IfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 7),
    _IfOutOctets_Type()
)
ifOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutOctets.setStatus("current")
_IfOutUcastPkts_Type = Integer32
_IfOutUcastPkts_Object = MibTableColumn
ifOutUcastPkts = _IfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 8),
    _IfOutUcastPkts_Type()
)
ifOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutUcastPkts.setStatus("current")
_IfOutNUcastPkts_Type = Integer32
_IfOutNUcastPkts_Object = MibTableColumn
ifOutNUcastPkts = _IfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 9),
    _IfOutNUcastPkts_Type()
)
ifOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutNUcastPkts.setStatus("current")
_IfOutDiscards_Type = Integer32
_IfOutDiscards_Object = MibTableColumn
ifOutDiscards = _IfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 10),
    _IfOutDiscards_Type()
)
ifOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutDiscards.setStatus("current")
_IfInMulticastPkts_Type = Integer32
_IfInMulticastPkts_Object = MibTableColumn
ifInMulticastPkts = _IfInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 11),
    _IfInMulticastPkts_Type()
)
ifInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInMulticastPkts.setStatus("current")
_IfInBroadcastPkts_Type = Integer32
_IfInBroadcastPkts_Object = MibTableColumn
ifInBroadcastPkts = _IfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 12),
    _IfInBroadcastPkts_Type()
)
ifInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInBroadcastPkts.setStatus("current")
_IfOutMulticastPkts_Type = Integer32
_IfOutMulticastPkts_Object = MibTableColumn
ifOutMulticastPkts = _IfOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 13),
    _IfOutMulticastPkts_Type()
)
ifOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutMulticastPkts.setStatus("current")
_IfOutBroadcastPkts_Type = Integer32
_IfOutBroadcastPkts_Object = MibTableColumn
ifOutBroadcastPkts = _IfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 14),
    _IfOutBroadcastPkts_Type()
)
ifOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutBroadcastPkts.setStatus("current")
_Dot3StatsAlignmentErrors_Type = Integer32
_Dot3StatsAlignmentErrors_Object = MibTableColumn
dot3StatsAlignmentErrors = _Dot3StatsAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 15),
    _Dot3StatsAlignmentErrors_Type()
)
dot3StatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsAlignmentErrors.setStatus("current")
_Dot3StatsFCSErrors_Type = Integer32
_Dot3StatsFCSErrors_Object = MibTableColumn
dot3StatsFCSErrors = _Dot3StatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 16),
    _Dot3StatsFCSErrors_Type()
)
dot3StatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsFCSErrors.setStatus("current")
_Dot3StatsSingleCollisionFrames_Type = Integer32
_Dot3StatsSingleCollisionFrames_Object = MibTableColumn
dot3StatsSingleCollisionFrames = _Dot3StatsSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 17),
    _Dot3StatsSingleCollisionFrames_Type()
)
dot3StatsSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSingleCollisionFrames.setStatus("current")
_Dot3StatsMultipleCollisionFrames_Type = Integer32
_Dot3StatsMultipleCollisionFrames_Object = MibTableColumn
dot3StatsMultipleCollisionFrames = _Dot3StatsMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 18),
    _Dot3StatsMultipleCollisionFrames_Type()
)
dot3StatsMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsMultipleCollisionFrames.setStatus("current")
_Dot3StatsDeferredTransmissions_Type = Integer32
_Dot3StatsDeferredTransmissions_Object = MibTableColumn
dot3StatsDeferredTransmissions = _Dot3StatsDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 19),
    _Dot3StatsDeferredTransmissions_Type()
)
dot3StatsDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsDeferredTransmissions.setStatus("current")
_Dot3StatsLateCollisions_Type = Integer32
_Dot3StatsLateCollisions_Object = MibTableColumn
dot3StatsLateCollisions = _Dot3StatsLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 20),
    _Dot3StatsLateCollisions_Type()
)
dot3StatsLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsLateCollisions.setStatus("current")
_Dot3StatsExcessiveCollisions_Type = Integer32
_Dot3StatsExcessiveCollisions_Object = MibTableColumn
dot3StatsExcessiveCollisions = _Dot3StatsExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 21),
    _Dot3StatsExcessiveCollisions_Type()
)
dot3StatsExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsExcessiveCollisions.setStatus("current")
_Dot3StatsFrameTooLongs_Type = Integer32
_Dot3StatsFrameTooLongs_Object = MibTableColumn
dot3StatsFrameTooLongs = _Dot3StatsFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 22),
    _Dot3StatsFrameTooLongs_Type()
)
dot3StatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsFrameTooLongs.setStatus("current")
_Dot3StatsSymbolErrors_Type = Integer32
_Dot3StatsSymbolErrors_Object = MibTableColumn
dot3StatsSymbolErrors = _Dot3StatsSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 23),
    _Dot3StatsSymbolErrors_Type()
)
dot3StatsSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSymbolErrors.setStatus("current")
_Dot3ControlInUnknownOpcodes_Type = Integer32
_Dot3ControlInUnknownOpcodes_Object = MibTableColumn
dot3ControlInUnknownOpcodes = _Dot3ControlInUnknownOpcodes_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 24),
    _Dot3ControlInUnknownOpcodes_Type()
)
dot3ControlInUnknownOpcodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ControlInUnknownOpcodes.setStatus("current")
_Dot3InPauseFrames_Type = Integer32
_Dot3InPauseFrames_Object = MibTableColumn
dot3InPauseFrames = _Dot3InPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 25),
    _Dot3InPauseFrames_Type()
)
dot3InPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3InPauseFrames.setStatus("current")
_Dot3OutPauseFrames_Type = Integer32
_Dot3OutPauseFrames_Object = MibTableColumn
dot3OutPauseFrames = _Dot3OutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 3, 1, 1, 26),
    _Dot3OutPauseFrames_Type()
)
dot3OutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OutPauseFrames.setStatus("current")
_LinkAggregation_ObjectIdentity = ObjectIdentity
linkAggregation = _LinkAggregation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4)
)
_LagStatusTable_Object = MibTable
lagStatusTable = _LagStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lagStatusTable.setStatus("current")
_LagStatusEntry_Object = MibTableRow
lagStatusEntry = _LagStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 1, 1)
)
lagStatusEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "lagStatusIndex"),
)
if mibBuilder.loadTexts:
    lagStatusEntry.setStatus("current")


class _LagStatusIndex_Type(Integer32):
    """Custom type lagStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LagStatusIndex_Type.__name__ = "Integer32"
_LagStatusIndex_Object = MibTableColumn
lagStatusIndex = _LagStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 1, 1, 1),
    _LagStatusIndex_Type()
)
lagStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagStatusIndex.setStatus("current")
_LagStatusName_Type = DisplayString
_LagStatusName_Object = MibTableColumn
lagStatusName = _LagStatusName_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 1, 1, 2),
    _LagStatusName_Type()
)
lagStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagStatusName.setStatus("current")


class _LagStatusType_Type(Integer32):
    """Custom type lagStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("lacp", 2),
          ("none", 3))
    )


_LagStatusType_Type.__name__ = "Integer32"
_LagStatusType_Object = MibTableColumn
lagStatusType = _LagStatusType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 1, 1, 3),
    _LagStatusType_Type()
)
lagStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagStatusType.setStatus("current")


class _LagStatusLinkState_Type(Integer32):
    """Custom type lagStatusLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("notPresent", 3))
    )


_LagStatusLinkState_Type.__name__ = "Integer32"
_LagStatusLinkState_Object = MibTableColumn
lagStatusLinkState = _LagStatusLinkState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 1, 1, 4),
    _LagStatusLinkState_Type()
)
lagStatusLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagStatusLinkState.setStatus("current")
_LagStatusActiveMember_Type = DisplayString
_LagStatusActiveMember_Object = MibTableColumn
lagStatusActiveMember = _LagStatusActiveMember_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 1, 1, 5),
    _LagStatusActiveMember_Type()
)
lagStatusActiveMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagStatusActiveMember.setStatus("current")
_LagStatusStandbyMember_Type = DisplayString
_LagStatusStandbyMember_Object = MibTableColumn
lagStatusStandbyMember = _LagStatusStandbyMember_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 1, 1, 6),
    _LagStatusStandbyMember_Type()
)
lagStatusStandbyMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagStatusStandbyMember.setStatus("current")
_LacpInfoTable_Object = MibTable
lacpInfoTable = _LacpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 2)
)
if mibBuilder.loadTexts:
    lacpInfoTable.setStatus("current")
_LacpInfoEntry_Object = MibTableRow
lacpInfoEntry = _LacpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 2, 1)
)
lacpInfoEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "lacpInfoLagIndex"),
    (0, "ADVANTECH-EKI-PRONEER-MIB", "lacpInfoPortIndex"),
)
if mibBuilder.loadTexts:
    lacpInfoEntry.setStatus("current")
_LacpInfoLagIndex_Type = DisplayString
_LacpInfoLagIndex_Object = MibTableColumn
lacpInfoLagIndex = _LacpInfoLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 2, 1, 1),
    _LacpInfoLagIndex_Type()
)
lacpInfoLagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpInfoLagIndex.setStatus("current")
_LacpInfoPortIndex_Type = DisplayString
_LacpInfoPortIndex_Object = MibTableColumn
lacpInfoPortIndex = _LacpInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 2, 1, 2),
    _LacpInfoPortIndex_Type()
)
lacpInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpInfoPortIndex.setStatus("current")
_LacpInfoPartnerSysId_Type = DisplayString
_LacpInfoPartnerSysId_Object = MibTableColumn
lacpInfoPartnerSysId = _LacpInfoPartnerSysId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 2, 1, 3),
    _LacpInfoPartnerSysId_Type()
)
lacpInfoPartnerSysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpInfoPartnerSysId.setStatus("current")
_LacpInfoPnkey_Type = DisplayString
_LacpInfoPnkey_Object = MibTableColumn
lacpInfoPnkey = _LacpInfoPnkey_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 2, 1, 4),
    _LacpInfoPnkey_Type()
)
lacpInfoPnkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpInfoPnkey.setStatus("current")
_LacpInfoAtkey_Type = DisplayString
_LacpInfoAtkey_Object = MibTableColumn
lacpInfoAtkey = _LacpInfoAtkey_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 2, 1, 5),
    _LacpInfoAtkey_Type()
)
lacpInfoAtkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpInfoAtkey.setStatus("current")
_LacpInfoSel_Type = DisplayString
_LacpInfoSel_Object = MibTableColumn
lacpInfoSel = _LacpInfoSel_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 2, 1, 6),
    _LacpInfoSel_Type()
)
lacpInfoSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpInfoSel.setStatus("current")
_LacpInfoMux_Type = DisplayString
_LacpInfoMux_Object = MibTableColumn
lacpInfoMux = _LacpInfoMux_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 2, 1, 7),
    _LacpInfoMux_Type()
)
lacpInfoMux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpInfoMux.setStatus("current")
_LacpInfoReceiv_Type = DisplayString
_LacpInfoReceiv_Object = MibTableColumn
lacpInfoReceiv = _LacpInfoReceiv_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 2, 1, 8),
    _LacpInfoReceiv_Type()
)
lacpInfoReceiv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpInfoReceiv.setStatus("current")
_LacpInfoPrdtx_Type = DisplayString
_LacpInfoPrdtx_Object = MibTableColumn
lacpInfoPrdtx = _LacpInfoPrdtx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 2, 1, 9),
    _LacpInfoPrdtx_Type()
)
lacpInfoPrdtx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpInfoPrdtx.setStatus("current")
_LacpInfoAtstat_Type = DisplayString
_LacpInfoAtstat_Object = MibTableColumn
lacpInfoAtstat = _LacpInfoAtstat_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 2, 1, 10),
    _LacpInfoAtstat_Type()
)
lacpInfoAtstat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpInfoAtstat.setStatus("current")
_LacpInfoPnstat_Type = DisplayString
_LacpInfoPnstat_Object = MibTableColumn
lacpInfoPnstat = _LacpInfoPnstat_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 4, 2, 1, 11),
    _LacpInfoPnstat_Type()
)
lacpInfoPnstat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpInfoPnstat.setStatus("current")
_LldpStatistics_ObjectIdentity = ObjectIdentity
lldpStatistics = _LldpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 5)
)


class _LldpClearStatistics_Type(Integer32):
    """Custom type lldpClearStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_LldpClearStatistics_Type.__name__ = "Integer32"
_LldpClearStatistics_Object = MibScalar
lldpClearStatistics = _LldpClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 5, 1),
    _LldpClearStatistics_Type()
)
lldpClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpClearStatistics.setStatus("current")
_Inertions_Type = Integer32
_Inertions_Object = MibScalar
inertions = _Inertions_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 5, 2),
    _Inertions_Type()
)
inertions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inertions.setStatus("current")
_Deletions_Type = Integer32
_Deletions_Object = MibScalar
deletions = _Deletions_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 5, 3),
    _Deletions_Type()
)
deletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deletions.setStatus("current")
_Drops_Type = Integer32
_Drops_Object = MibScalar
drops = _Drops_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 5, 4),
    _Drops_Type()
)
drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drops.setStatus("current")
_Ageouts_Type = Integer32
_Ageouts_Object = MibScalar
ageouts = _Ageouts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 5, 5),
    _Ageouts_Type()
)
ageouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ageouts.setStatus("current")
_LldpPortStatisticsTable_Object = MibTable
lldpPortStatisticsTable = _LldpPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 5, 6)
)
if mibBuilder.loadTexts:
    lldpPortStatisticsTable.setStatus("current")
_LldpPortStatisticsEntry_Object = MibTableRow
lldpPortStatisticsEntry = _LldpPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 5, 6, 1)
)
lldpPortStatisticsEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "lldpPortStatIndex"),
)
if mibBuilder.loadTexts:
    lldpPortStatisticsEntry.setStatus("current")


class _LldpPortStatIndex_Type(Integer32):
    """Custom type lldpPortStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LldpPortStatIndex_Type.__name__ = "Integer32"
_LldpPortStatIndex_Object = MibTableColumn
lldpPortStatIndex = _LldpPortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 5, 6, 1, 1),
    _LldpPortStatIndex_Type()
)
lldpPortStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpPortStatIndex.setStatus("current")
_LldpPortStatTotalTxFrame_Type = Integer32
_LldpPortStatTotalTxFrame_Object = MibTableColumn
lldpPortStatTotalTxFrame = _LldpPortStatTotalTxFrame_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 5, 6, 1, 2),
    _LldpPortStatTotalTxFrame_Type()
)
lldpPortStatTotalTxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpPortStatTotalTxFrame.setStatus("current")
_LldpPortStatTotalRxFrame_Type = Integer32
_LldpPortStatTotalRxFrame_Object = MibTableColumn
lldpPortStatTotalRxFrame = _LldpPortStatTotalRxFrame_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 5, 6, 1, 3),
    _LldpPortStatTotalRxFrame_Type()
)
lldpPortStatTotalRxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpPortStatTotalRxFrame.setStatus("current")
_LldpPortStatDiscardRxFrame_Type = Integer32
_LldpPortStatDiscardRxFrame_Object = MibTableColumn
lldpPortStatDiscardRxFrame = _LldpPortStatDiscardRxFrame_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 5, 6, 1, 4),
    _LldpPortStatDiscardRxFrame_Type()
)
lldpPortStatDiscardRxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpPortStatDiscardRxFrame.setStatus("current")
_LldpPortStatErrorRxFrame_Type = Integer32
_LldpPortStatErrorRxFrame_Object = MibTableColumn
lldpPortStatErrorRxFrame = _LldpPortStatErrorRxFrame_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 5, 6, 1, 5),
    _LldpPortStatErrorRxFrame_Type()
)
lldpPortStatErrorRxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpPortStatErrorRxFrame.setStatus("current")
_LldpPortStatDiscardRxTlv_Type = Integer32
_LldpPortStatDiscardRxTlv_Object = MibTableColumn
lldpPortStatDiscardRxTlv = _LldpPortStatDiscardRxTlv_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 5, 6, 1, 6),
    _LldpPortStatDiscardRxTlv_Type()
)
lldpPortStatDiscardRxTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpPortStatDiscardRxTlv.setStatus("current")
_LldpPortStatUnrecognizedRxTlv_Type = Integer32
_LldpPortStatUnrecognizedRxTlv_Object = MibTableColumn
lldpPortStatUnrecognizedRxTlv = _LldpPortStatUnrecognizedRxTlv_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 5, 6, 1, 7),
    _LldpPortStatUnrecognizedRxTlv_Type()
)
lldpPortStatUnrecognizedRxTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpPortStatUnrecognizedRxTlv.setStatus("current")
_LldpPortStatTotalRxAgeouts_Type = Integer32
_LldpPortStatTotalRxAgeouts_Object = MibTableColumn
lldpPortStatTotalRxAgeouts = _LldpPortStatTotalRxAgeouts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 5, 6, 1, 8),
    _LldpPortStatTotalRxAgeouts_Type()
)
lldpPortStatTotalRxAgeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpPortStatTotalRxAgeouts.setStatus("current")
_IgmpStatistics_ObjectIdentity = ObjectIdentity
igmpStatistics = _IgmpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 6)
)
_TotalRx_Type = Integer32
_TotalRx_Object = MibScalar
totalRx = _TotalRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 6, 1),
    _TotalRx_Type()
)
totalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalRx.setStatus("current")
_ValidRx_Type = Integer32
_ValidRx_Object = MibScalar
validRx = _ValidRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 6, 2),
    _ValidRx_Type()
)
validRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    validRx.setStatus("current")
_InvalidRx_Type = Integer32
_InvalidRx_Object = MibScalar
invalidRx = _InvalidRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 6, 3),
    _InvalidRx_Type()
)
invalidRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invalidRx.setStatus("current")
_OtherRx_Type = Integer32
_OtherRx_Object = MibScalar
otherRx = _OtherRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 6, 4),
    _OtherRx_Type()
)
otherRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherRx.setStatus("current")
_LeaveRx_Type = Integer32
_LeaveRx_Object = MibScalar
leaveRx = _LeaveRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 6, 5),
    _LeaveRx_Type()
)
leaveRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leaveRx.setStatus("current")
_ReportRx_Type = Integer32
_ReportRx_Object = MibScalar
reportRx = _ReportRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 6, 6),
    _ReportRx_Type()
)
reportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportRx.setStatus("current")
_GeneralQueryRx_Type = Integer32
_GeneralQueryRx_Object = MibScalar
generalQueryRx = _GeneralQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 6, 7),
    _GeneralQueryRx_Type()
)
generalQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalQueryRx.setStatus("current")
_SpecialGroupQueryRx_Type = Integer32
_SpecialGroupQueryRx_Object = MibScalar
specialGroupQueryRx = _SpecialGroupQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 6, 8),
    _SpecialGroupQueryRx_Type()
)
specialGroupQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specialGroupQueryRx.setStatus("current")
_SpecialGroupSourceQueryRx_Type = Integer32
_SpecialGroupSourceQueryRx_Object = MibScalar
specialGroupSourceQueryRx = _SpecialGroupSourceQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 6, 9),
    _SpecialGroupSourceQueryRx_Type()
)
specialGroupSourceQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specialGroupSourceQueryRx.setStatus("current")
_LeaveTx_Type = Integer32
_LeaveTx_Object = MibScalar
leaveTx = _LeaveTx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 6, 10),
    _LeaveTx_Type()
)
leaveTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leaveTx.setStatus("current")
_ReportTx_Type = Integer32
_ReportTx_Object = MibScalar
reportTx = _ReportTx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 6, 11),
    _ReportTx_Type()
)
reportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportTx.setStatus("current")
_GeneralQueryTx_Type = Integer32
_GeneralQueryTx_Object = MibScalar
generalQueryTx = _GeneralQueryTx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 6, 12),
    _GeneralQueryTx_Type()
)
generalQueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalQueryTx.setStatus("current")
_SpecialGroupQueryTx_Type = Integer32
_SpecialGroupQueryTx_Object = MibScalar
specialGroupQueryTx = _SpecialGroupQueryTx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 6, 13),
    _SpecialGroupQueryTx_Type()
)
specialGroupQueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specialGroupQueryTx.setStatus("current")
_SpecialGroupSourceQueryTx_Type = Integer32
_SpecialGroupSourceQueryTx_Object = MibScalar
specialGroupSourceQueryTx = _SpecialGroupSourceQueryTx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 6, 14),
    _SpecialGroupSourceQueryTx_Type()
)
specialGroupSourceQueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specialGroupSourceQueryTx.setStatus("current")


class _ClearigmpStatistics_Type(Integer32):
    """Custom type clearigmpStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_ClearigmpStatistics_Type.__name__ = "Integer32"
_ClearigmpStatistics_Object = MibScalar
clearigmpStatistics = _ClearigmpStatistics_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 6, 15),
    _ClearigmpStatistics_Type()
)
clearigmpStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearigmpStatistics.setStatus("current")
_MldStatistics_ObjectIdentity = ObjectIdentity
mldStatistics = _MldStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 7)
)
_MldtotalRx_Type = Integer32
_MldtotalRx_Object = MibScalar
mldtotalRx = _MldtotalRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 7, 1),
    _MldtotalRx_Type()
)
mldtotalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldtotalRx.setStatus("current")
_MldvalidRx_Type = Integer32
_MldvalidRx_Object = MibScalar
mldvalidRx = _MldvalidRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 7, 2),
    _MldvalidRx_Type()
)
mldvalidRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldvalidRx.setStatus("current")
_MldinvalidRx_Type = Integer32
_MldinvalidRx_Object = MibScalar
mldinvalidRx = _MldinvalidRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 7, 3),
    _MldinvalidRx_Type()
)
mldinvalidRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldinvalidRx.setStatus("current")
_MldotherRx_Type = Integer32
_MldotherRx_Object = MibScalar
mldotherRx = _MldotherRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 7, 4),
    _MldotherRx_Type()
)
mldotherRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldotherRx.setStatus("current")
_MldleaveRx_Type = Integer32
_MldleaveRx_Object = MibScalar
mldleaveRx = _MldleaveRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 7, 5),
    _MldleaveRx_Type()
)
mldleaveRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldleaveRx.setStatus("current")
_MldreportRx_Type = Integer32
_MldreportRx_Object = MibScalar
mldreportRx = _MldreportRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 7, 6),
    _MldreportRx_Type()
)
mldreportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldreportRx.setStatus("current")
_MldgeneralQueryRx_Type = Integer32
_MldgeneralQueryRx_Object = MibScalar
mldgeneralQueryRx = _MldgeneralQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 7, 7),
    _MldgeneralQueryRx_Type()
)
mldgeneralQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldgeneralQueryRx.setStatus("current")
_MldspecialGroupQueryRx_Type = Integer32
_MldspecialGroupQueryRx_Object = MibScalar
mldspecialGroupQueryRx = _MldspecialGroupQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 7, 8),
    _MldspecialGroupQueryRx_Type()
)
mldspecialGroupQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldspecialGroupQueryRx.setStatus("current")
_MldspecialGroupSourceQueryRx_Type = Integer32
_MldspecialGroupSourceQueryRx_Object = MibScalar
mldspecialGroupSourceQueryRx = _MldspecialGroupSourceQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 7, 9),
    _MldspecialGroupSourceQueryRx_Type()
)
mldspecialGroupSourceQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldspecialGroupSourceQueryRx.setStatus("current")
_MldleaveTx_Type = Integer32
_MldleaveTx_Object = MibScalar
mldleaveTx = _MldleaveTx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 7, 10),
    _MldleaveTx_Type()
)
mldleaveTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldleaveTx.setStatus("current")
_MldreportTx_Type = Integer32
_MldreportTx_Object = MibScalar
mldreportTx = _MldreportTx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 7, 11),
    _MldreportTx_Type()
)
mldreportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldreportTx.setStatus("current")
_MldgeneralQueryTx_Type = Integer32
_MldgeneralQueryTx_Object = MibScalar
mldgeneralQueryTx = _MldgeneralQueryTx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 7, 12),
    _MldgeneralQueryTx_Type()
)
mldgeneralQueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldgeneralQueryTx.setStatus("current")
_MldspecialGroupQueryTx_Type = Integer32
_MldspecialGroupQueryTx_Object = MibScalar
mldspecialGroupQueryTx = _MldspecialGroupQueryTx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 7, 13),
    _MldspecialGroupQueryTx_Type()
)
mldspecialGroupQueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldspecialGroupQueryTx.setStatus("current")
_MldspecialGroupSourceQueryTx_Type = Integer32
_MldspecialGroupSourceQueryTx_Object = MibScalar
mldspecialGroupSourceQueryTx = _MldspecialGroupSourceQueryTx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 7, 14),
    _MldspecialGroupSourceQueryTx_Type()
)
mldspecialGroupSourceQueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldspecialGroupSourceQueryTx.setStatus("current")


class _ClearmldStatistics_Type(Integer32):
    """Custom type clearmldStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_ClearmldStatistics_Type.__name__ = "Integer32"
_ClearmldStatistics_Object = MibScalar
clearmldStatistics = _ClearmldStatistics_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 1, 7, 15),
    _ClearmldStatistics_Type()
)
clearmldStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearmldStatistics.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2)
)
_IpSettings_ObjectIdentity = ObjectIdentity
ipSettings = _IpSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1)
)


class _Ipv4Mode_Type(Integer32):
    """Custom type ipv4Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp", 2))
    )


_Ipv4Mode_Type.__name__ = "Integer32"
_Ipv4Mode_Object = MibScalar
ipv4Mode = _Ipv4Mode_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1, 1),
    _Ipv4Mode_Type()
)
ipv4Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4Mode.setStatus("current")
_Ipv4Address_Type = IpAddress
_Ipv4Address_Object = MibScalar
ipv4Address = _Ipv4Address_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1, 2),
    _Ipv4Address_Type()
)
ipv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4Address.setStatus("current")
_Ipv4SubnetMask_Type = IpAddress
_Ipv4SubnetMask_Object = MibScalar
ipv4SubnetMask = _Ipv4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1, 3),
    _Ipv4SubnetMask_Type()
)
ipv4SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4SubnetMask.setStatus("current")
_Ipv4Gateway_Type = IpAddress
_Ipv4Gateway_Object = MibScalar
ipv4Gateway = _Ipv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1, 4),
    _Ipv4Gateway_Type()
)
ipv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4Gateway.setStatus("current")
_Ipv4DnsServer1_Type = IpAddress
_Ipv4DnsServer1_Object = MibScalar
ipv4DnsServer1 = _Ipv4DnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1, 5),
    _Ipv4DnsServer1_Type()
)
ipv4DnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4DnsServer1.setStatus("current")
_Ipv4DnsServer2_Type = IpAddress
_Ipv4DnsServer2_Object = MibScalar
ipv4DnsServer2 = _Ipv4DnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1, 6),
    _Ipv4DnsServer2_Type()
)
ipv4DnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4DnsServer2.setStatus("current")
_InterfaceIpv4Table_Object = MibTable
interfaceIpv4Table = _InterfaceIpv4Table_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1, 7)
)
if mibBuilder.loadTexts:
    interfaceIpv4Table.setStatus("current")
_InterfaceIpv4Entry_Object = MibTableRow
interfaceIpv4Entry = _InterfaceIpv4Entry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1, 7, 1)
)
interfaceIpv4Entry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "interfaceIpv4Index"),
)
if mibBuilder.loadTexts:
    interfaceIpv4Entry.setStatus("current")


class _InterfaceIpv4Index_Type(Integer32):
    """Custom type interfaceIpv4Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_InterfaceIpv4Index_Type.__name__ = "Integer32"
_InterfaceIpv4Index_Object = MibTableColumn
interfaceIpv4Index = _InterfaceIpv4Index_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1, 7, 1, 1),
    _InterfaceIpv4Index_Type()
)
interfaceIpv4Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIpv4Index.setStatus("current")


class _InterfaceIpv4Vlan_Type(Integer32):
    """Custom type interfaceIpv4Vlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_InterfaceIpv4Vlan_Type.__name__ = "Integer32"
_InterfaceIpv4Vlan_Object = MibTableColumn
interfaceIpv4Vlan = _InterfaceIpv4Vlan_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1, 7, 1, 2),
    _InterfaceIpv4Vlan_Type()
)
interfaceIpv4Vlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIpv4Vlan.setStatus("current")


class _InterfaceIpv4Mode_Type(Integer32):
    """Custom type interfaceIpv4Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp", 2))
    )


_InterfaceIpv4Mode_Type.__name__ = "Integer32"
_InterfaceIpv4Mode_Object = MibTableColumn
interfaceIpv4Mode = _InterfaceIpv4Mode_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1, 7, 1, 3),
    _InterfaceIpv4Mode_Type()
)
interfaceIpv4Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceIpv4Mode.setStatus("current")
_InterfaceIpv4Address_Type = IpAddress
_InterfaceIpv4Address_Object = MibTableColumn
interfaceIpv4Address = _InterfaceIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1, 7, 1, 4),
    _InterfaceIpv4Address_Type()
)
interfaceIpv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceIpv4Address.setStatus("current")
_InterfaceIpv4SubnetMask_Type = IpAddress
_InterfaceIpv4SubnetMask_Object = MibTableColumn
interfaceIpv4SubnetMask = _InterfaceIpv4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1, 7, 1, 5),
    _InterfaceIpv4SubnetMask_Type()
)
interfaceIpv4SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceIpv4SubnetMask.setStatus("current")
_InterfaceIpv4Gateway_Type = IpAddress
_InterfaceIpv4Gateway_Object = MibTableColumn
interfaceIpv4Gateway = _InterfaceIpv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1, 7, 1, 6),
    _InterfaceIpv4Gateway_Type()
)
interfaceIpv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceIpv4Gateway.setStatus("current")


class _InterCurrIpv4DhcpState_Type(Integer32):
    """Custom type interCurrIpv4DhcpState based on Integer32"""
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


_InterCurrIpv4DhcpState_Type.__name__ = "Integer32"
_InterCurrIpv4DhcpState_Object = MibTableColumn
interCurrIpv4DhcpState = _InterCurrIpv4DhcpState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1, 7, 1, 7),
    _InterCurrIpv4DhcpState_Type()
)
interCurrIpv4DhcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interCurrIpv4DhcpState.setStatus("current")
_InterCurrIpv4Address_Type = IpAddress
_InterCurrIpv4Address_Object = MibTableColumn
interCurrIpv4Address = _InterCurrIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1, 7, 1, 8),
    _InterCurrIpv4Address_Type()
)
interCurrIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interCurrIpv4Address.setStatus("current")
_InterCurrIpv4SubnetMask_Type = IpAddress
_InterCurrIpv4SubnetMask_Object = MibTableColumn
interCurrIpv4SubnetMask = _InterCurrIpv4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1, 7, 1, 9),
    _InterCurrIpv4SubnetMask_Type()
)
interCurrIpv4SubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interCurrIpv4SubnetMask.setStatus("current")
_InterCurrIpv4Gateway_Type = IpAddress
_InterCurrIpv4Gateway_Object = MibTableColumn
interCurrIpv4Gateway = _InterCurrIpv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 1, 7, 1, 10),
    _InterCurrIpv4Gateway_Type()
)
interCurrIpv4Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interCurrIpv4Gateway.setStatus("current")
_Ipv6Settings_ObjectIdentity = ObjectIdentity
ipv6Settings = _Ipv6Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 2)
)


class _AutoConfiguration_Type(Integer32):
    """Custom type autoConfiguration based on Integer32"""
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


_AutoConfiguration_Type.__name__ = "Integer32"
_AutoConfiguration_Object = MibScalar
autoConfiguration = _AutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 2, 1),
    _AutoConfiguration_Type()
)
autoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoConfiguration.setStatus("current")
_Ipv6Address_Type = DisplayString
_Ipv6Address_Object = MibScalar
ipv6Address = _Ipv6Address_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 2, 2),
    _Ipv6Address_Type()
)
ipv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6Address.setStatus("current")


class _Ipv6SubnetMask_Type(Integer32):
    """Custom type ipv6SubnetMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Ipv6SubnetMask_Type.__name__ = "Integer32"
_Ipv6SubnetMask_Object = MibScalar
ipv6SubnetMask = _Ipv6SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 2, 3),
    _Ipv6SubnetMask_Type()
)
ipv6SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6SubnetMask.setStatus("current")
_Ipv6Gateway_Type = DisplayString
_Ipv6Gateway_Object = MibScalar
ipv6Gateway = _Ipv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 2, 4),
    _Ipv6Gateway_Type()
)
ipv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6Gateway.setStatus("current")


class _Dhcpv6Client_Type(Integer32):
    """Custom type dhcpv6Client based on Integer32"""
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


_Dhcpv6Client_Type.__name__ = "Integer32"
_Dhcpv6Client_Object = MibScalar
dhcpv6Client = _Dhcpv6Client_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 2, 5),
    _Dhcpv6Client_Type()
)
dhcpv6Client.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpv6Client.setStatus("current")
_Ipv6InUseTable_Object = MibTable
ipv6InUseTable = _Ipv6InUseTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 2, 6)
)
if mibBuilder.loadTexts:
    ipv6InUseTable.setStatus("current")
_Ipv6InUseEntry_Object = MibTableRow
ipv6InUseEntry = _Ipv6InUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 2, 6, 1)
)
ipv6InUseEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "ipv6InUseIndex"),
)
if mibBuilder.loadTexts:
    ipv6InUseEntry.setStatus("current")


class _Ipv6InUseIndex_Type(Integer32):
    """Custom type ipv6InUseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Ipv6InUseIndex_Type.__name__ = "Integer32"
_Ipv6InUseIndex_Object = MibTableColumn
ipv6InUseIndex = _Ipv6InUseIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 2, 6, 1, 1),
    _Ipv6InUseIndex_Type()
)
ipv6InUseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6InUseIndex.setStatus("current")
_Ipv6InUseAddress_Type = DisplayString
_Ipv6InUseAddress_Object = MibTableColumn
ipv6InUseAddress = _Ipv6InUseAddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 2, 6, 1, 2),
    _Ipv6InUseAddress_Type()
)
ipv6InUseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6InUseAddress.setStatus("current")
_Ipv6InUseSubnetMask_Type = Integer32
_Ipv6InUseSubnetMask_Object = MibTableColumn
ipv6InUseSubnetMask = _Ipv6InUseSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 2, 6, 1, 3),
    _Ipv6InUseSubnetMask_Type()
)
ipv6InUseSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6InUseSubnetMask.setStatus("current")
_Ipv6InUseRouter_Type = DisplayString
_Ipv6InUseRouter_Object = MibScalar
ipv6InUseRouter = _Ipv6InUseRouter_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 2, 7),
    _Ipv6InUseRouter_Type()
)
ipv6InUseRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6InUseRouter.setStatus("current")
_Dhcpv6DUID_Type = DisplayString
_Dhcpv6DUID_Object = MibScalar
dhcpv6DUID = _Dhcpv6DUID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 2, 8),
    _Dhcpv6DUID_Type()
)
dhcpv6DUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpv6DUID.setStatus("current")
_Dhcpv6IPAddress_Type = DisplayString
_Dhcpv6IPAddress_Object = MibScalar
dhcpv6IPAddress = _Dhcpv6IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 2, 9),
    _Dhcpv6IPAddress_Type()
)
dhcpv6IPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpv6IPAddress.setStatus("current")


class _ManagementVlan_Type(Integer32):
    """Custom type managementVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ManagementVlan_Type.__name__ = "Integer32"
_ManagementVlan_Object = MibScalar
managementVlan = _ManagementVlan_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 3),
    _ManagementVlan_Type()
)
managementVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementVlan.setStatus("current")
_SystemTime_ObjectIdentity = ObjectIdentity
systemTime = _SystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4)
)
_SystemTimeSetting_ObjectIdentity = ObjectIdentity
systemTimeSetting = _SystemTimeSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1)
)


class _EnableSNTP_Type(Integer32):
    """Custom type enableSNTP based on Integer32"""
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


_EnableSNTP_Type.__name__ = "Integer32"
_EnableSNTP_Object = MibScalar
enableSNTP = _EnableSNTP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 1),
    _EnableSNTP_Type()
)
enableSNTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSNTP.setStatus("current")
_ManualTime_ObjectIdentity = ObjectIdentity
manualTime = _ManualTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 2)
)


class _Year_Type(Integer32):
    """Custom type year based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2035),
    )


_Year_Type.__name__ = "Integer32"
_Year_Object = MibScalar
year = _Year_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 2, 1),
    _Year_Type()
)
year.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    year.setStatus("current")


class _Month_Type(Integer32):
    """Custom type month based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Month_Type.__name__ = "Integer32"
_Month_Object = MibScalar
month = _Month_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 2, 2),
    _Month_Type()
)
month.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    month.setStatus("current")


class _Day_Type(Integer32):
    """Custom type day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Day_Type.__name__ = "Integer32"
_Day_Object = MibScalar
day = _Day_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 2, 3),
    _Day_Type()
)
day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    day.setStatus("current")


class _Hours_Type(Integer32):
    """Custom type hours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Hours_Type.__name__ = "Integer32"
_Hours_Object = MibScalar
hours = _Hours_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 2, 4),
    _Hours_Type()
)
hours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hours.setStatus("current")


class _Minutes_Type(Integer32):
    """Custom type minutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Minutes_Type.__name__ = "Integer32"
_Minutes_Object = MibScalar
minutes = _Minutes_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 2, 5),
    _Minutes_Type()
)
minutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minutes.setStatus("current")


class _Seconds_Type(Integer32):
    """Custom type seconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Seconds_Type.__name__ = "Integer32"
_Seconds_Object = MibScalar
seconds = _Seconds_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 2, 6),
    _Seconds_Type()
)
seconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seconds.setStatus("current")


class _TimeZone_Type(Integer32):
    """Custom type timeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("gmtminus1200-International-Date-Line-West", 1),
          ("gmtminus1100-MidwayIsland-Samoa", 2),
          ("gmtminus1000-Hawaii", 3),
          ("gmtminus0900-Alaska", 4),
          ("gmtminus0800-Pacific-Time-US-and-Canada", 5),
          ("gmtminus0800-Tijuana-Baja-California", 6),
          ("gmtminus0700-Arizona", 7),
          ("gmtminus0700-Chihuahua-La-Paz-Mazatlan-New", 8),
          ("gmtminus0700-Chihuahua-La-Paz-Mazatlan-Old", 9),
          ("gmtminus0700-Mountain-Time-US-and-Canada", 10),
          ("gmtminus0600-Central-America", 11),
          ("gmtminus0600-Central-Time-US-and-Canada", 12),
          ("gmtminus0600-Guadalajara-Mexico-City-Monterrey-New", 13),
          ("gmtminus0600-Guadalajara-Mexico-City-Monterrey-Old", 14),
          ("gmtminus0600-Saskatchewan", 15),
          ("gmtminus0500-Bogota-Lima-Quito-Rio-Branco", 16),
          ("gmtminus0500-Eastern-Time-US-and-Canada", 17),
          ("gmtminus0500-Indiana-East", 18),
          ("gmtminus0430-Caracas", 19),
          ("gmtminus0400-Atlantic-Time-Canada", 20),
          ("gmtminus0400-La-Paz", 21),
          ("gmtminus0400-Manaus", 22),
          ("gmtminus0400-Santiago", 23),
          ("gmtminus0330-Newfoundland", 24),
          ("gmtminus0300-Brasilia", 25),
          ("gmtminus0300-Buenos-Aires", 26),
          ("gmtminus0300-Georgetown", 27),
          ("gmtminus0300-Greenland", 28),
          ("gmtminus0300-Montevideo", 29),
          ("gmtminus0200-Mid-Atlantic", 30),
          ("gmtminus0100-Azores", 31),
          ("gmtminus0100-Cape-Verde-Is", 32),
          ("gmt-Casablanca", 33),
          ("gmt-Greenwich-Mean-Time-Dublin-Edinburgh-Lisbon-London", 34),
          ("gmt-Monrovia-Reykjavik", 35),
          ("gmtplus0100-Amsterdam-Berlin-Bern-Rome-Stockholm-Vienna", 36),
          ("gmtplus0100-Belgrade-Bratislava-Budapest-Ljubljana-Prague", 37),
          ("gmtplus0100-Brussels-Copenhagen-Madrid-Paris", 38),
          ("gmtplus0100-Sarajevo-Skopje-Warsaw-Zagreb", 39),
          ("gmtplus0100-West-Central-Africa", 40),
          ("gmtplus0200-Amman", 41),
          ("gmtplus0200-Athens-Bucharest-Istanbul", 42),
          ("gmtplus0200-Beirut", 43),
          ("gmtplus0200-Cairo", 44),
          ("gmtplus0200-Harare-Pretoria", 45),
          ("gmtplus0200-Helsinki-Kyiv-Riga-Sofia-Tallinn-Vilnius", 46),
          ("gmtplus0200-Jerusalem", 47),
          ("gmtplus0200-Minsk", 48),
          ("gmtplus0200-Windhoek", 49),
          ("gmtplus0300-Baghdad", 50),
          ("gmtplus0300-Kuwait-Riyadh", 51),
          ("gmtplus0300-Moscow-St-Petersburg-Volgograd", 52),
          ("gmtplus0300-Nairobi", 53),
          ("gmtplus0300-Tbilisi", 54),
          ("gmtplus0330-Tehran", 55),
          ("gmtplus0400-Abu-Dhabi-Muscat", 56),
          ("gmtplus0400-Baku", 57),
          ("gmtplus0400-Caucasus-Standard-Time", 58),
          ("gmtplus0400-Port-Louis", 59),
          ("gmtplus0400-Yerevan", 60),
          ("gmtplus0430-Kabul", 61),
          ("gmtplus0500-Ekaterinburg", 62),
          ("gmtplus0500-Islamabad-Karachi", 63),
          ("gmtplus0500-Tashkent", 64),
          ("gmtplus0530-Chennai-Kolkata-Mumbai-New-Delhi", 65),
          ("gmtplus0530-Sri-Jayawardenepura", 66),
          ("gmtplus0545-Kathmandu", 67),
          ("gmtplus0600-Almaty-Novosibirsk", 68),
          ("gmtplus0600-Astana-Dhaka", 69),
          ("gmtplus0630-Yangon-Rangoon", 70),
          ("gmtplus0700-Bangkok-Hanoi-Jakarta", 71),
          ("gmtplus0700-Krasnoyarsk", 72),
          ("gmtplus0800-Beijing-Chongqing-Hong-Kong-Urumqi", 73),
          ("gmtplus0800-Irkutsk-Ulaan-Bataar", 74),
          ("gmtplus0800-Kuala-Lumpur-Singapore", 75),
          ("gmtplus0800-Perth", 76),
          ("gmtplus0800-Taipei", 77),
          ("gmtplus0900-Osaka-Sapporo-Tokyo", 78),
          ("gmtplus0900-Seoul", 79),
          ("gmtplus0900-Yakutsk", 80),
          ("gmtplus0930-Adelaide", 81),
          ("gmtplus0930-Darwin", 82),
          ("gmtplus1000-Brisbane", 83),
          ("gmtplus1000-Canberra-Melbourne-Sydney", 84),
          ("gmtplus1000-Guam-Port-Moresby", 85),
          ("gmtplus1000-Hobart", 86),
          ("gmtplus1000-Vladivostok", 87),
          ("gmtplus1100-Magadan-Solomon-Is-New-Caledonia", 88),
          ("gmtplus1200-Auckland-Wellington", 89),
          ("gmtplus1200-Fiji-Kamchatka-Marshall-Is", 90),
          ("gmtplus1300-Nuku-alofa", 91))
    )


_TimeZone_Type.__name__ = "Integer32"
_TimeZone_Object = MibScalar
timeZone = _TimeZone_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 3),
    _TimeZone_Type()
)
timeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeZone.setStatus("current")


class _DaylightSaving_Type(Integer32):
    """Custom type daylightSaving based on Integer32"""
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
        *(("disable", 1),
          ("recurring", 2),
          ("no-recurring", 3),
          ("usa", 4),
          ("european", 5))
    )


_DaylightSaving_Type.__name__ = "Integer32"
_DaylightSaving_Object = MibScalar
daylightSaving = _DaylightSaving_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 4),
    _DaylightSaving_Type()
)
daylightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSaving.setStatus("current")


class _DaylightSavingOffset_Type(Integer32):
    """Custom type daylightSavingOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_DaylightSavingOffset_Type.__name__ = "Integer32"
_DaylightSavingOffset_Object = MibScalar
daylightSavingOffset = _DaylightSavingOffset_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 5),
    _DaylightSavingOffset_Type()
)
daylightSavingOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingOffset.setStatus("current")
_RecurringFrom_ObjectIdentity = ObjectIdentity
recurringFrom = _RecurringFrom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 6)
)


class _RecFromDay_Type(Integer32):
    """Custom type recFromDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_RecFromDay_Type.__name__ = "Integer32"
_RecFromDay_Object = MibScalar
recFromDay = _RecFromDay_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 6, 1),
    _RecFromDay_Type()
)
recFromDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recFromDay.setStatus("current")


class _RecFromWeek_Type(Integer32):
    """Custom type recFromWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RecFromWeek_Type.__name__ = "Integer32"
_RecFromWeek_Object = MibScalar
recFromWeek = _RecFromWeek_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 6, 2),
    _RecFromWeek_Type()
)
recFromWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recFromWeek.setStatus("current")


class _RecFromMonth_Type(Integer32):
    """Custom type recFromMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_RecFromMonth_Type.__name__ = "Integer32"
_RecFromMonth_Object = MibScalar
recFromMonth = _RecFromMonth_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 6, 3),
    _RecFromMonth_Type()
)
recFromMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recFromMonth.setStatus("current")


class _RecFromHours_Type(Integer32):
    """Custom type recFromHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_RecFromHours_Type.__name__ = "Integer32"
_RecFromHours_Object = MibScalar
recFromHours = _RecFromHours_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 6, 4),
    _RecFromHours_Type()
)
recFromHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recFromHours.setStatus("current")


class _RecFromMinutes_Type(Integer32):
    """Custom type recFromMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_RecFromMinutes_Type.__name__ = "Integer32"
_RecFromMinutes_Object = MibScalar
recFromMinutes = _RecFromMinutes_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 6, 5),
    _RecFromMinutes_Type()
)
recFromMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recFromMinutes.setStatus("current")
_RecurringTo_ObjectIdentity = ObjectIdentity
recurringTo = _RecurringTo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 7)
)


class _RecToDay_Type(Integer32):
    """Custom type recToDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_RecToDay_Type.__name__ = "Integer32"
_RecToDay_Object = MibScalar
recToDay = _RecToDay_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 7, 1),
    _RecToDay_Type()
)
recToDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recToDay.setStatus("current")


class _RecToWeek_Type(Integer32):
    """Custom type recToWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RecToWeek_Type.__name__ = "Integer32"
_RecToWeek_Object = MibScalar
recToWeek = _RecToWeek_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 7, 2),
    _RecToWeek_Type()
)
recToWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recToWeek.setStatus("current")


class _RecToMonth_Type(Integer32):
    """Custom type recToMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_RecToMonth_Type.__name__ = "Integer32"
_RecToMonth_Object = MibScalar
recToMonth = _RecToMonth_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 7, 3),
    _RecToMonth_Type()
)
recToMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recToMonth.setStatus("current")


class _RecToHours_Type(Integer32):
    """Custom type recToHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_RecToHours_Type.__name__ = "Integer32"
_RecToHours_Object = MibScalar
recToHours = _RecToHours_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 7, 4),
    _RecToHours_Type()
)
recToHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recToHours.setStatus("current")


class _RecToMinutes_Type(Integer32):
    """Custom type recToMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_RecToMinutes_Type.__name__ = "Integer32"
_RecToMinutes_Object = MibScalar
recToMinutes = _RecToMinutes_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 7, 5),
    _RecToMinutes_Type()
)
recToMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recToMinutes.setStatus("current")
_NonRecurringFrom_ObjectIdentity = ObjectIdentity
nonRecurringFrom = _NonRecurringFrom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 8)
)


class _NonRecFromYear_Type(Integer32):
    """Custom type nonRecFromYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2037),
    )


_NonRecFromYear_Type.__name__ = "Integer32"
_NonRecFromYear_Object = MibScalar
nonRecFromYear = _NonRecFromYear_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 8, 1),
    _NonRecFromYear_Type()
)
nonRecFromYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nonRecFromYear.setStatus("current")


class _NonRecFromMonth_Type(Integer32):
    """Custom type nonRecFromMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_NonRecFromMonth_Type.__name__ = "Integer32"
_NonRecFromMonth_Object = MibScalar
nonRecFromMonth = _NonRecFromMonth_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 8, 2),
    _NonRecFromMonth_Type()
)
nonRecFromMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nonRecFromMonth.setStatus("current")


class _NonRecFromDay_Type(Integer32):
    """Custom type nonRecFromDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_NonRecFromDay_Type.__name__ = "Integer32"
_NonRecFromDay_Object = MibScalar
nonRecFromDay = _NonRecFromDay_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 8, 3),
    _NonRecFromDay_Type()
)
nonRecFromDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nonRecFromDay.setStatus("current")


class _NonRecFromHours_Type(Integer32):
    """Custom type nonRecFromHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_NonRecFromHours_Type.__name__ = "Integer32"
_NonRecFromHours_Object = MibScalar
nonRecFromHours = _NonRecFromHours_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 8, 4),
    _NonRecFromHours_Type()
)
nonRecFromHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nonRecFromHours.setStatus("current")


class _NonRecFromMinutes_Type(Integer32):
    """Custom type nonRecFromMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_NonRecFromMinutes_Type.__name__ = "Integer32"
_NonRecFromMinutes_Object = MibScalar
nonRecFromMinutes = _NonRecFromMinutes_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 8, 5),
    _NonRecFromMinutes_Type()
)
nonRecFromMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nonRecFromMinutes.setStatus("current")
_NonRecurringTo_ObjectIdentity = ObjectIdentity
nonRecurringTo = _NonRecurringTo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 9)
)


class _NonRecToYear_Type(Integer32):
    """Custom type nonRecToYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2037),
    )


_NonRecToYear_Type.__name__ = "Integer32"
_NonRecToYear_Object = MibScalar
nonRecToYear = _NonRecToYear_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 9, 1),
    _NonRecToYear_Type()
)
nonRecToYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nonRecToYear.setStatus("current")


class _NonRecToMonth_Type(Integer32):
    """Custom type nonRecToMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_NonRecToMonth_Type.__name__ = "Integer32"
_NonRecToMonth_Object = MibScalar
nonRecToMonth = _NonRecToMonth_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 9, 2),
    _NonRecToMonth_Type()
)
nonRecToMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nonRecToMonth.setStatus("current")


class _NonRecToDay_Type(Integer32):
    """Custom type nonRecToDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_NonRecToDay_Type.__name__ = "Integer32"
_NonRecToDay_Object = MibScalar
nonRecToDay = _NonRecToDay_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 9, 3),
    _NonRecToDay_Type()
)
nonRecToDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nonRecToDay.setStatus("current")


class _NonRecToHours_Type(Integer32):
    """Custom type nonRecToHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_NonRecToHours_Type.__name__ = "Integer32"
_NonRecToHours_Object = MibScalar
nonRecToHours = _NonRecToHours_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 9, 4),
    _NonRecToHours_Type()
)
nonRecToHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nonRecToHours.setStatus("current")


class _NonRecToMinutes_Type(Integer32):
    """Custom type nonRecToMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_NonRecToMinutes_Type.__name__ = "Integer32"
_NonRecToMinutes_Object = MibScalar
nonRecToMinutes = _NonRecToMinutes_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 9, 5),
    _NonRecToMinutes_Type()
)
nonRecToMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nonRecToMinutes.setStatus("current")
_ServerAddress_Type = DisplayString
_ServerAddress_Object = MibScalar
serverAddress = _ServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 10),
    _ServerAddress_Type()
)
serverAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverAddress.setStatus("current")


class _ServerPort_Type(Integer32):
    """Custom type serverPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ServerPort_Type.__name__ = "Integer32"
_ServerPort_Object = MibScalar
serverPort = _ServerPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 11),
    _ServerPort_Type()
)
serverPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverPort.setStatus("current")


class _SystemTimeStatus_Type(Integer32):
    """Custom type systemTimeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2))
    )


_SystemTimeStatus_Type.__name__ = "Integer32"
_SystemTimeStatus_Object = MibScalar
systemTimeStatus = _SystemTimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 1, 12),
    _SystemTimeStatus_Type()
)
systemTimeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTimeStatus.setStatus("current")
_SystemTimeInfo_ObjectIdentity = ObjectIdentity
systemTimeInfo = _SystemTimeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 2)
)
_CurrentDateTime_Type = DisplayString
_CurrentDateTime_Object = MibScalar
currentDateTime = _CurrentDateTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 2, 1),
    _CurrentDateTime_Type()
)
currentDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDateTime.setStatus("current")


class _CurrentSNTP_Type(Integer32):
    """Custom type currentSNTP based on Integer32"""
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


_CurrentSNTP_Type.__name__ = "Integer32"
_CurrentSNTP_Object = MibScalar
currentSNTP = _CurrentSNTP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 2, 2),
    _CurrentSNTP_Type()
)
currentSNTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSNTP.setStatus("current")
_CurrentSNTPServerAddr_Type = DisplayString
_CurrentSNTPServerAddr_Object = MibScalar
currentSNTPServerAddr = _CurrentSNTPServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 2, 3),
    _CurrentSNTPServerAddr_Type()
)
currentSNTPServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSNTPServerAddr.setStatus("current")


class _CurrentSNTPServerPort_Type(Integer32):
    """Custom type currentSNTPServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CurrentSNTPServerPort_Type.__name__ = "Integer32"
_CurrentSNTPServerPort_Object = MibScalar
currentSNTPServerPort = _CurrentSNTPServerPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 2, 4),
    _CurrentSNTPServerPort_Type()
)
currentSNTPServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSNTPServerPort.setStatus("current")
_CurrentTimeZone_Type = DisplayString
_CurrentTimeZone_Object = MibScalar
currentTimeZone = _CurrentTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 2, 5),
    _CurrentTimeZone_Type()
)
currentTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentTimeZone.setStatus("current")
_CurrentDaylightSavingStatus_Type = DisplayString
_CurrentDaylightSavingStatus_Object = MibScalar
currentDaylightSavingStatus = _CurrentDaylightSavingStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 2, 6),
    _CurrentDaylightSavingStatus_Type()
)
currentDaylightSavingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDaylightSavingStatus.setStatus("current")
_CurrentDaylightSavingOffset_Type = DisplayString
_CurrentDaylightSavingOffset_Object = MibScalar
currentDaylightSavingOffset = _CurrentDaylightSavingOffset_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 2, 7),
    _CurrentDaylightSavingOffset_Type()
)
currentDaylightSavingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDaylightSavingOffset.setStatus("current")
_CurrentDaylightSavingFrom_Type = DisplayString
_CurrentDaylightSavingFrom_Object = MibScalar
currentDaylightSavingFrom = _CurrentDaylightSavingFrom_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 2, 8),
    _CurrentDaylightSavingFrom_Type()
)
currentDaylightSavingFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDaylightSavingFrom.setStatus("current")
_CurrentDaylightSavingTo_Type = DisplayString
_CurrentDaylightSavingTo_Object = MibScalar
currentDaylightSavingTo = _CurrentDaylightSavingTo_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 4, 2, 9),
    _CurrentDaylightSavingTo_Type()
)
currentDaylightSavingTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDaylightSavingTo.setStatus("current")
_Sfp_ObjectIdentity = ObjectIdentity
sfp = _Sfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5)
)
_SfpSerialInfoTable_Object = MibTable
sfpSerialInfoTable = _SfpSerialInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 1)
)
if mibBuilder.loadTexts:
    sfpSerialInfoTable.setStatus("current")
_SfpSerialInfoEntry_Object = MibTableRow
sfpSerialInfoEntry = _SfpSerialInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 1, 1)
)
sfpSerialInfoEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "sfpPortIndex"),
)
if mibBuilder.loadTexts:
    sfpSerialInfoEntry.setStatus("current")
_SfpPortIndex_Type = DisplayString
_SfpPortIndex_Object = MibTableColumn
sfpPortIndex = _SfpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 1, 1, 1),
    _SfpPortIndex_Type()
)
sfpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpPortIndex.setStatus("current")
_SfpConnector_Type = DisplayString
_SfpConnector_Object = MibTableColumn
sfpConnector = _SfpConnector_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 1, 1, 2),
    _SfpConnector_Type()
)
sfpConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConnector.setStatus("current")
_SfpSpeed_Type = DisplayString
_SfpSpeed_Object = MibTableColumn
sfpSpeed = _SfpSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 1, 1, 3),
    _SfpSpeed_Type()
)
sfpSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpSpeed.setStatus("current")
_SfpVendorName_Type = DisplayString
_SfpVendorName_Object = MibTableColumn
sfpVendorName = _SfpVendorName_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 1, 1, 4),
    _SfpVendorName_Type()
)
sfpVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorName.setStatus("current")
_SfpVendorPn_Type = DisplayString
_SfpVendorPn_Object = MibTableColumn
sfpVendorPn = _SfpVendorPn_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 1, 1, 6),
    _SfpVendorPn_Type()
)
sfpVendorPn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorPn.setStatus("current")
_SpfVendorRev_Type = DisplayString
_SpfVendorRev_Object = MibTableColumn
spfVendorRev = _SpfVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 1, 1, 7),
    _SpfVendorRev_Type()
)
spfVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spfVendorRev.setStatus("current")
_SfpVendorSn_Type = DisplayString
_SfpVendorSn_Object = MibTableColumn
sfpVendorSn = _SfpVendorSn_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 1, 1, 8),
    _SfpVendorSn_Type()
)
sfpVendorSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorSn.setStatus("current")
_SfpDateCode_Type = DisplayString
_SfpDateCode_Object = MibTableColumn
sfpDateCode = _SfpDateCode_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 1, 1, 9),
    _SfpDateCode_Type()
)
sfpDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDateCode.setStatus("current")
_SfpDMIInfoTable_Object = MibTable
sfpDMIInfoTable = _SfpDMIInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 2)
)
if mibBuilder.loadTexts:
    sfpDMIInfoTable.setStatus("current")
_SfpDMIInfoEntry_Object = MibTableRow
sfpDMIInfoEntry = _SfpDMIInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 2, 1)
)
sfpDMIInfoEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "sfpDMIPortIndex"),
)
if mibBuilder.loadTexts:
    sfpDMIInfoEntry.setStatus("current")
_SfpDMIPortIndex_Type = DisplayString
_SfpDMIPortIndex_Object = MibTableColumn
sfpDMIPortIndex = _SfpDMIPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 2, 1, 1),
    _SfpDMIPortIndex_Type()
)
sfpDMIPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDMIPortIndex.setStatus("current")
_SfpDMITemperature_Type = DisplayString
_SfpDMITemperature_Object = MibTableColumn
sfpDMITemperature = _SfpDMITemperature_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 2, 1, 2),
    _SfpDMITemperature_Type()
)
sfpDMITemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDMITemperature.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMITemperature.setUnits("C")
_SfpDMIVoltage_Type = DisplayString
_SfpDMIVoltage_Object = MibTableColumn
sfpDMIVoltage = _SfpDMIVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 2, 1, 3),
    _SfpDMIVoltage_Type()
)
sfpDMIVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDMIVoltage.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMIVoltage.setUnits("V")
_SfpDMITxBias_Type = DisplayString
_SfpDMITxBias_Object = MibTableColumn
sfpDMITxBias = _SfpDMITxBias_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 2, 1, 4),
    _SfpDMITxBias_Type()
)
sfpDMITxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDMITxBias.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMITxBias.setUnits("mA")
_SfpDMITxPower_Type = DisplayString
_SfpDMITxPower_Object = MibTableColumn
sfpDMITxPower = _SfpDMITxPower_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 2, 1, 5),
    _SfpDMITxPower_Type()
)
sfpDMITxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDMITxPower.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMITxPower.setUnits("dbm")
_SfpDMIRxPower_Type = DisplayString
_SfpDMIRxPower_Object = MibTableColumn
sfpDMIRxPower = _SfpDMIRxPower_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 2, 1, 6),
    _SfpDMIRxPower_Type()
)
sfpDMIRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDMIRxPower.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMIRxPower.setUnits("dbm")


class _DdmDiagnosticAlarm_Type(Integer32):
    """Custom type ddmDiagnosticAlarm based on Integer32"""
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
        *(("disabled", 1),
          ("syslog", 2),
          ("email", 3),
          ("snmp", 4))
    )


_DdmDiagnosticAlarm_Type.__name__ = "Integer32"
_DdmDiagnosticAlarm_Object = MibScalar
ddmDiagnosticAlarm = _DdmDiagnosticAlarm_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 3),
    _DdmDiagnosticAlarm_Type()
)
ddmDiagnosticAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmDiagnosticAlarm.setStatus("current")
_SfpDMIAlarmInfoTable_Object = MibTable
sfpDMIAlarmInfoTable = _SfpDMIAlarmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4)
)
if mibBuilder.loadTexts:
    sfpDMIAlarmInfoTable.setStatus("current")
_SfpDMIAlarmInfoEntry_Object = MibTableRow
sfpDMIAlarmInfoEntry = _SfpDMIAlarmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1)
)
sfpDMIAlarmInfoEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "sfpDMIAlarmPortIndex"),
)
if mibBuilder.loadTexts:
    sfpDMIAlarmInfoEntry.setStatus("current")
_SfpDMIAlarmPortIndex_Type = DisplayString
_SfpDMIAlarmPortIndex_Object = MibTableColumn
sfpDMIAlarmPortIndex = _SfpDMIAlarmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 1),
    _SfpDMIAlarmPortIndex_Type()
)
sfpDMIAlarmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDMIAlarmPortIndex.setStatus("current")


class _SfpDMITempHighAlarmState_Type(Integer32):
    """Custom type sfpDMITempHighAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMITempHighAlarmState_Type.__name__ = "Integer32"
_SfpDMITempHighAlarmState_Object = MibTableColumn
sfpDMITempHighAlarmState = _SfpDMITempHighAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 2),
    _SfpDMITempHighAlarmState_Type()
)
sfpDMITempHighAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITempHighAlarmState.setStatus("current")
_SfpDMITempHighAlarmValue_Type = DisplayString
_SfpDMITempHighAlarmValue_Object = MibTableColumn
sfpDMITempHighAlarmValue = _SfpDMITempHighAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 3),
    _SfpDMITempHighAlarmValue_Type()
)
sfpDMITempHighAlarmValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITempHighAlarmValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMITempHighAlarmValue.setUnits("C")


class _SfpDMITempHighWarnState_Type(Integer32):
    """Custom type sfpDMITempHighWarnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMITempHighWarnState_Type.__name__ = "Integer32"
_SfpDMITempHighWarnState_Object = MibTableColumn
sfpDMITempHighWarnState = _SfpDMITempHighWarnState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 4),
    _SfpDMITempHighWarnState_Type()
)
sfpDMITempHighWarnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITempHighWarnState.setStatus("current")
_SfpDMITempHighWarnValue_Type = DisplayString
_SfpDMITempHighWarnValue_Object = MibTableColumn
sfpDMITempHighWarnValue = _SfpDMITempHighWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 5),
    _SfpDMITempHighWarnValue_Type()
)
sfpDMITempHighWarnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITempHighWarnValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMITempHighWarnValue.setUnits("C")


class _SfpDMITempLowAlarmState_Type(Integer32):
    """Custom type sfpDMITempLowAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMITempLowAlarmState_Type.__name__ = "Integer32"
_SfpDMITempLowAlarmState_Object = MibTableColumn
sfpDMITempLowAlarmState = _SfpDMITempLowAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 6),
    _SfpDMITempLowAlarmState_Type()
)
sfpDMITempLowAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITempLowAlarmState.setStatus("current")
_SfpDMITempLowAlarmValue_Type = DisplayString
_SfpDMITempLowAlarmValue_Object = MibTableColumn
sfpDMITempLowAlarmValue = _SfpDMITempLowAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 7),
    _SfpDMITempLowAlarmValue_Type()
)
sfpDMITempLowAlarmValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITempLowAlarmValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMITempLowAlarmValue.setUnits("C")


class _SfpDMITempLowWarnState_Type(Integer32):
    """Custom type sfpDMITempLowWarnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMITempLowWarnState_Type.__name__ = "Integer32"
_SfpDMITempLowWarnState_Object = MibTableColumn
sfpDMITempLowWarnState = _SfpDMITempLowWarnState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 8),
    _SfpDMITempLowWarnState_Type()
)
sfpDMITempLowWarnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITempLowWarnState.setStatus("current")
_SfpDMITempLowWarnValue_Type = DisplayString
_SfpDMITempLowWarnValue_Object = MibTableColumn
sfpDMITempLowWarnValue = _SfpDMITempLowWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 9),
    _SfpDMITempLowWarnValue_Type()
)
sfpDMITempLowWarnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITempLowWarnValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMITempLowWarnValue.setUnits("C")


class _SfpDMIVoltageHighAlarmState_Type(Integer32):
    """Custom type sfpDMIVoltageHighAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMIVoltageHighAlarmState_Type.__name__ = "Integer32"
_SfpDMIVoltageHighAlarmState_Object = MibTableColumn
sfpDMIVoltageHighAlarmState = _SfpDMIVoltageHighAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 10),
    _SfpDMIVoltageHighAlarmState_Type()
)
sfpDMIVoltageHighAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMIVoltageHighAlarmState.setStatus("current")
_SfpDMIVoltageHighAlarmValue_Type = DisplayString
_SfpDMIVoltageHighAlarmValue_Object = MibTableColumn
sfpDMIVoltageHighAlarmValue = _SfpDMIVoltageHighAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 11),
    _SfpDMIVoltageHighAlarmValue_Type()
)
sfpDMIVoltageHighAlarmValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMIVoltageHighAlarmValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMIVoltageHighAlarmValue.setUnits("V")


class _SfpDMIVoltageHighWarnState_Type(Integer32):
    """Custom type sfpDMIVoltageHighWarnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMIVoltageHighWarnState_Type.__name__ = "Integer32"
_SfpDMIVoltageHighWarnState_Object = MibTableColumn
sfpDMIVoltageHighWarnState = _SfpDMIVoltageHighWarnState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 12),
    _SfpDMIVoltageHighWarnState_Type()
)
sfpDMIVoltageHighWarnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMIVoltageHighWarnState.setStatus("current")
_SfpDMIVoltageHighWarnValue_Type = DisplayString
_SfpDMIVoltageHighWarnValue_Object = MibTableColumn
sfpDMIVoltageHighWarnValue = _SfpDMIVoltageHighWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 13),
    _SfpDMIVoltageHighWarnValue_Type()
)
sfpDMIVoltageHighWarnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMIVoltageHighWarnValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMIVoltageHighWarnValue.setUnits("V")


class _SfpDMIVoltageLowAlarmState_Type(Integer32):
    """Custom type sfpDMIVoltageLowAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMIVoltageLowAlarmState_Type.__name__ = "Integer32"
_SfpDMIVoltageLowAlarmState_Object = MibTableColumn
sfpDMIVoltageLowAlarmState = _SfpDMIVoltageLowAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 14),
    _SfpDMIVoltageLowAlarmState_Type()
)
sfpDMIVoltageLowAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMIVoltageLowAlarmState.setStatus("current")
_SfpDMIVoltageLowAlarmValue_Type = DisplayString
_SfpDMIVoltageLowAlarmValue_Object = MibTableColumn
sfpDMIVoltageLowAlarmValue = _SfpDMIVoltageLowAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 15),
    _SfpDMIVoltageLowAlarmValue_Type()
)
sfpDMIVoltageLowAlarmValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMIVoltageLowAlarmValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMIVoltageLowAlarmValue.setUnits("V")


class _SfpDMIVoltageLowWarnState_Type(Integer32):
    """Custom type sfpDMIVoltageLowWarnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMIVoltageLowWarnState_Type.__name__ = "Integer32"
_SfpDMIVoltageLowWarnState_Object = MibTableColumn
sfpDMIVoltageLowWarnState = _SfpDMIVoltageLowWarnState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 16),
    _SfpDMIVoltageLowWarnState_Type()
)
sfpDMIVoltageLowWarnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMIVoltageLowWarnState.setStatus("current")
_SfpDMIVoltageLowWarnValue_Type = DisplayString
_SfpDMIVoltageLowWarnValue_Object = MibTableColumn
sfpDMIVoltageLowWarnValue = _SfpDMIVoltageLowWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 17),
    _SfpDMIVoltageLowWarnValue_Type()
)
sfpDMIVoltageLowWarnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMIVoltageLowWarnValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMIVoltageLowWarnValue.setUnits("V")


class _SfpDMITxBasisHighAlarmState_Type(Integer32):
    """Custom type sfpDMITxBasisHighAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMITxBasisHighAlarmState_Type.__name__ = "Integer32"
_SfpDMITxBasisHighAlarmState_Object = MibTableColumn
sfpDMITxBasisHighAlarmState = _SfpDMITxBasisHighAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 18),
    _SfpDMITxBasisHighAlarmState_Type()
)
sfpDMITxBasisHighAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITxBasisHighAlarmState.setStatus("current")
_SfpDMITxBasisHighAlarmValue_Type = DisplayString
_SfpDMITxBasisHighAlarmValue_Object = MibTableColumn
sfpDMITxBasisHighAlarmValue = _SfpDMITxBasisHighAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 19),
    _SfpDMITxBasisHighAlarmValue_Type()
)
sfpDMITxBasisHighAlarmValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITxBasisHighAlarmValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMITxBasisHighAlarmValue.setUnits("mA")


class _SfpDMITxBasisHighWarnState_Type(Integer32):
    """Custom type sfpDMITxBasisHighWarnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMITxBasisHighWarnState_Type.__name__ = "Integer32"
_SfpDMITxBasisHighWarnState_Object = MibTableColumn
sfpDMITxBasisHighWarnState = _SfpDMITxBasisHighWarnState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 20),
    _SfpDMITxBasisHighWarnState_Type()
)
sfpDMITxBasisHighWarnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITxBasisHighWarnState.setStatus("current")
_SfpDMITxBasisHighWarnValue_Type = DisplayString
_SfpDMITxBasisHighWarnValue_Object = MibTableColumn
sfpDMITxBasisHighWarnValue = _SfpDMITxBasisHighWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 21),
    _SfpDMITxBasisHighWarnValue_Type()
)
sfpDMITxBasisHighWarnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITxBasisHighWarnValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMITxBasisHighWarnValue.setUnits("mA")


class _SfpDMITxBasisLowAlarmState_Type(Integer32):
    """Custom type sfpDMITxBasisLowAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMITxBasisLowAlarmState_Type.__name__ = "Integer32"
_SfpDMITxBasisLowAlarmState_Object = MibTableColumn
sfpDMITxBasisLowAlarmState = _SfpDMITxBasisLowAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 22),
    _SfpDMITxBasisLowAlarmState_Type()
)
sfpDMITxBasisLowAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITxBasisLowAlarmState.setStatus("current")
_SfpDMITxBasisLowAlarmValue_Type = DisplayString
_SfpDMITxBasisLowAlarmValue_Object = MibTableColumn
sfpDMITxBasisLowAlarmValue = _SfpDMITxBasisLowAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 23),
    _SfpDMITxBasisLowAlarmValue_Type()
)
sfpDMITxBasisLowAlarmValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITxBasisLowAlarmValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMITxBasisLowAlarmValue.setUnits("mA")


class _SfpDMITxBasisLowWarnState_Type(Integer32):
    """Custom type sfpDMITxBasisLowWarnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMITxBasisLowWarnState_Type.__name__ = "Integer32"
_SfpDMITxBasisLowWarnState_Object = MibTableColumn
sfpDMITxBasisLowWarnState = _SfpDMITxBasisLowWarnState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 24),
    _SfpDMITxBasisLowWarnState_Type()
)
sfpDMITxBasisLowWarnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITxBasisLowWarnState.setStatus("current")
_SfpDMITxBasisLowWarnValue_Type = DisplayString
_SfpDMITxBasisLowWarnValue_Object = MibTableColumn
sfpDMITxBasisLowWarnValue = _SfpDMITxBasisLowWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 25),
    _SfpDMITxBasisLowWarnValue_Type()
)
sfpDMITxBasisLowWarnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITxBasisLowWarnValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMITxBasisLowWarnValue.setUnits("mA")


class _SfpDMITxPowerHighAlarmState_Type(Integer32):
    """Custom type sfpDMITxPowerHighAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMITxPowerHighAlarmState_Type.__name__ = "Integer32"
_SfpDMITxPowerHighAlarmState_Object = MibTableColumn
sfpDMITxPowerHighAlarmState = _SfpDMITxPowerHighAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 26),
    _SfpDMITxPowerHighAlarmState_Type()
)
sfpDMITxPowerHighAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITxPowerHighAlarmState.setStatus("current")
_SfpDMITxPowerHighAlarmValue_Type = DisplayString
_SfpDMITxPowerHighAlarmValue_Object = MibTableColumn
sfpDMITxPowerHighAlarmValue = _SfpDMITxPowerHighAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 27),
    _SfpDMITxPowerHighAlarmValue_Type()
)
sfpDMITxPowerHighAlarmValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITxPowerHighAlarmValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMITxPowerHighAlarmValue.setUnits("dbm")


class _SfpDMITxPowerHighWarnState_Type(Integer32):
    """Custom type sfpDMITxPowerHighWarnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMITxPowerHighWarnState_Type.__name__ = "Integer32"
_SfpDMITxPowerHighWarnState_Object = MibTableColumn
sfpDMITxPowerHighWarnState = _SfpDMITxPowerHighWarnState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 28),
    _SfpDMITxPowerHighWarnState_Type()
)
sfpDMITxPowerHighWarnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITxPowerHighWarnState.setStatus("current")
_SfpDMITxPowerHighWarnValue_Type = DisplayString
_SfpDMITxPowerHighWarnValue_Object = MibTableColumn
sfpDMITxPowerHighWarnValue = _SfpDMITxPowerHighWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 29),
    _SfpDMITxPowerHighWarnValue_Type()
)
sfpDMITxPowerHighWarnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITxPowerHighWarnValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMITxPowerHighWarnValue.setUnits("dbm")


class _SfpDMITxPowerLowAlarmState_Type(Integer32):
    """Custom type sfpDMITxPowerLowAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMITxPowerLowAlarmState_Type.__name__ = "Integer32"
_SfpDMITxPowerLowAlarmState_Object = MibTableColumn
sfpDMITxPowerLowAlarmState = _SfpDMITxPowerLowAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 30),
    _SfpDMITxPowerLowAlarmState_Type()
)
sfpDMITxPowerLowAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITxPowerLowAlarmState.setStatus("current")
_SfpDMITxPowerLowAlarmValue_Type = DisplayString
_SfpDMITxPowerLowAlarmValue_Object = MibTableColumn
sfpDMITxPowerLowAlarmValue = _SfpDMITxPowerLowAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 31),
    _SfpDMITxPowerLowAlarmValue_Type()
)
sfpDMITxPowerLowAlarmValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITxPowerLowAlarmValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMITxPowerLowAlarmValue.setUnits("dbm")


class _SfpDMITxPowerLowWarnState_Type(Integer32):
    """Custom type sfpDMITxPowerLowWarnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMITxPowerLowWarnState_Type.__name__ = "Integer32"
_SfpDMITxPowerLowWarnState_Object = MibTableColumn
sfpDMITxPowerLowWarnState = _SfpDMITxPowerLowWarnState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 32),
    _SfpDMITxPowerLowWarnState_Type()
)
sfpDMITxPowerLowWarnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITxPowerLowWarnState.setStatus("current")
_SfpDMITxPowerLowWarnValue_Type = DisplayString
_SfpDMITxPowerLowWarnValue_Object = MibTableColumn
sfpDMITxPowerLowWarnValue = _SfpDMITxPowerLowWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 33),
    _SfpDMITxPowerLowWarnValue_Type()
)
sfpDMITxPowerLowWarnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMITxPowerLowWarnValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMITxPowerLowWarnValue.setUnits("dbm")


class _SfpDMIRxPowerHighAlarmState_Type(Integer32):
    """Custom type sfpDMIRxPowerHighAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMIRxPowerHighAlarmState_Type.__name__ = "Integer32"
_SfpDMIRxPowerHighAlarmState_Object = MibTableColumn
sfpDMIRxPowerHighAlarmState = _SfpDMIRxPowerHighAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 34),
    _SfpDMIRxPowerHighAlarmState_Type()
)
sfpDMIRxPowerHighAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMIRxPowerHighAlarmState.setStatus("current")
_SfpDMIRxPowerHighAlarmValue_Type = DisplayString
_SfpDMIRxPowerHighAlarmValue_Object = MibTableColumn
sfpDMIRxPowerHighAlarmValue = _SfpDMIRxPowerHighAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 35),
    _SfpDMIRxPowerHighAlarmValue_Type()
)
sfpDMIRxPowerHighAlarmValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMIRxPowerHighAlarmValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMIRxPowerHighAlarmValue.setUnits("dbm")


class _SfpDMIRxPowerHighWarnState_Type(Integer32):
    """Custom type sfpDMIRxPowerHighWarnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMIRxPowerHighWarnState_Type.__name__ = "Integer32"
_SfpDMIRxPowerHighWarnState_Object = MibTableColumn
sfpDMIRxPowerHighWarnState = _SfpDMIRxPowerHighWarnState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 36),
    _SfpDMIRxPowerHighWarnState_Type()
)
sfpDMIRxPowerHighWarnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMIRxPowerHighWarnState.setStatus("current")
_SfpDMIRxPowerHighWarnValue_Type = DisplayString
_SfpDMIRxPowerHighWarnValue_Object = MibTableColumn
sfpDMIRxPowerHighWarnValue = _SfpDMIRxPowerHighWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 37),
    _SfpDMIRxPowerHighWarnValue_Type()
)
sfpDMIRxPowerHighWarnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMIRxPowerHighWarnValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMIRxPowerHighWarnValue.setUnits("dbm")


class _SfpDMIRxPowerLowAlarmState_Type(Integer32):
    """Custom type sfpDMIRxPowerLowAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMIRxPowerLowAlarmState_Type.__name__ = "Integer32"
_SfpDMIRxPowerLowAlarmState_Object = MibTableColumn
sfpDMIRxPowerLowAlarmState = _SfpDMIRxPowerLowAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 38),
    _SfpDMIRxPowerLowAlarmState_Type()
)
sfpDMIRxPowerLowAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMIRxPowerLowAlarmState.setStatus("current")
_SfpDMIRxPowerLowAlarmValue_Type = DisplayString
_SfpDMIRxPowerLowAlarmValue_Object = MibTableColumn
sfpDMIRxPowerLowAlarmValue = _SfpDMIRxPowerLowAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 39),
    _SfpDMIRxPowerLowAlarmValue_Type()
)
sfpDMIRxPowerLowAlarmValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMIRxPowerLowAlarmValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMIRxPowerLowAlarmValue.setUnits("dbm")


class _SfpDMIRxPowerLowWarnState_Type(Integer32):
    """Custom type sfpDMIRxPowerLowWarnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SfpDMIRxPowerLowWarnState_Type.__name__ = "Integer32"
_SfpDMIRxPowerLowWarnState_Object = MibTableColumn
sfpDMIRxPowerLowWarnState = _SfpDMIRxPowerLowWarnState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 40),
    _SfpDMIRxPowerLowWarnState_Type()
)
sfpDMIRxPowerLowWarnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMIRxPowerLowWarnState.setStatus("current")
_SfpDMIRxPowerLowWarnValue_Type = DisplayString
_SfpDMIRxPowerLowWarnValue_Object = MibTableColumn
sfpDMIRxPowerLowWarnValue = _SfpDMIRxPowerLowWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 5, 4, 1, 41),
    _SfpDMIRxPowerLowWarnValue_Type()
)
sfpDMIRxPowerLowWarnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDMIRxPowerLowWarnValue.setStatus("current")
if mibBuilder.loadTexts:
    sfpDMIRxPowerLowWarnValue.setUnits("dbm")
_DhcpClientOpt82_ObjectIdentity = ObjectIdentity
dhcpClientOpt82 = _DhcpClientOpt82_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 6)
)


class _DhcpClientOpt82Status_Type(Integer32):
    """Custom type dhcpClientOpt82Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_DhcpClientOpt82Status_Type.__name__ = "Integer32"
_DhcpClientOpt82Status_Object = MibScalar
dhcpClientOpt82Status = _DhcpClientOpt82Status_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 6, 1),
    _DhcpClientOpt82Status_Type()
)
dhcpClientOpt82Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientOpt82Status.setStatus("current")


class _DhcpClientOpt82CircuitIDFormat_Type(Integer32):
    """Custom type dhcpClientOpt82CircuitIDFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("string", 1),
          ("hex", 2),
          ("userDefined", 3))
    )


_DhcpClientOpt82CircuitIDFormat_Type.__name__ = "Integer32"
_DhcpClientOpt82CircuitIDFormat_Object = MibScalar
dhcpClientOpt82CircuitIDFormat = _DhcpClientOpt82CircuitIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 6, 2),
    _DhcpClientOpt82CircuitIDFormat_Type()
)
dhcpClientOpt82CircuitIDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientOpt82CircuitIDFormat.setStatus("current")
_DhcpClientOpt82CircuitIDString_Type = DisplayString
_DhcpClientOpt82CircuitIDString_Object = MibScalar
dhcpClientOpt82CircuitIDString = _DhcpClientOpt82CircuitIDString_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 6, 3),
    _DhcpClientOpt82CircuitIDString_Type()
)
dhcpClientOpt82CircuitIDString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientOpt82CircuitIDString.setStatus("current")
_DhcpClientOpt82CircuitIDHex_Type = DisplayString
_DhcpClientOpt82CircuitIDHex_Object = MibScalar
dhcpClientOpt82CircuitIDHex = _DhcpClientOpt82CircuitIDHex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 6, 4),
    _DhcpClientOpt82CircuitIDHex_Type()
)
dhcpClientOpt82CircuitIDHex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientOpt82CircuitIDHex.setStatus("current")
_DhcpClientOpt82CircuitIDUserDefine_Type = DisplayString
_DhcpClientOpt82CircuitIDUserDefine_Object = MibScalar
dhcpClientOpt82CircuitIDUserDefine = _DhcpClientOpt82CircuitIDUserDefine_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 6, 5),
    _DhcpClientOpt82CircuitIDUserDefine_Type()
)
dhcpClientOpt82CircuitIDUserDefine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientOpt82CircuitIDUserDefine.setStatus("current")


class _DhcpClientOpt82RemoteIDFormat_Type(Integer32):
    """Custom type dhcpClientOpt82RemoteIDFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("string", 1),
          ("hex", 2),
          ("userDefined", 3))
    )


_DhcpClientOpt82RemoteIDFormat_Type.__name__ = "Integer32"
_DhcpClientOpt82RemoteIDFormat_Object = MibScalar
dhcpClientOpt82RemoteIDFormat = _DhcpClientOpt82RemoteIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 6, 6),
    _DhcpClientOpt82RemoteIDFormat_Type()
)
dhcpClientOpt82RemoteIDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientOpt82RemoteIDFormat.setStatus("current")
_DhcpClientOpt82RemoteIDString_Type = DisplayString
_DhcpClientOpt82RemoteIDString_Object = MibScalar
dhcpClientOpt82RemoteIDString = _DhcpClientOpt82RemoteIDString_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 6, 7),
    _DhcpClientOpt82RemoteIDString_Type()
)
dhcpClientOpt82RemoteIDString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientOpt82RemoteIDString.setStatus("current")
_DhcpClientOpt82RemoteIDHex_Type = DisplayString
_DhcpClientOpt82RemoteIDHex_Object = MibScalar
dhcpClientOpt82RemoteIDHex = _DhcpClientOpt82RemoteIDHex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 6, 8),
    _DhcpClientOpt82RemoteIDHex_Type()
)
dhcpClientOpt82RemoteIDHex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientOpt82RemoteIDHex.setStatus("current")
_DhcpClientOpt82RemoteIDUserDefine_Type = DisplayString
_DhcpClientOpt82RemoteIDUserDefine_Object = MibScalar
dhcpClientOpt82RemoteIDUserDefine = _DhcpClientOpt82RemoteIDUserDefine_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 6, 9),
    _DhcpClientOpt82RemoteIDUserDefine_Type()
)
dhcpClientOpt82RemoteIDUserDefine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientOpt82RemoteIDUserDefine.setStatus("current")
_NetworkPort_ObjectIdentity = ObjectIdentity
networkPort = _NetworkPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 7)
)


class _HttpNetworkPort_Type(Integer32):
    """Custom type httpNetworkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HttpNetworkPort_Type.__name__ = "Integer32"
_HttpNetworkPort_Object = MibScalar
httpNetworkPort = _HttpNetworkPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 7, 1),
    _HttpNetworkPort_Type()
)
httpNetworkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpNetworkPort.setStatus("current")


class _HttpsNetworkPort_Type(Integer32):
    """Custom type httpsNetworkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HttpsNetworkPort_Type.__name__ = "Integer32"
_HttpsNetworkPort_Object = MibScalar
httpsNetworkPort = _HttpsNetworkPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 7, 2),
    _HttpsNetworkPort_Type()
)
httpsNetworkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpsNetworkPort.setStatus("current")


class _TelnetNetworkPort_Type(Integer32):
    """Custom type telnetNetworkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TelnetNetworkPort_Type.__name__ = "Integer32"
_TelnetNetworkPort_Object = MibScalar
telnetNetworkPort = _TelnetNetworkPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 7, 3),
    _TelnetNetworkPort_Type()
)
telnetNetworkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetNetworkPort.setStatus("current")


class _SshNetworkPort_Type(Integer32):
    """Custom type sshNetworkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SshNetworkPort_Type.__name__ = "Integer32"
_SshNetworkPort_Object = MibScalar
sshNetworkPort = _SshNetworkPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 2, 7, 4),
    _SshNetworkPort_Type()
)
sshNetworkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshNetworkPort.setStatus("current")
_L2switching_ObjectIdentity = ObjectIdentity
l2switching = _L2switching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3)
)
_PortSetting_ObjectIdentity = ObjectIdentity
portSetting = _PortSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 1)
)
_PortSettingTable_Object = MibTable
portSettingTable = _PortSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 1, 1)
)
if mibBuilder.loadTexts:
    portSettingTable.setStatus("current")
_PortSettingEntry_Object = MibTableRow
portSettingEntry = _PortSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 1, 1, 1)
)
portSettingEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "portSettingIndex"),
)
if mibBuilder.loadTexts:
    portSettingEntry.setStatus("current")


class _PortSettingIndex_Type(Integer32):
    """Custom type portSettingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortSettingIndex_Type.__name__ = "Integer32"
_PortSettingIndex_Object = MibTableColumn
portSettingIndex = _PortSettingIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 1, 1, 1, 1),
    _PortSettingIndex_Type()
)
portSettingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSettingIndex.setStatus("current")
_Description_Type = DisplayString
_Description_Object = MibTableColumn
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 1, 1, 1, 2),
    _Description_Type()
)
description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    description.setStatus("current")


class _EnableState_Type(Integer32):
    """Custom type enableState based on Integer32"""
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


_EnableState_Type.__name__ = "Integer32"
_EnableState_Object = MibTableColumn
enableState = _EnableState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 1, 1, 1, 3),
    _EnableState_Type()
)
enableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableState.setStatus("current")


class _LinkStatus_Type(Integer32):
    """Custom type linkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_LinkStatus_Type.__name__ = "Integer32"
_LinkStatus_Object = MibTableColumn
linkStatus = _LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 1, 1, 1, 4),
    _LinkStatus_Type()
)
linkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatus.setStatus("current")


class _Speed_Type(Integer32):
    """Custom type speed based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("auto-10M", 2),
          ("auto-100M", 3),
          ("auto-1000M", 4),
          ("auto-10M-100M", 5),
          ("fixed-10M", 6),
          ("fixed-100M", 7),
          ("fixed-1000M", 8))
    )


_Speed_Type.__name__ = "Integer32"
_Speed_Object = MibTableColumn
speed = _Speed_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 1, 1, 1, 5),
    _Speed_Type()
)
speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speed.setStatus("current")


class _Duplex_Type(Integer32):
    """Custom type duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("half", 2),
          ("full", 3))
    )


_Duplex_Type.__name__ = "Integer32"
_Duplex_Object = MibTableColumn
duplex = _Duplex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 1, 1, 1, 6),
    _Duplex_Type()
)
duplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    duplex.setStatus("current")


class _FlowControlConfig_Type(Integer32):
    """Custom type flowControlConfig based on Integer32"""
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


_FlowControlConfig_Type.__name__ = "Integer32"
_FlowControlConfig_Object = MibTableColumn
flowControlConfig = _FlowControlConfig_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 1, 1, 1, 7),
    _FlowControlConfig_Type()
)
flowControlConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowControlConfig.setStatus("current")


class _FlowControlStatus_Type(Integer32):
    """Custom type flowControlStatus based on Integer32"""
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


_FlowControlStatus_Type.__name__ = "Integer32"
_FlowControlStatus_Object = MibTableColumn
flowControlStatus = _FlowControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 1, 1, 1, 8),
    _FlowControlStatus_Type()
)
flowControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowControlStatus.setStatus("current")
_Mirror_ObjectIdentity = ObjectIdentity
mirror = _Mirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 2)
)
_MirrorTable_Object = MibTable
mirrorTable = _MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mirrorTable.setStatus("current")
_MirrorEntry_Object = MibTableRow
mirrorEntry = _MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 2, 1, 1)
)
mirrorEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "sessionId"),
)
if mibBuilder.loadTexts:
    mirrorEntry.setStatus("current")


class _SessionId_Type(Integer32):
    """Custom type sessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SessionId_Type.__name__ = "Integer32"
_SessionId_Object = MibTableColumn
sessionId = _SessionId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 2, 1, 1, 1),
    _SessionId_Type()
)
sessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionId.setStatus("current")


class _MonitorSessionState_Type(Integer32):
    """Custom type monitorSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port-based", 1),
          ("disable", 2))
    )


_MonitorSessionState_Type.__name__ = "Integer32"
_MonitorSessionState_Object = MibTableColumn
monitorSessionState = _MonitorSessionState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 2, 1, 1, 2),
    _MonitorSessionState_Type()
)
monitorSessionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorSessionState.setStatus("current")
_DestinationPort_Type = Integer32
_DestinationPort_Object = MibTableColumn
destinationPort = _DestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 2, 1, 1, 3),
    _DestinationPort_Type()
)
destinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destinationPort.setStatus("current")


class _IngressState_Type(Integer32):
    """Custom type ingressState based on Integer32"""
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


_IngressState_Type.__name__ = "Integer32"
_IngressState_Object = MibTableColumn
ingressState = _IngressState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 2, 1, 1, 4),
    _IngressState_Type()
)
ingressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressState.setStatus("current")


class _SourceTxPort_Type(Bits):
    """Custom type sourceTxPort based on Bits"""
    namedValues = NamedValues(
        *(("port1", 0),
          ("port2", 1),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11),
          ("port13", 12),
          ("port14", 13),
          ("port15", 14),
          ("port16", 15),
          ("port17", 16),
          ("port18", 17),
          ("port19", 18),
          ("port20", 19),
          ("port21", 20),
          ("port22", 21),
          ("port23", 22),
          ("port24", 23),
          ("port25", 24),
          ("port26", 25),
          ("port27", 26),
          ("port28", 27),
          ("port29", 28),
          ("port30", 29),
          ("port31", 30),
          ("port32", 31))
    )

_SourceTxPort_Type.__name__ = "Bits"
_SourceTxPort_Object = MibTableColumn
sourceTxPort = _SourceTxPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 2, 1, 1, 5),
    _SourceTxPort_Type()
)
sourceTxPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceTxPort.setStatus("current")


class _SourceRxPort_Type(Bits):
    """Custom type sourceRxPort based on Bits"""
    namedValues = NamedValues(
        *(("port1", 0),
          ("port2", 1),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11),
          ("port13", 12),
          ("port14", 13),
          ("port15", 14),
          ("port16", 15),
          ("port17", 16),
          ("port18", 17),
          ("port19", 18),
          ("port20", 19),
          ("port21", 20),
          ("port22", 21),
          ("port23", 22),
          ("port24", 23),
          ("port25", 24),
          ("port26", 25),
          ("port27", 26),
          ("port28", 27),
          ("port29", 28),
          ("port30", 29),
          ("port31", 30),
          ("port32", 31))
    )

_SourceRxPort_Type.__name__ = "Bits"
_SourceRxPort_Object = MibTableColumn
sourceRxPort = _SourceRxPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 2, 1, 1, 6),
    _SourceRxPort_Type()
)
sourceRxPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceRxPort.setStatus("current")
_Lag_ObjectIdentity = ObjectIdentity
lag = _Lag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3)
)


class _LoadBalanceAlgorithm_Type(Integer32):
    """Custom type loadBalanceAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mac-address", 1),
          ("ip-mac-address", 2),
          ("source-port", 3))
    )


_LoadBalanceAlgorithm_Type.__name__ = "Integer32"
_LoadBalanceAlgorithm_Object = MibScalar
loadBalanceAlgorithm = _LoadBalanceAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 1),
    _LoadBalanceAlgorithm_Type()
)
loadBalanceAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadBalanceAlgorithm.setStatus("current")
_LagManagementTable_Object = MibTable
lagManagementTable = _LagManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 2)
)
if mibBuilder.loadTexts:
    lagManagementTable.setStatus("current")
_LagManagementEntry_Object = MibTableRow
lagManagementEntry = _LagManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 2, 1)
)
lagManagementEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "lagIndex"),
)
if mibBuilder.loadTexts:
    lagManagementEntry.setStatus("current")


class _LagIndex_Type(Integer32):
    """Custom type lagIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LagIndex_Type.__name__ = "Integer32"
_LagIndex_Object = MibTableColumn
lagIndex = _LagIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 2, 1, 1),
    _LagIndex_Type()
)
lagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagIndex.setStatus("current")
_LagName_Type = DisplayString
_LagName_Object = MibTableColumn
lagName = _LagName_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 2, 1, 2),
    _LagName_Type()
)
lagName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lagName.setStatus("current")


class _LagType_Type(Integer32):
    """Custom type lagType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("lacp", 2),
          ("none", 3))
    )


_LagType_Type.__name__ = "Integer32"
_LagType_Object = MibTableColumn
lagType = _LagType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 2, 1, 3),
    _LagType_Type()
)
lagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lagType.setStatus("current")


class _LagPorts_Type(Bits):
    """Custom type lagPorts based on Bits"""
    namedValues = NamedValues(
        *(("port1", 0),
          ("port2", 1),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11),
          ("port13", 12),
          ("port14", 13),
          ("port15", 14),
          ("port16", 15),
          ("port17", 16),
          ("port18", 17),
          ("port19", 18),
          ("port20", 19),
          ("port21", 20),
          ("port22", 21),
          ("port23", 22),
          ("port24", 23),
          ("port25", 24),
          ("port26", 25),
          ("port27", 26),
          ("port28", 27),
          ("port29", 28),
          ("port30", 29),
          ("port31", 30),
          ("port32", 31))
    )

_LagPorts_Type.__name__ = "Bits"
_LagPorts_Object = MibTableColumn
lagPorts = _LagPorts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 2, 1, 4),
    _LagPorts_Type()
)
lagPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lagPorts.setStatus("current")


class _LagLinkState_Type(Integer32):
    """Custom type lagLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("not-present", 3))
    )


_LagLinkState_Type.__name__ = "Integer32"
_LagLinkState_Object = MibTableColumn
lagLinkState = _LagLinkState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 2, 1, 5),
    _LagLinkState_Type()
)
lagLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagLinkState.setStatus("current")
_LagActiveMember_Type = DisplayString
_LagActiveMember_Object = MibTableColumn
lagActiveMember = _LagActiveMember_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 2, 1, 6),
    _LagActiveMember_Type()
)
lagActiveMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagActiveMember.setStatus("current")
_LagStandbyMember_Type = DisplayString
_LagStandbyMember_Object = MibTableColumn
lagStandbyMember = _LagStandbyMember_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 2, 1, 7),
    _LagStandbyMember_Type()
)
lagStandbyMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagStandbyMember.setStatus("current")
_LagPortTable_Object = MibTable
lagPortTable = _LagPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 3)
)
if mibBuilder.loadTexts:
    lagPortTable.setStatus("current")
_LagPortEntry_Object = MibTableRow
lagPortEntry = _LagPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 3, 1)
)
lagPortEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "lagPortIndex"),
)
if mibBuilder.loadTexts:
    lagPortEntry.setStatus("current")


class _LagPortIndex_Type(Integer32):
    """Custom type lagPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LagPortIndex_Type.__name__ = "Integer32"
_LagPortIndex_Object = MibTableColumn
lagPortIndex = _LagPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 3, 1, 1),
    _LagPortIndex_Type()
)
lagPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagPortIndex.setStatus("current")
_LagPortDescription_Type = DisplayString
_LagPortDescription_Object = MibTableColumn
lagPortDescription = _LagPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 3, 1, 2),
    _LagPortDescription_Type()
)
lagPortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagPortDescription.setStatus("current")
_LagPortType_Type = DisplayString
_LagPortType_Object = MibTableColumn
lagPortType = _LagPortType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 3, 1, 3),
    _LagPortType_Type()
)
lagPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagPortType.setStatus("current")


class _LagPortEnableState_Type(Integer32):
    """Custom type lagPortEnableState based on Integer32"""
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


_LagPortEnableState_Type.__name__ = "Integer32"
_LagPortEnableState_Object = MibTableColumn
lagPortEnableState = _LagPortEnableState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 3, 1, 4),
    _LagPortEnableState_Type()
)
lagPortEnableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lagPortEnableState.setStatus("current")


class _LagPortLinkStatus_Type(Integer32):
    """Custom type lagPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_LagPortLinkStatus_Type.__name__ = "Integer32"
_LagPortLinkStatus_Object = MibTableColumn
lagPortLinkStatus = _LagPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 3, 1, 5),
    _LagPortLinkStatus_Type()
)
lagPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagPortLinkStatus.setStatus("current")


class _LagPortSpeed_Type(Integer32):
    """Custom type lagPortSpeed based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("auto-10M", 2),
          ("auto-100M", 3),
          ("auto-1000M", 4),
          ("auto-10M-100M", 5),
          ("fixed-10M", 6),
          ("fixed-100M", 7),
          ("fixed-1000M", 8))
    )


_LagPortSpeed_Type.__name__ = "Integer32"
_LagPortSpeed_Object = MibTableColumn
lagPortSpeed = _LagPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 3, 1, 6),
    _LagPortSpeed_Type()
)
lagPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lagPortSpeed.setStatus("current")


class _LagPortDuplex_Type(Integer32):
    """Custom type lagPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("half", 2),
          ("full", 3))
    )


_LagPortDuplex_Type.__name__ = "Integer32"
_LagPortDuplex_Object = MibTableColumn
lagPortDuplex = _LagPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 3, 1, 7),
    _LagPortDuplex_Type()
)
lagPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagPortDuplex.setStatus("current")


class _LagPortFlowCtrlConfig_Type(Integer32):
    """Custom type lagPortFlowCtrlConfig based on Integer32"""
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


_LagPortFlowCtrlConfig_Type.__name__ = "Integer32"
_LagPortFlowCtrlConfig_Object = MibTableColumn
lagPortFlowCtrlConfig = _LagPortFlowCtrlConfig_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 3, 1, 8),
    _LagPortFlowCtrlConfig_Type()
)
lagPortFlowCtrlConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lagPortFlowCtrlConfig.setStatus("current")


class _LagPortFlowCtrlStatus_Type(Integer32):
    """Custom type lagPortFlowCtrlStatus based on Integer32"""
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


_LagPortFlowCtrlStatus_Type.__name__ = "Integer32"
_LagPortFlowCtrlStatus_Object = MibTableColumn
lagPortFlowCtrlStatus = _LagPortFlowCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 3, 1, 9),
    _LagPortFlowCtrlStatus_Type()
)
lagPortFlowCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagPortFlowCtrlStatus.setStatus("current")


class _LacpSystemPriority_Type(Integer32):
    """Custom type lacpSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LacpSystemPriority_Type.__name__ = "Integer32"
_LacpSystemPriority_Object = MibScalar
lacpSystemPriority = _LacpSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 4),
    _LacpSystemPriority_Type()
)
lacpSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpSystemPriority.setStatus("current")
_LacpPortTable_Object = MibTable
lacpPortTable = _LacpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 5)
)
if mibBuilder.loadTexts:
    lacpPortTable.setStatus("current")
_LacpPortEntry_Object = MibTableRow
lacpPortEntry = _LacpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 5, 1)
)
lacpPortEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "lacpPortIndex"),
)
if mibBuilder.loadTexts:
    lacpPortEntry.setStatus("current")


class _LacpPortIndex_Type(Integer32):
    """Custom type lacpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LacpPortIndex_Type.__name__ = "Integer32"
_LacpPortIndex_Object = MibTableColumn
lacpPortIndex = _LacpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 5, 1, 1),
    _LacpPortIndex_Type()
)
lacpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpPortIndex.setStatus("current")


class _LacpPriority_Type(Integer32):
    """Custom type lacpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LacpPriority_Type.__name__ = "Integer32"
_LacpPriority_Object = MibTableColumn
lacpPriority = _LacpPriority_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 5, 1, 2),
    _LacpPriority_Type()
)
lacpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpPriority.setStatus("current")


class _LacpTimeout_Type(Integer32):
    """Custom type lacpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("short", 2))
    )


_LacpTimeout_Type.__name__ = "Integer32"
_LacpTimeout_Object = MibTableColumn
lacpTimeout = _LacpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 5, 1, 3),
    _LacpTimeout_Type()
)
lacpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpTimeout.setStatus("current")


class _LacpPortMode_Type(Integer32):
    """Custom type lacpPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_LacpPortMode_Type.__name__ = "Integer32"
_LacpPortMode_Object = MibTableColumn
lacpPortMode = _LacpPortMode_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 3, 5, 1, 4),
    _LacpPortMode_Type()
)
lacpPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpPortMode.setStatus("current")
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4)
)
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 1)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 1, 1)
)
vlanEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "vlanIndex"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")


class _VlanIndex_Type(Integer32):
    """Custom type vlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanIndex_Type.__name__ = "Integer32"
_VlanIndex_Object = MibTableColumn
vlanIndex = _VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 1, 1, 1),
    _VlanIndex_Type()
)
vlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIndex.setStatus("current")


class _VlanId_Type(Integer32):
    """Custom type vlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanId_Type.__name__ = "Integer32"
_VlanId_Object = MibTableColumn
vlanId = _VlanId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 1, 1, 2),
    _VlanId_Type()
)
vlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanId.setStatus("current")
_VlanNamePrefix_Type = DisplayString
_VlanNamePrefix_Object = MibTableColumn
vlanNamePrefix = _VlanNamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 1, 1, 3),
    _VlanNamePrefix_Type()
)
vlanNamePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanNamePrefix.setStatus("current")


class _VlanType_Type(Integer32):
    """Custom type vlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("static", 2),
          ("dyanmic", 3))
    )


_VlanType_Type.__name__ = "Integer32"
_VlanType_Object = MibTableColumn
vlanType = _VlanType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 1, 1, 4),
    _VlanType_Type()
)
vlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanType.setStatus("current")


class _VlanRowStatus_Type(Integer32):
    """Custom type vlanRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("createAndWait", 5),
          ("destory", 6))
    )


_VlanRowStatus_Type.__name__ = "Integer32"
_VlanRowStatus_Object = MibTableColumn
vlanRowStatus = _VlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 1, 1, 99),
    _VlanRowStatus_Type()
)
vlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanRowStatus.setStatus("current")
_VlanInterfaceTable_Object = MibTable
vlanInterfaceTable = _VlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 2)
)
if mibBuilder.loadTexts:
    vlanInterfaceTable.setStatus("current")
_VlanInterfaceEntry_Object = MibTableRow
vlanInterfaceEntry = _VlanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 2, 1)
)
vlanInterfaceEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "vlanPortIndex"),
)
if mibBuilder.loadTexts:
    vlanInterfaceEntry.setStatus("current")


class _VlanPortIndex_Type(Integer32):
    """Custom type vlanPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlanPortIndex_Type.__name__ = "Integer32"
_VlanPortIndex_Object = MibTableColumn
vlanPortIndex = _VlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 2, 1, 1),
    _VlanPortIndex_Type()
)
vlanPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortIndex.setStatus("current")


class _VlanInterfaceVlanMode_Type(Integer32):
    """Custom type vlanInterfaceVlanMode based on Integer32"""
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
        *(("hybrid", 1),
          ("access", 2),
          ("trunk", 3),
          ("tunnel", 4))
    )


_VlanInterfaceVlanMode_Type.__name__ = "Integer32"
_VlanInterfaceVlanMode_Object = MibTableColumn
vlanInterfaceVlanMode = _VlanInterfaceVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 2, 1, 2),
    _VlanInterfaceVlanMode_Type()
)
vlanInterfaceVlanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanInterfaceVlanMode.setStatus("current")


class _VlanPvid_Type(Integer32):
    """Custom type vlanPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanPvid_Type.__name__ = "Integer32"
_VlanPvid_Object = MibTableColumn
vlanPvid = _VlanPvid_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 2, 1, 3),
    _VlanPvid_Type()
)
vlanPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPvid.setStatus("current")


class _VlanAcceptedType_Type(Integer32):
    """Custom type vlanAcceptedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("tag-only", 2),
          ("untag-only", 3))
    )


_VlanAcceptedType_Type.__name__ = "Integer32"
_VlanAcceptedType_Object = MibTableColumn
vlanAcceptedType = _VlanAcceptedType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 2, 1, 4),
    _VlanAcceptedType_Type()
)
vlanAcceptedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanAcceptedType.setStatus("current")


class _VlanIngressFiltering_Type(Integer32):
    """Custom type vlanIngressFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disbale", 2))
    )


_VlanIngressFiltering_Type.__name__ = "Integer32"
_VlanIngressFiltering_Object = MibTableColumn
vlanIngressFiltering = _VlanIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 2, 1, 5),
    _VlanIngressFiltering_Type()
)
vlanIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIngressFiltering.setStatus("current")
_PortToVlanTable_Object = MibTable
portToVlanTable = _PortToVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 3)
)
if mibBuilder.loadTexts:
    portToVlanTable.setStatus("current")
_PortToVlanEntry_Object = MibTableRow
portToVlanEntry = _PortToVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 3, 1)
)
portToVlanEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "portToVlanVlanIndex"),
)
if mibBuilder.loadTexts:
    portToVlanEntry.setStatus("current")


class _PortToVlanVlanIndex_Type(Integer32):
    """Custom type portToVlanVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PortToVlanVlanIndex_Type.__name__ = "Integer32"
_PortToVlanVlanIndex_Object = MibTableColumn
portToVlanVlanIndex = _PortToVlanVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 3, 1, 1),
    _PortToVlanVlanIndex_Type()
)
portToVlanVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portToVlanVlanIndex.setStatus("current")


class _PortToVlanPortIndex_Type(Integer32):
    """Custom type portToVlanPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortToVlanPortIndex_Type.__name__ = "Integer32"
_PortToVlanPortIndex_Object = MibTableColumn
portToVlanPortIndex = _PortToVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 3, 1, 2),
    _PortToVlanPortIndex_Type()
)
portToVlanPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portToVlanPortIndex.setStatus("current")
_PortToVlanVlanId_Type = Integer32
_PortToVlanVlanId_Object = MibTableColumn
portToVlanVlanId = _PortToVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 3, 1, 3),
    _PortToVlanVlanId_Type()
)
portToVlanVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portToVlanVlanId.setStatus("current")


class _PortToVlanInterfaceVlanMode_Type(Integer32):
    """Custom type portToVlanInterfaceVlanMode based on Integer32"""
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
        *(("hybrid", 1),
          ("access", 2),
          ("trunk", 3),
          ("tunnel", 4))
    )


_PortToVlanInterfaceVlanMode_Type.__name__ = "Integer32"
_PortToVlanInterfaceVlanMode_Object = MibTableColumn
portToVlanInterfaceVlanMode = _PortToVlanInterfaceVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 3, 1, 4),
    _PortToVlanInterfaceVlanMode_Type()
)
portToVlanInterfaceVlanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portToVlanInterfaceVlanMode.setStatus("current")


class _PortToVlanMembership_Type(Integer32):
    """Custom type portToVlanMembership based on Integer32"""
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
        *(("forbidden", 1),
          ("exclued", 2),
          ("tagged", 3),
          ("untagged", 4))
    )


_PortToVlanMembership_Type.__name__ = "Integer32"
_PortToVlanMembership_Object = MibTableColumn
portToVlanMembership = _PortToVlanMembership_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 3, 1, 5),
    _PortToVlanMembership_Type()
)
portToVlanMembership.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portToVlanMembership.setStatus("current")


class _PortToVlanPvid_Type(Integer32):
    """Custom type portToVlanPvid based on Integer32"""
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


_PortToVlanPvid_Type.__name__ = "Integer32"
_PortToVlanPvid_Object = MibTableColumn
portToVlanPvid = _PortToVlanPvid_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 3, 1, 6),
    _PortToVlanPvid_Type()
)
portToVlanPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portToVlanPvid.setStatus("current")
_PortVlanTable_Object = MibTable
portVlanTable = _PortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 4)
)
if mibBuilder.loadTexts:
    portVlanTable.setStatus("current")
_PortVlanEntry_Object = MibTableRow
portVlanEntry = _PortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 4, 1)
)
portVlanEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "portVlanPortIndex"),
)
if mibBuilder.loadTexts:
    portVlanEntry.setStatus("current")


class _PortVlanPortIndex_Type(Integer32):
    """Custom type portVlanPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortVlanPortIndex_Type.__name__ = "Integer32"
_PortVlanPortIndex_Object = MibTableColumn
portVlanPortIndex = _PortVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 4, 1, 1),
    _PortVlanPortIndex_Type()
)
portVlanPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVlanPortIndex.setStatus("current")


class _PortVlanPortMode_Type(Integer32):
    """Custom type portVlanPortMode based on Integer32"""
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
        *(("hybrid", 1),
          ("access", 2),
          ("trunk", 3),
          ("tunnel", 4))
    )


_PortVlanPortMode_Type.__name__ = "Integer32"
_PortVlanPortMode_Object = MibTableColumn
portVlanPortMode = _PortVlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 4, 1, 2),
    _PortVlanPortMode_Type()
)
portVlanPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVlanPortMode.setStatus("current")
_PortVlanAdminVlans_Type = DisplayString
_PortVlanAdminVlans_Object = MibTableColumn
portVlanAdminVlans = _PortVlanAdminVlans_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 4, 1, 3),
    _PortVlanAdminVlans_Type()
)
portVlanAdminVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVlanAdminVlans.setStatus("current")
_PortVlanOperVlans_Type = DisplayString
_PortVlanOperVlans_Object = MibTableColumn
portVlanOperVlans = _PortVlanOperVlans_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 4, 1, 4),
    _PortVlanOperVlans_Type()
)
portVlanOperVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVlanOperVlans.setStatus("current")
_VoiceVlan_ObjectIdentity = ObjectIdentity
voiceVlan = _VoiceVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 5)
)


class _VoiceVlanState_Type(Integer32):
    """Custom type voiceVlanState based on Integer32"""
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


_VoiceVlanState_Type.__name__ = "Integer32"
_VoiceVlanState_Object = MibScalar
voiceVlanState = _VoiceVlanState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 5, 1),
    _VoiceVlanState_Type()
)
voiceVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanState.setStatus("current")


class _VoiceVlanId_Type(Integer32):
    """Custom type voiceVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VoiceVlanId_Type.__name__ = "Integer32"
_VoiceVlanId_Object = MibScalar
voiceVlanId = _VoiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 5, 2),
    _VoiceVlanId_Type()
)
voiceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanId.setStatus("current")


class _VoiceVlanRemarkCos_8021p_Type(Integer32):
    """Custom type voiceVlanRemarkCos_8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VoiceVlanRemarkCos_8021p_Type.__name__ = "Integer32"
_VoiceVlanRemarkCos_8021p_Object = MibScalar
voiceVlanRemarkCos_8021p = _VoiceVlanRemarkCos_8021p_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 5, 3),
    _VoiceVlanRemarkCos_8021p_Type()
)
voiceVlanRemarkCos_8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanRemarkCos_8021p.setStatus("current")


class _VoiceVlanRemark1q_Type(Integer32):
    """Custom type voiceVlanRemark1q based on Integer32"""
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


_VoiceVlanRemark1q_Type.__name__ = "Integer32"
_VoiceVlanRemark1q_Object = MibScalar
voiceVlanRemark1q = _VoiceVlanRemark1q_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 5, 4),
    _VoiceVlanRemark1q_Type()
)
voiceVlanRemark1q.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanRemark1q.setStatus("current")


class _VoiceVlanAgingTime_Type(Integer32):
    """Custom type voiceVlanAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 65535),
    )


_VoiceVlanAgingTime_Type.__name__ = "Integer32"
_VoiceVlanAgingTime_Object = MibScalar
voiceVlanAgingTime = _VoiceVlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 5, 5),
    _VoiceVlanAgingTime_Type()
)
voiceVlanAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanAgingTime.setStatus("current")
_TelephonyOUITable_Object = MibTable
telephonyOUITable = _TelephonyOUITable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 5, 6)
)
if mibBuilder.loadTexts:
    telephonyOUITable.setStatus("current")
_TelephonyOUIEntry_Object = MibTableRow
telephonyOUIEntry = _TelephonyOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 5, 6, 1)
)
telephonyOUIEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "telephonyOUIIndex"),
)
if mibBuilder.loadTexts:
    telephonyOUIEntry.setStatus("current")


class _TelephonyOUIIndex_Type(Integer32):
    """Custom type telephonyOUIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TelephonyOUIIndex_Type.__name__ = "Integer32"
_TelephonyOUIIndex_Object = MibTableColumn
telephonyOUIIndex = _TelephonyOUIIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 5, 6, 1, 1),
    _TelephonyOUIIndex_Type()
)
telephonyOUIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyOUIIndex.setStatus("current")
_TelephonyOUIAddress_Type = DisplayString
_TelephonyOUIAddress_Object = MibTableColumn
telephonyOUIAddress = _TelephonyOUIAddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 5, 6, 1, 2),
    _TelephonyOUIAddress_Type()
)
telephonyOUIAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyOUIAddress.setStatus("current")
_TelephonyOUIDescription_Type = DisplayString
_TelephonyOUIDescription_Object = MibTableColumn
telephonyOUIDescription = _TelephonyOUIDescription_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 5, 6, 1, 3),
    _TelephonyOUIDescription_Type()
)
telephonyOUIDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyOUIDescription.setStatus("current")


class _TelephonyOUIRowStatus_Type(Integer32):
    """Custom type telephonyOUIRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("createAndWait", 5),
          ("destory", 6))
    )


_TelephonyOUIRowStatus_Type.__name__ = "Integer32"
_TelephonyOUIRowStatus_Object = MibTableColumn
telephonyOUIRowStatus = _TelephonyOUIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 5, 6, 1, 99),
    _TelephonyOUIRowStatus_Type()
)
telephonyOUIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telephonyOUIRowStatus.setStatus("current")
_TelephonyOUIPortTable_Object = MibTable
telephonyOUIPortTable = _TelephonyOUIPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 5, 7)
)
if mibBuilder.loadTexts:
    telephonyOUIPortTable.setStatus("current")
_TelephonyOUIPortEntry_Object = MibTableRow
telephonyOUIPortEntry = _TelephonyOUIPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 5, 7, 1)
)
telephonyOUIPortEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "telephonyOUIPortIndex"),
)
if mibBuilder.loadTexts:
    telephonyOUIPortEntry.setStatus("current")


class _TelephonyOUIPortIndex_Type(Integer32):
    """Custom type telephonyOUIPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TelephonyOUIPortIndex_Type.__name__ = "Integer32"
_TelephonyOUIPortIndex_Object = MibTableColumn
telephonyOUIPortIndex = _TelephonyOUIPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 5, 7, 1, 1),
    _TelephonyOUIPortIndex_Type()
)
telephonyOUIPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyOUIPortIndex.setStatus("current")


class _TelephonyOUIState_Type(Integer32):
    """Custom type telephonyOUIState based on Integer32"""
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


_TelephonyOUIState_Type.__name__ = "Integer32"
_TelephonyOUIState_Object = MibTableColumn
telephonyOUIState = _TelephonyOUIState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 5, 7, 1, 2),
    _TelephonyOUIState_Type()
)
telephonyOUIState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyOUIState.setStatus("current")


class _TelephonyOUICosMode_Type(Integer32):
    """Custom type telephonyOUICosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("src", 2))
    )


_TelephonyOUICosMode_Type.__name__ = "Integer32"
_TelephonyOUICosMode_Object = MibTableColumn
telephonyOUICosMode = _TelephonyOUICosMode_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 5, 7, 1, 3),
    _TelephonyOUICosMode_Type()
)
telephonyOUICosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyOUICosMode.setStatus("current")
_InterfaceVlanTable_Object = MibTable
interfaceVlanTable = _InterfaceVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 6)
)
if mibBuilder.loadTexts:
    interfaceVlanTable.setStatus("current")
_InterfaceVlanEntry_Object = MibTableRow
interfaceVlanEntry = _InterfaceVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 6, 1)
)
interfaceVlanEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "interfaceVlanIndex"),
)
if mibBuilder.loadTexts:
    interfaceVlanEntry.setStatus("current")


class _InterfaceVlanIndex_Type(Integer32):
    """Custom type interfaceVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_InterfaceVlanIndex_Type.__name__ = "Integer32"
_InterfaceVlanIndex_Object = MibTableColumn
interfaceVlanIndex = _InterfaceVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 6, 1, 1),
    _InterfaceVlanIndex_Type()
)
interfaceVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceVlanIndex.setStatus("current")


class _InterfaceVlanId_Type(Integer32):
    """Custom type interfaceVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_InterfaceVlanId_Type.__name__ = "Integer32"
_InterfaceVlanId_Object = MibTableColumn
interfaceVlanId = _InterfaceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 6, 1, 2),
    _InterfaceVlanId_Type()
)
interfaceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceVlanId.setStatus("current")
_InterfaceVlanName_Type = DisplayString
_InterfaceVlanName_Object = MibTableColumn
interfaceVlanName = _InterfaceVlanName_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 6, 1, 3),
    _InterfaceVlanName_Type()
)
interfaceVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceVlanName.setStatus("current")


class _InterfaceVlanRowStatus_Type(Integer32):
    """Custom type interfaceVlanRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("createAndWait", 5),
          ("destory", 6))
    )


_InterfaceVlanRowStatus_Type.__name__ = "Integer32"
_InterfaceVlanRowStatus_Object = MibTableColumn
interfaceVlanRowStatus = _InterfaceVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 4, 6, 1, 99),
    _InterfaceVlanRowStatus_Type()
)
interfaceVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    interfaceVlanRowStatus.setStatus("current")
_Eee_ObjectIdentity = ObjectIdentity
eee = _Eee_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 5)
)
_EeePortTable_Object = MibTable
eeePortTable = _EeePortTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 5, 1)
)
if mibBuilder.loadTexts:
    eeePortTable.setStatus("current")
_EeePortEntry_Object = MibTableRow
eeePortEntry = _EeePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 5, 1, 1)
)
eeePortEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "eeePortIndex"),
)
if mibBuilder.loadTexts:
    eeePortEntry.setStatus("current")


class _EeePortIndex_Type(Integer32):
    """Custom type eeePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EeePortIndex_Type.__name__ = "Integer32"
_EeePortIndex_Object = MibTableColumn
eeePortIndex = _EeePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 5, 1, 1, 1),
    _EeePortIndex_Type()
)
eeePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eeePortIndex.setStatus("current")


class _EeeState_Type(Integer32):
    """Custom type eeeState based on Integer32"""
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


_EeeState_Type.__name__ = "Integer32"
_EeeState_Object = MibTableColumn
eeeState = _EeeState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 5, 1, 1, 2),
    _EeeState_Type()
)
eeeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eeeState.setStatus("current")
_Multicast_ObjectIdentity = ObjectIdentity
multicast = _Multicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6)
)


class _UnknownMulticastAction_Type(Integer32):
    """Custom type unknownMulticastAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("flood", 2),
          ("routerPort", 3))
    )


_UnknownMulticastAction_Type.__name__ = "Integer32"
_UnknownMulticastAction_Object = MibScalar
unknownMulticastAction = _UnknownMulticastAction_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 1),
    _UnknownMulticastAction_Type()
)
unknownMulticastAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unknownMulticastAction.setStatus("current")


class _ForwardMethod_Type(Integer32):
    """Custom type forwardMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mac", 1)
    )


_ForwardMethod_Type.__name__ = "Integer32"
_ForwardMethod_Object = MibScalar
forwardMethod = _ForwardMethod_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 2),
    _ForwardMethod_Type()
)
forwardMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardMethod.setStatus("current")
_IgmpSnooping_ObjectIdentity = ObjectIdentity
igmpSnooping = _IgmpSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3)
)


class _IgmpSnoopingState_Type(Integer32):
    """Custom type igmpSnoopingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disabled", 2))
    )


_IgmpSnoopingState_Type.__name__ = "Integer32"
_IgmpSnoopingState_Object = MibScalar
igmpSnoopingState = _IgmpSnoopingState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 1),
    _IgmpSnoopingState_Type()
)
igmpSnoopingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingState.setStatus("current")


class _IgmpSnoopingVersion_Type(Integer32):
    """Custom type igmpSnoopingVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v2", 1),
          ("v3", 2))
    )


_IgmpSnoopingVersion_Type.__name__ = "Integer32"
_IgmpSnoopingVersion_Object = MibScalar
igmpSnoopingVersion = _IgmpSnoopingVersion_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 2),
    _IgmpSnoopingVersion_Type()
)
igmpSnoopingVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingVersion.setStatus("current")


class _IgmpSnoopingReportSuppression_Type(Integer32):
    """Custom type igmpSnoopingReportSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disabled", 2))
    )


_IgmpSnoopingReportSuppression_Type.__name__ = "Integer32"
_IgmpSnoopingReportSuppression_Object = MibScalar
igmpSnoopingReportSuppression = _IgmpSnoopingReportSuppression_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 3),
    _IgmpSnoopingReportSuppression_Type()
)
igmpSnoopingReportSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingReportSuppression.setStatus("current")
_IgmpSnoopingTable_Object = MibTable
igmpSnoopingTable = _IgmpSnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 4)
)
if mibBuilder.loadTexts:
    igmpSnoopingTable.setStatus("current")
_IgmpSnoopingEntry_Object = MibTableRow
igmpSnoopingEntry = _IgmpSnoopingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 4, 1)
)
igmpSnoopingEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "igmpSnoopingIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopingEntry.setStatus("current")


class _IgmpSnoopingIndex_Type(Integer32):
    """Custom type igmpSnoopingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgmpSnoopingIndex_Type.__name__ = "Integer32"
_IgmpSnoopingIndex_Object = MibTableColumn
igmpSnoopingIndex = _IgmpSnoopingIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 4, 1, 1),
    _IgmpSnoopingIndex_Type()
)
igmpSnoopingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingIndex.setStatus("current")


class _IgmpSnoopingVlanId_Type(Integer32):
    """Custom type igmpSnoopingVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4904),
    )


_IgmpSnoopingVlanId_Type.__name__ = "Integer32"
_IgmpSnoopingVlanId_Object = MibTableColumn
igmpSnoopingVlanId = _IgmpSnoopingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 4, 1, 2),
    _IgmpSnoopingVlanId_Type()
)
igmpSnoopingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingVlanId.setStatus("current")


class _IgmpSnoopStatus_Type(Integer32):
    """Custom type igmpSnoopStatus based on Integer32"""
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


_IgmpSnoopStatus_Type.__name__ = "Integer32"
_IgmpSnoopStatus_Object = MibTableColumn
igmpSnoopStatus = _IgmpSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 4, 1, 3),
    _IgmpSnoopStatus_Type()
)
igmpSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopStatus.setStatus("current")


class _RouterPortsAutoLearn_Type(Integer32):
    """Custom type routerPortsAutoLearn based on Integer32"""
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


_RouterPortsAutoLearn_Type.__name__ = "Integer32"
_RouterPortsAutoLearn_Object = MibTableColumn
routerPortsAutoLearn = _RouterPortsAutoLearn_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 4, 1, 4),
    _RouterPortsAutoLearn_Type()
)
routerPortsAutoLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routerPortsAutoLearn.setStatus("current")


class _QueryRobustness_Type(Integer32):
    """Custom type queryRobustness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_QueryRobustness_Type.__name__ = "Integer32"
_QueryRobustness_Object = MibTableColumn
queryRobustness = _QueryRobustness_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 4, 1, 5),
    _QueryRobustness_Type()
)
queryRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queryRobustness.setStatus("current")


class _QueryInterval_Type(Integer32):
    """Custom type queryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 18000),
    )


_QueryInterval_Type.__name__ = "Integer32"
_QueryInterval_Object = MibTableColumn
queryInterval = _QueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 4, 1, 6),
    _QueryInterval_Type()
)
queryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queryInterval.setStatus("current")


class _QueryMaxResponseInterval_Type(Integer32):
    """Custom type queryMaxResponseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_QueryMaxResponseInterval_Type.__name__ = "Integer32"
_QueryMaxResponseInterval_Object = MibTableColumn
queryMaxResponseInterval = _QueryMaxResponseInterval_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 4, 1, 7),
    _QueryMaxResponseInterval_Type()
)
queryMaxResponseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queryMaxResponseInterval.setStatus("current")


class _LastMemberQueryCounter_Type(Integer32):
    """Custom type lastMemberQueryCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_LastMemberQueryCounter_Type.__name__ = "Integer32"
_LastMemberQueryCounter_Object = MibTableColumn
lastMemberQueryCounter = _LastMemberQueryCounter_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 4, 1, 8),
    _LastMemberQueryCounter_Type()
)
lastMemberQueryCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lastMemberQueryCounter.setStatus("current")


class _LastMemberQueryInterval_Type(Integer32):
    """Custom type lastMemberQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_LastMemberQueryInterval_Type.__name__ = "Integer32"
_LastMemberQueryInterval_Object = MibTableColumn
lastMemberQueryInterval = _LastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 4, 1, 9),
    _LastMemberQueryInterval_Type()
)
lastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lastMemberQueryInterval.setStatus("current")


class _ImmediateLeave_Type(Integer32):
    """Custom type immediateLeave based on Integer32"""
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


_ImmediateLeave_Type.__name__ = "Integer32"
_ImmediateLeave_Object = MibTableColumn
immediateLeave = _ImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 4, 1, 10),
    _ImmediateLeave_Type()
)
immediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    immediateLeave.setStatus("current")
_OperQueryRobustness_Type = Integer32
_OperQueryRobustness_Object = MibTableColumn
operQueryRobustness = _OperQueryRobustness_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 4, 1, 11),
    _OperQueryRobustness_Type()
)
operQueryRobustness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operQueryRobustness.setStatus("current")
_OperQueryInterval_Type = Integer32
_OperQueryInterval_Object = MibTableColumn
operQueryInterval = _OperQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 4, 1, 12),
    _OperQueryInterval_Type()
)
operQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operQueryInterval.setStatus("current")
_OperQueryMaxResponseInterval_Type = Integer32
_OperQueryMaxResponseInterval_Object = MibTableColumn
operQueryMaxResponseInterval = _OperQueryMaxResponseInterval_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 4, 1, 13),
    _OperQueryMaxResponseInterval_Type()
)
operQueryMaxResponseInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operQueryMaxResponseInterval.setStatus("current")
_OperLastMemberQueryCounter_Type = Integer32
_OperLastMemberQueryCounter_Object = MibTableColumn
operLastMemberQueryCounter = _OperLastMemberQueryCounter_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 4, 1, 14),
    _OperLastMemberQueryCounter_Type()
)
operLastMemberQueryCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operLastMemberQueryCounter.setStatus("current")
_OperLastMemberQueryInterval_Type = Integer32
_OperLastMemberQueryInterval_Object = MibTableColumn
operLastMemberQueryInterval = _OperLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 4, 1, 15),
    _OperLastMemberQueryInterval_Type()
)
operLastMemberQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operLastMemberQueryInterval.setStatus("current")
_IgmpQuerierTable_Object = MibTable
igmpQuerierTable = _IgmpQuerierTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 5)
)
if mibBuilder.loadTexts:
    igmpQuerierTable.setStatus("current")
_IgmpQuerierEntry_Object = MibTableRow
igmpQuerierEntry = _IgmpQuerierEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 5, 1)
)
igmpQuerierEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "igmpQuerierVlanId"),
)
if mibBuilder.loadTexts:
    igmpQuerierEntry.setStatus("current")


class _IgmpQuerierVlanId_Type(Integer32):
    """Custom type igmpQuerierVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgmpQuerierVlanId_Type.__name__ = "Integer32"
_IgmpQuerierVlanId_Object = MibTableColumn
igmpQuerierVlanId = _IgmpQuerierVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 5, 1, 1),
    _IgmpQuerierVlanId_Type()
)
igmpQuerierVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpQuerierVlanId.setStatus("current")


class _IgmpQuerierState_Type(Integer32):
    """Custom type igmpQuerierState based on Integer32"""
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


_IgmpQuerierState_Type.__name__ = "Integer32"
_IgmpQuerierState_Object = MibTableColumn
igmpQuerierState = _IgmpQuerierState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 5, 1, 2),
    _IgmpQuerierState_Type()
)
igmpQuerierState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpQuerierState.setStatus("current")


class _IgmpQuerierStatus_Type(Integer32):
    """Custom type igmpQuerierStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("querier", 1),
          ("nonQuerier", 2))
    )


_IgmpQuerierStatus_Type.__name__ = "Integer32"
_IgmpQuerierStatus_Object = MibTableColumn
igmpQuerierStatus = _IgmpQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 5, 1, 3),
    _IgmpQuerierStatus_Type()
)
igmpQuerierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpQuerierStatus.setStatus("current")


class _IgmpQuerierVersion_Type(Integer32):
    """Custom type igmpQuerierVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v2", 1),
          ("v3", 2))
    )


_IgmpQuerierVersion_Type.__name__ = "Integer32"
_IgmpQuerierVersion_Object = MibTableColumn
igmpQuerierVersion = _IgmpQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 5, 1, 4),
    _IgmpQuerierVersion_Type()
)
igmpQuerierVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpQuerierVersion.setStatus("current")
_IgmpQuerierIP_Type = DisplayString
_IgmpQuerierIP_Object = MibTableColumn
igmpQuerierIP = _IgmpQuerierIP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 5, 1, 5),
    _IgmpQuerierIP_Type()
)
igmpQuerierIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpQuerierIP.setStatus("current")
_IgmpStaticGroupTable_Object = MibTable
igmpStaticGroupTable = _IgmpStaticGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 6)
)
if mibBuilder.loadTexts:
    igmpStaticGroupTable.setStatus("current")
_IgmpStaticGroupEntry_Object = MibTableRow
igmpStaticGroupEntry = _IgmpStaticGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 6, 1)
)
igmpStaticGroupEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "igmpStaticGroupIndex"),
)
if mibBuilder.loadTexts:
    igmpStaticGroupEntry.setStatus("current")


class _IgmpStaticGroupIndex_Type(Integer32):
    """Custom type igmpStaticGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_IgmpStaticGroupIndex_Type.__name__ = "Integer32"
_IgmpStaticGroupIndex_Object = MibTableColumn
igmpStaticGroupIndex = _IgmpStaticGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 6, 1, 1),
    _IgmpStaticGroupIndex_Type()
)
igmpStaticGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpStaticGroupIndex.setStatus("current")
_IgmpStaticGroupVlanId_Type = Integer32
_IgmpStaticGroupVlanId_Object = MibTableColumn
igmpStaticGroupVlanId = _IgmpStaticGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 6, 1, 2),
    _IgmpStaticGroupVlanId_Type()
)
igmpStaticGroupVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpStaticGroupVlanId.setStatus("current")
_IgmpStaticGroupIPaddress_Type = IpAddress
_IgmpStaticGroupIPaddress_Object = MibTableColumn
igmpStaticGroupIPaddress = _IgmpStaticGroupIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 6, 1, 3),
    _IgmpStaticGroupIPaddress_Type()
)
igmpStaticGroupIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpStaticGroupIPaddress.setStatus("current")


class _IgmpStaticGroupMemberPorts_Type(Bits):
    """Custom type igmpStaticGroupMemberPorts based on Bits"""
    namedValues = NamedValues(
        *(("port1", 0),
          ("port2", 1),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11),
          ("port13", 12),
          ("port14", 13),
          ("port15", 14),
          ("port16", 15),
          ("port17", 16),
          ("port18", 17),
          ("port19", 18),
          ("port20", 19),
          ("port21", 20),
          ("port22", 21),
          ("port23", 22),
          ("port24", 23),
          ("port25", 24),
          ("port26", 25),
          ("port27", 26),
          ("port28", 27),
          ("port29", 28),
          ("port30", 29),
          ("port31", 30),
          ("port32", 31))
    )

_IgmpStaticGroupMemberPorts_Type.__name__ = "Bits"
_IgmpStaticGroupMemberPorts_Object = MibTableColumn
igmpStaticGroupMemberPorts = _IgmpStaticGroupMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 6, 1, 4),
    _IgmpStaticGroupMemberPorts_Type()
)
igmpStaticGroupMemberPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpStaticGroupMemberPorts.setStatus("current")


class _IgmpStaticGroupRowStatus_Type(Integer32):
    """Custom type igmpStaticGroupRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("createAndWait", 5),
          ("destory", 6))
    )


_IgmpStaticGroupRowStatus_Type.__name__ = "Integer32"
_IgmpStaticGroupRowStatus_Object = MibTableColumn
igmpStaticGroupRowStatus = _IgmpStaticGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 6, 1, 99),
    _IgmpStaticGroupRowStatus_Type()
)
igmpStaticGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpStaticGroupRowStatus.setStatus("current")
_IgmpGroupTable_Object = MibTable
igmpGroupTable = _IgmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 7)
)
if mibBuilder.loadTexts:
    igmpGroupTable.setStatus("current")
_IgmpGroupEntry_Object = MibTableRow
igmpGroupEntry = _IgmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 7, 1)
)
igmpGroupEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "igmpGroupVlanId"),
)
if mibBuilder.loadTexts:
    igmpGroupEntry.setStatus("current")


class _IgmpGroupVlanId_Type(Integer32):
    """Custom type igmpGroupVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgmpGroupVlanId_Type.__name__ = "Integer32"
_IgmpGroupVlanId_Object = MibTableColumn
igmpGroupVlanId = _IgmpGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 7, 1, 1),
    _IgmpGroupVlanId_Type()
)
igmpGroupVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupVlanId.setStatus("current")
_IgmpGroupIPaddress_Type = IpAddress
_IgmpGroupIPaddress_Object = MibTableColumn
igmpGroupIPaddress = _IgmpGroupIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 7, 1, 2),
    _IgmpGroupIPaddress_Type()
)
igmpGroupIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupIPaddress.setStatus("current")
_IgmpGroupMemberPorts_Type = DisplayString
_IgmpGroupMemberPorts_Object = MibTableColumn
igmpGroupMemberPorts = _IgmpGroupMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 7, 1, 3),
    _IgmpGroupMemberPorts_Type()
)
igmpGroupMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupMemberPorts.setStatus("current")


class _IgmpGroupType_Type(Integer32):
    """Custom type igmpGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_IgmpGroupType_Type.__name__ = "Integer32"
_IgmpGroupType_Object = MibTableColumn
igmpGroupType = _IgmpGroupType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 7, 1, 4),
    _IgmpGroupType_Type()
)
igmpGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupType.setStatus("current")
_IgmpGroupLife_Type = Integer32
_IgmpGroupLife_Object = MibTableColumn
igmpGroupLife = _IgmpGroupLife_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 7, 1, 5),
    _IgmpGroupLife_Type()
)
igmpGroupLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupLife.setStatus("current")
_IgmpRouterTable_Object = MibTable
igmpRouterTable = _IgmpRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 8)
)
if mibBuilder.loadTexts:
    igmpRouterTable.setStatus("current")
_IgmpRouterEntry_Object = MibTableRow
igmpRouterEntry = _IgmpRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 8, 1)
)
igmpRouterEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "igmpRouterVlanId"),
)
if mibBuilder.loadTexts:
    igmpRouterEntry.setStatus("current")


class _IgmpRouterVlanId_Type(Integer32):
    """Custom type igmpRouterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgmpRouterVlanId_Type.__name__ = "Integer32"
_IgmpRouterVlanId_Object = MibTableColumn
igmpRouterVlanId = _IgmpRouterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 8, 1, 1),
    _IgmpRouterVlanId_Type()
)
igmpRouterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpRouterVlanId.setStatus("current")
_IgmpRouterPort_Type = DisplayString
_IgmpRouterPort_Object = MibTableColumn
igmpRouterPort = _IgmpRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 8, 1, 2),
    _IgmpRouterPort_Type()
)
igmpRouterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpRouterPort.setStatus("current")
_IgmpRouterExpireTime_Type = Integer32
_IgmpRouterExpireTime_Object = MibTableColumn
igmpRouterExpireTime = _IgmpRouterExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 3, 8, 1, 3),
    _IgmpRouterExpireTime_Type()
)
igmpRouterExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpRouterExpireTime.setStatus("current")
_MldSnooping_ObjectIdentity = ObjectIdentity
mldSnooping = _MldSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4)
)


class _MldSnoopingState_Type(Integer32):
    """Custom type mldSnoopingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disabled", 2))
    )


_MldSnoopingState_Type.__name__ = "Integer32"
_MldSnoopingState_Object = MibScalar
mldSnoopingState = _MldSnoopingState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 1),
    _MldSnoopingState_Type()
)
mldSnoopingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopingState.setStatus("current")


class _MldSnoopingVersion_Type(Integer32):
    """Custom type mldSnoopingVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_MldSnoopingVersion_Type.__name__ = "Integer32"
_MldSnoopingVersion_Object = MibScalar
mldSnoopingVersion = _MldSnoopingVersion_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 2),
    _MldSnoopingVersion_Type()
)
mldSnoopingVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopingVersion.setStatus("current")


class _MldSnoopingReportSuppression_Type(Integer32):
    """Custom type mldSnoopingReportSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disabled", 2))
    )


_MldSnoopingReportSuppression_Type.__name__ = "Integer32"
_MldSnoopingReportSuppression_Object = MibScalar
mldSnoopingReportSuppression = _MldSnoopingReportSuppression_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 3),
    _MldSnoopingReportSuppression_Type()
)
mldSnoopingReportSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopingReportSuppression.setStatus("current")
_MldSnoopingTable_Object = MibTable
mldSnoopingTable = _MldSnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 4)
)
if mibBuilder.loadTexts:
    mldSnoopingTable.setStatus("current")
_MldSnoopingEntry_Object = MibTableRow
mldSnoopingEntry = _MldSnoopingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 4, 1)
)
mldSnoopingEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "mldSnoopingIndex"),
)
if mibBuilder.loadTexts:
    mldSnoopingEntry.setStatus("current")


class _MldSnoopingIndex_Type(Integer32):
    """Custom type mldSnoopingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MldSnoopingIndex_Type.__name__ = "Integer32"
_MldSnoopingIndex_Object = MibTableColumn
mldSnoopingIndex = _MldSnoopingIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 4, 1, 1),
    _MldSnoopingIndex_Type()
)
mldSnoopingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopingIndex.setStatus("current")


class _MldSnoopingVlanId_Type(Integer32):
    """Custom type mldSnoopingVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4904),
    )


_MldSnoopingVlanId_Type.__name__ = "Integer32"
_MldSnoopingVlanId_Object = MibTableColumn
mldSnoopingVlanId = _MldSnoopingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 4, 1, 2),
    _MldSnoopingVlanId_Type()
)
mldSnoopingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopingVlanId.setStatus("current")


class _MldSnoopStatus_Type(Integer32):
    """Custom type mldSnoopStatus based on Integer32"""
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


_MldSnoopStatus_Type.__name__ = "Integer32"
_MldSnoopStatus_Object = MibTableColumn
mldSnoopStatus = _MldSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 4, 1, 3),
    _MldSnoopStatus_Type()
)
mldSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopStatus.setStatus("current")


class _MldSnoopRouterPortsAutoLearn_Type(Integer32):
    """Custom type mldSnoopRouterPortsAutoLearn based on Integer32"""
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


_MldSnoopRouterPortsAutoLearn_Type.__name__ = "Integer32"
_MldSnoopRouterPortsAutoLearn_Object = MibTableColumn
mldSnoopRouterPortsAutoLearn = _MldSnoopRouterPortsAutoLearn_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 4, 1, 4),
    _MldSnoopRouterPortsAutoLearn_Type()
)
mldSnoopRouterPortsAutoLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopRouterPortsAutoLearn.setStatus("current")


class _MldSnoopQueryRobustness_Type(Integer32):
    """Custom type mldSnoopQueryRobustness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MldSnoopQueryRobustness_Type.__name__ = "Integer32"
_MldSnoopQueryRobustness_Object = MibTableColumn
mldSnoopQueryRobustness = _MldSnoopQueryRobustness_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 4, 1, 5),
    _MldSnoopQueryRobustness_Type()
)
mldSnoopQueryRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopQueryRobustness.setStatus("current")


class _MldSnoopQueryInterval_Type(Integer32):
    """Custom type mldSnoopQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 18000),
    )


_MldSnoopQueryInterval_Type.__name__ = "Integer32"
_MldSnoopQueryInterval_Object = MibTableColumn
mldSnoopQueryInterval = _MldSnoopQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 4, 1, 6),
    _MldSnoopQueryInterval_Type()
)
mldSnoopQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopQueryInterval.setStatus("current")


class _MldSnoopQueryMaxResponseInterval_Type(Integer32):
    """Custom type mldSnoopQueryMaxResponseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_MldSnoopQueryMaxResponseInterval_Type.__name__ = "Integer32"
_MldSnoopQueryMaxResponseInterval_Object = MibTableColumn
mldSnoopQueryMaxResponseInterval = _MldSnoopQueryMaxResponseInterval_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 4, 1, 7),
    _MldSnoopQueryMaxResponseInterval_Type()
)
mldSnoopQueryMaxResponseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopQueryMaxResponseInterval.setStatus("current")


class _MldSnoopLastMemberQueryCounter_Type(Integer32):
    """Custom type mldSnoopLastMemberQueryCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MldSnoopLastMemberQueryCounter_Type.__name__ = "Integer32"
_MldSnoopLastMemberQueryCounter_Object = MibTableColumn
mldSnoopLastMemberQueryCounter = _MldSnoopLastMemberQueryCounter_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 4, 1, 8),
    _MldSnoopLastMemberQueryCounter_Type()
)
mldSnoopLastMemberQueryCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopLastMemberQueryCounter.setStatus("current")


class _MldSnoopLastMemberQueryInterval_Type(Integer32):
    """Custom type mldSnoopLastMemberQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_MldSnoopLastMemberQueryInterval_Type.__name__ = "Integer32"
_MldSnoopLastMemberQueryInterval_Object = MibTableColumn
mldSnoopLastMemberQueryInterval = _MldSnoopLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 4, 1, 9),
    _MldSnoopLastMemberQueryInterval_Type()
)
mldSnoopLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopLastMemberQueryInterval.setStatus("current")


class _MldSnoopImmediateLeave_Type(Integer32):
    """Custom type mldSnoopImmediateLeave based on Integer32"""
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


_MldSnoopImmediateLeave_Type.__name__ = "Integer32"
_MldSnoopImmediateLeave_Object = MibTableColumn
mldSnoopImmediateLeave = _MldSnoopImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 4, 1, 10),
    _MldSnoopImmediateLeave_Type()
)
mldSnoopImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopImmediateLeave.setStatus("current")
_OperMldSnoopQueryRobustness_Type = Integer32
_OperMldSnoopQueryRobustness_Object = MibTableColumn
operMldSnoopQueryRobustness = _OperMldSnoopQueryRobustness_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 4, 1, 11),
    _OperMldSnoopQueryRobustness_Type()
)
operMldSnoopQueryRobustness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operMldSnoopQueryRobustness.setStatus("current")
_OperMldSnoopQueryInterval_Type = Integer32
_OperMldSnoopQueryInterval_Object = MibTableColumn
operMldSnoopQueryInterval = _OperMldSnoopQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 4, 1, 12),
    _OperMldSnoopQueryInterval_Type()
)
operMldSnoopQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operMldSnoopQueryInterval.setStatus("current")
_OperMldSnoopQueryMaxResponseInterval_Type = Integer32
_OperMldSnoopQueryMaxResponseInterval_Object = MibTableColumn
operMldSnoopQueryMaxResponseInterval = _OperMldSnoopQueryMaxResponseInterval_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 4, 1, 13),
    _OperMldSnoopQueryMaxResponseInterval_Type()
)
operMldSnoopQueryMaxResponseInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operMldSnoopQueryMaxResponseInterval.setStatus("current")
_OperMldSnoopLastMemberQueryCounter_Type = Integer32
_OperMldSnoopLastMemberQueryCounter_Object = MibTableColumn
operMldSnoopLastMemberQueryCounter = _OperMldSnoopLastMemberQueryCounter_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 4, 1, 14),
    _OperMldSnoopLastMemberQueryCounter_Type()
)
operMldSnoopLastMemberQueryCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operMldSnoopLastMemberQueryCounter.setStatus("current")
_OperMldSnoopLastMemberQueryInterval_Type = Integer32
_OperMldSnoopLastMemberQueryInterval_Object = MibTableColumn
operMldSnoopLastMemberQueryInterval = _OperMldSnoopLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 4, 1, 15),
    _OperMldSnoopLastMemberQueryInterval_Type()
)
operMldSnoopLastMemberQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operMldSnoopLastMemberQueryInterval.setStatus("current")
_MldQuerierTable_Object = MibTable
mldQuerierTable = _MldQuerierTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 5)
)
if mibBuilder.loadTexts:
    mldQuerierTable.setStatus("current")
_MldQuerierEntry_Object = MibTableRow
mldQuerierEntry = _MldQuerierEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 5, 1)
)
mldQuerierEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "mldQuerierVlanId"),
)
if mibBuilder.loadTexts:
    mldQuerierEntry.setStatus("current")


class _MldQuerierVlanId_Type(Integer32):
    """Custom type mldQuerierVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MldQuerierVlanId_Type.__name__ = "Integer32"
_MldQuerierVlanId_Object = MibTableColumn
mldQuerierVlanId = _MldQuerierVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 5, 1, 1),
    _MldQuerierVlanId_Type()
)
mldQuerierVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldQuerierVlanId.setStatus("current")


class _MldQuerierState_Type(Integer32):
    """Custom type mldQuerierState based on Integer32"""
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


_MldQuerierState_Type.__name__ = "Integer32"
_MldQuerierState_Object = MibTableColumn
mldQuerierState = _MldQuerierState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 5, 1, 2),
    _MldQuerierState_Type()
)
mldQuerierState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldQuerierState.setStatus("current")


class _MldQuerierStatus_Type(Integer32):
    """Custom type mldQuerierStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("querier", 1),
          ("nonQuerier", 2))
    )


_MldQuerierStatus_Type.__name__ = "Integer32"
_MldQuerierStatus_Object = MibTableColumn
mldQuerierStatus = _MldQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 5, 1, 3),
    _MldQuerierStatus_Type()
)
mldQuerierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldQuerierStatus.setStatus("current")


class _MldQuerierVersion_Type(Integer32):
    """Custom type mldQuerierVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_MldQuerierVersion_Type.__name__ = "Integer32"
_MldQuerierVersion_Object = MibTableColumn
mldQuerierVersion = _MldQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 5, 1, 4),
    _MldQuerierVersion_Type()
)
mldQuerierVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldQuerierVersion.setStatus("current")
_MldQuerierIP_Type = DisplayString
_MldQuerierIP_Object = MibTableColumn
mldQuerierIP = _MldQuerierIP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 5, 1, 5),
    _MldQuerierIP_Type()
)
mldQuerierIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldQuerierIP.setStatus("current")
_MldStaticGroupTable_Object = MibTable
mldStaticGroupTable = _MldStaticGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 6)
)
if mibBuilder.loadTexts:
    mldStaticGroupTable.setStatus("current")
_MldStaticGroupEntry_Object = MibTableRow
mldStaticGroupEntry = _MldStaticGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 6, 1)
)
mldStaticGroupEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "mldStaticGroupIndex"),
)
if mibBuilder.loadTexts:
    mldStaticGroupEntry.setStatus("current")


class _MldStaticGroupIndex_Type(Integer32):
    """Custom type mldStaticGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_MldStaticGroupIndex_Type.__name__ = "Integer32"
_MldStaticGroupIndex_Object = MibTableColumn
mldStaticGroupIndex = _MldStaticGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 6, 1, 1),
    _MldStaticGroupIndex_Type()
)
mldStaticGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStaticGroupIndex.setStatus("current")


class _MldStaticGroupVlanId_Type(Integer32):
    """Custom type mldStaticGroupVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MldStaticGroupVlanId_Type.__name__ = "Integer32"
_MldStaticGroupVlanId_Object = MibTableColumn
mldStaticGroupVlanId = _MldStaticGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 6, 1, 2),
    _MldStaticGroupVlanId_Type()
)
mldStaticGroupVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldStaticGroupVlanId.setStatus("current")
_MldStaticGroupIPaddress_Type = DisplayString
_MldStaticGroupIPaddress_Object = MibTableColumn
mldStaticGroupIPaddress = _MldStaticGroupIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 6, 1, 3),
    _MldStaticGroupIPaddress_Type()
)
mldStaticGroupIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldStaticGroupIPaddress.setStatus("current")


class _MldStaticGroupMemberPorts_Type(Bits):
    """Custom type mldStaticGroupMemberPorts based on Bits"""
    namedValues = NamedValues(
        *(("port1", 0),
          ("port2", 1),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11),
          ("port13", 12),
          ("port14", 13),
          ("port15", 14),
          ("port16", 15),
          ("port17", 16),
          ("port18", 17),
          ("port19", 18),
          ("port20", 19),
          ("port21", 20),
          ("port22", 21),
          ("port23", 22),
          ("port24", 23),
          ("port25", 24),
          ("port26", 25),
          ("port27", 26),
          ("port28", 27),
          ("port29", 28),
          ("port30", 29),
          ("port31", 30),
          ("port32", 31))
    )

_MldStaticGroupMemberPorts_Type.__name__ = "Bits"
_MldStaticGroupMemberPorts_Object = MibTableColumn
mldStaticGroupMemberPorts = _MldStaticGroupMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 6, 1, 4),
    _MldStaticGroupMemberPorts_Type()
)
mldStaticGroupMemberPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldStaticGroupMemberPorts.setStatus("current")


class _MldStaticGroupRowStatus_Type(Integer32):
    """Custom type mldStaticGroupRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("createAndWait", 5),
          ("destory", 6))
    )


_MldStaticGroupRowStatus_Type.__name__ = "Integer32"
_MldStaticGroupRowStatus_Object = MibTableColumn
mldStaticGroupRowStatus = _MldStaticGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 6, 1, 99),
    _MldStaticGroupRowStatus_Type()
)
mldStaticGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldStaticGroupRowStatus.setStatus("current")
_MldGroupTable_Object = MibTable
mldGroupTable = _MldGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 7)
)
if mibBuilder.loadTexts:
    mldGroupTable.setStatus("current")
_MldGroupEntry_Object = MibTableRow
mldGroupEntry = _MldGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 7, 1)
)
mldGroupEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "mldGroupVlanId"),
)
if mibBuilder.loadTexts:
    mldGroupEntry.setStatus("current")


class _MldGroupVlanId_Type(Integer32):
    """Custom type mldGroupVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MldGroupVlanId_Type.__name__ = "Integer32"
_MldGroupVlanId_Object = MibTableColumn
mldGroupVlanId = _MldGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 7, 1, 1),
    _MldGroupVlanId_Type()
)
mldGroupVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldGroupVlanId.setStatus("current")
_MldGroupIPaddress_Type = DisplayString
_MldGroupIPaddress_Object = MibTableColumn
mldGroupIPaddress = _MldGroupIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 7, 1, 2),
    _MldGroupIPaddress_Type()
)
mldGroupIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldGroupIPaddress.setStatus("current")
_MldGroupMemberPorts_Type = DisplayString
_MldGroupMemberPorts_Object = MibTableColumn
mldGroupMemberPorts = _MldGroupMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 7, 1, 3),
    _MldGroupMemberPorts_Type()
)
mldGroupMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldGroupMemberPorts.setStatus("current")


class _MldGroupType_Type(Integer32):
    """Custom type mldGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_MldGroupType_Type.__name__ = "Integer32"
_MldGroupType_Object = MibTableColumn
mldGroupType = _MldGroupType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 7, 1, 4),
    _MldGroupType_Type()
)
mldGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldGroupType.setStatus("current")
_MldGroupLife_Type = Integer32
_MldGroupLife_Object = MibTableColumn
mldGroupLife = _MldGroupLife_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 7, 1, 5),
    _MldGroupLife_Type()
)
mldGroupLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldGroupLife.setStatus("current")
_MldRouterTable_Object = MibTable
mldRouterTable = _MldRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 8)
)
if mibBuilder.loadTexts:
    mldRouterTable.setStatus("current")
_MldRouterEntry_Object = MibTableRow
mldRouterEntry = _MldRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 8, 1)
)
mldRouterEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "mldRouterVlanId"),
)
if mibBuilder.loadTexts:
    mldRouterEntry.setStatus("current")


class _MldRouterVlanId_Type(Integer32):
    """Custom type mldRouterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MldRouterVlanId_Type.__name__ = "Integer32"
_MldRouterVlanId_Object = MibTableColumn
mldRouterVlanId = _MldRouterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 8, 1, 1),
    _MldRouterVlanId_Type()
)
mldRouterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldRouterVlanId.setStatus("current")
_MldRouterPort_Type = DisplayString
_MldRouterPort_Object = MibTableColumn
mldRouterPort = _MldRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 8, 1, 2),
    _MldRouterPort_Type()
)
mldRouterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldRouterPort.setStatus("current")
_MldRouterExpireTime_Type = Integer32
_MldRouterExpireTime_Object = MibTableColumn
mldRouterExpireTime = _MldRouterExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 6, 4, 8, 1, 3),
    _MldRouterExpireTime_Type()
)
mldRouterExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldRouterExpireTime.setStatus("current")
_JamboFrame_ObjectIdentity = ObjectIdentity
jamboFrame = _JamboFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 7)
)


class _JamboFramePktSize_Type(Integer32):
    """Custom type jamboFramePktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9216),
    )


_JamboFramePktSize_Type.__name__ = "Integer32"
_JamboFramePktSize_Object = MibScalar
jamboFramePktSize = _JamboFramePktSize_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 7, 1),
    _JamboFramePktSize_Type()
)
jamboFramePktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jamboFramePktSize.setStatus("current")
_Stp_ObjectIdentity = ObjectIdentity
stp = _Stp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8)
)


class _StpEnable_Type(Integer32):
    """Custom type stpEnable based on Integer32"""
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


_StpEnable_Type.__name__ = "Integer32"
_StpEnable_Object = MibScalar
stpEnable = _StpEnable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 1),
    _StpEnable_Type()
)
stpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpEnable.setStatus("current")


class _BpduForward_Type(Integer32):
    """Custom type bpduForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flooding", 1),
          ("filtering", 2))
    )


_BpduForward_Type.__name__ = "Integer32"
_BpduForward_Object = MibScalar
bpduForward = _BpduForward_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 2),
    _BpduForward_Type()
)
bpduForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bpduForward.setStatus("current")


class _PathCostMethod_Type(Integer32):
    """Custom type pathCostMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("short", 1),
          ("long", 2))
    )


_PathCostMethod_Type.__name__ = "Integer32"
_PathCostMethod_Object = MibScalar
pathCostMethod = _PathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 3),
    _PathCostMethod_Type()
)
pathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pathCostMethod.setStatus("current")


class _ForceVersion_Type(Integer32):
    """Custom type forceVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stp-compatible", 1),
          ("rstp-operation", 2),
          ("mstp-operation", 3))
    )


_ForceVersion_Type.__name__ = "Integer32"
_ForceVersion_Object = MibScalar
forceVersion = _ForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 4),
    _ForceVersion_Type()
)
forceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forceVersion.setStatus("current")
_StpPortTable_Object = MibTable
stpPortTable = _StpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 5)
)
if mibBuilder.loadTexts:
    stpPortTable.setStatus("current")
_StpPortEntry_Object = MibTableRow
stpPortEntry = _StpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 5, 1)
)
stpPortEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "stpPortIndex"),
)
if mibBuilder.loadTexts:
    stpPortEntry.setStatus("current")


class _StpPortIndex_Type(Integer32):
    """Custom type stpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpPortIndex_Type.__name__ = "Integer32"
_StpPortIndex_Object = MibTableColumn
stpPortIndex = _StpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 5, 1, 1),
    _StpPortIndex_Type()
)
stpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortIndex.setStatus("current")


class _StpAdminEnable_Type(Integer32):
    """Custom type stpAdminEnable based on Integer32"""
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


_StpAdminEnable_Type.__name__ = "Integer32"
_StpAdminEnable_Object = MibTableColumn
stpAdminEnable = _StpAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 5, 1, 2),
    _StpAdminEnable_Type()
)
stpAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpAdminEnable.setStatus("current")
_StpPathCost_Type = Integer32
_StpPathCost_Object = MibTableColumn
stpPathCost = _StpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 5, 1, 3),
    _StpPathCost_Type()
)
stpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPathCost.setStatus("current")


class _StpEdgePort_Type(Integer32):
    """Custom type stpEdgePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_StpEdgePort_Type.__name__ = "Integer32"
_StpEdgePort_Object = MibTableColumn
stpEdgePort = _StpEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 5, 1, 4),
    _StpEdgePort_Type()
)
stpEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpEdgePort.setStatus("current")


class _StpP2pMac_Type(Integer32):
    """Custom type stpP2pMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_StpP2pMac_Type.__name__ = "Integer32"
_StpP2pMac_Object = MibTableColumn
stpP2pMac = _StpP2pMac_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 5, 1, 5),
    _StpP2pMac_Type()
)
stpP2pMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpP2pMac.setStatus("current")


class _StpMigrate_Type(Integer32):
    """Custom type stpMigrate based on Integer32"""
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


_StpMigrate_Type.__name__ = "Integer32"
_StpMigrate_Object = MibTableColumn
stpMigrate = _StpMigrate_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 5, 1, 6),
    _StpMigrate_Type()
)
stpMigrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpMigrate.setStatus("current")
_StpBridgeInfo_ObjectIdentity = ObjectIdentity
stpBridgeInfo = _StpBridgeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 6)
)
_StpBridgePriority_Type = Integer32
_StpBridgePriority_Object = MibScalar
stpBridgePriority = _StpBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 6, 1),
    _StpBridgePriority_Type()
)
stpBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgePriority.setStatus("current")


class _StpBridgeForwardDelay_Type(Integer32):
    """Custom type stpBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_StpBridgeForwardDelay_Type.__name__ = "Integer32"
_StpBridgeForwardDelay_Object = MibScalar
stpBridgeForwardDelay = _StpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 6, 2),
    _StpBridgeForwardDelay_Type()
)
stpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeForwardDelay.setStatus("current")


class _StpBridgeMaxAge_Type(Integer32):
    """Custom type stpBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_StpBridgeMaxAge_Type.__name__ = "Integer32"
_StpBridgeMaxAge_Object = MibScalar
stpBridgeMaxAge = _StpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 6, 3),
    _StpBridgeMaxAge_Type()
)
stpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeMaxAge.setStatus("current")


class _StpBridgeTxHoldCount_Type(Integer32):
    """Custom type stpBridgeTxHoldCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StpBridgeTxHoldCount_Type.__name__ = "Integer32"
_StpBridgeTxHoldCount_Object = MibScalar
stpBridgeTxHoldCount = _StpBridgeTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 6, 4),
    _StpBridgeTxHoldCount_Type()
)
stpBridgeTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeTxHoldCount.setStatus("current")


class _StpBridgeHelloTime_Type(Integer32):
    """Custom type stpBridgeHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StpBridgeHelloTime_Type.__name__ = "Integer32"
_StpBridgeHelloTime_Object = MibScalar
stpBridgeHelloTime = _StpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 6, 5),
    _StpBridgeHelloTime_Type()
)
stpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeHelloTime.setStatus("current")
_StpBridgeStatus_ObjectIdentity = ObjectIdentity
stpBridgeStatus = _StpBridgeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 7)
)
_BridgeIdentifier_Type = DisplayString
_BridgeIdentifier_Object = MibScalar
bridgeIdentifier = _BridgeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 7, 1),
    _BridgeIdentifier_Type()
)
bridgeIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeIdentifier.setStatus("current")
_DefinatedRootBridge_Type = DisplayString
_DefinatedRootBridge_Object = MibScalar
definatedRootBridge = _DefinatedRootBridge_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 7, 2),
    _DefinatedRootBridge_Type()
)
definatedRootBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    definatedRootBridge.setStatus("current")
_RootPathCost_Type = Integer32
_RootPathCost_Object = MibScalar
rootPathCost = _RootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 7, 3),
    _RootPathCost_Type()
)
rootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rootPathCost.setStatus("current")
_DesignatedBridge_Type = DisplayString
_DesignatedBridge_Object = MibScalar
designatedBridge = _DesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 7, 4),
    _DesignatedBridge_Type()
)
designatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    designatedBridge.setStatus("current")
_RootPort_Type = DisplayString
_RootPort_Object = MibScalar
rootPort = _RootPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 7, 5),
    _RootPort_Type()
)
rootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rootPort.setStatus("current")
_LastTopologyChange_Type = Integer32
_LastTopologyChange_Object = MibScalar
lastTopologyChange = _LastTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 7, 6),
    _LastTopologyChange_Type()
)
lastTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastTopologyChange.setStatus("current")
_StpPortStatusTable_Object = MibTable
stpPortStatusTable = _StpPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 8)
)
if mibBuilder.loadTexts:
    stpPortStatusTable.setStatus("current")
_StpPortStatusEntry_Object = MibTableRow
stpPortStatusEntry = _StpPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 8, 1)
)
stpPortStatusEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "stpPortStatusIndex"),
)
if mibBuilder.loadTexts:
    stpPortStatusEntry.setStatus("current")


class _StpPortStatusIndex_Type(Integer32):
    """Custom type stpPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpPortStatusIndex_Type.__name__ = "Integer32"
_StpPortStatusIndex_Object = MibTableColumn
stpPortStatusIndex = _StpPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 8, 1, 1),
    _StpPortStatusIndex_Type()
)
stpPortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortStatusIndex.setStatus("current")
_StpPortPriority_Type = Integer32
_StpPortPriority_Object = MibTableColumn
stpPortPriority = _StpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 8, 1, 2),
    _StpPortPriority_Type()
)
stpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortPriority.setStatus("current")
_StpPortPathCost_Type = DisplayString
_StpPortPathCost_Object = MibTableColumn
stpPortPathCost = _StpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 8, 1, 3),
    _StpPortPathCost_Type()
)
stpPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortPathCost.setStatus("current")
_StpPortDesignatedRootBridge_Type = DisplayString
_StpPortDesignatedRootBridge_Object = MibTableColumn
stpPortDesignatedRootBridge = _StpPortDesignatedRootBridge_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 8, 1, 4),
    _StpPortDesignatedRootBridge_Type()
)
stpPortDesignatedRootBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedRootBridge.setStatus("current")
_StpPortRootPathCost_Type = Integer32
_StpPortRootPathCost_Object = MibTableColumn
stpPortRootPathCost = _StpPortRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 8, 1, 5),
    _StpPortRootPathCost_Type()
)
stpPortRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortRootPathCost.setStatus("current")
_StpPortDesignatedBridge_Type = DisplayString
_StpPortDesignatedBridge_Object = MibTableColumn
stpPortDesignatedBridge = _StpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 8, 1, 6),
    _StpPortDesignatedBridge_Type()
)
stpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedBridge.setStatus("current")
_StpPortEdgrPortConf_Type = DisplayString
_StpPortEdgrPortConf_Object = MibTableColumn
stpPortEdgrPortConf = _StpPortEdgrPortConf_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 8, 1, 7),
    _StpPortEdgrPortConf_Type()
)
stpPortEdgrPortConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortEdgrPortConf.setStatus("current")
_StpPortP2PMacConf_Type = DisplayString
_StpPortP2PMacConf_Object = MibTableColumn
stpPortP2PMacConf = _StpPortP2PMacConf_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 8, 1, 8),
    _StpPortP2PMacConf_Type()
)
stpPortP2PMacConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortP2PMacConf.setStatus("current")


class _StpPortRoles_Type(Integer32):
    """Custom type stpPortRoles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("master", 1),
          ("root", 2),
          ("designated", 3),
          ("alternate", 4),
          ("backup", 5))
    )


_StpPortRoles_Type.__name__ = "Integer32"
_StpPortRoles_Object = MibTableColumn
stpPortRoles = _StpPortRoles_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 8, 1, 9),
    _StpPortRoles_Type()
)
stpPortRoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortRoles.setStatus("current")


class _StpPortStatus_Type(Integer32):
    """Custom type stpPortStatus based on Integer32"""
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
        *(("disabled", 0),
          ("discarding", 1),
          ("learning", 2),
          ("forwarding", 3))
    )


_StpPortStatus_Type.__name__ = "Integer32"
_StpPortStatus_Object = MibTableColumn
stpPortStatus = _StpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 8, 1, 10),
    _StpPortStatus_Type()
)
stpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortStatus.setStatus("current")
_StpStatisticTable_Object = MibTable
stpStatisticTable = _StpStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 9)
)
if mibBuilder.loadTexts:
    stpStatisticTable.setStatus("current")
_StpStatisticEntry_Object = MibTableRow
stpStatisticEntry = _StpStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 9, 1)
)
stpStatisticEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "stpStatisticPortIndex"),
)
if mibBuilder.loadTexts:
    stpStatisticEntry.setStatus("current")


class _StpStatisticPortIndex_Type(Integer32):
    """Custom type stpStatisticPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpStatisticPortIndex_Type.__name__ = "Integer32"
_StpStatisticPortIndex_Object = MibTableColumn
stpStatisticPortIndex = _StpStatisticPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 9, 1, 1),
    _StpStatisticPortIndex_Type()
)
stpStatisticPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpStatisticPortIndex.setStatus("current")
_ConfigurationBPDUsReceived_Type = Integer32
_ConfigurationBPDUsReceived_Object = MibTableColumn
configurationBPDUsReceived = _ConfigurationBPDUsReceived_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 9, 1, 2),
    _ConfigurationBPDUsReceived_Type()
)
configurationBPDUsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationBPDUsReceived.setStatus("current")
_TcnBPDUsReceived_Type = Integer32
_TcnBPDUsReceived_Object = MibTableColumn
tcnBPDUsReceived = _TcnBPDUsReceived_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 9, 1, 3),
    _TcnBPDUsReceived_Type()
)
tcnBPDUsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcnBPDUsReceived.setStatus("current")
_ConfigurationBPDUsTransmitted_Type = Integer32
_ConfigurationBPDUsTransmitted_Object = MibTableColumn
configurationBPDUsTransmitted = _ConfigurationBPDUsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 9, 1, 4),
    _ConfigurationBPDUsTransmitted_Type()
)
configurationBPDUsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationBPDUsTransmitted.setStatus("current")
_TcnBPDUsTransmitted_Type = Integer32
_TcnBPDUsTransmitted_Object = MibTableColumn
tcnBPDUsTransmitted = _TcnBPDUsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 9, 1, 5),
    _TcnBPDUsTransmitted_Type()
)
tcnBPDUsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcnBPDUsTransmitted.setStatus("current")
_Mstp_ObjectIdentity = ObjectIdentity
mstp = _Mstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10)
)
_MstConfigIdentification_ObjectIdentity = ObjectIdentity
mstConfigIdentification = _MstConfigIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 1)
)
_MstConfigName_Type = DisplayString
_MstConfigName_Object = MibScalar
mstConfigName = _MstConfigName_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 1, 1),
    _MstConfigName_Type()
)
mstConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstConfigName.setStatus("current")


class _MstRevisionLevel_Type(Integer32):
    """Custom type mstRevisionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MstRevisionLevel_Type.__name__ = "Integer32"
_MstRevisionLevel_Object = MibScalar
mstRevisionLevel = _MstRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 1, 2),
    _MstRevisionLevel_Type()
)
mstRevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstRevisionLevel.setStatus("current")
_MstInstanceID_ObjectIdentity = ObjectIdentity
mstInstanceID = _MstInstanceID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 2)
)


class _MstiIDSetting_Type(Integer32):
    """Custom type mstiIDSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MstiIDSetting_Type.__name__ = "Integer32"
_MstiIDSetting_Object = MibScalar
mstiIDSetting = _MstiIDSetting_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 2, 1),
    _MstiIDSetting_Type()
)
mstiIDSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstiIDSetting.setStatus("current")
_MstiVlanListSetting_Type = DisplayString
_MstiVlanListSetting_Object = MibScalar
mstiVlanListSetting = _MstiVlanListSetting_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 2, 2),
    _MstiVlanListSetting_Type()
)
mstiVlanListSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstiVlanListSetting.setStatus("current")


class _MstiIDSettingMove_Type(Integer32):
    """Custom type mstiIDSettingMove based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 1),
          ("move", 2))
    )


_MstiIDSettingMove_Type.__name__ = "Integer32"
_MstiIDSettingMove_Object = MibScalar
mstiIDSettingMove = _MstiIDSettingMove_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 2, 3),
    _MstiIDSettingMove_Type()
)
mstiIDSettingMove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstiIDSettingMove.setStatus("current")
_MstiIDInfoTable_Object = MibTable
mstiIDInfoTable = _MstiIDInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 2, 4)
)
if mibBuilder.loadTexts:
    mstiIDInfoTable.setStatus("current")
_MstiIDInfoEntry_Object = MibTableRow
mstiIDInfoEntry = _MstiIDInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 2, 4, 1)
)
mstiIDInfoEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "mstiIDIndex"),
)
if mibBuilder.loadTexts:
    mstiIDInfoEntry.setStatus("current")


class _MstiIDIndex_Type(Integer32):
    """Custom type mstiIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MstiIDIndex_Type.__name__ = "Integer32"
_MstiIDIndex_Object = MibTableColumn
mstiIDIndex = _MstiIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 2, 4, 1, 1),
    _MstiIDIndex_Type()
)
mstiIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstiIDIndex.setStatus("current")
_MstiVLANList_Type = DisplayString
_MstiVLANList_Object = MibTableColumn
mstiVLANList = _MstiVLANList_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 2, 4, 1, 2),
    _MstiVLANList_Type()
)
mstiVLANList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstiVLANList.setStatus("current")
_StpInstance_ObjectIdentity = ObjectIdentity
stpInstance = _StpInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 3)
)
_StpPriorityInfoTable_Object = MibTable
stpPriorityInfoTable = _StpPriorityInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 3, 1)
)
if mibBuilder.loadTexts:
    stpPriorityInfoTable.setStatus("current")
_StpPriorityInfoEntry_Object = MibTableRow
stpPriorityInfoEntry = _StpPriorityInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 3, 1, 1)
)
stpPriorityInfoEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "stpMstiIDIndex"),
)
if mibBuilder.loadTexts:
    stpPriorityInfoEntry.setStatus("current")


class _StpMstiIDIndex_Type(Integer32):
    """Custom type stpMstiIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_StpMstiIDIndex_Type.__name__ = "Integer32"
_StpMstiIDIndex_Object = MibTableColumn
stpMstiIDIndex = _StpMstiIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 3, 1, 1, 1),
    _StpMstiIDIndex_Type()
)
stpMstiIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpMstiIDIndex.setStatus("current")
_StpPriorityValue_Type = Integer32
_StpPriorityValue_Object = MibTableColumn
stpPriorityValue = _StpPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 3, 1, 1, 2),
    _StpPriorityValue_Type()
)
stpPriorityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPriorityValue.setStatus("current")


class _StpPriorityDefault_Type(Integer32):
    """Custom type stpPriorityDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 1),
          ("default", 2))
    )


_StpPriorityDefault_Type.__name__ = "Integer32"
_StpPriorityDefault_Object = MibTableColumn
stpPriorityDefault = _StpPriorityDefault_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 3, 1, 1, 3),
    _StpPriorityDefault_Type()
)
stpPriorityDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPriorityDefault.setStatus("current")
_MstInstanceInfo_ObjectIdentity = ObjectIdentity
mstInstanceInfo = _MstInstanceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4)
)
_MstBridgeIdentifier_Type = DisplayString
_MstBridgeIdentifier_Object = MibScalar
mstBridgeIdentifier = _MstBridgeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 1),
    _MstBridgeIdentifier_Type()
)
mstBridgeIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstBridgeIdentifier.setStatus("current")
_MstDesignatedRootBridge_Type = DisplayString
_MstDesignatedRootBridge_Object = MibScalar
mstDesignatedRootBridge = _MstDesignatedRootBridge_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 2),
    _MstDesignatedRootBridge_Type()
)
mstDesignatedRootBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstDesignatedRootBridge.setStatus("current")
_MstRootPathCost_Type = Integer32
_MstRootPathCost_Object = MibScalar
mstRootPathCost = _MstRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 3),
    _MstRootPathCost_Type()
)
mstRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstRootPathCost.setStatus("current")
_MstDesignatedBridge_Type = DisplayString
_MstDesignatedBridge_Object = MibScalar
mstDesignatedBridge = _MstDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 4),
    _MstDesignatedBridge_Type()
)
mstDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstDesignatedBridge.setStatus("current")
_MstRootPort_Type = DisplayString
_MstRootPort_Object = MibScalar
mstRootPort = _MstRootPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 5),
    _MstRootPort_Type()
)
mstRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstRootPort.setStatus("current")
_MstLastTopologyChange_Type = Integer32
_MstLastTopologyChange_Object = MibScalar
mstLastTopologyChange = _MstLastTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 6),
    _MstLastTopologyChange_Type()
)
mstLastTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstLastTopologyChange.setStatus("current")
_MstStpPortStatusTable_Object = MibTable
mstStpPortStatusTable = _MstStpPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 7)
)
if mibBuilder.loadTexts:
    mstStpPortStatusTable.setStatus("current")
_MstStpPortStatusEntry_Object = MibTableRow
mstStpPortStatusEntry = _MstStpPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 7, 1)
)
mstStpPortStatusEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "mstStpPortStatusIndex"),
)
if mibBuilder.loadTexts:
    mstStpPortStatusEntry.setStatus("current")


class _MstStpPortStatusIndex_Type(Integer32):
    """Custom type mstStpPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MstStpPortStatusIndex_Type.__name__ = "Integer32"
_MstStpPortStatusIndex_Object = MibTableColumn
mstStpPortStatusIndex = _MstStpPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 7, 1, 1),
    _MstStpPortStatusIndex_Type()
)
mstStpPortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstStpPortStatusIndex.setStatus("current")
_MstStpPortPriority_Type = DisplayString
_MstStpPortPriority_Object = MibTableColumn
mstStpPortPriority = _MstStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 7, 1, 2),
    _MstStpPortPriority_Type()
)
mstStpPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstStpPortPriority.setStatus("current")
_MstStpPortPathCost_Type = DisplayString
_MstStpPortPathCost_Object = MibTableColumn
mstStpPortPathCost = _MstStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 7, 1, 3),
    _MstStpPortPathCost_Type()
)
mstStpPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstStpPortPathCost.setStatus("current")
_MstStpPortDesignatedRootBridge_Type = DisplayString
_MstStpPortDesignatedRootBridge_Object = MibTableColumn
mstStpPortDesignatedRootBridge = _MstStpPortDesignatedRootBridge_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 7, 1, 4),
    _MstStpPortDesignatedRootBridge_Type()
)
mstStpPortDesignatedRootBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstStpPortDesignatedRootBridge.setStatus("current")
_MstStpPortRootPathCost_Type = DisplayString
_MstStpPortRootPathCost_Object = MibTableColumn
mstStpPortRootPathCost = _MstStpPortRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 7, 1, 5),
    _MstStpPortRootPathCost_Type()
)
mstStpPortRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstStpPortRootPathCost.setStatus("current")
_MstStpPortDesignatedBridge_Type = DisplayString
_MstStpPortDesignatedBridge_Object = MibTableColumn
mstStpPortDesignatedBridge = _MstStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 7, 1, 6),
    _MstStpPortDesignatedBridge_Type()
)
mstStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstStpPortDesignatedBridge.setStatus("current")
_MstStpPortEdgrPortConf_Type = DisplayString
_MstStpPortEdgrPortConf_Object = MibTableColumn
mstStpPortEdgrPortConf = _MstStpPortEdgrPortConf_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 7, 1, 7),
    _MstStpPortEdgrPortConf_Type()
)
mstStpPortEdgrPortConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstStpPortEdgrPortConf.setStatus("current")
_MstStpPortP2PMacConf_Type = DisplayString
_MstStpPortP2PMacConf_Object = MibTableColumn
mstStpPortP2PMacConf = _MstStpPortP2PMacConf_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 7, 1, 8),
    _MstStpPortP2PMacConf_Type()
)
mstStpPortP2PMacConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstStpPortP2PMacConf.setStatus("current")
_MstStpPortRoles_Type = DisplayString
_MstStpPortRoles_Object = MibTableColumn
mstStpPortRoles = _MstStpPortRoles_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 7, 1, 9),
    _MstStpPortRoles_Type()
)
mstStpPortRoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstStpPortRoles.setStatus("current")
_MstStpPortStatus_Type = DisplayString
_MstStpPortStatus_Object = MibTableColumn
mstStpPortStatus = _MstStpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 7, 1, 10),
    _MstStpPortStatus_Type()
)
mstStpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstStpPortStatus.setStatus("current")
_MstInstanceInfoID_Type = Integer32
_MstInstanceInfoID_Object = MibScalar
mstInstanceInfoID = _MstInstanceInfoID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 8, 10, 4, 8),
    _MstInstanceInfoID_Type()
)
mstInstanceInfoID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstInstanceInfoID.setStatus("current")
_QinqVlan_ObjectIdentity = ObjectIdentity
qinqVlan = _QinqVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 9)
)
_OuterVlanEthtype_Type = DisplayString
_OuterVlanEthtype_Object = MibScalar
outerVlanEthtype = _OuterVlanEthtype_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 9, 1),
    _OuterVlanEthtype_Type()
)
outerVlanEthtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outerVlanEthtype.setStatus("current")
_QinqPortInfoTable_Object = MibTable
qinqPortInfoTable = _QinqPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 9, 2)
)
if mibBuilder.loadTexts:
    qinqPortInfoTable.setStatus("current")
_QinqPortInfoEntry_Object = MibTableRow
qinqPortInfoEntry = _QinqPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 9, 2, 1)
)
qinqPortInfoEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "qinqPortIndex"),
)
if mibBuilder.loadTexts:
    qinqPortInfoEntry.setStatus("current")


class _QinqPortIndex_Type(Integer32):
    """Custom type qinqPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QinqPortIndex_Type.__name__ = "Integer32"
_QinqPortIndex_Object = MibTableColumn
qinqPortIndex = _QinqPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 9, 2, 1, 1),
    _QinqPortIndex_Type()
)
qinqPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qinqPortIndex.setStatus("current")


class _QinqOuterPVID_Type(Integer32):
    """Custom type qinqOuterPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_QinqOuterPVID_Type.__name__ = "Integer32"
_QinqOuterPVID_Object = MibTableColumn
qinqOuterPVID = _QinqOuterPVID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 9, 2, 1, 2),
    _QinqOuterPVID_Type()
)
qinqOuterPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinqOuterPVID.setStatus("current")


class _QinqOuterMode_Type(Integer32):
    """Custom type qinqOuterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 1),
          ("uni", 2))
    )


_QinqOuterMode_Type.__name__ = "Integer32"
_QinqOuterMode_Object = MibTableColumn
qinqOuterMode = _QinqOuterMode_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 9, 2, 1, 3),
    _QinqOuterMode_Type()
)
qinqOuterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinqOuterMode.setStatus("current")
_Garp_ObjectIdentity = ObjectIdentity
garp = _Garp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 10)
)


class _GarpJoinTime_Type(Integer32):
    """Custom type garpJoinTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_GarpJoinTime_Type.__name__ = "Integer32"
_GarpJoinTime_Object = MibScalar
garpJoinTime = _GarpJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 10, 1),
    _GarpJoinTime_Type()
)
garpJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    garpJoinTime.setStatus("current")
if mibBuilder.loadTexts:
    garpJoinTime.setUnits("Second")


class _GarpLeaveTime_Type(Integer32):
    """Custom type garpLeaveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3000),
    )


_GarpLeaveTime_Type.__name__ = "Integer32"
_GarpLeaveTime_Object = MibScalar
garpLeaveTime = _GarpLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 10, 2),
    _GarpLeaveTime_Type()
)
garpLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    garpLeaveTime.setStatus("current")
if mibBuilder.loadTexts:
    garpLeaveTime.setUnits("Second")


class _GarpLeaveAllTime_Type(Integer32):
    """Custom type garpLeaveAllTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 12000),
    )


_GarpLeaveAllTime_Type.__name__ = "Integer32"
_GarpLeaveAllTime_Object = MibScalar
garpLeaveAllTime = _GarpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 10, 3),
    _GarpLeaveAllTime_Type()
)
garpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    garpLeaveAllTime.setStatus("current")
if mibBuilder.loadTexts:
    garpLeaveAllTime.setUnits("Second")
_Gvrp_ObjectIdentity = ObjectIdentity
gvrp = _Gvrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 11)
)


class _GvrpStatus_Type(Integer32):
    """Custom type gvrpStatus based on Integer32"""
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


_GvrpStatus_Type.__name__ = "Integer32"
_GvrpStatus_Object = MibScalar
gvrpStatus = _GvrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 11, 1),
    _GvrpStatus_Type()
)
gvrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvrpStatus.setStatus("current")
_XRingElite_ObjectIdentity = ObjectIdentity
xRingElite = _XRingElite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 12)
)


class _XRingEliteState_Type(Integer32):
    """Custom type xRingEliteState based on Integer32"""
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


_XRingEliteState_Type.__name__ = "Integer32"
_XRingEliteState_Object = MibScalar
xRingEliteState = _XRingEliteState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 12, 1),
    _XRingEliteState_Type()
)
xRingEliteState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingEliteState.setStatus("current")
_XRingEliteRingIDTable_Object = MibTable
xRingEliteRingIDTable = _XRingEliteRingIDTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 12, 2)
)
if mibBuilder.loadTexts:
    xRingEliteRingIDTable.setStatus("current")
_XRingEliteRingIDEntry_Object = MibTableRow
xRingEliteRingIDEntry = _XRingEliteRingIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 12, 2, 1)
)
xRingEliteRingIDEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "xRingEliteRingIDIndex"),
)
if mibBuilder.loadTexts:
    xRingEliteRingIDEntry.setStatus("current")


class _XRingEliteRingIDIndex_Type(Integer32):
    """Custom type xRingEliteRingIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_XRingEliteRingIDIndex_Type.__name__ = "Integer32"
_XRingEliteRingIDIndex_Object = MibTableColumn
xRingEliteRingIDIndex = _XRingEliteRingIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 12, 2, 1, 1),
    _XRingEliteRingIDIndex_Type()
)
xRingEliteRingIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRingEliteRingIDIndex.setStatus("current")


class _XRingEliteRingID_Type(Integer32):
    """Custom type xRingEliteRingID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_XRingEliteRingID_Type.__name__ = "Integer32"
_XRingEliteRingID_Object = MibTableColumn
xRingEliteRingID = _XRingEliteRingID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 12, 2, 1, 2),
    _XRingEliteRingID_Type()
)
xRingEliteRingID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingEliteRingID.setStatus("current")


class _XRingEliteRule_Type(Integer32):
    """Custom type xRingEliteRule based on Integer32"""
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
        *(("basic", 1),
          ("couple", 2),
          ("tunnel", 3),
          ("mrm", 4),
          ("mrc", 5),
          ("legacy", 6))
    )


_XRingEliteRule_Type.__name__ = "Integer32"
_XRingEliteRule_Object = MibTableColumn
xRingEliteRule = _XRingEliteRule_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 12, 2, 1, 3),
    _XRingEliteRule_Type()
)
xRingEliteRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingEliteRule.setStatus("current")
_XRingElitePort1_Type = Integer32
_XRingElitePort1_Object = MibTableColumn
xRingElitePort1 = _XRingElitePort1_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 12, 2, 1, 4),
    _XRingElitePort1_Type()
)
xRingElitePort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingElitePort1.setStatus("current")
_XRingElitePort2_Type = Integer32
_XRingElitePort2_Object = MibTableColumn
xRingElitePort2 = _XRingElitePort2_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 12, 2, 1, 5),
    _XRingElitePort2_Type()
)
xRingElitePort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingElitePort2.setStatus("current")
_XRingEliteRingIDStatus_Type = DisplayString
_XRingEliteRingIDStatus_Object = MibTableColumn
xRingEliteRingIDStatus = _XRingEliteRingIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 12, 2, 1, 6),
    _XRingEliteRingIDStatus_Type()
)
xRingEliteRingIDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRingEliteRingIDStatus.setStatus("current")
_XRingElitePort1Status_Type = DisplayString
_XRingElitePort1Status_Object = MibTableColumn
xRingElitePort1Status = _XRingElitePort1Status_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 12, 2, 1, 7),
    _XRingElitePort1Status_Type()
)
xRingElitePort1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRingElitePort1Status.setStatus("current")
_XRingElitePort2Status_Type = DisplayString
_XRingElitePort2Status_Object = MibTableColumn
xRingElitePort2Status = _XRingElitePort2Status_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 12, 2, 1, 8),
    _XRingElitePort2Status_Type()
)
xRingElitePort2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRingElitePort2Status.setStatus("current")


class _XRingEliteRowStatus_Type(Integer32):
    """Custom type xRingEliteRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("createAndWait", 5),
          ("destory", 6))
    )


_XRingEliteRowStatus_Type.__name__ = "Integer32"
_XRingEliteRowStatus_Object = MibTableColumn
xRingEliteRowStatus = _XRingEliteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 12, 2, 1, 99),
    _XRingEliteRowStatus_Type()
)
xRingEliteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xRingEliteRowStatus.setStatus("current")
_Loopback_ObjectIdentity = ObjectIdentity
loopback = _Loopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 13)
)


class _LoopbackEnabled_Type(Integer32):
    """Custom type loopbackEnabled based on Integer32"""
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


_LoopbackEnabled_Type.__name__ = "Integer32"
_LoopbackEnabled_Object = MibScalar
loopbackEnabled = _LoopbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 13, 1),
    _LoopbackEnabled_Type()
)
loopbackEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbackEnabled.setStatus("current")


class _LoopbackInterval_Type(Integer32):
    """Custom type loopbackInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_LoopbackInterval_Type.__name__ = "Integer32"
_LoopbackInterval_Object = MibScalar
loopbackInterval = _LoopbackInterval_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 13, 2),
    _LoopbackInterval_Type()
)
loopbackInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbackInterval.setStatus("current")
if mibBuilder.loadTexts:
    loopbackInterval.setUnits("Second")


class _LoopbackRecoverTime_Type(Integer32):
    """Custom type loopbackRecoverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1000000),
    )


_LoopbackRecoverTime_Type.__name__ = "Integer32"
_LoopbackRecoverTime_Object = MibScalar
loopbackRecoverTime = _LoopbackRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 13, 3),
    _LoopbackRecoverTime_Type()
)
loopbackRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbackRecoverTime.setStatus("current")
if mibBuilder.loadTexts:
    loopbackRecoverTime.setUnits("Second")
_LoopbackPortTable_Object = MibTable
loopbackPortTable = _LoopbackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 13, 4)
)
if mibBuilder.loadTexts:
    loopbackPortTable.setStatus("current")
_LoopbackPortEntry_Object = MibTableRow
loopbackPortEntry = _LoopbackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 13, 4, 1)
)
loopbackPortEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "loopbackPortIndex"),
)
if mibBuilder.loadTexts:
    loopbackPortEntry.setStatus("current")


class _LoopbackPortIndex_Type(Integer32):
    """Custom type loopbackPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LoopbackPortIndex_Type.__name__ = "Integer32"
_LoopbackPortIndex_Object = MibTableColumn
loopbackPortIndex = _LoopbackPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 13, 4, 1, 1),
    _LoopbackPortIndex_Type()
)
loopbackPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopbackPortIndex.setStatus("current")


class _LoopbackPortEnabled_Type(Integer32):
    """Custom type loopbackPortEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_LoopbackPortEnabled_Type.__name__ = "Integer32"
_LoopbackPortEnabled_Object = MibTableColumn
loopbackPortEnabled = _LoopbackPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 13, 4, 1, 2),
    _LoopbackPortEnabled_Type()
)
loopbackPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbackPortEnabled.setStatus("current")


class _LoopbackPortLoopStatus_Type(Integer32):
    """Custom type loopbackPortLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("shutdown", 2))
    )


_LoopbackPortLoopStatus_Type.__name__ = "Integer32"
_LoopbackPortLoopStatus_Object = MibTableColumn
loopbackPortLoopStatus = _LoopbackPortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 13, 4, 1, 3),
    _LoopbackPortLoopStatus_Type()
)
loopbackPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopbackPortLoopStatus.setStatus("current")
_XRingPro_ObjectIdentity = ObjectIdentity
xRingPro = _XRingPro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14)
)


class _XRingProStatus_Type(Integer32):
    """Custom type xRingProStatus based on Integer32"""
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


_XRingProStatus_Type.__name__ = "Integer32"
_XRingProStatus_Object = MibScalar
xRingProStatus = _XRingProStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 1),
    _XRingProStatus_Type()
)
xRingProStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProStatus.setStatus("current")
_XRingProRingSetting_ObjectIdentity = ObjectIdentity
xRingProRingSetting = _XRingProRingSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 2)
)


class _XRingProRingID_Type(Integer32):
    """Custom type xRingProRingID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_XRingProRingID_Type.__name__ = "Integer32"
_XRingProRingID_Object = MibScalar
xRingProRingID = _XRingProRingID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 2, 1),
    _XRingProRingID_Type()
)
xRingProRingID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProRingID.setStatus("current")


class _XRingProRingPort1_Type(Integer32):
    """Custom type xRingProRingPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XRingProRingPort1_Type.__name__ = "Integer32"
_XRingProRingPort1_Object = MibScalar
xRingProRingPort1 = _XRingProRingPort1_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 2, 2),
    _XRingProRingPort1_Type()
)
xRingProRingPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProRingPort1.setStatus("current")


class _XRingProRingPort2_Type(Integer32):
    """Custom type xRingProRingPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XRingProRingPort2_Type.__name__ = "Integer32"
_XRingProRingPort2_Object = MibScalar
xRingProRingPort2 = _XRingProRingPort2_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 2, 3),
    _XRingProRingPort2_Type()
)
xRingProRingPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProRingPort2.setStatus("current")


class _XRingProRingAdd_Type(Integer32):
    """Custom type xRingProRingAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("add", 1))
    )


_XRingProRingAdd_Type.__name__ = "Integer32"
_XRingProRingAdd_Object = MibScalar
xRingProRingAdd = _XRingProRingAdd_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 2, 4),
    _XRingProRingAdd_Type()
)
xRingProRingAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProRingAdd.setStatus("current")
_XRingProCoupleSetting_ObjectIdentity = ObjectIdentity
xRingProCoupleSetting = _XRingProCoupleSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 3)
)


class _XRingProCoupleID_Type(Integer32):
    """Custom type xRingProCoupleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_XRingProCoupleID_Type.__name__ = "Integer32"
_XRingProCoupleID_Object = MibScalar
xRingProCoupleID = _XRingProCoupleID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 3, 1),
    _XRingProCoupleID_Type()
)
xRingProCoupleID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProCoupleID.setStatus("current")


class _XRingProCouplePort_Type(Bits):
    """Custom type xRingProCouplePort based on Bits"""
    namedValues = NamedValues(
        *(("port1", 0),
          ("port2", 1),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11),
          ("port13", 12),
          ("port14", 13),
          ("port15", 14),
          ("port16", 15),
          ("port17", 16),
          ("port18", 17),
          ("port19", 18),
          ("port20", 19),
          ("port21", 20),
          ("port22", 21),
          ("port23", 22),
          ("port24", 23),
          ("port25", 24),
          ("port26", 25),
          ("port27", 26),
          ("port28", 27),
          ("port29", 28),
          ("port30", 29),
          ("port31", 30),
          ("port32", 31))
    )

_XRingProCouplePort_Type.__name__ = "Bits"
_XRingProCouplePort_Object = MibScalar
xRingProCouplePort = _XRingProCouplePort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 3, 2),
    _XRingProCouplePort_Type()
)
xRingProCouplePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProCouplePort.setStatus("current")


class _XRingProCoupleMasterRingID_Type(Integer32):
    """Custom type xRingProCoupleMasterRingID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_XRingProCoupleMasterRingID_Type.__name__ = "Integer32"
_XRingProCoupleMasterRingID_Object = MibScalar
xRingProCoupleMasterRingID = _XRingProCoupleMasterRingID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 3, 3),
    _XRingProCoupleMasterRingID_Type()
)
xRingProCoupleMasterRingID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProCoupleMasterRingID.setStatus("current")


class _XRingProCoupleAdd_Type(Integer32):
    """Custom type xRingProCoupleAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("add", 1))
    )


_XRingProCoupleAdd_Type.__name__ = "Integer32"
_XRingProCoupleAdd_Object = MibScalar
xRingProCoupleAdd = _XRingProCoupleAdd_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 3, 4),
    _XRingProCoupleAdd_Type()
)
xRingProCoupleAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProCoupleAdd.setStatus("current")
_XRingProInfoTable_Object = MibTable
xRingProInfoTable = _XRingProInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 4)
)
if mibBuilder.loadTexts:
    xRingProInfoTable.setStatus("current")
_XRingProInfoEntry_Object = MibTableRow
xRingProInfoEntry = _XRingProInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 4, 1)
)
xRingProInfoEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "xRingProInfoRingID"),
)
if mibBuilder.loadTexts:
    xRingProInfoEntry.setStatus("current")


class _XRingProInfoRingID_Type(Integer32):
    """Custom type xRingProInfoRingID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_XRingProInfoRingID_Type.__name__ = "Integer32"
_XRingProInfoRingID_Object = MibTableColumn
xRingProInfoRingID = _XRingProInfoRingID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 4, 1, 1),
    _XRingProInfoRingID_Type()
)
xRingProInfoRingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRingProInfoRingID.setStatus("current")
_XRingProInfoMode_Type = DisplayString
_XRingProInfoMode_Object = MibTableColumn
xRingProInfoMode = _XRingProInfoMode_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 4, 1, 2),
    _XRingProInfoMode_Type()
)
xRingProInfoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRingProInfoMode.setStatus("current")
_XRingProInfoOperState_Type = DisplayString
_XRingProInfoOperState_Object = MibTableColumn
xRingProInfoOperState = _XRingProInfoOperState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 4, 1, 3),
    _XRingProInfoOperState_Type()
)
xRingProInfoOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRingProInfoOperState.setStatus("current")
_XRingProInfoPort1_Type = DisplayString
_XRingProInfoPort1_Object = MibTableColumn
xRingProInfoPort1 = _XRingProInfoPort1_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 4, 1, 4),
    _XRingProInfoPort1_Type()
)
xRingProInfoPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRingProInfoPort1.setStatus("current")
_XRingProInfoPort1FwdState_Type = DisplayString
_XRingProInfoPort1FwdState_Object = MibTableColumn
xRingProInfoPort1FwdState = _XRingProInfoPort1FwdState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 4, 1, 5),
    _XRingProInfoPort1FwdState_Type()
)
xRingProInfoPort1FwdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRingProInfoPort1FwdState.setStatus("current")
_XRingProInfoPort2_Type = DisplayString
_XRingProInfoPort2_Object = MibTableColumn
xRingProInfoPort2 = _XRingProInfoPort2_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 4, 1, 6),
    _XRingProInfoPort2_Type()
)
xRingProInfoPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRingProInfoPort2.setStatus("current")
_XRingProInfoPort2FwdState_Type = DisplayString
_XRingProInfoPort2FwdState_Object = MibTableColumn
xRingProInfoPort2FwdState = _XRingProInfoPort2FwdState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 4, 1, 7),
    _XRingProInfoPort2FwdState_Type()
)
xRingProInfoPort2FwdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRingProInfoPort2FwdState.setStatus("current")


class _XRingProInfoDel_Type(Integer32):
    """Custom type xRingProInfoDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("del", 1))
    )


_XRingProInfoDel_Type.__name__ = "Integer32"
_XRingProInfoDel_Object = MibTableColumn
xRingProInfoDel = _XRingProInfoDel_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 4, 1, 8),
    _XRingProInfoDel_Type()
)
xRingProInfoDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProInfoDel.setStatus("current")


class _XRingProInfoRole_Type(Integer32):
    """Custom type xRingProInfoRole based on Integer32"""
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
        *(("member", 0),
          ("head", 1),
          ("tail", 2),
          ("none", 3))
    )


_XRingProInfoRole_Type.__name__ = "Integer32"
_XRingProInfoRole_Object = MibTableColumn
xRingProInfoRole = _XRingProInfoRole_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 4, 1, 9),
    _XRingProInfoRole_Type()
)
xRingProInfoRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRingProInfoRole.setStatus("current")
_XRingProPairSetting_ObjectIdentity = ObjectIdentity
xRingProPairSetting = _XRingProPairSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 5)
)


class _XRingProPairID_Type(Integer32):
    """Custom type xRingProPairID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_XRingProPairID_Type.__name__ = "Integer32"
_XRingProPairID_Object = MibScalar
xRingProPairID = _XRingProPairID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 5, 1),
    _XRingProPairID_Type()
)
xRingProPairID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProPairID.setStatus("current")


class _XRingProPairPort_Type(Bits):
    """Custom type xRingProPairPort based on Bits"""
    namedValues = NamedValues(
        *(("port1", 0),
          ("port2", 1),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11),
          ("port13", 12),
          ("port14", 13),
          ("port15", 14),
          ("port16", 15),
          ("port17", 16),
          ("port18", 17),
          ("port19", 18),
          ("port20", 19),
          ("port21", 20),
          ("port22", 21),
          ("port23", 22),
          ("port24", 23),
          ("port25", 24),
          ("port26", 25),
          ("port27", 26),
          ("port28", 27),
          ("port29", 28),
          ("port30", 29),
          ("port31", 30),
          ("port32", 31))
    )

_XRingProPairPort_Type.__name__ = "Bits"
_XRingProPairPort_Object = MibScalar
xRingProPairPort = _XRingProPairPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 5, 2),
    _XRingProPairPort_Type()
)
xRingProPairPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProPairPort.setStatus("current")


class _XRingProPairMasterRingID_Type(Integer32):
    """Custom type xRingProPairMasterRingID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_XRingProPairMasterRingID_Type.__name__ = "Integer32"
_XRingProPairMasterRingID_Object = MibScalar
xRingProPairMasterRingID = _XRingProPairMasterRingID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 5, 3),
    _XRingProPairMasterRingID_Type()
)
xRingProPairMasterRingID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProPairMasterRingID.setStatus("current")


class _XRingProPairAdd_Type(Integer32):
    """Custom type xRingProPairAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("add", 1))
    )


_XRingProPairAdd_Type.__name__ = "Integer32"
_XRingProPairAdd_Object = MibScalar
xRingProPairAdd = _XRingProPairAdd_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 5, 4),
    _XRingProPairAdd_Type()
)
xRingProPairAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProPairAdd.setStatus("current")
_XRingProRPairSetting_ObjectIdentity = ObjectIdentity
xRingProRPairSetting = _XRingProRPairSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 6)
)


class _XRingProRPairID_Type(Integer32):
    """Custom type xRingProRPairID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_XRingProRPairID_Type.__name__ = "Integer32"
_XRingProRPairID_Object = MibScalar
xRingProRPairID = _XRingProRPairID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 6, 1),
    _XRingProRPairID_Type()
)
xRingProRPairID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProRPairID.setStatus("current")


class _XRingProRPairPort_Type(Integer32):
    """Custom type xRingProRPairPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XRingProRPairPort_Type.__name__ = "Integer32"
_XRingProRPairPort_Object = MibScalar
xRingProRPairPort = _XRingProRPairPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 6, 2),
    _XRingProRPairPort_Type()
)
xRingProRPairPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProRPairPort.setStatus("current")


class _XRingProRPairMasterRingID_Type(Integer32):
    """Custom type xRingProRPairMasterRingID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_XRingProRPairMasterRingID_Type.__name__ = "Integer32"
_XRingProRPairMasterRingID_Object = MibScalar
xRingProRPairMasterRingID = _XRingProRPairMasterRingID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 6, 3),
    _XRingProRPairMasterRingID_Type()
)
xRingProRPairMasterRingID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProRPairMasterRingID.setStatus("current")


class _XRingProRPairAdd_Type(Integer32):
    """Custom type xRingProRPairAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("add", 1))
    )


_XRingProRPairAdd_Type.__name__ = "Integer32"
_XRingProRPairAdd_Object = MibScalar
xRingProRPairAdd = _XRingProRPairAdd_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 6, 4),
    _XRingProRPairAdd_Type()
)
xRingProRPairAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProRPairAdd.setStatus("current")
_XRingProChainSetting_ObjectIdentity = ObjectIdentity
xRingProChainSetting = _XRingProChainSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 7)
)


class _XRingProChainID_Type(Integer32):
    """Custom type xRingProChainID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_XRingProChainID_Type.__name__ = "Integer32"
_XRingProChainID_Object = MibScalar
xRingProChainID = _XRingProChainID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 7, 1),
    _XRingProChainID_Type()
)
xRingProChainID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProChainID.setStatus("current")


class _XRingProChainRole_Type(Integer32):
    """Custom type xRingProChainRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("member", 0),
          ("head", 1),
          ("tail", 2))
    )


_XRingProChainRole_Type.__name__ = "Integer32"
_XRingProChainRole_Object = MibScalar
xRingProChainRole = _XRingProChainRole_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 7, 2),
    _XRingProChainRole_Type()
)
xRingProChainRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProChainRole.setStatus("current")


class _XRingProChainHeadPort_Type(Integer32):
    """Custom type xRingProChainHeadPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XRingProChainHeadPort_Type.__name__ = "Integer32"
_XRingProChainHeadPort_Object = MibScalar
xRingProChainHeadPort = _XRingProChainHeadPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 7, 3),
    _XRingProChainHeadPort_Type()
)
xRingProChainHeadPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProChainHeadPort.setStatus("current")


class _XRingProChainMemberPort_Type(Integer32):
    """Custom type xRingProChainMemberPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XRingProChainMemberPort_Type.__name__ = "Integer32"
_XRingProChainMemberPort_Object = MibScalar
xRingProChainMemberPort = _XRingProChainMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 7, 4),
    _XRingProChainMemberPort_Type()
)
xRingProChainMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProChainMemberPort.setStatus("current")


class _XRingProChainAdd_Type(Integer32):
    """Custom type xRingProChainAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("add", 1))
    )


_XRingProChainAdd_Type.__name__ = "Integer32"
_XRingProChainAdd_Object = MibScalar
xRingProChainAdd = _XRingProChainAdd_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 14, 7, 5),
    _XRingProChainAdd_Type()
)
xRingProChainAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRingProChainAdd.setStatus("current")
_Gmrp_ObjectIdentity = ObjectIdentity
gmrp = _Gmrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 15)
)


class _GmrpStatus_Type(Integer32):
    """Custom type gmrpStatus based on Integer32"""
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


_GmrpStatus_Type.__name__ = "Integer32"
_GmrpStatus_Object = MibScalar
gmrpStatus = _GmrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 15, 1),
    _GmrpStatus_Type()
)
gmrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmrpStatus.setStatus("current")
_GmrpMulticastGroupTable_Object = MibTable
gmrpMulticastGroupTable = _GmrpMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 15, 2)
)
if mibBuilder.loadTexts:
    gmrpMulticastGroupTable.setStatus("current")
_GmrpMulticastGroupEntry_Object = MibTableRow
gmrpMulticastGroupEntry = _GmrpMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 15, 2, 1)
)
gmrpMulticastGroupEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "gmrpMulticastGroupVlanId"),
)
if mibBuilder.loadTexts:
    gmrpMulticastGroupEntry.setStatus("current")


class _GmrpMulticastGroupIndex_Type(Integer32):
    """Custom type gmrpMulticastGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_GmrpMulticastGroupIndex_Type.__name__ = "Integer32"
_GmrpMulticastGroupIndex_Object = MibTableColumn
gmrpMulticastGroupIndex = _GmrpMulticastGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 15, 2, 1, 1),
    _GmrpMulticastGroupIndex_Type()
)
gmrpMulticastGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmrpMulticastGroupIndex.setStatus("current")


class _GmrpMulticastGroupVlanId_Type(Integer32):
    """Custom type gmrpMulticastGroupVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_GmrpMulticastGroupVlanId_Type.__name__ = "Integer32"
_GmrpMulticastGroupVlanId_Object = MibTableColumn
gmrpMulticastGroupVlanId = _GmrpMulticastGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 15, 2, 1, 2),
    _GmrpMulticastGroupVlanId_Type()
)
gmrpMulticastGroupVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmrpMulticastGroupVlanId.setStatus("current")
_GmrpMulticastGroupMacAddress_Type = DisplayString
_GmrpMulticastGroupMacAddress_Object = MibTableColumn
gmrpMulticastGroupMacAddress = _GmrpMulticastGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 15, 2, 1, 3),
    _GmrpMulticastGroupMacAddress_Type()
)
gmrpMulticastGroupMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmrpMulticastGroupMacAddress.setStatus("current")


class _GmrpMulticastGroupType_Type(Integer32):
    """Custom type gmrpMulticastGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_GmrpMulticastGroupType_Type.__name__ = "Integer32"
_GmrpMulticastGroupType_Object = MibTableColumn
gmrpMulticastGroupType = _GmrpMulticastGroupType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 15, 2, 1, 4),
    _GmrpMulticastGroupType_Type()
)
gmrpMulticastGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmrpMulticastGroupType.setStatus("current")
_GmrpMulticastGroupMemberPorts_Type = DisplayString
_GmrpMulticastGroupMemberPorts_Object = MibTableColumn
gmrpMulticastGroupMemberPorts = _GmrpMulticastGroupMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 15, 2, 1, 5),
    _GmrpMulticastGroupMemberPorts_Type()
)
gmrpMulticastGroupMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmrpMulticastGroupMemberPorts.setStatus("current")
_Erps_ObjectIdentity = ObjectIdentity
erps = _Erps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16)
)


class _ErpsState_Type(Integer32):
    """Custom type erpsState based on Integer32"""
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


_ErpsState_Type.__name__ = "Integer32"
_ErpsState_Object = MibScalar
erpsState = _ErpsState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 1),
    _ErpsState_Type()
)
erpsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsState.setStatus("current")
_ErpsGroupTable_Object = MibTable
erpsGroupTable = _ErpsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2)
)
if mibBuilder.loadTexts:
    erpsGroupTable.setStatus("current")
_ErpsGroupEntry_Object = MibTableRow
erpsGroupEntry = _ErpsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1)
)
erpsGroupEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "erpsGroupRingId"),
)
if mibBuilder.loadTexts:
    erpsGroupEntry.setStatus("current")


class _ErpsGroupRingIndex_Type(Integer32):
    """Custom type erpsGroupRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ErpsGroupRingIndex_Type.__name__ = "Integer32"
_ErpsGroupRingIndex_Object = MibTableColumn
erpsGroupRingIndex = _ErpsGroupRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 1),
    _ErpsGroupRingIndex_Type()
)
erpsGroupRingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsGroupRingIndex.setStatus("current")


class _ErpsGroupInstance_Type(Integer32):
    """Custom type erpsGroupInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ErpsGroupInstance_Type.__name__ = "Integer32"
_ErpsGroupInstance_Object = MibTableColumn
erpsGroupInstance = _ErpsGroupInstance_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 2),
    _ErpsGroupInstance_Type()
)
erpsGroupInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsGroupInstance.setStatus("current")


class _ErpsGroupRingId_Type(Integer32):
    """Custom type erpsGroupRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ErpsGroupRingId_Type.__name__ = "Integer32"
_ErpsGroupRingId_Object = MibTableColumn
erpsGroupRingId = _ErpsGroupRingId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 3),
    _ErpsGroupRingId_Type()
)
erpsGroupRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsGroupRingId.setStatus("current")


class _ErpsGroupRole_Type(Integer32):
    """Custom type erpsGroupRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rplowner", 0),
          ("rplneighbor", 1),
          ("other", 2))
    )


_ErpsGroupRole_Type.__name__ = "Integer32"
_ErpsGroupRole_Object = MibTableColumn
erpsGroupRole = _ErpsGroupRole_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 4),
    _ErpsGroupRole_Type()
)
erpsGroupRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsGroupRole.setStatus("current")
_ErpsGroupState_Type = DisplayString
_ErpsGroupState_Object = MibTableColumn
erpsGroupState = _ErpsGroupState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 5),
    _ErpsGroupState_Type()
)
erpsGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsGroupState.setStatus("current")


class _ErpsGroupEastLink_Type(Integer32):
    """Custom type erpsGroupEastLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ErpsGroupEastLink_Type.__name__ = "Integer32"
_ErpsGroupEastLink_Object = MibTableColumn
erpsGroupEastLink = _ErpsGroupEastLink_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 6),
    _ErpsGroupEastLink_Type()
)
erpsGroupEastLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsGroupEastLink.setStatus("current")


class _ErpsGroupEastLinkRPL_Type(Integer32):
    """Custom type erpsGroupEastLinkRPL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rpl", 1),
          ("n-rpl", 2))
    )


_ErpsGroupEastLinkRPL_Type.__name__ = "Integer32"
_ErpsGroupEastLinkRPL_Object = MibTableColumn
erpsGroupEastLinkRPL = _ErpsGroupEastLinkRPL_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 7),
    _ErpsGroupEastLinkRPL_Type()
)
erpsGroupEastLinkRPL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsGroupEastLinkRPL.setStatus("current")
_ErpsGroupEastLinkState_Type = DisplayString
_ErpsGroupEastLinkState_Object = MibTableColumn
erpsGroupEastLinkState = _ErpsGroupEastLinkState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 8),
    _ErpsGroupEastLinkState_Type()
)
erpsGroupEastLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsGroupEastLinkState.setStatus("current")


class _ErpsGroupWestLink_Type(Integer32):
    """Custom type erpsGroupWestLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ErpsGroupWestLink_Type.__name__ = "Integer32"
_ErpsGroupWestLink_Object = MibTableColumn
erpsGroupWestLink = _ErpsGroupWestLink_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 9),
    _ErpsGroupWestLink_Type()
)
erpsGroupWestLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsGroupWestLink.setStatus("current")


class _ErpsGroupWestLinkRPL_Type(Integer32):
    """Custom type erpsGroupWestLinkRPL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rpl", 1),
          ("n-rpl", 2))
    )


_ErpsGroupWestLinkRPL_Type.__name__ = "Integer32"
_ErpsGroupWestLinkRPL_Object = MibTableColumn
erpsGroupWestLinkRPL = _ErpsGroupWestLinkRPL_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 10),
    _ErpsGroupWestLinkRPL_Type()
)
erpsGroupWestLinkRPL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsGroupWestLinkRPL.setStatus("current")
_ErpsGroupWestLinkState_Type = DisplayString
_ErpsGroupWestLinkState_Object = MibTableColumn
erpsGroupWestLinkState = _ErpsGroupWestLinkState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 11),
    _ErpsGroupWestLinkState_Type()
)
erpsGroupWestLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsGroupWestLinkState.setStatus("current")


class _ErpsGroupMEL_Type(Integer32):
    """Custom type erpsGroupMEL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ErpsGroupMEL_Type.__name__ = "Integer32"
_ErpsGroupMEL_Object = MibTableColumn
erpsGroupMEL = _ErpsGroupMEL_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 12),
    _ErpsGroupMEL_Type()
)
erpsGroupMEL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsGroupMEL.setStatus("current")


class _ErpsGroupRAPSChannelVlan_Type(Integer32):
    """Custom type erpsGroupRAPSChannelVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ErpsGroupRAPSChannelVlan_Type.__name__ = "Integer32"
_ErpsGroupRAPSChannelVlan_Object = MibTableColumn
erpsGroupRAPSChannelVlan = _ErpsGroupRAPSChannelVlan_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 13),
    _ErpsGroupRAPSChannelVlan_Type()
)
erpsGroupRAPSChannelVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsGroupRAPSChannelVlan.setStatus("current")


class _ErpsGroupTrafficChannel_Type(Integer32):
    """Custom type erpsGroupTrafficChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ErpsGroupTrafficChannel_Type.__name__ = "Integer32"
_ErpsGroupTrafficChannel_Object = MibTableColumn
erpsGroupTrafficChannel = _ErpsGroupTrafficChannel_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 14),
    _ErpsGroupTrafficChannel_Type()
)
erpsGroupTrafficChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsGroupTrafficChannel.setStatus("current")


class _ErpsGroupRevertive_Type(Integer32):
    """Custom type erpsGroupRevertive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("revertive", 1),
          ("none-revertive", 2))
    )


_ErpsGroupRevertive_Type.__name__ = "Integer32"
_ErpsGroupRevertive_Object = MibTableColumn
erpsGroupRevertive = _ErpsGroupRevertive_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 15),
    _ErpsGroupRevertive_Type()
)
erpsGroupRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsGroupRevertive.setStatus("current")


class _ErpsGroupType_Type(Integer32):
    """Custom type erpsGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("majorRing", 1),
          ("subRing", 2))
    )


_ErpsGroupType_Type.__name__ = "Integer32"
_ErpsGroupType_Object = MibTableColumn
erpsGroupType = _ErpsGroupType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 16),
    _ErpsGroupType_Type()
)
erpsGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsGroupType.setStatus("current")


class _ErpsGroupInterconnected_Type(Integer32):
    """Custom type erpsGroupInterconnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interconnected", 1),
          ("none-interconnected", 2))
    )


_ErpsGroupInterconnected_Type.__name__ = "Integer32"
_ErpsGroupInterconnected_Object = MibTableColumn
erpsGroupInterconnected = _ErpsGroupInterconnected_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 17),
    _ErpsGroupInterconnected_Type()
)
erpsGroupInterconnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsGroupInterconnected.setStatus("current")


class _ErpsGroupChannel_Type(Integer32):
    """Custom type erpsGroupChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("with-virtual-channel", 1),
          ("without-virtual-channel", 2))
    )


_ErpsGroupChannel_Type.__name__ = "Integer32"
_ErpsGroupChannel_Object = MibTableColumn
erpsGroupChannel = _ErpsGroupChannel_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 18),
    _ErpsGroupChannel_Type()
)
erpsGroupChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsGroupChannel.setStatus("current")


class _ErpsGroupTcPropagation_Type(Integer32):
    """Custom type erpsGroupTcPropagation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tc-propagation", 1),
          ("none-tc-propagation", 2))
    )


_ErpsGroupTcPropagation_Type.__name__ = "Integer32"
_ErpsGroupTcPropagation_Object = MibTableColumn
erpsGroupTcPropagation = _ErpsGroupTcPropagation_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 19),
    _ErpsGroupTcPropagation_Type()
)
erpsGroupTcPropagation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsGroupTcPropagation.setStatus("current")


class _ErpsWTRTimer_Type(Integer32):
    """Custom type erpsWTRTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ErpsWTRTimer_Type.__name__ = "Integer32"
_ErpsWTRTimer_Object = MibTableColumn
erpsWTRTimer = _ErpsWTRTimer_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 20),
    _ErpsWTRTimer_Type()
)
erpsWTRTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsWTRTimer.setStatus("current")
if mibBuilder.loadTexts:
    erpsWTRTimer.setUnits("Unit")


class _ErpsGuardTimer_Type(Integer32):
    """Custom type erpsGuardTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ErpsGuardTimer_Type.__name__ = "Integer32"
_ErpsGuardTimer_Object = MibTableColumn
erpsGuardTimer = _ErpsGuardTimer_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 21),
    _ErpsGuardTimer_Type()
)
erpsGuardTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsGuardTimer.setStatus("current")
if mibBuilder.loadTexts:
    erpsGuardTimer.setUnits("Unit")


class _ErpsHoldOffTimer_Type(Integer32):
    """Custom type erpsHoldOffTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ErpsHoldOffTimer_Type.__name__ = "Integer32"
_ErpsHoldOffTimer_Object = MibTableColumn
erpsHoldOffTimer = _ErpsHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 22),
    _ErpsHoldOffTimer_Type()
)
erpsHoldOffTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsHoldOffTimer.setStatus("current")
if mibBuilder.loadTexts:
    erpsHoldOffTimer.setUnits("Unit")


class _ErpsGroupRowStatus_Type(Integer32):
    """Custom type erpsGroupRowStatus based on Integer32"""
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )


_ErpsGroupRowStatus_Type.__name__ = "Integer32"
_ErpsGroupRowStatus_Object = MibTableColumn
erpsGroupRowStatus = _ErpsGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 3, 16, 2, 1, 99),
    _ErpsGroupRowStatus_Type()
)
erpsGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsGroupRowStatus.setStatus("current")
_MacAddressTable_ObjectIdentity = ObjectIdentity
macAddressTable = _MacAddressTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4)
)
_StaticMacSetting_ObjectIdentity = ObjectIdentity
staticMacSetting = _StaticMacSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 1)
)
_StaticMacSettingTable_Object = MibTable
staticMacSettingTable = _StaticMacSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 1, 1)
)
if mibBuilder.loadTexts:
    staticMacSettingTable.setStatus("current")
_StaticMacSettingEntry_Object = MibTableRow
staticMacSettingEntry = _StaticMacSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 1, 1, 1)
)
staticMacSettingEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "staticMacSettingIndex"),
)
if mibBuilder.loadTexts:
    staticMacSettingEntry.setStatus("current")


class _StaticMacSettingIndex_Type(Integer32):
    """Custom type staticMacSettingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_StaticMacSettingIndex_Type.__name__ = "Integer32"
_StaticMacSettingIndex_Object = MibTableColumn
staticMacSettingIndex = _StaticMacSettingIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 1, 1, 1, 1),
    _StaticMacSettingIndex_Type()
)
staticMacSettingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMacSettingIndex.setStatus("current")
_StaticMacSettingMacAddress_Type = DisplayString
_StaticMacSettingMacAddress_Object = MibTableColumn
staticMacSettingMacAddress = _StaticMacSettingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 1, 1, 1, 2),
    _StaticMacSettingMacAddress_Type()
)
staticMacSettingMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMacSettingMacAddress.setStatus("current")


class _StaticMacSettingVlan_Type(Integer32):
    """Custom type staticMacSettingVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_StaticMacSettingVlan_Type.__name__ = "Integer32"
_StaticMacSettingVlan_Object = MibTableColumn
staticMacSettingVlan = _StaticMacSettingVlan_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 1, 1, 1, 3),
    _StaticMacSettingVlan_Type()
)
staticMacSettingVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMacSettingVlan.setStatus("current")
_StaticMacSettingPort_Type = Integer32
_StaticMacSettingPort_Object = MibTableColumn
staticMacSettingPort = _StaticMacSettingPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 1, 1, 1, 4),
    _StaticMacSettingPort_Type()
)
staticMacSettingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMacSettingPort.setStatus("current")


class _StaticMacSettingRowStatus_Type(Integer32):
    """Custom type staticMacSettingRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("createAndWait", 5),
          ("destory", 6))
    )


_StaticMacSettingRowStatus_Type.__name__ = "Integer32"
_StaticMacSettingRowStatus_Object = MibTableColumn
staticMacSettingRowStatus = _StaticMacSettingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 1, 1, 1, 99),
    _StaticMacSettingRowStatus_Type()
)
staticMacSettingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticMacSettingRowStatus.setStatus("current")
_DynamicMacSetting_ObjectIdentity = ObjectIdentity
dynamicMacSetting = _DynamicMacSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 2)
)


class _MacAgingTime_Type(Integer32):
    """Custom type macAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 630),
    )


_MacAgingTime_Type.__name__ = "Integer32"
_MacAgingTime_Object = MibScalar
macAgingTime = _MacAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 2, 1),
    _MacAgingTime_Type()
)
macAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAgingTime.setStatus("current")
_DynamicLearned_ObjectIdentity = ObjectIdentity
dynamicLearned = _DynamicLearned_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 3)
)


class _ClearMacAddressTable_Type(Integer32):
    """Custom type clearMacAddressTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_ClearMacAddressTable_Type.__name__ = "Integer32"
_ClearMacAddressTable_Object = MibScalar
clearMacAddressTable = _ClearMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 3, 1),
    _ClearMacAddressTable_Type()
)
clearMacAddressTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearMacAddressTable.setStatus("current")
_MacAddressInfoTable_Object = MibTable
macAddressInfoTable = _MacAddressInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 3, 2)
)
if mibBuilder.loadTexts:
    macAddressInfoTable.setStatus("current")
_MacAddressInfoEntry_Object = MibTableRow
macAddressInfoEntry = _MacAddressInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 3, 2, 1)
)
macAddressInfoEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "macAddressInfoIndex"),
)
if mibBuilder.loadTexts:
    macAddressInfoEntry.setStatus("current")


class _MacAddressInfoIndex_Type(Integer32):
    """Custom type macAddressInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MacAddressInfoIndex_Type.__name__ = "Integer32"
_MacAddressInfoIndex_Object = MibTableColumn
macAddressInfoIndex = _MacAddressInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 3, 2, 1, 1),
    _MacAddressInfoIndex_Type()
)
macAddressInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddressInfoIndex.setStatus("current")
_MacAddressInfoMAC_Type = DisplayString
_MacAddressInfoMAC_Object = MibTableColumn
macAddressInfoMAC = _MacAddressInfoMAC_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 3, 2, 1, 2),
    _MacAddressInfoMAC_Type()
)
macAddressInfoMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddressInfoMAC.setStatus("current")


class _MacAddressInfoVlan_Type(Integer32):
    """Custom type macAddressInfoVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MacAddressInfoVlan_Type.__name__ = "Integer32"
_MacAddressInfoVlan_Object = MibTableColumn
macAddressInfoVlan = _MacAddressInfoVlan_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 3, 2, 1, 3),
    _MacAddressInfoVlan_Type()
)
macAddressInfoVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddressInfoVlan.setStatus("current")


class _MacAddressInfoType_Type(Integer32):
    """Custom type macAddressInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_MacAddressInfoType_Type.__name__ = "Integer32"
_MacAddressInfoType_Object = MibTableColumn
macAddressInfoType = _MacAddressInfoType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 3, 2, 1, 4),
    _MacAddressInfoType_Type()
)
macAddressInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddressInfoType.setStatus("current")
_MacAddressInfoPort_Type = DisplayString
_MacAddressInfoPort_Object = MibTableColumn
macAddressInfoPort = _MacAddressInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 3, 2, 1, 5),
    _MacAddressInfoPort_Type()
)
macAddressInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddressInfoPort.setStatus("current")


class _AddtoStaticMacTable_Type(Integer32):
    """Custom type addtoStaticMacTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("addtoStaticMac", 1))
    )


_AddtoStaticMacTable_Type.__name__ = "Integer32"
_AddtoStaticMacTable_Object = MibTableColumn
addtoStaticMacTable = _AddtoStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 4, 3, 2, 1, 6),
    _AddtoStaticMacTable_Type()
)
addtoStaticMacTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addtoStaticMacTable.setStatus("current")
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5)
)
_StormControl_ObjectIdentity = ObjectIdentity
stormControl = _StormControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 1)
)


class _StromControlUnit_Type(Integer32):
    """Custom type stromControlUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pps", 1),
          ("bps", 2))
    )


_StromControlUnit_Type.__name__ = "Integer32"
_StromControlUnit_Object = MibScalar
stromControlUnit = _StromControlUnit_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 1, 1),
    _StromControlUnit_Type()
)
stromControlUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stromControlUnit.setStatus("current")


class _StromControlPreamble_IFG_Type(Integer32):
    """Custom type stromControlPreamble_IFG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 1),
          ("included", 2))
    )


_StromControlPreamble_IFG_Type.__name__ = "Integer32"
_StromControlPreamble_IFG_Object = MibScalar
stromControlPreamble_IFG = _StromControlPreamble_IFG_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 1, 2),
    _StromControlPreamble_IFG_Type()
)
stromControlPreamble_IFG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stromControlPreamble_IFG.setStatus("current")
_StromControlPortTable_Object = MibTable
stromControlPortTable = _StromControlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 1, 3)
)
if mibBuilder.loadTexts:
    stromControlPortTable.setStatus("current")
_StromControlPortEntry_Object = MibTableRow
stromControlPortEntry = _StromControlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 1, 3, 1)
)
stromControlPortEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "stromControlPortIndex"),
)
if mibBuilder.loadTexts:
    stromControlPortEntry.setStatus("current")


class _StromControlPortIndex_Type(Integer32):
    """Custom type stromControlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StromControlPortIndex_Type.__name__ = "Integer32"
_StromControlPortIndex_Object = MibTableColumn
stromControlPortIndex = _StromControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 1, 3, 1, 1),
    _StromControlPortIndex_Type()
)
stromControlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stromControlPortIndex.setStatus("current")


class _StromControlPortState_Type(Integer32):
    """Custom type stromControlPortState based on Integer32"""
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


_StromControlPortState_Type.__name__ = "Integer32"
_StromControlPortState_Object = MibTableColumn
stromControlPortState = _StromControlPortState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 1, 3, 1, 2),
    _StromControlPortState_Type()
)
stromControlPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stromControlPortState.setStatus("current")


class _StromControlPortAction_Type(Integer32):
    """Custom type stromControlPortAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("shutdown", 2))
    )


_StromControlPortAction_Type.__name__ = "Integer32"
_StromControlPortAction_Object = MibTableColumn
stromControlPortAction = _StromControlPortAction_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 1, 3, 1, 3),
    _StromControlPortAction_Type()
)
stromControlPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stromControlPortAction.setStatus("current")


class _Enablebroadcast_Type(Integer32):
    """Custom type enablebroadcast based on Integer32"""
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


_Enablebroadcast_Type.__name__ = "Integer32"
_Enablebroadcast_Object = MibTableColumn
enablebroadcast = _Enablebroadcast_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 1, 3, 1, 4),
    _Enablebroadcast_Type()
)
enablebroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablebroadcast.setStatus("current")


class _BroadcastRate_Type(Integer32):
    """Custom type broadcastRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_BroadcastRate_Type.__name__ = "Integer32"
_BroadcastRate_Object = MibTableColumn
broadcastRate = _BroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 1, 3, 1, 5),
    _BroadcastRate_Type()
)
broadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastRate.setStatus("current")


class _EnableunknownMulticast_Type(Integer32):
    """Custom type enableunknownMulticast based on Integer32"""
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


_EnableunknownMulticast_Type.__name__ = "Integer32"
_EnableunknownMulticast_Object = MibTableColumn
enableunknownMulticast = _EnableunknownMulticast_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 1, 3, 1, 6),
    _EnableunknownMulticast_Type()
)
enableunknownMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableunknownMulticast.setStatus("current")


class _UnknownMulticastRate_Type(Integer32):
    """Custom type unknownMulticastRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_UnknownMulticastRate_Type.__name__ = "Integer32"
_UnknownMulticastRate_Object = MibTableColumn
unknownMulticastRate = _UnknownMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 1, 3, 1, 7),
    _UnknownMulticastRate_Type()
)
unknownMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unknownMulticastRate.setStatus("current")


class _EnableunknownUnicast_Type(Integer32):
    """Custom type enableunknownUnicast based on Integer32"""
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


_EnableunknownUnicast_Type.__name__ = "Integer32"
_EnableunknownUnicast_Object = MibTableColumn
enableunknownUnicast = _EnableunknownUnicast_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 1, 3, 1, 8),
    _EnableunknownUnicast_Type()
)
enableunknownUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableunknownUnicast.setStatus("current")


class _UnknownUnicastRate_Type(Integer32):
    """Custom type unknownUnicastRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_UnknownUnicastRate_Type.__name__ = "Integer32"
_UnknownUnicastRate_Object = MibTableColumn
unknownUnicastRate = _UnknownUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 1, 3, 1, 9),
    _UnknownUnicastRate_Type()
)
unknownUnicastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unknownUnicastRate.setStatus("current")
_ProtectedPort_ObjectIdentity = ObjectIdentity
protectedPort = _ProtectedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 2)
)
_ProtectedPortTable_Object = MibTable
protectedPortTable = _ProtectedPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 2, 1)
)
if mibBuilder.loadTexts:
    protectedPortTable.setStatus("current")
_ProtectedPortEntry_Object = MibTableRow
protectedPortEntry = _ProtectedPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 2, 1, 1)
)
protectedPortEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "protectedPortIndex"),
)
if mibBuilder.loadTexts:
    protectedPortEntry.setStatus("current")


class _ProtectedPortIndex_Type(Integer32):
    """Custom type protectedPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ProtectedPortIndex_Type.__name__ = "Integer32"
_ProtectedPortIndex_Object = MibTableColumn
protectedPortIndex = _ProtectedPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 2, 1, 1, 1),
    _ProtectedPortIndex_Type()
)
protectedPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectedPortIndex.setStatus("current")


class _ProtectedPortType_Type(Integer32):
    """Custom type protectedPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unprotected", 1),
          ("porotected", 2))
    )


_ProtectedPortType_Type.__name__ = "Integer32"
_ProtectedPortType_Object = MibTableColumn
protectedPortType = _ProtectedPortType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 2, 1, 1, 2),
    _ProtectedPortType_Type()
)
protectedPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protectedPortType.setStatus("current")
_Dos_ObjectIdentity = ObjectIdentity
dos = _Dos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3)
)


class _DmacEqualsmac_Type(Integer32):
    """Custom type dmacEqualsmac based on Integer32"""
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


_DmacEqualsmac_Type.__name__ = "Integer32"
_DmacEqualsmac_Object = MibScalar
dmacEqualsmac = _DmacEqualsmac_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 1),
    _DmacEqualsmac_Type()
)
dmacEqualsmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmacEqualsmac.setStatus("current")


class _Land_Type(Integer32):
    """Custom type land based on Integer32"""
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


_Land_Type.__name__ = "Integer32"
_Land_Object = MibScalar
land = _Land_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 2),
    _Land_Type()
)
land.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    land.setStatus("current")


class _UdpBlat_Type(Integer32):
    """Custom type udpBlat based on Integer32"""
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


_UdpBlat_Type.__name__ = "Integer32"
_UdpBlat_Object = MibScalar
udpBlat = _UdpBlat_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 3),
    _UdpBlat_Type()
)
udpBlat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpBlat.setStatus("current")


class _TcpBlat_Type(Integer32):
    """Custom type tcpBlat based on Integer32"""
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


_TcpBlat_Type.__name__ = "Integer32"
_TcpBlat_Object = MibScalar
tcpBlat = _TcpBlat_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 4),
    _TcpBlat_Type()
)
tcpBlat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpBlat.setStatus("current")


class _Pod_Type(Integer32):
    """Custom type pod based on Integer32"""
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


_Pod_Type.__name__ = "Integer32"
_Pod_Object = MibScalar
pod = _Pod_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 5),
    _Pod_Type()
)
pod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pod.setStatus("current")


class _Ipv6MinFragment_Type(Integer32):
    """Custom type ipv6MinFragment based on Integer32"""
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


_Ipv6MinFragment_Type.__name__ = "Integer32"
_Ipv6MinFragment_Object = MibScalar
ipv6MinFragment = _Ipv6MinFragment_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 6),
    _Ipv6MinFragment_Type()
)
ipv6MinFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6MinFragment.setStatus("current")


class _Ipv6MinFragmentValue_Type(Integer32):
    """Custom type ipv6MinFragmentValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ipv6MinFragmentValue_Type.__name__ = "Integer32"
_Ipv6MinFragmentValue_Object = MibScalar
ipv6MinFragmentValue = _Ipv6MinFragmentValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 7),
    _Ipv6MinFragmentValue_Type()
)
ipv6MinFragmentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6MinFragmentValue.setStatus("current")


class _IcmpFragment_Type(Integer32):
    """Custom type icmpFragment based on Integer32"""
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


_IcmpFragment_Type.__name__ = "Integer32"
_IcmpFragment_Object = MibScalar
icmpFragment = _IcmpFragment_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 8),
    _IcmpFragment_Type()
)
icmpFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmpFragment.setStatus("current")


class _Ipv4PingMaxSize_Type(Integer32):
    """Custom type ipv4PingMaxSize based on Integer32"""
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


_Ipv4PingMaxSize_Type.__name__ = "Integer32"
_Ipv4PingMaxSize_Object = MibScalar
ipv4PingMaxSize = _Ipv4PingMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 9),
    _Ipv4PingMaxSize_Type()
)
ipv4PingMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4PingMaxSize.setStatus("current")


class _Ipv6PingMaxSize_Type(Integer32):
    """Custom type ipv6PingMaxSize based on Integer32"""
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


_Ipv6PingMaxSize_Type.__name__ = "Integer32"
_Ipv6PingMaxSize_Object = MibScalar
ipv6PingMaxSize = _Ipv6PingMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 10),
    _Ipv6PingMaxSize_Type()
)
ipv6PingMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6PingMaxSize.setStatus("current")


class _PingMaxSizeSetting_Type(Integer32):
    """Custom type pingMaxSizeSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PingMaxSizeSetting_Type.__name__ = "Integer32"
_PingMaxSizeSetting_Object = MibScalar
pingMaxSizeSetting = _PingMaxSizeSetting_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 11),
    _PingMaxSizeSetting_Type()
)
pingMaxSizeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingMaxSizeSetting.setStatus("current")


class _SmurfAttack_Type(Integer32):
    """Custom type smurfAttack based on Integer32"""
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


_SmurfAttack_Type.__name__ = "Integer32"
_SmurfAttack_Object = MibScalar
smurfAttack = _SmurfAttack_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 12),
    _SmurfAttack_Type()
)
smurfAttack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smurfAttack.setStatus("current")


class _SmurfAttackValue_Type(Integer32):
    """Custom type smurfAttackValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SmurfAttackValue_Type.__name__ = "Integer32"
_SmurfAttackValue_Object = MibScalar
smurfAttackValue = _SmurfAttackValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 13),
    _SmurfAttackValue_Type()
)
smurfAttackValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smurfAttackValue.setStatus("current")


class _TcpMinHdrSize_Type(Integer32):
    """Custom type tcpMinHdrSize based on Integer32"""
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


_TcpMinHdrSize_Type.__name__ = "Integer32"
_TcpMinHdrSize_Object = MibScalar
tcpMinHdrSize = _TcpMinHdrSize_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 14),
    _TcpMinHdrSize_Type()
)
tcpMinHdrSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpMinHdrSize.setStatus("current")


class _TcpMinHdrSizeValue_Type(Integer32):
    """Custom type tcpMinHdrSizeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_TcpMinHdrSizeValue_Type.__name__ = "Integer32"
_TcpMinHdrSizeValue_Object = MibScalar
tcpMinHdrSizeValue = _TcpMinHdrSizeValue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 15),
    _TcpMinHdrSizeValue_Type()
)
tcpMinHdrSizeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpMinHdrSizeValue.setStatus("current")


class _Tcp_Syn_Type(Integer32):
    """Custom type tcp_Syn based on Integer32"""
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


_Tcp_Syn_Type.__name__ = "Integer32"
_Tcp_Syn_Object = MibScalar
tcp_Syn = _Tcp_Syn_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 16),
    _Tcp_Syn_Type()
)
tcp_Syn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcp_Syn.setStatus("current")


class _NullScanAttack_Type(Integer32):
    """Custom type nullScanAttack based on Integer32"""
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


_NullScanAttack_Type.__name__ = "Integer32"
_NullScanAttack_Object = MibScalar
nullScanAttack = _NullScanAttack_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 17),
    _NullScanAttack_Type()
)
nullScanAttack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nullScanAttack.setStatus("current")


class _XMasScanAttack_Type(Integer32):
    """Custom type xMasScanAttack based on Integer32"""
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


_XMasScanAttack_Type.__name__ = "Integer32"
_XMasScanAttack_Object = MibScalar
xMasScanAttack = _XMasScanAttack_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 18),
    _XMasScanAttack_Type()
)
xMasScanAttack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xMasScanAttack.setStatus("current")


class _TcpSYN_FINAttack_Type(Integer32):
    """Custom type tcpSYN_FINAttack based on Integer32"""
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


_TcpSYN_FINAttack_Type.__name__ = "Integer32"
_TcpSYN_FINAttack_Object = MibScalar
tcpSYN_FINAttack = _TcpSYN_FINAttack_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 19),
    _TcpSYN_FINAttack_Type()
)
tcpSYN_FINAttack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpSYN_FINAttack.setStatus("current")


class _TcpSYN_RSTAttack_Type(Integer32):
    """Custom type tcpSYN_RSTAttack based on Integer32"""
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


_TcpSYN_RSTAttack_Type.__name__ = "Integer32"
_TcpSYN_RSTAttack_Object = MibScalar
tcpSYN_RSTAttack = _TcpSYN_RSTAttack_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 20),
    _TcpSYN_RSTAttack_Type()
)
tcpSYN_RSTAttack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpSYN_RSTAttack.setStatus("current")


class _TcpFragment_Type(Integer32):
    """Custom type tcpFragment based on Integer32"""
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


_TcpFragment_Type.__name__ = "Integer32"
_TcpFragment_Object = MibScalar
tcpFragment = _TcpFragment_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 21),
    _TcpFragment_Type()
)
tcpFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpFragment.setStatus("current")
_DosPortTable_Object = MibTable
dosPortTable = _DosPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 22)
)
if mibBuilder.loadTexts:
    dosPortTable.setStatus("current")
_DosPortEntry_Object = MibTableRow
dosPortEntry = _DosPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 22, 1)
)
dosPortEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "dosportIndex"),
)
if mibBuilder.loadTexts:
    dosPortEntry.setStatus("current")


class _DosportIndex_Type(Integer32):
    """Custom type dosportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DosportIndex_Type.__name__ = "Integer32"
_DosportIndex_Object = MibTableColumn
dosportIndex = _DosportIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 22, 1, 1),
    _DosportIndex_Type()
)
dosportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosportIndex.setStatus("current")


class _DosProtection_Type(Integer32):
    """Custom type dosProtection based on Integer32"""
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


_DosProtection_Type.__name__ = "Integer32"
_DosProtection_Object = MibTableColumn
dosProtection = _DosProtection_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 3, 22, 1, 2),
    _DosProtection_Type()
)
dosProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosProtection.setStatus("current")
_Access_ObjectIdentity = ObjectIdentity
access = _Access_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 4)
)
_TelnetInfo_ObjectIdentity = ObjectIdentity
telnetInfo = _TelnetInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 4, 1)
)


class _TelnetService_Type(Integer32):
    """Custom type telnetService based on Integer32"""
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


_TelnetService_Type.__name__ = "Integer32"
_TelnetService_Object = MibScalar
telnetService = _TelnetService_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 4, 1, 1),
    _TelnetService_Type()
)
telnetService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetService.setStatus("current")
_CurrentTelnetSessionCount_Type = Integer32
_CurrentTelnetSessionCount_Object = MibScalar
currentTelnetSessionCount = _CurrentTelnetSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 4, 1, 2),
    _CurrentTelnetSessionCount_Type()
)
currentTelnetSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentTelnetSessionCount.setStatus("current")
_HttpSetting_ObjectIdentity = ObjectIdentity
httpSetting = _HttpSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 4, 2)
)


class _HttpService_Type(Integer32):
    """Custom type httpService based on Integer32"""
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


_HttpService_Type.__name__ = "Integer32"
_HttpService_Object = MibScalar
httpService = _HttpService_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 4, 2, 1),
    _HttpService_Type()
)
httpService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpService.setStatus("current")


class _HttpSessionTimeout_Type(Integer32):
    """Custom type httpSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_HttpSessionTimeout_Type.__name__ = "Integer32"
_HttpSessionTimeout_Object = MibScalar
httpSessionTimeout = _HttpSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 4, 2, 2),
    _HttpSessionTimeout_Type()
)
httpSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpSessionTimeout.setStatus("current")
_HttpsSetting_ObjectIdentity = ObjectIdentity
httpsSetting = _HttpsSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 4, 3)
)


class _HttpsService_Type(Integer32):
    """Custom type httpsService based on Integer32"""
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


_HttpsService_Type.__name__ = "Integer32"
_HttpsService_Object = MibScalar
httpsService = _HttpsService_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 4, 3, 1),
    _HttpsService_Type()
)
httpsService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpsService.setStatus("current")


class _HttpsSessionTimeout_Type(Integer32):
    """Custom type httpsSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_HttpsSessionTimeout_Type.__name__ = "Integer32"
_HttpsSessionTimeout_Object = MibScalar
httpsSessionTimeout = _HttpsSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 4, 3, 2),
    _HttpsSessionTimeout_Type()
)
httpsSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpsSessionTimeout.setStatus("current")
_SshInfo_ObjectIdentity = ObjectIdentity
sshInfo = _SshInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 4, 4)
)


class _SshService_Type(Integer32):
    """Custom type sshService based on Integer32"""
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


_SshService_Type.__name__ = "Integer32"
_SshService_Object = MibScalar
sshService = _SshService_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 4, 4, 1),
    _SshService_Type()
)
sshService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshService.setStatus("current")
_PortSecurity_ObjectIdentity = ObjectIdentity
portSecurity = _PortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 5)
)
_PortSecurityTable_Object = MibTable
portSecurityTable = _PortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 5, 1)
)
if mibBuilder.loadTexts:
    portSecurityTable.setStatus("current")
_PortSecurityEntry_Object = MibTableRow
portSecurityEntry = _PortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 5, 1, 1)
)
portSecurityEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "portSecurityPortIndex"),
)
if mibBuilder.loadTexts:
    portSecurityEntry.setStatus("current")


class _PortSecurityPortIndex_Type(Integer32):
    """Custom type portSecurityPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortSecurityPortIndex_Type.__name__ = "Integer32"
_PortSecurityPortIndex_Object = MibTableColumn
portSecurityPortIndex = _PortSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 5, 1, 1, 1),
    _PortSecurityPortIndex_Type()
)
portSecurityPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityPortIndex.setStatus("current")


class _PortSecurityEnabled_Type(Integer32):
    """Custom type portSecurityEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_PortSecurityEnabled_Type.__name__ = "Integer32"
_PortSecurityEnabled_Object = MibTableColumn
portSecurityEnabled = _PortSecurityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 5, 1, 1, 2),
    _PortSecurityEnabled_Type()
)
portSecurityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityEnabled.setStatus("current")


class _PortSecurityFDBLimit_Type(Integer32):
    """Custom type portSecurityFDBLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PortSecurityFDBLimit_Type.__name__ = "Integer32"
_PortSecurityFDBLimit_Object = MibTableColumn
portSecurityFDBLimit = _PortSecurityFDBLimit_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 5, 1, 1, 3),
    _PortSecurityFDBLimit_Type()
)
portSecurityFDBLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityFDBLimit.setStatus("current")


class _PortSecurityViolationMACNotify_Type(Integer32):
    """Custom type portSecurityViolationMACNotify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_PortSecurityViolationMACNotify_Type.__name__ = "Integer32"
_PortSecurityViolationMACNotify_Object = MibTableColumn
portSecurityViolationMACNotify = _PortSecurityViolationMACNotify_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 5, 1, 1, 4),
    _PortSecurityViolationMACNotify_Type()
)
portSecurityViolationMACNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityViolationMACNotify.setStatus("current")
_IpSecurity_ObjectIdentity = ObjectIdentity
ipSecurity = _IpSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 6)
)


class _IpSecurityStatus_Type(Integer32):
    """Custom type ipSecurityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpSecurityStatus_Type.__name__ = "Integer32"
_IpSecurityStatus_Object = MibScalar
ipSecurityStatus = _IpSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 6, 1),
    _IpSecurityStatus_Type()
)
ipSecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecurityStatus.setStatus("current")
_IpSecurityTable_Object = MibTable
ipSecurityTable = _IpSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 6, 2)
)
if mibBuilder.loadTexts:
    ipSecurityTable.setStatus("current")
_IpSecurityEntry_Object = MibTableRow
ipSecurityEntry = _IpSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 6, 2, 1)
)
ipSecurityEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "ipSecurityIndex"),
)
if mibBuilder.loadTexts:
    ipSecurityEntry.setStatus("current")


class _IpSecurityIndex_Type(Integer32):
    """Custom type ipSecurityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IpSecurityIndex_Type.__name__ = "Integer32"
_IpSecurityIndex_Object = MibTableColumn
ipSecurityIndex = _IpSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 6, 2, 1, 1),
    _IpSecurityIndex_Type()
)
ipSecurityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecurityIndex.setStatus("current")
_IpSecurityIPAddr_Type = IpAddress
_IpSecurityIPAddr_Object = MibTableColumn
ipSecurityIPAddr = _IpSecurityIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 6, 2, 1, 2),
    _IpSecurityIPAddr_Type()
)
ipSecurityIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecurityIPAddr.setStatus("current")
_IpSecurityIPMask_Type = IpAddress
_IpSecurityIPMask_Object = MibTableColumn
ipSecurityIPMask = _IpSecurityIPMask_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 6, 2, 1, 3),
    _IpSecurityIPMask_Type()
)
ipSecurityIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecurityIPMask.setStatus("current")


class _IpSecurityService_Type(Bits):
    """Custom type ipSecurityService based on Bits"""
    namedValues = NamedValues(
        *(("ping", 0),
          ("http", 1),
          ("telnet", 2),
          ("ssh", 3),
          ("snmp", 4))
    )

_IpSecurityService_Type.__name__ = "Bits"
_IpSecurityService_Object = MibTableColumn
ipSecurityService = _IpSecurityService_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 6, 2, 1, 4),
    _IpSecurityService_Type()
)
ipSecurityService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecurityService.setStatus("current")


class _IpSecurityVlanId_Type(Integer32):
    """Custom type ipSecurityVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IpSecurityVlanId_Type.__name__ = "Integer32"
_IpSecurityVlanId_Object = MibTableColumn
ipSecurityVlanId = _IpSecurityVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 6, 2, 1, 5),
    _IpSecurityVlanId_Type()
)
ipSecurityVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecurityVlanId.setStatus("current")


class _IpSecurityRowStatus_Type(Integer32):
    """Custom type ipSecurityRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("createAndWait", 5),
          ("destory", 6))
    )


_IpSecurityRowStatus_Type.__name__ = "Integer32"
_IpSecurityRowStatus_Object = MibTableColumn
ipSecurityRowStatus = _IpSecurityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 6, 2, 1, 99),
    _IpSecurityRowStatus_Type()
)
ipSecurityRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecurityRowStatus.setStatus("current")
_Ieee8021x_ObjectIdentity = ObjectIdentity
ieee8021x = _Ieee8021x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 7)
)


class _Ieee8021xState_Type(Integer32):
    """Custom type ieee8021xState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_Ieee8021xState_Type.__name__ = "Integer32"
_Ieee8021xState_Object = MibScalar
ieee8021xState = _Ieee8021xState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 7, 1),
    _Ieee8021xState_Type()
)
ieee8021xState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021xState.setStatus("current")
_Ieee8021xServerIP_Type = IpAddress
_Ieee8021xServerIP_Object = MibScalar
ieee8021xServerIP = _Ieee8021xServerIP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 7, 2),
    _Ieee8021xServerIP_Type()
)
ieee8021xServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021xServerIP.setStatus("current")


class _Ieee8021xServerPort_Type(Integer32):
    """Custom type ieee8021xServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ieee8021xServerPort_Type.__name__ = "Integer32"
_Ieee8021xServerPort_Object = MibScalar
ieee8021xServerPort = _Ieee8021xServerPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 7, 3),
    _Ieee8021xServerPort_Type()
)
ieee8021xServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021xServerPort.setStatus("current")


class _Ieee8021xAccountingPort_Type(Integer32):
    """Custom type ieee8021xAccountingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ieee8021xAccountingPort_Type.__name__ = "Integer32"
_Ieee8021xAccountingPort_Object = MibScalar
ieee8021xAccountingPort = _Ieee8021xAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 7, 4),
    _Ieee8021xAccountingPort_Type()
)
ieee8021xAccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021xAccountingPort.setStatus("current")
_Ieee8021xSecurityKey_Type = DisplayString
_Ieee8021xSecurityKey_Object = MibScalar
ieee8021xSecurityKey = _Ieee8021xSecurityKey_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 7, 5),
    _Ieee8021xSecurityKey_Type()
)
ieee8021xSecurityKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021xSecurityKey.setStatus("current")


class _Ieee8021xReauthPeriod_Type(Integer32):
    """Custom type ieee8021xReauthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ieee8021xReauthPeriod_Type.__name__ = "Integer32"
_Ieee8021xReauthPeriod_Object = MibScalar
ieee8021xReauthPeriod = _Ieee8021xReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 7, 6),
    _Ieee8021xReauthPeriod_Type()
)
ieee8021xReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021xReauthPeriod.setStatus("current")
_Ieee8021xPortTable_Object = MibTable
ieee8021xPortTable = _Ieee8021xPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 7, 7)
)
if mibBuilder.loadTexts:
    ieee8021xPortTable.setStatus("current")
_Ieee8021xPortEntry_Object = MibTableRow
ieee8021xPortEntry = _Ieee8021xPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 7, 7, 1)
)
ieee8021xPortEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "ieee8021xPortIndex"),
)
if mibBuilder.loadTexts:
    ieee8021xPortEntry.setStatus("current")


class _Ieee8021xPortIndex_Type(Integer32):
    """Custom type ieee8021xPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ieee8021xPortIndex_Type.__name__ = "Integer32"
_Ieee8021xPortIndex_Object = MibTableColumn
ieee8021xPortIndex = _Ieee8021xPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 7, 7, 1, 1),
    _Ieee8021xPortIndex_Type()
)
ieee8021xPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021xPortIndex.setStatus("current")


class _Ieee8021xPortState_Type(Integer32):
    """Custom type ieee8021xPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorize", 1),
          ("disabled", 2))
    )


_Ieee8021xPortState_Type.__name__ = "Integer32"
_Ieee8021xPortState_Object = MibTableColumn
ieee8021xPortState = _Ieee8021xPortState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 7, 7, 1, 2),
    _Ieee8021xPortState_Type()
)
ieee8021xPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021xPortState.setStatus("current")


class _Ieee8021xAuthBased_Type(Integer32):
    """Custom type ieee8021xAuthBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("mac", 2),
          ("mac-auth-bypass", 3))
    )


_Ieee8021xAuthBased_Type.__name__ = "Integer32"
_Ieee8021xAuthBased_Object = MibScalar
ieee8021xAuthBased = _Ieee8021xAuthBased_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 7, 8),
    _Ieee8021xAuthBased_Type()
)
ieee8021xAuthBased.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021xAuthBased.setStatus("current")
_SecurityLogin_ObjectIdentity = ObjectIdentity
securityLogin = _SecurityLogin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 8)
)


class _SecurityLoginState_Type(Integer32):
    """Custom type securityLoginState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SecurityLoginState_Type.__name__ = "Integer32"
_SecurityLoginState_Object = MibScalar
securityLoginState = _SecurityLoginState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 8, 1),
    _SecurityLoginState_Type()
)
securityLoginState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityLoginState.setStatus("current")
_RadiusServer_ObjectIdentity = ObjectIdentity
radiusServer = _RadiusServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 8, 2)
)
_RadiusServerIP_Type = IpAddress
_RadiusServerIP_Object = MibScalar
radiusServerIP = _RadiusServerIP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 8, 2, 1),
    _RadiusServerIP_Type()
)
radiusServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerIP.setStatus("current")


class _RadiusServerPort_Type(Integer32):
    """Custom type radiusServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerPort_Type.__name__ = "Integer32"
_RadiusServerPort_Object = MibScalar
radiusServerPort = _RadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 8, 2, 2),
    _RadiusServerPort_Type()
)
radiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerPort.setStatus("current")
_RadiusServerSecurityKey_Type = DisplayString
_RadiusServerSecurityKey_Object = MibScalar
radiusServerSecurityKey = _RadiusServerSecurityKey_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 8, 2, 3),
    _RadiusServerSecurityKey_Type()
)
radiusServerSecurityKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerSecurityKey.setStatus("current")
_TacacsServer_ObjectIdentity = ObjectIdentity
tacacsServer = _TacacsServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 8, 3)
)
_TacacsServerIP_Type = IpAddress
_TacacsServerIP_Object = MibScalar
tacacsServerIP = _TacacsServerIP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 8, 3, 1),
    _TacacsServerIP_Type()
)
tacacsServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsServerIP.setStatus("current")


class _TacacsServerPort_Type(Integer32):
    """Custom type tacacsServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TacacsServerPort_Type.__name__ = "Integer32"
_TacacsServerPort_Object = MibScalar
tacacsServerPort = _TacacsServerPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 8, 3, 2),
    _TacacsServerPort_Type()
)
tacacsServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsServerPort.setStatus("current")
_TacacsServerSecurityKey_Type = DisplayString
_TacacsServerSecurityKey_Object = MibScalar
tacacsServerSecurityKey = _TacacsServerSecurityKey_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 8, 3, 3),
    _TacacsServerSecurityKey_Type()
)
tacacsServerSecurityKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsServerSecurityKey.setStatus("current")


class _SecurityLoginType_Type(Integer32):
    """Custom type securityLoginType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("radius", 1),
          ("tacacs", 2),
          ("radiusAndtacacs", 3),
          ("radiusAndtacacsAndweb", 4))
    )


_SecurityLoginType_Type.__name__ = "Integer32"
_SecurityLoginType_Object = MibScalar
securityLoginType = _SecurityLoginType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 8, 4),
    _SecurityLoginType_Type()
)
securityLoginType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityLoginType.setStatus("current")


class _SecurityLoginHttpState_Type(Integer32):
    """Custom type securityLoginHttpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SecurityLoginHttpState_Type.__name__ = "Integer32"
_SecurityLoginHttpState_Object = MibScalar
securityLoginHttpState = _SecurityLoginHttpState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 8, 5),
    _SecurityLoginHttpState_Type()
)
securityLoginHttpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityLoginHttpState.setStatus("current")


class _SecurityLoginTelnetState_Type(Integer32):
    """Custom type securityLoginTelnetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SecurityLoginTelnetState_Type.__name__ = "Integer32"
_SecurityLoginTelnetState_Object = MibScalar
securityLoginTelnetState = _SecurityLoginTelnetState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 8, 6),
    _SecurityLoginTelnetState_Type()
)
securityLoginTelnetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityLoginTelnetState.setStatus("current")


class _SecurityLoginSSHState_Type(Integer32):
    """Custom type securityLoginSSHState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SecurityLoginSSHState_Type.__name__ = "Integer32"
_SecurityLoginSSHState_Object = MibScalar
securityLoginSSHState = _SecurityLoginSSHState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 8, 7),
    _SecurityLoginSSHState_Type()
)
securityLoginSSHState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityLoginSSHState.setStatus("current")
_Acl_ObjectIdentity = ObjectIdentity
acl = _Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9)
)
_MacAclTable_Object = MibTable
macAclTable = _MacAclTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 1)
)
if mibBuilder.loadTexts:
    macAclTable.setStatus("current")
_MacAclEntry_Object = MibTableRow
macAclEntry = _MacAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 1, 1)
)
macAclEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "macAclIndex"),
)
if mibBuilder.loadTexts:
    macAclEntry.setStatus("current")


class _MacAclIndex_Type(Integer32):
    """Custom type macAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_MacAclIndex_Type.__name__ = "Integer32"
_MacAclIndex_Object = MibTableColumn
macAclIndex = _MacAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 1, 1, 1),
    _MacAclIndex_Type()
)
macAclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAclIndex.setStatus("current")
_DestinationMacAddress_Type = DisplayString
_DestinationMacAddress_Object = MibTableColumn
destinationMacAddress = _DestinationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 1, 1, 2),
    _DestinationMacAddress_Type()
)
destinationMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destinationMacAddress.setStatus("current")
_DestinationMacMask_Type = DisplayString
_DestinationMacMask_Object = MibTableColumn
destinationMacMask = _DestinationMacMask_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 1, 1, 3),
    _DestinationMacMask_Type()
)
destinationMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destinationMacMask.setStatus("current")
_SourceMacAddress_Type = DisplayString
_SourceMacAddress_Object = MibTableColumn
sourceMacAddress = _SourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 1, 1, 4),
    _SourceMacAddress_Type()
)
sourceMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceMacAddress.setStatus("current")
_SourceMacMask_Type = DisplayString
_SourceMacMask_Object = MibTableColumn
sourceMacMask = _SourceMacMask_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 1, 1, 5),
    _SourceMacMask_Type()
)
sourceMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceMacMask.setStatus("current")


class _MacAclEtherType_Type(Integer32):
    """Custom type macAclEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MacAclEtherType_Type.__name__ = "Integer32"
_MacAclEtherType_Object = MibTableColumn
macAclEtherType = _MacAclEtherType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 1, 1, 6),
    _MacAclEtherType_Type()
)
macAclEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAclEtherType.setStatus("current")


class _MacAclVlanID_Type(Integer32):
    """Custom type macAclVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MacAclVlanID_Type.__name__ = "Integer32"
_MacAclVlanID_Object = MibTableColumn
macAclVlanID = _MacAclVlanID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 1, 1, 7),
    _MacAclVlanID_Type()
)
macAclVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAclVlanID.setStatus("current")


class _MacAclPortList_Type(Bits):
    """Custom type macAclPortList based on Bits"""
    namedValues = NamedValues(
        *(("port1", 0),
          ("port2", 1),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11),
          ("port13", 12),
          ("port14", 13),
          ("port15", 14),
          ("port16", 15),
          ("port17", 16),
          ("port18", 17),
          ("port19", 18),
          ("port20", 19),
          ("port21", 20),
          ("port22", 21),
          ("port23", 22),
          ("port24", 23),
          ("port25", 24),
          ("port26", 25),
          ("port27", 26),
          ("port28", 27),
          ("port29", 28),
          ("port30", 29),
          ("port31", 30),
          ("port32", 31))
    )

_MacAclPortList_Type.__name__ = "Bits"
_MacAclPortList_Object = MibTableColumn
macAclPortList = _MacAclPortList_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 1, 1, 8),
    _MacAclPortList_Type()
)
macAclPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAclPortList.setStatus("current")


class _MacAclAction_Type(Integer32):
    """Custom type macAclAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("drop", 2))
    )


_MacAclAction_Type.__name__ = "Integer32"
_MacAclAction_Object = MibTableColumn
macAclAction = _MacAclAction_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 1, 1, 9),
    _MacAclAction_Type()
)
macAclAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAclAction.setStatus("current")


class _MacAclActiveStatus_Type(Integer32):
    """Custom type macAclActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_MacAclActiveStatus_Type.__name__ = "Integer32"
_MacAclActiveStatus_Object = MibTableColumn
macAclActiveStatus = _MacAclActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 1, 1, 10),
    _MacAclActiveStatus_Type()
)
macAclActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAclActiveStatus.setStatus("current")


class _MacAclRowStatus_Type(Integer32):
    """Custom type macAclRowStatus based on Integer32"""
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )


_MacAclRowStatus_Type.__name__ = "Integer32"
_MacAclRowStatus_Object = MibTableColumn
macAclRowStatus = _MacAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 1, 1, 99),
    _MacAclRowStatus_Type()
)
macAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAclRowStatus.setStatus("current")
_IpAclTable_Object = MibTable
ipAclTable = _IpAclTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 2)
)
if mibBuilder.loadTexts:
    ipAclTable.setStatus("current")
_IpAclEntry_Object = MibTableRow
ipAclEntry = _IpAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 2, 1)
)
ipAclEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "ipAclIndex"),
)
if mibBuilder.loadTexts:
    ipAclEntry.setStatus("current")


class _IpAclIndex_Type(Integer32):
    """Custom type ipAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_IpAclIndex_Type.__name__ = "Integer32"
_IpAclIndex_Object = MibTableColumn
ipAclIndex = _IpAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 2, 1, 1),
    _IpAclIndex_Type()
)
ipAclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAclIndex.setStatus("current")
_DestinationIpAddress_Type = IpAddress
_DestinationIpAddress_Object = MibTableColumn
destinationIpAddress = _DestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 2, 1, 2),
    _DestinationIpAddress_Type()
)
destinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destinationIpAddress.setStatus("current")
_DestinationIpMask_Type = IpAddress
_DestinationIpMask_Object = MibTableColumn
destinationIpMask = _DestinationIpMask_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 2, 1, 3),
    _DestinationIpMask_Type()
)
destinationIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destinationIpMask.setStatus("current")
_SourceIpAddress_Type = IpAddress
_SourceIpAddress_Object = MibTableColumn
sourceIpAddress = _SourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 2, 1, 4),
    _SourceIpAddress_Type()
)
sourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceIpAddress.setStatus("current")
_SourceIpMask_Type = IpAddress
_SourceIpMask_Object = MibTableColumn
sourceIpMask = _SourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 2, 1, 5),
    _SourceIpMask_Type()
)
sourceIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceIpMask.setStatus("current")


class _IpProtocol_Type(Integer32):
    """Custom type ipProtocol based on Integer32"""
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
          ("icmp", 2),
          ("tcp", 3),
          ("udp", 4))
    )


_IpProtocol_Type.__name__ = "Integer32"
_IpProtocol_Object = MibTableColumn
ipProtocol = _IpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 2, 1, 6),
    _IpProtocol_Type()
)
ipProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipProtocol.setStatus("current")


class _L4DestinationPort_Type(Integer32):
    """Custom type l4DestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_L4DestinationPort_Type.__name__ = "Integer32"
_L4DestinationPort_Object = MibTableColumn
l4DestinationPort = _L4DestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 2, 1, 7),
    _L4DestinationPort_Type()
)
l4DestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l4DestinationPort.setStatus("current")


class _L4SourcePort_Type(Integer32):
    """Custom type l4SourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_L4SourcePort_Type.__name__ = "Integer32"
_L4SourcePort_Object = MibTableColumn
l4SourcePort = _L4SourcePort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 2, 1, 8),
    _L4SourcePort_Type()
)
l4SourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l4SourcePort.setStatus("current")


class _IpAclPortList_Type(Bits):
    """Custom type ipAclPortList based on Bits"""
    namedValues = NamedValues(
        *(("port1", 0),
          ("port2", 1),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11),
          ("port13", 12),
          ("port14", 13),
          ("port15", 14),
          ("port16", 15),
          ("port17", 16),
          ("port18", 17),
          ("port19", 18),
          ("port20", 19),
          ("port21", 20),
          ("port22", 21),
          ("port23", 22),
          ("port24", 23),
          ("port25", 24),
          ("port26", 25),
          ("port27", 26),
          ("port28", 27),
          ("port29", 28),
          ("port30", 29),
          ("port31", 30),
          ("port32", 31))
    )

_IpAclPortList_Type.__name__ = "Bits"
_IpAclPortList_Object = MibTableColumn
ipAclPortList = _IpAclPortList_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 2, 1, 9),
    _IpAclPortList_Type()
)
ipAclPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAclPortList.setStatus("current")


class _IpAclAction_Type(Integer32):
    """Custom type ipAclAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("drop", 2))
    )


_IpAclAction_Type.__name__ = "Integer32"
_IpAclAction_Object = MibTableColumn
ipAclAction = _IpAclAction_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 2, 1, 10),
    _IpAclAction_Type()
)
ipAclAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAclAction.setStatus("current")


class _IpAclActiveStatus_Type(Integer32):
    """Custom type ipAclActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_IpAclActiveStatus_Type.__name__ = "Integer32"
_IpAclActiveStatus_Object = MibTableColumn
ipAclActiveStatus = _IpAclActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 2, 1, 11),
    _IpAclActiveStatus_Type()
)
ipAclActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAclActiveStatus.setStatus("current")


class _IpAclRowStatus_Type(Integer32):
    """Custom type ipAclRowStatus based on Integer32"""
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )


_IpAclRowStatus_Type.__name__ = "Integer32"
_IpAclRowStatus_Object = MibTableColumn
ipAclRowStatus = _IpAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 9, 2, 1, 99),
    _IpAclRowStatus_Type()
)
ipAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAclRowStatus.setStatus("current")
_IpSourceGuard_ObjectIdentity = ObjectIdentity
ipSourceGuard = _IpSourceGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 10)
)


class _IpSourceGuardEnablePorts_Type(Bits):
    """Custom type ipSourceGuardEnablePorts based on Bits"""
    namedValues = NamedValues(
        *(("port1", 0),
          ("port2", 1),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11),
          ("port13", 12),
          ("port14", 13),
          ("port15", 14),
          ("port16", 15),
          ("port17", 16),
          ("port18", 17),
          ("port19", 18),
          ("port20", 19),
          ("port21", 20),
          ("port22", 21),
          ("port23", 22),
          ("port24", 23),
          ("port25", 24),
          ("port26", 25),
          ("port27", 26),
          ("port28", 27),
          ("port29", 28),
          ("port30", 29),
          ("port31", 30),
          ("port32", 31))
    )

_IpSourceGuardEnablePorts_Type.__name__ = "Bits"
_IpSourceGuardEnablePorts_Object = MibScalar
ipSourceGuardEnablePorts = _IpSourceGuardEnablePorts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 10, 1),
    _IpSourceGuardEnablePorts_Type()
)
ipSourceGuardEnablePorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSourceGuardEnablePorts.setStatus("current")
_IpSourceGuardTable_Object = MibTable
ipSourceGuardTable = _IpSourceGuardTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 10, 2)
)
if mibBuilder.loadTexts:
    ipSourceGuardTable.setStatus("current")
_IpSourceGuardEntry_Object = MibTableRow
ipSourceGuardEntry = _IpSourceGuardEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 10, 2, 1)
)
ipSourceGuardEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "ipSourceGuardIndex"),
)
if mibBuilder.loadTexts:
    ipSourceGuardEntry.setStatus("current")


class _IpSourceGuardIndex_Type(Integer32):
    """Custom type ipSourceGuardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_IpSourceGuardIndex_Type.__name__ = "Integer32"
_IpSourceGuardIndex_Object = MibTableColumn
ipSourceGuardIndex = _IpSourceGuardIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 10, 2, 1, 1),
    _IpSourceGuardIndex_Type()
)
ipSourceGuardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSourceGuardIndex.setStatus("current")
_IpSourceGuardSourceIp_Type = IpAddress
_IpSourceGuardSourceIp_Object = MibTableColumn
ipSourceGuardSourceIp = _IpSourceGuardSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 10, 2, 1, 2),
    _IpSourceGuardSourceIp_Type()
)
ipSourceGuardSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSourceGuardSourceIp.setStatus("current")
_IpSourceGuardSourceMac_Type = DisplayString
_IpSourceGuardSourceMac_Object = MibTableColumn
ipSourceGuardSourceMac = _IpSourceGuardSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 10, 2, 1, 3),
    _IpSourceGuardSourceMac_Type()
)
ipSourceGuardSourceMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSourceGuardSourceMac.setStatus("current")


class _IpSourceGuardPort_Type(Integer32):
    """Custom type ipSourceGuardPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpSourceGuardPort_Type.__name__ = "Integer32"
_IpSourceGuardPort_Object = MibTableColumn
ipSourceGuardPort = _IpSourceGuardPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 10, 2, 1, 4),
    _IpSourceGuardPort_Type()
)
ipSourceGuardPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSourceGuardPort.setStatus("current")


class _IpSourceGuardRowStatus_Type(Integer32):
    """Custom type ipSourceGuardRowStatus based on Integer32"""
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )


_IpSourceGuardRowStatus_Type.__name__ = "Integer32"
_IpSourceGuardRowStatus_Object = MibTableColumn
ipSourceGuardRowStatus = _IpSourceGuardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 10, 2, 1, 5),
    _IpSourceGuardRowStatus_Type()
)
ipSourceGuardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipSourceGuardRowStatus.setStatus("current")
_DhcpSnooping_ObjectIdentity = ObjectIdentity
dhcpSnooping = _DhcpSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 11)
)


class _DhcpSnoopingState_Type(Integer32):
    """Custom type dhcpSnoopingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_DhcpSnoopingState_Type.__name__ = "Integer32"
_DhcpSnoopingState_Object = MibScalar
dhcpSnoopingState = _DhcpSnoopingState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 11, 1),
    _DhcpSnoopingState_Type()
)
dhcpSnoopingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingState.setStatus("current")


class _DhcpSnoopingPorts_Type(Bits):
    """Custom type dhcpSnoopingPorts based on Bits"""
    namedValues = NamedValues(
        *(("port1", 0),
          ("port2", 1),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11),
          ("port13", 12),
          ("port14", 13),
          ("port15", 14),
          ("port16", 15),
          ("port17", 16),
          ("port18", 17),
          ("port19", 18),
          ("port20", 19),
          ("port21", 20),
          ("port22", 21),
          ("port23", 22),
          ("port24", 23),
          ("port25", 24),
          ("port26", 25),
          ("port27", 26),
          ("port28", 27),
          ("port29", 28),
          ("port30", 29),
          ("port31", 30),
          ("port32", 31))
    )

_DhcpSnoopingPorts_Type.__name__ = "Bits"
_DhcpSnoopingPorts_Object = MibScalar
dhcpSnoopingPorts = _DhcpSnoopingPorts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 11, 2),
    _DhcpSnoopingPorts_Type()
)
dhcpSnoopingPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingPorts.setStatus("current")


class _DhcpSnoopingBindingPorts_Type(Bits):
    """Custom type dhcpSnoopingBindingPorts based on Bits"""
    namedValues = NamedValues(
        *(("port1", 0),
          ("port2", 1),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11),
          ("port13", 12),
          ("port14", 13),
          ("port15", 14),
          ("port16", 15),
          ("port17", 16),
          ("port18", 17),
          ("port19", 18),
          ("port20", 19),
          ("port21", 20),
          ("port22", 21),
          ("port23", 22),
          ("port24", 23),
          ("port25", 24),
          ("port26", 25),
          ("port27", 26),
          ("port28", 27),
          ("port29", 28),
          ("port30", 29),
          ("port31", 30),
          ("port32", 31))
    )

_DhcpSnoopingBindingPorts_Type.__name__ = "Bits"
_DhcpSnoopingBindingPorts_Object = MibScalar
dhcpSnoopingBindingPorts = _DhcpSnoopingBindingPorts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 11, 3),
    _DhcpSnoopingBindingPorts_Type()
)
dhcpSnoopingBindingPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingBindingPorts.setStatus("current")
_DhcpSnoopingTable_Object = MibTable
dhcpSnoopingTable = _DhcpSnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 11, 4)
)
if mibBuilder.loadTexts:
    dhcpSnoopingTable.setStatus("current")
_DhcpSnoopingEntry_Object = MibTableRow
dhcpSnoopingEntry = _DhcpSnoopingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 11, 4, 1)
)
dhcpSnoopingEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "dhcpSnoopingIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopingEntry.setStatus("current")


class _DhcpSnoopingIndex_Type(Integer32):
    """Custom type dhcpSnoopingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_DhcpSnoopingIndex_Type.__name__ = "Integer32"
_DhcpSnoopingIndex_Object = MibTableColumn
dhcpSnoopingIndex = _DhcpSnoopingIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 11, 4, 1, 1),
    _DhcpSnoopingIndex_Type()
)
dhcpSnoopingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingIndex.setStatus("current")
_DhcpSnoopingMac_Type = DisplayString
_DhcpSnoopingMac_Object = MibTableColumn
dhcpSnoopingMac = _DhcpSnoopingMac_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 11, 4, 1, 2),
    _DhcpSnoopingMac_Type()
)
dhcpSnoopingMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingMac.setStatus("current")
_DhcpSnoopingIp_Type = IpAddress
_DhcpSnoopingIp_Object = MibTableColumn
dhcpSnoopingIp = _DhcpSnoopingIp_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 11, 4, 1, 3),
    _DhcpSnoopingIp_Type()
)
dhcpSnoopingIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingIp.setStatus("current")


class _DhcpSnoopingLeaseTime_Type(Integer32):
    """Custom type dhcpSnoopingLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 864000),
    )


_DhcpSnoopingLeaseTime_Type.__name__ = "Integer32"
_DhcpSnoopingLeaseTime_Object = MibTableColumn
dhcpSnoopingLeaseTime = _DhcpSnoopingLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 11, 4, 1, 4),
    _DhcpSnoopingLeaseTime_Type()
)
dhcpSnoopingLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    dhcpSnoopingLeaseTime.setUnits("second")


class _DhcpSnoopingVlanId_Type(Integer32):
    """Custom type dhcpSnoopingVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpSnoopingVlanId_Type.__name__ = "Integer32"
_DhcpSnoopingVlanId_Object = MibTableColumn
dhcpSnoopingVlanId = _DhcpSnoopingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 11, 4, 1, 5),
    _DhcpSnoopingVlanId_Type()
)
dhcpSnoopingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingVlanId.setStatus("current")


class _DhcpSnoopingPort_Type(Integer32):
    """Custom type dhcpSnoopingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DhcpSnoopingPort_Type.__name__ = "Integer32"
_DhcpSnoopingPort_Object = MibTableColumn
dhcpSnoopingPort = _DhcpSnoopingPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 11, 4, 1, 6),
    _DhcpSnoopingPort_Type()
)
dhcpSnoopingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingPort.setStatus("current")
_ArpSpoofing_ObjectIdentity = ObjectIdentity
arpSpoofing = _ArpSpoofing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 12)
)
_ArpSpoofingTable_Object = MibTable
arpSpoofingTable = _ArpSpoofingTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 12, 1)
)
if mibBuilder.loadTexts:
    arpSpoofingTable.setStatus("current")
_ArpSpoofingEntry_Object = MibTableRow
arpSpoofingEntry = _ArpSpoofingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 12, 1, 1)
)
arpSpoofingEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "arpSpoofingIndex"),
)
if mibBuilder.loadTexts:
    arpSpoofingEntry.setStatus("current")


class _ArpSpoofingIndex_Type(Integer32):
    """Custom type arpSpoofingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ArpSpoofingIndex_Type.__name__ = "Integer32"
_ArpSpoofingIndex_Object = MibTableColumn
arpSpoofingIndex = _ArpSpoofingIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 12, 1, 1, 1),
    _ArpSpoofingIndex_Type()
)
arpSpoofingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpSpoofingIndex.setStatus("current")
_ArpSpoofingSourceMac_Type = DisplayString
_ArpSpoofingSourceMac_Object = MibTableColumn
arpSpoofingSourceMac = _ArpSpoofingSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 12, 1, 1, 2),
    _ArpSpoofingSourceMac_Type()
)
arpSpoofingSourceMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpSpoofingSourceMac.setStatus("current")
_ArpSpoofingSourceIp_Type = IpAddress
_ArpSpoofingSourceIp_Object = MibTableColumn
arpSpoofingSourceIp = _ArpSpoofingSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 12, 1, 1, 3),
    _ArpSpoofingSourceIp_Type()
)
arpSpoofingSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpSpoofingSourceIp.setStatus("current")


class _ArpSpoofingRowStatus_Type(Integer32):
    """Custom type arpSpoofingRowStatus based on Integer32"""
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )


_ArpSpoofingRowStatus_Type.__name__ = "Integer32"
_ArpSpoofingRowStatus_Object = MibTableColumn
arpSpoofingRowStatus = _ArpSpoofingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 5, 12, 1, 1, 4),
    _ArpSpoofingRowStatus_Type()
)
arpSpoofingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arpSpoofingRowStatus.setStatus("current")
_Qos_ObjectIdentity = ObjectIdentity
qos = _Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1)
)


class _QosMode_Type(Integer32):
    """Custom type qosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("disable", 2))
    )


_QosMode_Type.__name__ = "Integer32"
_QosMode_Object = MibScalar
qosMode = _QosMode_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 1),
    _QosMode_Type()
)
qosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMode.setStatus("current")
_QosPortSettingTable_Object = MibTable
qosPortSettingTable = _QosPortSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 2)
)
if mibBuilder.loadTexts:
    qosPortSettingTable.setStatus("current")
_QosPortSettingEntry_Object = MibTableRow
qosPortSettingEntry = _QosPortSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 2, 1)
)
qosPortSettingEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "qosPortIndex"),
)
if mibBuilder.loadTexts:
    qosPortSettingEntry.setStatus("current")


class _QosPortIndex_Type(Integer32):
    """Custom type qosPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QosPortIndex_Type.__name__ = "Integer32"
_QosPortIndex_Object = MibTableColumn
qosPortIndex = _QosPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 2, 1, 1),
    _QosPortIndex_Type()
)
qosPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPortIndex.setStatus("current")


class _QosPortCos_Type(Integer32):
    """Custom type qosPortCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosPortCos_Type.__name__ = "Integer32"
_QosPortCos_Object = MibTableColumn
qosPortCos = _QosPortCos_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 2, 1, 2),
    _QosPortCos_Type()
)
qosPortCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPortCos.setStatus("current")


class _QosPortRemarkCoS_Type(Integer32):
    """Custom type qosPortRemarkCoS based on Integer32"""
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


_QosPortRemarkCoS_Type.__name__ = "Integer32"
_QosPortRemarkCoS_Object = MibTableColumn
qosPortRemarkCoS = _QosPortRemarkCoS_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 2, 1, 3),
    _QosPortRemarkCoS_Type()
)
qosPortRemarkCoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPortRemarkCoS.setStatus("current")


class _QosPortRemarkDSCP_Type(Integer32):
    """Custom type qosPortRemarkDSCP based on Integer32"""
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


_QosPortRemarkDSCP_Type.__name__ = "Integer32"
_QosPortRemarkDSCP_Object = MibTableColumn
qosPortRemarkDSCP = _QosPortRemarkDSCP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 2, 1, 4),
    _QosPortRemarkDSCP_Type()
)
qosPortRemarkDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPortRemarkDSCP.setStatus("current")


class _QosPortRemarkIPPrecedence_Type(Integer32):
    """Custom type qosPortRemarkIPPrecedence based on Integer32"""
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


_QosPortRemarkIPPrecedence_Type.__name__ = "Integer32"
_QosPortRemarkIPPrecedence_Object = MibTableColumn
qosPortRemarkIPPrecedence = _QosPortRemarkIPPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 2, 1, 5),
    _QosPortRemarkIPPrecedence_Type()
)
qosPortRemarkIPPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPortRemarkIPPrecedence.setStatus("current")
_QueueSettingTable_Object = MibTable
queueSettingTable = _QueueSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 3)
)
if mibBuilder.loadTexts:
    queueSettingTable.setStatus("current")
_QueueSettingEntry_Object = MibTableRow
queueSettingEntry = _QueueSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 3, 1)
)
queueSettingEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "queueIndex"),
)
if mibBuilder.loadTexts:
    queueSettingEntry.setStatus("current")


class _QueueIndex_Type(Integer32):
    """Custom type queueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_QueueIndex_Type.__name__ = "Integer32"
_QueueIndex_Object = MibTableColumn
queueIndex = _QueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 3, 1, 1),
    _QueueIndex_Type()
)
queueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueIndex.setStatus("current")


class _QueueMethod_Type(Integer32):
    """Custom type queueMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strictPriority", 1),
          ("wrr", 2))
    )


_QueueMethod_Type.__name__ = "Integer32"
_QueueMethod_Object = MibTableColumn
queueMethod = _QueueMethod_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 3, 1, 2),
    _QueueMethod_Type()
)
queueMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueMethod.setStatus("current")
_QueueWeight_Type = Integer32
_QueueWeight_Object = MibTableColumn
queueWeight = _QueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 3, 1, 3),
    _QueueWeight_Type()
)
queueWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueWeight.setStatus("current")
_QueuePercentOfWRRBandwidth_Type = DisplayString
_QueuePercentOfWRRBandwidth_Object = MibTableColumn
queuePercentOfWRRBandwidth = _QueuePercentOfWRRBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 3, 1, 4),
    _QueuePercentOfWRRBandwidth_Type()
)
queuePercentOfWRRBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queuePercentOfWRRBandwidth.setStatus("current")
_CostoQueueMapTable_Object = MibTable
costoQueueMapTable = _CostoQueueMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 4)
)
if mibBuilder.loadTexts:
    costoQueueMapTable.setStatus("current")
_CostoQueueMapEntry_Object = MibTableRow
costoQueueMapEntry = _CostoQueueMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 4, 1)
)
costoQueueMapEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "cosIndex"),
)
if mibBuilder.loadTexts:
    costoQueueMapEntry.setStatus("current")


class _CosIndex_Type(Integer32):
    """Custom type cosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CosIndex_Type.__name__ = "Integer32"
_CosIndex_Object = MibTableColumn
cosIndex = _CosIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 4, 1, 1),
    _CosIndex_Type()
)
cosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cosIndex.setStatus("current")


class _CosQueue_Type(Integer32):
    """Custom type cosQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CosQueue_Type.__name__ = "Integer32"
_CosQueue_Object = MibTableColumn
cosQueue = _CosQueue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 4, 1, 2),
    _CosQueue_Type()
)
cosQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cosQueue.setStatus("current")
_QueuetoCosMapTable_Object = MibTable
queuetoCosMapTable = _QueuetoCosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 5)
)
if mibBuilder.loadTexts:
    queuetoCosMapTable.setStatus("current")
_QueuetoCosMapEntry_Object = MibTableRow
queuetoCosMapEntry = _QueuetoCosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 5, 1)
)
queuetoCosMapEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "queuetoCosIndex"),
)
if mibBuilder.loadTexts:
    queuetoCosMapEntry.setStatus("current")


class _QueuetoCosIndex_Type(Integer32):
    """Custom type queuetoCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_QueuetoCosIndex_Type.__name__ = "Integer32"
_QueuetoCosIndex_Object = MibTableColumn
queuetoCosIndex = _QueuetoCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 5, 1, 1),
    _QueuetoCosIndex_Type()
)
queuetoCosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queuetoCosIndex.setStatus("current")


class _QueueCos_Type(Integer32):
    """Custom type queueCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QueueCos_Type.__name__ = "Integer32"
_QueueCos_Object = MibTableColumn
queueCos = _QueueCos_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 5, 1, 2),
    _QueueCos_Type()
)
queueCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueCos.setStatus("current")
_DscptoQueueMapTable_Object = MibTable
dscptoQueueMapTable = _DscptoQueueMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 6)
)
if mibBuilder.loadTexts:
    dscptoQueueMapTable.setStatus("current")
_DscptoQueueMapEntry_Object = MibTableRow
dscptoQueueMapEntry = _DscptoQueueMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 6, 1)
)
dscptoQueueMapEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "dscpIndex"),
)
if mibBuilder.loadTexts:
    dscptoQueueMapEntry.setStatus("current")


class _DscpIndex_Type(Integer32):
    """Custom type dscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_DscpIndex_Type.__name__ = "Integer32"
_DscpIndex_Object = MibTableColumn
dscpIndex = _DscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 6, 1, 1),
    _DscpIndex_Type()
)
dscpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dscpIndex.setStatus("current")


class _DscpQueue_Type(Integer32):
    """Custom type dscpQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DscpQueue_Type.__name__ = "Integer32"
_DscpQueue_Object = MibTableColumn
dscpQueue = _DscpQueue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 6, 1, 2),
    _DscpQueue_Type()
)
dscpQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpQueue.setStatus("current")
_QueuetoDSCPMapTable_Object = MibTable
queuetoDSCPMapTable = _QueuetoDSCPMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 7)
)
if mibBuilder.loadTexts:
    queuetoDSCPMapTable.setStatus("current")
_QueuetoDSCPMapEntry_Object = MibTableRow
queuetoDSCPMapEntry = _QueuetoDSCPMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 7, 1)
)
queuetoDSCPMapEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "queuetoDSCPIndex"),
)
if mibBuilder.loadTexts:
    queuetoDSCPMapEntry.setStatus("current")


class _QueuetoDSCPIndex_Type(Integer32):
    """Custom type queuetoDSCPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_QueuetoDSCPIndex_Type.__name__ = "Integer32"
_QueuetoDSCPIndex_Object = MibTableColumn
queuetoDSCPIndex = _QueuetoDSCPIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 7, 1, 1),
    _QueuetoDSCPIndex_Type()
)
queuetoDSCPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queuetoDSCPIndex.setStatus("current")


class _QueuDscp_Type(Integer32):
    """Custom type queuDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_QueuDscp_Type.__name__ = "Integer32"
_QueuDscp_Object = MibTableColumn
queuDscp = _QueuDscp_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 7, 1, 2),
    _QueuDscp_Type()
)
queuDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queuDscp.setStatus("current")
_IpPrecedencetoQueueMapTable_Object = MibTable
ipPrecedencetoQueueMapTable = _IpPrecedencetoQueueMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 8)
)
if mibBuilder.loadTexts:
    ipPrecedencetoQueueMapTable.setStatus("current")
_IpPrecedencetoQueueMapEntry_Object = MibTableRow
ipPrecedencetoQueueMapEntry = _IpPrecedencetoQueueMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 8, 1)
)
ipPrecedencetoQueueMapEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "ipPrecedenceIndex"),
)
if mibBuilder.loadTexts:
    ipPrecedencetoQueueMapEntry.setStatus("current")


class _IpPrecedenceIndex_Type(Integer32):
    """Custom type ipPrecedenceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_IpPrecedenceIndex_Type.__name__ = "Integer32"
_IpPrecedenceIndex_Object = MibTableColumn
ipPrecedenceIndex = _IpPrecedenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 8, 1, 1),
    _IpPrecedenceIndex_Type()
)
ipPrecedenceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPrecedenceIndex.setStatus("current")


class _IpPrecedenceQueue_Type(Integer32):
    """Custom type ipPrecedenceQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IpPrecedenceQueue_Type.__name__ = "Integer32"
_IpPrecedenceQueue_Object = MibTableColumn
ipPrecedenceQueue = _IpPrecedenceQueue_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 8, 1, 2),
    _IpPrecedenceQueue_Type()
)
ipPrecedenceQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPrecedenceQueue.setStatus("current")
_QueueToipPrecedenceMapTable_Object = MibTable
queueToipPrecedenceMapTable = _QueueToipPrecedenceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 9)
)
if mibBuilder.loadTexts:
    queueToipPrecedenceMapTable.setStatus("current")
_QueueToipPrecedenceMapEntry_Object = MibTableRow
queueToipPrecedenceMapEntry = _QueueToipPrecedenceMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 9, 1)
)
queueToipPrecedenceMapEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "queueToipPrecedenceIndex"),
)
if mibBuilder.loadTexts:
    queueToipPrecedenceMapEntry.setStatus("current")


class _QueueToipPrecedenceIndex_Type(Integer32):
    """Custom type queueToipPrecedenceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_QueueToipPrecedenceIndex_Type.__name__ = "Integer32"
_QueueToipPrecedenceIndex_Object = MibTableColumn
queueToipPrecedenceIndex = _QueueToipPrecedenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 9, 1, 1),
    _QueueToipPrecedenceIndex_Type()
)
queueToipPrecedenceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueToipPrecedenceIndex.setStatus("current")


class _IpPrecedence_Type(Integer32):
    """Custom type ipPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IpPrecedence_Type.__name__ = "Integer32"
_IpPrecedence_Object = MibTableColumn
ipPrecedence = _IpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 1, 9, 1, 2),
    _IpPrecedence_Type()
)
ipPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPrecedence.setStatus("current")
_QosBasicMode_ObjectIdentity = ObjectIdentity
qosBasicMode = _QosBasicMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 2)
)


class _TrustMode_Type(Integer32):
    """Custom type trustMode based on Integer32"""
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
        *(("cos-8021p", 1),
          ("dscp", 2),
          ("cos8021p-dscp", 3),
          ("ip-precendence", 4),
          ("none", 5))
    )


_TrustMode_Type.__name__ = "Integer32"
_TrustMode_Object = MibScalar
trustMode = _TrustMode_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 2, 1),
    _TrustMode_Type()
)
trustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustMode.setStatus("current")
_QosBasicPortTable_Object = MibTable
qosBasicPortTable = _QosBasicPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 2, 2)
)
if mibBuilder.loadTexts:
    qosBasicPortTable.setStatus("current")
_QosBasicPortEntry_Object = MibTableRow
qosBasicPortEntry = _QosBasicPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 2, 2, 1)
)
qosBasicPortEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "qosBasicPortIndex"),
)
if mibBuilder.loadTexts:
    qosBasicPortEntry.setStatus("current")


class _QosBasicPortIndex_Type(Integer32):
    """Custom type qosBasicPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QosBasicPortIndex_Type.__name__ = "Integer32"
_QosBasicPortIndex_Object = MibTableColumn
qosBasicPortIndex = _QosBasicPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 2, 2, 1, 1),
    _QosBasicPortIndex_Type()
)
qosBasicPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosBasicPortIndex.setStatus("current")


class _QosBasicPortTrust_Type(Integer32):
    """Custom type qosBasicPortTrust based on Integer32"""
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


_QosBasicPortTrust_Type.__name__ = "Integer32"
_QosBasicPortTrust_Object = MibTableColumn
qosBasicPortTrust = _QosBasicPortTrust_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 2, 2, 1, 2),
    _QosBasicPortTrust_Type()
)
qosBasicPortTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosBasicPortTrust.setStatus("current")
_RateLimit_ObjectIdentity = ObjectIdentity
rateLimit = _RateLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3)
)
_IngressBandwidthControl_ObjectIdentity = ObjectIdentity
ingressBandwidthControl = _IngressBandwidthControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 1)
)
_IngressBandwidthTable_Object = MibTable
ingressBandwidthTable = _IngressBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ingressBandwidthTable.setStatus("current")
_IngressBandwidthEntry_Object = MibTableRow
ingressBandwidthEntry = _IngressBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 1, 1, 1)
)
ingressBandwidthEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "ingressBandwidthPortIndex"),
)
if mibBuilder.loadTexts:
    ingressBandwidthEntry.setStatus("current")


class _IngressBandwidthPortIndex_Type(Integer32):
    """Custom type ingressBandwidthPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IngressBandwidthPortIndex_Type.__name__ = "Integer32"
_IngressBandwidthPortIndex_Object = MibTableColumn
ingressBandwidthPortIndex = _IngressBandwidthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 1, 1, 1, 1),
    _IngressBandwidthPortIndex_Type()
)
ingressBandwidthPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressBandwidthPortIndex.setStatus("current")


class _IngressBandwidthState_Type(Integer32):
    """Custom type ingressBandwidthState based on Integer32"""
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


_IngressBandwidthState_Type.__name__ = "Integer32"
_IngressBandwidthState_Object = MibTableColumn
ingressBandwidthState = _IngressBandwidthState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 1, 1, 1, 2),
    _IngressBandwidthState_Type()
)
ingressBandwidthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressBandwidthState.setStatus("current")


class _IngressBandwidthRate_Type(Integer32):
    """Custom type ingressBandwidthRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1000000),
    )


_IngressBandwidthRate_Type.__name__ = "Integer32"
_IngressBandwidthRate_Object = MibTableColumn
ingressBandwidthRate = _IngressBandwidthRate_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 1, 1, 1, 3),
    _IngressBandwidthRate_Type()
)
ingressBandwidthRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressBandwidthRate.setStatus("current")
_EgressBandwidthControl_ObjectIdentity = ObjectIdentity
egressBandwidthControl = _EgressBandwidthControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 2)
)
_EgressBandwidthTable_Object = MibTable
egressBandwidthTable = _EgressBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    egressBandwidthTable.setStatus("current")
_EgressBandwidthEntry_Object = MibTableRow
egressBandwidthEntry = _EgressBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 2, 1, 1)
)
egressBandwidthEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "egressBandwidthPortIndex"),
)
if mibBuilder.loadTexts:
    egressBandwidthEntry.setStatus("current")


class _EgressBandwidthPortIndex_Type(Integer32):
    """Custom type egressBandwidthPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EgressBandwidthPortIndex_Type.__name__ = "Integer32"
_EgressBandwidthPortIndex_Object = MibTableColumn
egressBandwidthPortIndex = _EgressBandwidthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 2, 1, 1, 1),
    _EgressBandwidthPortIndex_Type()
)
egressBandwidthPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressBandwidthPortIndex.setStatus("current")


class _EgressBandwidthState_Type(Integer32):
    """Custom type egressBandwidthState based on Integer32"""
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


_EgressBandwidthState_Type.__name__ = "Integer32"
_EgressBandwidthState_Object = MibTableColumn
egressBandwidthState = _EgressBandwidthState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 2, 1, 1, 2),
    _EgressBandwidthState_Type()
)
egressBandwidthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressBandwidthState.setStatus("current")


class _EgressBandwidthRate_Type(Integer32):
    """Custom type egressBandwidthRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_EgressBandwidthRate_Type.__name__ = "Integer32"
_EgressBandwidthRate_Object = MibTableColumn
egressBandwidthRate = _EgressBandwidthRate_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 2, 1, 1, 3),
    _EgressBandwidthRate_Type()
)
egressBandwidthRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressBandwidthRate.setStatus("current")
_EgressQueueBandwidthControl_ObjectIdentity = ObjectIdentity
egressQueueBandwidthControl = _EgressQueueBandwidthControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 3)
)
_EgressqueueBandwidthTable_Object = MibTable
egressqueueBandwidthTable = _EgressqueueBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 3, 1)
)
if mibBuilder.loadTexts:
    egressqueueBandwidthTable.setStatus("current")
_EgressqueueBandwidthEntry_Object = MibTableRow
egressqueueBandwidthEntry = _EgressqueueBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 3, 1, 1)
)
egressqueueBandwidthEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "egressqueueBandwidthPortIndex"),
)
if mibBuilder.loadTexts:
    egressqueueBandwidthEntry.setStatus("current")


class _EgressqueueBandwidthPortIndex_Type(Integer32):
    """Custom type egressqueueBandwidthPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EgressqueueBandwidthPortIndex_Type.__name__ = "Integer32"
_EgressqueueBandwidthPortIndex_Object = MibTableColumn
egressqueueBandwidthPortIndex = _EgressqueueBandwidthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 3, 1, 1, 1),
    _EgressqueueBandwidthPortIndex_Type()
)
egressqueueBandwidthPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressqueueBandwidthPortIndex.setStatus("current")


class _EgressqueueBandwidthQueueIndex_Type(Integer32):
    """Custom type egressqueueBandwidthQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EgressqueueBandwidthQueueIndex_Type.__name__ = "Integer32"
_EgressqueueBandwidthQueueIndex_Object = MibTableColumn
egressqueueBandwidthQueueIndex = _EgressqueueBandwidthQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 3, 1, 1, 2),
    _EgressqueueBandwidthQueueIndex_Type()
)
egressqueueBandwidthQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressqueueBandwidthQueueIndex.setStatus("current")


class _EgressqueueBandwidthState_Type(Integer32):
    """Custom type egressqueueBandwidthState based on Integer32"""
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


_EgressqueueBandwidthState_Type.__name__ = "Integer32"
_EgressqueueBandwidthState_Object = MibTableColumn
egressqueueBandwidthState = _EgressqueueBandwidthState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 3, 1, 1, 3),
    _EgressqueueBandwidthState_Type()
)
egressqueueBandwidthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressqueueBandwidthState.setStatus("current")


class _EgressqueueBandwidthCir_Type(Integer32):
    """Custom type egressqueueBandwidthCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1000000),
    )


_EgressqueueBandwidthCir_Type.__name__ = "Integer32"
_EgressqueueBandwidthCir_Object = MibTableColumn
egressqueueBandwidthCir = _EgressqueueBandwidthCir_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 6, 3, 3, 1, 1, 4),
    _EgressqueueBandwidthCir_Type()
)
egressqueueBandwidthCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressqueueBandwidthCir.setStatus("current")
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7)
)
_Lldp_ObjectIdentity = ObjectIdentity
lldp = _Lldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1)
)


class _LldpEnabled_Type(Integer32):
    """Custom type lldpEnabled based on Integer32"""
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


_LldpEnabled_Type.__name__ = "Integer32"
_LldpEnabled_Object = MibScalar
lldpEnabled = _LldpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 1),
    _LldpEnabled_Type()
)
lldpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpEnabled.setStatus("current")


class _LldpPduDisableAction_Type(Integer32):
    """Custom type lldpPduDisableAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filtering", 1),
          ("bridging", 2),
          ("flooding", 3))
    )


_LldpPduDisableAction_Type.__name__ = "Integer32"
_LldpPduDisableAction_Object = MibScalar
lldpPduDisableAction = _LldpPduDisableAction_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 2),
    _LldpPduDisableAction_Type()
)
lldpPduDisableAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPduDisableAction.setStatus("current")


class _LldpTransmissionInterval_Type(Integer32):
    """Custom type lldpTransmissionInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 32767),
    )


_LldpTransmissionInterval_Type.__name__ = "Integer32"
_LldpTransmissionInterval_Object = MibScalar
lldpTransmissionInterval = _LldpTransmissionInterval_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 3),
    _LldpTransmissionInterval_Type()
)
lldpTransmissionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpTransmissionInterval.setStatus("current")


class _LldpHoldtimeMultiplier_Type(Integer32):
    """Custom type lldpHoldtimeMultiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_LldpHoldtimeMultiplier_Type.__name__ = "Integer32"
_LldpHoldtimeMultiplier_Object = MibScalar
lldpHoldtimeMultiplier = _LldpHoldtimeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 4),
    _LldpHoldtimeMultiplier_Type()
)
lldpHoldtimeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpHoldtimeMultiplier.setStatus("current")


class _LldpReinitializationDelay_Type(Integer32):
    """Custom type lldpReinitializationDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LldpReinitializationDelay_Type.__name__ = "Integer32"
_LldpReinitializationDelay_Object = MibScalar
lldpReinitializationDelay = _LldpReinitializationDelay_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 5),
    _LldpReinitializationDelay_Type()
)
lldpReinitializationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpReinitializationDelay.setStatus("current")


class _LldpTransmitDelay_Type(Integer32):
    """Custom type lldpTransmitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_LldpTransmitDelay_Type.__name__ = "Integer32"
_LldpTransmitDelay_Object = MibScalar
lldpTransmitDelay = _LldpTransmitDelay_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 6),
    _LldpTransmitDelay_Type()
)
lldpTransmitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpTransmitDelay.setStatus("current")
_LldpPortConfTable_Object = MibTable
lldpPortConfTable = _LldpPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 7)
)
if mibBuilder.loadTexts:
    lldpPortConfTable.setStatus("current")
_LldpPortConfEntry_Object = MibTableRow
lldpPortConfEntry = _LldpPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 7, 1)
)
lldpPortConfEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "lldpPortIndex"),
)
if mibBuilder.loadTexts:
    lldpPortConfEntry.setStatus("current")


class _LldpPortIndex_Type(Integer32):
    """Custom type lldpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LldpPortIndex_Type.__name__ = "Integer32"
_LldpPortIndex_Object = MibTableColumn
lldpPortIndex = _LldpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 7, 1, 1),
    _LldpPortIndex_Type()
)
lldpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpPortIndex.setStatus("current")


class _LldpPortState_Type(Integer32):
    """Custom type lldpPortState based on Integer32"""
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
        *(("disable", 1),
          ("rx-only", 2),
          ("tx-only", 3),
          ("rx-tx", 4))
    )


_LldpPortState_Type.__name__ = "Integer32"
_LldpPortState_Object = MibTableColumn
lldpPortState = _LldpPortState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 7, 1, 2),
    _LldpPortState_Type()
)
lldpPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortState.setStatus("current")


class _LldpPortOptionalTLVs_Type(Bits):
    """Custom type lldpPortOptionalTLVs based on Bits"""
    namedValues = NamedValues(
        *(("systemName", 0),
          ("portDescription", 1),
          ("systemDescription", 2),
          ("systemCapability", 3),
          ("ieee8023MAC-PHY", 4),
          ("ieee8023LinkAggeration", 5),
          ("ieee8023MaxFrameSize", 6),
          ("managementAddress", 7),
          ("ieee8021PVID", 8))
    )

_LldpPortOptionalTLVs_Type.__name__ = "Bits"
_LldpPortOptionalTLVs_Object = MibTableColumn
lldpPortOptionalTLVs = _LldpPortOptionalTLVs_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 7, 1, 3),
    _LldpPortOptionalTLVs_Type()
)
lldpPortOptionalTLVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortOptionalTLVs.setStatus("current")
_LldpPortVlans_Type = DisplayString
_LldpPortVlans_Object = MibTableColumn
lldpPortVlans = _LldpPortVlans_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 7, 1, 4),
    _LldpPortVlans_Type()
)
lldpPortVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortVlans.setStatus("current")
_LocalDevice_ObjectIdentity = ObjectIdentity
localDevice = _LocalDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8)
)
_LldpLocalDeviceChassisidsubtype_Type = DisplayString
_LldpLocalDeviceChassisidsubtype_Object = MibScalar
lldpLocalDeviceChassisidsubtype = _LldpLocalDeviceChassisidsubtype_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 1),
    _LldpLocalDeviceChassisidsubtype_Type()
)
lldpLocalDeviceChassisidsubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalDeviceChassisidsubtype.setStatus("current")
_LldpLocalDeviceChassisID_Type = DisplayString
_LldpLocalDeviceChassisID_Object = MibScalar
lldpLocalDeviceChassisID = _LldpLocalDeviceChassisID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 2),
    _LldpLocalDeviceChassisID_Type()
)
lldpLocalDeviceChassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalDeviceChassisID.setStatus("current")
_LldpLocalDeviceSystemName_Type = DisplayString
_LldpLocalDeviceSystemName_Object = MibScalar
lldpLocalDeviceSystemName = _LldpLocalDeviceSystemName_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 3),
    _LldpLocalDeviceSystemName_Type()
)
lldpLocalDeviceSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalDeviceSystemName.setStatus("current")
_LldpLocalDeviceSystemDescription_Type = DisplayString
_LldpLocalDeviceSystemDescription_Object = MibScalar
lldpLocalDeviceSystemDescription = _LldpLocalDeviceSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 4),
    _LldpLocalDeviceSystemDescription_Type()
)
lldpLocalDeviceSystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalDeviceSystemDescription.setStatus("current")
_LldpLocalDeviceCapabilitiesSupported_Type = DisplayString
_LldpLocalDeviceCapabilitiesSupported_Object = MibScalar
lldpLocalDeviceCapabilitiesSupported = _LldpLocalDeviceCapabilitiesSupported_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 5),
    _LldpLocalDeviceCapabilitiesSupported_Type()
)
lldpLocalDeviceCapabilitiesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalDeviceCapabilitiesSupported.setStatus("current")
_LldpLocalDeviceCapabilitiesEnabled_Type = DisplayString
_LldpLocalDeviceCapabilitiesEnabled_Object = MibScalar
lldpLocalDeviceCapabilitiesEnabled = _LldpLocalDeviceCapabilitiesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 6),
    _LldpLocalDeviceCapabilitiesEnabled_Type()
)
lldpLocalDeviceCapabilitiesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalDeviceCapabilitiesEnabled.setStatus("current")
_LldpLocalDevicePortIDsubtype_Type = DisplayString
_LldpLocalDevicePortIDsubtype_Object = MibScalar
lldpLocalDevicePortIDsubtype = _LldpLocalDevicePortIDsubtype_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 7),
    _LldpLocalDevicePortIDsubtype_Type()
)
lldpLocalDevicePortIDsubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalDevicePortIDsubtype.setStatus("current")
_LldpLocalPortStatusTable_Object = MibTable
lldpLocalPortStatusTable = _LldpLocalPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8)
)
if mibBuilder.loadTexts:
    lldpLocalPortStatusTable.setStatus("current")
_LldpLocalPortStatusEntry_Object = MibTableRow
lldpLocalPortStatusEntry = _LldpLocalPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1)
)
lldpLocalPortStatusEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "lldpLocalPortIndex"),
)
if mibBuilder.loadTexts:
    lldpLocalPortStatusEntry.setStatus("current")


class _LldpLocalPortIndex_Type(Integer32):
    """Custom type lldpLocalPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LldpLocalPortIndex_Type.__name__ = "Integer32"
_LldpLocalPortIndex_Object = MibTableColumn
lldpLocalPortIndex = _LldpLocalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 1),
    _LldpLocalPortIndex_Type()
)
lldpLocalPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortIndex.setStatus("current")


class _LldpLocalPortStatus_Type(Integer32):
    """Custom type lldpLocalPortStatus based on Integer32"""
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
        *(("disable", 1),
          ("rx-only", 2),
          ("tx-only", 3),
          ("rx-tx", 4))
    )


_LldpLocalPortStatus_Type.__name__ = "Integer32"
_LldpLocalPortStatus_Object = MibTableColumn
lldpLocalPortStatus = _LldpLocalPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 2),
    _LldpLocalPortStatus_Type()
)
lldpLocalPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortStatus.setStatus("current")
_LldpLocalPortChassisIDsubtype_Type = DisplayString
_LldpLocalPortChassisIDsubtype_Object = MibTableColumn
lldpLocalPortChassisIDsubtype = _LldpLocalPortChassisIDsubtype_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 3),
    _LldpLocalPortChassisIDsubtype_Type()
)
lldpLocalPortChassisIDsubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortChassisIDsubtype.setStatus("current")
_LldpLocalPortChassisID_Type = DisplayString
_LldpLocalPortChassisID_Object = MibTableColumn
lldpLocalPortChassisID = _LldpLocalPortChassisID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 4),
    _LldpLocalPortChassisID_Type()
)
lldpLocalPortChassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortChassisID.setStatus("current")
_LldpLocalPortSystemname_Type = DisplayString
_LldpLocalPortSystemname_Object = MibTableColumn
lldpLocalPortSystemname = _LldpLocalPortSystemname_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 5),
    _LldpLocalPortSystemname_Type()
)
lldpLocalPortSystemname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortSystemname.setStatus("current")
_LldpLocalPortSystemdescription_Type = DisplayString
_LldpLocalPortSystemdescription_Object = MibTableColumn
lldpLocalPortSystemdescription = _LldpLocalPortSystemdescription_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 6),
    _LldpLocalPortSystemdescription_Type()
)
lldpLocalPortSystemdescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortSystemdescription.setStatus("current")
_LldpLocalPortSupportedsystemcapabilities_Type = DisplayString
_LldpLocalPortSupportedsystemcapabilities_Object = MibTableColumn
lldpLocalPortSupportedsystemcapabilities = _LldpLocalPortSupportedsystemcapabilities_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 7),
    _LldpLocalPortSupportedsystemcapabilities_Type()
)
lldpLocalPortSupportedsystemcapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortSupportedsystemcapabilities.setStatus("current")
_LldpLocalPortEnablesystemcapabilities_Type = DisplayString
_LldpLocalPortEnablesystemcapabilities_Object = MibTableColumn
lldpLocalPortEnablesystemcapabilities = _LldpLocalPortEnablesystemcapabilities_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 8),
    _LldpLocalPortEnablesystemcapabilities_Type()
)
lldpLocalPortEnablesystemcapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortEnablesystemcapabilities.setStatus("current")
_LldpLocalPortIDsubtype_Type = DisplayString
_LldpLocalPortIDsubtype_Object = MibTableColumn
lldpLocalPortIDsubtype = _LldpLocalPortIDsubtype_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 9),
    _LldpLocalPortIDsubtype_Type()
)
lldpLocalPortIDsubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortIDsubtype.setStatus("current")
_LldpLocalPortID_Type = DisplayString
_LldpLocalPortID_Object = MibTableColumn
lldpLocalPortID = _LldpLocalPortID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 10),
    _LldpLocalPortID_Type()
)
lldpLocalPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortID.setStatus("current")
_LldpLocalPortDescription_Type = DisplayString
_LldpLocalPortDescription_Object = MibTableColumn
lldpLocalPortDescription = _LldpLocalPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 11),
    _LldpLocalPortDescription_Type()
)
lldpLocalPortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortDescription.setStatus("current")
_LldpLocalPortManagementAddress_Type = DisplayString
_LldpLocalPortManagementAddress_Object = MibTableColumn
lldpLocalPortManagementAddress = _LldpLocalPortManagementAddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 12),
    _LldpLocalPortManagementAddress_Type()
)
lldpLocalPortManagementAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortManagementAddress.setStatus("current")
_LldpLocalPortAuto_negosupported_Type = DisplayString
_LldpLocalPortAuto_negosupported_Object = MibTableColumn
lldpLocalPortAuto_negosupported = _LldpLocalPortAuto_negosupported_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 13),
    _LldpLocalPortAuto_negosupported_Type()
)
lldpLocalPortAuto_negosupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortAuto_negosupported.setStatus("current")
_LldpLocalPortAuto_negoenabled_Type = DisplayString
_LldpLocalPortAuto_negoenabled_Object = MibTableColumn
lldpLocalPortAuto_negoenabled = _LldpLocalPortAuto_negoenabled_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 14),
    _LldpLocalPortAuto_negoenabled_Type()
)
lldpLocalPortAuto_negoenabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortAuto_negoenabled.setStatus("current")
_LldpLocalPortAuto_negoAdvertisedCapabilities_Type = DisplayString
_LldpLocalPortAuto_negoAdvertisedCapabilities_Object = MibTableColumn
lldpLocalPortAuto_negoAdvertisedCapabilities = _LldpLocalPortAuto_negoAdvertisedCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 15),
    _LldpLocalPortAuto_negoAdvertisedCapabilities_Type()
)
lldpLocalPortAuto_negoAdvertisedCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortAuto_negoAdvertisedCapabilities.setStatus("current")
_LldpLocalPortOperationMAUtype_Type = DisplayString
_LldpLocalPortOperationMAUtype_Object = MibTableColumn
lldpLocalPortOperationMAUtype = _LldpLocalPortOperationMAUtype_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 16),
    _LldpLocalPortOperationMAUtype_Type()
)
lldpLocalPortOperationMAUtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortOperationMAUtype.setStatus("current")
_LldpLocalPortIeee8023MaxFrameSize_Type = DisplayString
_LldpLocalPortIeee8023MaxFrameSize_Object = MibTableColumn
lldpLocalPortIeee8023MaxFrameSize = _LldpLocalPortIeee8023MaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 17),
    _LldpLocalPortIeee8023MaxFrameSize_Type()
)
lldpLocalPortIeee8023MaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortIeee8023MaxFrameSize.setStatus("current")
_LldpLocalPortAggregationCapability_Type = DisplayString
_LldpLocalPortAggregationCapability_Object = MibTableColumn
lldpLocalPortAggregationCapability = _LldpLocalPortAggregationCapability_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 18),
    _LldpLocalPortAggregationCapability_Type()
)
lldpLocalPortAggregationCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortAggregationCapability.setStatus("current")
_LldpLocalPortAggregationStatus_Type = DisplayString
_LldpLocalPortAggregationStatus_Object = MibTableColumn
lldpLocalPortAggregationStatus = _LldpLocalPortAggregationStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 19),
    _LldpLocalPortAggregationStatus_Type()
)
lldpLocalPortAggregationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortAggregationStatus.setStatus("current")
_LldpLocalPortAggregationPortID_Type = DisplayString
_LldpLocalPortAggregationPortID_Object = MibTableColumn
lldpLocalPortAggregationPortID = _LldpLocalPortAggregationPortID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 20),
    _LldpLocalPortAggregationPortID_Type()
)
lldpLocalPortAggregationPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortAggregationPortID.setStatus("current")
_LldpLocalPortPvid_Type = DisplayString
_LldpLocalPortPvid_Object = MibTableColumn
lldpLocalPortPvid = _LldpLocalPortPvid_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 21),
    _LldpLocalPortPvid_Type()
)
lldpLocalPortPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortPvid.setStatus("current")
_LldpLocalPortVlanName_Type = DisplayString
_LldpLocalPortVlanName_Object = MibTableColumn
lldpLocalPortVlanName = _LldpLocalPortVlanName_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 8, 8, 1, 22),
    _LldpLocalPortVlanName_Type()
)
lldpLocalPortVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortVlanName.setStatus("current")
_RemoteDevice_ObjectIdentity = ObjectIdentity
remoteDevice = _RemoteDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9)
)
_LldpremoteDeviceTable_Object = MibTable
lldpremoteDeviceTable = _LldpremoteDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1)
)
if mibBuilder.loadTexts:
    lldpremoteDeviceTable.setStatus("current")
_LldpremoteDeviceEntry_Object = MibTableRow
lldpremoteDeviceEntry = _LldpremoteDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1)
)
lldpremoteDeviceEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "lldpremoteDeviceIndex"),
)
if mibBuilder.loadTexts:
    lldpremoteDeviceEntry.setStatus("current")


class _LldpremoteDeviceIndex_Type(Integer32):
    """Custom type lldpremoteDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LldpremoteDeviceIndex_Type.__name__ = "Integer32"
_LldpremoteDeviceIndex_Object = MibTableColumn
lldpremoteDeviceIndex = _LldpremoteDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 1),
    _LldpremoteDeviceIndex_Type()
)
lldpremoteDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceIndex.setStatus("current")
_LldpremoteDeviceLocalPort_Type = DisplayString
_LldpremoteDeviceLocalPort_Object = MibTableColumn
lldpremoteDeviceLocalPort = _LldpremoteDeviceLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 2),
    _LldpremoteDeviceLocalPort_Type()
)
lldpremoteDeviceLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceLocalPort.setStatus("current")
_LldpremoteDeviceChassisIDsubtype_Type = DisplayString
_LldpremoteDeviceChassisIDsubtype_Object = MibTableColumn
lldpremoteDeviceChassisIDsubtype = _LldpremoteDeviceChassisIDsubtype_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 3),
    _LldpremoteDeviceChassisIDsubtype_Type()
)
lldpremoteDeviceChassisIDsubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceChassisIDsubtype.setStatus("current")
_LldpremoteDeviceChassisID_Type = DisplayString
_LldpremoteDeviceChassisID_Object = MibTableColumn
lldpremoteDeviceChassisID = _LldpremoteDeviceChassisID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 4),
    _LldpremoteDeviceChassisID_Type()
)
lldpremoteDeviceChassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceChassisID.setStatus("current")
_LldpremoteDevicePortIDsubtype_Type = DisplayString
_LldpremoteDevicePortIDsubtype_Object = MibTableColumn
lldpremoteDevicePortIDsubtype = _LldpremoteDevicePortIDsubtype_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 5),
    _LldpremoteDevicePortIDsubtype_Type()
)
lldpremoteDevicePortIDsubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDevicePortIDsubtype.setStatus("current")
_LldpremoteDevicePortID_Type = DisplayString
_LldpremoteDevicePortID_Object = MibTableColumn
lldpremoteDevicePortID = _LldpremoteDevicePortID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 6),
    _LldpremoteDevicePortID_Type()
)
lldpremoteDevicePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDevicePortID.setStatus("current")
_LldpremoteDeviceSystemName_Type = DisplayString
_LldpremoteDeviceSystemName_Object = MibTableColumn
lldpremoteDeviceSystemName = _LldpremoteDeviceSystemName_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 7),
    _LldpremoteDeviceSystemName_Type()
)
lldpremoteDeviceSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceSystemName.setStatus("current")
_LldpremoteDeviceTimetolive_Type = DisplayString
_LldpremoteDeviceTimetolive_Object = MibTableColumn
lldpremoteDeviceTimetolive = _LldpremoteDeviceTimetolive_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 8),
    _LldpremoteDeviceTimetolive_Type()
)
lldpremoteDeviceTimetolive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceTimetolive.setStatus("current")
_LldpremoteDeviceEntryIndex_Type = DisplayString
_LldpremoteDeviceEntryIndex_Object = MibTableColumn
lldpremoteDeviceEntryIndex = _LldpremoteDeviceEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 9),
    _LldpremoteDeviceEntryIndex_Type()
)
lldpremoteDeviceEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceEntryIndex.setStatus("current")
_LldpremoteDevicePortDescription_Type = DisplayString
_LldpremoteDevicePortDescription_Object = MibTableColumn
lldpremoteDevicePortDescription = _LldpremoteDevicePortDescription_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 10),
    _LldpremoteDevicePortDescription_Type()
)
lldpremoteDevicePortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDevicePortDescription.setStatus("current")
_LldpremoteDeviceSystemdescription_Type = DisplayString
_LldpremoteDeviceSystemdescription_Object = MibTableColumn
lldpremoteDeviceSystemdescription = _LldpremoteDeviceSystemdescription_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 11),
    _LldpremoteDeviceSystemdescription_Type()
)
lldpremoteDeviceSystemdescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceSystemdescription.setStatus("current")
_LldpremoteDeviceSupportedsystemcapabilities_Type = DisplayString
_LldpremoteDeviceSupportedsystemcapabilities_Object = MibTableColumn
lldpremoteDeviceSupportedsystemcapabilities = _LldpremoteDeviceSupportedsystemcapabilities_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 12),
    _LldpremoteDeviceSupportedsystemcapabilities_Type()
)
lldpremoteDeviceSupportedsystemcapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceSupportedsystemcapabilities.setStatus("current")
_LldpremoteDeviceEnablesystemcapabilities_Type = DisplayString
_LldpremoteDeviceEnablesystemcapabilities_Object = MibTableColumn
lldpremoteDeviceEnablesystemcapabilities = _LldpremoteDeviceEnablesystemcapabilities_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 13),
    _LldpremoteDeviceEnablesystemcapabilities_Type()
)
lldpremoteDeviceEnablesystemcapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceEnablesystemcapabilities.setStatus("current")
_LldpremoteDeviceManagementAddress_Type = DisplayString
_LldpremoteDeviceManagementAddress_Object = MibTableColumn
lldpremoteDeviceManagementAddress = _LldpremoteDeviceManagementAddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 14),
    _LldpremoteDeviceManagementAddress_Type()
)
lldpremoteDeviceManagementAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceManagementAddress.setStatus("current")
_LldpremoteDeviceAuto_negosupported_Type = DisplayString
_LldpremoteDeviceAuto_negosupported_Object = MibTableColumn
lldpremoteDeviceAuto_negosupported = _LldpremoteDeviceAuto_negosupported_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 15),
    _LldpremoteDeviceAuto_negosupported_Type()
)
lldpremoteDeviceAuto_negosupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceAuto_negosupported.setStatus("current")
_LldpremoteDeviceAuto_negoenabled_Type = DisplayString
_LldpremoteDeviceAuto_negoenabled_Object = MibTableColumn
lldpremoteDeviceAuto_negoenabled = _LldpremoteDeviceAuto_negoenabled_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 16),
    _LldpremoteDeviceAuto_negoenabled_Type()
)
lldpremoteDeviceAuto_negoenabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceAuto_negoenabled.setStatus("current")
_LldpremoteDeviceAuto_negoAdvertisedCapabilities_Type = DisplayString
_LldpremoteDeviceAuto_negoAdvertisedCapabilities_Object = MibTableColumn
lldpremoteDeviceAuto_negoAdvertisedCapabilities = _LldpremoteDeviceAuto_negoAdvertisedCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 17),
    _LldpremoteDeviceAuto_negoAdvertisedCapabilities_Type()
)
lldpremoteDeviceAuto_negoAdvertisedCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceAuto_negoAdvertisedCapabilities.setStatus("current")
_LldpremoteDeviceOperationMAUtype_Type = DisplayString
_LldpremoteDeviceOperationMAUtype_Object = MibTableColumn
lldpremoteDeviceOperationMAUtype = _LldpremoteDeviceOperationMAUtype_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 18),
    _LldpremoteDeviceOperationMAUtype_Type()
)
lldpremoteDeviceOperationMAUtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceOperationMAUtype.setStatus("current")
_LldpremoteDeviceMdipowersupportportclass_Type = DisplayString
_LldpremoteDeviceMdipowersupportportclass_Object = MibTableColumn
lldpremoteDeviceMdipowersupportportclass = _LldpremoteDeviceMdipowersupportportclass_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 19),
    _LldpremoteDeviceMdipowersupportportclass_Type()
)
lldpremoteDeviceMdipowersupportportclass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceMdipowersupportportclass.setStatus("current")
_LldpremoteDevicePsemdipowersupport_Type = DisplayString
_LldpremoteDevicePsemdipowersupport_Object = MibTableColumn
lldpremoteDevicePsemdipowersupport = _LldpremoteDevicePsemdipowersupport_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 20),
    _LldpremoteDevicePsemdipowersupport_Type()
)
lldpremoteDevicePsemdipowersupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDevicePsemdipowersupport.setStatus("current")
_LldpremoteDevicePsemdipowerstatus_Type = DisplayString
_LldpremoteDevicePsemdipowerstatus_Object = MibTableColumn
lldpremoteDevicePsemdipowerstatus = _LldpremoteDevicePsemdipowerstatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 21),
    _LldpremoteDevicePsemdipowerstatus_Type()
)
lldpremoteDevicePsemdipowerstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDevicePsemdipowerstatus.setStatus("current")
_LldpremoteDevicePsepowerpaircontrolability_Type = DisplayString
_LldpremoteDevicePsepowerpaircontrolability_Object = MibTableColumn
lldpremoteDevicePsepowerpaircontrolability = _LldpremoteDevicePsepowerpaircontrolability_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 22),
    _LldpremoteDevicePsepowerpaircontrolability_Type()
)
lldpremoteDevicePsepowerpaircontrolability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDevicePsepowerpaircontrolability.setStatus("current")
_LldpremoteDevicePsepowerpair_Type = DisplayString
_LldpremoteDevicePsepowerpair_Object = MibTableColumn
lldpremoteDevicePsepowerpair = _LldpremoteDevicePsepowerpair_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 23),
    _LldpremoteDevicePsepowerpair_Type()
)
lldpremoteDevicePsepowerpair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDevicePsepowerpair.setStatus("current")
_LldpremoteDevicePsepowerclass_Type = DisplayString
_LldpremoteDevicePsepowerclass_Object = MibTableColumn
lldpremoteDevicePsepowerclass = _LldpremoteDevicePsepowerclass_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 24),
    _LldpremoteDevicePsepowerclass_Type()
)
lldpremoteDevicePsepowerclass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDevicePsepowerclass.setStatus("current")
_LldpremoteDeviceIeee8023MaxFrameSize_Type = DisplayString
_LldpremoteDeviceIeee8023MaxFrameSize_Object = MibTableColumn
lldpremoteDeviceIeee8023MaxFrameSize = _LldpremoteDeviceIeee8023MaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 25),
    _LldpremoteDeviceIeee8023MaxFrameSize_Type()
)
lldpremoteDeviceIeee8023MaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceIeee8023MaxFrameSize.setStatus("current")
_LldpremoteDeviceAggregationCapability_Type = DisplayString
_LldpremoteDeviceAggregationCapability_Object = MibTableColumn
lldpremoteDeviceAggregationCapability = _LldpremoteDeviceAggregationCapability_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 26),
    _LldpremoteDeviceAggregationCapability_Type()
)
lldpremoteDeviceAggregationCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceAggregationCapability.setStatus("current")
_LldpremoteDeviceAggregationStatus_Type = DisplayString
_LldpremoteDeviceAggregationStatus_Object = MibTableColumn
lldpremoteDeviceAggregationStatus = _LldpremoteDeviceAggregationStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 27),
    _LldpremoteDeviceAggregationStatus_Type()
)
lldpremoteDeviceAggregationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceAggregationStatus.setStatus("current")
_LldpremoteDeviceAggregationPortID_Type = DisplayString
_LldpremoteDeviceAggregationPortID_Object = MibTableColumn
lldpremoteDeviceAggregationPortID = _LldpremoteDeviceAggregationPortID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 28),
    _LldpremoteDeviceAggregationPortID_Type()
)
lldpremoteDeviceAggregationPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceAggregationPortID.setStatus("current")
_LldpremoteDevicePvid_Type = DisplayString
_LldpremoteDevicePvid_Object = MibTableColumn
lldpremoteDevicePvid = _LldpremoteDevicePvid_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 29),
    _LldpremoteDevicePvid_Type()
)
lldpremoteDevicePvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDevicePvid.setStatus("current")
_LldpremoteDeviceVlanName_Type = DisplayString
_LldpremoteDeviceVlanName_Object = MibTableColumn
lldpremoteDeviceVlanName = _LldpremoteDeviceVlanName_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 30),
    _LldpremoteDeviceVlanName_Type()
)
lldpremoteDeviceVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpremoteDeviceVlanName.setStatus("current")


class _LldpremoteDeviceRowStatus_Type(Integer32):
    """Custom type lldpremoteDeviceRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("desroty", 6))
    )


_LldpremoteDeviceRowStatus_Type.__name__ = "Integer32"
_LldpremoteDeviceRowStatus_Object = MibTableColumn
lldpremoteDeviceRowStatus = _LldpremoteDeviceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 9, 1, 1, 31),
    _LldpremoteDeviceRowStatus_Type()
)
lldpremoteDeviceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpremoteDeviceRowStatus.setStatus("current")
_LldpOverloadingTable_Object = MibTable
lldpOverloadingTable = _LldpOverloadingTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 10)
)
if mibBuilder.loadTexts:
    lldpOverloadingTable.setStatus("current")
_LldpOverloadingEntry_Object = MibTableRow
lldpOverloadingEntry = _LldpOverloadingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 10, 1)
)
lldpOverloadingEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "lldpOverloadingPortIndex"),
)
if mibBuilder.loadTexts:
    lldpOverloadingEntry.setStatus("current")


class _LldpOverloadingPortIndex_Type(Integer32):
    """Custom type lldpOverloadingPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LldpOverloadingPortIndex_Type.__name__ = "Integer32"
_LldpOverloadingPortIndex_Object = MibTableColumn
lldpOverloadingPortIndex = _LldpOverloadingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 10, 1, 1),
    _LldpOverloadingPortIndex_Type()
)
lldpOverloadingPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpOverloadingPortIndex.setStatus("current")
_LldpOverloadingTotal_Type = Integer32
_LldpOverloadingTotal_Object = MibTableColumn
lldpOverloadingTotal = _LldpOverloadingTotal_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 10, 1, 2),
    _LldpOverloadingTotal_Type()
)
lldpOverloadingTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpOverloadingTotal.setStatus("current")
_LldpOverloadingLeftToSend_Type = Integer32
_LldpOverloadingLeftToSend_Object = MibTableColumn
lldpOverloadingLeftToSend = _LldpOverloadingLeftToSend_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 10, 1, 3),
    _LldpOverloadingLeftToSend_Type()
)
lldpOverloadingLeftToSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpOverloadingLeftToSend.setStatus("current")
_LldpOverloadingStatus_Type = DisplayString
_LldpOverloadingStatus_Object = MibTableColumn
lldpOverloadingStatus = _LldpOverloadingStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 10, 1, 4),
    _LldpOverloadingStatus_Type()
)
lldpOverloadingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpOverloadingStatus.setStatus("current")
_LldpOverloadingMandatoryTLVs_Type = DisplayString
_LldpOverloadingMandatoryTLVs_Object = MibTableColumn
lldpOverloadingMandatoryTLVs = _LldpOverloadingMandatoryTLVs_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 10, 1, 5),
    _LldpOverloadingMandatoryTLVs_Type()
)
lldpOverloadingMandatoryTLVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpOverloadingMandatoryTLVs.setStatus("current")
_LldpOverloadingIeee8023TLVs_Type = DisplayString
_LldpOverloadingIeee8023TLVs_Object = MibTableColumn
lldpOverloadingIeee8023TLVs = _LldpOverloadingIeee8023TLVs_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 10, 1, 6),
    _LldpOverloadingIeee8023TLVs_Type()
)
lldpOverloadingIeee8023TLVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpOverloadingIeee8023TLVs.setStatus("current")
_LldpOverloadingOptionalTLVs_Type = DisplayString
_LldpOverloadingOptionalTLVs_Object = MibTableColumn
lldpOverloadingOptionalTLVs = _LldpOverloadingOptionalTLVs_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 10, 1, 7),
    _LldpOverloadingOptionalTLVs_Type()
)
lldpOverloadingOptionalTLVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpOverloadingOptionalTLVs.setStatus("current")
_LldpOverloadingIeee8021TLVs_Type = DisplayString
_LldpOverloadingIeee8021TLVs_Object = MibTableColumn
lldpOverloadingIeee8021TLVs = _LldpOverloadingIeee8021TLVs_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 1, 10, 1, 8),
    _LldpOverloadingIeee8021TLVs_Type()
)
lldpOverloadingIeee8021TLVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpOverloadingIeee8021TLVs.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2)
)


class _SnmpState_Type(Integer32):
    """Custom type snmpState based on Integer32"""
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


_SnmpState_Type.__name__ = "Integer32"
_SnmpState_Object = MibScalar
snmpState = _SnmpState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 1),
    _SnmpState_Type()
)
snmpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpState.setStatus("current")
_SnmpCommunityTable_Object = MibTable
snmpCommunityTable = _SnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 2)
)
if mibBuilder.loadTexts:
    snmpCommunityTable.setStatus("current")
_SnmpCommunityEntry_Object = MibTableRow
snmpCommunityEntry = _SnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 2, 1)
)
snmpCommunityEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "snmpCommunityIndex"),
)
if mibBuilder.loadTexts:
    snmpCommunityEntry.setStatus("current")


class _SnmpCommunityIndex_Type(Integer32):
    """Custom type snmpCommunityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SnmpCommunityIndex_Type.__name__ = "Integer32"
_SnmpCommunityIndex_Object = MibTableColumn
snmpCommunityIndex = _SnmpCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 2, 1, 1),
    _SnmpCommunityIndex_Type()
)
snmpCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCommunityIndex.setStatus("current")
_SnmpCommunityString_Type = DisplayString
_SnmpCommunityString_Object = MibTableColumn
snmpCommunityString = _SnmpCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 2, 1, 2),
    _SnmpCommunityString_Type()
)
snmpCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityString.setStatus("current")


class _SnmpCommunityAccessRight_Type(Integer32):
    """Custom type snmpCommunityAccessRight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ro", 1),
          ("rw", 2))
    )


_SnmpCommunityAccessRight_Type.__name__ = "Integer32"
_SnmpCommunityAccessRight_Object = MibTableColumn
snmpCommunityAccessRight = _SnmpCommunityAccessRight_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 2, 1, 3),
    _SnmpCommunityAccessRight_Type()
)
snmpCommunityAccessRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityAccessRight.setStatus("current")


class _SnmpCommunityRowStatus_Type(Integer32):
    """Custom type snmpCommunityRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("createAndWait", 5),
          ("destory", 6))
    )


_SnmpCommunityRowStatus_Type.__name__ = "Integer32"
_SnmpCommunityRowStatus_Object = MibTableColumn
snmpCommunityRowStatus = _SnmpCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 2, 1, 99),
    _SnmpCommunityRowStatus_Type()
)
snmpCommunityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityRowStatus.setStatus("current")
_SnmpTrapHostTable_Object = MibTable
snmpTrapHostTable = _SnmpTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 3)
)
if mibBuilder.loadTexts:
    snmpTrapHostTable.setStatus("current")
_SnmpTrapHostEntry_Object = MibTableRow
snmpTrapHostEntry = _SnmpTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 3, 1)
)
snmpTrapHostEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "snmpTrapHostIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapHostEntry.setStatus("current")


class _SnmpTrapHostIndex_Type(Integer32):
    """Custom type snmpTrapHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SnmpTrapHostIndex_Type.__name__ = "Integer32"
_SnmpTrapHostIndex_Object = MibTableColumn
snmpTrapHostIndex = _SnmpTrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 3, 1, 1),
    _SnmpTrapHostIndex_Type()
)
snmpTrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapHostIndex.setStatus("current")
_SnmpTrapHostIpaddress_Type = DisplayString
_SnmpTrapHostIpaddress_Object = MibTableColumn
snmpTrapHostIpaddress = _SnmpTrapHostIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 3, 1, 2),
    _SnmpTrapHostIpaddress_Type()
)
snmpTrapHostIpaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapHostIpaddress.setStatus("current")
_SnmpTrapHostCommunityName_Type = DisplayString
_SnmpTrapHostCommunityName_Object = MibTableColumn
snmpTrapHostCommunityName = _SnmpTrapHostCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 3, 1, 3),
    _SnmpTrapHostCommunityName_Type()
)
snmpTrapHostCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapHostCommunityName.setStatus("current")


class _SnmpTrapHostVersion_Type(Integer32):
    """Custom type snmpTrapHostVersion based on Integer32"""
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
        *(("v1", 1),
          ("v2cTrap", 2),
          ("v2cInform", 3),
          ("v3Trap", 4),
          ("v3Inform", 5))
    )


_SnmpTrapHostVersion_Type.__name__ = "Integer32"
_SnmpTrapHostVersion_Object = MibTableColumn
snmpTrapHostVersion = _SnmpTrapHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 3, 1, 4),
    _SnmpTrapHostVersion_Type()
)
snmpTrapHostVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapHostVersion.setStatus("current")


class _SnmpTrapHostRowStatus_Type(Integer32):
    """Custom type snmpTrapHostRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("createAndWait", 5),
          ("destory", 6))
    )


_SnmpTrapHostRowStatus_Type.__name__ = "Integer32"
_SnmpTrapHostRowStatus_Object = MibTableColumn
snmpTrapHostRowStatus = _SnmpTrapHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 3, 1, 99),
    _SnmpTrapHostRowStatus_Type()
)
snmpTrapHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapHostRowStatus.setStatus("current")
_Snmpv3UserTable_Object = MibTable
snmpv3UserTable = _Snmpv3UserTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 4)
)
if mibBuilder.loadTexts:
    snmpv3UserTable.setStatus("current")
_Snmpv3UserEntry_Object = MibTableRow
snmpv3UserEntry = _Snmpv3UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 4, 1)
)
snmpv3UserEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "snmpv3UserIndex"),
)
if mibBuilder.loadTexts:
    snmpv3UserEntry.setStatus("current")


class _Snmpv3UserIndex_Type(Integer32):
    """Custom type snmpv3UserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Snmpv3UserIndex_Type.__name__ = "Integer32"
_Snmpv3UserIndex_Object = MibTableColumn
snmpv3UserIndex = _Snmpv3UserIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 4, 1, 1),
    _Snmpv3UserIndex_Type()
)
snmpv3UserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3UserIndex.setStatus("current")
_Snmpv3UserName_Type = DisplayString
_Snmpv3UserName_Object = MibTableColumn
snmpv3UserName = _Snmpv3UserName_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 4, 1, 2),
    _Snmpv3UserName_Type()
)
snmpv3UserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3UserName.setStatus("current")


class _Snmpv3UserAccessRight_Type(Integer32):
    """Custom type snmpv3UserAccessRight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 1),
          ("readwrite", 2))
    )


_Snmpv3UserAccessRight_Type.__name__ = "Integer32"
_Snmpv3UserAccessRight_Object = MibTableColumn
snmpv3UserAccessRight = _Snmpv3UserAccessRight_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 4, 1, 3),
    _Snmpv3UserAccessRight_Type()
)
snmpv3UserAccessRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3UserAccessRight.setStatus("current")


class _Snmpv3UserAuthProtocol_Type(Integer32):
    """Custom type snmpv3UserAuthProtocol based on Integer32"""
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
          ("md5", 2),
          ("sha", 3))
    )


_Snmpv3UserAuthProtocol_Type.__name__ = "Integer32"
_Snmpv3UserAuthProtocol_Object = MibTableColumn
snmpv3UserAuthProtocol = _Snmpv3UserAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 4, 1, 4),
    _Snmpv3UserAuthProtocol_Type()
)
snmpv3UserAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3UserAuthProtocol.setStatus("current")
_Snmpv3UserAuthPassword_Type = DisplayString
_Snmpv3UserAuthPassword_Object = MibTableColumn
snmpv3UserAuthPassword = _Snmpv3UserAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 4, 1, 5),
    _Snmpv3UserAuthPassword_Type()
)
snmpv3UserAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3UserAuthPassword.setStatus("current")


class _Snmpv3UserPrivProtocol_Type(Integer32):
    """Custom type snmpv3UserPrivProtocol based on Integer32"""
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
          ("des", 2),
          ("aes", 3))
    )


_Snmpv3UserPrivProtocol_Type.__name__ = "Integer32"
_Snmpv3UserPrivProtocol_Object = MibTableColumn
snmpv3UserPrivProtocol = _Snmpv3UserPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 4, 1, 6),
    _Snmpv3UserPrivProtocol_Type()
)
snmpv3UserPrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3UserPrivProtocol.setStatus("current")
_Snmpv3UserPrivPassword_Type = DisplayString
_Snmpv3UserPrivPassword_Object = MibTableColumn
snmpv3UserPrivPassword = _Snmpv3UserPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 4, 1, 7),
    _Snmpv3UserPrivPassword_Type()
)
snmpv3UserPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3UserPrivPassword.setStatus("current")


class _Snmpv3UserRowStatus_Type(Integer32):
    """Custom type snmpv3UserRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("createAndWait", 5),
          ("destory", 6))
    )


_Snmpv3UserRowStatus_Type.__name__ = "Integer32"
_Snmpv3UserRowStatus_Object = MibTableColumn
snmpv3UserRowStatus = _Snmpv3UserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 4, 1, 99),
    _Snmpv3UserRowStatus_Type()
)
snmpv3UserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpv3UserRowStatus.setStatus("current")
_Snmpv3EngineID_Type = DisplayString
_Snmpv3EngineID_Object = MibScalar
snmpv3EngineID = _Snmpv3EngineID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 2, 5),
    _Snmpv3EngineID_Type()
)
snmpv3EngineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3EngineID.setStatus("current")
_Poe_ObjectIdentity = ObjectIdentity
poe = _Poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3)
)
_PoeSystemSetting_ObjectIdentity = ObjectIdentity
poeSystemSetting = _PoeSystemSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 1)
)
_PoeFwVersion_Type = DisplayString
_PoeFwVersion_Object = MibScalar
poeFwVersion = _PoeFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 1, 1),
    _PoeFwVersion_Type()
)
poeFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeFwVersion.setStatus("current")


class _PoeMaxPowerAvailable_Type(Integer32):
    """Custom type poeMaxPowerAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_PoeMaxPowerAvailable_Type.__name__ = "Integer32"
_PoeMaxPowerAvailable_Object = MibScalar
poeMaxPowerAvailable = _PoeMaxPowerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 1, 2),
    _PoeMaxPowerAvailable_Type()
)
poeMaxPowerAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeMaxPowerAvailable.setStatus("current")
if mibBuilder.loadTexts:
    poeMaxPowerAvailable.setUnits("W")
_PoeActualPowerConsumption_Type = Integer32
_PoeActualPowerConsumption_Object = MibScalar
poeActualPowerConsumption = _PoeActualPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 1, 3),
    _PoeActualPowerConsumption_Type()
)
poeActualPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeActualPowerConsumption.setStatus("current")
if mibBuilder.loadTexts:
    poeActualPowerConsumption.setUnits("W")


class _PoeOverLoadDisconnect_Type(Integer32):
    """Custom type poeOverLoadDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("overload-port-first", 1),
          ("port-based-priority", 2))
    )


_PoeOverLoadDisconnect_Type.__name__ = "Integer32"
_PoeOverLoadDisconnect_Object = MibScalar
poeOverLoadDisconnect = _PoeOverLoadDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 1, 4),
    _PoeOverLoadDisconnect_Type()
)
poeOverLoadDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeOverLoadDisconnect.setStatus("current")
_PoePortSettingTable_Object = MibTable
poePortSettingTable = _PoePortSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 2)
)
if mibBuilder.loadTexts:
    poePortSettingTable.setStatus("current")
_PoePortSettingEntry_Object = MibTableRow
poePortSettingEntry = _PoePortSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 2, 1)
)
poePortSettingEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "poePortIndex"),
)
if mibBuilder.loadTexts:
    poePortSettingEntry.setStatus("current")


class _PoePortIndex_Type(Integer32):
    """Custom type poePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PoePortIndex_Type.__name__ = "Integer32"
_PoePortIndex_Object = MibTableColumn
poePortIndex = _PoePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 2, 1, 1),
    _PoePortIndex_Type()
)
poePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortIndex.setStatus("current")


class _PoePortState_Type(Integer32):
    """Custom type poePortState based on Integer32"""
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


_PoePortState_Type.__name__ = "Integer32"
_PoePortState_Object = MibTableColumn
poePortState = _PoePortState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 2, 1, 2),
    _PoePortState_Type()
)
poePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poePortState.setStatus("current")


class _PoePortLegacy_Type(Integer32):
    """Custom type poePortLegacy based on Integer32"""
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


_PoePortLegacy_Type.__name__ = "Integer32"
_PoePortLegacy_Object = MibTableColumn
poePortLegacy = _PoePortLegacy_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 2, 1, 3),
    _PoePortLegacy_Type()
)
poePortLegacy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poePortLegacy.setStatus("current")


class _PoePortPowerLimitClass_Type(Integer32):
    """Custom type poePortPowerLimitClass based on Integer32"""
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


_PoePortPowerLimitClass_Type.__name__ = "Integer32"
_PoePortPowerLimitClass_Object = MibTableColumn
poePortPowerLimitClass = _PoePortPowerLimitClass_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 2, 1, 4),
    _PoePortPowerLimitClass_Type()
)
poePortPowerLimitClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poePortPowerLimitClass.setStatus("current")


class _PoePortPriority_Type(Integer32):
    """Custom type poePortPriority based on Integer32"""
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
        *(("low", 1),
          ("medium", 2),
          ("high", 3),
          ("critical", 4))
    )


_PoePortPriority_Type.__name__ = "Integer32"
_PoePortPriority_Object = MibTableColumn
poePortPriority = _PoePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 2, 1, 5),
    _PoePortPriority_Type()
)
poePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poePortPriority.setStatus("current")


class _PoePortPowerLimit_Type(Integer32):
    """Custom type poePortPowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_PoePortPowerLimit_Type.__name__ = "Integer32"
_PoePortPowerLimit_Object = MibTableColumn
poePortPowerLimit = _PoePortPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 2, 1, 6),
    _PoePortPowerLimit_Type()
)
poePortPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poePortPowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    poePortPowerLimit.setUnits("mW")
_PoePortStatusTable_Object = MibTable
poePortStatusTable = _PoePortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 3)
)
if mibBuilder.loadTexts:
    poePortStatusTable.setStatus("current")
_PoePortStatusEntry_Object = MibTableRow
poePortStatusEntry = _PoePortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 3, 1)
)
poePortStatusEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "poePortStatusIndex"),
)
if mibBuilder.loadTexts:
    poePortStatusEntry.setStatus("current")


class _PoePortStatusIndex_Type(Integer32):
    """Custom type poePortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PoePortStatusIndex_Type.__name__ = "Integer32"
_PoePortStatusIndex_Object = MibTableColumn
poePortStatusIndex = _PoePortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 3, 1, 1),
    _PoePortStatusIndex_Type()
)
poePortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortStatusIndex.setStatus("current")
_PoePortCurrent_Type = DisplayString
_PoePortCurrent_Object = MibTableColumn
poePortCurrent = _PoePortCurrent_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 3, 1, 2),
    _PoePortCurrent_Type()
)
poePortCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortCurrent.setStatus("current")
if mibBuilder.loadTexts:
    poePortCurrent.setUnits("mA")
_PoePortVoltage_Type = DisplayString
_PoePortVoltage_Object = MibTableColumn
poePortVoltage = _PoePortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 3, 1, 3),
    _PoePortVoltage_Type()
)
poePortVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortVoltage.setStatus("current")
if mibBuilder.loadTexts:
    poePortVoltage.setUnits("V")
_PoePortPower_Type = DisplayString
_PoePortPower_Object = MibTableColumn
poePortPower = _PoePortPower_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 3, 1, 4),
    _PoePortPower_Type()
)
poePortPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortPower.setStatus("current")
if mibBuilder.loadTexts:
    poePortPower.setUnits("W")
_PoePortTemp_Type = DisplayString
_PoePortTemp_Object = MibTableColumn
poePortTemp = _PoePortTemp_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 3, 3, 1, 5),
    _PoePortTemp_Type()
)
poePortTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortTemp.setStatus("current")
if mibBuilder.loadTexts:
    poePortTemp.setUnits("C")
_TcpModbus_ObjectIdentity = ObjectIdentity
tcpModbus = _TcpModbus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 4)
)


class _TcpModbusState_Type(Integer32):
    """Custom type tcpModbusState based on Integer32"""
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


_TcpModbusState_Type.__name__ = "Integer32"
_TcpModbusState_Object = MibScalar
tcpModbusState = _TcpModbusState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 4, 1),
    _TcpModbusState_Type()
)
tcpModbusState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpModbusState.setStatus("current")


class _TcpModbusTimeout_Type(Integer32):
    """Custom type tcpModbusTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_TcpModbusTimeout_Type.__name__ = "Integer32"
_TcpModbusTimeout_Object = MibScalar
tcpModbusTimeout = _TcpModbusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 4, 2),
    _TcpModbusTimeout_Type()
)
tcpModbusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpModbusTimeout.setStatus("current")
_DhcpServer_ObjectIdentity = ObjectIdentity
dhcpServer = _DhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5)
)


class _DhcpServerState_Type(Integer32):
    """Custom type dhcpServerState based on Integer32"""
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


_DhcpServerState_Type.__name__ = "Integer32"
_DhcpServerState_Object = MibScalar
dhcpServerState = _DhcpServerState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 1),
    _DhcpServerState_Type()
)
dhcpServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerState.setStatus("current")
_DhcpServerGlobalSetting_ObjectIdentity = ObjectIdentity
dhcpServerGlobalSetting = _DhcpServerGlobalSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 2)
)


class _DhcpServerLeaseTime_Type(Integer32):
    """Custom type dhcpServerLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 864000),
    )


_DhcpServerLeaseTime_Type.__name__ = "Integer32"
_DhcpServerLeaseTime_Object = MibScalar
dhcpServerLeaseTime = _DhcpServerLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 2, 1),
    _DhcpServerLeaseTime_Type()
)
dhcpServerLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    dhcpServerLeaseTime.setUnits("second")
_DhcpServerLowIP_Type = IpAddress
_DhcpServerLowIP_Object = MibScalar
dhcpServerLowIP = _DhcpServerLowIP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 2, 2),
    _DhcpServerLowIP_Type()
)
dhcpServerLowIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerLowIP.setStatus("current")
_DhcpServerHighIP_Type = IpAddress
_DhcpServerHighIP_Object = MibScalar
dhcpServerHighIP = _DhcpServerHighIP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 2, 3),
    _DhcpServerHighIP_Type()
)
dhcpServerHighIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerHighIP.setStatus("current")
_DhcpServerSubmask_Type = IpAddress
_DhcpServerSubmask_Object = MibScalar
dhcpServerSubmask = _DhcpServerSubmask_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 2, 4),
    _DhcpServerSubmask_Type()
)
dhcpServerSubmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerSubmask.setStatus("current")
_DhcpServerGateway_Type = IpAddress
_DhcpServerGateway_Object = MibScalar
dhcpServerGateway = _DhcpServerGateway_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 2, 5),
    _DhcpServerGateway_Type()
)
dhcpServerGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerGateway.setStatus("current")
_DhcpServerDNS_Type = IpAddress
_DhcpServerDNS_Object = MibScalar
dhcpServerDNS = _DhcpServerDNS_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 2, 6),
    _DhcpServerDNS_Type()
)
dhcpServerDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerDNS.setStatus("current")


class _DhcpServerStatus_Type(Integer32):
    """Custom type dhcpServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2))
    )


_DhcpServerStatus_Type.__name__ = "Integer32"
_DhcpServerStatus_Object = MibScalar
dhcpServerStatus = _DhcpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 2, 7),
    _DhcpServerStatus_Type()
)
dhcpServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerStatus.setStatus("current")


class _DhcpServerClearIpPool_Type(Integer32):
    """Custom type dhcpServerClearIpPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_DhcpServerClearIpPool_Type.__name__ = "Integer32"
_DhcpServerClearIpPool_Object = MibScalar
dhcpServerClearIpPool = _DhcpServerClearIpPool_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 2, 8),
    _DhcpServerClearIpPool_Type()
)
dhcpServerClearIpPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerClearIpPool.setStatus("current")
_DhcpServerPortTable_Object = MibTable
dhcpServerPortTable = _DhcpServerPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 3)
)
if mibBuilder.loadTexts:
    dhcpServerPortTable.setStatus("current")
_DhcpServerPortEntry_Object = MibTableRow
dhcpServerPortEntry = _DhcpServerPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 3, 1)
)
dhcpServerPortEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "dhcpServerPortIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerPortEntry.setStatus("current")


class _DhcpServerPortIndex_Type(Integer32):
    """Custom type dhcpServerPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DhcpServerPortIndex_Type.__name__ = "Integer32"
_DhcpServerPortIndex_Object = MibTableColumn
dhcpServerPortIndex = _DhcpServerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 3, 1, 1),
    _DhcpServerPortIndex_Type()
)
dhcpServerPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerPortIndex.setStatus("current")
_DhcpServerPortLowIP_Type = IpAddress
_DhcpServerPortLowIP_Object = MibTableColumn
dhcpServerPortLowIP = _DhcpServerPortLowIP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 3, 1, 2),
    _DhcpServerPortLowIP_Type()
)
dhcpServerPortLowIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerPortLowIP.setStatus("current")
_DhcpServerPortHighIP_Type = IpAddress
_DhcpServerPortHighIP_Object = MibTableColumn
dhcpServerPortHighIP = _DhcpServerPortHighIP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 3, 1, 3),
    _DhcpServerPortHighIP_Type()
)
dhcpServerPortHighIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerPortHighIP.setStatus("current")
_DhcpServerPortMask_Type = IpAddress
_DhcpServerPortMask_Object = MibTableColumn
dhcpServerPortMask = _DhcpServerPortMask_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 3, 1, 4),
    _DhcpServerPortMask_Type()
)
dhcpServerPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerPortMask.setStatus("current")
_DhcpServerPortGW_Type = IpAddress
_DhcpServerPortGW_Object = MibTableColumn
dhcpServerPortGW = _DhcpServerPortGW_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 3, 1, 5),
    _DhcpServerPortGW_Type()
)
dhcpServerPortGW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerPortGW.setStatus("current")
_DhcpServerPortDNS_Type = IpAddress
_DhcpServerPortDNS_Object = MibTableColumn
dhcpServerPortDNS = _DhcpServerPortDNS_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 3, 1, 6),
    _DhcpServerPortDNS_Type()
)
dhcpServerPortDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerPortDNS.setStatus("current")


class _DhcpServerPortStatus_Type(Integer32):
    """Custom type dhcpServerPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2))
    )


_DhcpServerPortStatus_Type.__name__ = "Integer32"
_DhcpServerPortStatus_Object = MibTableColumn
dhcpServerPortStatus = _DhcpServerPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 3, 1, 7),
    _DhcpServerPortStatus_Type()
)
dhcpServerPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerPortStatus.setStatus("current")


class _DhcpServerPortClear_Type(Integer32):
    """Custom type dhcpServerPortClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("clear", 1))
    )


_DhcpServerPortClear_Type.__name__ = "Integer32"
_DhcpServerPortClear_Object = MibTableColumn
dhcpServerPortClear = _DhcpServerPortClear_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 3, 1, 8),
    _DhcpServerPortClear_Type()
)
dhcpServerPortClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerPortClear.setStatus("current")
_DhcpServerOpt82Table_Object = MibTable
dhcpServerOpt82Table = _DhcpServerOpt82Table_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 4)
)
if mibBuilder.loadTexts:
    dhcpServerOpt82Table.setStatus("current")
_DhcpServerOpt82Entry_Object = MibTableRow
dhcpServerOpt82Entry = _DhcpServerOpt82Entry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 4, 1)
)
dhcpServerOpt82Entry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "dhcpServerOpt82Index"),
)
if mibBuilder.loadTexts:
    dhcpServerOpt82Entry.setStatus("current")


class _DhcpServerOpt82Index_Type(Integer32):
    """Custom type dhcpServerOpt82Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DhcpServerOpt82Index_Type.__name__ = "Integer32"
_DhcpServerOpt82Index_Object = MibTableColumn
dhcpServerOpt82Index = _DhcpServerOpt82Index_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 4, 1, 1),
    _DhcpServerOpt82Index_Type()
)
dhcpServerOpt82Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerOpt82Index.setStatus("current")


class _DhcpServerOpt82CircuitIDFormat_Type(Integer32):
    """Custom type dhcpServerOpt82CircuitIDFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("string", 1),
          ("hex", 2))
    )


_DhcpServerOpt82CircuitIDFormat_Type.__name__ = "Integer32"
_DhcpServerOpt82CircuitIDFormat_Object = MibTableColumn
dhcpServerOpt82CircuitIDFormat = _DhcpServerOpt82CircuitIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 4, 1, 2),
    _DhcpServerOpt82CircuitIDFormat_Type()
)
dhcpServerOpt82CircuitIDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerOpt82CircuitIDFormat.setStatus("current")
_DhcpServerOpt82CircuitID_Type = DisplayString
_DhcpServerOpt82CircuitID_Object = MibTableColumn
dhcpServerOpt82CircuitID = _DhcpServerOpt82CircuitID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 4, 1, 3),
    _DhcpServerOpt82CircuitID_Type()
)
dhcpServerOpt82CircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerOpt82CircuitID.setStatus("current")


class _DhcpServerOpt82RemoteIDFormat_Type(Integer32):
    """Custom type dhcpServerOpt82RemoteIDFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("string", 1),
          ("hex", 2))
    )


_DhcpServerOpt82RemoteIDFormat_Type.__name__ = "Integer32"
_DhcpServerOpt82RemoteIDFormat_Object = MibTableColumn
dhcpServerOpt82RemoteIDFormat = _DhcpServerOpt82RemoteIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 4, 1, 4),
    _DhcpServerOpt82RemoteIDFormat_Type()
)
dhcpServerOpt82RemoteIDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerOpt82RemoteIDFormat.setStatus("current")
_DhcpServerOpt82RemoteID_Type = DisplayString
_DhcpServerOpt82RemoteID_Object = MibTableColumn
dhcpServerOpt82RemoteID = _DhcpServerOpt82RemoteID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 4, 1, 5),
    _DhcpServerOpt82RemoteID_Type()
)
dhcpServerOpt82RemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerOpt82RemoteID.setStatus("current")
_DhcpServerOpt82LowIP_Type = IpAddress
_DhcpServerOpt82LowIP_Object = MibTableColumn
dhcpServerOpt82LowIP = _DhcpServerOpt82LowIP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 4, 1, 6),
    _DhcpServerOpt82LowIP_Type()
)
dhcpServerOpt82LowIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerOpt82LowIP.setStatus("current")
_DhcpServerOpt82HighIP_Type = IpAddress
_DhcpServerOpt82HighIP_Object = MibTableColumn
dhcpServerOpt82HighIP = _DhcpServerOpt82HighIP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 4, 1, 7),
    _DhcpServerOpt82HighIP_Type()
)
dhcpServerOpt82HighIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerOpt82HighIP.setStatus("current")
_DhcpServerOpt82Mask_Type = IpAddress
_DhcpServerOpt82Mask_Object = MibTableColumn
dhcpServerOpt82Mask = _DhcpServerOpt82Mask_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 4, 1, 8),
    _DhcpServerOpt82Mask_Type()
)
dhcpServerOpt82Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerOpt82Mask.setStatus("current")
_DhcpServerOpt82GW_Type = IpAddress
_DhcpServerOpt82GW_Object = MibTableColumn
dhcpServerOpt82GW = _DhcpServerOpt82GW_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 4, 1, 9),
    _DhcpServerOpt82GW_Type()
)
dhcpServerOpt82GW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerOpt82GW.setStatus("current")
_DhcpServerOpt82DNS_Type = IpAddress
_DhcpServerOpt82DNS_Object = MibTableColumn
dhcpServerOpt82DNS = _DhcpServerOpt82DNS_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 4, 1, 10),
    _DhcpServerOpt82DNS_Type()
)
dhcpServerOpt82DNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerOpt82DNS.setStatus("current")


class _DhcpServerOpt82Status_Type(Integer32):
    """Custom type dhcpServerOpt82Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2))
    )


_DhcpServerOpt82Status_Type.__name__ = "Integer32"
_DhcpServerOpt82Status_Object = MibTableColumn
dhcpServerOpt82Status = _DhcpServerOpt82Status_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 4, 1, 11),
    _DhcpServerOpt82Status_Type()
)
dhcpServerOpt82Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerOpt82Status.setStatus("current")


class _DhcpServerOpt82Clear_Type(Integer32):
    """Custom type dhcpServerOpt82Clear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("clear", 1))
    )


_DhcpServerOpt82Clear_Type.__name__ = "Integer32"
_DhcpServerOpt82Clear_Object = MibTableColumn
dhcpServerOpt82Clear = _DhcpServerOpt82Clear_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 4, 1, 12),
    _DhcpServerOpt82Clear_Type()
)
dhcpServerOpt82Clear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerOpt82Clear.setStatus("current")
_DhcpServerLeaseTable_Object = MibTable
dhcpServerLeaseTable = _DhcpServerLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 5)
)
if mibBuilder.loadTexts:
    dhcpServerLeaseTable.setStatus("current")
_DhcpServerLeaseEntry_Object = MibTableRow
dhcpServerLeaseEntry = _DhcpServerLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 5, 1)
)
dhcpServerLeaseEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "dhcpServerLeaseIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerLeaseEntry.setStatus("current")


class _DhcpServerLeaseIndex_Type(Integer32):
    """Custom type dhcpServerLeaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_DhcpServerLeaseIndex_Type.__name__ = "Integer32"
_DhcpServerLeaseIndex_Object = MibTableColumn
dhcpServerLeaseIndex = _DhcpServerLeaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 5, 1, 1),
    _DhcpServerLeaseIndex_Type()
)
dhcpServerLeaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerLeaseIndex.setStatus("current")
_DhcpServerLeaseIp_Type = DisplayString
_DhcpServerLeaseIp_Object = MibTableColumn
dhcpServerLeaseIp = _DhcpServerLeaseIp_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 5, 1, 2),
    _DhcpServerLeaseIp_Type()
)
dhcpServerLeaseIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerLeaseIp.setStatus("current")
_DhcpServerLeaseClientMac_Type = DisplayString
_DhcpServerLeaseClientMac_Object = MibTableColumn
dhcpServerLeaseClientMac = _DhcpServerLeaseClientMac_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 5, 1, 3),
    _DhcpServerLeaseClientMac_Type()
)
dhcpServerLeaseClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerLeaseClientMac.setStatus("current")
_DhcpServerLeaseStartTime_Type = DisplayString
_DhcpServerLeaseStartTime_Object = MibTableColumn
dhcpServerLeaseStartTime = _DhcpServerLeaseStartTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 5, 1, 4),
    _DhcpServerLeaseStartTime_Type()
)
dhcpServerLeaseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerLeaseStartTime.setStatus("current")
_DhcpServerLeaseEndTime_Type = DisplayString
_DhcpServerLeaseEndTime_Object = MibTableColumn
dhcpServerLeaseEndTime = _DhcpServerLeaseEndTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 5, 1, 5),
    _DhcpServerLeaseEndTime_Type()
)
dhcpServerLeaseEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerLeaseEndTime.setStatus("current")
_DhcpServerLeaseType_Type = DisplayString
_DhcpServerLeaseType_Object = MibTableColumn
dhcpServerLeaseType = _DhcpServerLeaseType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 5, 1, 6),
    _DhcpServerLeaseType_Type()
)
dhcpServerLeaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerLeaseType.setStatus("current")


class _DhcpServerRestart_Type(Integer32):
    """Custom type dhcpServerRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_DhcpServerRestart_Type.__name__ = "Integer32"
_DhcpServerRestart_Object = MibScalar
dhcpServerRestart = _DhcpServerRestart_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 6),
    _DhcpServerRestart_Type()
)
dhcpServerRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerRestart.setStatus("current")
_DhcpServerVlanTable_Object = MibTable
dhcpServerVlanTable = _DhcpServerVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 7)
)
if mibBuilder.loadTexts:
    dhcpServerVlanTable.setStatus("current")
_DhcpServerVlanEntry_Object = MibTableRow
dhcpServerVlanEntry = _DhcpServerVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 7, 1)
)
dhcpServerVlanEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "dhcpServerVlanIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerVlanEntry.setStatus("current")


class _DhcpServerVlanIndex_Type(Integer32):
    """Custom type dhcpServerVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DhcpServerVlanIndex_Type.__name__ = "Integer32"
_DhcpServerVlanIndex_Object = MibTableColumn
dhcpServerVlanIndex = _DhcpServerVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 7, 1, 1),
    _DhcpServerVlanIndex_Type()
)
dhcpServerVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerVlanIndex.setStatus("current")


class _DhcpServerVlanId_Type(Integer32):
    """Custom type dhcpServerVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpServerVlanId_Type.__name__ = "Integer32"
_DhcpServerVlanId_Object = MibTableColumn
dhcpServerVlanId = _DhcpServerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 7, 1, 2),
    _DhcpServerVlanId_Type()
)
dhcpServerVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerVlanId.setStatus("current")
_DhcpServerVlanLowIP_Type = IpAddress
_DhcpServerVlanLowIP_Object = MibTableColumn
dhcpServerVlanLowIP = _DhcpServerVlanLowIP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 7, 1, 3),
    _DhcpServerVlanLowIP_Type()
)
dhcpServerVlanLowIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerVlanLowIP.setStatus("current")
_DhcpServerVlanHighIP_Type = IpAddress
_DhcpServerVlanHighIP_Object = MibTableColumn
dhcpServerVlanHighIP = _DhcpServerVlanHighIP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 7, 1, 4),
    _DhcpServerVlanHighIP_Type()
)
dhcpServerVlanHighIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerVlanHighIP.setStatus("current")
_DhcpServerVlanMask_Type = IpAddress
_DhcpServerVlanMask_Object = MibTableColumn
dhcpServerVlanMask = _DhcpServerVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 7, 1, 5),
    _DhcpServerVlanMask_Type()
)
dhcpServerVlanMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerVlanMask.setStatus("current")
_DhcpServerVlanGW_Type = IpAddress
_DhcpServerVlanGW_Object = MibTableColumn
dhcpServerVlanGW = _DhcpServerVlanGW_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 7, 1, 6),
    _DhcpServerVlanGW_Type()
)
dhcpServerVlanGW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerVlanGW.setStatus("current")
_DhcpServerVlanDNS_Type = IpAddress
_DhcpServerVlanDNS_Object = MibTableColumn
dhcpServerVlanDNS = _DhcpServerVlanDNS_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 7, 1, 7),
    _DhcpServerVlanDNS_Type()
)
dhcpServerVlanDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerVlanDNS.setStatus("current")


class _DhcpServerVlanStatus_Type(Integer32):
    """Custom type dhcpServerVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2))
    )


_DhcpServerVlanStatus_Type.__name__ = "Integer32"
_DhcpServerVlanStatus_Object = MibTableColumn
dhcpServerVlanStatus = _DhcpServerVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 7, 1, 8),
    _DhcpServerVlanStatus_Type()
)
dhcpServerVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerVlanStatus.setStatus("current")


class _DhcpServerVlanClear_Type(Integer32):
    """Custom type dhcpServerVlanClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("clear", 1))
    )


_DhcpServerVlanClear_Type.__name__ = "Integer32"
_DhcpServerVlanClear_Object = MibTableColumn
dhcpServerVlanClear = _DhcpServerVlanClear_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 7, 1, 9),
    _DhcpServerVlanClear_Type()
)
dhcpServerVlanClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerVlanClear.setStatus("current")
_DhcpServerClientMacTable_Object = MibTable
dhcpServerClientMacTable = _DhcpServerClientMacTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 8)
)
if mibBuilder.loadTexts:
    dhcpServerClientMacTable.setStatus("current")
_DhcpServerClientMacEntry_Object = MibTableRow
dhcpServerClientMacEntry = _DhcpServerClientMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 8, 1)
)
dhcpServerClientMacEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "dhcpServerClientMacEntryID"),
)
if mibBuilder.loadTexts:
    dhcpServerClientMacEntry.setStatus("current")


class _DhcpServerClientMacEntryID_Type(Integer32):
    """Custom type dhcpServerClientMacEntryID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_DhcpServerClientMacEntryID_Type.__name__ = "Integer32"
_DhcpServerClientMacEntryID_Object = MibTableColumn
dhcpServerClientMacEntryID = _DhcpServerClientMacEntryID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 8, 1, 1),
    _DhcpServerClientMacEntryID_Type()
)
dhcpServerClientMacEntryID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerClientMacEntryID.setStatus("current")
_DhcpServerClientMacEntryMac_Type = DisplayString
_DhcpServerClientMacEntryMac_Object = MibTableColumn
dhcpServerClientMacEntryMac = _DhcpServerClientMacEntryMac_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 8, 1, 2),
    _DhcpServerClientMacEntryMac_Type()
)
dhcpServerClientMacEntryMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerClientMacEntryMac.setStatus("current")
_DhcpServerClientMacEntryIP_Type = IpAddress
_DhcpServerClientMacEntryIP_Object = MibTableColumn
dhcpServerClientMacEntryIP = _DhcpServerClientMacEntryIP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 8, 1, 3),
    _DhcpServerClientMacEntryIP_Type()
)
dhcpServerClientMacEntryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerClientMacEntryIP.setStatus("current")
_DhcpServerClientMacEntryMask_Type = IpAddress
_DhcpServerClientMacEntryMask_Object = MibTableColumn
dhcpServerClientMacEntryMask = _DhcpServerClientMacEntryMask_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 8, 1, 4),
    _DhcpServerClientMacEntryMask_Type()
)
dhcpServerClientMacEntryMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerClientMacEntryMask.setStatus("current")
_DhcpServerClientMacEntryGW_Type = IpAddress
_DhcpServerClientMacEntryGW_Object = MibTableColumn
dhcpServerClientMacEntryGW = _DhcpServerClientMacEntryGW_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 8, 1, 5),
    _DhcpServerClientMacEntryGW_Type()
)
dhcpServerClientMacEntryGW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerClientMacEntryGW.setStatus("current")
_DhcpServerClientMacEntryDNS_Type = IpAddress
_DhcpServerClientMacEntryDNS_Object = MibTableColumn
dhcpServerClientMacEntryDNS = _DhcpServerClientMacEntryDNS_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 8, 1, 6),
    _DhcpServerClientMacEntryDNS_Type()
)
dhcpServerClientMacEntryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerClientMacEntryDNS.setStatus("current")


class _DhcpServerClientMacEntryRowStatus_Type(Integer32):
    """Custom type dhcpServerClientMacEntryRowStatus based on Integer32"""
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )


_DhcpServerClientMacEntryRowStatus_Type.__name__ = "Integer32"
_DhcpServerClientMacEntryRowStatus_Object = MibTableColumn
dhcpServerClientMacEntryRowStatus = _DhcpServerClientMacEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 5, 8, 1, 7),
    _DhcpServerClientMacEntryRowStatus_Type()
)
dhcpServerClientMacEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpServerClientMacEntryRowStatus.setStatus("current")
_SmtpClient_ObjectIdentity = ObjectIdentity
smtpClient = _SmtpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 6)
)


class _SmtpActiveProfile_Type(Integer32):
    """Custom type smtpActiveProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2),
          ("none", 3))
    )


_SmtpActiveProfile_Type.__name__ = "Integer32"
_SmtpActiveProfile_Object = MibScalar
smtpActiveProfile = _SmtpActiveProfile_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 6, 1),
    _SmtpActiveProfile_Type()
)
smtpActiveProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpActiveProfile.setStatus("current")
_SmtpProfileTable_Object = MibTable
smtpProfileTable = _SmtpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 6, 2)
)
if mibBuilder.loadTexts:
    smtpProfileTable.setStatus("current")
_SmtpProfileEntry_Object = MibTableRow
smtpProfileEntry = _SmtpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 6, 2, 1)
)
smtpProfileEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "smtpProfileIndex"),
)
if mibBuilder.loadTexts:
    smtpProfileEntry.setStatus("current")


class _SmtpProfileIndex_Type(Integer32):
    """Custom type smtpProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SmtpProfileIndex_Type.__name__ = "Integer32"
_SmtpProfileIndex_Object = MibTableColumn
smtpProfileIndex = _SmtpProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 6, 2, 1, 1),
    _SmtpProfileIndex_Type()
)
smtpProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpProfileIndex.setStatus("current")
_SmtpServerIp_Type = DisplayString
_SmtpServerIp_Object = MibTableColumn
smtpServerIp = _SmtpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 6, 2, 1, 2),
    _SmtpServerIp_Type()
)
smtpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerIp.setStatus("current")
_SmtpServerPort_Type = Integer32
_SmtpServerPort_Object = MibTableColumn
smtpServerPort = _SmtpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 6, 2, 1, 3),
    _SmtpServerPort_Type()
)
smtpServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpServerPort.setStatus("current")
_SmtpSenderMail_Type = DisplayString
_SmtpSenderMail_Object = MibTableColumn
smtpSenderMail = _SmtpSenderMail_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 6, 2, 1, 4),
    _SmtpSenderMail_Type()
)
smtpSenderMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSenderMail.setStatus("current")
_SmtpTargetMail1_Type = DisplayString
_SmtpTargetMail1_Object = MibTableColumn
smtpTargetMail1 = _SmtpTargetMail1_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 6, 2, 1, 5),
    _SmtpTargetMail1_Type()
)
smtpTargetMail1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpTargetMail1.setStatus("current")
_SmtpTargetMail2_Type = DisplayString
_SmtpTargetMail2_Object = MibTableColumn
smtpTargetMail2 = _SmtpTargetMail2_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 6, 2, 1, 6),
    _SmtpTargetMail2_Type()
)
smtpTargetMail2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpTargetMail2.setStatus("current")
_SmtpTargetMail3_Type = DisplayString
_SmtpTargetMail3_Object = MibTableColumn
smtpTargetMail3 = _SmtpTargetMail3_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 6, 2, 1, 7),
    _SmtpTargetMail3_Type()
)
smtpTargetMail3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpTargetMail3.setStatus("current")
_SmtpTargetMail4_Type = DisplayString
_SmtpTargetMail4_Object = MibTableColumn
smtpTargetMail4 = _SmtpTargetMail4_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 6, 2, 1, 8),
    _SmtpTargetMail4_Type()
)
smtpTargetMail4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpTargetMail4.setStatus("current")
_SmtpTargetMail5_Type = DisplayString
_SmtpTargetMail5_Object = MibTableColumn
smtpTargetMail5 = _SmtpTargetMail5_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 6, 2, 1, 9),
    _SmtpTargetMail5_Type()
)
smtpTargetMail5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpTargetMail5.setStatus("current")
_SmtpTargetMail6_Type = DisplayString
_SmtpTargetMail6_Object = MibTableColumn
smtpTargetMail6 = _SmtpTargetMail6_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 6, 2, 1, 10),
    _SmtpTargetMail6_Type()
)
smtpTargetMail6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpTargetMail6.setStatus("current")
_SmtpTargetMail7_Type = DisplayString
_SmtpTargetMail7_Object = MibTableColumn
smtpTargetMail7 = _SmtpTargetMail7_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 6, 2, 1, 11),
    _SmtpTargetMail7_Type()
)
smtpTargetMail7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpTargetMail7.setStatus("current")
_SmtpTargetMail8_Type = DisplayString
_SmtpTargetMail8_Object = MibTableColumn
smtpTargetMail8 = _SmtpTargetMail8_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 6, 2, 1, 12),
    _SmtpTargetMail8_Type()
)
smtpTargetMail8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpTargetMail8.setStatus("current")
_Rmon_ObjectIdentity = ObjectIdentity
rmon = _Rmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7)
)
_RmonStatisticsTable_Object = MibTable
rmonStatisticsTable = _RmonStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 1)
)
if mibBuilder.loadTexts:
    rmonStatisticsTable.setStatus("current")
_RmonStatisticsEntry_Object = MibTableRow
rmonStatisticsEntry = _RmonStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 1, 1)
)
rmonStatisticsEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "rmonStatisticsIndex"),
)
if mibBuilder.loadTexts:
    rmonStatisticsEntry.setStatus("current")


class _RmonStatisticsIndex_Type(Integer32):
    """Custom type rmonStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonStatisticsIndex_Type.__name__ = "Integer32"
_RmonStatisticsIndex_Object = MibTableColumn
rmonStatisticsIndex = _RmonStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 1, 1, 1),
    _RmonStatisticsIndex_Type()
)
rmonStatisticsIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonStatisticsIndex.setStatus("current")
_RmonStatisticsPort_Type = Integer32
_RmonStatisticsPort_Object = MibTableColumn
rmonStatisticsPort = _RmonStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 1, 1, 2),
    _RmonStatisticsPort_Type()
)
rmonStatisticsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonStatisticsPort.setStatus("current")
_RmonStatisticsDropEvents_Type = Counter32
_RmonStatisticsDropEvents_Object = MibTableColumn
rmonStatisticsDropEvents = _RmonStatisticsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 1, 1, 3),
    _RmonStatisticsDropEvents_Type()
)
rmonStatisticsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatisticsDropEvents.setStatus("current")
_RmonStatisticsOctets_Type = Counter32
_RmonStatisticsOctets_Object = MibTableColumn
rmonStatisticsOctets = _RmonStatisticsOctets_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 1, 1, 4),
    _RmonStatisticsOctets_Type()
)
rmonStatisticsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatisticsOctets.setStatus("current")
_RmonStatisticsPackets_Type = Counter32
_RmonStatisticsPackets_Object = MibTableColumn
rmonStatisticsPackets = _RmonStatisticsPackets_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 1, 1, 5),
    _RmonStatisticsPackets_Type()
)
rmonStatisticsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatisticsPackets.setStatus("current")
_RmonStatisticsBroadcast_Type = Counter32
_RmonStatisticsBroadcast_Object = MibTableColumn
rmonStatisticsBroadcast = _RmonStatisticsBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 1, 1, 6),
    _RmonStatisticsBroadcast_Type()
)
rmonStatisticsBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatisticsBroadcast.setStatus("current")
_RmonStatisticsMulticast_Type = Counter32
_RmonStatisticsMulticast_Object = MibTableColumn
rmonStatisticsMulticast = _RmonStatisticsMulticast_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 1, 1, 7),
    _RmonStatisticsMulticast_Type()
)
rmonStatisticsMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatisticsMulticast.setStatus("current")
_RmonStatisticsOwner_Type = DisplayString
_RmonStatisticsOwner_Object = MibTableColumn
rmonStatisticsOwner = _RmonStatisticsOwner_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 1, 1, 8),
    _RmonStatisticsOwner_Type()
)
rmonStatisticsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonStatisticsOwner.setStatus("current")


class _RmonStatisticsRowStatus_Type(Integer32):
    """Custom type rmonStatisticsRowStatus based on Integer32"""
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )


_RmonStatisticsRowStatus_Type.__name__ = "Integer32"
_RmonStatisticsRowStatus_Object = MibTableColumn
rmonStatisticsRowStatus = _RmonStatisticsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 1, 1, 9),
    _RmonStatisticsRowStatus_Type()
)
rmonStatisticsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonStatisticsRowStatus.setStatus("current")
_RmonHistoryTable_Object = MibTable
rmonHistoryTable = _RmonHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 2)
)
if mibBuilder.loadTexts:
    rmonHistoryTable.setStatus("current")
_RmonHistoryEntry_Object = MibTableRow
rmonHistoryEntry = _RmonHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 2, 1)
)
rmonHistoryEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "rmonHistoryIndex"),
)
if mibBuilder.loadTexts:
    rmonHistoryEntry.setStatus("current")


class _RmonHistoryIndex_Type(Integer32):
    """Custom type rmonHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonHistoryIndex_Type.__name__ = "Integer32"
_RmonHistoryIndex_Object = MibTableColumn
rmonHistoryIndex = _RmonHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 2, 1, 1),
    _RmonHistoryIndex_Type()
)
rmonHistoryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHistoryIndex.setStatus("current")
_RmonHistoryPort_Type = Integer32
_RmonHistoryPort_Object = MibTableColumn
rmonHistoryPort = _RmonHistoryPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 2, 1, 2),
    _RmonHistoryPort_Type()
)
rmonHistoryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHistoryPort.setStatus("current")


class _RmonHistoryBucketsRequest_Type(Integer32):
    """Custom type rmonHistoryBucketsRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_RmonHistoryBucketsRequest_Type.__name__ = "Integer32"
_RmonHistoryBucketsRequest_Object = MibTableColumn
rmonHistoryBucketsRequest = _RmonHistoryBucketsRequest_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 2, 1, 3),
    _RmonHistoryBucketsRequest_Type()
)
rmonHistoryBucketsRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHistoryBucketsRequest.setStatus("current")


class _RmonHistoryInterval_Type(Integer32):
    """Custom type rmonHistoryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RmonHistoryInterval_Type.__name__ = "Integer32"
_RmonHistoryInterval_Object = MibTableColumn
rmonHistoryInterval = _RmonHistoryInterval_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 2, 1, 5),
    _RmonHistoryInterval_Type()
)
rmonHistoryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHistoryInterval.setStatus("current")
_RmonHistoryOwner_Type = DisplayString
_RmonHistoryOwner_Object = MibTableColumn
rmonHistoryOwner = _RmonHistoryOwner_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 2, 1, 6),
    _RmonHistoryOwner_Type()
)
rmonHistoryOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHistoryOwner.setStatus("current")


class _RmonHistoryRowStatus_Type(Integer32):
    """Custom type rmonHistoryRowStatus based on Integer32"""
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )


_RmonHistoryRowStatus_Type.__name__ = "Integer32"
_RmonHistoryRowStatus_Object = MibTableColumn
rmonHistoryRowStatus = _RmonHistoryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 2, 1, 7),
    _RmonHistoryRowStatus_Type()
)
rmonHistoryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonHistoryRowStatus.setStatus("current")
_RmonAlarmTable_Object = MibTable
rmonAlarmTable = _RmonAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 3)
)
if mibBuilder.loadTexts:
    rmonAlarmTable.setStatus("current")
_RmonAlarmEntry_Object = MibTableRow
rmonAlarmEntry = _RmonAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 3, 1)
)
rmonAlarmEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "rmonAlarmIndex"),
)
if mibBuilder.loadTexts:
    rmonAlarmEntry.setStatus("current")


class _RmonAlarmIndex_Type(Integer32):
    """Custom type rmonAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonAlarmIndex_Type.__name__ = "Integer32"
_RmonAlarmIndex_Object = MibTableColumn
rmonAlarmIndex = _RmonAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 3, 1, 1),
    _RmonAlarmIndex_Type()
)
rmonAlarmIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmIndex.setStatus("current")


class _RmonAlarmInterval_Type(Integer32):
    """Custom type rmonAlarmInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RmonAlarmInterval_Type.__name__ = "Integer32"
_RmonAlarmInterval_Object = MibTableColumn
rmonAlarmInterval = _RmonAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 3, 1, 2),
    _RmonAlarmInterval_Type()
)
rmonAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmInterval.setStatus("current")
_RmonAlarmVariable_Type = DisplayString
_RmonAlarmVariable_Object = MibTableColumn
rmonAlarmVariable = _RmonAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 3, 1, 3),
    _RmonAlarmVariable_Type()
)
rmonAlarmVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmVariable.setStatus("current")


class _RmonAlarmSampleType_Type(Integer32):
    """Custom type rmonAlarmSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("delta", 2))
    )


_RmonAlarmSampleType_Type.__name__ = "Integer32"
_RmonAlarmSampleType_Object = MibTableColumn
rmonAlarmSampleType = _RmonAlarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 3, 1, 4),
    _RmonAlarmSampleType_Type()
)
rmonAlarmSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmSampleType.setStatus("current")


class _RmonAlarmRisingThreshold_Type(Integer32):
    """Custom type rmonAlarmRisingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RmonAlarmRisingThreshold_Type.__name__ = "Integer32"
_RmonAlarmRisingThreshold_Object = MibTableColumn
rmonAlarmRisingThreshold = _RmonAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 3, 1, 5),
    _RmonAlarmRisingThreshold_Type()
)
rmonAlarmRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmRisingThreshold.setStatus("current")


class _RmonAlarmFallingThreshold_Type(Integer32):
    """Custom type rmonAlarmFallingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RmonAlarmFallingThreshold_Type.__name__ = "Integer32"
_RmonAlarmFallingThreshold_Object = MibTableColumn
rmonAlarmFallingThreshold = _RmonAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 3, 1, 6),
    _RmonAlarmFallingThreshold_Type()
)
rmonAlarmFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmFallingThreshold.setStatus("current")


class _RmonAlarmRisingEventIndex_Type(Integer32):
    """Custom type rmonAlarmRisingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonAlarmRisingEventIndex_Type.__name__ = "Integer32"
_RmonAlarmRisingEventIndex_Object = MibTableColumn
rmonAlarmRisingEventIndex = _RmonAlarmRisingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 3, 1, 7),
    _RmonAlarmRisingEventIndex_Type()
)
rmonAlarmRisingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmRisingEventIndex.setStatus("current")


class _RmonAlarmFallingEventIndex_Type(Integer32):
    """Custom type rmonAlarmFallingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonAlarmFallingEventIndex_Type.__name__ = "Integer32"
_RmonAlarmFallingEventIndex_Object = MibTableColumn
rmonAlarmFallingEventIndex = _RmonAlarmFallingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 3, 1, 8),
    _RmonAlarmFallingEventIndex_Type()
)
rmonAlarmFallingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmFallingEventIndex.setStatus("current")
_RmonAlarmOwner_Type = DisplayString
_RmonAlarmOwner_Object = MibTableColumn
rmonAlarmOwner = _RmonAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 3, 1, 9),
    _RmonAlarmOwner_Type()
)
rmonAlarmOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmOwner.setStatus("current")


class _RmonAlarmRowStatus_Type(Integer32):
    """Custom type rmonAlarmRowStatus based on Integer32"""
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )


_RmonAlarmRowStatus_Type.__name__ = "Integer32"
_RmonAlarmRowStatus_Object = MibTableColumn
rmonAlarmRowStatus = _RmonAlarmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 3, 1, 10),
    _RmonAlarmRowStatus_Type()
)
rmonAlarmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmRowStatus.setStatus("current")
_RmonEventTable_Object = MibTable
rmonEventTable = _RmonEventTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 4)
)
if mibBuilder.loadTexts:
    rmonEventTable.setStatus("current")
_RmonEventEntry_Object = MibTableRow
rmonEventEntry = _RmonEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 4, 1)
)
rmonEventEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "rmonEventIndex"),
)
if mibBuilder.loadTexts:
    rmonEventEntry.setStatus("current")


class _RmonEventIndex_Type(Integer32):
    """Custom type rmonEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonEventIndex_Type.__name__ = "Integer32"
_RmonEventIndex_Object = MibTableColumn
rmonEventIndex = _RmonEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 4, 1, 1),
    _RmonEventIndex_Type()
)
rmonEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonEventIndex.setStatus("current")
_RmonEventDescription_Type = DisplayString
_RmonEventDescription_Object = MibTableColumn
rmonEventDescription = _RmonEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 4, 1, 2),
    _RmonEventDescription_Type()
)
rmonEventDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonEventDescription.setStatus("current")


class _RmonEventType_Type(Integer32):
    """Custom type rmonEventType based on Integer32"""
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
          ("log", 2),
          ("trap", 3),
          ("logTrap", 4))
    )


_RmonEventType_Type.__name__ = "Integer32"
_RmonEventType_Object = MibTableColumn
rmonEventType = _RmonEventType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 4, 1, 3),
    _RmonEventType_Type()
)
rmonEventType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonEventType.setStatus("current")
_RmonEventCommunity_Type = DisplayString
_RmonEventCommunity_Object = MibTableColumn
rmonEventCommunity = _RmonEventCommunity_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 4, 1, 4),
    _RmonEventCommunity_Type()
)
rmonEventCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonEventCommunity.setStatus("current")
_RmonEventOwner_Type = DisplayString
_RmonEventOwner_Object = MibTableColumn
rmonEventOwner = _RmonEventOwner_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 4, 1, 5),
    _RmonEventOwner_Type()
)
rmonEventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonEventOwner.setStatus("current")


class _RmonEventRowStatus_Type(Integer32):
    """Custom type rmonEventRowStatus based on Integer32"""
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )


_RmonEventRowStatus_Type.__name__ = "Integer32"
_RmonEventRowStatus_Object = MibTableColumn
rmonEventRowStatus = _RmonEventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 7, 4, 1, 7),
    _RmonEventRowStatus_Type()
)
rmonEventRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonEventRowStatus.setStatus("current")
_Ntp_ObjectIdentity = ObjectIdentity
ntp = _Ntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 8)
)


class _NtpServer_Type(Integer32):
    """Custom type ntpServer based on Integer32"""
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


_NtpServer_Type.__name__ = "Integer32"
_NtpServer_Object = MibScalar
ntpServer = _NtpServer_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 8, 1),
    _NtpServer_Type()
)
ntpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServer.setStatus("current")


class _NtpManualTime_Type(Integer32):
    """Custom type ntpManualTime based on Integer32"""
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


_NtpManualTime_Type.__name__ = "Integer32"
_NtpManualTime_Object = MibScalar
ntpManualTime = _NtpManualTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 8, 2),
    _NtpManualTime_Type()
)
ntpManualTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpManualTime.setStatus("current")
_NtpServerTable_Object = MibTable
ntpServerTable = _NtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 8, 3)
)
if mibBuilder.loadTexts:
    ntpServerTable.setStatus("current")
_NtpServerEntry_Object = MibTableRow
ntpServerEntry = _NtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 8, 3, 1)
)
ntpServerEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "ntpServerIndex"),
)
if mibBuilder.loadTexts:
    ntpServerEntry.setStatus("current")


class _NtpServerIndex_Type(Integer32):
    """Custom type ntpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NtpServerIndex_Type.__name__ = "Integer32"
_NtpServerIndex_Object = MibTableColumn
ntpServerIndex = _NtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 8, 3, 1, 1),
    _NtpServerIndex_Type()
)
ntpServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpServerIndex.setStatus("current")
_NtpServerIp_Type = IpAddress
_NtpServerIp_Object = MibTableColumn
ntpServerIp = _NtpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 7, 8, 3, 1, 2),
    _NtpServerIp_Type()
)
ntpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServerIp.setStatus("current")
_Diagnostics_ObjectIdentity = ObjectIdentity
diagnostics = _Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8)
)
_CopperTest_ObjectIdentity = ObjectIdentity
copperTest = _CopperTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 1)
)
_PortNumber_Type = Integer32
_PortNumber_Object = MibScalar
portNumber = _PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 1, 1),
    _PortNumber_Type()
)
portNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portNumber.setStatus("current")


class _CopperTestAction_Type(Integer32):
    """Custom type copperTestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("copperTest", 1)
    )


_CopperTestAction_Type.__name__ = "Integer32"
_CopperTestAction_Object = MibScalar
copperTestAction = _CopperTestAction_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 1, 2),
    _CopperTestAction_Type()
)
copperTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copperTestAction.setStatus("current")
_CopperTestResult_ObjectIdentity = ObjectIdentity
copperTestResult = _CopperTestResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 1, 3)
)
_ResultPort_Type = Integer32
_ResultPort_Object = MibScalar
resultPort = _ResultPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 1, 3, 1),
    _ResultPort_Type()
)
resultPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resultPort.setStatus("current")
_ChannelA_Type = DisplayString
_ChannelA_Object = MibScalar
channelA = _ChannelA_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 1, 3, 2),
    _ChannelA_Type()
)
channelA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelA.setStatus("current")
_CableLengthA_Type = DisplayString
_CableLengthA_Object = MibScalar
cableLengthA = _CableLengthA_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 1, 3, 3),
    _CableLengthA_Type()
)
cableLengthA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableLengthA.setStatus("current")
_ChannelB_Type = DisplayString
_ChannelB_Object = MibScalar
channelB = _ChannelB_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 1, 3, 4),
    _ChannelB_Type()
)
channelB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelB.setStatus("current")
_CableLengthB_Type = DisplayString
_CableLengthB_Object = MibScalar
cableLengthB = _CableLengthB_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 1, 3, 5),
    _CableLengthB_Type()
)
cableLengthB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableLengthB.setStatus("current")
_ChannelC_Type = DisplayString
_ChannelC_Object = MibScalar
channelC = _ChannelC_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 1, 3, 6),
    _ChannelC_Type()
)
channelC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelC.setStatus("current")
_CableLengthC_Type = DisplayString
_CableLengthC_Object = MibScalar
cableLengthC = _CableLengthC_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 1, 3, 7),
    _CableLengthC_Type()
)
cableLengthC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableLengthC.setStatus("current")
_ChannelD_Type = DisplayString
_ChannelD_Object = MibScalar
channelD = _ChannelD_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 1, 3, 8),
    _ChannelD_Type()
)
channelD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelD.setStatus("current")
_CableLengthD_Type = DisplayString
_CableLengthD_Object = MibScalar
cableLengthD = _CableLengthD_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 1, 3, 9),
    _CableLengthD_Type()
)
cableLengthD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableLengthD.setStatus("current")
_ChannelRx_Type = DisplayString
_ChannelRx_Object = MibScalar
channelRx = _ChannelRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 1, 3, 10),
    _ChannelRx_Type()
)
channelRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelRx.setStatus("current")
_CableLengthRx_Type = DisplayString
_CableLengthRx_Object = MibScalar
cableLengthRx = _CableLengthRx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 1, 3, 11),
    _CableLengthRx_Type()
)
cableLengthRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableLengthRx.setStatus("current")
_ChannelTx_Type = DisplayString
_ChannelTx_Object = MibScalar
channelTx = _ChannelTx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 1, 3, 12),
    _ChannelTx_Type()
)
channelTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelTx.setStatus("current")
_CableLengthTx_Type = DisplayString
_CableLengthTx_Object = MibScalar
cableLengthTx = _CableLengthTx_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 1, 3, 13),
    _CableLengthTx_Type()
)
cableLengthTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableLengthTx.setStatus("current")
_PingTest_ObjectIdentity = ObjectIdentity
pingTest = _PingTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 2)
)
_PingIPAddress_Type = DisplayString
_PingIPAddress_Object = MibScalar
pingIPAddress = _PingIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 2, 1),
    _PingIPAddress_Type()
)
pingIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingIPAddress.setStatus("current")


class _PingCount_Type(Integer32):
    """Custom type pingCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_PingCount_Type.__name__ = "Integer32"
_PingCount_Object = MibScalar
pingCount = _PingCount_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 2, 2),
    _PingCount_Type()
)
pingCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingCount.setStatus("current")


class _PingInterval_Type(Integer32):
    """Custom type pingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_PingInterval_Type.__name__ = "Integer32"
_PingInterval_Object = MibScalar
pingInterval = _PingInterval_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 2, 3),
    _PingInterval_Type()
)
pingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingInterval.setStatus("current")


class _PingSize_Type(Integer32):
    """Custom type pingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 5120),
    )


_PingSize_Type.__name__ = "Integer32"
_PingSize_Object = MibScalar
pingSize = _PingSize_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 2, 4),
    _PingSize_Type()
)
pingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingSize.setStatus("current")


class _PingAction_Type(Integer32):
    """Custom type pingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ping", 1)
    )


_PingAction_Type.__name__ = "Integer32"
_PingAction_Object = MibScalar
pingAction = _PingAction_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 2, 5),
    _PingAction_Type()
)
pingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingAction.setStatus("current")
_PingResult_Type = DisplayString
_PingResult_Object = MibScalar
pingResult = _PingResult_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 2, 6),
    _PingResult_Type()
)
pingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResult.setStatus("current")
_Ipv6pingTest_ObjectIdentity = ObjectIdentity
ipv6pingTest = _Ipv6pingTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 3)
)
_PingIPv6Address_Type = DisplayString
_PingIPv6Address_Object = MibScalar
pingIPv6Address = _PingIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 3, 1),
    _PingIPv6Address_Type()
)
pingIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingIPv6Address.setStatus("current")


class _PingIPv6Count_Type(Integer32):
    """Custom type pingIPv6Count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_PingIPv6Count_Type.__name__ = "Integer32"
_PingIPv6Count_Object = MibScalar
pingIPv6Count = _PingIPv6Count_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 3, 2),
    _PingIPv6Count_Type()
)
pingIPv6Count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingIPv6Count.setStatus("current")


class _PingIPv6Interval_Type(Integer32):
    """Custom type pingIPv6Interval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_PingIPv6Interval_Type.__name__ = "Integer32"
_PingIPv6Interval_Object = MibScalar
pingIPv6Interval = _PingIPv6Interval_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 3, 3),
    _PingIPv6Interval_Type()
)
pingIPv6Interval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingIPv6Interval.setStatus("current")


class _PingIPv6Size_Type(Integer32):
    """Custom type pingIPv6Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 5120),
    )


_PingIPv6Size_Type.__name__ = "Integer32"
_PingIPv6Size_Object = MibScalar
pingIPv6Size = _PingIPv6Size_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 3, 4),
    _PingIPv6Size_Type()
)
pingIPv6Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingIPv6Size.setStatus("current")


class _PingIPv6Action_Type(Integer32):
    """Custom type pingIPv6Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ping", 1)
    )


_PingIPv6Action_Type.__name__ = "Integer32"
_PingIPv6Action_Object = MibScalar
pingIPv6Action = _PingIPv6Action_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 3, 5),
    _PingIPv6Action_Type()
)
pingIPv6Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingIPv6Action.setStatus("current")
_PingIPv6Result_Type = DisplayString
_PingIPv6Result_Object = MibScalar
pingIPv6Result = _PingIPv6Result_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 3, 6),
    _PingIPv6Result_Type()
)
pingIPv6Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingIPv6Result.setStatus("current")
_LoggingSetting_ObjectIdentity = ObjectIdentity
loggingSetting = _LoggingSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 4)
)


class _LoggingService_Type(Integer32):
    """Custom type loggingService based on Integer32"""
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


_LoggingService_Type.__name__ = "Integer32"
_LoggingService_Object = MibScalar
loggingService = _LoggingService_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 4, 1),
    _LoggingService_Type()
)
loggingService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingService.setStatus("current")
_LocalLoggingTable_Object = MibTable
localLoggingTable = _LocalLoggingTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 4, 2)
)
if mibBuilder.loadTexts:
    localLoggingTable.setStatus("current")
_LocalLoggingEntry_Object = MibTableRow
localLoggingEntry = _LocalLoggingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 4, 2, 1)
)
localLoggingEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "localLoggingIndex"),
)
if mibBuilder.loadTexts:
    localLoggingEntry.setStatus("current")


class _LocalLoggingIndex_Type(Integer32):
    """Custom type localLoggingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LocalLoggingIndex_Type.__name__ = "Integer32"
_LocalLoggingIndex_Object = MibTableColumn
localLoggingIndex = _LocalLoggingIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 4, 2, 1, 1),
    _LocalLoggingIndex_Type()
)
localLoggingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localLoggingIndex.setStatus("current")


class _Bufferedtarget_Type(Integer32):
    """Custom type bufferedtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("buffered", 1),
          ("console", 2),
          ("file", 3))
    )


_Bufferedtarget_Type.__name__ = "Integer32"
_Bufferedtarget_Object = MibTableColumn
bufferedtarget = _Bufferedtarget_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 4, 2, 1, 2),
    _Bufferedtarget_Type()
)
bufferedtarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferedtarget.setStatus("current")


class _LocalLoggingStatus_Type(Integer32):
    """Custom type localLoggingStatus based on Integer32"""
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


_LocalLoggingStatus_Type.__name__ = "Integer32"
_LocalLoggingStatus_Object = MibTableColumn
localLoggingStatus = _LocalLoggingStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 4, 2, 1, 3),
    _LocalLoggingStatus_Type()
)
localLoggingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localLoggingStatus.setStatus("current")


class _LocalLoggingSeverity_Type(Bits):
    """Custom type localLoggingSeverity based on Bits"""
    namedValues = NamedValues(
        *(("emerg", 0),
          ("alert", 1),
          ("crit", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )

_LocalLoggingSeverity_Type.__name__ = "Bits"
_LocalLoggingSeverity_Object = MibTableColumn
localLoggingSeverity = _LocalLoggingSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 4, 2, 1, 4),
    _LocalLoggingSeverity_Type()
)
localLoggingSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localLoggingSeverity.setStatus("current")
_RemoteloggingTable_Object = MibTable
remoteloggingTable = _RemoteloggingTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 4, 3)
)
if mibBuilder.loadTexts:
    remoteloggingTable.setStatus("current")
_RemoteloggingEntry_Object = MibTableRow
remoteloggingEntry = _RemoteloggingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 4, 3, 1)
)
remoteloggingEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "serverAddress"),
)
if mibBuilder.loadTexts:
    remoteloggingEntry.setStatus("current")


class _RemoteloggingIndex_Type(Integer32):
    """Custom type remoteloggingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RemoteloggingIndex_Type.__name__ = "Integer32"
_RemoteloggingIndex_Object = MibTableColumn
remoteloggingIndex = _RemoteloggingIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 4, 3, 1, 1),
    _RemoteloggingIndex_Type()
)
remoteloggingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteloggingIndex.setStatus("current")
_RemoteloggingAddress_Type = IpAddress
_RemoteloggingAddress_Object = MibTableColumn
remoteloggingAddress = _RemoteloggingAddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 4, 3, 1, 2),
    _RemoteloggingAddress_Type()
)
remoteloggingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteloggingAddress.setStatus("current")


class _RemoteloggingPort_Type(Integer32):
    """Custom type remoteloggingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RemoteloggingPort_Type.__name__ = "Integer32"
_RemoteloggingPort_Object = MibTableColumn
remoteloggingPort = _RemoteloggingPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 4, 3, 1, 3),
    _RemoteloggingPort_Type()
)
remoteloggingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteloggingPort.setStatus("current")


class _RemoteloggingSeverity_Type(Bits):
    """Custom type remoteloggingSeverity based on Bits"""
    namedValues = NamedValues(
        *(("emerg", 0),
          ("alert", 1),
          ("crit", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )

_RemoteloggingSeverity_Type.__name__ = "Bits"
_RemoteloggingSeverity_Object = MibTableColumn
remoteloggingSeverity = _RemoteloggingSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 4, 3, 1, 4),
    _RemoteloggingSeverity_Type()
)
remoteloggingSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteloggingSeverity.setStatus("current")


class _RemoteloggingFacility_Type(Integer32):
    """Custom type remoteloggingFacility based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("local0", 1),
          ("local1", 2),
          ("local2", 3),
          ("local3", 4),
          ("local4", 5),
          ("local5", 6),
          ("local6", 7),
          ("local7", 8))
    )


_RemoteloggingFacility_Type.__name__ = "Integer32"
_RemoteloggingFacility_Object = MibTableColumn
remoteloggingFacility = _RemoteloggingFacility_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 4, 3, 1, 5),
    _RemoteloggingFacility_Type()
)
remoteloggingFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteloggingFacility.setStatus("current")


class _RemoteloggingRowStatus_Type(Integer32):
    """Custom type remoteloggingRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("createAndWait", 5),
          ("destory", 6))
    )


_RemoteloggingRowStatus_Type.__name__ = "Integer32"
_RemoteloggingRowStatus_Object = MibTableColumn
remoteloggingRowStatus = _RemoteloggingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 4, 3, 1, 99),
    _RemoteloggingRowStatus_Type()
)
remoteloggingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remoteloggingRowStatus.setStatus("current")
_FactoryDefault_ObjectIdentity = ObjectIdentity
factoryDefault = _FactoryDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 5)
)


class _FactoryDefaultAction_Type(Integer32):
    """Custom type factoryDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("factoryDefault", 1)
    )


_FactoryDefaultAction_Type.__name__ = "Integer32"
_FactoryDefaultAction_Object = MibScalar
factoryDefaultAction = _FactoryDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 5, 1),
    _FactoryDefaultAction_Type()
)
factoryDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    factoryDefaultAction.setStatus("current")


class _FactoryDefaultKeepFlag_Type(Bits):
    """Custom type factoryDefaultKeepFlag based on Bits"""
    namedValues = NamedValues(
        *(("vlan", 1),
          ("ipaddress", 2),
          ("useraccount", 3))
    )

_FactoryDefaultKeepFlag_Type.__name__ = "Bits"
_FactoryDefaultKeepFlag_Object = MibScalar
factoryDefaultKeepFlag = _FactoryDefaultKeepFlag_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 5, 2),
    _FactoryDefaultKeepFlag_Type()
)
factoryDefaultKeepFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    factoryDefaultKeepFlag.setStatus("current")
_Reboot_ObjectIdentity = ObjectIdentity
reboot = _Reboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 6)
)


class _RebootAction_Type(Integer32):
    """Custom type rebootAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_RebootAction_Type.__name__ = "Integer32"
_RebootAction_Object = MibScalar
rebootAction = _RebootAction_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 6, 1),
    _RebootAction_Type()
)
rebootAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootAction.setStatus("current")
_DhcpAutoProvision_ObjectIdentity = ObjectIdentity
dhcpAutoProvision = _DhcpAutoProvision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 7)
)


class _DhcpAutoProvisionEnable_Type(Integer32):
    """Custom type dhcpAutoProvisionEnable based on Integer32"""
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


_DhcpAutoProvisionEnable_Type.__name__ = "Integer32"
_DhcpAutoProvisionEnable_Object = MibScalar
dhcpAutoProvisionEnable = _DhcpAutoProvisionEnable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 7, 1),
    _DhcpAutoProvisionEnable_Type()
)
dhcpAutoProvisionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpAutoProvisionEnable.setStatus("current")
_LedIndication_ObjectIdentity = ObjectIdentity
ledIndication = _LedIndication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 8)
)


class _LedAlarmState_Type(Integer32):
    """Custom type ledAlarmState based on Integer32"""
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


_LedAlarmState_Type.__name__ = "Integer32"
_LedAlarmState_Object = MibScalar
ledAlarmState = _LedAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 8, 1),
    _LedAlarmState_Type()
)
ledAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledAlarmState.setStatus("current")


class _LedPowerFailureEvent_Type(Integer32):
    """Custom type ledPowerFailureEvent based on Integer32"""
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


_LedPowerFailureEvent_Type.__name__ = "Integer32"
_LedPowerFailureEvent_Object = MibScalar
ledPowerFailureEvent = _LedPowerFailureEvent_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 8, 2),
    _LedPowerFailureEvent_Type()
)
ledPowerFailureEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledPowerFailureEvent.setStatus("current")


class _LedFiberLinkdownEvent_Type(Integer32):
    """Custom type ledFiberLinkdownEvent based on Integer32"""
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


_LedFiberLinkdownEvent_Type.__name__ = "Integer32"
_LedFiberLinkdownEvent_Object = MibScalar
ledFiberLinkdownEvent = _LedFiberLinkdownEvent_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 8, 3),
    _LedFiberLinkdownEvent_Type()
)
ledFiberLinkdownEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledFiberLinkdownEvent.setStatus("current")


class _LedPortLinkdownEvent_Type(Integer32):
    """Custom type ledPortLinkdownEvent based on Integer32"""
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


_LedPortLinkdownEvent_Type.__name__ = "Integer32"
_LedPortLinkdownEvent_Object = MibScalar
ledPortLinkdownEvent = _LedPortLinkdownEvent_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 8, 4),
    _LedPortLinkdownEvent_Type()
)
ledPortLinkdownEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledPortLinkdownEvent.setStatus("current")


class _LedPortLinkdownEventPort_Type(Bits):
    """Custom type ledPortLinkdownEventPort based on Bits"""
    namedValues = NamedValues(
        *(("port1", 0),
          ("port2", 1),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11),
          ("port13", 12),
          ("port14", 13),
          ("port15", 14),
          ("port16", 15),
          ("port17", 16),
          ("port18", 17),
          ("port19", 18),
          ("port20", 19),
          ("port21", 20),
          ("port22", 21),
          ("port23", 22),
          ("port24", 23),
          ("port25", 24),
          ("port26", 25),
          ("port27", 26),
          ("port28", 27),
          ("port29", 28),
          ("port30", 29),
          ("port31", 30),
          ("port32", 31))
    )

_LedPortLinkdownEventPort_Type.__name__ = "Bits"
_LedPortLinkdownEventPort_Object = MibScalar
ledPortLinkdownEventPort = _LedPortLinkdownEventPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 8, 5),
    _LedPortLinkdownEventPort_Type()
)
ledPortLinkdownEventPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledPortLinkdownEventPort.setStatus("current")
_LedEventInfoTable_Object = MibTable
ledEventInfoTable = _LedEventInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 8, 6)
)
if mibBuilder.loadTexts:
    ledEventInfoTable.setStatus("current")
_LedEventInfoEntry_Object = MibTableRow
ledEventInfoEntry = _LedEventInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 8, 6, 1)
)
ledEventInfoEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "ledEventIndex"),
)
if mibBuilder.loadTexts:
    ledEventInfoEntry.setStatus("current")


class _LedEventIndex_Type(Integer32):
    """Custom type ledEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LedEventIndex_Type.__name__ = "Integer32"
_LedEventIndex_Object = MibTableColumn
ledEventIndex = _LedEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 8, 6, 1, 1),
    _LedEventIndex_Type()
)
ledEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledEventIndex.setStatus("current")
_LedType_Type = DisplayString
_LedType_Object = MibTableColumn
ledType = _LedType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 8, 6, 1, 2),
    _LedType_Type()
)
ledType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledType.setStatus("current")
_LedEvent_Type = DisplayString
_LedEvent_Object = MibTableColumn
ledEvent = _LedEvent_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 8, 6, 1, 3),
    _LedEvent_Type()
)
ledEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledEvent.setStatus("current")
_LedState_Type = DisplayString
_LedState_Object = MibTableColumn
ledState = _LedState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 8, 6, 1, 4),
    _LedState_Type()
)
ledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledState.setStatus("current")


class _LedErrorTimes_Type(Integer32):
    """Custom type ledErrorTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LedErrorTimes_Type.__name__ = "Integer32"
_LedErrorTimes_Object = MibTableColumn
ledErrorTimes = _LedErrorTimes_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 8, 8, 6, 1, 5),
    _LedErrorTimes_Type()
)
ledErrorTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledErrorTimes.setStatus("current")
_Maintenance_ObjectIdentity = ObjectIdentity
maintenance = _Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9)
)
_BackupManager_ObjectIdentity = ObjectIdentity
backupManager = _BackupManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 1)
)


class _BackupMethod_Type(Integer32):
    """Custom type backupMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("tftp", 1)
    )


_BackupMethod_Type.__name__ = "Integer32"
_BackupMethod_Object = MibScalar
backupMethod = _BackupMethod_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 1, 1),
    _BackupMethod_Type()
)
backupMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupMethod.setStatus("current")
_BackupServerIP_Type = DisplayString
_BackupServerIP_Object = MibScalar
backupServerIP = _BackupServerIP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 1, 2),
    _BackupServerIP_Type()
)
backupServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupServerIP.setStatus("current")


class _BackupType_Type(Integer32):
    """Custom type backupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("image", 1),
          ("startupConfig", 2),
          ("runningConfig", 3),
          ("flashlog", 5),
          ("bufferlog", 6))
    )


_BackupType_Type.__name__ = "Integer32"
_BackupType_Object = MibScalar
backupType = _BackupType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 1, 3),
    _BackupType_Type()
)
backupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupType.setStatus("current")


class _BackupImage_Type(Integer32):
    """Custom type backupImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("partition0", 1),
          ("partition1", 2))
    )


_BackupImage_Type.__name__ = "Integer32"
_BackupImage_Object = MibScalar
backupImage = _BackupImage_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 1, 4),
    _BackupImage_Type()
)
backupImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupImage.setStatus("current")


class _BackupAction_Type(Integer32):
    """Custom type backupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("backup", 1)
    )


_BackupAction_Type.__name__ = "Integer32"
_BackupAction_Object = MibScalar
backupAction = _BackupAction_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 1, 5),
    _BackupAction_Type()
)
backupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupAction.setStatus("current")
_UpgradeManager_ObjectIdentity = ObjectIdentity
upgradeManager = _UpgradeManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 2)
)


class _UpgradeMethod_Type(Integer32):
    """Custom type upgradeMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("tftp", 1)
    )


_UpgradeMethod_Type.__name__ = "Integer32"
_UpgradeMethod_Object = MibScalar
upgradeMethod = _UpgradeMethod_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 2, 1),
    _UpgradeMethod_Type()
)
upgradeMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeMethod.setStatus("current")
_UpgradeServerIP_Type = DisplayString
_UpgradeServerIP_Object = MibScalar
upgradeServerIP = _UpgradeServerIP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 2, 2),
    _UpgradeServerIP_Type()
)
upgradeServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeServerIP.setStatus("current")
_UpgradeFileName_Type = DisplayString
_UpgradeFileName_Object = MibScalar
upgradeFileName = _UpgradeFileName_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 2, 3),
    _UpgradeFileName_Type()
)
upgradeFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeFileName.setStatus("current")


class _UpgradeType_Type(Integer32):
    """Custom type upgradeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("image", 1),
          ("startupConfig", 2),
          ("runningConfig", 3))
    )


_UpgradeType_Type.__name__ = "Integer32"
_UpgradeType_Object = MibScalar
upgradeType = _UpgradeType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 2, 4),
    _UpgradeType_Type()
)
upgradeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeType.setStatus("current")


class _UpgradeImage_Type(Integer32):
    """Custom type upgradeImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("backup", 2))
    )


_UpgradeImage_Type.__name__ = "Integer32"
_UpgradeImage_Object = MibScalar
upgradeImage = _UpgradeImage_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 2, 5),
    _UpgradeImage_Type()
)
upgradeImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeImage.setStatus("current")


class _UpgradeAction_Type(Integer32):
    """Custom type upgradeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("upgrade", 1)
    )


_UpgradeAction_Type.__name__ = "Integer32"
_UpgradeAction_Object = MibScalar
upgradeAction = _UpgradeAction_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 2, 6),
    _UpgradeAction_Type()
)
upgradeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeAction.setStatus("current")


class _UpgradeStatus_Type(Integer32):
    """Custom type upgradeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on-going", 1),
          ("done", 2))
    )


_UpgradeStatus_Type.__name__ = "Integer32"
_UpgradeStatus_Object = MibScalar
upgradeStatus = _UpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 2, 7),
    _UpgradeStatus_Type()
)
upgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeStatus.setStatus("current")
_DualImage_ObjectIdentity = ObjectIdentity
dualImage = _DualImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 3)
)


class _ActiveImage_Type(Integer32):
    """Custom type activeImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("image1", 1),
          ("image2", 2))
    )


_ActiveImage_Type.__name__ = "Integer32"
_ActiveImage_Object = MibScalar
activeImage = _ActiveImage_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 3, 1),
    _ActiveImage_Type()
)
activeImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeImage.setStatus("current")
_ImageInfoTable_Object = MibTable
imageInfoTable = _ImageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 3, 2)
)
if mibBuilder.loadTexts:
    imageInfoTable.setStatus("current")
_ImageInfoEntry_Object = MibTableRow
imageInfoEntry = _ImageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 3, 2, 1)
)
imageInfoEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "flashPartition"),
)
if mibBuilder.loadTexts:
    imageInfoEntry.setStatus("current")


class _FlashPartition_Type(Integer32):
    """Custom type flashPartition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_FlashPartition_Type.__name__ = "Integer32"
_FlashPartition_Object = MibTableColumn
flashPartition = _FlashPartition_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 3, 2, 1, 1),
    _FlashPartition_Type()
)
flashPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashPartition.setStatus("current")
_ImageName_Type = DisplayString
_ImageName_Object = MibTableColumn
imageName = _ImageName_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 3, 2, 1, 2),
    _ImageName_Type()
)
imageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageName.setStatus("current")
_ImageSize_Type = Integer32
_ImageSize_Object = MibTableColumn
imageSize = _ImageSize_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 3, 2, 1, 3),
    _ImageSize_Type()
)
imageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageSize.setStatus("current")
_CreatedTime_Type = DisplayString
_CreatedTime_Object = MibTableColumn
createdTime = _CreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 3, 2, 1, 4),
    _CreatedTime_Type()
)
createdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    createdTime.setStatus("current")
_ImageVersion_Type = DisplayString
_ImageVersion_Object = MibTableColumn
imageVersion = _ImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 3, 2, 1, 5),
    _ImageVersion_Type()
)
imageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageVersion.setStatus("current")
_ConfigurationManager_ObjectIdentity = ObjectIdentity
configurationManager = _ConfigurationManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 4)
)


class _SourceFile_Type(Integer32):
    """Custom type sourceFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("startup", 2))
    )


_SourceFile_Type.__name__ = "Integer32"
_SourceFile_Object = MibScalar
sourceFile = _SourceFile_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 4, 1),
    _SourceFile_Type()
)
sourceFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceFile.setStatus("current")


class _DestinationFile_Type(Integer32):
    """Custom type destinationFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("startup", 2))
    )


_DestinationFile_Type.__name__ = "Integer32"
_DestinationFile_Object = MibScalar
destinationFile = _DestinationFile_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 4, 2),
    _DestinationFile_Type()
)
destinationFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destinationFile.setStatus("current")


class _SaveConfiguration_Type(Integer32):
    """Custom type saveConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("save", 1)
    )


_SaveConfiguration_Type.__name__ = "Integer32"
_SaveConfiguration_Object = MibScalar
saveConfiguration = _SaveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 4, 3),
    _SaveConfiguration_Type()
)
saveConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveConfiguration.setStatus("current")
_AccountManager_ObjectIdentity = ObjectIdentity
accountManager = _AccountManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 5)
)
_LocalUserTable_Object = MibTable
localUserTable = _LocalUserTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 5, 1)
)
if mibBuilder.loadTexts:
    localUserTable.setStatus("current")
_LocalUserEntry_Object = MibTableRow
localUserEntry = _LocalUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 5, 1, 1)
)
localUserEntry.setIndexNames(
    (0, "ADVANTECH-EKI-PRONEER-MIB", "localUserIndex"),
)
if mibBuilder.loadTexts:
    localUserEntry.setStatus("current")


class _LocalUserIndex_Type(Integer32):
    """Custom type localUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_LocalUserIndex_Type.__name__ = "Integer32"
_LocalUserIndex_Object = MibTableColumn
localUserIndex = _LocalUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 5, 1, 1, 1),
    _LocalUserIndex_Type()
)
localUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localUserIndex.setStatus("current")
_LocalUserName_Type = DisplayString
_LocalUserName_Object = MibTableColumn
localUserName = _LocalUserName_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 5, 1, 1, 2),
    _LocalUserName_Type()
)
localUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUserName.setStatus("current")


class _LocalUserPasswordType_Type(Integer32):
    """Custom type localUserPasswordType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cleartext", 1),
          ("encrypted", 2),
          ("noPassword", 3))
    )


_LocalUserPasswordType_Type.__name__ = "Integer32"
_LocalUserPasswordType_Object = MibTableColumn
localUserPasswordType = _LocalUserPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 5, 1, 1, 3),
    _LocalUserPasswordType_Type()
)
localUserPasswordType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUserPasswordType.setStatus("current")
_LocalUserPassword_Type = DisplayString
_LocalUserPassword_Object = MibTableColumn
localUserPassword = _LocalUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 5, 1, 1, 4),
    _LocalUserPassword_Type()
)
localUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUserPassword.setStatus("current")


class _LocalUserPrivilegeType_Type(Integer32):
    """Custom type localUserPrivilegeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admin", 1),
          ("user", 2))
    )


_LocalUserPrivilegeType_Type.__name__ = "Integer32"
_LocalUserPrivilegeType_Object = MibTableColumn
localUserPrivilegeType = _LocalUserPrivilegeType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 5, 1, 1, 5),
    _LocalUserPrivilegeType_Type()
)
localUserPrivilegeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUserPrivilegeType.setStatus("current")


class _LocalUserRowStatus_Type(Integer32):
    """Custom type localUserRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("createAndWait", 5),
          ("destory", 6))
    )


_LocalUserRowStatus_Type.__name__ = "Integer32"
_LocalUserRowStatus_Object = MibTableColumn
localUserRowStatus = _LocalUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 5, 1, 1, 99),
    _LocalUserRowStatus_Type()
)
localUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    localUserRowStatus.setStatus("current")
_NKey_ObjectIdentity = ObjectIdentity
nKey = _NKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 6)
)


class _NKeyAutoMode_Type(Integer32):
    """Custom type nKeyAutoMode based on Integer32"""
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


_NKeyAutoMode_Type.__name__ = "Integer32"
_NKeyAutoMode_Object = MibScalar
nKeyAutoMode = _NKeyAutoMode_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 6, 1),
    _NKeyAutoMode_Type()
)
nKeyAutoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nKeyAutoMode.setStatus("current")


class _NKeyStatus_Type(Integer32):
    """Custom type nKeyStatus based on Integer32"""
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
        *(("idle", 0),
          ("backup", 1),
          ("restore", 2),
          ("running", 3))
    )


_NKeyStatus_Type.__name__ = "Integer32"
_NKeyStatus_Object = MibScalar
nKeyStatus = _NKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 9, 6, 2),
    _NKeyStatus_Type()
)
nKeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nKeyStatus.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 99)
)
_TrapObject_ObjectIdentity = ObjectIdentity
trapObject = _TrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 99, 1)
)
_DdmiAlarmDescr_Type = DisplayString
_DdmiAlarmDescr_Object = MibScalar
ddmiAlarmDescr = _DdmiAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 99, 1, 1),
    _DdmiAlarmDescr_Type()
)
ddmiAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmiAlarmDescr.setStatus("current")


class _XRingMasterStatus_Type(Integer32):
    """Custom type xRingMasterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("masterToSlave", 1),
          ("slaveToMaster", 2))
    )


_XRingMasterStatus_Type.__name__ = "Integer32"
_XRingMasterStatus_Object = MibScalar
xRingMasterStatus = _XRingMasterStatus_Object(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 99, 1, 2),
    _XRingMasterStatus_Type()
)
xRingMasterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRingMasterStatus.setStatus("current")

# Managed Objects groups


# Notification objects

ddmiAlarmWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 99, 2)
)
ddmiAlarmWarning.setObjects(
    ("ADVANTECH-EKI-PRONEER-MIB", "ddmiAlarmDescr")
)
if mibBuilder.loadTexts:
    ddmiAlarmWarning.setStatus(
        "current"
    )

xRingProMasterChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 99, 3)
)
xRingProMasterChange.setObjects(
      *(("ADVANTECH-EKI-PRONEER-MIB", "xRingMasterStatus"),
        ("ADVANTECH-EKI-PRONEER-MIB", "xRingProRingID"))
)
if mibBuilder.loadTexts:
    xRingProMasterChange.setStatus(
        "current"
    )

stpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 10297, 202, 7000, 99, 5)
)
stpStateChange.setObjects(
      *(("ADVANTECH-EKI-PRONEER-MIB", "stpPortStatusIndex"),
        ("ADVANTECH-EKI-PRONEER-MIB", "stpPortStatus"))
)
if mibBuilder.loadTexts:
    stpStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADVANTECH-EKI-PRONEER-MIB",
    **{"advantech": advantech,
       "aSwitchMIB": aSwitchMIB,
       "proneer": proneer,
       "monitoring": monitoring,
       "deviceInfo": deviceInfo,
       "systemName": systemName,
       "systemLocation": systemLocation,
       "systemContact": systemContact,
       "macAddress": macAddress,
       "ipAddress": ipAddress,
       "subnetMask": subnetMask,
       "gateway": gateway,
       "loaderVersion": loaderVersion,
       "loaderDate": loaderDate,
       "firmwareVersion": firmwareVersion,
       "firmwareDate": firmwareDate,
       "systemObjectID": systemObjectID,
       "systemUpTime": systemUpTime,
       "ledStatus": ledStatus,
       "ledSYSStatus": ledSYSStatus,
       "ledRMStatus": ledRMStatus,
       "ledPWR1Status": ledPWR1Status,
       "ledPWR2Status": ledPWR2Status,
       "ledAlarmStatus": ledAlarmStatus,
       "ledPFAILStatus": ledPFAILStatus,
       "ledRFAILStatus": ledRFAILStatus,
       "ledLOOPStatus": ledLOOPStatus,
       "ledTempStatus": ledTempStatus,
       "buildVersion": buildVersion,
       "loggingMessage": loggingMessage,
       "loggingBufferTable": loggingBufferTable,
       "loggingBufferEntry": loggingBufferEntry,
       "loggingBufferIndex": loggingBufferIndex,
       "loggingBufferSeverity": loggingBufferSeverity,
       "loggingBufferCategory": loggingBufferCategory,
       "loggingBufferTimeStamp": loggingBufferTimeStamp,
       "loggingBufferMessage": loggingBufferMessage,
       "clearBufferedMsg": clearBufferedMsg,
       "loggingFileTable": loggingFileTable,
       "loggingFileEntry": loggingFileEntry,
       "loggingFileIndex": loggingFileIndex,
       "loggingFileSeverity": loggingFileSeverity,
       "loggingFileCategory": loggingFileCategory,
       "loggingFileTimeStamp": loggingFileTimeStamp,
       "loggingFileMessage": loggingFileMessage,
       "clearFileMsg": clearFileMsg,
       "portMonitoring": portMonitoring,
       "portStatisticTable": portStatisticTable,
       "portStatisticEntry": portStatisticEntry,
       "portStatisticIndex": portStatisticIndex,
       "portCounterClear": portCounterClear,
       "ifInOctets": ifInOctets,
       "ifInUcastPkts": ifInUcastPkts,
       "ifInNUcastPkts": ifInNUcastPkts,
       "ifInDiscards": ifInDiscards,
       "ifOutOctets": ifOutOctets,
       "ifOutUcastPkts": ifOutUcastPkts,
       "ifOutNUcastPkts": ifOutNUcastPkts,
       "ifOutDiscards": ifOutDiscards,
       "ifInMulticastPkts": ifInMulticastPkts,
       "ifInBroadcastPkts": ifInBroadcastPkts,
       "ifOutMulticastPkts": ifOutMulticastPkts,
       "ifOutBroadcastPkts": ifOutBroadcastPkts,
       "dot3StatsAlignmentErrors": dot3StatsAlignmentErrors,
       "dot3StatsFCSErrors": dot3StatsFCSErrors,
       "dot3StatsSingleCollisionFrames": dot3StatsSingleCollisionFrames,
       "dot3StatsMultipleCollisionFrames": dot3StatsMultipleCollisionFrames,
       "dot3StatsDeferredTransmissions": dot3StatsDeferredTransmissions,
       "dot3StatsLateCollisions": dot3StatsLateCollisions,
       "dot3StatsExcessiveCollisions": dot3StatsExcessiveCollisions,
       "dot3StatsFrameTooLongs": dot3StatsFrameTooLongs,
       "dot3StatsSymbolErrors": dot3StatsSymbolErrors,
       "dot3ControlInUnknownOpcodes": dot3ControlInUnknownOpcodes,
       "dot3InPauseFrames": dot3InPauseFrames,
       "dot3OutPauseFrames": dot3OutPauseFrames,
       "linkAggregation": linkAggregation,
       "lagStatusTable": lagStatusTable,
       "lagStatusEntry": lagStatusEntry,
       "lagStatusIndex": lagStatusIndex,
       "lagStatusName": lagStatusName,
       "lagStatusType": lagStatusType,
       "lagStatusLinkState": lagStatusLinkState,
       "lagStatusActiveMember": lagStatusActiveMember,
       "lagStatusStandbyMember": lagStatusStandbyMember,
       "lacpInfoTable": lacpInfoTable,
       "lacpInfoEntry": lacpInfoEntry,
       "lacpInfoLagIndex": lacpInfoLagIndex,
       "lacpInfoPortIndex": lacpInfoPortIndex,
       "lacpInfoPartnerSysId": lacpInfoPartnerSysId,
       "lacpInfoPnkey": lacpInfoPnkey,
       "lacpInfoAtkey": lacpInfoAtkey,
       "lacpInfoSel": lacpInfoSel,
       "lacpInfoMux": lacpInfoMux,
       "lacpInfoReceiv": lacpInfoReceiv,
       "lacpInfoPrdtx": lacpInfoPrdtx,
       "lacpInfoAtstat": lacpInfoAtstat,
       "lacpInfoPnstat": lacpInfoPnstat,
       "lldpStatistics": lldpStatistics,
       "lldpClearStatistics": lldpClearStatistics,
       "inertions": inertions,
       "deletions": deletions,
       "drops": drops,
       "ageouts": ageouts,
       "lldpPortStatisticsTable": lldpPortStatisticsTable,
       "lldpPortStatisticsEntry": lldpPortStatisticsEntry,
       "lldpPortStatIndex": lldpPortStatIndex,
       "lldpPortStatTotalTxFrame": lldpPortStatTotalTxFrame,
       "lldpPortStatTotalRxFrame": lldpPortStatTotalRxFrame,
       "lldpPortStatDiscardRxFrame": lldpPortStatDiscardRxFrame,
       "lldpPortStatErrorRxFrame": lldpPortStatErrorRxFrame,
       "lldpPortStatDiscardRxTlv": lldpPortStatDiscardRxTlv,
       "lldpPortStatUnrecognizedRxTlv": lldpPortStatUnrecognizedRxTlv,
       "lldpPortStatTotalRxAgeouts": lldpPortStatTotalRxAgeouts,
       "igmpStatistics": igmpStatistics,
       "totalRx": totalRx,
       "validRx": validRx,
       "invalidRx": invalidRx,
       "otherRx": otherRx,
       "leaveRx": leaveRx,
       "reportRx": reportRx,
       "generalQueryRx": generalQueryRx,
       "specialGroupQueryRx": specialGroupQueryRx,
       "specialGroupSourceQueryRx": specialGroupSourceQueryRx,
       "leaveTx": leaveTx,
       "reportTx": reportTx,
       "generalQueryTx": generalQueryTx,
       "specialGroupQueryTx": specialGroupQueryTx,
       "specialGroupSourceQueryTx": specialGroupSourceQueryTx,
       "clearigmpStatistics": clearigmpStatistics,
       "mldStatistics": mldStatistics,
       "mldtotalRx": mldtotalRx,
       "mldvalidRx": mldvalidRx,
       "mldinvalidRx": mldinvalidRx,
       "mldotherRx": mldotherRx,
       "mldleaveRx": mldleaveRx,
       "mldreportRx": mldreportRx,
       "mldgeneralQueryRx": mldgeneralQueryRx,
       "mldspecialGroupQueryRx": mldspecialGroupQueryRx,
       "mldspecialGroupSourceQueryRx": mldspecialGroupSourceQueryRx,
       "mldleaveTx": mldleaveTx,
       "mldreportTx": mldreportTx,
       "mldgeneralQueryTx": mldgeneralQueryTx,
       "mldspecialGroupQueryTx": mldspecialGroupQueryTx,
       "mldspecialGroupSourceQueryTx": mldspecialGroupSourceQueryTx,
       "clearmldStatistics": clearmldStatistics,
       "system": system,
       "ipSettings": ipSettings,
       "ipv4Mode": ipv4Mode,
       "ipv4Address": ipv4Address,
       "ipv4SubnetMask": ipv4SubnetMask,
       "ipv4Gateway": ipv4Gateway,
       "ipv4DnsServer1": ipv4DnsServer1,
       "ipv4DnsServer2": ipv4DnsServer2,
       "interfaceIpv4Table": interfaceIpv4Table,
       "interfaceIpv4Entry": interfaceIpv4Entry,
       "interfaceIpv4Index": interfaceIpv4Index,
       "interfaceIpv4Vlan": interfaceIpv4Vlan,
       "interfaceIpv4Mode": interfaceIpv4Mode,
       "interfaceIpv4Address": interfaceIpv4Address,
       "interfaceIpv4SubnetMask": interfaceIpv4SubnetMask,
       "interfaceIpv4Gateway": interfaceIpv4Gateway,
       "interCurrIpv4DhcpState": interCurrIpv4DhcpState,
       "interCurrIpv4Address": interCurrIpv4Address,
       "interCurrIpv4SubnetMask": interCurrIpv4SubnetMask,
       "interCurrIpv4Gateway": interCurrIpv4Gateway,
       "ipv6Settings": ipv6Settings,
       "autoConfiguration": autoConfiguration,
       "ipv6Address": ipv6Address,
       "ipv6SubnetMask": ipv6SubnetMask,
       "ipv6Gateway": ipv6Gateway,
       "dhcpv6Client": dhcpv6Client,
       "ipv6InUseTable": ipv6InUseTable,
       "ipv6InUseEntry": ipv6InUseEntry,
       "ipv6InUseIndex": ipv6InUseIndex,
       "ipv6InUseAddress": ipv6InUseAddress,
       "ipv6InUseSubnetMask": ipv6InUseSubnetMask,
       "ipv6InUseRouter": ipv6InUseRouter,
       "dhcpv6DUID": dhcpv6DUID,
       "dhcpv6IPAddress": dhcpv6IPAddress,
       "managementVlan": managementVlan,
       "systemTime": systemTime,
       "systemTimeSetting": systemTimeSetting,
       "enableSNTP": enableSNTP,
       "manualTime": manualTime,
       "year": year,
       "month": month,
       "day": day,
       "hours": hours,
       "minutes": minutes,
       "seconds": seconds,
       "timeZone": timeZone,
       "daylightSaving": daylightSaving,
       "daylightSavingOffset": daylightSavingOffset,
       "recurringFrom": recurringFrom,
       "recFromDay": recFromDay,
       "recFromWeek": recFromWeek,
       "recFromMonth": recFromMonth,
       "recFromHours": recFromHours,
       "recFromMinutes": recFromMinutes,
       "recurringTo": recurringTo,
       "recToDay": recToDay,
       "recToWeek": recToWeek,
       "recToMonth": recToMonth,
       "recToHours": recToHours,
       "recToMinutes": recToMinutes,
       "nonRecurringFrom": nonRecurringFrom,
       "nonRecFromYear": nonRecFromYear,
       "nonRecFromMonth": nonRecFromMonth,
       "nonRecFromDay": nonRecFromDay,
       "nonRecFromHours": nonRecFromHours,
       "nonRecFromMinutes": nonRecFromMinutes,
       "nonRecurringTo": nonRecurringTo,
       "nonRecToYear": nonRecToYear,
       "nonRecToMonth": nonRecToMonth,
       "nonRecToDay": nonRecToDay,
       "nonRecToHours": nonRecToHours,
       "nonRecToMinutes": nonRecToMinutes,
       "serverAddress": serverAddress,
       "serverPort": serverPort,
       "systemTimeStatus": systemTimeStatus,
       "systemTimeInfo": systemTimeInfo,
       "currentDateTime": currentDateTime,
       "currentSNTP": currentSNTP,
       "currentSNTPServerAddr": currentSNTPServerAddr,
       "currentSNTPServerPort": currentSNTPServerPort,
       "currentTimeZone": currentTimeZone,
       "currentDaylightSavingStatus": currentDaylightSavingStatus,
       "currentDaylightSavingOffset": currentDaylightSavingOffset,
       "currentDaylightSavingFrom": currentDaylightSavingFrom,
       "currentDaylightSavingTo": currentDaylightSavingTo,
       "sfp": sfp,
       "sfpSerialInfoTable": sfpSerialInfoTable,
       "sfpSerialInfoEntry": sfpSerialInfoEntry,
       "sfpPortIndex": sfpPortIndex,
       "sfpConnector": sfpConnector,
       "sfpSpeed": sfpSpeed,
       "sfpVendorName": sfpVendorName,
       "sfpVendorPn": sfpVendorPn,
       "spfVendorRev": spfVendorRev,
       "sfpVendorSn": sfpVendorSn,
       "sfpDateCode": sfpDateCode,
       "sfpDMIInfoTable": sfpDMIInfoTable,
       "sfpDMIInfoEntry": sfpDMIInfoEntry,
       "sfpDMIPortIndex": sfpDMIPortIndex,
       "sfpDMITemperature": sfpDMITemperature,
       "sfpDMIVoltage": sfpDMIVoltage,
       "sfpDMITxBias": sfpDMITxBias,
       "sfpDMITxPower": sfpDMITxPower,
       "sfpDMIRxPower": sfpDMIRxPower,
       "ddmDiagnosticAlarm": ddmDiagnosticAlarm,
       "sfpDMIAlarmInfoTable": sfpDMIAlarmInfoTable,
       "sfpDMIAlarmInfoEntry": sfpDMIAlarmInfoEntry,
       "sfpDMIAlarmPortIndex": sfpDMIAlarmPortIndex,
       "sfpDMITempHighAlarmState": sfpDMITempHighAlarmState,
       "sfpDMITempHighAlarmValue": sfpDMITempHighAlarmValue,
       "sfpDMITempHighWarnState": sfpDMITempHighWarnState,
       "sfpDMITempHighWarnValue": sfpDMITempHighWarnValue,
       "sfpDMITempLowAlarmState": sfpDMITempLowAlarmState,
       "sfpDMITempLowAlarmValue": sfpDMITempLowAlarmValue,
       "sfpDMITempLowWarnState": sfpDMITempLowWarnState,
       "sfpDMITempLowWarnValue": sfpDMITempLowWarnValue,
       "sfpDMIVoltageHighAlarmState": sfpDMIVoltageHighAlarmState,
       "sfpDMIVoltageHighAlarmValue": sfpDMIVoltageHighAlarmValue,
       "sfpDMIVoltageHighWarnState": sfpDMIVoltageHighWarnState,
       "sfpDMIVoltageHighWarnValue": sfpDMIVoltageHighWarnValue,
       "sfpDMIVoltageLowAlarmState": sfpDMIVoltageLowAlarmState,
       "sfpDMIVoltageLowAlarmValue": sfpDMIVoltageLowAlarmValue,
       "sfpDMIVoltageLowWarnState": sfpDMIVoltageLowWarnState,
       "sfpDMIVoltageLowWarnValue": sfpDMIVoltageLowWarnValue,
       "sfpDMITxBasisHighAlarmState": sfpDMITxBasisHighAlarmState,
       "sfpDMITxBasisHighAlarmValue": sfpDMITxBasisHighAlarmValue,
       "sfpDMITxBasisHighWarnState": sfpDMITxBasisHighWarnState,
       "sfpDMITxBasisHighWarnValue": sfpDMITxBasisHighWarnValue,
       "sfpDMITxBasisLowAlarmState": sfpDMITxBasisLowAlarmState,
       "sfpDMITxBasisLowAlarmValue": sfpDMITxBasisLowAlarmValue,
       "sfpDMITxBasisLowWarnState": sfpDMITxBasisLowWarnState,
       "sfpDMITxBasisLowWarnValue": sfpDMITxBasisLowWarnValue,
       "sfpDMITxPowerHighAlarmState": sfpDMITxPowerHighAlarmState,
       "sfpDMITxPowerHighAlarmValue": sfpDMITxPowerHighAlarmValue,
       "sfpDMITxPowerHighWarnState": sfpDMITxPowerHighWarnState,
       "sfpDMITxPowerHighWarnValue": sfpDMITxPowerHighWarnValue,
       "sfpDMITxPowerLowAlarmState": sfpDMITxPowerLowAlarmState,
       "sfpDMITxPowerLowAlarmValue": sfpDMITxPowerLowAlarmValue,
       "sfpDMITxPowerLowWarnState": sfpDMITxPowerLowWarnState,
       "sfpDMITxPowerLowWarnValue": sfpDMITxPowerLowWarnValue,
       "sfpDMIRxPowerHighAlarmState": sfpDMIRxPowerHighAlarmState,
       "sfpDMIRxPowerHighAlarmValue": sfpDMIRxPowerHighAlarmValue,
       "sfpDMIRxPowerHighWarnState": sfpDMIRxPowerHighWarnState,
       "sfpDMIRxPowerHighWarnValue": sfpDMIRxPowerHighWarnValue,
       "sfpDMIRxPowerLowAlarmState": sfpDMIRxPowerLowAlarmState,
       "sfpDMIRxPowerLowAlarmValue": sfpDMIRxPowerLowAlarmValue,
       "sfpDMIRxPowerLowWarnState": sfpDMIRxPowerLowWarnState,
       "sfpDMIRxPowerLowWarnValue": sfpDMIRxPowerLowWarnValue,
       "dhcpClientOpt82": dhcpClientOpt82,
       "dhcpClientOpt82Status": dhcpClientOpt82Status,
       "dhcpClientOpt82CircuitIDFormat": dhcpClientOpt82CircuitIDFormat,
       "dhcpClientOpt82CircuitIDString": dhcpClientOpt82CircuitIDString,
       "dhcpClientOpt82CircuitIDHex": dhcpClientOpt82CircuitIDHex,
       "dhcpClientOpt82CircuitIDUserDefine": dhcpClientOpt82CircuitIDUserDefine,
       "dhcpClientOpt82RemoteIDFormat": dhcpClientOpt82RemoteIDFormat,
       "dhcpClientOpt82RemoteIDString": dhcpClientOpt82RemoteIDString,
       "dhcpClientOpt82RemoteIDHex": dhcpClientOpt82RemoteIDHex,
       "dhcpClientOpt82RemoteIDUserDefine": dhcpClientOpt82RemoteIDUserDefine,
       "networkPort": networkPort,
       "httpNetworkPort": httpNetworkPort,
       "httpsNetworkPort": httpsNetworkPort,
       "telnetNetworkPort": telnetNetworkPort,
       "sshNetworkPort": sshNetworkPort,
       "l2switching": l2switching,
       "portSetting": portSetting,
       "portSettingTable": portSettingTable,
       "portSettingEntry": portSettingEntry,
       "portSettingIndex": portSettingIndex,
       "description": description,
       "enableState": enableState,
       "linkStatus": linkStatus,
       "speed": speed,
       "duplex": duplex,
       "flowControlConfig": flowControlConfig,
       "flowControlStatus": flowControlStatus,
       "mirror": mirror,
       "mirrorTable": mirrorTable,
       "mirrorEntry": mirrorEntry,
       "sessionId": sessionId,
       "monitorSessionState": monitorSessionState,
       "destinationPort": destinationPort,
       "ingressState": ingressState,
       "sourceTxPort": sourceTxPort,
       "sourceRxPort": sourceRxPort,
       "lag": lag,
       "loadBalanceAlgorithm": loadBalanceAlgorithm,
       "lagManagementTable": lagManagementTable,
       "lagManagementEntry": lagManagementEntry,
       "lagIndex": lagIndex,
       "lagName": lagName,
       "lagType": lagType,
       "lagPorts": lagPorts,
       "lagLinkState": lagLinkState,
       "lagActiveMember": lagActiveMember,
       "lagStandbyMember": lagStandbyMember,
       "lagPortTable": lagPortTable,
       "lagPortEntry": lagPortEntry,
       "lagPortIndex": lagPortIndex,
       "lagPortDescription": lagPortDescription,
       "lagPortType": lagPortType,
       "lagPortEnableState": lagPortEnableState,
       "lagPortLinkStatus": lagPortLinkStatus,
       "lagPortSpeed": lagPortSpeed,
       "lagPortDuplex": lagPortDuplex,
       "lagPortFlowCtrlConfig": lagPortFlowCtrlConfig,
       "lagPortFlowCtrlStatus": lagPortFlowCtrlStatus,
       "lacpSystemPriority": lacpSystemPriority,
       "lacpPortTable": lacpPortTable,
       "lacpPortEntry": lacpPortEntry,
       "lacpPortIndex": lacpPortIndex,
       "lacpPriority": lacpPriority,
       "lacpTimeout": lacpTimeout,
       "lacpPortMode": lacpPortMode,
       "vlan": vlan,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanIndex": vlanIndex,
       "vlanId": vlanId,
       "vlanNamePrefix": vlanNamePrefix,
       "vlanType": vlanType,
       "vlanRowStatus": vlanRowStatus,
       "vlanInterfaceTable": vlanInterfaceTable,
       "vlanInterfaceEntry": vlanInterfaceEntry,
       "vlanPortIndex": vlanPortIndex,
       "vlanInterfaceVlanMode": vlanInterfaceVlanMode,
       "vlanPvid": vlanPvid,
       "vlanAcceptedType": vlanAcceptedType,
       "vlanIngressFiltering": vlanIngressFiltering,
       "portToVlanTable": portToVlanTable,
       "portToVlanEntry": portToVlanEntry,
       "portToVlanVlanIndex": portToVlanVlanIndex,
       "portToVlanPortIndex": portToVlanPortIndex,
       "portToVlanVlanId": portToVlanVlanId,
       "portToVlanInterfaceVlanMode": portToVlanInterfaceVlanMode,
       "portToVlanMembership": portToVlanMembership,
       "portToVlanPvid": portToVlanPvid,
       "portVlanTable": portVlanTable,
       "portVlanEntry": portVlanEntry,
       "portVlanPortIndex": portVlanPortIndex,
       "portVlanPortMode": portVlanPortMode,
       "portVlanAdminVlans": portVlanAdminVlans,
       "portVlanOperVlans": portVlanOperVlans,
       "voiceVlan": voiceVlan,
       "voiceVlanState": voiceVlanState,
       "voiceVlanId": voiceVlanId,
       "voiceVlanRemarkCos-8021p": voiceVlanRemarkCos_8021p,
       "voiceVlanRemark1q": voiceVlanRemark1q,
       "voiceVlanAgingTime": voiceVlanAgingTime,
       "telephonyOUITable": telephonyOUITable,
       "telephonyOUIEntry": telephonyOUIEntry,
       "telephonyOUIIndex": telephonyOUIIndex,
       "telephonyOUIAddress": telephonyOUIAddress,
       "telephonyOUIDescription": telephonyOUIDescription,
       "telephonyOUIRowStatus": telephonyOUIRowStatus,
       "telephonyOUIPortTable": telephonyOUIPortTable,
       "telephonyOUIPortEntry": telephonyOUIPortEntry,
       "telephonyOUIPortIndex": telephonyOUIPortIndex,
       "telephonyOUIState": telephonyOUIState,
       "telephonyOUICosMode": telephonyOUICosMode,
       "interfaceVlanTable": interfaceVlanTable,
       "interfaceVlanEntry": interfaceVlanEntry,
       "interfaceVlanIndex": interfaceVlanIndex,
       "interfaceVlanId": interfaceVlanId,
       "interfaceVlanName": interfaceVlanName,
       "interfaceVlanRowStatus": interfaceVlanRowStatus,
       "eee": eee,
       "eeePortTable": eeePortTable,
       "eeePortEntry": eeePortEntry,
       "eeePortIndex": eeePortIndex,
       "eeeState": eeeState,
       "multicast": multicast,
       "unknownMulticastAction": unknownMulticastAction,
       "forwardMethod": forwardMethod,
       "igmpSnooping": igmpSnooping,
       "igmpSnoopingState": igmpSnoopingState,
       "igmpSnoopingVersion": igmpSnoopingVersion,
       "igmpSnoopingReportSuppression": igmpSnoopingReportSuppression,
       "igmpSnoopingTable": igmpSnoopingTable,
       "igmpSnoopingEntry": igmpSnoopingEntry,
       "igmpSnoopingIndex": igmpSnoopingIndex,
       "igmpSnoopingVlanId": igmpSnoopingVlanId,
       "igmpSnoopStatus": igmpSnoopStatus,
       "routerPortsAutoLearn": routerPortsAutoLearn,
       "queryRobustness": queryRobustness,
       "queryInterval": queryInterval,
       "queryMaxResponseInterval": queryMaxResponseInterval,
       "lastMemberQueryCounter": lastMemberQueryCounter,
       "lastMemberQueryInterval": lastMemberQueryInterval,
       "immediateLeave": immediateLeave,
       "operQueryRobustness": operQueryRobustness,
       "operQueryInterval": operQueryInterval,
       "operQueryMaxResponseInterval": operQueryMaxResponseInterval,
       "operLastMemberQueryCounter": operLastMemberQueryCounter,
       "operLastMemberQueryInterval": operLastMemberQueryInterval,
       "igmpQuerierTable": igmpQuerierTable,
       "igmpQuerierEntry": igmpQuerierEntry,
       "igmpQuerierVlanId": igmpQuerierVlanId,
       "igmpQuerierState": igmpQuerierState,
       "igmpQuerierStatus": igmpQuerierStatus,
       "igmpQuerierVersion": igmpQuerierVersion,
       "igmpQuerierIP": igmpQuerierIP,
       "igmpStaticGroupTable": igmpStaticGroupTable,
       "igmpStaticGroupEntry": igmpStaticGroupEntry,
       "igmpStaticGroupIndex": igmpStaticGroupIndex,
       "igmpStaticGroupVlanId": igmpStaticGroupVlanId,
       "igmpStaticGroupIPaddress": igmpStaticGroupIPaddress,
       "igmpStaticGroupMemberPorts": igmpStaticGroupMemberPorts,
       "igmpStaticGroupRowStatus": igmpStaticGroupRowStatus,
       "igmpGroupTable": igmpGroupTable,
       "igmpGroupEntry": igmpGroupEntry,
       "igmpGroupVlanId": igmpGroupVlanId,
       "igmpGroupIPaddress": igmpGroupIPaddress,
       "igmpGroupMemberPorts": igmpGroupMemberPorts,
       "igmpGroupType": igmpGroupType,
       "igmpGroupLife": igmpGroupLife,
       "igmpRouterTable": igmpRouterTable,
       "igmpRouterEntry": igmpRouterEntry,
       "igmpRouterVlanId": igmpRouterVlanId,
       "igmpRouterPort": igmpRouterPort,
       "igmpRouterExpireTime": igmpRouterExpireTime,
       "mldSnooping": mldSnooping,
       "mldSnoopingState": mldSnoopingState,
       "mldSnoopingVersion": mldSnoopingVersion,
       "mldSnoopingReportSuppression": mldSnoopingReportSuppression,
       "mldSnoopingTable": mldSnoopingTable,
       "mldSnoopingEntry": mldSnoopingEntry,
       "mldSnoopingIndex": mldSnoopingIndex,
       "mldSnoopingVlanId": mldSnoopingVlanId,
       "mldSnoopStatus": mldSnoopStatus,
       "mldSnoopRouterPortsAutoLearn": mldSnoopRouterPortsAutoLearn,
       "mldSnoopQueryRobustness": mldSnoopQueryRobustness,
       "mldSnoopQueryInterval": mldSnoopQueryInterval,
       "mldSnoopQueryMaxResponseInterval": mldSnoopQueryMaxResponseInterval,
       "mldSnoopLastMemberQueryCounter": mldSnoopLastMemberQueryCounter,
       "mldSnoopLastMemberQueryInterval": mldSnoopLastMemberQueryInterval,
       "mldSnoopImmediateLeave": mldSnoopImmediateLeave,
       "operMldSnoopQueryRobustness": operMldSnoopQueryRobustness,
       "operMldSnoopQueryInterval": operMldSnoopQueryInterval,
       "operMldSnoopQueryMaxResponseInterval": operMldSnoopQueryMaxResponseInterval,
       "operMldSnoopLastMemberQueryCounter": operMldSnoopLastMemberQueryCounter,
       "operMldSnoopLastMemberQueryInterval": operMldSnoopLastMemberQueryInterval,
       "mldQuerierTable": mldQuerierTable,
       "mldQuerierEntry": mldQuerierEntry,
       "mldQuerierVlanId": mldQuerierVlanId,
       "mldQuerierState": mldQuerierState,
       "mldQuerierStatus": mldQuerierStatus,
       "mldQuerierVersion": mldQuerierVersion,
       "mldQuerierIP": mldQuerierIP,
       "mldStaticGroupTable": mldStaticGroupTable,
       "mldStaticGroupEntry": mldStaticGroupEntry,
       "mldStaticGroupIndex": mldStaticGroupIndex,
       "mldStaticGroupVlanId": mldStaticGroupVlanId,
       "mldStaticGroupIPaddress": mldStaticGroupIPaddress,
       "mldStaticGroupMemberPorts": mldStaticGroupMemberPorts,
       "mldStaticGroupRowStatus": mldStaticGroupRowStatus,
       "mldGroupTable": mldGroupTable,
       "mldGroupEntry": mldGroupEntry,
       "mldGroupVlanId": mldGroupVlanId,
       "mldGroupIPaddress": mldGroupIPaddress,
       "mldGroupMemberPorts": mldGroupMemberPorts,
       "mldGroupType": mldGroupType,
       "mldGroupLife": mldGroupLife,
       "mldRouterTable": mldRouterTable,
       "mldRouterEntry": mldRouterEntry,
       "mldRouterVlanId": mldRouterVlanId,
       "mldRouterPort": mldRouterPort,
       "mldRouterExpireTime": mldRouterExpireTime,
       "jamboFrame": jamboFrame,
       "jamboFramePktSize": jamboFramePktSize,
       "stp": stp,
       "stpEnable": stpEnable,
       "bpduForward": bpduForward,
       "pathCostMethod": pathCostMethod,
       "forceVersion": forceVersion,
       "stpPortTable": stpPortTable,
       "stpPortEntry": stpPortEntry,
       "stpPortIndex": stpPortIndex,
       "stpAdminEnable": stpAdminEnable,
       "stpPathCost": stpPathCost,
       "stpEdgePort": stpEdgePort,
       "stpP2pMac": stpP2pMac,
       "stpMigrate": stpMigrate,
       "stpBridgeInfo": stpBridgeInfo,
       "stpBridgePriority": stpBridgePriority,
       "stpBridgeForwardDelay": stpBridgeForwardDelay,
       "stpBridgeMaxAge": stpBridgeMaxAge,
       "stpBridgeTxHoldCount": stpBridgeTxHoldCount,
       "stpBridgeHelloTime": stpBridgeHelloTime,
       "stpBridgeStatus": stpBridgeStatus,
       "bridgeIdentifier": bridgeIdentifier,
       "definatedRootBridge": definatedRootBridge,
       "rootPathCost": rootPathCost,
       "designatedBridge": designatedBridge,
       "rootPort": rootPort,
       "lastTopologyChange": lastTopologyChange,
       "stpPortStatusTable": stpPortStatusTable,
       "stpPortStatusEntry": stpPortStatusEntry,
       "stpPortStatusIndex": stpPortStatusIndex,
       "stpPortPriority": stpPortPriority,
       "stpPortPathCost": stpPortPathCost,
       "stpPortDesignatedRootBridge": stpPortDesignatedRootBridge,
       "stpPortRootPathCost": stpPortRootPathCost,
       "stpPortDesignatedBridge": stpPortDesignatedBridge,
       "stpPortEdgrPortConf": stpPortEdgrPortConf,
       "stpPortP2PMacConf": stpPortP2PMacConf,
       "stpPortRoles": stpPortRoles,
       "stpPortStatus": stpPortStatus,
       "stpStatisticTable": stpStatisticTable,
       "stpStatisticEntry": stpStatisticEntry,
       "stpStatisticPortIndex": stpStatisticPortIndex,
       "configurationBPDUsReceived": configurationBPDUsReceived,
       "tcnBPDUsReceived": tcnBPDUsReceived,
       "configurationBPDUsTransmitted": configurationBPDUsTransmitted,
       "tcnBPDUsTransmitted": tcnBPDUsTransmitted,
       "mstp": mstp,
       "mstConfigIdentification": mstConfigIdentification,
       "mstConfigName": mstConfigName,
       "mstRevisionLevel": mstRevisionLevel,
       "mstInstanceID": mstInstanceID,
       "mstiIDSetting": mstiIDSetting,
       "mstiVlanListSetting": mstiVlanListSetting,
       "mstiIDSettingMove": mstiIDSettingMove,
       "mstiIDInfoTable": mstiIDInfoTable,
       "mstiIDInfoEntry": mstiIDInfoEntry,
       "mstiIDIndex": mstiIDIndex,
       "mstiVLANList": mstiVLANList,
       "stpInstance": stpInstance,
       "stpPriorityInfoTable": stpPriorityInfoTable,
       "stpPriorityInfoEntry": stpPriorityInfoEntry,
       "stpMstiIDIndex": stpMstiIDIndex,
       "stpPriorityValue": stpPriorityValue,
       "stpPriorityDefault": stpPriorityDefault,
       "mstInstanceInfo": mstInstanceInfo,
       "mstBridgeIdentifier": mstBridgeIdentifier,
       "mstDesignatedRootBridge": mstDesignatedRootBridge,
       "mstRootPathCost": mstRootPathCost,
       "mstDesignatedBridge": mstDesignatedBridge,
       "mstRootPort": mstRootPort,
       "mstLastTopologyChange": mstLastTopologyChange,
       "mstStpPortStatusTable": mstStpPortStatusTable,
       "mstStpPortStatusEntry": mstStpPortStatusEntry,
       "mstStpPortStatusIndex": mstStpPortStatusIndex,
       "mstStpPortPriority": mstStpPortPriority,
       "mstStpPortPathCost": mstStpPortPathCost,
       "mstStpPortDesignatedRootBridge": mstStpPortDesignatedRootBridge,
       "mstStpPortRootPathCost": mstStpPortRootPathCost,
       "mstStpPortDesignatedBridge": mstStpPortDesignatedBridge,
       "mstStpPortEdgrPortConf": mstStpPortEdgrPortConf,
       "mstStpPortP2PMacConf": mstStpPortP2PMacConf,
       "mstStpPortRoles": mstStpPortRoles,
       "mstStpPortStatus": mstStpPortStatus,
       "mstInstanceInfoID": mstInstanceInfoID,
       "qinqVlan": qinqVlan,
       "outerVlanEthtype": outerVlanEthtype,
       "qinqPortInfoTable": qinqPortInfoTable,
       "qinqPortInfoEntry": qinqPortInfoEntry,
       "qinqPortIndex": qinqPortIndex,
       "qinqOuterPVID": qinqOuterPVID,
       "qinqOuterMode": qinqOuterMode,
       "garp": garp,
       "garpJoinTime": garpJoinTime,
       "garpLeaveTime": garpLeaveTime,
       "garpLeaveAllTime": garpLeaveAllTime,
       "gvrp": gvrp,
       "gvrpStatus": gvrpStatus,
       "xRingElite": xRingElite,
       "xRingEliteState": xRingEliteState,
       "xRingEliteRingIDTable": xRingEliteRingIDTable,
       "xRingEliteRingIDEntry": xRingEliteRingIDEntry,
       "xRingEliteRingIDIndex": xRingEliteRingIDIndex,
       "xRingEliteRingID": xRingEliteRingID,
       "xRingEliteRule": xRingEliteRule,
       "xRingElitePort1": xRingElitePort1,
       "xRingElitePort2": xRingElitePort2,
       "xRingEliteRingIDStatus": xRingEliteRingIDStatus,
       "xRingElitePort1Status": xRingElitePort1Status,
       "xRingElitePort2Status": xRingElitePort2Status,
       "xRingEliteRowStatus": xRingEliteRowStatus,
       "loopback": loopback,
       "loopbackEnabled": loopbackEnabled,
       "loopbackInterval": loopbackInterval,
       "loopbackRecoverTime": loopbackRecoverTime,
       "loopbackPortTable": loopbackPortTable,
       "loopbackPortEntry": loopbackPortEntry,
       "loopbackPortIndex": loopbackPortIndex,
       "loopbackPortEnabled": loopbackPortEnabled,
       "loopbackPortLoopStatus": loopbackPortLoopStatus,
       "xRingPro": xRingPro,
       "xRingProStatus": xRingProStatus,
       "xRingProRingSetting": xRingProRingSetting,
       "xRingProRingID": xRingProRingID,
       "xRingProRingPort1": xRingProRingPort1,
       "xRingProRingPort2": xRingProRingPort2,
       "xRingProRingAdd": xRingProRingAdd,
       "xRingProCoupleSetting": xRingProCoupleSetting,
       "xRingProCoupleID": xRingProCoupleID,
       "xRingProCouplePort": xRingProCouplePort,
       "xRingProCoupleMasterRingID": xRingProCoupleMasterRingID,
       "xRingProCoupleAdd": xRingProCoupleAdd,
       "xRingProInfoTable": xRingProInfoTable,
       "xRingProInfoEntry": xRingProInfoEntry,
       "xRingProInfoRingID": xRingProInfoRingID,
       "xRingProInfoMode": xRingProInfoMode,
       "xRingProInfoOperState": xRingProInfoOperState,
       "xRingProInfoPort1": xRingProInfoPort1,
       "xRingProInfoPort1FwdState": xRingProInfoPort1FwdState,
       "xRingProInfoPort2": xRingProInfoPort2,
       "xRingProInfoPort2FwdState": xRingProInfoPort2FwdState,
       "xRingProInfoDel": xRingProInfoDel,
       "xRingProInfoRole": xRingProInfoRole,
       "xRingProPairSetting": xRingProPairSetting,
       "xRingProPairID": xRingProPairID,
       "xRingProPairPort": xRingProPairPort,
       "xRingProPairMasterRingID": xRingProPairMasterRingID,
       "xRingProPairAdd": xRingProPairAdd,
       "xRingProRPairSetting": xRingProRPairSetting,
       "xRingProRPairID": xRingProRPairID,
       "xRingProRPairPort": xRingProRPairPort,
       "xRingProRPairMasterRingID": xRingProRPairMasterRingID,
       "xRingProRPairAdd": xRingProRPairAdd,
       "xRingProChainSetting": xRingProChainSetting,
       "xRingProChainID": xRingProChainID,
       "xRingProChainRole": xRingProChainRole,
       "xRingProChainHeadPort": xRingProChainHeadPort,
       "xRingProChainMemberPort": xRingProChainMemberPort,
       "xRingProChainAdd": xRingProChainAdd,
       "gmrp": gmrp,
       "gmrpStatus": gmrpStatus,
       "gmrpMulticastGroupTable": gmrpMulticastGroupTable,
       "gmrpMulticastGroupEntry": gmrpMulticastGroupEntry,
       "gmrpMulticastGroupIndex": gmrpMulticastGroupIndex,
       "gmrpMulticastGroupVlanId": gmrpMulticastGroupVlanId,
       "gmrpMulticastGroupMacAddress": gmrpMulticastGroupMacAddress,
       "gmrpMulticastGroupType": gmrpMulticastGroupType,
       "gmrpMulticastGroupMemberPorts": gmrpMulticastGroupMemberPorts,
       "erps": erps,
       "erpsState": erpsState,
       "erpsGroupTable": erpsGroupTable,
       "erpsGroupEntry": erpsGroupEntry,
       "erpsGroupRingIndex": erpsGroupRingIndex,
       "erpsGroupInstance": erpsGroupInstance,
       "erpsGroupRingId": erpsGroupRingId,
       "erpsGroupRole": erpsGroupRole,
       "erpsGroupState": erpsGroupState,
       "erpsGroupEastLink": erpsGroupEastLink,
       "erpsGroupEastLinkRPL": erpsGroupEastLinkRPL,
       "erpsGroupEastLinkState": erpsGroupEastLinkState,
       "erpsGroupWestLink": erpsGroupWestLink,
       "erpsGroupWestLinkRPL": erpsGroupWestLinkRPL,
       "erpsGroupWestLinkState": erpsGroupWestLinkState,
       "erpsGroupMEL": erpsGroupMEL,
       "erpsGroupRAPSChannelVlan": erpsGroupRAPSChannelVlan,
       "erpsGroupTrafficChannel": erpsGroupTrafficChannel,
       "erpsGroupRevertive": erpsGroupRevertive,
       "erpsGroupType": erpsGroupType,
       "erpsGroupInterconnected": erpsGroupInterconnected,
       "erpsGroupChannel": erpsGroupChannel,
       "erpsGroupTcPropagation": erpsGroupTcPropagation,
       "erpsWTRTimer": erpsWTRTimer,
       "erpsGuardTimer": erpsGuardTimer,
       "erpsHoldOffTimer": erpsHoldOffTimer,
       "erpsGroupRowStatus": erpsGroupRowStatus,
       "macAddressTable": macAddressTable,
       "staticMacSetting": staticMacSetting,
       "staticMacSettingTable": staticMacSettingTable,
       "staticMacSettingEntry": staticMacSettingEntry,
       "staticMacSettingIndex": staticMacSettingIndex,
       "staticMacSettingMacAddress": staticMacSettingMacAddress,
       "staticMacSettingVlan": staticMacSettingVlan,
       "staticMacSettingPort": staticMacSettingPort,
       "staticMacSettingRowStatus": staticMacSettingRowStatus,
       "dynamicMacSetting": dynamicMacSetting,
       "macAgingTime": macAgingTime,
       "dynamicLearned": dynamicLearned,
       "clearMacAddressTable": clearMacAddressTable,
       "macAddressInfoTable": macAddressInfoTable,
       "macAddressInfoEntry": macAddressInfoEntry,
       "macAddressInfoIndex": macAddressInfoIndex,
       "macAddressInfoMAC": macAddressInfoMAC,
       "macAddressInfoVlan": macAddressInfoVlan,
       "macAddressInfoType": macAddressInfoType,
       "macAddressInfoPort": macAddressInfoPort,
       "addtoStaticMacTable": addtoStaticMacTable,
       "security": security,
       "stormControl": stormControl,
       "stromControlUnit": stromControlUnit,
       "stromControlPreamble-IFG": stromControlPreamble_IFG,
       "stromControlPortTable": stromControlPortTable,
       "stromControlPortEntry": stromControlPortEntry,
       "stromControlPortIndex": stromControlPortIndex,
       "stromControlPortState": stromControlPortState,
       "stromControlPortAction": stromControlPortAction,
       "enablebroadcast": enablebroadcast,
       "broadcastRate": broadcastRate,
       "enableunknownMulticast": enableunknownMulticast,
       "unknownMulticastRate": unknownMulticastRate,
       "enableunknownUnicast": enableunknownUnicast,
       "unknownUnicastRate": unknownUnicastRate,
       "protectedPort": protectedPort,
       "protectedPortTable": protectedPortTable,
       "protectedPortEntry": protectedPortEntry,
       "protectedPortIndex": protectedPortIndex,
       "protectedPortType": protectedPortType,
       "dos": dos,
       "dmacEqualsmac": dmacEqualsmac,
       "land": land,
       "udpBlat": udpBlat,
       "tcpBlat": tcpBlat,
       "pod": pod,
       "ipv6MinFragment": ipv6MinFragment,
       "ipv6MinFragmentValue": ipv6MinFragmentValue,
       "icmpFragment": icmpFragment,
       "ipv4PingMaxSize": ipv4PingMaxSize,
       "ipv6PingMaxSize": ipv6PingMaxSize,
       "pingMaxSizeSetting": pingMaxSizeSetting,
       "smurfAttack": smurfAttack,
       "smurfAttackValue": smurfAttackValue,
       "tcpMinHdrSize": tcpMinHdrSize,
       "tcpMinHdrSizeValue": tcpMinHdrSizeValue,
       "tcp-Syn": tcp_Syn,
       "nullScanAttack": nullScanAttack,
       "xMasScanAttack": xMasScanAttack,
       "tcpSYN-FINAttack": tcpSYN_FINAttack,
       "tcpSYN-RSTAttack": tcpSYN_RSTAttack,
       "tcpFragment": tcpFragment,
       "dosPortTable": dosPortTable,
       "dosPortEntry": dosPortEntry,
       "dosportIndex": dosportIndex,
       "dosProtection": dosProtection,
       "access": access,
       "telnetInfo": telnetInfo,
       "telnetService": telnetService,
       "currentTelnetSessionCount": currentTelnetSessionCount,
       "httpSetting": httpSetting,
       "httpService": httpService,
       "httpSessionTimeout": httpSessionTimeout,
       "httpsSetting": httpsSetting,
       "httpsService": httpsService,
       "httpsSessionTimeout": httpsSessionTimeout,
       "sshInfo": sshInfo,
       "sshService": sshService,
       "portSecurity": portSecurity,
       "portSecurityTable": portSecurityTable,
       "portSecurityEntry": portSecurityEntry,
       "portSecurityPortIndex": portSecurityPortIndex,
       "portSecurityEnabled": portSecurityEnabled,
       "portSecurityFDBLimit": portSecurityFDBLimit,
       "portSecurityViolationMACNotify": portSecurityViolationMACNotify,
       "ipSecurity": ipSecurity,
       "ipSecurityStatus": ipSecurityStatus,
       "ipSecurityTable": ipSecurityTable,
       "ipSecurityEntry": ipSecurityEntry,
       "ipSecurityIndex": ipSecurityIndex,
       "ipSecurityIPAddr": ipSecurityIPAddr,
       "ipSecurityIPMask": ipSecurityIPMask,
       "ipSecurityService": ipSecurityService,
       "ipSecurityVlanId": ipSecurityVlanId,
       "ipSecurityRowStatus": ipSecurityRowStatus,
       "ieee8021x": ieee8021x,
       "ieee8021xState": ieee8021xState,
       "ieee8021xServerIP": ieee8021xServerIP,
       "ieee8021xServerPort": ieee8021xServerPort,
       "ieee8021xAccountingPort": ieee8021xAccountingPort,
       "ieee8021xSecurityKey": ieee8021xSecurityKey,
       "ieee8021xReauthPeriod": ieee8021xReauthPeriod,
       "ieee8021xPortTable": ieee8021xPortTable,
       "ieee8021xPortEntry": ieee8021xPortEntry,
       "ieee8021xPortIndex": ieee8021xPortIndex,
       "ieee8021xPortState": ieee8021xPortState,
       "ieee8021xAuthBased": ieee8021xAuthBased,
       "securityLogin": securityLogin,
       "securityLoginState": securityLoginState,
       "radiusServer": radiusServer,
       "radiusServerIP": radiusServerIP,
       "radiusServerPort": radiusServerPort,
       "radiusServerSecurityKey": radiusServerSecurityKey,
       "tacacsServer": tacacsServer,
       "tacacsServerIP": tacacsServerIP,
       "tacacsServerPort": tacacsServerPort,
       "tacacsServerSecurityKey": tacacsServerSecurityKey,
       "securityLoginType": securityLoginType,
       "securityLoginHttpState": securityLoginHttpState,
       "securityLoginTelnetState": securityLoginTelnetState,
       "securityLoginSSHState": securityLoginSSHState,
       "acl": acl,
       "macAclTable": macAclTable,
       "macAclEntry": macAclEntry,
       "macAclIndex": macAclIndex,
       "destinationMacAddress": destinationMacAddress,
       "destinationMacMask": destinationMacMask,
       "sourceMacAddress": sourceMacAddress,
       "sourceMacMask": sourceMacMask,
       "macAclEtherType": macAclEtherType,
       "macAclVlanID": macAclVlanID,
       "macAclPortList": macAclPortList,
       "macAclAction": macAclAction,
       "macAclActiveStatus": macAclActiveStatus,
       "macAclRowStatus": macAclRowStatus,
       "ipAclTable": ipAclTable,
       "ipAclEntry": ipAclEntry,
       "ipAclIndex": ipAclIndex,
       "destinationIpAddress": destinationIpAddress,
       "destinationIpMask": destinationIpMask,
       "sourceIpAddress": sourceIpAddress,
       "sourceIpMask": sourceIpMask,
       "ipProtocol": ipProtocol,
       "l4DestinationPort": l4DestinationPort,
       "l4SourcePort": l4SourcePort,
       "ipAclPortList": ipAclPortList,
       "ipAclAction": ipAclAction,
       "ipAclActiveStatus": ipAclActiveStatus,
       "ipAclRowStatus": ipAclRowStatus,
       "ipSourceGuard": ipSourceGuard,
       "ipSourceGuardEnablePorts": ipSourceGuardEnablePorts,
       "ipSourceGuardTable": ipSourceGuardTable,
       "ipSourceGuardEntry": ipSourceGuardEntry,
       "ipSourceGuardIndex": ipSourceGuardIndex,
       "ipSourceGuardSourceIp": ipSourceGuardSourceIp,
       "ipSourceGuardSourceMac": ipSourceGuardSourceMac,
       "ipSourceGuardPort": ipSourceGuardPort,
       "ipSourceGuardRowStatus": ipSourceGuardRowStatus,
       "dhcpSnooping": dhcpSnooping,
       "dhcpSnoopingState": dhcpSnoopingState,
       "dhcpSnoopingPorts": dhcpSnoopingPorts,
       "dhcpSnoopingBindingPorts": dhcpSnoopingBindingPorts,
       "dhcpSnoopingTable": dhcpSnoopingTable,
       "dhcpSnoopingEntry": dhcpSnoopingEntry,
       "dhcpSnoopingIndex": dhcpSnoopingIndex,
       "dhcpSnoopingMac": dhcpSnoopingMac,
       "dhcpSnoopingIp": dhcpSnoopingIp,
       "dhcpSnoopingLeaseTime": dhcpSnoopingLeaseTime,
       "dhcpSnoopingVlanId": dhcpSnoopingVlanId,
       "dhcpSnoopingPort": dhcpSnoopingPort,
       "arpSpoofing": arpSpoofing,
       "arpSpoofingTable": arpSpoofingTable,
       "arpSpoofingEntry": arpSpoofingEntry,
       "arpSpoofingIndex": arpSpoofingIndex,
       "arpSpoofingSourceMac": arpSpoofingSourceMac,
       "arpSpoofingSourceIp": arpSpoofingSourceIp,
       "arpSpoofingRowStatus": arpSpoofingRowStatus,
       "qos": qos,
       "general": general,
       "qosMode": qosMode,
       "qosPortSettingTable": qosPortSettingTable,
       "qosPortSettingEntry": qosPortSettingEntry,
       "qosPortIndex": qosPortIndex,
       "qosPortCos": qosPortCos,
       "qosPortRemarkCoS": qosPortRemarkCoS,
       "qosPortRemarkDSCP": qosPortRemarkDSCP,
       "qosPortRemarkIPPrecedence": qosPortRemarkIPPrecedence,
       "queueSettingTable": queueSettingTable,
       "queueSettingEntry": queueSettingEntry,
       "queueIndex": queueIndex,
       "queueMethod": queueMethod,
       "queueWeight": queueWeight,
       "queuePercentOfWRRBandwidth": queuePercentOfWRRBandwidth,
       "costoQueueMapTable": costoQueueMapTable,
       "costoQueueMapEntry": costoQueueMapEntry,
       "cosIndex": cosIndex,
       "cosQueue": cosQueue,
       "queuetoCosMapTable": queuetoCosMapTable,
       "queuetoCosMapEntry": queuetoCosMapEntry,
       "queuetoCosIndex": queuetoCosIndex,
       "queueCos": queueCos,
       "dscptoQueueMapTable": dscptoQueueMapTable,
       "dscptoQueueMapEntry": dscptoQueueMapEntry,
       "dscpIndex": dscpIndex,
       "dscpQueue": dscpQueue,
       "queuetoDSCPMapTable": queuetoDSCPMapTable,
       "queuetoDSCPMapEntry": queuetoDSCPMapEntry,
       "queuetoDSCPIndex": queuetoDSCPIndex,
       "queuDscp": queuDscp,
       "ipPrecedencetoQueueMapTable": ipPrecedencetoQueueMapTable,
       "ipPrecedencetoQueueMapEntry": ipPrecedencetoQueueMapEntry,
       "ipPrecedenceIndex": ipPrecedenceIndex,
       "ipPrecedenceQueue": ipPrecedenceQueue,
       "queueToipPrecedenceMapTable": queueToipPrecedenceMapTable,
       "queueToipPrecedenceMapEntry": queueToipPrecedenceMapEntry,
       "queueToipPrecedenceIndex": queueToipPrecedenceIndex,
       "ipPrecedence": ipPrecedence,
       "qosBasicMode": qosBasicMode,
       "trustMode": trustMode,
       "qosBasicPortTable": qosBasicPortTable,
       "qosBasicPortEntry": qosBasicPortEntry,
       "qosBasicPortIndex": qosBasicPortIndex,
       "qosBasicPortTrust": qosBasicPortTrust,
       "rateLimit": rateLimit,
       "ingressBandwidthControl": ingressBandwidthControl,
       "ingressBandwidthTable": ingressBandwidthTable,
       "ingressBandwidthEntry": ingressBandwidthEntry,
       "ingressBandwidthPortIndex": ingressBandwidthPortIndex,
       "ingressBandwidthState": ingressBandwidthState,
       "ingressBandwidthRate": ingressBandwidthRate,
       "egressBandwidthControl": egressBandwidthControl,
       "egressBandwidthTable": egressBandwidthTable,
       "egressBandwidthEntry": egressBandwidthEntry,
       "egressBandwidthPortIndex": egressBandwidthPortIndex,
       "egressBandwidthState": egressBandwidthState,
       "egressBandwidthRate": egressBandwidthRate,
       "egressQueueBandwidthControl": egressQueueBandwidthControl,
       "egressqueueBandwidthTable": egressqueueBandwidthTable,
       "egressqueueBandwidthEntry": egressqueueBandwidthEntry,
       "egressqueueBandwidthPortIndex": egressqueueBandwidthPortIndex,
       "egressqueueBandwidthQueueIndex": egressqueueBandwidthQueueIndex,
       "egressqueueBandwidthState": egressqueueBandwidthState,
       "egressqueueBandwidthCir": egressqueueBandwidthCir,
       "management": management,
       "lldp": lldp,
       "lldpEnabled": lldpEnabled,
       "lldpPduDisableAction": lldpPduDisableAction,
       "lldpTransmissionInterval": lldpTransmissionInterval,
       "lldpHoldtimeMultiplier": lldpHoldtimeMultiplier,
       "lldpReinitializationDelay": lldpReinitializationDelay,
       "lldpTransmitDelay": lldpTransmitDelay,
       "lldpPortConfTable": lldpPortConfTable,
       "lldpPortConfEntry": lldpPortConfEntry,
       "lldpPortIndex": lldpPortIndex,
       "lldpPortState": lldpPortState,
       "lldpPortOptionalTLVs": lldpPortOptionalTLVs,
       "lldpPortVlans": lldpPortVlans,
       "localDevice": localDevice,
       "lldpLocalDeviceChassisidsubtype": lldpLocalDeviceChassisidsubtype,
       "lldpLocalDeviceChassisID": lldpLocalDeviceChassisID,
       "lldpLocalDeviceSystemName": lldpLocalDeviceSystemName,
       "lldpLocalDeviceSystemDescription": lldpLocalDeviceSystemDescription,
       "lldpLocalDeviceCapabilitiesSupported": lldpLocalDeviceCapabilitiesSupported,
       "lldpLocalDeviceCapabilitiesEnabled": lldpLocalDeviceCapabilitiesEnabled,
       "lldpLocalDevicePortIDsubtype": lldpLocalDevicePortIDsubtype,
       "lldpLocalPortStatusTable": lldpLocalPortStatusTable,
       "lldpLocalPortStatusEntry": lldpLocalPortStatusEntry,
       "lldpLocalPortIndex": lldpLocalPortIndex,
       "lldpLocalPortStatus": lldpLocalPortStatus,
       "lldpLocalPortChassisIDsubtype": lldpLocalPortChassisIDsubtype,
       "lldpLocalPortChassisID": lldpLocalPortChassisID,
       "lldpLocalPortSystemname": lldpLocalPortSystemname,
       "lldpLocalPortSystemdescription": lldpLocalPortSystemdescription,
       "lldpLocalPortSupportedsystemcapabilities": lldpLocalPortSupportedsystemcapabilities,
       "lldpLocalPortEnablesystemcapabilities": lldpLocalPortEnablesystemcapabilities,
       "lldpLocalPortIDsubtype": lldpLocalPortIDsubtype,
       "lldpLocalPortID": lldpLocalPortID,
       "lldpLocalPortDescription": lldpLocalPortDescription,
       "lldpLocalPortManagementAddress": lldpLocalPortManagementAddress,
       "lldpLocalPortAuto-negosupported": lldpLocalPortAuto_negosupported,
       "lldpLocalPortAuto-negoenabled": lldpLocalPortAuto_negoenabled,
       "lldpLocalPortAuto-negoAdvertisedCapabilities": lldpLocalPortAuto_negoAdvertisedCapabilities,
       "lldpLocalPortOperationMAUtype": lldpLocalPortOperationMAUtype,
       "lldpLocalPortIeee8023MaxFrameSize": lldpLocalPortIeee8023MaxFrameSize,
       "lldpLocalPortAggregationCapability": lldpLocalPortAggregationCapability,
       "lldpLocalPortAggregationStatus": lldpLocalPortAggregationStatus,
       "lldpLocalPortAggregationPortID": lldpLocalPortAggregationPortID,
       "lldpLocalPortPvid": lldpLocalPortPvid,
       "lldpLocalPortVlanName": lldpLocalPortVlanName,
       "remoteDevice": remoteDevice,
       "lldpremoteDeviceTable": lldpremoteDeviceTable,
       "lldpremoteDeviceEntry": lldpremoteDeviceEntry,
       "lldpremoteDeviceIndex": lldpremoteDeviceIndex,
       "lldpremoteDeviceLocalPort": lldpremoteDeviceLocalPort,
       "lldpremoteDeviceChassisIDsubtype": lldpremoteDeviceChassisIDsubtype,
       "lldpremoteDeviceChassisID": lldpremoteDeviceChassisID,
       "lldpremoteDevicePortIDsubtype": lldpremoteDevicePortIDsubtype,
       "lldpremoteDevicePortID": lldpremoteDevicePortID,
       "lldpremoteDeviceSystemName": lldpremoteDeviceSystemName,
       "lldpremoteDeviceTimetolive": lldpremoteDeviceTimetolive,
       "lldpremoteDeviceEntryIndex": lldpremoteDeviceEntryIndex,
       "lldpremoteDevicePortDescription": lldpremoteDevicePortDescription,
       "lldpremoteDeviceSystemdescription": lldpremoteDeviceSystemdescription,
       "lldpremoteDeviceSupportedsystemcapabilities": lldpremoteDeviceSupportedsystemcapabilities,
       "lldpremoteDeviceEnablesystemcapabilities": lldpremoteDeviceEnablesystemcapabilities,
       "lldpremoteDeviceManagementAddress": lldpremoteDeviceManagementAddress,
       "lldpremoteDeviceAuto-negosupported": lldpremoteDeviceAuto_negosupported,
       "lldpremoteDeviceAuto-negoenabled": lldpremoteDeviceAuto_negoenabled,
       "lldpremoteDeviceAuto-negoAdvertisedCapabilities": lldpremoteDeviceAuto_negoAdvertisedCapabilities,
       "lldpremoteDeviceOperationMAUtype": lldpremoteDeviceOperationMAUtype,
       "lldpremoteDeviceMdipowersupportportclass": lldpremoteDeviceMdipowersupportportclass,
       "lldpremoteDevicePsemdipowersupport": lldpremoteDevicePsemdipowersupport,
       "lldpremoteDevicePsemdipowerstatus": lldpremoteDevicePsemdipowerstatus,
       "lldpremoteDevicePsepowerpaircontrolability": lldpremoteDevicePsepowerpaircontrolability,
       "lldpremoteDevicePsepowerpair": lldpremoteDevicePsepowerpair,
       "lldpremoteDevicePsepowerclass": lldpremoteDevicePsepowerclass,
       "lldpremoteDeviceIeee8023MaxFrameSize": lldpremoteDeviceIeee8023MaxFrameSize,
       "lldpremoteDeviceAggregationCapability": lldpremoteDeviceAggregationCapability,
       "lldpremoteDeviceAggregationStatus": lldpremoteDeviceAggregationStatus,
       "lldpremoteDeviceAggregationPortID": lldpremoteDeviceAggregationPortID,
       "lldpremoteDevicePvid": lldpremoteDevicePvid,
       "lldpremoteDeviceVlanName": lldpremoteDeviceVlanName,
       "lldpremoteDeviceRowStatus": lldpremoteDeviceRowStatus,
       "lldpOverloadingTable": lldpOverloadingTable,
       "lldpOverloadingEntry": lldpOverloadingEntry,
       "lldpOverloadingPortIndex": lldpOverloadingPortIndex,
       "lldpOverloadingTotal": lldpOverloadingTotal,
       "lldpOverloadingLeftToSend": lldpOverloadingLeftToSend,
       "lldpOverloadingStatus": lldpOverloadingStatus,
       "lldpOverloadingMandatoryTLVs": lldpOverloadingMandatoryTLVs,
       "lldpOverloadingIeee8023TLVs": lldpOverloadingIeee8023TLVs,
       "lldpOverloadingOptionalTLVs": lldpOverloadingOptionalTLVs,
       "lldpOverloadingIeee8021TLVs": lldpOverloadingIeee8021TLVs,
       "snmp": snmp,
       "snmpState": snmpState,
       "snmpCommunityTable": snmpCommunityTable,
       "snmpCommunityEntry": snmpCommunityEntry,
       "snmpCommunityIndex": snmpCommunityIndex,
       "snmpCommunityString": snmpCommunityString,
       "snmpCommunityAccessRight": snmpCommunityAccessRight,
       "snmpCommunityRowStatus": snmpCommunityRowStatus,
       "snmpTrapHostTable": snmpTrapHostTable,
       "snmpTrapHostEntry": snmpTrapHostEntry,
       "snmpTrapHostIndex": snmpTrapHostIndex,
       "snmpTrapHostIpaddress": snmpTrapHostIpaddress,
       "snmpTrapHostCommunityName": snmpTrapHostCommunityName,
       "snmpTrapHostVersion": snmpTrapHostVersion,
       "snmpTrapHostRowStatus": snmpTrapHostRowStatus,
       "snmpv3UserTable": snmpv3UserTable,
       "snmpv3UserEntry": snmpv3UserEntry,
       "snmpv3UserIndex": snmpv3UserIndex,
       "snmpv3UserName": snmpv3UserName,
       "snmpv3UserAccessRight": snmpv3UserAccessRight,
       "snmpv3UserAuthProtocol": snmpv3UserAuthProtocol,
       "snmpv3UserAuthPassword": snmpv3UserAuthPassword,
       "snmpv3UserPrivProtocol": snmpv3UserPrivProtocol,
       "snmpv3UserPrivPassword": snmpv3UserPrivPassword,
       "snmpv3UserRowStatus": snmpv3UserRowStatus,
       "snmpv3EngineID": snmpv3EngineID,
       "poe": poe,
       "poeSystemSetting": poeSystemSetting,
       "poeFwVersion": poeFwVersion,
       "poeMaxPowerAvailable": poeMaxPowerAvailable,
       "poeActualPowerConsumption": poeActualPowerConsumption,
       "poeOverLoadDisconnect": poeOverLoadDisconnect,
       "poePortSettingTable": poePortSettingTable,
       "poePortSettingEntry": poePortSettingEntry,
       "poePortIndex": poePortIndex,
       "poePortState": poePortState,
       "poePortLegacy": poePortLegacy,
       "poePortPowerLimitClass": poePortPowerLimitClass,
       "poePortPriority": poePortPriority,
       "poePortPowerLimit": poePortPowerLimit,
       "poePortStatusTable": poePortStatusTable,
       "poePortStatusEntry": poePortStatusEntry,
       "poePortStatusIndex": poePortStatusIndex,
       "poePortCurrent": poePortCurrent,
       "poePortVoltage": poePortVoltage,
       "poePortPower": poePortPower,
       "poePortTemp": poePortTemp,
       "tcpModbus": tcpModbus,
       "tcpModbusState": tcpModbusState,
       "tcpModbusTimeout": tcpModbusTimeout,
       "dhcpServer": dhcpServer,
       "dhcpServerState": dhcpServerState,
       "dhcpServerGlobalSetting": dhcpServerGlobalSetting,
       "dhcpServerLeaseTime": dhcpServerLeaseTime,
       "dhcpServerLowIP": dhcpServerLowIP,
       "dhcpServerHighIP": dhcpServerHighIP,
       "dhcpServerSubmask": dhcpServerSubmask,
       "dhcpServerGateway": dhcpServerGateway,
       "dhcpServerDNS": dhcpServerDNS,
       "dhcpServerStatus": dhcpServerStatus,
       "dhcpServerClearIpPool": dhcpServerClearIpPool,
       "dhcpServerPortTable": dhcpServerPortTable,
       "dhcpServerPortEntry": dhcpServerPortEntry,
       "dhcpServerPortIndex": dhcpServerPortIndex,
       "dhcpServerPortLowIP": dhcpServerPortLowIP,
       "dhcpServerPortHighIP": dhcpServerPortHighIP,
       "dhcpServerPortMask": dhcpServerPortMask,
       "dhcpServerPortGW": dhcpServerPortGW,
       "dhcpServerPortDNS": dhcpServerPortDNS,
       "dhcpServerPortStatus": dhcpServerPortStatus,
       "dhcpServerPortClear": dhcpServerPortClear,
       "dhcpServerOpt82Table": dhcpServerOpt82Table,
       "dhcpServerOpt82Entry": dhcpServerOpt82Entry,
       "dhcpServerOpt82Index": dhcpServerOpt82Index,
       "dhcpServerOpt82CircuitIDFormat": dhcpServerOpt82CircuitIDFormat,
       "dhcpServerOpt82CircuitID": dhcpServerOpt82CircuitID,
       "dhcpServerOpt82RemoteIDFormat": dhcpServerOpt82RemoteIDFormat,
       "dhcpServerOpt82RemoteID": dhcpServerOpt82RemoteID,
       "dhcpServerOpt82LowIP": dhcpServerOpt82LowIP,
       "dhcpServerOpt82HighIP": dhcpServerOpt82HighIP,
       "dhcpServerOpt82Mask": dhcpServerOpt82Mask,
       "dhcpServerOpt82GW": dhcpServerOpt82GW,
       "dhcpServerOpt82DNS": dhcpServerOpt82DNS,
       "dhcpServerOpt82Status": dhcpServerOpt82Status,
       "dhcpServerOpt82Clear": dhcpServerOpt82Clear,
       "dhcpServerLeaseTable": dhcpServerLeaseTable,
       "dhcpServerLeaseEntry": dhcpServerLeaseEntry,
       "dhcpServerLeaseIndex": dhcpServerLeaseIndex,
       "dhcpServerLeaseIp": dhcpServerLeaseIp,
       "dhcpServerLeaseClientMac": dhcpServerLeaseClientMac,
       "dhcpServerLeaseStartTime": dhcpServerLeaseStartTime,
       "dhcpServerLeaseEndTime": dhcpServerLeaseEndTime,
       "dhcpServerLeaseType": dhcpServerLeaseType,
       "dhcpServerRestart": dhcpServerRestart,
       "dhcpServerVlanTable": dhcpServerVlanTable,
       "dhcpServerVlanEntry": dhcpServerVlanEntry,
       "dhcpServerVlanIndex": dhcpServerVlanIndex,
       "dhcpServerVlanId": dhcpServerVlanId,
       "dhcpServerVlanLowIP": dhcpServerVlanLowIP,
       "dhcpServerVlanHighIP": dhcpServerVlanHighIP,
       "dhcpServerVlanMask": dhcpServerVlanMask,
       "dhcpServerVlanGW": dhcpServerVlanGW,
       "dhcpServerVlanDNS": dhcpServerVlanDNS,
       "dhcpServerVlanStatus": dhcpServerVlanStatus,
       "dhcpServerVlanClear": dhcpServerVlanClear,
       "dhcpServerClientMacTable": dhcpServerClientMacTable,
       "dhcpServerClientMacEntry": dhcpServerClientMacEntry,
       "dhcpServerClientMacEntryID": dhcpServerClientMacEntryID,
       "dhcpServerClientMacEntryMac": dhcpServerClientMacEntryMac,
       "dhcpServerClientMacEntryIP": dhcpServerClientMacEntryIP,
       "dhcpServerClientMacEntryMask": dhcpServerClientMacEntryMask,
       "dhcpServerClientMacEntryGW": dhcpServerClientMacEntryGW,
       "dhcpServerClientMacEntryDNS": dhcpServerClientMacEntryDNS,
       "dhcpServerClientMacEntryRowStatus": dhcpServerClientMacEntryRowStatus,
       "smtpClient": smtpClient,
       "smtpActiveProfile": smtpActiveProfile,
       "smtpProfileTable": smtpProfileTable,
       "smtpProfileEntry": smtpProfileEntry,
       "smtpProfileIndex": smtpProfileIndex,
       "smtpServerIp": smtpServerIp,
       "smtpServerPort": smtpServerPort,
       "smtpSenderMail": smtpSenderMail,
       "smtpTargetMail1": smtpTargetMail1,
       "smtpTargetMail2": smtpTargetMail2,
       "smtpTargetMail3": smtpTargetMail3,
       "smtpTargetMail4": smtpTargetMail4,
       "smtpTargetMail5": smtpTargetMail5,
       "smtpTargetMail6": smtpTargetMail6,
       "smtpTargetMail7": smtpTargetMail7,
       "smtpTargetMail8": smtpTargetMail8,
       "rmon": rmon,
       "rmonStatisticsTable": rmonStatisticsTable,
       "rmonStatisticsEntry": rmonStatisticsEntry,
       "rmonStatisticsIndex": rmonStatisticsIndex,
       "rmonStatisticsPort": rmonStatisticsPort,
       "rmonStatisticsDropEvents": rmonStatisticsDropEvents,
       "rmonStatisticsOctets": rmonStatisticsOctets,
       "rmonStatisticsPackets": rmonStatisticsPackets,
       "rmonStatisticsBroadcast": rmonStatisticsBroadcast,
       "rmonStatisticsMulticast": rmonStatisticsMulticast,
       "rmonStatisticsOwner": rmonStatisticsOwner,
       "rmonStatisticsRowStatus": rmonStatisticsRowStatus,
       "rmonHistoryTable": rmonHistoryTable,
       "rmonHistoryEntry": rmonHistoryEntry,
       "rmonHistoryIndex": rmonHistoryIndex,
       "rmonHistoryPort": rmonHistoryPort,
       "rmonHistoryBucketsRequest": rmonHistoryBucketsRequest,
       "rmonHistoryInterval": rmonHistoryInterval,
       "rmonHistoryOwner": rmonHistoryOwner,
       "rmonHistoryRowStatus": rmonHistoryRowStatus,
       "rmonAlarmTable": rmonAlarmTable,
       "rmonAlarmEntry": rmonAlarmEntry,
       "rmonAlarmIndex": rmonAlarmIndex,
       "rmonAlarmInterval": rmonAlarmInterval,
       "rmonAlarmVariable": rmonAlarmVariable,
       "rmonAlarmSampleType": rmonAlarmSampleType,
       "rmonAlarmRisingThreshold": rmonAlarmRisingThreshold,
       "rmonAlarmFallingThreshold": rmonAlarmFallingThreshold,
       "rmonAlarmRisingEventIndex": rmonAlarmRisingEventIndex,
       "rmonAlarmFallingEventIndex": rmonAlarmFallingEventIndex,
       "rmonAlarmOwner": rmonAlarmOwner,
       "rmonAlarmRowStatus": rmonAlarmRowStatus,
       "rmonEventTable": rmonEventTable,
       "rmonEventEntry": rmonEventEntry,
       "rmonEventIndex": rmonEventIndex,
       "rmonEventDescription": rmonEventDescription,
       "rmonEventType": rmonEventType,
       "rmonEventCommunity": rmonEventCommunity,
       "rmonEventOwner": rmonEventOwner,
       "rmonEventRowStatus": rmonEventRowStatus,
       "ntp": ntp,
       "ntpServer": ntpServer,
       "ntpManualTime": ntpManualTime,
       "ntpServerTable": ntpServerTable,
       "ntpServerEntry": ntpServerEntry,
       "ntpServerIndex": ntpServerIndex,
       "ntpServerIp": ntpServerIp,
       "diagnostics": diagnostics,
       "copperTest": copperTest,
       "portNumber": portNumber,
       "copperTestAction": copperTestAction,
       "copperTestResult": copperTestResult,
       "resultPort": resultPort,
       "channelA": channelA,
       "cableLengthA": cableLengthA,
       "channelB": channelB,
       "cableLengthB": cableLengthB,
       "channelC": channelC,
       "cableLengthC": cableLengthC,
       "channelD": channelD,
       "cableLengthD": cableLengthD,
       "channelRx": channelRx,
       "cableLengthRx": cableLengthRx,
       "channelTx": channelTx,
       "cableLengthTx": cableLengthTx,
       "pingTest": pingTest,
       "pingIPAddress": pingIPAddress,
       "pingCount": pingCount,
       "pingInterval": pingInterval,
       "pingSize": pingSize,
       "pingAction": pingAction,
       "pingResult": pingResult,
       "ipv6pingTest": ipv6pingTest,
       "pingIPv6Address": pingIPv6Address,
       "pingIPv6Count": pingIPv6Count,
       "pingIPv6Interval": pingIPv6Interval,
       "pingIPv6Size": pingIPv6Size,
       "pingIPv6Action": pingIPv6Action,
       "pingIPv6Result": pingIPv6Result,
       "loggingSetting": loggingSetting,
       "loggingService": loggingService,
       "localLoggingTable": localLoggingTable,
       "localLoggingEntry": localLoggingEntry,
       "localLoggingIndex": localLoggingIndex,
       "bufferedtarget": bufferedtarget,
       "localLoggingStatus": localLoggingStatus,
       "localLoggingSeverity": localLoggingSeverity,
       "remoteloggingTable": remoteloggingTable,
       "remoteloggingEntry": remoteloggingEntry,
       "remoteloggingIndex": remoteloggingIndex,
       "remoteloggingAddress": remoteloggingAddress,
       "remoteloggingPort": remoteloggingPort,
       "remoteloggingSeverity": remoteloggingSeverity,
       "remoteloggingFacility": remoteloggingFacility,
       "remoteloggingRowStatus": remoteloggingRowStatus,
       "factoryDefault": factoryDefault,
       "factoryDefaultAction": factoryDefaultAction,
       "factoryDefaultKeepFlag": factoryDefaultKeepFlag,
       "reboot": reboot,
       "rebootAction": rebootAction,
       "dhcpAutoProvision": dhcpAutoProvision,
       "dhcpAutoProvisionEnable": dhcpAutoProvisionEnable,
       "ledIndication": ledIndication,
       "ledAlarmState": ledAlarmState,
       "ledPowerFailureEvent": ledPowerFailureEvent,
       "ledFiberLinkdownEvent": ledFiberLinkdownEvent,
       "ledPortLinkdownEvent": ledPortLinkdownEvent,
       "ledPortLinkdownEventPort": ledPortLinkdownEventPort,
       "ledEventInfoTable": ledEventInfoTable,
       "ledEventInfoEntry": ledEventInfoEntry,
       "ledEventIndex": ledEventIndex,
       "ledType": ledType,
       "ledEvent": ledEvent,
       "ledState": ledState,
       "ledErrorTimes": ledErrorTimes,
       "maintenance": maintenance,
       "backupManager": backupManager,
       "backupMethod": backupMethod,
       "backupServerIP": backupServerIP,
       "backupType": backupType,
       "backupImage": backupImage,
       "backupAction": backupAction,
       "upgradeManager": upgradeManager,
       "upgradeMethod": upgradeMethod,
       "upgradeServerIP": upgradeServerIP,
       "upgradeFileName": upgradeFileName,
       "upgradeType": upgradeType,
       "upgradeImage": upgradeImage,
       "upgradeAction": upgradeAction,
       "upgradeStatus": upgradeStatus,
       "dualImage": dualImage,
       "activeImage": activeImage,
       "imageInfoTable": imageInfoTable,
       "imageInfoEntry": imageInfoEntry,
       "flashPartition": flashPartition,
       "imageName": imageName,
       "imageSize": imageSize,
       "createdTime": createdTime,
       "imageVersion": imageVersion,
       "configurationManager": configurationManager,
       "sourceFile": sourceFile,
       "destinationFile": destinationFile,
       "saveConfiguration": saveConfiguration,
       "accountManager": accountManager,
       "localUserTable": localUserTable,
       "localUserEntry": localUserEntry,
       "localUserIndex": localUserIndex,
       "localUserName": localUserName,
       "localUserPasswordType": localUserPasswordType,
       "localUserPassword": localUserPassword,
       "localUserPrivilegeType": localUserPrivilegeType,
       "localUserRowStatus": localUserRowStatus,
       "nKey": nKey,
       "nKeyAutoMode": nKeyAutoMode,
       "nKeyStatus": nKeyStatus,
       "traps": traps,
       "trapObject": trapObject,
       "ddmiAlarmDescr": ddmiAlarmDescr,
       "xRingMasterStatus": xRingMasterStatus,
       "ddmiAlarmWarning": ddmiAlarmWarning,
       "xRingProMasterChange": xRingProMasterChange,
       "stpStateChange": stpStateChange}
)
