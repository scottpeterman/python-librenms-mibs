# SNMP MIB module (ERICSSON-ROUTER-OPTICAL-TRANSCEIVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ericsson\ERICSSON-ROUTER-OPTICAL-TRANSCEIVER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:31 2025
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

(EriRouterAlarmId,
 EriRouterAlarmPerceivedSeverity,
 EriRouterAlarmServiceAffecting) = mibBuilder.importSymbols(
    "ERICSSON-ROUTER-ALARM-TC",
    "EriRouterAlarmId",
    "EriRouterAlarmPerceivedSeverity",
    "EriRouterAlarmServiceAffecting")

(eriRouterSfpAlarmDateAndTime,
 eriRouterSfpAlarmDescription,
 eriRouterSfpAlarmId,
 eriRouterSfpAlarmProbableCause,
 eriRouterSfpAlarmSeverity,
 eriRouterSfpAlarmType,
 eriRouterSfpMonMIBConformance,
 eriRouterSfpMonMIBNotifications,
 eriRouterSfpMonMIBObjects) = mibBuilder.importSymbols(
    "ERICSSON-ROUTER-SFP-MIB",
    "eriRouterSfpAlarmDateAndTime",
    "eriRouterSfpAlarmDescription",
    "eriRouterSfpAlarmId",
    "eriRouterSfpAlarmProbableCause",
    "eriRouterSfpAlarmSeverity",
    "eriRouterSfpAlarmType",
    "eriRouterSfpMonMIBConformance",
    "eriRouterSfpMonMIBNotifications",
    "eriRouterSfpMonMIBObjects")

(eriRouterMgmt,) = mibBuilder.importSymbols(
    "ERICSSON-ROUTER-SMI",
    "eriRouterMgmt")

(EriRouterPort,
 EriRouterSlot) = mibBuilder.importSymbols(
    "ERICSSON-ROUTER-TC",
    "EriRouterPort",
    "EriRouterSlot")

(IANAItuProbableCause,) = mibBuilder.importSymbols(
    "IANA-ITU-ALARM-TC-MIB",
    "IANAItuProbableCause")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eriRouterOpticalTransceiver = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50)
)
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiver.setRevisions(
        ("2015-06-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EriRouterOpticalTransceiverParamType(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("txpower", 1),
          ("rxpower", 2),
          ("temperature", 3),
          ("laserBiasCurrent", 4),
          ("soaBiasCurrent", 5),
          ("vcc", 6),
          ("aux1", 7),
          ("aux2", 8))
    )



class EriRouterOpticalTransceiverParamWaveLength(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000, 1000000),
    )



class EriRouterOpticalTransceiverParameterValue(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000, 1000000),
    )



class EriRouterLaneInOpticalTransceiverParamType(TextualConvention, Integer32):
    status = "current"
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
        *(("laneTxPower", 1),
          ("laneRxPower", 2),
          ("laneTemperature", 3),
          ("laneLaserBiasCurrent", 4))
    )



class EriRouterLaneInOpticalTransceiverParameterValue(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000, 1000000),
    )



# MIB Managed Objects in the order of their OIDs

_EriRouterOpticalTransceiverMonMIBGroups_ObjectIdentity = ObjectIdentity
eriRouterOpticalTransceiverMonMIBGroups = _EriRouterOpticalTransceiverMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 2, 3)
)
_EriRouterOpticalTransceiverMonMIBCompliances_ObjectIdentity = ObjectIdentity
eriRouterOpticalTransceiverMonMIBCompliances = _EriRouterOpticalTransceiverMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 2, 4)
)
_EriRouterOpticalTransceiverDetails_ObjectIdentity = ObjectIdentity
eriRouterOpticalTransceiverDetails = _EriRouterOpticalTransceiverDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1)
)
_EriRouterOpticalTransceiverPortTable_Object = MibTable
eriRouterOpticalTransceiverPortTable = _EriRouterOpticalTransceiverPortTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1)
)
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverPortTable.setStatus("current")
_EriRouterOpticalTransceiverPortEntry_Object = MibTableRow
eriRouterOpticalTransceiverPortEntry = _EriRouterOpticalTransceiverPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1)
)
eriRouterOpticalTransceiverPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverPortEntry.setStatus("current")
_EriRouterOpticalTransceiverCardSlot_Type = EriRouterSlot
_EriRouterOpticalTransceiverCardSlot_Object = MibTableColumn
eriRouterOpticalTransceiverCardSlot = _EriRouterOpticalTransceiverCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 1),
    _EriRouterOpticalTransceiverCardSlot_Type()
)
eriRouterOpticalTransceiverCardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverCardSlot.setStatus("current")
_EriRouterOpticalTransceiverPort_Type = EriRouterPort
_EriRouterOpticalTransceiverPort_Object = MibTableColumn
eriRouterOpticalTransceiverPort = _EriRouterOpticalTransceiverPort_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 2),
    _EriRouterOpticalTransceiverPort_Type()
)
eriRouterOpticalTransceiverPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverPort.setStatus("current")


