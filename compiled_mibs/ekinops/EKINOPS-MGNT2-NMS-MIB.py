# SNMP MIB module (EKINOPS-MGNT2-NMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ekinops\EKINOPS-MGNT2-NMS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:13 2025
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

(EkiOnOff,
 ekinops) = mibBuilder.importSymbols(
    "EKINOPS-MIB",
    "EkiOnOff",
    "ekinops")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(SnmpUDPAddress,) = mibBuilder.importSymbols(
    "SNMPv2-TM",
    "SnmpUDPAddress")


# MODULE-IDENTITY

mgnt2NMS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 1000)
)
if mibBuilder.loadTexts:
    mgnt2NMS.setRevisions(
        ("2009-07-26 15:00",
         "2015-04-13 00:00",
         "2015-11-12 00:00",
         "2016-06-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Mgnt2NotificationId(TextualConvention, Counter32):
    status = "current"


class Mgnt2AlmProbableCause(TextualConvention, Integer32):
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
              1000)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("adapterError", 2),
          ("applicationSubsystemFailure", 3),
          ("bandwidthReduced", 4),
          ("callEstablishmentError", 5),
          ("communicationsProtocolError", 6),
          ("communicationsSubsystemFailure", 7),
          ("configurationOrCustomizationError", 8),
          ("congestion", 9),
          ("corruptData", 10),
          ("cpuCyclesLimitExceeded", 11),
          ("dataSetOrModemError", 12),
          ("degradedSignal", 13),
          ("dteDceInterfaceError", 14),
          ("enclosureDoorOpen", 15),
          ("equipmentMalfunction", 16),
          ("excessiveVibration", 17),
          ("fileError", 18),
          ("fireDetected", 19),
          ("floodDetected", 20),
          ("framingError", 21),
          ("heatingVentCoolingSystemProblem", 22),
          ("humidityUnacceptable", 23),
          ("inputOutputDeviceError", 24),
          ("inputDeviceError", 25),
          ("lanError", 26),
          ("leakDetected", 27),
          ("localNodeTransmissionError", 28),
          ("lossOfFrame", 29),
          ("lossOfSignal", 30),
          ("materialSupplyExhausted", 31),
          ("multiplexerProblem", 32),
          ("outOfMemory", 33),
          ("ouputDeviceError", 34),
          ("performanceDegraded", 35),
          ("powerProblem", 36),
          ("pressureUnacceptable", 37),
          ("processorProblem", 38),
          ("pumpFailure", 39),
          ("queueSizeExceeded", 40),
          ("receiveFailure", 41),
          ("receiverFailure", 42),
          ("remoteNodeTransmissionError", 43),
          ("resourceAtOrNearingCapacity", 44),
          ("responseTimeExecessive", 45),
          ("retransmissionRateExcessive", 46),
          ("softwareError", 47),
          ("softwareProgramAbnormallyTerminated", 48),
          ("softwareProgramError", 49),
          ("storageCapacityProblem", 50),
          ("temperatureUnacceptable", 51),
          ("thresholdCrossed", 52),
          ("timingProblem", 53),
          ("toxicLeakDetected", 54),
          ("transmitFailure", 55),
          ("transmitterFailure", 56),
          ("underlyingResourceUnavailable", 57),
          ("versionMismatch", 58),
          ("authenticationFailure", 59),
          ("breachOfConfidentiality", 60),
          ("cableTamper", 61),
          ("delayedInformation", 62),
          ("denialOfService", 63),
          ("duplicateInformation", 64),
          ("informationMissing", 65),
          ("informationModificationDetected", 66),
          ("informationOutOfSequence", 67),
          ("intrusionDetection", 68),
          ("keyExpired", 69),
          ("nonRepudiationFailure", 70),
          ("outOfHoursActivity", 71),
          ("outOfService", 72),
          ("proceduralError", 73),
          ("unauthorizedAccessAttempt", 74),
          ("unexpectedInformation", 75),
          ("informationalStatus", 1000))
    )



class Mgnt2ObjectClassId(TextualConvention, Integer32):
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
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("chassis", 3),
          ("backplane", 4),
          ("container", 5),
          ("powerSupply", 6),
          ("fan", 7),
          ("sensor", 8),
          ("module", 9),
          ("port", 10),
          ("stack", 11),
          ("cpu", 12),
          ("mgnt", 13))
    )



class Mgnt2AlmSeverity(TextualConvention, Integer32):
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("indeterminate", 5),
          ("cleared", 6))
    )



class Mgnt2AlmType(TextualConvention, Integer32):
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
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("communicationsAlarm", 2),
          ("qualityOfServiceAlarm", 3),
          ("processingErrorAlarm", 4),
          ("equipmentAlarm", 5),
          ("environmentalAlarm", 6),
          ("integrityViolation", 7),
          ("operationalViolation", 8),
          ("physicalViolation", 9),
          ("securityServiceOrMechanismViolation", 10),
          ("timeDomainViolation", 11),
          ("synthesisAlarm", 12))
    )



class Mgnt2EventType(TextualConvention, Integer32):
    status = "current"
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
        *(("objectCreation", 1),
          ("objectDeletion", 2),
          ("attributeValueChange", 3),
          ("stateChange", 4),
          ("activityLog", 5))
    )



class Mgnt2EventSourceType(TextualConvention, Integer32):
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
        *(("event", 1),
          ("control", 2),
          ("config", 3))
    )



class Mgnt2LacState(TextualConvention, Integer32):
    status = "current"
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
        *(("accessDenied", 0),
          ("accessRequested", 1),
          ("accessGrantedCraft", 2),
          ("accessGrantedCli", 3),
          ("accessGrantedSnmp", 4))
    )



class Mgnt2ServerAddress(TextualConvention, OctetString):
    status = "current"


class Mgnt2UploadDownloadFileEncoding(TextualConvention, Integer32):
    status = "current"
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
        *(("other", 1),
          ("ascii", 2),
          ("xml", 3),
          ("bin", 4),
          ("data", 5))
    )



class Mgnt2UploadDownloadFileCompression(TextualConvention, Integer32):
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
        *(("noCompression", 1),
          ("bzip", 2),
          ("gzip", 3))
    )



class Mgnt2UploadDownloadActionStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("success", 0),
          ("start", 1),
          ("inProgress", 2),
          ("failed", 3),
          ("automatic", 4),
          ("abort", 5))
    )



class Mgnt2UploadDownloadErrorCode(TextualConvention, Integer32):
    status = "current"
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("missingLogin", 1),
          ("missingPassword", 2),
          ("missingFile", 3),
          ("serverUnreachable", 4),
          ("badPassword", 5),
          ("noSpaceLeft", 6),
          ("corruptedFile", 7),
          ("canceled", 8),
          ("noWriteAccess", 9),
          ("undefinedError", 10),
          ("accessViolation", 11),
          ("fileExist", 12),
          ("wrongDirection", 13),
          ("wrongName", 14),
          ("wrongCompression", 15))
    )