class _EriRouterOpticalTransceiverType_Type(OctetString):
    """Custom type eriRouterOpticalTransceiverType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EriRouterOpticalTransceiverType_Type.__name__ = "OctetString"
_EriRouterOpticalTransceiverType_Object = MibTableColumn
eriRouterOpticalTransceiverType = _EriRouterOpticalTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 3),
    _EriRouterOpticalTransceiverType_Type()
)
eriRouterOpticalTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverType.setStatus("current")


class _EriRouterOpticalTransceiverMediaType_Type(OctetString):
    """Custom type eriRouterOpticalTransceiverMediaType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EriRouterOpticalTransceiverMediaType_Type.__name__ = "OctetString"
_EriRouterOpticalTransceiverMediaType_Object = MibTableColumn
eriRouterOpticalTransceiverMediaType = _EriRouterOpticalTransceiverMediaType_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 4),
    _EriRouterOpticalTransceiverMediaType_Type()
)
eriRouterOpticalTransceiverMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverMediaType.setStatus("current")
_EriRouterOpticalTransceiverEriRouterEricssonApproved_Type = TruthValue
_EriRouterOpticalTransceiverEriRouterEricssonApproved_Object = MibTableColumn
eriRouterOpticalTransceiverEriRouterEricssonApproved = _EriRouterOpticalTransceiverEriRouterEricssonApproved_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 5),
    _EriRouterOpticalTransceiverEriRouterEricssonApproved_Type()
)
eriRouterOpticalTransceiverEriRouterEricssonApproved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverEriRouterEricssonApproved.setStatus("current")
_EriRouterOpticalTransceiverDiagMonitoring_Type = TruthValue
_EriRouterOpticalTransceiverDiagMonitoring_Object = MibTableColumn
eriRouterOpticalTransceiverDiagMonitoring = _EriRouterOpticalTransceiverDiagMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 6),
    _EriRouterOpticalTransceiverDiagMonitoring_Type()
)
eriRouterOpticalTransceiverDiagMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverDiagMonitoring.setStatus("current")


class _EriRouterOpticalTransceiverCLEIcode_Type(OctetString):
    """Custom type eriRouterOpticalTransceiverCLEIcode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EriRouterOpticalTransceiverCLEIcode_Type.__name__ = "OctetString"
_EriRouterOpticalTransceiverCLEIcode_Object = MibTableColumn
eriRouterOpticalTransceiverCLEIcode = _EriRouterOpticalTransceiverCLEIcode_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 7),
    _EriRouterOpticalTransceiverCLEIcode_Type()
)
eriRouterOpticalTransceiverCLEIcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverCLEIcode.setStatus("current")


class _EriRouterOpticalTransceiverSerialNo_Type(OctetString):
    """Custom type eriRouterOpticalTransceiverSerialNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EriRouterOpticalTransceiverSerialNo_Type.__name__ = "OctetString"
_EriRouterOpticalTransceiverSerialNo_Object = MibTableColumn
eriRouterOpticalTransceiverSerialNo = _EriRouterOpticalTransceiverSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 8),
    _EriRouterOpticalTransceiverSerialNo_Type()
)
eriRouterOpticalTransceiverSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverSerialNo.setStatus("current")