class Mgnt2SoftwareDownloadActionStatus(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("missingLogin", 1),
          ("missingPassword", 2),
          ("missingFile", 3),
          ("serverUnreachable", 4),
          ("badPassword", 5),
          ("noSpaceLeft", 6),
          ("corruptedFile", 7),
          ("canceled", 8),
          ("noWriteAccess", 9))
    )



class Mgnt2DownloadFileType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("pmPackage", 0),
          ("mgntPackage", 1),
          ("configurationFile", 2),
          ("logFile", 3),
          ("perfFile", 4),
          ("wavePlan", 5),
          ("adminPackage", 6))
    )



# MIB Managed Objects in the order of their OIDs

_Mgnt2NMSMibObject_ObjectIdentity = ObjectIdentity
mgnt2NMSMibObject = _Mgnt2NMSMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1)
)
_Mgnt2ActiveAlmTable_Object = MibTable
mgnt2ActiveAlmTable = _Mgnt2ActiveAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1)
)
if mibBuilder.loadTexts:
    mgnt2ActiveAlmTable.setStatus("current")
_Mgnt2ActiveAlmEntry_Object = MibTableRow
mgnt2ActiveAlmEntry = _Mgnt2ActiveAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1)
)
mgnt2ActiveAlmEntry.setIndexNames(
    (0, "EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmNotificationId"),
)
if mibBuilder.loadTexts:
    mgnt2ActiveAlmEntry.setStatus("current")
_Mgnt2ActiveAlmNotificationId_Type = Mgnt2NotificationId
_Mgnt2ActiveAlmNotificationId_Object = MibTableColumn
mgnt2ActiveAlmNotificationId = _Mgnt2ActiveAlmNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 1),
    _Mgnt2ActiveAlmNotificationId_Type()
)
mgnt2ActiveAlmNotificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ActiveAlmNotificationId.setStatus("current")
_Mgnt2ActiveAlmProbableCause_Type = Mgnt2AlmProbableCause
_Mgnt2ActiveAlmProbableCause_Object = MibTableColumn
mgnt2ActiveAlmProbableCause = _Mgnt2ActiveAlmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 2),
    _Mgnt2ActiveAlmProbableCause_Type()
)
mgnt2ActiveAlmProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ActiveAlmProbableCause.setStatus("current")
_Mgnt2ActiveAlmObjectClassIdentifier_Type = Mgnt2ObjectClassId
_Mgnt2ActiveAlmObjectClassIdentifier_Object = MibTableColumn
mgnt2ActiveAlmObjectClassIdentifier = _Mgnt2ActiveAlmObjectClassIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 3),
    _Mgnt2ActiveAlmObjectClassIdentifier_Type()
)
mgnt2ActiveAlmObjectClassIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ActiveAlmObjectClassIdentifier.setStatus("current")
_Mgnt2ActiveAlmSourcePm_Type = DisplayString
_Mgnt2ActiveAlmSourcePm_Object = MibTableColumn
mgnt2ActiveAlmSourcePm = _Mgnt2ActiveAlmSourcePm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 4),
    _Mgnt2ActiveAlmSourcePm_Type()
)
mgnt2ActiveAlmSourcePm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ActiveAlmSourcePm.setStatus("current")


class _Mgnt2ActiveAlmBoardNumber_Type(Integer32):
    """Custom type mgnt2ActiveAlmBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgnt2ActiveAlmBoardNumber_Type.__name__ = "Integer32"
_Mgnt2ActiveAlmBoardNumber_Object = MibTableColumn
mgnt2ActiveAlmBoardNumber = _Mgnt2ActiveAlmBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 5),
    _Mgnt2ActiveAlmBoardNumber_Type()
)
mgnt2ActiveAlmBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ActiveAlmBoardNumber.setStatus("current")
_Mgnt2ActiveAlmSourcePortType_Type = DisplayString
_Mgnt2ActiveAlmSourcePortType_Object = MibTableColumn
mgnt2ActiveAlmSourcePortType = _Mgnt2ActiveAlmSourcePortType_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 6),
    _Mgnt2ActiveAlmSourcePortType_Type()
)
mgnt2ActiveAlmSourcePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ActiveAlmSourcePortType.setStatus("current")


class _Mgnt2ActiveAlmSourcePortNumber_Type(Integer32):
    """Custom type mgnt2ActiveAlmSourcePortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgnt2ActiveAlmSourcePortNumber_Type.__name__ = "Integer32"
_Mgnt2ActiveAlmSourcePortNumber_Object = MibTableColumn
mgnt2ActiveAlmSourcePortNumber = _Mgnt2ActiveAlmSourcePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 7),
    _Mgnt2ActiveAlmSourcePortNumber_Type()
)
mgnt2ActiveAlmSourcePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ActiveAlmSourcePortNumber.setStatus("current")
_Mgnt2ActiveAlmSeverity_Type = Mgnt2AlmSeverity
_Mgnt2ActiveAlmSeverity_Object = MibTableColumn
mgnt2ActiveAlmSeverity = _Mgnt2ActiveAlmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 8),
    _Mgnt2ActiveAlmSeverity_Type()
)
mgnt2ActiveAlmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ActiveAlmSeverity.setStatus("current")
_Mgnt2ActiveAlmSpecificProblem_Type = DisplayString
_Mgnt2ActiveAlmSpecificProblem_Object = MibTableColumn
mgnt2ActiveAlmSpecificProblem = _Mgnt2ActiveAlmSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 9),
    _Mgnt2ActiveAlmSpecificProblem_Type()
)
mgnt2ActiveAlmSpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ActiveAlmSpecificProblem.setStatus("current")
_Mgnt2ActiveAlmAdditionalText_Type = DisplayString
_Mgnt2ActiveAlmAdditionalText_Object = MibTableColumn
mgnt2ActiveAlmAdditionalText = _Mgnt2ActiveAlmAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 10),
    _Mgnt2ActiveAlmAdditionalText_Type()
)
mgnt2ActiveAlmAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ActiveAlmAdditionalText.setStatus("current")
_Mgnt2ActiveAlmType_Type = Mgnt2AlmType
_Mgnt2ActiveAlmType_Object = MibTableColumn
mgnt2ActiveAlmType = _Mgnt2ActiveAlmType_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 11),
    _Mgnt2ActiveAlmType_Type()
)
mgnt2ActiveAlmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ActiveAlmType.setStatus("current")
_Mgnt2ActiveAlmTime_Type = DateAndTime
_Mgnt2ActiveAlmTime_Object = MibTableColumn
mgnt2ActiveAlmTime = _Mgnt2ActiveAlmTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 12),
    _Mgnt2ActiveAlmTime_Type()
)
mgnt2ActiveAlmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ActiveAlmTime.setStatus("current")
_Mgnt2ActiveAlmNodeControllerIpAddress_Type = IpAddress
_Mgnt2ActiveAlmNodeControllerIpAddress_Object = MibTableColumn
mgnt2ActiveAlmNodeControllerIpAddress = _Mgnt2ActiveAlmNodeControllerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 13),
    _Mgnt2ActiveAlmNodeControllerIpAddress_Type()
)
mgnt2ActiveAlmNodeControllerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ActiveAlmNodeControllerIpAddress.setStatus("current")
_Mgnt2ActiveAlmChassisId_Type = DisplayString
_Mgnt2ActiveAlmChassisId_Object = MibTableColumn
mgnt2ActiveAlmChassisId = _Mgnt2ActiveAlmChassisId_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 14),
    _Mgnt2ActiveAlmChassisId_Type()
)
mgnt2ActiveAlmChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ActiveAlmChassisId.setStatus("current")
_Mgnt2AlmLogTable_Object = MibTable
mgnt2AlmLogTable = _Mgnt2AlmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2)
)
if mibBuilder.loadTexts:
    mgnt2AlmLogTable.setStatus("current")
_Mgnt2AlmLogEntry_Object = MibTableRow
mgnt2AlmLogEntry = _Mgnt2AlmLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1)
)
mgnt2AlmLogEntry.setIndexNames(
    (0, "EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogNotificationId"),
)
if mibBuilder.loadTexts:
    mgnt2AlmLogEntry.setStatus("current")
_Mgnt2AlmLogNotificationId_Type = Mgnt2NotificationId
_Mgnt2AlmLogNotificationId_Object = MibTableColumn
mgnt2AlmLogNotificationId = _Mgnt2AlmLogNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 1),
    _Mgnt2AlmLogNotificationId_Type()
)
mgnt2AlmLogNotificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmLogNotificationId.setStatus("current")
_Mgnt2AlmLogProbableCause_Type = Mgnt2AlmProbableCause
_Mgnt2AlmLogProbableCause_Object = MibTableColumn
mgnt2AlmLogProbableCause = _Mgnt2AlmLogProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 2),
    _Mgnt2AlmLogProbableCause_Type()
)
mgnt2AlmLogProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmLogProbableCause.setStatus("current")
_Mgnt2AlmLogObjectClassIdentifier_Type = Mgnt2ObjectClassId
_Mgnt2AlmLogObjectClassIdentifier_Object = MibTableColumn
mgnt2AlmLogObjectClassIdentifier = _Mgnt2AlmLogObjectClassIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 3),
    _Mgnt2AlmLogObjectClassIdentifier_Type()
)
mgnt2AlmLogObjectClassIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmLogObjectClassIdentifier.setStatus("current")
_Mgnt2AlmLogSourcePm_Type = DisplayString
_Mgnt2AlmLogSourcePm_Object = MibTableColumn
mgnt2AlmLogSourcePm = _Mgnt2AlmLogSourcePm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 4),
    _Mgnt2AlmLogSourcePm_Type()
)
mgnt2AlmLogSourcePm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmLogSourcePm.setStatus("current")


class _Mgnt2AlmLogBoardNumber_Type(Integer32):
    """Custom type mgnt2AlmLogBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgnt2AlmLogBoardNumber_Type.__name__ = "Integer32"
_Mgnt2AlmLogBoardNumber_Object = MibTableColumn
mgnt2AlmLogBoardNumber = _Mgnt2AlmLogBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 5),
    _Mgnt2AlmLogBoardNumber_Type()
)
mgnt2AlmLogBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmLogBoardNumber.setStatus("current")
_Mgnt2AlmLogSourcePortType_Type = DisplayString
_Mgnt2AlmLogSourcePortType_Object = MibTableColumn
mgnt2AlmLogSourcePortType = _Mgnt2AlmLogSourcePortType_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 6),
    _Mgnt2AlmLogSourcePortType_Type()
)
mgnt2AlmLogSourcePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmLogSourcePortType.setStatus("current")


class _Mgnt2AlmLogSourcePortNumber_Type(Integer32):
    """Custom type mgnt2AlmLogSourcePortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgnt2AlmLogSourcePortNumber_Type.__name__ = "Integer32"
_Mgnt2AlmLogSourcePortNumber_Object = MibTableColumn
mgnt2AlmLogSourcePortNumber = _Mgnt2AlmLogSourcePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 7),
    _Mgnt2AlmLogSourcePortNumber_Type()
)
mgnt2AlmLogSourcePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmLogSourcePortNumber.setStatus("current")
_Mgnt2AlmLogSeverity_Type = Mgnt2AlmSeverity
_Mgnt2AlmLogSeverity_Object = MibTableColumn
mgnt2AlmLogSeverity = _Mgnt2AlmLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 8),
    _Mgnt2AlmLogSeverity_Type()
)
mgnt2AlmLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmLogSeverity.setStatus("current")
_Mgnt2AlmLogSpecificProblem_Type = DisplayString
_Mgnt2AlmLogSpecificProblem_Object = MibTableColumn
mgnt2AlmLogSpecificProblem = _Mgnt2AlmLogSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 9),
    _Mgnt2AlmLogSpecificProblem_Type()
)
mgnt2AlmLogSpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmLogSpecificProblem.setStatus("current")
_Mgnt2AlmLogAdditionalText_Type = DisplayString
_Mgnt2AlmLogAdditionalText_Object = MibTableColumn
mgnt2AlmLogAdditionalText = _Mgnt2AlmLogAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 10),
    _Mgnt2AlmLogAdditionalText_Type()
)
mgnt2AlmLogAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmLogAdditionalText.setStatus("current")
_Mgnt2AlmLogAlarmType_Type = Mgnt2AlmType
_Mgnt2AlmLogAlarmType_Object = MibTableColumn
mgnt2AlmLogAlarmType = _Mgnt2AlmLogAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 11),
    _Mgnt2AlmLogAlarmType_Type()
)
mgnt2AlmLogAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmLogAlarmType.setStatus("current")
_Mgnt2AlmLogTime_Type = DateAndTime
_Mgnt2AlmLogTime_Object = MibTableColumn
mgnt2AlmLogTime = _Mgnt2AlmLogTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 13),
    _Mgnt2AlmLogTime_Type()
)
mgnt2AlmLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmLogTime.setStatus("current")
_Mgnt2AlmLogNodeControllerIpAddress_Type = IpAddress
_Mgnt2AlmLogNodeControllerIpAddress_Object = MibTableColumn
mgnt2AlmLogNodeControllerIpAddress = _Mgnt2AlmLogNodeControllerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 14),
    _Mgnt2AlmLogNodeControllerIpAddress_Type()
)
mgnt2AlmLogNodeControllerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmLogNodeControllerIpAddress.setStatus("current")
_Mgnt2AlmLogChassisId_Type = DisplayString
_Mgnt2AlmLogChassisId_Object = MibTableColumn
mgnt2AlmLogChassisId = _Mgnt2AlmLogChassisId_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 15),
    _Mgnt2AlmLogChassisId_Type()
)
mgnt2AlmLogChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmLogChassisId.setStatus("current")
_Mgnt2EventLogTable_Object = MibTable
mgnt2EventLogTable = _Mgnt2EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3)
)
if mibBuilder.loadTexts:
    mgnt2EventLogTable.setStatus("current")