class _EriRouterOpticalTransceiverFrequency_Type(OctetString):
    """Custom type eriRouterOpticalTransceiverFrequency based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EriRouterOpticalTransceiverFrequency_Type.__name__ = "OctetString"
_EriRouterOpticalTransceiverFrequency_Object = MibTableColumn
eriRouterOpticalTransceiverFrequency = _EriRouterOpticalTransceiverFrequency_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 9),
    _EriRouterOpticalTransceiverFrequency_Type()
)
eriRouterOpticalTransceiverFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverFrequency.setStatus("current")
_EriRouterOpticalTransceiverWaveLength_Type = EriRouterOpticalTransceiverParamWaveLength
_EriRouterOpticalTransceiverWaveLength_Object = MibTableColumn
eriRouterOpticalTransceiverWaveLength = _EriRouterOpticalTransceiverWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 10),
    _EriRouterOpticalTransceiverWaveLength_Type()
)
eriRouterOpticalTransceiverWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverWaveLength.setStatus("current")


class _EriRouterOpticalTransceiverAdditionalFeatures_Type(OctetString):
    """Custom type eriRouterOpticalTransceiverAdditionalFeatures based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EriRouterOpticalTransceiverAdditionalFeatures_Type.__name__ = "OctetString"
_EriRouterOpticalTransceiverAdditionalFeatures_Object = MibTableColumn
eriRouterOpticalTransceiverAdditionalFeatures = _EriRouterOpticalTransceiverAdditionalFeatures_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 11),
    _EriRouterOpticalTransceiverAdditionalFeatures_Type()
)
eriRouterOpticalTransceiverAdditionalFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverAdditionalFeatures.setStatus("current")


class _EriRouterOpticalTransceiverFrequencyStart_Type(OctetString):
    """Custom type eriRouterOpticalTransceiverFrequencyStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EriRouterOpticalTransceiverFrequencyStart_Type.__name__ = "OctetString"
_EriRouterOpticalTransceiverFrequencyStart_Object = MibTableColumn
eriRouterOpticalTransceiverFrequencyStart = _EriRouterOpticalTransceiverFrequencyStart_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 12),
    _EriRouterOpticalTransceiverFrequencyStart_Type()
)
eriRouterOpticalTransceiverFrequencyStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverFrequencyStart.setStatus("current")


class _EriRouterOpticalTransceiverFrequencyEnd_Type(OctetString):
    """Custom type eriRouterOpticalTransceiverFrequencyEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EriRouterOpticalTransceiverFrequencyEnd_Type.__name__ = "OctetString"
_EriRouterOpticalTransceiverFrequencyEnd_Object = MibTableColumn
eriRouterOpticalTransceiverFrequencyEnd = _EriRouterOpticalTransceiverFrequencyEnd_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 13),
    _EriRouterOpticalTransceiverFrequencyEnd_Type()
)
eriRouterOpticalTransceiverFrequencyEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverFrequencyEnd.setStatus("current")


class _EriRouterOpticalTransceiverFrequencySpacing_Type(OctetString):
    """Custom type eriRouterOpticalTransceiverFrequencySpacing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EriRouterOpticalTransceiverFrequencySpacing_Type.__name__ = "OctetString"
_EriRouterOpticalTransceiverFrequencySpacing_Object = MibTableColumn
eriRouterOpticalTransceiverFrequencySpacing = _EriRouterOpticalTransceiverFrequencySpacing_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 14),
    _EriRouterOpticalTransceiverFrequencySpacing_Type()
)
eriRouterOpticalTransceiverFrequencySpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverFrequencySpacing.setStatus("current")


class _EriRouterOpticalTransceiverOTNFramer_Type(OctetString):
    """Custom type eriRouterOpticalTransceiverOTNFramer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EriRouterOpticalTransceiverOTNFramer_Type.__name__ = "OctetString"
_EriRouterOpticalTransceiverOTNFramer_Object = MibTableColumn
eriRouterOpticalTransceiverOTNFramer = _EriRouterOpticalTransceiverOTNFramer_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 15),
    _EriRouterOpticalTransceiverOTNFramer_Type()
)
eriRouterOpticalTransceiverOTNFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverOTNFramer.setStatus("current")