_Mgnt2EventLogEntry_Object = MibTableRow
mgnt2EventLogEntry = _Mgnt2EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1)
)
mgnt2EventLogEntry.setIndexNames(
    (0, "EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogNotificationId"),
)
if mibBuilder.loadTexts:
    mgnt2EventLogEntry.setStatus("current")
_Mgnt2EventLogNotificationId_Type = Mgnt2NotificationId
_Mgnt2EventLogNotificationId_Object = MibTableColumn
mgnt2EventLogNotificationId = _Mgnt2EventLogNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 1),
    _Mgnt2EventLogNotificationId_Type()
)
mgnt2EventLogNotificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2EventLogNotificationId.setStatus("current")
_Mgnt2EventLogObjectClassIdentifier_Type = Mgnt2ObjectClassId
_Mgnt2EventLogObjectClassIdentifier_Object = MibTableColumn
mgnt2EventLogObjectClassIdentifier = _Mgnt2EventLogObjectClassIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 2),
    _Mgnt2EventLogObjectClassIdentifier_Type()
)
mgnt2EventLogObjectClassIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2EventLogObjectClassIdentifier.setStatus("current")
_Mgnt2EventLogSourcePm_Type = DisplayString
_Mgnt2EventLogSourcePm_Object = MibTableColumn
mgnt2EventLogSourcePm = _Mgnt2EventLogSourcePm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 4),
    _Mgnt2EventLogSourcePm_Type()
)
mgnt2EventLogSourcePm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2EventLogSourcePm.setStatus("current")


class _Mgnt2EventLogBoardNumber_Type(Integer32):
    """Custom type mgnt2EventLogBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgnt2EventLogBoardNumber_Type.__name__ = "Integer32"
_Mgnt2EventLogBoardNumber_Object = MibTableColumn
mgnt2EventLogBoardNumber = _Mgnt2EventLogBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 5),
    _Mgnt2EventLogBoardNumber_Type()
)
mgnt2EventLogBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2EventLogBoardNumber.setStatus("current")
_Mgnt2EventLogSourcePortType_Type = DisplayString
_Mgnt2EventLogSourcePortType_Object = MibTableColumn
mgnt2EventLogSourcePortType = _Mgnt2EventLogSourcePortType_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 6),
    _Mgnt2EventLogSourcePortType_Type()
)
mgnt2EventLogSourcePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2EventLogSourcePortType.setStatus("current")


class _Mgnt2EventLogSourcePortNumber_Type(Integer32):
    """Custom type mgnt2EventLogSourcePortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgnt2EventLogSourcePortNumber_Type.__name__ = "Integer32"
_Mgnt2EventLogSourcePortNumber_Object = MibTableColumn
mgnt2EventLogSourcePortNumber = _Mgnt2EventLogSourcePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 7),
    _Mgnt2EventLogSourcePortNumber_Type()
)
mgnt2EventLogSourcePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2EventLogSourcePortNumber.setStatus("current")
_Mgnt2EventLogEventType_Type = Mgnt2EventType
_Mgnt2EventLogEventType_Object = MibTableColumn
mgnt2EventLogEventType = _Mgnt2EventLogEventType_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 8),
    _Mgnt2EventLogEventType_Type()
)
mgnt2EventLogEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2EventLogEventType.setStatus("current")
_Mgnt2EventLogSourceType_Type = Mgnt2EventSourceType
_Mgnt2EventLogSourceType_Object = MibTableColumn
mgnt2EventLogSourceType = _Mgnt2EventLogSourceType_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 9),
    _Mgnt2EventLogSourceType_Type()
)
mgnt2EventLogSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2EventLogSourceType.setStatus("current")
_Mgnt2EventLogReason_Type = DisplayString
_Mgnt2EventLogReason_Object = MibTableColumn
mgnt2EventLogReason = _Mgnt2EventLogReason_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 10),
    _Mgnt2EventLogReason_Type()
)
mgnt2EventLogReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2EventLogReason.setStatus("current")
_Mgnt2EventLogAdditionalText_Type = DisplayString
_Mgnt2EventLogAdditionalText_Object = MibTableColumn
mgnt2EventLogAdditionalText = _Mgnt2EventLogAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 11),
    _Mgnt2EventLogAdditionalText_Type()
)
mgnt2EventLogAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2EventLogAdditionalText.setStatus("current")
_Mgnt2EventLogTime_Type = DateAndTime
_Mgnt2EventLogTime_Object = MibTableColumn
mgnt2EventLogTime = _Mgnt2EventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 12),
    _Mgnt2EventLogTime_Type()
)
mgnt2EventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2EventLogTime.setStatus("current")
_Mgnt2EventLogNodeControllerIpAddress_Type = IpAddress
_Mgnt2EventLogNodeControllerIpAddress_Object = MibTableColumn
mgnt2EventLogNodeControllerIpAddress = _Mgnt2EventLogNodeControllerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 13),
    _Mgnt2EventLogNodeControllerIpAddress_Type()
)
mgnt2EventLogNodeControllerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2EventLogNodeControllerIpAddress.setStatus("current")
_Mgnt2EventLogChassisId_Type = DisplayString
_Mgnt2EventLogChassisId_Object = MibTableColumn
mgnt2EventLogChassisId = _Mgnt2EventLogChassisId_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 14),
    _Mgnt2EventLogChassisId_Type()
)
mgnt2EventLogChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2EventLogChassisId.setStatus("current")
_Mgnt2UploadDownload_ObjectIdentity = ObjectIdentity
mgnt2UploadDownload = _Mgnt2UploadDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5)
)
_Mgnt2UploadDownloadFilename_Type = DisplayString
_Mgnt2UploadDownloadFilename_Object = MibScalar
mgnt2UploadDownloadFilename = _Mgnt2UploadDownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 1),
    _Mgnt2UploadDownloadFilename_Type()
)
mgnt2UploadDownloadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2UploadDownloadFilename.setStatus("current")
_Mgnt2UploadDownloadAddress_Type = Mgnt2ServerAddress
_Mgnt2UploadDownloadAddress_Object = MibScalar
mgnt2UploadDownloadAddress = _Mgnt2UploadDownloadAddress_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 2),
    _Mgnt2UploadDownloadAddress_Type()
)
mgnt2UploadDownloadAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2UploadDownloadAddress.setStatus("current")
_Mgnt2UploadDownloadLogin_Type = DisplayString
_Mgnt2UploadDownloadLogin_Object = MibScalar
mgnt2UploadDownloadLogin = _Mgnt2UploadDownloadLogin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 3),
    _Mgnt2UploadDownloadLogin_Type()
)
mgnt2UploadDownloadLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2UploadDownloadLogin.setStatus("current")
_Mgnt2UploadDownloadPasswd_Type = DisplayString
_Mgnt2UploadDownloadPasswd_Object = MibScalar
mgnt2UploadDownloadPasswd = _Mgnt2UploadDownloadPasswd_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 4),
    _Mgnt2UploadDownloadPasswd_Type()
)
mgnt2UploadDownloadPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2UploadDownloadPasswd.setStatus("current")
_Mgnt2UploadDownloadTxRetries_Type = Integer32
_Mgnt2UploadDownloadTxRetries_Object = MibScalar
mgnt2UploadDownloadTxRetries = _Mgnt2UploadDownloadTxRetries_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 5),
    _Mgnt2UploadDownloadTxRetries_Type()
)
mgnt2UploadDownloadTxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2UploadDownloadTxRetries.setStatus("current")
_Mgnt2UploadDownloadActionStatus_Type = Mgnt2UploadDownloadActionStatus
_Mgnt2UploadDownloadActionStatus_Object = MibScalar
mgnt2UploadDownloadActionStatus = _Mgnt2UploadDownloadActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 6),
    _Mgnt2UploadDownloadActionStatus_Type()
)
mgnt2UploadDownloadActionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2UploadDownloadActionStatus.setStatus("current")
_Mgnt2UploadDownloadErrorCode_Type = Mgnt2UploadDownloadErrorCode
_Mgnt2UploadDownloadErrorCode_Object = MibScalar
mgnt2UploadDownloadErrorCode = _Mgnt2UploadDownloadErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 7),
    _Mgnt2UploadDownloadErrorCode_Type()
)
mgnt2UploadDownloadErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2UploadDownloadErrorCode.setStatus("current")
_Mgnt2UploadDownloadDirection_Type = Integer32
_Mgnt2UploadDownloadDirection_Object = MibScalar
mgnt2UploadDownloadDirection = _Mgnt2UploadDownloadDirection_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 8),
    _Mgnt2UploadDownloadDirection_Type()
)
mgnt2UploadDownloadDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2UploadDownloadDirection.setStatus("current")
_Mgnt2UploadDownloadProgress_Type = Integer32
_Mgnt2UploadDownloadProgress_Object = MibScalar
mgnt2UploadDownloadProgress = _Mgnt2UploadDownloadProgress_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 9),
    _Mgnt2UploadDownloadProgress_Type()
)
mgnt2UploadDownloadProgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2UploadDownloadProgress.setStatus("current")
_Mgnt2UploadDownloadReceivedFiles_Type = Integer32
_Mgnt2UploadDownloadReceivedFiles_Object = MibScalar
mgnt2UploadDownloadReceivedFiles = _Mgnt2UploadDownloadReceivedFiles_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 10),
    _Mgnt2UploadDownloadReceivedFiles_Type()
)
mgnt2UploadDownloadReceivedFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2UploadDownloadReceivedFiles.setStatus("current")
_Mgnt2UploadDownloadRemainingFiles_Type = Integer32
_Mgnt2UploadDownloadRemainingFiles_Object = MibScalar
mgnt2UploadDownloadRemainingFiles = _Mgnt2UploadDownloadRemainingFiles_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 11),
    _Mgnt2UploadDownloadRemainingFiles_Type()
)
mgnt2UploadDownloadRemainingFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2UploadDownloadRemainingFiles.setStatus("current")
_Mgnt2UploadDownloadFileType_Type = Mgnt2DownloadFileType
_Mgnt2UploadDownloadFileType_Object = MibScalar
mgnt2UploadDownloadFileType = _Mgnt2UploadDownloadFileType_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 12),
    _Mgnt2UploadDownloadFileType_Type()
)
mgnt2UploadDownloadFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2UploadDownloadFileType.setStatus("current")
_Mgnt2UploadDownloadFileCompression_Type = Mgnt2UploadDownloadFileCompression
_Mgnt2UploadDownloadFileCompression_Object = MibScalar
mgnt2UploadDownloadFileCompression = _Mgnt2UploadDownloadFileCompression_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 13),
    _Mgnt2UploadDownloadFileCompression_Type()
)
mgnt2UploadDownloadFileCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2UploadDownloadFileCompression.setStatus("current")
_Mgnt2UploadDownloadDeleteLastFile_Type = EkiOnOff
_Mgnt2UploadDownloadDeleteLastFile_Object = MibScalar
mgnt2UploadDownloadDeleteLastFile = _Mgnt2UploadDownloadDeleteLastFile_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 14),
    _Mgnt2UploadDownloadDeleteLastFile_Type()
)
mgnt2UploadDownloadDeleteLastFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2UploadDownloadDeleteLastFile.setStatus("current")
_Mgnt2Configuration_ObjectIdentity = ObjectIdentity
mgnt2Configuration = _Mgnt2Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 6)
)
_Mgnt2ConfigurationChecksum_Type = DisplayString
_Mgnt2ConfigurationChecksum_Object = MibScalar
mgnt2ConfigurationChecksum = _Mgnt2ConfigurationChecksum_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 6, 1),
    _Mgnt2ConfigurationChecksum_Type()
)
mgnt2ConfigurationChecksum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgnt2ConfigurationChecksum.setStatus("deprecated")
_Mgnt2ConfigurationActionStatus_Type = Integer32
_Mgnt2ConfigurationActionStatus_Object = MibScalar
mgnt2ConfigurationActionStatus = _Mgnt2ConfigurationActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 6, 2),
    _Mgnt2ConfigurationActionStatus_Type()
)
mgnt2ConfigurationActionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2ConfigurationActionStatus.setStatus("current")
_Mgnt2ConfigurationActivationErrorCode_Type = Integer32
_Mgnt2ConfigurationActivationErrorCode_Object = MibScalar
mgnt2ConfigurationActivationErrorCode = _Mgnt2ConfigurationActivationErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 6, 3),
    _Mgnt2ConfigurationActivationErrorCode_Type()
)
mgnt2ConfigurationActivationErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ConfigurationActivationErrorCode.setStatus("current")
_Mgnt2ConfigurationActivationErrorString_Type = DisplayString
_Mgnt2ConfigurationActivationErrorString_Object = MibScalar
mgnt2ConfigurationActivationErrorString = _Mgnt2ConfigurationActivationErrorString_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 6, 4),
    _Mgnt2ConfigurationActivationErrorString_Type()
)
mgnt2ConfigurationActivationErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ConfigurationActivationErrorString.setStatus("current")
_Mgnt2SoftwareDownload_ObjectIdentity = ObjectIdentity
mgnt2SoftwareDownload = _Mgnt2SoftwareDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 7)
)
_Mgnt2SoftwareDownloadActionStatus_Type = Integer32
_Mgnt2SoftwareDownloadActionStatus_Object = MibScalar
mgnt2SoftwareDownloadActionStatus = _Mgnt2SoftwareDownloadActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 7, 2),
    _Mgnt2SoftwareDownloadActionStatus_Type()
)
mgnt2SoftwareDownloadActionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2SoftwareDownloadActionStatus.setStatus("current")
_Mgnt2SoftwareDownloadActivationErrorCode_Type = Integer32
_Mgnt2SoftwareDownloadActivationErrorCode_Object = MibScalar
mgnt2SoftwareDownloadActivationErrorCode = _Mgnt2SoftwareDownloadActivationErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 7, 3),
    _Mgnt2SoftwareDownloadActivationErrorCode_Type()
)
mgnt2SoftwareDownloadActivationErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2SoftwareDownloadActivationErrorCode.setStatus("current")
_Mgnt2SoftwareDownloadActivationErrorString_Type = DisplayString
_Mgnt2SoftwareDownloadActivationErrorString_Object = MibScalar
mgnt2SoftwareDownloadActivationErrorString = _Mgnt2SoftwareDownloadActivationErrorString_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 7, 4),
    _Mgnt2SoftwareDownloadActivationErrorString_Type()
)
mgnt2SoftwareDownloadActivationErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2SoftwareDownloadActivationErrorString.setStatus("current")