class _EriRouterOpticalTransceiverOTNFEC_Type(OctetString):
    """Custom type eriRouterOpticalTransceiverOTNFEC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EriRouterOpticalTransceiverOTNFEC_Type.__name__ = "OctetString"
_EriRouterOpticalTransceiverOTNFEC_Object = MibTableColumn
eriRouterOpticalTransceiverOTNFEC = _EriRouterOpticalTransceiverOTNFEC_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 16),
    _EriRouterOpticalTransceiverOTNFEC_Type()
)
eriRouterOpticalTransceiverOTNFEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverOTNFEC.setStatus("current")


class _EriRouterOpticalTransceiverPowerLevel_Type(OctetString):
    """Custom type eriRouterOpticalTransceiverPowerLevel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EriRouterOpticalTransceiverPowerLevel_Type.__name__ = "OctetString"
_EriRouterOpticalTransceiverPowerLevel_Object = MibTableColumn
eriRouterOpticalTransceiverPowerLevel = _EriRouterOpticalTransceiverPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 17),
    _EriRouterOpticalTransceiverPowerLevel_Type()
)
eriRouterOpticalTransceiverPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverPowerLevel.setStatus("current")
_EriRouterOpticalTransceiverActiveAlarmCount_Type = Integer32
_EriRouterOpticalTransceiverActiveAlarmCount_Object = MibTableColumn
eriRouterOpticalTransceiverActiveAlarmCount = _EriRouterOpticalTransceiverActiveAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 18),
    _EriRouterOpticalTransceiverActiveAlarmCount_Type()
)
eriRouterOpticalTransceiverActiveAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverActiveAlarmCount.setStatus("current")
_EriRouterOpticalTransceiverParamBitMask_Type = Integer32
_EriRouterOpticalTransceiverParamBitMask_Object = MibTableColumn
eriRouterOpticalTransceiverParamBitMask = _EriRouterOpticalTransceiverParamBitMask_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 19),
    _EriRouterOpticalTransceiverParamBitMask_Type()
)
eriRouterOpticalTransceiverParamBitMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverParamBitMask.setStatus("current")
_EriRouterOpticalTransceiverLaneCount_Type = Integer32
_EriRouterOpticalTransceiverLaneCount_Object = MibTableColumn
eriRouterOpticalTransceiverLaneCount = _EriRouterOpticalTransceiverLaneCount_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 1, 1, 20),
    _EriRouterOpticalTransceiverLaneCount_Type()
)
eriRouterOpticalTransceiverLaneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverLaneCount.setStatus("current")
_EriRouterOpticalTransceiverParamTable_Object = MibTable
eriRouterOpticalTransceiverParamTable = _EriRouterOpticalTransceiverParamTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 2)
)
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverParamTable.setStatus("current")
_EriRouterOpticalTransceiverParamEntry_Object = MibTableRow
eriRouterOpticalTransceiverParamEntry = _EriRouterOpticalTransceiverParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 2, 1)
)
eriRouterOpticalTransceiverParamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ERICSSON-ROUTER-OPTICAL-TRANSCEIVER-MIB", "eriRouterOpticalTransceiverParamType"),
)
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverParamEntry.setStatus("current")
_EriRouterOpticalTransceiverParamType_Type = EriRouterOpticalTransceiverParamType
_EriRouterOpticalTransceiverParamType_Object = MibTableColumn
eriRouterOpticalTransceiverParamType = _EriRouterOpticalTransceiverParamType_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 2, 1, 1),
    _EriRouterOpticalTransceiverParamType_Type()
)
eriRouterOpticalTransceiverParamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverParamType.setStatus("current")