class _Mgnt2SoftwareDownloadActivationSlotNumber_Type(Integer32):
    """Custom type mgnt2SoftwareDownloadActivationSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgnt2SoftwareDownloadActivationSlotNumber_Type.__name__ = "Integer32"
_Mgnt2SoftwareDownloadActivationSlotNumber_Object = MibScalar
mgnt2SoftwareDownloadActivationSlotNumber = _Mgnt2SoftwareDownloadActivationSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 7, 5),
    _Mgnt2SoftwareDownloadActivationSlotNumber_Type()
)
mgnt2SoftwareDownloadActivationSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2SoftwareDownloadActivationSlotNumber.setStatus("current")
_Mgnt2SoftwareDownloadActivationClearFile_Type = Integer32
_Mgnt2SoftwareDownloadActivationClearFile_Object = MibScalar
mgnt2SoftwareDownloadActivationClearFile = _Mgnt2SoftwareDownloadActivationClearFile_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 7, 6),
    _Mgnt2SoftwareDownloadActivationClearFile_Type()
)
mgnt2SoftwareDownloadActivationClearFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2SoftwareDownloadActivationClearFile.setStatus("current")
_Mgnt2SoftwareDownloadActivationFilename_Type = DisplayString
_Mgnt2SoftwareDownloadActivationFilename_Object = MibScalar
mgnt2SoftwareDownloadActivationFilename = _Mgnt2SoftwareDownloadActivationFilename_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 7, 7),
    _Mgnt2SoftwareDownloadActivationFilename_Type()
)
mgnt2SoftwareDownloadActivationFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2SoftwareDownloadActivationFilename.setStatus("current")
_Mgnt2SoftwareDownloadActivationAutoRestart_Type = Integer32
_Mgnt2SoftwareDownloadActivationAutoRestart_Object = MibScalar
mgnt2SoftwareDownloadActivationAutoRestart = _Mgnt2SoftwareDownloadActivationAutoRestart_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 7, 8),
    _Mgnt2SoftwareDownloadActivationAutoRestart_Type()
)
mgnt2SoftwareDownloadActivationAutoRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2SoftwareDownloadActivationAutoRestart.setStatus("current")
_Mgnt2SoftwareDownloadActivationFileType_Type = Mgnt2DownloadFileType
_Mgnt2SoftwareDownloadActivationFileType_Object = MibScalar
mgnt2SoftwareDownloadActivationFileType = _Mgnt2SoftwareDownloadActivationFileType_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 7, 9),
    _Mgnt2SoftwareDownloadActivationFileType_Type()
)
mgnt2SoftwareDownloadActivationFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2SoftwareDownloadActivationFileType.setStatus("current")
_Mgnt2LacTable_Object = MibTable
mgnt2LacTable = _Mgnt2LacTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 8)
)
if mibBuilder.loadTexts:
    mgnt2LacTable.setStatus("current")
_Mgnt2LacEntry_Object = MibTableRow
mgnt2LacEntry = _Mgnt2LacEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 8, 1)
)
mgnt2LacEntry.setIndexNames(
    (0, "EKINOPS-MGNT2-NMS-MIB", "mgnt2LacIndex"),
)
if mibBuilder.loadTexts:
    mgnt2LacEntry.setStatus("current")
_Mgnt2LacIndex_Type = Integer32
_Mgnt2LacIndex_Object = MibTableColumn
mgnt2LacIndex = _Mgnt2LacIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 8, 1, 1),
    _Mgnt2LacIndex_Type()
)
mgnt2LacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2LacIndex.setStatus("current")
_Mgnt2LacState_Type = Mgnt2LacState
_Mgnt2LacState_Object = MibTableColumn
mgnt2LacState = _Mgnt2LacState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 8, 1, 2),
    _Mgnt2LacState_Type()
)
mgnt2LacState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2LacState.setStatus("current")


class _Mgnt2LacNoResponseTimeOutPeriod_Type(Integer32):
    """Custom type mgnt2LacNoResponseTimeOutPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_Mgnt2LacNoResponseTimeOutPeriod_Type.__name__ = "Integer32"
_Mgnt2LacNoResponseTimeOutPeriod_Object = MibTableColumn
mgnt2LacNoResponseTimeOutPeriod = _Mgnt2LacNoResponseTimeOutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 8, 1, 3),
    _Mgnt2LacNoResponseTimeOutPeriod_Type()
)
mgnt2LacNoResponseTimeOutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2LacNoResponseTimeOutPeriod.setStatus("current")
if mibBuilder.loadTexts:
    mgnt2LacNoResponseTimeOutPeriod.setUnits("seconds")