class _EriRouterOpticalTransceiverParamDescription_Type(OctetString):
    """Custom type eriRouterOpticalTransceiverParamDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EriRouterOpticalTransceiverParamDescription_Type.__name__ = "OctetString"
_EriRouterOpticalTransceiverParamDescription_Object = MibTableColumn
eriRouterOpticalTransceiverParamDescription = _EriRouterOpticalTransceiverParamDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 2, 1, 2),
    _EriRouterOpticalTransceiverParamDescription_Type()
)
eriRouterOpticalTransceiverParamDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverParamDescription.setStatus("current")
_EriRouterOpticalTransceiverCurrentValue_Type = EriRouterOpticalTransceiverParameterValue
_EriRouterOpticalTransceiverCurrentValue_Object = MibTableColumn
eriRouterOpticalTransceiverCurrentValue = _EriRouterOpticalTransceiverCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 2, 1, 3),
    _EriRouterOpticalTransceiverCurrentValue_Type()
)
eriRouterOpticalTransceiverCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverCurrentValue.setStatus("current")
_EriRouterOpticalTransceiverMaxAlarmValue_Type = EriRouterOpticalTransceiverParameterValue
_EriRouterOpticalTransceiverMaxAlarmValue_Object = MibTableColumn
eriRouterOpticalTransceiverMaxAlarmValue = _EriRouterOpticalTransceiverMaxAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 2, 1, 4),
    _EriRouterOpticalTransceiverMaxAlarmValue_Type()
)
eriRouterOpticalTransceiverMaxAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverMaxAlarmValue.setStatus("current")
_EriRouterOpticalTransceiverMaxWarningValue_Type = EriRouterOpticalTransceiverParameterValue
_EriRouterOpticalTransceiverMaxWarningValue_Object = MibTableColumn
eriRouterOpticalTransceiverMaxWarningValue = _EriRouterOpticalTransceiverMaxWarningValue_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 2, 1, 5),
    _EriRouterOpticalTransceiverMaxWarningValue_Type()
)
eriRouterOpticalTransceiverMaxWarningValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverMaxWarningValue.setStatus("current")
_EriRouterOpticalTransceiverMinAlarmValue_Type = EriRouterOpticalTransceiverParameterValue
_EriRouterOpticalTransceiverMinAlarmValue_Object = MibTableColumn
eriRouterOpticalTransceiverMinAlarmValue = _EriRouterOpticalTransceiverMinAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 2, 1, 6),
    _EriRouterOpticalTransceiverMinAlarmValue_Type()
)
eriRouterOpticalTransceiverMinAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverMinAlarmValue.setStatus("current")
_EriRouterOpticalTransceiverMinWarningValue_Type = EriRouterOpticalTransceiverParameterValue
_EriRouterOpticalTransceiverMinWarningValue_Object = MibTableColumn
eriRouterOpticalTransceiverMinWarningValue = _EriRouterOpticalTransceiverMinWarningValue_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 2, 1, 7),
    _EriRouterOpticalTransceiverMinWarningValue_Type()
)
eriRouterOpticalTransceiverMinWarningValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverMinWarningValue.setStatus("current")
_EriRouterLaneInOpticalTransceiverParamTable_Object = MibTable
eriRouterLaneInOpticalTransceiverParamTable = _EriRouterLaneInOpticalTransceiverParamTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 3)
)
if mibBuilder.loadTexts:
    eriRouterLaneInOpticalTransceiverParamTable.setStatus("current")
_EriRouterLaneInOpticalTransceiverParamEntry_Object = MibTableRow
eriRouterLaneInOpticalTransceiverParamEntry = _EriRouterLaneInOpticalTransceiverParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 3, 1)
)
eriRouterLaneInOpticalTransceiverParamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ERICSSON-ROUTER-OPTICAL-TRANSCEIVER-MIB", "eriRouterLaneInOpticalTransceiverParamType"),
    (0, "ERICSSON-ROUTER-OPTICAL-TRANSCEIVER-MIB", "eriRouterLaneInOpticalTransceiver"),
)
if mibBuilder.loadTexts:
    eriRouterLaneInOpticalTransceiverParamEntry.setStatus("current")


class _EriRouterLaneInOpticalTransceiver_Type(Integer32):
    """Custom type eriRouterLaneInOpticalTransceiver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EriRouterLaneInOpticalTransceiver_Type.__name__ = "Integer32"