_Mgnt2PolledInfo_ObjectIdentity = ObjectIdentity
mgnt2PolledInfo = _Mgnt2PolledInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 10)
)
_Mgnt2PolledInfoLastAlarmNotificationId_Type = Counter32
_Mgnt2PolledInfoLastAlarmNotificationId_Object = MibScalar
mgnt2PolledInfoLastAlarmNotificationId = _Mgnt2PolledInfoLastAlarmNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 10, 1),
    _Mgnt2PolledInfoLastAlarmNotificationId_Type()
)
mgnt2PolledInfoLastAlarmNotificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2PolledInfoLastAlarmNotificationId.setStatus("current")
_Mgnt2PolledInfoLastEventNotificationId_Type = Counter32
_Mgnt2PolledInfoLastEventNotificationId_Object = MibScalar
mgnt2PolledInfoLastEventNotificationId = _Mgnt2PolledInfoLastEventNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 10, 2),
    _Mgnt2PolledInfoLastEventNotificationId_Type()
)
mgnt2PolledInfoLastEventNotificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2PolledInfoLastEventNotificationId.setStatus("current")
_Mgnt2PolledInfoConfigurationChecksum_Type = DisplayString
_Mgnt2PolledInfoConfigurationChecksum_Object = MibScalar
mgnt2PolledInfoConfigurationChecksum = _Mgnt2PolledInfoConfigurationChecksum_Object(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 10, 3),
    _Mgnt2PolledInfoConfigurationChecksum_Type()
)
mgnt2PolledInfoConfigurationChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2PolledInfoConfigurationChecksum.setStatus("current")
_Mgnt2SupportMCConf_ObjectIdentity = ObjectIdentity
mgnt2SupportMCConf = _Mgnt2SupportMCConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 2)
)
_Mgnt2SupportMCCompl_ObjectIdentity = ObjectIdentity
mgnt2SupportMCCompl = _Mgnt2SupportMCCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 2, 1)
)
_Mgnt2SupportMCGroup_ObjectIdentity = ObjectIdentity
mgnt2SupportMCGroup = _Mgnt2SupportMCGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 2, 2)
)

# Managed Objects groups

mgnt2ActiveAlmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 2, 1, 2)
)
mgnt2ActiveAlmGroup.setObjects(
      *(("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmProbableCause"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmObjectClassIdentifier"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmSourcePm"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmBoardNumber"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmSourcePortType"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmSourcePortNumber"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmSeverity"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmType"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmTime"))
)
if mibBuilder.loadTexts:
    mgnt2ActiveAlmGroup.setStatus("current")

mgnt2AlmLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 2, 1, 3)
)
mgnt2AlmLogGroup.setObjects(
      *(("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogProbableCause"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogObjectClassIdentifier"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogSourcePm"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogBoardNumber"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogSourcePortType"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogSourcePortNumber"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogSeverity"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogAlarmType"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogTime"))
)
if mibBuilder.loadTexts:
    mgnt2AlmLogGroup.setStatus("current")

mgnt2EventLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 2, 1, 4)
)
mgnt2EventLogGroup.setObjects(
      *(("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogObjectClassIdentifier"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogSourcePm"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogBoardNumber"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogSourcePortType"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogSourcePortNumber"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogEventType"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogSourceType"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogTime"))
)
if mibBuilder.loadTexts:
    mgnt2EventLogGroup.setStatus("current")


# Notification objects

mgnt2TrapNMSAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 11)
)
mgnt2TrapNMSAlarm.setObjects(
      *(("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogNotificationId"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogObjectClassIdentifier"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogSourcePm"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogBoardNumber"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogSourcePortType"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogSourcePortNumber"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogProbableCause"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogSeverity"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogSpecificProblem"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogAdditionalText"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogAlarmType"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogTime"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogNodeControllerIpAddress"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogChassisId"))
)
if mibBuilder.loadTexts:
    mgnt2TrapNMSAlarm.setStatus(
        "current"
    )

mgnt2TrapNMSEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 1, 12)
)
mgnt2TrapNMSEvent.setObjects(
      *(("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogNotificationId"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogObjectClassIdentifier"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogSourcePm"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogBoardNumber"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogSourcePortType"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogSourcePortNumber"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogEventType"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogSourceType"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogReason"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogAdditionalText"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogTime"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogNodeControllerIpAddress"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogChassisId"))
)
if mibBuilder.loadTexts:
    mgnt2TrapNMSEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