_EriRouterLaneInOpticalTransceiver_Object = MibTableColumn
eriRouterLaneInOpticalTransceiver = _EriRouterLaneInOpticalTransceiver_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 3, 1, 1),
    _EriRouterLaneInOpticalTransceiver_Type()
)
eriRouterLaneInOpticalTransceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterLaneInOpticalTransceiver.setStatus("current")
_EriRouterLaneInOpticalTransceiverParamType_Type = EriRouterLaneInOpticalTransceiverParamType
_EriRouterLaneInOpticalTransceiverParamType_Object = MibTableColumn
eriRouterLaneInOpticalTransceiverParamType = _EriRouterLaneInOpticalTransceiverParamType_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 3, 1, 2),
    _EriRouterLaneInOpticalTransceiverParamType_Type()
)
eriRouterLaneInOpticalTransceiverParamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterLaneInOpticalTransceiverParamType.setStatus("current")
_EriRouterLaneInOpticalTransceiverCurrentValue_Type = EriRouterLaneInOpticalTransceiverParameterValue
_EriRouterLaneInOpticalTransceiverCurrentValue_Object = MibTableColumn
eriRouterLaneInOpticalTransceiverCurrentValue = _EriRouterLaneInOpticalTransceiverCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 3, 1, 3),
    _EriRouterLaneInOpticalTransceiverCurrentValue_Type()
)
eriRouterLaneInOpticalTransceiverCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterLaneInOpticalTransceiverCurrentValue.setStatus("current")
_EriRouterLaneInOpticalTransceiverMaxAlarmValue_Type = EriRouterLaneInOpticalTransceiverParameterValue
_EriRouterLaneInOpticalTransceiverMaxAlarmValue_Object = MibTableColumn
eriRouterLaneInOpticalTransceiverMaxAlarmValue = _EriRouterLaneInOpticalTransceiverMaxAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 3, 1, 4),
    _EriRouterLaneInOpticalTransceiverMaxAlarmValue_Type()
)
eriRouterLaneInOpticalTransceiverMaxAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterLaneInOpticalTransceiverMaxAlarmValue.setStatus("current")
_EriRouterLaneInOpticalTransceiverMaxWarningValue_Type = EriRouterLaneInOpticalTransceiverParameterValue
_EriRouterLaneInOpticalTransceiverMaxWarningValue_Object = MibTableColumn
eriRouterLaneInOpticalTransceiverMaxWarningValue = _EriRouterLaneInOpticalTransceiverMaxWarningValue_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 3, 1, 5),
    _EriRouterLaneInOpticalTransceiverMaxWarningValue_Type()
)
eriRouterLaneInOpticalTransceiverMaxWarningValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterLaneInOpticalTransceiverMaxWarningValue.setStatus("current")
_EriRouterLaneInOpticalTransceiverMinAlarmValue_Type = EriRouterLaneInOpticalTransceiverParameterValue
_EriRouterLaneInOpticalTransceiverMinAlarmValue_Object = MibTableColumn
eriRouterLaneInOpticalTransceiverMinAlarmValue = _EriRouterLaneInOpticalTransceiverMinAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 3, 1, 6),
    _EriRouterLaneInOpticalTransceiverMinAlarmValue_Type()
)
eriRouterLaneInOpticalTransceiverMinAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterLaneInOpticalTransceiverMinAlarmValue.setStatus("current")
_EriRouterLaneInOpticalTransceiverMinWarningValue_Type = EriRouterLaneInOpticalTransceiverParameterValue
_EriRouterLaneInOpticalTransceiverMinWarningValue_Object = MibTableColumn
eriRouterLaneInOpticalTransceiverMinWarningValue = _EriRouterLaneInOpticalTransceiverMinWarningValue_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 50, 1, 3, 1, 7),
    _EriRouterLaneInOpticalTransceiverMinWarningValue_Type()
)
eriRouterLaneInOpticalTransceiverMinWarningValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterLaneInOpticalTransceiverMinWarningValue.setStatus("current")

# Managed Objects groups


# Notification objects

eriRouterOpticalTransceiverAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 0, 2)
)
eriRouterOpticalTransceiverAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ERICSSON-ROUTER-OPTICAL-TRANSCEIVER-MIB", "eriRouterOpticalTransceiverCardSlot"),
        ("ERICSSON-ROUTER-OPTICAL-TRANSCEIVER-MIB", "eriRouterOpticalTransceiverPort"),
        ("ERICSSON-ROUTER-OPTICAL-TRANSCEIVER-MIB", "eriRouterOpticalTransceiverParamType"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmId"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmSeverity"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmType"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmDateAndTime"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmDescription"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmProbableCause"))
)
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverAlarm.setStatus(
        "current"
    )

eriRouterOpticalTransceiverLaneAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 0, 3)
)
eriRouterOpticalTransceiverLaneAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ERICSSON-ROUTER-OPTICAL-TRANSCEIVER-MIB", "eriRouterOpticalTransceiverCardSlot"),
        ("ERICSSON-ROUTER-OPTICAL-TRANSCEIVER-MIB", "eriRouterOpticalTransceiverPort"),
        ("ERICSSON-ROUTER-OPTICAL-TRANSCEIVER-MIB", "eriRouterLaneInOpticalTransceiver"),
        ("ERICSSON-ROUTER-OPTICAL-TRANSCEIVER-MIB", "eriRouterLaneInOpticalTransceiverParamType"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmId"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmSeverity"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmType"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmDateAndTime"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmDescription"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmProbableCause"))
)
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverLaneAlarm.setStatus(
        "current"
    )


# Notifications groups

eriRouterOpticalTransceiverMonMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 2, 3, 2)
)
eriRouterOpticalTransceiverMonMIBNotificationGroup.setObjects(
      *(("ERICSSON-ROUTER-OPTICAL-TRANSCEIVER-MIB", "eriRouterOpticalTransceiverAlarm"),
        ("ERICSSON-ROUTER-OPTICAL-TRANSCEIVER-MIB", "eriRouterOpticalTransceiverLaneAlarm"))
)
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverMonMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

eriRouterOpticalTransceiverMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 2, 4, 1)
)
eriRouterOpticalTransceiverMonMIBCompliance.setObjects(
    ("ERICSSON-ROUTER-OPTICAL-TRANSCEIVER-MIB", "eriRouterOpticalTransceiverMonMIBNotificationGroup")
)
if mibBuilder.loadTexts:
    eriRouterOpticalTransceiverMonMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERICSSON-ROUTER-OPTICAL-TRANSCEIVER-MIB",
    **{"EriRouterOpticalTransceiverParamType": EriRouterOpticalTransceiverParamType,
       "EriRouterOpticalTransceiverParamWaveLength": EriRouterOpticalTransceiverParamWaveLength,
       "EriRouterOpticalTransceiverParameterValue": EriRouterOpticalTransceiverParameterValue,
       "EriRouterLaneInOpticalTransceiverParamType": EriRouterLaneInOpticalTransceiverParamType,
       "EriRouterLaneInOpticalTransceiverParameterValue": EriRouterLaneInOpticalTransceiverParameterValue,
       "eriRouterOpticalTransceiverAlarm": eriRouterOpticalTransceiverAlarm,
       "eriRouterOpticalTransceiverLaneAlarm": eriRouterOpticalTransceiverLaneAlarm,
       "eriRouterOpticalTransceiverMonMIBGroups": eriRouterOpticalTransceiverMonMIBGroups,
       "eriRouterOpticalTransceiverMonMIBNotificationGroup": eriRouterOpticalTransceiverMonMIBNotificationGroup,
       "eriRouterOpticalTransceiverMonMIBCompliances": eriRouterOpticalTransceiverMonMIBCompliances,
       "eriRouterOpticalTransceiverMonMIBCompliance": eriRouterOpticalTransceiverMonMIBCompliance,
       "eriRouterOpticalTransceiver": eriRouterOpticalTransceiver,
       "eriRouterOpticalTransceiverDetails": eriRouterOpticalTransceiverDetails,
       "eriRouterOpticalTransceiverPortTable": eriRouterOpticalTransceiverPortTable,
       "eriRouterOpticalTransceiverPortEntry": eriRouterOpticalTransceiverPortEntry,
       "eriRouterOpticalTransceiverCardSlot": eriRouterOpticalTransceiverCardSlot,
       "eriRouterOpticalTransceiverPort": eriRouterOpticalTransceiverPort,
       "eriRouterOpticalTransceiverType": eriRouterOpticalTransceiverType,
       "eriRouterOpticalTransceiverMediaType": eriRouterOpticalTransceiverMediaType,
       "eriRouterOpticalTransceiverEriRouterEricssonApproved": eriRouterOpticalTransceiverEriRouterEricssonApproved,
       "eriRouterOpticalTransceiverDiagMonitoring": eriRouterOpticalTransceiverDiagMonitoring,
       "eriRouterOpticalTransceiverCLEIcode": eriRouterOpticalTransceiverCLEIcode,
       "eriRouterOpticalTransceiverSerialNo": eriRouterOpticalTransceiverSerialNo,
       "eriRouterOpticalTransceiverFrequency": eriRouterOpticalTransceiverFrequency,
       "eriRouterOpticalTransceiverWaveLength": eriRouterOpticalTransceiverWaveLength,
       "eriRouterOpticalTransceiverAdditionalFeatures": eriRouterOpticalTransceiverAdditionalFeatures,
       "eriRouterOpticalTransceiverFrequencyStart": eriRouterOpticalTransceiverFrequencyStart,
       "eriRouterOpticalTransceiverFrequencyEnd": eriRouterOpticalTransceiverFrequencyEnd,
       "eriRouterOpticalTransceiverFrequencySpacing": eriRouterOpticalTransceiverFrequencySpacing,
       "eriRouterOpticalTransceiverOTNFramer": eriRouterOpticalTransceiverOTNFramer,
       "eriRouterOpticalTransceiverOTNFEC": eriRouterOpticalTransceiverOTNFEC,
       "eriRouterOpticalTransceiverPowerLevel": eriRouterOpticalTransceiverPowerLevel,
       "eriRouterOpticalTransceiverActiveAlarmCount": eriRouterOpticalTransceiverActiveAlarmCount,
       "eriRouterOpticalTransceiverParamBitMask": eriRouterOpticalTransceiverParamBitMask,
       "eriRouterOpticalTransceiverLaneCount": eriRouterOpticalTransceiverLaneCount,
       "eriRouterOpticalTransceiverParamTable": eriRouterOpticalTransceiverParamTable,
       "eriRouterOpticalTransceiverParamEntry": eriRouterOpticalTransceiverParamEntry,
       "eriRouterOpticalTransceiverParamType": eriRouterOpticalTransceiverParamType,
       "eriRouterOpticalTransceiverParamDescription": eriRouterOpticalTransceiverParamDescription,
       "eriRouterOpticalTransceiverCurrentValue": eriRouterOpticalTransceiverCurrentValue,
       "eriRouterOpticalTransceiverMaxAlarmValue": eriRouterOpticalTransceiverMaxAlarmValue,
       "eriRouterOpticalTransceiverMaxWarningValue": eriRouterOpticalTransceiverMaxWarningValue,
       "eriRouterOpticalTransceiverMinAlarmValue": eriRouterOpticalTransceiverMinAlarmValue,
       "eriRouterOpticalTransceiverMinWarningValue": eriRouterOpticalTransceiverMinWarningValue,
       "eriRouterLaneInOpticalTransceiverParamTable": eriRouterLaneInOpticalTransceiverParamTable,
       "eriRouterLaneInOpticalTransceiverParamEntry": eriRouterLaneInOpticalTransceiverParamEntry,
       "eriRouterLaneInOpticalTransceiver": eriRouterLaneInOpticalTransceiver,
       "eriRouterLaneInOpticalTransceiverParamType": eriRouterLaneInOpticalTransceiverParamType,
       "eriRouterLaneInOpticalTransceiverCurrentValue": eriRouterLaneInOpticalTransceiverCurrentValue,
       "eriRouterLaneInOpticalTransceiverMaxAlarmValue": eriRouterLaneInOpticalTransceiverMaxAlarmValue,
       "eriRouterLaneInOpticalTransceiverMaxWarningValue": eriRouterLaneInOpticalTransceiverMaxWarningValue,
       "eriRouterLaneInOpticalTransceiverMinAlarmValue": eriRouterLaneInOpticalTransceiverMinAlarmValue,
       "eriRouterLaneInOpticalTransceiverMinWarningValue": eriRouterLaneInOpticalTransceiverMinWarningValue}
)