mgnt2SupportMc = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 20044, 1000, 2, 1, 1)
)
mgnt2SupportMc.setObjects(
      *(("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmGroup"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogGroup"),
        ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogGroup"))
)
if mibBuilder.loadTexts:
    mgnt2SupportMc.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-MGNT2-NMS-MIB",
    **{"Mgnt2NotificationId": Mgnt2NotificationId,
       "Mgnt2AlmProbableCause": Mgnt2AlmProbableCause,
       "Mgnt2ObjectClassId": Mgnt2ObjectClassId,
       "Mgnt2AlmSeverity": Mgnt2AlmSeverity,
       "Mgnt2AlmType": Mgnt2AlmType,
       "Mgnt2EventType": Mgnt2EventType,
       "Mgnt2EventSourceType": Mgnt2EventSourceType,
       "Mgnt2LacState": Mgnt2LacState,
       "Mgnt2ServerAddress": Mgnt2ServerAddress,
       "Mgnt2UploadDownloadFileEncoding": Mgnt2UploadDownloadFileEncoding,
       "Mgnt2UploadDownloadFileCompression": Mgnt2UploadDownloadFileCompression,
       "Mgnt2UploadDownloadActionStatus": Mgnt2UploadDownloadActionStatus,
       "Mgnt2UploadDownloadErrorCode": Mgnt2UploadDownloadErrorCode,
       "Mgnt2SoftwareDownloadActionStatus": Mgnt2SoftwareDownloadActionStatus,
       "Mgnt2DownloadFileType": Mgnt2DownloadFileType,
       "mgnt2NMS": mgnt2NMS,
       "mgnt2NMSMibObject": mgnt2NMSMibObject,
       "mgnt2ActiveAlmTable": mgnt2ActiveAlmTable,
       "mgnt2ActiveAlmEntry": mgnt2ActiveAlmEntry,
       "mgnt2ActiveAlmNotificationId": mgnt2ActiveAlmNotificationId,
       "mgnt2ActiveAlmProbableCause": mgnt2ActiveAlmProbableCause,
       "mgnt2ActiveAlmObjectClassIdentifier": mgnt2ActiveAlmObjectClassIdentifier,
       "mgnt2ActiveAlmSourcePm": mgnt2ActiveAlmSourcePm,
       "mgnt2ActiveAlmBoardNumber": mgnt2ActiveAlmBoardNumber,
       "mgnt2ActiveAlmSourcePortType": mgnt2ActiveAlmSourcePortType,
       "mgnt2ActiveAlmSourcePortNumber": mgnt2ActiveAlmSourcePortNumber,
       "mgnt2ActiveAlmSeverity": mgnt2ActiveAlmSeverity,
       "mgnt2ActiveAlmSpecificProblem": mgnt2ActiveAlmSpecificProblem,
       "mgnt2ActiveAlmAdditionalText": mgnt2ActiveAlmAdditionalText,
       "mgnt2ActiveAlmType": mgnt2ActiveAlmType,
       "mgnt2ActiveAlmTime": mgnt2ActiveAlmTime,
       "mgnt2ActiveAlmNodeControllerIpAddress": mgnt2ActiveAlmNodeControllerIpAddress,
       "mgnt2ActiveAlmChassisId": mgnt2ActiveAlmChassisId,
       "mgnt2AlmLogTable": mgnt2AlmLogTable,
       "mgnt2AlmLogEntry": mgnt2AlmLogEntry,
       "mgnt2AlmLogNotificationId": mgnt2AlmLogNotificationId,
       "mgnt2AlmLogProbableCause": mgnt2AlmLogProbableCause,
       "mgnt2AlmLogObjectClassIdentifier": mgnt2AlmLogObjectClassIdentifier,
       "mgnt2AlmLogSourcePm": mgnt2AlmLogSourcePm,
       "mgnt2AlmLogBoardNumber": mgnt2AlmLogBoardNumber,
       "mgnt2AlmLogSourcePortType": mgnt2AlmLogSourcePortType,
       "mgnt2AlmLogSourcePortNumber": mgnt2AlmLogSourcePortNumber,
       "mgnt2AlmLogSeverity": mgnt2AlmLogSeverity,
       "mgnt2AlmLogSpecificProblem": mgnt2AlmLogSpecificProblem,
       "mgnt2AlmLogAdditionalText": mgnt2AlmLogAdditionalText,
       "mgnt2AlmLogAlarmType": mgnt2AlmLogAlarmType,
       "mgnt2AlmLogTime": mgnt2AlmLogTime,
       "mgnt2AlmLogNodeControllerIpAddress": mgnt2AlmLogNodeControllerIpAddress,
       "mgnt2AlmLogChassisId": mgnt2AlmLogChassisId,
       "mgnt2EventLogTable": mgnt2EventLogTable,
       "mgnt2EventLogEntry": mgnt2EventLogEntry,
       "mgnt2EventLogNotificationId": mgnt2EventLogNotificationId,
       "mgnt2EventLogObjectClassIdentifier": mgnt2EventLogObjectClassIdentifier,
       "mgnt2EventLogSourcePm": mgnt2EventLogSourcePm,
       "mgnt2EventLogBoardNumber": mgnt2EventLogBoardNumber,
       "mgnt2EventLogSourcePortType": mgnt2EventLogSourcePortType,
       "mgnt2EventLogSourcePortNumber": mgnt2EventLogSourcePortNumber,
       "mgnt2EventLogEventType": mgnt2EventLogEventType,
       "mgnt2EventLogSourceType": mgnt2EventLogSourceType,
       "mgnt2EventLogReason": mgnt2EventLogReason,
       "mgnt2EventLogAdditionalText": mgnt2EventLogAdditionalText,
       "mgnt2EventLogTime": mgnt2EventLogTime,
       "mgnt2EventLogNodeControllerIpAddress": mgnt2EventLogNodeControllerIpAddress,
       "mgnt2EventLogChassisId": mgnt2EventLogChassisId,
       "mgnt2UploadDownload": mgnt2UploadDownload,
       "mgnt2UploadDownloadFilename": mgnt2UploadDownloadFilename,
       "mgnt2UploadDownloadAddress": mgnt2UploadDownloadAddress,
       "mgnt2UploadDownloadLogin": mgnt2UploadDownloadLogin,
       "mgnt2UploadDownloadPasswd": mgnt2UploadDownloadPasswd,
       "mgnt2UploadDownloadTxRetries": mgnt2UploadDownloadTxRetries,
       "mgnt2UploadDownloadActionStatus": mgnt2UploadDownloadActionStatus,
       "mgnt2UploadDownloadErrorCode": mgnt2UploadDownloadErrorCode,
       "mgnt2UploadDownloadDirection": mgnt2UploadDownloadDirection,
       "mgnt2UploadDownloadProgress": mgnt2UploadDownloadProgress,
       "mgnt2UploadDownloadReceivedFiles": mgnt2UploadDownloadReceivedFiles,
       "mgnt2UploadDownloadRemainingFiles": mgnt2UploadDownloadRemainingFiles,
       "mgnt2UploadDownloadFileType": mgnt2UploadDownloadFileType,
       "mgnt2UploadDownloadFileCompression": mgnt2UploadDownloadFileCompression,
       "mgnt2UploadDownloadDeleteLastFile": mgnt2UploadDownloadDeleteLastFile,
       "mgnt2Configuration": mgnt2Configuration,
       "mgnt2ConfigurationChecksum": mgnt2ConfigurationChecksum,
       "mgnt2ConfigurationActionStatus": mgnt2ConfigurationActionStatus,
       "mgnt2ConfigurationActivationErrorCode": mgnt2ConfigurationActivationErrorCode,
       "mgnt2ConfigurationActivationErrorString": mgnt2ConfigurationActivationErrorString,
       "mgnt2SoftwareDownload": mgnt2SoftwareDownload,
       "mgnt2SoftwareDownloadActionStatus": mgnt2SoftwareDownloadActionStatus,
       "mgnt2SoftwareDownloadActivationErrorCode": mgnt2SoftwareDownloadActivationErrorCode,
       "mgnt2SoftwareDownloadActivationErrorString": mgnt2SoftwareDownloadActivationErrorString,
       "mgnt2SoftwareDownloadActivationSlotNumber": mgnt2SoftwareDownloadActivationSlotNumber,
       "mgnt2SoftwareDownloadActivationClearFile": mgnt2SoftwareDownloadActivationClearFile,
       "mgnt2SoftwareDownloadActivationFilename": mgnt2SoftwareDownloadActivationFilename,
       "mgnt2SoftwareDownloadActivationAutoRestart": mgnt2SoftwareDownloadActivationAutoRestart,
       "mgnt2SoftwareDownloadActivationFileType": mgnt2SoftwareDownloadActivationFileType,
       "mgnt2LacTable": mgnt2LacTable,
       "mgnt2LacEntry": mgnt2LacEntry,
       "mgnt2LacIndex": mgnt2LacIndex,
       "mgnt2LacState": mgnt2LacState,
       "mgnt2LacNoResponseTimeOutPeriod": mgnt2LacNoResponseTimeOutPeriod,
       "mgnt2PolledInfo": mgnt2PolledInfo,
       "mgnt2PolledInfoLastAlarmNotificationId": mgnt2PolledInfoLastAlarmNotificationId,
       "mgnt2PolledInfoLastEventNotificationId": mgnt2PolledInfoLastEventNotificationId,
       "mgnt2PolledInfoConfigurationChecksum": mgnt2PolledInfoConfigurationChecksum,
       "mgnt2TrapNMSAlarm": mgnt2TrapNMSAlarm,
       "mgnt2TrapNMSEvent": mgnt2TrapNMSEvent,
       "mgnt2SupportMCConf": mgnt2SupportMCConf,
       "mgnt2SupportMCCompl": mgnt2SupportMCCompl,
       "mgnt2SupportMc": mgnt2SupportMc,
       "mgnt2ActiveAlmGroup": mgnt2ActiveAlmGroup,
       "mgnt2AlmLogGroup": mgnt2AlmLogGroup,
       "mgnt2EventLogGroup": mgnt2EventLogGroup,
       "mgnt2SupportMCGroup": mgnt2SupportMCGroup}
)
