# SNMP MIB module (SIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\d5\SIM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:36 2025
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
 Bits,
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

simMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ECMGCSuCasId(TextualConvention, Unsigned32):
    status = "current"


class Signed16(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class AdministrativeState(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlocked", 1),
          ("shuttingDown", 2))
    )


class CaDescInsMode(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("psigInsertion", 0),
          ("noPsigInsertion", 1))
    )


class DelayType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("immediate", 0),
          ("synchronized", 1))
    )


class DescriptorStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("success", 0),
          ("unknownTrigger", 1),
          ("unknownLocation", 2),
          ("unsupportedDelay", 3),
          ("unknownContext", 4),
          ("unknownOtherTS", 5),
          ("unknownNetwork", 6),
          ("unknownTS", 7),
          ("unknownES", 8),
          ("unknownBouquet", 9),
          ("unknownEvent", 10),
          ("tableNotSupported", 11),
          ("tableFull", 12),
          ("other", 13))
    )


class ECMGChannelId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ECMGDelayValue(Signed16):
    status = "current"


class ECMTriggerType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ecmStreamOpen", 0),
          ("ecmStreamClose", 1),
          ("ecmStreamChange", 2),
          ("accessCriteriaChange", 3))
    )


class EMMGChannelId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class EMMGCommCapability(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("both", 0),
          ("tcp", 1),
          ("udp", 2))
    )


class EMMGCommType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("tcp", 0),
          ("udp", 1))
    )


class EMMGDataType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("emm", 0),
          ("other", 1))
    )


class FlowId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class FlowType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ecm", 0),
          ("emm", 1),
          ("privatedata", 2))
    )


class InsertLocation(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("pmtLoop1", 0),
          ("pmtLoop2", 1),
          ("cat", 2),
          ("nitLopp1ActualNet", 3),
          ("nitLoop2ActualNet", 4),
          ("nitLopp1OtherNet", 5),
          ("nitLoop2OtherNet", 6),
          ("batLoop1", 7),
          ("batLoop2", 8),
          ("sdtActualTS", 9),
          ("sdtOtherTS", 10),
          ("eitPFActualTS", 11),
          ("eitPFOtherTS", 12),
          ("eitScheduleActualTS", 13),
          ("eitScheduleOtherTS", 14))
    )


class ProvTableId(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("pat", 0),
          ("cat", 1),
          ("pmt", 2),
          ("nitActualNet", 3),
          ("nitOtherNet", 4),
          ("bat", 5),
          ("sdtActualTS", 6),
          ("sdtOtherTS", 7),
          ("eitPFActualTS", 8),
          ("eitPFOtherTS", 9),
          ("eitScheduleActualTS", 10),
          ("eitScheduleOtherTS", 11))
    )


class PsigType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("sig", 0),
          ("psig", 1),
          ("psisig", 2))
    )


class SectionTSPktFlag(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("section", 0),
          ("tspacket", 1))
    )


class StreamId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class SuperCasId(TextualConvention, Unsigned32):
    status = "current"


class TriggerType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("dvbEvent", 0),
          ("futureDvbEvent", 1),
          ("newEcmStream", 2),
          ("flowPidChange", 3),
          ("accessCriteriaChange", 4),
          ("ecmStreamClosure", 5),
          ("pdStreamCEvent", 6))
    )


# MIB Managed Objects in the order of their OIDs

_SimMIBObjects_ObjectIdentity = ObjectIdentity
simMIBObjects = _SimMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1)
)
_SimIdent_ObjectIdentity = ObjectIdentity
simIdent = _SimIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 1)
)


class _SimSofwareVersion_Type(DisplayString):
    """Custom type simSofwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )
    fixed_length = 80


_SimSofwareVersion_Type.__name__ = "DisplayString"
_SimSofwareVersion_Object = MibScalar
simSofwareVersion = _SimSofwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 1, 1),
    _SimSofwareVersion_Type()
)
simSofwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simSofwareVersion.setStatus("current")


class _SimMIBVersion_Type(DisplayString):
    """Custom type simMIBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )
    fixed_length = 80


_SimMIBVersion_Type.__name__ = "DisplayString"
_SimMIBVersion_Object = MibScalar
simMIBVersion = _SimMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 1, 2),
    _SimMIBVersion_Type()
)
simMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simMIBVersion.setStatus("current")


class _SimMIBPrivateVersion_Type(DisplayString):
    """Custom type simMIBPrivateVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )
    fixed_length = 80


_SimMIBPrivateVersion_Type.__name__ = "DisplayString"
_SimMIBPrivateVersion_Object = MibScalar
simMIBPrivateVersion = _SimMIBPrivateVersion_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 1, 3),
    _SimMIBPrivateVersion_Type()
)
simMIBPrivateVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simMIBPrivateVersion.setStatus("current")


class _SimAgentVersion_Type(DisplayString):
    """Custom type simAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )
    fixed_length = 80


_SimAgentVersion_Type.__name__ = "DisplayString"
_SimAgentVersion_Object = MibScalar
simAgentVersion = _SimAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 1, 4),
    _SimAgentVersion_Type()
)
simAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simAgentVersion.setStatus("current")
_SimECMG_ObjectIdentity = ObjectIdentity
simECMG = _SimECMG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2)
)
_SimEcmgTable_Object = MibTable
simEcmgTable = _SimEcmgTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    simEcmgTable.setStatus("current")
_SimEcmgEntry_Object = MibTableRow
simEcmgEntry = _SimEcmgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 1, 1)
)
simEcmgEntry.setIndexNames(
    (0, "SIM-MIB", "simEcmgIndex"),
)
if mibBuilder.loadTexts:
    simEcmgEntry.setStatus("current")


class _SimEcmgIndex_Type(Integer32):
    """Custom type simEcmgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimEcmgIndex_Type.__name__ = "Integer32"
_SimEcmgIndex_Object = MibTableColumn
simEcmgIndex = _SimEcmgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 1, 1, 1),
    _SimEcmgIndex_Type()
)
simEcmgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgIndex.setStatus("current")
_SimEcmgIpAddress_Type = IpAddress
_SimEcmgIpAddress_Object = MibTableColumn
simEcmgIpAddress = _SimEcmgIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 1, 1, 2),
    _SimEcmgIpAddress_Type()
)
simEcmgIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgIpAddress.setStatus("current")


class _SimEcmgTcpPort_Type(Integer32):
    """Custom type simEcmgTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimEcmgTcpPort_Type.__name__ = "Integer32"
_SimEcmgTcpPort_Object = MibTableColumn
simEcmgTcpPort = _SimEcmgTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 1, 1, 3),
    _SimEcmgTcpPort_Type()
)
simEcmgTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgTcpPort.setStatus("current")
_SimEcmgSuCasId_Type = SuperCasId
_SimEcmgSuCasId_Object = MibTableColumn
simEcmgSuCasId = _SimEcmgSuCasId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 1, 1, 4),
    _SimEcmgSuCasId_Type()
)
simEcmgSuCasId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgSuCasId.setStatus("current")
_SimEcmgChannels_Type = Counter32
_SimEcmgChannels_Object = MibTableColumn
simEcmgChannels = _SimEcmgChannels_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 1, 1, 5),
    _SimEcmgChannels_Type()
)
simEcmgChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgChannels.setStatus("current")
_SimEcmgCwPrs_Type = Counter32
_SimEcmgCwPrs_Object = MibTableColumn
simEcmgCwPrs = _SimEcmgCwPrs_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 1, 1, 6),
    _SimEcmgCwPrs_Type()
)
simEcmgCwPrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgCwPrs.setStatus("current")
_SimEcmgErrs_Type = Counter32
_SimEcmgErrs_Object = MibTableColumn
simEcmgErrs = _SimEcmgErrs_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 1, 1, 7),
    _SimEcmgErrs_Type()
)
simEcmgErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgErrs.setStatus("current")


class _SimEcmgTargetCpsig_Type(Integer32):
    """Custom type simEcmgTargetCpsig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimEcmgTargetCpsig_Type.__name__ = "Integer32"
_SimEcmgTargetCpsig_Object = MibTableColumn
simEcmgTargetCpsig = _SimEcmgTargetCpsig_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 1, 1, 8),
    _SimEcmgTargetCpsig_Type()
)
simEcmgTargetCpsig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgTargetCpsig.setStatus("current")
_SimEcmgCaMib_Type = ObjectIdentifier
_SimEcmgCaMib_Object = MibTableColumn
simEcmgCaMib = _SimEcmgCaMib_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 1, 1, 9),
    _SimEcmgCaMib_Type()
)
simEcmgCaMib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgCaMib.setStatus("current")
_SimEcmgCTable_Object = MibTable
simEcmgCTable = _SimEcmgCTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    simEcmgCTable.setStatus("current")
_SimEcmgCEntry_Object = MibTableRow
simEcmgCEntry = _SimEcmgCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1)
)
simEcmgCEntry.setIndexNames(
    (0, "SIM-MIB", "simEcmgIndex"),
    (0, "SIM-MIB", "simEcmgChannelId"),
)
if mibBuilder.loadTexts:
    simEcmgCEntry.setStatus("current")
_SimEcmgChannelId_Type = ECMGChannelId
_SimEcmgChannelId_Object = MibTableColumn
simEcmgChannelId = _SimEcmgChannelId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 1),
    _SimEcmgChannelId_Type()
)
simEcmgChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgChannelId.setStatus("current")
_SimEcmgCScsIpAddress_Type = IpAddress
_SimEcmgCScsIpAddress_Object = MibTableColumn
simEcmgCScsIpAddress = _SimEcmgCScsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 2),
    _SimEcmgCScsIpAddress_Type()
)
simEcmgCScsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgCScsIpAddress.setStatus("current")


class _SimEcmgCScsTcpPort_Type(Integer32):
    """Custom type simEcmgCScsTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimEcmgCScsTcpPort_Type.__name__ = "Integer32"
_SimEcmgCScsTcpPort_Object = MibTableColumn
simEcmgCScsTcpPort = _SimEcmgCScsTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 3),
    _SimEcmgCScsTcpPort_Type()
)
simEcmgCScsTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgCScsTcpPort.setStatus("current")
_SimEcmgCStreams_Type = Counter32
_SimEcmgCStreams_Object = MibTableColumn
simEcmgCStreams = _SimEcmgCStreams_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 4),
    _SimEcmgCStreams_Type()
)
simEcmgCStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgCStreams.setStatus("current")
_SimEcmgCCwPrs_Type = Counter32
_SimEcmgCCwPrs_Object = MibTableColumn
simEcmgCCwPrs = _SimEcmgCCwPrs_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 5),
    _SimEcmgCCwPrs_Type()
)
simEcmgCCwPrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgCCwPrs.setStatus("current")
_SimEcmgCErrs_Type = Counter32
_SimEcmgCErrs_Object = MibTableColumn
simEcmgCErrs = _SimEcmgCErrs_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 6),
    _SimEcmgCErrs_Type()
)
simEcmgCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgCErrs.setStatus("current")
_SimEcmgCSuCasId_Type = ECMGCSuCasId
_SimEcmgCSuCasId_Object = MibTableColumn
simEcmgCSuCasId = _SimEcmgCSuCasId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 7),
    _SimEcmgCSuCasId_Type()
)
simEcmgCSuCasId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgCSuCasId.setStatus("current")
_SimEcmgFormat_Type = SectionTSPktFlag
_SimEcmgFormat_Object = MibTableColumn
simEcmgFormat = _SimEcmgFormat_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 8),
    _SimEcmgFormat_Type()
)
simEcmgFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgFormat.setStatus("current")
_SimACDelayStart_Type = ECMGDelayValue
_SimACDelayStart_Object = MibTableColumn
simACDelayStart = _SimACDelayStart_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 9),
    _SimACDelayStart_Type()
)
simACDelayStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simACDelayStart.setStatus("current")
_SimACDelayStop_Type = ECMGDelayValue
_SimACDelayStop_Object = MibTableColumn
simACDelayStop = _SimACDelayStop_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 10),
    _SimACDelayStop_Type()
)
simACDelayStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simACDelayStop.setStatus("current")
_SimDelayStart_Type = ECMGDelayValue
_SimDelayStart_Object = MibTableColumn
simDelayStart = _SimDelayStart_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 11),
    _SimDelayStart_Type()
)
simDelayStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simDelayStart.setStatus("current")
_SimDelayStop_Type = ECMGDelayValue
_SimDelayStop_Object = MibTableColumn
simDelayStop = _SimDelayStop_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 12),
    _SimDelayStop_Type()
)
simDelayStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simDelayStop.setStatus("current")
_SimTransitionDelayStart_Type = ECMGDelayValue
_SimTransitionDelayStart_Object = MibTableColumn
simTransitionDelayStart = _SimTransitionDelayStart_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 13),
    _SimTransitionDelayStart_Type()
)
simTransitionDelayStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simTransitionDelayStart.setStatus("current")
_SimTransitionDelayStop_Type = ECMGDelayValue
_SimTransitionDelayStop_Object = MibTableColumn
simTransitionDelayStop = _SimTransitionDelayStop_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 14),
    _SimTransitionDelayStop_Type()
)
simTransitionDelayStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simTransitionDelayStop.setStatus("current")


class _SimECMRepPeriod_Type(Integer32):
    """Custom type simECMRepPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimECMRepPeriod_Type.__name__ = "Integer32"
_SimECMRepPeriod_Object = MibTableColumn
simECMRepPeriod = _SimECMRepPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 15),
    _SimECMRepPeriod_Type()
)
simECMRepPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simECMRepPeriod.setStatus("current")
_SimMaxStreams_Type = Counter32
_SimMaxStreams_Object = MibTableColumn
simMaxStreams = _SimMaxStreams_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 16),
    _SimMaxStreams_Type()
)
simMaxStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simMaxStreams.setStatus("current")


class _SimMinCPDuration_Type(Integer32):
    """Custom type simMinCPDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimMinCPDuration_Type.__name__ = "Integer32"
_SimMinCPDuration_Object = MibTableColumn
simMinCPDuration = _SimMinCPDuration_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 17),
    _SimMinCPDuration_Type()
)
simMinCPDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simMinCPDuration.setStatus("current")
_SimLeadCW_Type = Counter32
_SimLeadCW_Object = MibTableColumn
simLeadCW = _SimLeadCW_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 18),
    _SimLeadCW_Type()
)
simLeadCW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simLeadCW.setStatus("current")
_SimCWPerMsg_Type = Counter32
_SimCWPerMsg_Object = MibTableColumn
simCWPerMsg = _SimCWPerMsg_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 19),
    _SimCWPerMsg_Type()
)
simCWPerMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCWPerMsg.setStatus("current")


class _SimMaxCompTime_Type(Integer32):
    """Custom type simMaxCompTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimMaxCompTime_Type.__name__ = "Integer32"
_SimMaxCompTime_Object = MibTableColumn
simMaxCompTime = _SimMaxCompTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 2, 1, 20),
    _SimMaxCompTime_Type()
)
simMaxCompTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simMaxCompTime.setStatus("current")
_SimEcmgSTable_Object = MibTable
simEcmgSTable = _SimEcmgSTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    simEcmgSTable.setStatus("current")
_SimEcmgSEntry_Object = MibTableRow
simEcmgSEntry = _SimEcmgSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 3, 1)
)
simEcmgSEntry.setIndexNames(
    (0, "SIM-MIB", "simEcmgIndex"),
    (0, "SIM-MIB", "simEcmgChannelId"),
    (0, "SIM-MIB", "simEcmgStreamId"),
)
if mibBuilder.loadTexts:
    simEcmgSEntry.setStatus("current")
_SimEcmgStreamId_Type = StreamId
_SimEcmgStreamId_Object = MibTableColumn
simEcmgStreamId = _SimEcmgStreamId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 3, 1, 1),
    _SimEcmgStreamId_Type()
)
simEcmgStreamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgStreamId.setStatus("current")
_SimEcmgEcmId_Type = FlowId
_SimEcmgEcmId_Object = MibTableColumn
simEcmgEcmId = _SimEcmgEcmId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 3, 1, 2),
    _SimEcmgEcmId_Type()
)
simEcmgEcmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgEcmId.setStatus("current")
_SimEcmgSLastCp_Type = Unsigned32
_SimEcmgSLastCp_Object = MibTableColumn
simEcmgSLastCp = _SimEcmgSLastCp_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 3, 1, 3),
    _SimEcmgSLastCp_Type()
)
simEcmgSLastCp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgSLastCp.setStatus("current")
_SimEcmgSCwPrs_Type = Counter32
_SimEcmgSCwPrs_Object = MibTableColumn
simEcmgSCwPrs = _SimEcmgSCwPrs_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 3, 1, 4),
    _SimEcmgSCwPrs_Type()
)
simEcmgSCwPrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgSCwPrs.setStatus("current")
_SimEcmgSErrs_Type = Counter32
_SimEcmgSErrs_Object = MibTableColumn
simEcmgSErrs = _SimEcmgSErrs_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 2, 3, 1, 5),
    _SimEcmgSErrs_Type()
)
simEcmgSErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEcmgSErrs.setStatus("current")
_SimEMMG_ObjectIdentity = ObjectIdentity
simEMMG = _SimEMMG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3)
)
_SimEmOrPdTable_Object = MibTable
simEmOrPdTable = _SimEmOrPdTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    simEmOrPdTable.setStatus("current")
_SimEmOrPdEntry_Object = MibTableRow
simEmOrPdEntry = _SimEmOrPdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 1, 1)
)
simEmOrPdEntry.setIndexNames(
    (0, "SIM-MIB", "simEmOrPdIndex"),
)
if mibBuilder.loadTexts:
    simEmOrPdEntry.setStatus("current")


class _SimEmOrPdIndex_Type(Integer32):
    """Custom type simEmOrPdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimEmOrPdIndex_Type.__name__ = "Integer32"
_SimEmOrPdIndex_Object = MibTableColumn
simEmOrPdIndex = _SimEmOrPdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 1, 1, 1),
    _SimEmOrPdIndex_Type()
)
simEmOrPdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEmOrPdIndex.setStatus("current")
_SimEmOrPdDataType_Type = EMMGDataType
_SimEmOrPdDataType_Object = MibTableColumn
simEmOrPdDataType = _SimEmOrPdDataType_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 1, 1, 2),
    _SimEmOrPdDataType_Type()
)
simEmOrPdDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEmOrPdDataType.setStatus("current")
_SimEmOrPdClientId_Type = SuperCasId
_SimEmOrPdClientId_Object = MibTableColumn
simEmOrPdClientId = _SimEmOrPdClientId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 1, 1, 3),
    _SimEmOrPdClientId_Type()
)
simEmOrPdClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEmOrPdClientId.setStatus("current")
_SimEmOrPdCommCapability_Type = EMMGCommCapability
_SimEmOrPdCommCapability_Object = MibTableColumn
simEmOrPdCommCapability = _SimEmOrPdCommCapability_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 1, 1, 4),
    _SimEmOrPdCommCapability_Type()
)
simEmOrPdCommCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEmOrPdCommCapability.setStatus("current")
_SimEmOrPdErrs_Type = Counter32
_SimEmOrPdErrs_Object = MibTableColumn
simEmOrPdErrs = _SimEmOrPdErrs_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 1, 1, 5),
    _SimEmOrPdErrs_Type()
)
simEmOrPdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEmOrPdErrs.setStatus("current")


class _SimEmOrPdTargetCpsig_Type(Integer32):
    """Custom type simEmOrPdTargetCpsig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimEmOrPdTargetCpsig_Type.__name__ = "Integer32"
_SimEmOrPdTargetCpsig_Object = MibTableColumn
simEmOrPdTargetCpsig = _SimEmOrPdTargetCpsig_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 1, 1, 6),
    _SimEmOrPdTargetCpsig_Type()
)
simEmOrPdTargetCpsig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simEmOrPdTargetCpsig.setStatus("current")
_SimEmOrPdCaMib_Type = ObjectIdentifier
_SimEmOrPdCaMib_Object = MibTableColumn
simEmOrPdCaMib = _SimEmOrPdCaMib_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 1, 1, 7),
    _SimEmOrPdCaMib_Type()
)
simEmOrPdCaMib.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simEmOrPdCaMib.setStatus("current")
_SimEmOrPdLapTable_Object = MibTable
simEmOrPdLapTable = _SimEmOrPdLapTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    simEmOrPdLapTable.setStatus("current")
_SimEmOrPdLapEntry_Object = MibTableRow
simEmOrPdLapEntry = _SimEmOrPdLapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 2, 1)
)
simEmOrPdLapEntry.setIndexNames(
    (0, "SIM-MIB", "simEmOrPdLapIndex"),
)
if mibBuilder.loadTexts:
    simEmOrPdLapEntry.setStatus("current")


class _SimEmOrPdLapIndex_Type(Integer32):
    """Custom type simEmOrPdLapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimEmOrPdLapIndex_Type.__name__ = "Integer32"
_SimEmOrPdLapIndex_Object = MibTableColumn
simEmOrPdLapIndex = _SimEmOrPdLapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 2, 1, 1),
    _SimEmOrPdLapIndex_Type()
)
simEmOrPdLapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEmOrPdLapIndex.setStatus("current")
_SimEmOrPdLapAdminState_Type = AdministrativeState
_SimEmOrPdLapAdminState_Object = MibTableColumn
simEmOrPdLapAdminState = _SimEmOrPdLapAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 2, 1, 2),
    _SimEmOrPdLapAdminState_Type()
)
simEmOrPdLapAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simEmOrPdLapAdminState.setStatus("current")
_SimEmOrPdLapCommType_Type = EMMGCommType
_SimEmOrPdLapCommType_Object = MibTableColumn
simEmOrPdLapCommType = _SimEmOrPdLapCommType_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 2, 1, 3),
    _SimEmOrPdLapCommType_Type()
)
simEmOrPdLapCommType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simEmOrPdLapCommType.setStatus("current")
_SimEmOrPdLapMuxIpAddress_Type = IpAddress
_SimEmOrPdLapMuxIpAddress_Object = MibTableColumn
simEmOrPdLapMuxIpAddress = _SimEmOrPdLapMuxIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 2, 1, 4),
    _SimEmOrPdLapMuxIpAddress_Type()
)
simEmOrPdLapMuxIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simEmOrPdLapMuxIpAddress.setStatus("current")


class _SimEmOrPdLapMuxPort_Type(Integer32):
    """Custom type simEmOrPdLapMuxPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimEmOrPdLapMuxPort_Type.__name__ = "Integer32"
_SimEmOrPdLapMuxPort_Object = MibTableColumn
simEmOrPdLapMuxPort = _SimEmOrPdLapMuxPort_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 2, 1, 5),
    _SimEmOrPdLapMuxPort_Type()
)
simEmOrPdLapMuxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simEmOrPdLapMuxPort.setStatus("current")
_SimEmOrPdLapStatus_Type = RowStatus
_SimEmOrPdLapStatus_Object = MibTableColumn
simEmOrPdLapStatus = _SimEmOrPdLapStatus_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 2, 1, 6),
    _SimEmOrPdLapStatus_Type()
)
simEmOrPdLapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simEmOrPdLapStatus.setStatus("current")
_SimEmOrPdLapMuxUIpAddress_Type = IpAddress
_SimEmOrPdLapMuxUIpAddress_Object = MibTableColumn
simEmOrPdLapMuxUIpAddress = _SimEmOrPdLapMuxUIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 2, 1, 7),
    _SimEmOrPdLapMuxUIpAddress_Type()
)
simEmOrPdLapMuxUIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simEmOrPdLapMuxUIpAddress.setStatus("current")


class _SimEmOrPdLapMuxUPort_Type(Integer32):
    """Custom type simEmOrPdLapMuxUPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimEmOrPdLapMuxUPort_Type.__name__ = "Integer32"
_SimEmOrPdLapMuxUPort_Object = MibTableColumn
simEmOrPdLapMuxUPort = _SimEmOrPdLapMuxUPort_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 2, 1, 8),
    _SimEmOrPdLapMuxUPort_Type()
)
simEmOrPdLapMuxUPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simEmOrPdLapMuxUPort.setStatus("current")
_SimEmOrPdLapGTable_Object = MibTable
simEmOrPdLapGTable = _SimEmOrPdLapGTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    simEmOrPdLapGTable.setStatus("current")
_SimEmOrPdLapGEntry_Object = MibTableRow
simEmOrPdLapGEntry = _SimEmOrPdLapGEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 3, 1)
)
simEmOrPdLapGEntry.setIndexNames(
    (0, "SIM-MIB", "simEmOrPdLapGroup"),
    (0, "SIM-MIB", "simEmOrPdLapIndex"),
)
if mibBuilder.loadTexts:
    simEmOrPdLapGEntry.setStatus("current")


class _SimEmOrPdLapGroup_Type(Integer32):
    """Custom type simEmOrPdLapGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimEmOrPdLapGroup_Type.__name__ = "Integer32"
_SimEmOrPdLapGroup_Object = MibTableColumn
simEmOrPdLapGroup = _SimEmOrPdLapGroup_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 3, 1, 1),
    _SimEmOrPdLapGroup_Type()
)
simEmOrPdLapGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEmOrPdLapGroup.setStatus("current")
_SimEmOrPdLapGAdminState_Type = AdministrativeState
_SimEmOrPdLapGAdminState_Object = MibTableColumn
simEmOrPdLapGAdminState = _SimEmOrPdLapGAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 3, 1, 2),
    _SimEmOrPdLapGAdminState_Type()
)
simEmOrPdLapGAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simEmOrPdLapGAdminState.setStatus("current")
_SimEmOrPdLapGStatus_Type = RowStatus
_SimEmOrPdLapGStatus_Object = MibTableColumn
simEmOrPdLapGStatus = _SimEmOrPdLapGStatus_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 3, 1, 3),
    _SimEmOrPdLapGStatus_Type()
)
simEmOrPdLapGStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simEmOrPdLapGStatus.setStatus("current")
_SimEmOrPdCTable_Object = MibTable
simEmOrPdCTable = _SimEmOrPdCTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    simEmOrPdCTable.setStatus("current")
_SimEmOrPdCEntry_Object = MibTableRow
simEmOrPdCEntry = _SimEmOrPdCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 4, 1)
)
simEmOrPdCEntry.setIndexNames(
    (0, "SIM-MIB", "simEmOrPdIndex"),
    (0, "SIM-MIB", "simEmOrPdLapIndex"),
    (0, "SIM-MIB", "simEmOrPdChannelId"),
)
if mibBuilder.loadTexts:
    simEmOrPdCEntry.setStatus("current")
_SimEmOrPdChannelId_Type = EMMGChannelId
_SimEmOrPdChannelId_Object = MibTableColumn
simEmOrPdChannelId = _SimEmOrPdChannelId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 4, 1, 1),
    _SimEmOrPdChannelId_Type()
)
simEmOrPdChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEmOrPdChannelId.setStatus("current")
_SimEmOrPdCommType_Type = EMMGCommType
_SimEmOrPdCommType_Object = MibTableColumn
simEmOrPdCommType = _SimEmOrPdCommType_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 4, 1, 2),
    _SimEmOrPdCommType_Type()
)
simEmOrPdCommType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simEmOrPdCommType.setStatus("current")
_SimEmOrPdCIpAddress_Type = IpAddress
_SimEmOrPdCIpAddress_Object = MibTableColumn
simEmOrPdCIpAddress = _SimEmOrPdCIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 4, 1, 3),
    _SimEmOrPdCIpAddress_Type()
)
simEmOrPdCIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEmOrPdCIpAddress.setStatus("current")


class _SimEmOrPdCPort_Type(Integer32):
    """Custom type simEmOrPdCPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimEmOrPdCPort_Type.__name__ = "Integer32"
_SimEmOrPdCPort_Object = MibTableColumn
simEmOrPdCPort = _SimEmOrPdCPort_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 4, 1, 4),
    _SimEmOrPdCPort_Type()
)
simEmOrPdCPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEmOrPdCPort.setStatus("current")
_SimEmOrPdCErrs_Type = Counter32
_SimEmOrPdCErrs_Object = MibTableColumn
simEmOrPdCErrs = _SimEmOrPdCErrs_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 4, 1, 5),
    _SimEmOrPdCErrs_Type()
)
simEmOrPdCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEmOrPdCErrs.setStatus("current")
_SimEmOrPdCFormat_Type = SectionTSPktFlag
_SimEmOrPdCFormat_Object = MibTableColumn
simEmOrPdCFormat = _SimEmOrPdCFormat_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 4, 1, 6),
    _SimEmOrPdCFormat_Type()
)
simEmOrPdCFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEmOrPdCFormat.setStatus("current")
_SimEmOrPdCUIpAddress_Type = IpAddress
_SimEmOrPdCUIpAddress_Object = MibTableColumn
simEmOrPdCUIpAddress = _SimEmOrPdCUIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 4, 1, 7),
    _SimEmOrPdCUIpAddress_Type()
)
simEmOrPdCUIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEmOrPdCUIpAddress.setStatus("current")


class _SimEmOrPdCUPort_Type(Integer32):
    """Custom type simEmOrPdCUPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimEmOrPdCUPort_Type.__name__ = "Integer32"
_SimEmOrPdCUPort_Object = MibTableColumn
simEmOrPdCUPort = _SimEmOrPdCUPort_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 4, 1, 8),
    _SimEmOrPdCUPort_Type()
)
simEmOrPdCUPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEmOrPdCUPort.setStatus("current")
_SimEmOrPdSTable_Object = MibTable
simEmOrPdSTable = _SimEmOrPdSTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    simEmOrPdSTable.setStatus("current")
_SimEmOrPdSEntry_Object = MibTableRow
simEmOrPdSEntry = _SimEmOrPdSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 5, 1)
)
simEmOrPdSEntry.setIndexNames(
    (0, "SIM-MIB", "simEmOrPdIndex"),
    (0, "SIM-MIB", "simEmOrPdLapIndex"),
    (0, "SIM-MIB", "simEmOrPdDataId"),
)
if mibBuilder.loadTexts:
    simEmOrPdSEntry.setStatus("current")
_SimEmOrPdDataId_Type = FlowId
_SimEmOrPdDataId_Object = MibTableColumn
simEmOrPdDataId = _SimEmOrPdDataId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 5, 1, 1),
    _SimEmOrPdDataId_Type()
)
simEmOrPdDataId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simEmOrPdDataId.setStatus("current")
_SimEmOrPdSChannelId_Type = EMMGChannelId
_SimEmOrPdSChannelId_Object = MibTableColumn
simEmOrPdSChannelId = _SimEmOrPdSChannelId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 5, 1, 2),
    _SimEmOrPdSChannelId_Type()
)
simEmOrPdSChannelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simEmOrPdSChannelId.setStatus("current")
_SimEmOrPdBwidth_Type = Unsigned32
_SimEmOrPdBwidth_Object = MibTableColumn
simEmOrPdBwidth = _SimEmOrPdBwidth_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 5, 1, 3),
    _SimEmOrPdBwidth_Type()
)
simEmOrPdBwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simEmOrPdBwidth.setStatus("current")
_SimEmOrPdStreamId_Type = StreamId
_SimEmOrPdStreamId_Object = MibTableColumn
simEmOrPdStreamId = _SimEmOrPdStreamId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 5, 1, 4),
    _SimEmOrPdStreamId_Type()
)
simEmOrPdStreamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEmOrPdStreamId.setStatus("current")
_SimEmOrPdSErrs_Type = Counter32
_SimEmOrPdSErrs_Object = MibTableColumn
simEmOrPdSErrs = _SimEmOrPdSErrs_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 5, 1, 5),
    _SimEmOrPdSErrs_Type()
)
simEmOrPdSErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEmOrPdSErrs.setStatus("current")
_SimEmOrPdSBytes_Type = Counter32
_SimEmOrPdSBytes_Object = MibTableColumn
simEmOrPdSBytes = _SimEmOrPdSBytes_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 5, 1, 6),
    _SimEmOrPdSBytes_Type()
)
simEmOrPdSBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simEmOrPdSBytes.setStatus("current")
_SimEmOrPdSReqBwidth_Type = Unsigned32
_SimEmOrPdSReqBwidth_Object = MibTableColumn
simEmOrPdSReqBwidth = _SimEmOrPdSReqBwidth_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 3, 5, 1, 7),
    _SimEmOrPdSReqBwidth_Type()
)
simEmOrPdSReqBwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simEmOrPdSReqBwidth.setStatus("current")
_SimCPSI_ObjectIdentity = ObjectIdentity
simCPSI = _SimCPSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4)
)
_SimCpsigTable_Object = MibTable
simCpsigTable = _SimCpsigTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    simCpsigTable.setStatus("current")
_SimCpsigEntry_Object = MibTableRow
simCpsigEntry = _SimCpsigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 1, 1)
)
simCpsigEntry.setIndexNames(
    (0, "SIM-MIB", "simCpsigIndex"),
)
if mibBuilder.loadTexts:
    simCpsigEntry.setStatus("current")


class _SimCpsigIndex_Type(Integer32):
    """Custom type simCpsigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimCpsigIndex_Type.__name__ = "Integer32"
_SimCpsigIndex_Object = MibTableColumn
simCpsigIndex = _SimCpsigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 1, 1, 1),
    _SimCpsigIndex_Type()
)
simCpsigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigIndex.setStatus("current")
_SimCpsigSuperCasId_Type = SuperCasId
_SimCpsigSuperCasId_Object = MibTableColumn
simCpsigSuperCasId = _SimCpsigSuperCasId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 1, 1, 2),
    _SimCpsigSuperCasId_Type()
)
simCpsigSuperCasId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigSuperCasId.setStatus("current")
_SimCpsigErrs_Type = Counter32
_SimCpsigErrs_Object = MibTableColumn
simCpsigErrs = _SimCpsigErrs_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 1, 1, 3),
    _SimCpsigErrs_Type()
)
simCpsigErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigErrs.setStatus("current")
_SimCpsigChannels_Type = Counter32
_SimCpsigChannels_Object = MibTableColumn
simCpsigChannels = _SimCpsigChannels_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 1, 1, 4),
    _SimCpsigChannels_Type()
)
simCpsigChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigChannels.setStatus("current")
_SimCpsigCpsigIpAddress_Type = IpAddress
_SimCpsigCpsigIpAddress_Object = MibTableColumn
simCpsigCpsigIpAddress = _SimCpsigCpsigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 1, 1, 5),
    _SimCpsigCpsigIpAddress_Type()
)
simCpsigCpsigIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigCpsigIpAddress.setStatus("current")


class _SimCpsigCpsigPort_Type(Integer32):
    """Custom type simCpsigCpsigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimCpsigCpsigPort_Type.__name__ = "Integer32"
_SimCpsigCpsigPort_Object = MibTableColumn
simCpsigCpsigPort = _SimCpsigCpsigPort_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 1, 1, 6),
    _SimCpsigCpsigPort_Type()
)
simCpsigCpsigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigCpsigPort.setStatus("current")
_SimCpsigCaMib_Type = ObjectIdentifier
_SimCpsigCaMib_Object = MibTableColumn
simCpsigCaMib = _SimCpsigCaMib_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 1, 1, 7),
    _SimCpsigCaMib_Type()
)
simCpsigCaMib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigCaMib.setStatus("current")
_SimCpsigCTable_Object = MibTable
simCpsigCTable = _SimCpsigCTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    simCpsigCTable.setStatus("current")
_SimCpsigCEntry_Object = MibTableRow
simCpsigCEntry = _SimCpsigCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 2, 1)
)
simCpsigCEntry.setIndexNames(
    (0, "SIM-MIB", "simCpsigIndex"),
    (0, "SIM-MIB", "simCpsigChannelId"),
)
if mibBuilder.loadTexts:
    simCpsigCEntry.setStatus("current")


class _SimCpsigChannelId_Type(Integer32):
    """Custom type simCpsigChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimCpsigChannelId_Type.__name__ = "Integer32"
_SimCpsigChannelId_Object = MibTableColumn
simCpsigChannelId = _SimCpsigChannelId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 2, 1, 1),
    _SimCpsigChannelId_Type()
)
simCpsigChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigChannelId.setStatus("current")
_SimCpsigPsigIpAddress_Type = IpAddress
_SimCpsigPsigIpAddress_Object = MibTableColumn
simCpsigPsigIpAddress = _SimCpsigPsigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 2, 1, 2),
    _SimCpsigPsigIpAddress_Type()
)
simCpsigPsigIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigPsigIpAddress.setStatus("current")


class _SimCpsigPsigPort_Type(Integer32):
    """Custom type simCpsigPsigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimCpsigPsigPort_Type.__name__ = "Integer32"
_SimCpsigPsigPort_Object = MibTableColumn
simCpsigPsigPort = _SimCpsigPsigPort_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 2, 1, 3),
    _SimCpsigPsigPort_Type()
)
simCpsigPsigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigPsigPort.setStatus("current")
_SimCpsigCErrs_Type = Counter32
_SimCpsigCErrs_Object = MibTableColumn
simCpsigCErrs = _SimCpsigCErrs_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 2, 1, 4),
    _SimCpsigCErrs_Type()
)
simCpsigCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigCErrs.setStatus("current")
_SimCpsigCTstrms_Type = Counter32
_SimCpsigCTstrms_Object = MibTableColumn
simCpsigCTstrms = _SimCpsigCTstrms_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 2, 1, 5),
    _SimCpsigCTstrms_Type()
)
simCpsigCTstrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigCTstrms.setStatus("current")
_SimCpsigCSstrms_Type = Counter32
_SimCpsigCSstrms_Object = MibTableColumn
simCpsigCSstrms = _SimCpsigCSstrms_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 2, 1, 6),
    _SimCpsigCSstrms_Type()
)
simCpsigCSstrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigCSstrms.setStatus("current")
_SimCpsigStreamTable_Object = MibTable
simCpsigStreamTable = _SimCpsigStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    simCpsigStreamTable.setStatus("current")
_SimCpsigStreamEntry_Object = MibTableRow
simCpsigStreamEntry = _SimCpsigStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 3, 1)
)
simCpsigStreamEntry.setIndexNames(
    (0, "SIM-MIB", "simCpsigIndex"),
    (0, "SIM-MIB", "simCpsigChannelId"),
    (0, "SIM-MIB", "simCpsigStreamId"),
)
if mibBuilder.loadTexts:
    simCpsigStreamEntry.setStatus("current")


class _SimCpsigStreamId_Type(Integer32):
    """Custom type simCpsigStreamId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimCpsigStreamId_Type.__name__ = "Integer32"
_SimCpsigStreamId_Object = MibTableColumn
simCpsigStreamId = _SimCpsigStreamId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 3, 1, 1),
    _SimCpsigStreamId_Type()
)
simCpsigStreamId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    simCpsigStreamId.setStatus("current")


class _SimCpsigStreamTStreamId_Type(Integer32):
    """Custom type simCpsigStreamTStreamId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimCpsigStreamTStreamId_Type.__name__ = "Integer32"
_SimCpsigStreamTStreamId_Object = MibTableColumn
simCpsigStreamTStreamId = _SimCpsigStreamTStreamId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 3, 1, 2),
    _SimCpsigStreamTStreamId_Type()
)
simCpsigStreamTStreamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigStreamTStreamId.setStatus("current")


class _SimCpsigStreamNid_Type(Integer32):
    """Custom type simCpsigStreamNid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimCpsigStreamNid_Type.__name__ = "Integer32"
_SimCpsigStreamNid_Object = MibTableColumn
simCpsigStreamNid = _SimCpsigStreamNid_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 3, 1, 3),
    _SimCpsigStreamNid_Type()
)
simCpsigStreamNid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigStreamNid.setStatus("current")


class _SimCpsigStreamOnid_Type(Integer32):
    """Custom type simCpsigStreamOnid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimCpsigStreamOnid_Type.__name__ = "Integer32"
_SimCpsigStreamOnid_Object = MibTableColumn
simCpsigStreamOnid = _SimCpsigStreamOnid_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 3, 1, 4),
    _SimCpsigStreamOnid_Type()
)
simCpsigStreamOnid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigStreamOnid.setStatus("current")


class _SimCpsigStreamMaxCompTime_Type(Integer32):
    """Custom type simCpsigStreamMaxCompTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimCpsigStreamMaxCompTime_Type.__name__ = "Integer32"
_SimCpsigStreamMaxCompTime_Object = MibTableColumn
simCpsigStreamMaxCompTime = _SimCpsigStreamMaxCompTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 3, 1, 5),
    _SimCpsigStreamMaxCompTime_Type()
)
simCpsigStreamMaxCompTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigStreamMaxCompTime.setStatus("current")
_SimCpsigStreamTriggerEnable_Type = TriggerType
_SimCpsigStreamTriggerEnable_Object = MibTableColumn
simCpsigStreamTriggerEnable = _SimCpsigStreamTriggerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 3, 1, 6),
    _SimCpsigStreamTriggerEnable_Type()
)
simCpsigStreamTriggerEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigStreamTriggerEnable.setStatus("current")
_SimCpsigStreamLastTrigger_Type = TriggerType
_SimCpsigStreamLastTrigger_Object = MibTableColumn
simCpsigStreamLastTrigger = _SimCpsigStreamLastTrigger_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 3, 1, 7),
    _SimCpsigStreamLastTrigger_Type()
)
simCpsigStreamLastTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigStreamLastTrigger.setStatus("current")


class _SimCpsigStreamLastEventId_Type(Integer32):
    """Custom type simCpsigStreamLastEventId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimCpsigStreamLastEventId_Type.__name__ = "Integer32"
_SimCpsigStreamLastEventId_Object = MibTableColumn
simCpsigStreamLastEventId = _SimCpsigStreamLastEventId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 3, 1, 8),
    _SimCpsigStreamLastEventId_Type()
)
simCpsigStreamLastEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigStreamLastEventId.setStatus("current")


class _SimCpsigStreamLastServiceId_Type(Integer32):
    """Custom type simCpsigStreamLastServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimCpsigStreamLastServiceId_Type.__name__ = "Integer32"
_SimCpsigStreamLastServiceId_Object = MibTableColumn
simCpsigStreamLastServiceId = _SimCpsigStreamLastServiceId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 3, 1, 9),
    _SimCpsigStreamLastServiceId_Type()
)
simCpsigStreamLastServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigStreamLastServiceId.setStatus("current")


class _SimCpsigStreamLastEsId_Type(Integer32):
    """Custom type simCpsigStreamLastEsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimCpsigStreamLastEsId_Type.__name__ = "Integer32"
_SimCpsigStreamLastEsId_Object = MibTableColumn
simCpsigStreamLastEsId = _SimCpsigStreamLastEsId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 3, 1, 10),
    _SimCpsigStreamLastEsId_Type()
)
simCpsigStreamLastEsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigStreamLastEsId.setStatus("current")


class _SimCpsigStreamLastEcmPid_Type(Integer32):
    """Custom type simCpsigStreamLastEcmPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimCpsigStreamLastEcmPid_Type.__name__ = "Integer32"
_SimCpsigStreamLastEcmPid_Object = MibTableColumn
simCpsigStreamLastEcmPid = _SimCpsigStreamLastEcmPid_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 3, 1, 11),
    _SimCpsigStreamLastEcmPid_Type()
)
simCpsigStreamLastEcmPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigStreamLastEcmPid.setStatus("current")
_SimCpsigStreamErrs_Type = Counter32
_SimCpsigStreamErrs_Object = MibTableColumn
simCpsigStreamErrs = _SimCpsigStreamErrs_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 3, 1, 12),
    _SimCpsigStreamErrs_Type()
)
simCpsigStreamErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigStreamErrs.setStatus("current")
_SimCpsigStreamBytes_Type = Counter32
_SimCpsigStreamBytes_Object = MibTableColumn
simCpsigStreamBytes = _SimCpsigStreamBytes_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 4, 3, 1, 13),
    _SimCpsigStreamBytes_Type()
)
simCpsigStreamBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simCpsigStreamBytes.setStatus("current")
_SimPSI_ObjectIdentity = ObjectIdentity
simPSI = _SimPSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5)
)
_SimPsigTable_Object = MibTable
simPsigTable = _SimPsigTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    simPsigTable.setStatus("current")
_SimPsigEntry_Object = MibTableRow
simPsigEntry = _SimPsigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 1, 1)
)
simPsigEntry.setIndexNames(
    (0, "SIM-MIB", "simPsigIndex"),
)
if mibBuilder.loadTexts:
    simPsigEntry.setStatus("current")


class _SimPsigIndex_Type(Integer32):
    """Custom type simPsigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigIndex_Type.__name__ = "Integer32"
_SimPsigIndex_Object = MibTableColumn
simPsigIndex = _SimPsigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 1, 1, 1),
    _SimPsigIndex_Type()
)
simPsigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simPsigIndex.setStatus("current")
_SimPsigType_Type = PsigType
_SimPsigType_Object = MibTableColumn
simPsigType = _SimPsigType_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 1, 1, 2),
    _SimPsigType_Type()
)
simPsigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simPsigType.setStatus("current")
_SimPsigTriggerSupport_Type = TriggerType
_SimPsigTriggerSupport_Object = MibTableColumn
simPsigTriggerSupport = _SimPsigTriggerSupport_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 1, 1, 3),
    _SimPsigTriggerSupport_Type()
)
simPsigTriggerSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simPsigTriggerSupport.setStatus("current")


class _SimPsigNetworkId_Type(Integer32):
    """Custom type simPsigNetworkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigNetworkId_Type.__name__ = "Integer32"
_SimPsigNetworkId_Object = MibTableColumn
simPsigNetworkId = _SimPsigNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 1, 1, 4),
    _SimPsigNetworkId_Type()
)
simPsigNetworkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simPsigNetworkId.setStatus("current")


class _SimPsigONetworkId_Type(Integer32):
    """Custom type simPsigONetworkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigONetworkId_Type.__name__ = "Integer32"
_SimPsigONetworkId_Object = MibTableColumn
simPsigONetworkId = _SimPsigONetworkId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 1, 1, 5),
    _SimPsigONetworkId_Type()
)
simPsigONetworkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simPsigONetworkId.setStatus("current")


class _SimPsigTransStreamId_Type(Integer32):
    """Custom type simPsigTransStreamId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigTransStreamId_Type.__name__ = "Integer32"
_SimPsigTransStreamId_Object = MibTableColumn
simPsigTransStreamId = _SimPsigTransStreamId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 1, 1, 6),
    _SimPsigTransStreamId_Type()
)
simPsigTransStreamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simPsigTransStreamId.setStatus("current")


class _SimPsigTSServices_Type(OctetString):
    """Custom type simPsigTSServices based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_SimPsigTSServices_Type.__name__ = "OctetString"
_SimPsigTSServices_Object = MibTableColumn
simPsigTSServices = _SimPsigTSServices_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 1, 1, 7),
    _SimPsigTSServices_Type()
)
simPsigTSServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simPsigTSServices.setStatus("current")
_SimPsigConfigTable_Object = MibTable
simPsigConfigTable = _SimPsigConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    simPsigConfigTable.setStatus("current")
_SimPsigConfigEntry_Object = MibTableRow
simPsigConfigEntry = _SimPsigConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 2, 1)
)
simPsigConfigEntry.setIndexNames(
    (0, "SIM-MIB", "simPsigConfigCustCasId"),
    (0, "SIM-MIB", "simPsigConfigIndex"),
    (0, "SIM-MIB", "simPsigIndex"),
)
if mibBuilder.loadTexts:
    simPsigConfigEntry.setStatus("current")


class _SimPsigConfigIndex_Type(Integer32):
    """Custom type simPsigConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigConfigIndex_Type.__name__ = "Integer32"
_SimPsigConfigIndex_Object = MibTableColumn
simPsigConfigIndex = _SimPsigConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 2, 1, 1),
    _SimPsigConfigIndex_Type()
)
simPsigConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    simPsigConfigIndex.setStatus("current")
_SimPsigConfigAdminState_Type = AdministrativeState
_SimPsigConfigAdminState_Object = MibTableColumn
simPsigConfigAdminState = _SimPsigConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 2, 1, 2),
    _SimPsigConfigAdminState_Type()
)
simPsigConfigAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigConfigAdminState.setStatus("current")
_SimPsigConfigCpsigType_Type = PsigType
_SimPsigConfigCpsigType_Object = MibTableColumn
simPsigConfigCpsigType = _SimPsigConfigCpsigType_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 2, 1, 3),
    _SimPsigConfigCpsigType_Type()
)
simPsigConfigCpsigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigConfigCpsigType.setStatus("current")
_SimPsigConfigCustCasId_Type = SuperCasId
_SimPsigConfigCustCasId_Object = MibTableColumn
simPsigConfigCustCasId = _SimPsigConfigCustCasId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 2, 1, 4),
    _SimPsigConfigCustCasId_Type()
)
simPsigConfigCustCasId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigConfigCustCasId.setStatus("current")


class _SimPsigConfigMaxCompTime_Type(Integer32):
    """Custom type simPsigConfigMaxCompTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigConfigMaxCompTime_Type.__name__ = "Integer32"
_SimPsigConfigMaxCompTime_Object = MibTableColumn
simPsigConfigMaxCompTime = _SimPsigConfigMaxCompTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 2, 1, 5),
    _SimPsigConfigMaxCompTime_Type()
)
simPsigConfigMaxCompTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigConfigMaxCompTime.setStatus("current")


class _SimPsigConfigServiceId_Type(Integer32):
    """Custom type simPsigConfigServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigConfigServiceId_Type.__name__ = "Integer32"
_SimPsigConfigServiceId_Object = MibTableColumn
simPsigConfigServiceId = _SimPsigConfigServiceId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 2, 1, 6),
    _SimPsigConfigServiceId_Type()
)
simPsigConfigServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigConfigServiceId.setStatus("current")
_SimPsigConfigTriggerEnable_Type = TriggerType
_SimPsigConfigTriggerEnable_Object = MibTableColumn
simPsigConfigTriggerEnable = _SimPsigConfigTriggerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 2, 1, 7),
    _SimPsigConfigTriggerEnable_Type()
)
simPsigConfigTriggerEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigConfigTriggerEnable.setStatus("current")
_SimPsigConfigCADInsMode_Type = CaDescInsMode
_SimPsigConfigCADInsMode_Object = MibTableColumn
simPsigConfigCADInsMode = _SimPsigConfigCADInsMode_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 2, 1, 8),
    _SimPsigConfigCADInsMode_Type()
)
simPsigConfigCADInsMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigConfigCADInsMode.setStatus("current")
_SimPsigConfigEntryStatus_Type = RowStatus
_SimPsigConfigEntryStatus_Object = MibTableColumn
simPsigConfigEntryStatus = _SimPsigConfigEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 2, 1, 9),
    _SimPsigConfigEntryStatus_Type()
)
simPsigConfigEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigConfigEntryStatus.setStatus("current")
_SimPsigEcmTrTable_Object = MibTable
simPsigEcmTrTable = _SimPsigEcmTrTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    simPsigEcmTrTable.setStatus("current")
_SimPsigEcmTrEntry_Object = MibTableRow
simPsigEcmTrEntry = _SimPsigEcmTrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 3, 1)
)
simPsigEcmTrEntry.setIndexNames(
    (0, "SIM-MIB", "simPsigEcmTrIndex"),
)
if mibBuilder.loadTexts:
    simPsigEcmTrEntry.setStatus("current")


class _SimPsigEcmTrIndex_Type(Integer32):
    """Custom type simPsigEcmTrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigEcmTrIndex_Type.__name__ = "Integer32"
_SimPsigEcmTrIndex_Object = MibTableColumn
simPsigEcmTrIndex = _SimPsigEcmTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 3, 1, 1),
    _SimPsigEcmTrIndex_Type()
)
simPsigEcmTrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    simPsigEcmTrIndex.setStatus("current")


class _SimPsigEcmTrNetworkId_Type(Integer32):
    """Custom type simPsigEcmTrNetworkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigEcmTrNetworkId_Type.__name__ = "Integer32"
_SimPsigEcmTrNetworkId_Object = MibTableColumn
simPsigEcmTrNetworkId = _SimPsigEcmTrNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 3, 1, 2),
    _SimPsigEcmTrNetworkId_Type()
)
simPsigEcmTrNetworkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigEcmTrNetworkId.setStatus("current")


class _SimPsigEcmTrONetworkId_Type(Integer32):
    """Custom type simPsigEcmTrONetworkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigEcmTrONetworkId_Type.__name__ = "Integer32"
_SimPsigEcmTrONetworkId_Object = MibTableColumn
simPsigEcmTrONetworkId = _SimPsigEcmTrONetworkId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 3, 1, 3),
    _SimPsigEcmTrONetworkId_Type()
)
simPsigEcmTrONetworkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigEcmTrONetworkId.setStatus("current")


class _SimPsigEcmTrTransStreamId_Type(Integer32):
    """Custom type simPsigEcmTrTransStreamId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigEcmTrTransStreamId_Type.__name__ = "Integer32"
_SimPsigEcmTrTransStreamId_Object = MibTableColumn
simPsigEcmTrTransStreamId = _SimPsigEcmTrTransStreamId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 3, 1, 4),
    _SimPsigEcmTrTransStreamId_Type()
)
simPsigEcmTrTransStreamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigEcmTrTransStreamId.setStatus("current")


class _SimPsigEcmTrServiceId_Type(Integer32):
    """Custom type simPsigEcmTrServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigEcmTrServiceId_Type.__name__ = "Integer32"
_SimPsigEcmTrServiceId_Object = MibTableColumn
simPsigEcmTrServiceId = _SimPsigEcmTrServiceId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 3, 1, 5),
    _SimPsigEcmTrServiceId_Type()
)
simPsigEcmTrServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigEcmTrServiceId.setStatus("current")


class _SimPsigEcmTrEsId_Type(Integer32):
    """Custom type simPsigEcmTrEsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigEcmTrEsId_Type.__name__ = "Integer32"
_SimPsigEcmTrEsId_Object = MibTableColumn
simPsigEcmTrEsId = _SimPsigEcmTrEsId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 3, 1, 6),
    _SimPsigEcmTrEsId_Type()
)
simPsigEcmTrEsId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigEcmTrEsId.setStatus("current")
_SimPsigEcmTrType_Type = ECMTriggerType
_SimPsigEcmTrType_Object = MibTableColumn
simPsigEcmTrType = _SimPsigEcmTrType_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 3, 1, 7),
    _SimPsigEcmTrType_Type()
)
simPsigEcmTrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigEcmTrType.setStatus("current")
_SimPsigEcmTrSuCasId_Type = SuperCasId
_SimPsigEcmTrSuCasId_Object = MibTableColumn
simPsigEcmTrSuCasId = _SimPsigEcmTrSuCasId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 3, 1, 8),
    _SimPsigEcmTrSuCasId_Type()
)
simPsigEcmTrSuCasId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigEcmTrSuCasId.setStatus("current")
_SimPsigEcmTrEcmId_Type = FlowId
_SimPsigEcmTrEcmId_Object = MibTableColumn
simPsigEcmTrEcmId = _SimPsigEcmTrEcmId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 3, 1, 9),
    _SimPsigEcmTrEcmId_Type()
)
simPsigEcmTrEcmId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigEcmTrEcmId.setStatus("current")


class _SimPsigEcmTrEcmPid_Type(Integer32):
    """Custom type simPsigEcmTrEcmPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigEcmTrEcmPid_Type.__name__ = "Integer32"
_SimPsigEcmTrEcmPid_Object = MibTableColumn
simPsigEcmTrEcmPid = _SimPsigEcmTrEcmPid_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 3, 1, 10),
    _SimPsigEcmTrEcmPid_Type()
)
simPsigEcmTrEcmPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigEcmTrEcmPid.setStatus("current")


class _SimPsigEcmTrAccessCriteria_Type(OctetString):
    """Custom type simPsigEcmTrAccessCriteria based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SimPsigEcmTrAccessCriteria_Type.__name__ = "OctetString"
_SimPsigEcmTrAccessCriteria_Object = MibTableColumn
simPsigEcmTrAccessCriteria = _SimPsigEcmTrAccessCriteria_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 3, 1, 11),
    _SimPsigEcmTrAccessCriteria_Type()
)
simPsigEcmTrAccessCriteria.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigEcmTrAccessCriteria.setStatus("current")
_SimPsigFlowTrTable_Object = MibTable
simPsigFlowTrTable = _SimPsigFlowTrTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    simPsigFlowTrTable.setStatus("current")
_SimPsigFlowTrEntry_Object = MibTableRow
simPsigFlowTrEntry = _SimPsigFlowTrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 4, 1)
)
simPsigFlowTrEntry.setIndexNames(
    (0, "SIM-MIB", "simPsigFlowTrIndex"),
)
if mibBuilder.loadTexts:
    simPsigFlowTrEntry.setStatus("current")


class _SimPsigFlowTrIndex_Type(Integer32):
    """Custom type simPsigFlowTrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigFlowTrIndex_Type.__name__ = "Integer32"
_SimPsigFlowTrIndex_Object = MibTableColumn
simPsigFlowTrIndex = _SimPsigFlowTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 4, 1, 1),
    _SimPsigFlowTrIndex_Type()
)
simPsigFlowTrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigFlowTrIndex.setStatus("current")
_SimPsigFlowTrType_Type = FlowType
_SimPsigFlowTrType_Object = MibTableColumn
simPsigFlowTrType = _SimPsigFlowTrType_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 4, 1, 2),
    _SimPsigFlowTrType_Type()
)
simPsigFlowTrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigFlowTrType.setStatus("current")
_SimPsigFlowTrSuCasId_Type = SuperCasId
_SimPsigFlowTrSuCasId_Object = MibTableColumn
simPsigFlowTrSuCasId = _SimPsigFlowTrSuCasId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 4, 1, 3),
    _SimPsigFlowTrSuCasId_Type()
)
simPsigFlowTrSuCasId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigFlowTrSuCasId.setStatus("current")
_SimPsigFlowTrFlowId_Type = FlowId
_SimPsigFlowTrFlowId_Object = MibTableColumn
simPsigFlowTrFlowId = _SimPsigFlowTrFlowId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 4, 1, 4),
    _SimPsigFlowTrFlowId_Type()
)
simPsigFlowTrFlowId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigFlowTrFlowId.setStatus("current")


class _SimPsigFlowTrFlowPID_Type(Integer32):
    """Custom type simPsigFlowTrFlowPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigFlowTrFlowPID_Type.__name__ = "Integer32"
_SimPsigFlowTrFlowPID_Object = MibTableColumn
simPsigFlowTrFlowPID = _SimPsigFlowTrFlowPID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 4, 1, 5),
    _SimPsigFlowTrFlowPID_Type()
)
simPsigFlowTrFlowPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigFlowTrFlowPID.setStatus("current")
_SimPsigEvntTrTable_Object = MibTable
simPsigEvntTrTable = _SimPsigEvntTrTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 5)
)
if mibBuilder.loadTexts:
    simPsigEvntTrTable.setStatus("current")
_SimPsigEvntTrEntry_Object = MibTableRow
simPsigEvntTrEntry = _SimPsigEvntTrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 5, 1)
)
simPsigEvntTrEntry.setIndexNames(
    (0, "SIM-MIB", "simPsigEvntTrIndex"),
)
if mibBuilder.loadTexts:
    simPsigEvntTrEntry.setStatus("current")


class _SimPsigEvntTrIndex_Type(Integer32):
    """Custom type simPsigEvntTrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigEvntTrIndex_Type.__name__ = "Integer32"
_SimPsigEvntTrIndex_Object = MibTableColumn
simPsigEvntTrIndex = _SimPsigEvntTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 5, 1, 1),
    _SimPsigEvntTrIndex_Type()
)
simPsigEvntTrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    simPsigEvntTrIndex.setStatus("current")


class _SimPsigEvntTrNetworkId_Type(Integer32):
    """Custom type simPsigEvntTrNetworkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigEvntTrNetworkId_Type.__name__ = "Integer32"
_SimPsigEvntTrNetworkId_Object = MibTableColumn
simPsigEvntTrNetworkId = _SimPsigEvntTrNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 5, 1, 2),
    _SimPsigEvntTrNetworkId_Type()
)
simPsigEvntTrNetworkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigEvntTrNetworkId.setStatus("current")


class _SimPsigEvntTrONetworkId_Type(Integer32):
    """Custom type simPsigEvntTrONetworkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigEvntTrONetworkId_Type.__name__ = "Integer32"
_SimPsigEvntTrONetworkId_Object = MibTableColumn
simPsigEvntTrONetworkId = _SimPsigEvntTrONetworkId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 5, 1, 3),
    _SimPsigEvntTrONetworkId_Type()
)
simPsigEvntTrONetworkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigEvntTrONetworkId.setStatus("current")


class _SimPsigEvntTrTransStreamId_Type(Integer32):
    """Custom type simPsigEvntTrTransStreamId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigEvntTrTransStreamId_Type.__name__ = "Integer32"
_SimPsigEvntTrTransStreamId_Object = MibTableColumn
simPsigEvntTrTransStreamId = _SimPsigEvntTrTransStreamId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 5, 1, 4),
    _SimPsigEvntTrTransStreamId_Type()
)
simPsigEvntTrTransStreamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigEvntTrTransStreamId.setStatus("current")


class _SimPsigEvntTrServiceId_Type(Integer32):
    """Custom type simPsigEvntTrServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigEvntTrServiceId_Type.__name__ = "Integer32"
_SimPsigEvntTrServiceId_Object = MibTableColumn
simPsigEvntTrServiceId = _SimPsigEvntTrServiceId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 5, 1, 5),
    _SimPsigEvntTrServiceId_Type()
)
simPsigEvntTrServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigEvntTrServiceId.setStatus("current")


class _SimPsigEvntTrEventId_Type(Integer32):
    """Custom type simPsigEvntTrEventId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigEvntTrEventId_Type.__name__ = "Integer32"
_SimPsigEvntTrEventId_Object = MibTableColumn
simPsigEvntTrEventId = _SimPsigEvntTrEventId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 5, 1, 6),
    _SimPsigEvntTrEventId_Type()
)
simPsigEvntTrEventId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigEvntTrEventId.setStatus("current")


class _SimPsigEvntTrStartTime_Type(OctetString):
    """Custom type simPsigEvntTrStartTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SimPsigEvntTrStartTime_Type.__name__ = "OctetString"
_SimPsigEvntTrStartTime_Object = MibTableColumn
simPsigEvntTrStartTime = _SimPsigEvntTrStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 5, 1, 7),
    _SimPsigEvntTrStartTime_Type()
)
simPsigEvntTrStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigEvntTrStartTime.setStatus("current")


class _SimPsigEvntTrDuration_Type(OctetString):
    """Custom type simPsigEvntTrDuration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_SimPsigEvntTrDuration_Type.__name__ = "OctetString"
_SimPsigEvntTrDuration_Object = MibTableColumn
simPsigEvntTrDuration = _SimPsigEvntTrDuration_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 5, 1, 8),
    _SimPsigEvntTrDuration_Type()
)
simPsigEvntTrDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigEvntTrDuration.setStatus("current")


class _SimPsigEvntTrPrivateData_Type(OctetString):
    """Custom type simPsigEvntTrPrivateData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SimPsigEvntTrPrivateData_Type.__name__ = "OctetString"
_SimPsigEvntTrPrivateData_Object = MibTableColumn
simPsigEvntTrPrivateData = _SimPsigEvntTrPrivateData_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 5, 1, 9),
    _SimPsigEvntTrPrivateData_Type()
)
simPsigEvntTrPrivateData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigEvntTrPrivateData.setStatus("current")
_SimPsigDescInsTable_Object = MibTable
simPsigDescInsTable = _SimPsigDescInsTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6)
)
if mibBuilder.loadTexts:
    simPsigDescInsTable.setStatus("current")
_SimPsigDescInsEntry_Object = MibTableRow
simPsigDescInsEntry = _SimPsigDescInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1)
)
simPsigDescInsEntry.setIndexNames(
    (0, "SIM-MIB", "simPsigDescInsIndex"),
)
if mibBuilder.loadTexts:
    simPsigDescInsEntry.setStatus("current")


class _SimPsigDescInsIndex_Type(Integer32):
    """Custom type simPsigDescInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigDescInsIndex_Type.__name__ = "Integer32"
_SimPsigDescInsIndex_Object = MibTableColumn
simPsigDescInsIndex = _SimPsigDescInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 1),
    _SimPsigDescInsIndex_Type()
)
simPsigDescInsIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsIndex.setStatus("current")
_SimPsigDescInsAdminState_Type = AdministrativeState
_SimPsigDescInsAdminState_Object = MibTableColumn
simPsigDescInsAdminState = _SimPsigDescInsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 2),
    _SimPsigDescInsAdminState_Type()
)
simPsigDescInsAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsAdminState.setStatus("current")


class _SimPsigDescInsTrIndex_Type(Integer32):
    """Custom type simPsigDescInsTrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigDescInsTrIndex_Type.__name__ = "Integer32"
_SimPsigDescInsTrIndex_Object = MibTableColumn
simPsigDescInsTrIndex = _SimPsigDescInsTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 3),
    _SimPsigDescInsTrIndex_Type()
)
simPsigDescInsTrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsTrIndex.setStatus("current")
_SimPsigDescInsTrType_Type = TriggerType
_SimPsigDescInsTrType_Object = MibTableColumn
simPsigDescInsTrType = _SimPsigDescInsTrType_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 4),
    _SimPsigDescInsTrType_Type()
)
simPsigDescInsTrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsTrType.setStatus("current")
_SimPsigDescInsLocationId_Type = InsertLocation
_SimPsigDescInsLocationId_Object = MibTableColumn
simPsigDescInsLocationId = _SimPsigDescInsLocationId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 5),
    _SimPsigDescInsLocationId_Type()
)
simPsigDescInsLocationId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsLocationId.setStatus("current")


class _SimPsigDescInsNetworkId_Type(Integer32):
    """Custom type simPsigDescInsNetworkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigDescInsNetworkId_Type.__name__ = "Integer32"
_SimPsigDescInsNetworkId_Object = MibTableColumn
simPsigDescInsNetworkId = _SimPsigDescInsNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 6),
    _SimPsigDescInsNetworkId_Type()
)
simPsigDescInsNetworkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsNetworkId.setStatus("current")


class _SimPsigDescInsONetworkId_Type(Integer32):
    """Custom type simPsigDescInsONetworkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigDescInsONetworkId_Type.__name__ = "Integer32"
_SimPsigDescInsONetworkId_Object = MibTableColumn
simPsigDescInsONetworkId = _SimPsigDescInsONetworkId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 7),
    _SimPsigDescInsONetworkId_Type()
)
simPsigDescInsONetworkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsONetworkId.setStatus("current")


class _SimPsigDescInsTransStreamId_Type(Integer32):
    """Custom type simPsigDescInsTransStreamId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigDescInsTransStreamId_Type.__name__ = "Integer32"
_SimPsigDescInsTransStreamId_Object = MibTableColumn
simPsigDescInsTransStreamId = _SimPsigDescInsTransStreamId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 8),
    _SimPsigDescInsTransStreamId_Type()
)
simPsigDescInsTransStreamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsTransStreamId.setStatus("current")


class _SimPsigDescInsServiceId_Type(Integer32):
    """Custom type simPsigDescInsServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigDescInsServiceId_Type.__name__ = "Integer32"
_SimPsigDescInsServiceId_Object = MibTableColumn
simPsigDescInsServiceId = _SimPsigDescInsServiceId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 9),
    _SimPsigDescInsServiceId_Type()
)
simPsigDescInsServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsServiceId.setStatus("current")


class _SimPsigDescInsElmStreamId_Type(Integer32):
    """Custom type simPsigDescInsElmStreamId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigDescInsElmStreamId_Type.__name__ = "Integer32"
_SimPsigDescInsElmStreamId_Object = MibTableColumn
simPsigDescInsElmStreamId = _SimPsigDescInsElmStreamId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 10),
    _SimPsigDescInsElmStreamId_Type()
)
simPsigDescInsElmStreamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsElmStreamId.setStatus("current")


class _SimPsigDescInsBouquetId_Type(Integer32):
    """Custom type simPsigDescInsBouquetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigDescInsBouquetId_Type.__name__ = "Integer32"
_SimPsigDescInsBouquetId_Object = MibTableColumn
simPsigDescInsBouquetId = _SimPsigDescInsBouquetId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 11),
    _SimPsigDescInsBouquetId_Type()
)
simPsigDescInsBouquetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsBouquetId.setStatus("current")


class _SimPsigDescInsEventId_Type(Integer32):
    """Custom type simPsigDescInsEventId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigDescInsEventId_Type.__name__ = "Integer32"
_SimPsigDescInsEventId_Object = MibTableColumn
simPsigDescInsEventId = _SimPsigDescInsEventId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 12),
    _SimPsigDescInsEventId_Type()
)
simPsigDescInsEventId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsEventId.setStatus("current")


class _SimPsigDescInsONetworkId2loop_Type(Integer32):
    """Custom type simPsigDescInsONetworkId2loop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigDescInsONetworkId2loop_Type.__name__ = "Integer32"
_SimPsigDescInsONetworkId2loop_Object = MibTableColumn
simPsigDescInsONetworkId2loop = _SimPsigDescInsONetworkId2loop_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 13),
    _SimPsigDescInsONetworkId2loop_Type()
)
simPsigDescInsONetworkId2loop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsONetworkId2loop.setStatus("current")


class _SimPsigDescInsNetworkIdOther_Type(Integer32):
    """Custom type simPsigDescInsNetworkIdOther based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigDescInsNetworkIdOther_Type.__name__ = "Integer32"
_SimPsigDescInsNetworkIdOther_Object = MibTableColumn
simPsigDescInsNetworkIdOther = _SimPsigDescInsNetworkIdOther_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 14),
    _SimPsigDescInsNetworkIdOther_Type()
)
simPsigDescInsNetworkIdOther.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsNetworkIdOther.setStatus("current")


class _SimPsigDescInsTransStreamId2OrO_Type(Integer32):
    """Custom type simPsigDescInsTransStreamId2OrO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigDescInsTransStreamId2OrO_Type.__name__ = "Integer32"
_SimPsigDescInsTransStreamId2OrO_Object = MibTableColumn
simPsigDescInsTransStreamId2OrO = _SimPsigDescInsTransStreamId2OrO_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 15),
    _SimPsigDescInsTransStreamId2OrO_Type()
)
simPsigDescInsTransStreamId2OrO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsTransStreamId2OrO.setStatus("current")
_SimPsigDescInsDelayType_Type = DelayType
_SimPsigDescInsDelayType_Object = MibTableColumn
simPsigDescInsDelayType = _SimPsigDescInsDelayType_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 16),
    _SimPsigDescInsDelayType_Type()
)
simPsigDescInsDelayType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsDelayType.setStatus("current")


class _SimPsigDescInsDelay_Type(OctetString):
    """Custom type simPsigDescInsDelay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_SimPsigDescInsDelay_Type.__name__ = "OctetString"
_SimPsigDescInsDelay_Object = MibTableColumn
simPsigDescInsDelay = _SimPsigDescInsDelay_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 17),
    _SimPsigDescInsDelay_Type()
)
simPsigDescInsDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsDelay.setStatus("current")


class _SimPsigDescPrivDataSpfier_Type(Integer32):
    """Custom type simPsigDescPrivDataSpfier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigDescPrivDataSpfier_Type.__name__ = "Integer32"
_SimPsigDescPrivDataSpfier_Object = MibTableColumn
simPsigDescPrivDataSpfier = _SimPsigDescPrivDataSpfier_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 18),
    _SimPsigDescPrivDataSpfier_Type()
)
simPsigDescPrivDataSpfier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescPrivDataSpfier.setStatus("current")
_SimPsigDescInsEntryStatus_Type = RowStatus
_SimPsigDescInsEntryStatus_Object = MibTableColumn
simPsigDescInsEntryStatus = _SimPsigDescInsEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 6, 1, 19),
    _SimPsigDescInsEntryStatus_Type()
)
simPsigDescInsEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsEntryStatus.setStatus("current")
_SimPsigDescInsDescTable_Object = MibTable
simPsigDescInsDescTable = _SimPsigDescInsDescTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 7)
)
if mibBuilder.loadTexts:
    simPsigDescInsDescTable.setStatus("current")
_SimPsigDescInsDescEntry_Object = MibTableRow
simPsigDescInsDescEntry = _SimPsigDescInsDescEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 7, 1)
)
simPsigDescInsDescEntry.setIndexNames(
    (0, "SIM-MIB", "simPsigDescInsIndex"),
    (0, "SIM-MIB", "simPsigDescInsDescIndex"),
)
if mibBuilder.loadTexts:
    simPsigDescInsDescEntry.setStatus("current")


class _SimPsigDescInsDescIndex_Type(Integer32):
    """Custom type simPsigDescInsDescIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigDescInsDescIndex_Type.__name__ = "Integer32"
_SimPsigDescInsDescIndex_Object = MibTableColumn
simPsigDescInsDescIndex = _SimPsigDescInsDescIndex_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 7, 1, 1),
    _SimPsigDescInsDescIndex_Type()
)
simPsigDescInsDescIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsDescIndex.setStatus("current")
_SimPsigDescInsDescAdminState_Type = AdministrativeState
_SimPsigDescInsDescAdminState_Object = MibTableColumn
simPsigDescInsDescAdminState = _SimPsigDescInsDescAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 7, 1, 2),
    _SimPsigDescInsDescAdminState_Type()
)
simPsigDescInsDescAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsDescAdminState.setStatus("current")


class _SimPsigDescInsDescriptor_Type(OctetString):
    """Custom type simPsigDescInsDescriptor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8191),
    )


_SimPsigDescInsDescriptor_Type.__name__ = "OctetString"
_SimPsigDescInsDescriptor_Object = MibTableColumn
simPsigDescInsDescriptor = _SimPsigDescInsDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 7, 1, 3),
    _SimPsigDescInsDescriptor_Type()
)
simPsigDescInsDescriptor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsDescriptor.setStatus("current")
_SimPsigDescInsDescriptorStatus_Type = DescriptorStatus
_SimPsigDescInsDescriptorStatus_Object = MibTableColumn
simPsigDescInsDescriptorStatus = _SimPsigDescInsDescriptorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 7, 1, 4),
    _SimPsigDescInsDescriptorStatus_Type()
)
simPsigDescInsDescriptorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsDescriptorStatus.setStatus("current")
_SimPsigDescInsDescEntryStatus_Type = RowStatus
_SimPsigDescInsDescEntryStatus_Object = MibTableColumn
simPsigDescInsDescEntryStatus = _SimPsigDescInsDescEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 7, 1, 5),
    _SimPsigDescInsDescEntryStatus_Type()
)
simPsigDescInsDescEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigDescInsDescEntryStatus.setStatus("current")
_SimPsigTblProvTable_Object = MibTable
simPsigTblProvTable = _SimPsigTblProvTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 8)
)
if mibBuilder.loadTexts:
    simPsigTblProvTable.setStatus("current")
_SimPsigTblProvEntry_Object = MibTableRow
simPsigTblProvEntry = _SimPsigTblProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 8, 1)
)
simPsigTblProvEntry.setIndexNames(
    (0, "SIM-MIB", "simPsigTblProvIndex"),
)
if mibBuilder.loadTexts:
    simPsigTblProvEntry.setStatus("current")


class _SimPsigTblProvIndex_Type(Integer32):
    """Custom type simPsigTblProvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigTblProvIndex_Type.__name__ = "Integer32"
_SimPsigTblProvIndex_Object = MibTableColumn
simPsigTblProvIndex = _SimPsigTblProvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 8, 1, 1),
    _SimPsigTblProvIndex_Type()
)
simPsigTblProvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simPsigTblProvIndex.setStatus("current")
_SimPsigTblProvTableId_Type = ProvTableId
_SimPsigTblProvTableId_Object = MibTableColumn
simPsigTblProvTableId = _SimPsigTblProvTableId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 8, 1, 2),
    _SimPsigTblProvTableId_Type()
)
simPsigTblProvTableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simPsigTblProvTableId.setStatus("current")


class _SimPsigTblNetworkId_Type(Integer32):
    """Custom type simPsigTblNetworkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigTblNetworkId_Type.__name__ = "Integer32"
_SimPsigTblNetworkId_Object = MibTableColumn
simPsigTblNetworkId = _SimPsigTblNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 8, 1, 3),
    _SimPsigTblNetworkId_Type()
)
simPsigTblNetworkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigTblNetworkId.setStatus("current")


class _SimPsigTblONetworkId_Type(Integer32):
    """Custom type simPsigTblONetworkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigTblONetworkId_Type.__name__ = "Integer32"
_SimPsigTblONetworkId_Object = MibTableColumn
simPsigTblONetworkId = _SimPsigTblONetworkId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 8, 1, 4),
    _SimPsigTblONetworkId_Type()
)
simPsigTblONetworkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigTblONetworkId.setStatus("current")


class _SimPsigTblTransStreamId_Type(Integer32):
    """Custom type simPsigTblTransStreamId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigTblTransStreamId_Type.__name__ = "Integer32"
_SimPsigTblTransStreamId_Object = MibTableColumn
simPsigTblTransStreamId = _SimPsigTblTransStreamId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 8, 1, 5),
    _SimPsigTblTransStreamId_Type()
)
simPsigTblTransStreamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigTblTransStreamId.setStatus("current")


class _SimPsigTblServiceId_Type(Integer32):
    """Custom type simPsigTblServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigTblServiceId_Type.__name__ = "Integer32"
_SimPsigTblServiceId_Object = MibTableColumn
simPsigTblServiceId = _SimPsigTblServiceId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 8, 1, 6),
    _SimPsigTblServiceId_Type()
)
simPsigTblServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigTblServiceId.setStatus("current")


class _SimPsigTblBouquetId_Type(Integer32):
    """Custom type simPsigTblBouquetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigTblBouquetId_Type.__name__ = "Integer32"
_SimPsigTblBouquetId_Object = MibTableColumn
simPsigTblBouquetId = _SimPsigTblBouquetId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 8, 1, 7),
    _SimPsigTblBouquetId_Type()
)
simPsigTblBouquetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigTblBouquetId.setStatus("current")


class _SimPsigTblEventId_Type(Integer32):
    """Custom type simPsigTblEventId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigTblEventId_Type.__name__ = "Integer32"
_SimPsigTblEventId_Object = MibTableColumn
simPsigTblEventId = _SimPsigTblEventId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 8, 1, 8),
    _SimPsigTblEventId_Type()
)
simPsigTblEventId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigTblEventId.setStatus("current")


class _SimPsigTblONetworkId2loop_Type(Integer32):
    """Custom type simPsigTblONetworkId2loop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigTblONetworkId2loop_Type.__name__ = "Integer32"
_SimPsigTblONetworkId2loop_Object = MibTableColumn
simPsigTblONetworkId2loop = _SimPsigTblONetworkId2loop_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 8, 1, 9),
    _SimPsigTblONetworkId2loop_Type()
)
simPsigTblONetworkId2loop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigTblONetworkId2loop.setStatus("current")


class _SimPsigTblNetworkIdOther_Type(Integer32):
    """Custom type simPsigTblNetworkIdOther based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigTblNetworkIdOther_Type.__name__ = "Integer32"
_SimPsigTblNetworkIdOther_Object = MibTableColumn
simPsigTblNetworkIdOther = _SimPsigTblNetworkIdOther_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 8, 1, 10),
    _SimPsigTblNetworkIdOther_Type()
)
simPsigTblNetworkIdOther.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigTblNetworkIdOther.setStatus("current")


class _SimPsigTblTransStreamId2OrO_Type(Integer32):
    """Custom type simPsigTblTransStreamId2OrO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigTblTransStreamId2OrO_Type.__name__ = "Integer32"
_SimPsigTblTransStreamId2OrO_Object = MibTableColumn
simPsigTblTransStreamId2OrO = _SimPsigTblTransStreamId2OrO_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 8, 1, 11),
    _SimPsigTblTransStreamId2OrO_Type()
)
simPsigTblTransStreamId2OrO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigTblTransStreamId2OrO.setStatus("current")


class _SimPsigTblSegmentNr_Type(Integer32):
    """Custom type simPsigTblSegmentNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigTblSegmentNr_Type.__name__ = "Integer32"
_SimPsigTblSegmentNr_Object = MibTableColumn
simPsigTblSegmentNr = _SimPsigTblSegmentNr_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 8, 1, 12),
    _SimPsigTblSegmentNr_Type()
)
simPsigTblSegmentNr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigTblSegmentNr.setStatus("current")


class _SimPsigTblProvPart_Type(OctetString):
    """Custom type simPsigTblProvPart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8191),
    )


_SimPsigTblProvPart_Type.__name__ = "OctetString"
_SimPsigTblProvPart_Object = MibTableColumn
simPsigTblProvPart = _SimPsigTblProvPart_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 8, 1, 13),
    _SimPsigTblProvPart_Type()
)
simPsigTblProvPart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigTblProvPart.setStatus("current")


class _SimPsigTblProvPartNumber_Type(Integer32):
    """Custom type simPsigTblProvPartNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigTblProvPartNumber_Type.__name__ = "Integer32"
_SimPsigTblProvPartNumber_Object = MibTableColumn
simPsigTblProvPartNumber = _SimPsigTblProvPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 8, 1, 14),
    _SimPsigTblProvPartNumber_Type()
)
simPsigTblProvPartNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigTblProvPartNumber.setStatus("current")
_SimPsigPIDProvTable_Object = MibTable
simPsigPIDProvTable = _SimPsigPIDProvTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 9)
)
if mibBuilder.loadTexts:
    simPsigPIDProvTable.setStatus("current")
_SimPsigPIDProvEntry_Object = MibTableRow
simPsigPIDProvEntry = _SimPsigPIDProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 9, 1)
)
simPsigPIDProvEntry.setIndexNames(
    (0, "SIM-MIB", "simPsigPIDProvSuCasId"),
    (0, "SIM-MIB", "simPsigPIDProvFlowId"),
)
if mibBuilder.loadTexts:
    simPsigPIDProvEntry.setStatus("current")
_SimPsigPIDProvFlowType_Type = FlowType
_SimPsigPIDProvFlowType_Object = MibTableColumn
simPsigPIDProvFlowType = _SimPsigPIDProvFlowType_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 9, 1, 1),
    _SimPsigPIDProvFlowType_Type()
)
simPsigPIDProvFlowType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simPsigPIDProvFlowType.setStatus("current")
_SimPsigPIDProvSuCasId_Type = SuperCasId
_SimPsigPIDProvSuCasId_Object = MibTableColumn
simPsigPIDProvSuCasId = _SimPsigPIDProvSuCasId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 9, 1, 2),
    _SimPsigPIDProvSuCasId_Type()
)
simPsigPIDProvSuCasId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simPsigPIDProvSuCasId.setStatus("current")
_SimPsigPIDProvFlowId_Type = FlowId
_SimPsigPIDProvFlowId_Object = MibTableColumn
simPsigPIDProvFlowId = _SimPsigPIDProvFlowId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 9, 1, 3),
    _SimPsigPIDProvFlowId_Type()
)
simPsigPIDProvFlowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simPsigPIDProvFlowId.setStatus("current")


class _SimPsigPIDProvFlowPID_Type(Integer32):
    """Custom type simPsigPIDProvFlowPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigPIDProvFlowPID_Type.__name__ = "Integer32"
_SimPsigPIDProvFlowPID_Object = MibTableColumn
simPsigPIDProvFlowPID = _SimPsigPIDProvFlowPID_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 9, 1, 4),
    _SimPsigPIDProvFlowPID_Type()
)
simPsigPIDProvFlowPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simPsigPIDProvFlowPID.setStatus("current")
_SimPsigPdTrTable_Object = MibTable
simPsigPdTrTable = _SimPsigPdTrTable_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 10)
)
if mibBuilder.loadTexts:
    simPsigPdTrTable.setStatus("current")
_SimPsigPdTrEntry_Object = MibTableRow
simPsigPdTrEntry = _SimPsigPdTrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 10, 1)
)
simPsigPdTrEntry.setIndexNames(
    (0, "SIM-MIB", "simPsigPdTrIndex"),
)
if mibBuilder.loadTexts:
    simPsigPdTrEntry.setStatus("current")


class _SimPsigPdTrIndex_Type(Integer32):
    """Custom type simPsigPdTrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigPdTrIndex_Type.__name__ = "Integer32"
_SimPsigPdTrIndex_Object = MibTableColumn
simPsigPdTrIndex = _SimPsigPdTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 10, 1, 1),
    _SimPsigPdTrIndex_Type()
)
simPsigPdTrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    simPsigPdTrIndex.setStatus("current")


class _SimPsigPdTrNetworkId_Type(Integer32):
    """Custom type simPsigPdTrNetworkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigPdTrNetworkId_Type.__name__ = "Integer32"
_SimPsigPdTrNetworkId_Object = MibTableColumn
simPsigPdTrNetworkId = _SimPsigPdTrNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 10, 1, 2),
    _SimPsigPdTrNetworkId_Type()
)
simPsigPdTrNetworkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigPdTrNetworkId.setStatus("current")


class _SimPsigPdTrONetworkId_Type(Integer32):
    """Custom type simPsigPdTrONetworkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigPdTrONetworkId_Type.__name__ = "Integer32"
_SimPsigPdTrONetworkId_Object = MibTableColumn
simPsigPdTrONetworkId = _SimPsigPdTrONetworkId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 10, 1, 3),
    _SimPsigPdTrONetworkId_Type()
)
simPsigPdTrONetworkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigPdTrONetworkId.setStatus("current")


class _SimPsigPdTrTransStreamId_Type(Integer32):
    """Custom type simPsigPdTrTransStreamId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigPdTrTransStreamId_Type.__name__ = "Integer32"
_SimPsigPdTrTransStreamId_Object = MibTableColumn
simPsigPdTrTransStreamId = _SimPsigPdTrTransStreamId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 10, 1, 4),
    _SimPsigPdTrTransStreamId_Type()
)
simPsigPdTrTransStreamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigPdTrTransStreamId.setStatus("current")


class _SimPsigPdTrServiceId_Type(Integer32):
    """Custom type simPsigPdTrServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigPdTrServiceId_Type.__name__ = "Integer32"
_SimPsigPdTrServiceId_Object = MibTableColumn
simPsigPdTrServiceId = _SimPsigPdTrServiceId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 10, 1, 5),
    _SimPsigPdTrServiceId_Type()
)
simPsigPdTrServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigPdTrServiceId.setStatus("current")


class _SimPsigPdTrEsId_Type(Integer32):
    """Custom type simPsigPdTrEsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigPdTrEsId_Type.__name__ = "Integer32"
_SimPsigPdTrEsId_Object = MibTableColumn
simPsigPdTrEsId = _SimPsigPdTrEsId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 10, 1, 6),
    _SimPsigPdTrEsId_Type()
)
simPsigPdTrEsId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigPdTrEsId.setStatus("current")
_SimPsigPdTrType_Type = ECMTriggerType
_SimPsigPdTrType_Object = MibTableColumn
simPsigPdTrType = _SimPsigPdTrType_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 10, 1, 7),
    _SimPsigPdTrType_Type()
)
simPsigPdTrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigPdTrType.setStatus("current")
_SimPsigPdTrSuCasId_Type = SuperCasId
_SimPsigPdTrSuCasId_Object = MibTableColumn
simPsigPdTrSuCasId = _SimPsigPdTrSuCasId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 10, 1, 8),
    _SimPsigPdTrSuCasId_Type()
)
simPsigPdTrSuCasId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigPdTrSuCasId.setStatus("current")
_SimPsigPdTrPdId_Type = FlowId
_SimPsigPdTrPdId_Object = MibTableColumn
simPsigPdTrPdId = _SimPsigPdTrPdId_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 10, 1, 9),
    _SimPsigPdTrPdId_Type()
)
simPsigPdTrPdId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigPdTrPdId.setStatus("current")


class _SimPsigPdTrPdPid_Type(Integer32):
    """Custom type simPsigPdTrPdPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SimPsigPdTrPdPid_Type.__name__ = "Integer32"
_SimPsigPdTrPdPid_Object = MibTableColumn
simPsigPdTrPdPid = _SimPsigPdTrPdPid_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 10, 1, 10),
    _SimPsigPdTrPdPid_Type()
)
simPsigPdTrPdPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigPdTrPdPid.setStatus("current")


class _SimPsigPdTrPdStreamType_Type(Integer32):
    """Custom type simPsigPdTrPdStreamType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SimPsigPdTrPdStreamType_Type.__name__ = "Integer32"
_SimPsigPdTrPdStreamType_Object = MibTableColumn
simPsigPdTrPdStreamType = _SimPsigPdTrPdStreamType_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 10, 1, 11),
    _SimPsigPdTrPdStreamType_Type()
)
simPsigPdTrPdStreamType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigPdTrPdStreamType.setStatus("current")


class _SimPsigPdTrPrivateData_Type(OctetString):
    """Custom type simPsigPdTrPrivateData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SimPsigPdTrPrivateData_Type.__name__ = "OctetString"
_SimPsigPdTrPrivateData_Object = MibTableColumn
simPsigPdTrPrivateData = _SimPsigPdTrPrivateData_Object(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 1, 5, 10, 1, 12),
    _SimPsigPdTrPrivateData_Type()
)
simPsigPdTrPrivateData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    simPsigPdTrPrivateData.setStatus("current")
_SimMIBConformance_ObjectIdentity = ObjectIdentity
simMIBConformance = _SimMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 2)
)
_SimCompliances_ObjectIdentity = ObjectIdentity
simCompliances = _SimCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 2, 1)
)
_SimGroups_ObjectIdentity = ObjectIdentity
simGroups = _SimGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 2, 2)
)

# Managed Objects groups

simIdentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 2, 2, 1)
)
simIdentGroup.setObjects(
      *(("SIM-MIB", "simSofwareVersion"),
        ("SIM-MIB", "simMIBVersion"),
        ("SIM-MIB", "simMIBPrivateVersion"),
        ("SIM-MIB", "simAgentVersion"))
)
if mibBuilder.loadTexts:
    simIdentGroup.setStatus("current")

simEcmgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 2, 2, 2)
)
simEcmgGroup.setObjects(
      *(("SIM-MIB", "simEcmgIndex"),
        ("SIM-MIB", "simEcmgIpAddress"),
        ("SIM-MIB", "simEcmgTcpPort"),
        ("SIM-MIB", "simEcmgSuCasId"),
        ("SIM-MIB", "simEcmgChannels"),
        ("SIM-MIB", "simEcmgCwPrs"),
        ("SIM-MIB", "simEcmgErrs"),
        ("SIM-MIB", "simEcmgTargetCpsig"),
        ("SIM-MIB", "simEcmgCaMib"),
        ("SIM-MIB", "simEcmgChannelId"),
        ("SIM-MIB", "simEcmgCScsIpAddress"),
        ("SIM-MIB", "simEcmgCScsTcpPort"),
        ("SIM-MIB", "simEcmgCStreams"),
        ("SIM-MIB", "simEcmgCCwPrs"),
        ("SIM-MIB", "simEcmgCErrs"),
        ("SIM-MIB", "simEcmgStreamId"),
        ("SIM-MIB", "simEcmgEcmId"),
        ("SIM-MIB", "simEcmgSLastCp"),
        ("SIM-MIB", "simEcmgSCwPrs"),
        ("SIM-MIB", "simEcmgSErrs"))
)
if mibBuilder.loadTexts:
    simEcmgGroup.setStatus("current")

simEmOrPdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 2, 2, 3)
)
simEmOrPdGroup.setObjects(
      *(("SIM-MIB", "simEmOrPdIndex"),
        ("SIM-MIB", "simEmOrPdDataType"),
        ("SIM-MIB", "simEmOrPdClientId"),
        ("SIM-MIB", "simEmOrPdCommCapability"),
        ("SIM-MIB", "simEmOrPdErrs"),
        ("SIM-MIB", "simEmOrPdTargetCpsig"),
        ("SIM-MIB", "simEmOrPdCaMib"),
        ("SIM-MIB", "simEmOrPdLapIndex"),
        ("SIM-MIB", "simEmOrPdLapAdminState"),
        ("SIM-MIB", "simEmOrPdLapCommType"),
        ("SIM-MIB", "simEmOrPdLapMuxIpAddress"),
        ("SIM-MIB", "simEmOrPdLapMuxPort"),
        ("SIM-MIB", "simEmOrPdLapStatus"),
        ("SIM-MIB", "simEmOrPdChannelId"),
        ("SIM-MIB", "simEmOrPdCommType"),
        ("SIM-MIB", "simEmOrPdCIpAddress"),
        ("SIM-MIB", "simEmOrPdCPort"),
        ("SIM-MIB", "simEmOrPdCErrs"),
        ("SIM-MIB", "simEmOrPdDataId"),
        ("SIM-MIB", "simEmOrPdSChannelId"),
        ("SIM-MIB", "simEmOrPdBwidth"),
        ("SIM-MIB", "simEmOrPdStreamId"),
        ("SIM-MIB", "simEmOrPdSErrs"),
        ("SIM-MIB", "simEmOrPdSBytes"))
)
if mibBuilder.loadTexts:
    simEmOrPdGroup.setStatus("current")

simEmOrPdLapGGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 2, 2, 4)
)
simEmOrPdLapGGroup.setObjects(
      *(("SIM-MIB", "simEmOrPdLapGroup"),
        ("SIM-MIB", "simEmOrPdLapGAdminState"),
        ("SIM-MIB", "simEmOrPdLapGStatus"))
)
if mibBuilder.loadTexts:
    simEmOrPdLapGGroup.setStatus("current")

simCpsigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 2, 2, 5)
)
simCpsigGroup.setObjects(
      *(("SIM-MIB", "simCpsigIndex"),
        ("SIM-MIB", "simCpsigSuperCasId"),
        ("SIM-MIB", "simCpsigErrs"),
        ("SIM-MIB", "simCpsigChannels"),
        ("SIM-MIB", "simCpsigCpsigIpAddress"),
        ("SIM-MIB", "simCpsigCpsigPort"),
        ("SIM-MIB", "simCpsigCaMib"),
        ("SIM-MIB", "simCpsigChannelId"),
        ("SIM-MIB", "simCpsigPsigIpAddress"),
        ("SIM-MIB", "simCpsigPsigPort"),
        ("SIM-MIB", "simCpsigCErrs"),
        ("SIM-MIB", "simCpsigCTstrms"),
        ("SIM-MIB", "simCpsigCSstrms"),
        ("SIM-MIB", "simCpsigStreamTStreamId"),
        ("SIM-MIB", "simCpsigStreamNid"),
        ("SIM-MIB", "simCpsigStreamOnid"),
        ("SIM-MIB", "simCpsigStreamMaxCompTime"),
        ("SIM-MIB", "simCpsigStreamTriggerEnable"),
        ("SIM-MIB", "simCpsigStreamLastTrigger"),
        ("SIM-MIB", "simCpsigStreamLastEventId"),
        ("SIM-MIB", "simCpsigStreamLastServiceId"),
        ("SIM-MIB", "simCpsigStreamLastEsId"),
        ("SIM-MIB", "simCpsigStreamLastEcmPid"),
        ("SIM-MIB", "simCpsigStreamErrs"),
        ("SIM-MIB", "simCpsigStreamBytes"))
)
if mibBuilder.loadTexts:
    simCpsigGroup.setStatus("current")

simPsigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 2, 2, 6)
)
simPsigGroup.setObjects(
      *(("SIM-MIB", "simPsigIndex"),
        ("SIM-MIB", "simPsigType"),
        ("SIM-MIB", "simPsigTriggerSupport"),
        ("SIM-MIB", "simPsigNetworkId"),
        ("SIM-MIB", "simPsigONetworkId"),
        ("SIM-MIB", "simPsigTransStreamId"),
        ("SIM-MIB", "simPsigTSServices"),
        ("SIM-MIB", "simPsigConfigAdminState"),
        ("SIM-MIB", "simPsigConfigCustCasId"),
        ("SIM-MIB", "simPsigConfigMaxCompTime"),
        ("SIM-MIB", "simPsigConfigServiceId"),
        ("SIM-MIB", "simPsigConfigTriggerEnable"),
        ("SIM-MIB", "simPsigConfigEntryStatus"),
        ("SIM-MIB", "simPsigConfigCpsigType"),
        ("SIM-MIB", "simPsigConfigCADInsMode"),
        ("SIM-MIB", "simPsigEcmTrNetworkId"),
        ("SIM-MIB", "simPsigEcmTrONetworkId"),
        ("SIM-MIB", "simPsigEcmTrTransStreamId"),
        ("SIM-MIB", "simPsigEcmTrServiceId"),
        ("SIM-MIB", "simPsigEcmTrEsId"),
        ("SIM-MIB", "simPsigEcmTrType"),
        ("SIM-MIB", "simPsigEcmTrSuCasId"),
        ("SIM-MIB", "simPsigEcmTrEcmId"),
        ("SIM-MIB", "simPsigEcmTrEcmPid"),
        ("SIM-MIB", "simPsigEcmTrAccessCriteria"),
        ("SIM-MIB", "simPsigEvntTrNetworkId"),
        ("SIM-MIB", "simPsigEvntTrONetworkId"),
        ("SIM-MIB", "simPsigEvntTrTransStreamId"),
        ("SIM-MIB", "simPsigEvntTrServiceId"),
        ("SIM-MIB", "simPsigEvntTrEventId"),
        ("SIM-MIB", "simPsigEvntTrStartTime"),
        ("SIM-MIB", "simPsigEvntTrDuration"),
        ("SIM-MIB", "simPsigEvntTrPrivateData"),
        ("SIM-MIB", "simPsigFlowTrIndex"),
        ("SIM-MIB", "simPsigFlowTrType"),
        ("SIM-MIB", "simPsigFlowTrSuCasId"),
        ("SIM-MIB", "simPsigFlowTrFlowId"),
        ("SIM-MIB", "simPsigFlowTrFlowPID"),
        ("SIM-MIB", "simPsigDescInsIndex"),
        ("SIM-MIB", "simPsigDescInsAdminState"),
        ("SIM-MIB", "simPsigDescInsTrIndex"),
        ("SIM-MIB", "simPsigDescInsTrType"),
        ("SIM-MIB", "simPsigDescInsLocationId"),
        ("SIM-MIB", "simPsigDescInsNetworkId"),
        ("SIM-MIB", "simPsigDescInsONetworkId"),
        ("SIM-MIB", "simPsigDescInsTransStreamId"),
        ("SIM-MIB", "simPsigDescInsServiceId"),
        ("SIM-MIB", "simPsigDescInsElmStreamId"),
        ("SIM-MIB", "simPsigDescInsBouquetId"),
        ("SIM-MIB", "simPsigDescInsEventId"),
        ("SIM-MIB", "simPsigDescInsNetworkIdOther"),
        ("SIM-MIB", "simPsigDescInsONetworkId2loop"),
        ("SIM-MIB", "simPsigDescInsTransStreamId2OrO"),
        ("SIM-MIB", "simPsigDescInsDelayType"),
        ("SIM-MIB", "simPsigDescInsDelay"),
        ("SIM-MIB", "simPsigDescPrivDataSpfier"),
        ("SIM-MIB", "simPsigDescInsEntryStatus"),
        ("SIM-MIB", "simPsigDescInsDescIndex"),
        ("SIM-MIB", "simPsigDescInsDescAdminState"),
        ("SIM-MIB", "simPsigDescInsDescriptor"),
        ("SIM-MIB", "simPsigDescInsDescriptorStatus"),
        ("SIM-MIB", "simPsigDescInsDescEntryStatus"),
        ("SIM-MIB", "simPsigTblProvIndex"),
        ("SIM-MIB", "simPsigTblProvTableId"),
        ("SIM-MIB", "simPsigTblNetworkId"),
        ("SIM-MIB", "simPsigTblONetworkId"),
        ("SIM-MIB", "simPsigTblTransStreamId"),
        ("SIM-MIB", "simPsigTblServiceId"),
        ("SIM-MIB", "simPsigTblBouquetId"),
        ("SIM-MIB", "simPsigTblEventId"),
        ("SIM-MIB", "simPsigTblNetworkIdOther"),
        ("SIM-MIB", "simPsigTblONetworkId2loop"),
        ("SIM-MIB", "simPsigTblTransStreamId2OrO"),
        ("SIM-MIB", "simPsigTblSegmentNr"),
        ("SIM-MIB", "simPsigTblProvPart"),
        ("SIM-MIB", "simPsigTblProvPartNumber"),
        ("SIM-MIB", "simPsigPIDProvFlowType"),
        ("SIM-MIB", "simPsigPIDProvSuCasId"),
        ("SIM-MIB", "simPsigPIDProvFlowId"),
        ("SIM-MIB", "simPsigPIDProvFlowPID"),
        ("SIM-MIB", "simPsigPdTrNetworkId"),
        ("SIM-MIB", "simPsigPdTrONetworkId"),
        ("SIM-MIB", "simPsigPdTrTransStreamId"),
        ("SIM-MIB", "simPsigPdTrServiceId"),
        ("SIM-MIB", "simPsigPdTrEsId"),
        ("SIM-MIB", "simPsigPdTrType"),
        ("SIM-MIB", "simPsigPdTrSuCasId"),
        ("SIM-MIB", "simPsigPdTrPdId"),
        ("SIM-MIB", "simPsigPdTrPdPid"),
        ("SIM-MIB", "simPsigPdTrPdStreamType"),
        ("SIM-MIB", "simPsigPdTrPrivateData"))
)
if mibBuilder.loadTexts:
    simPsigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

simEcmgCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 2, 1, 1)
)
simEcmgCompliance.setObjects(
      *(("SIM-MIB", "simIdentGroup"),
        ("SIM-MIB", "simEcmgGroup"))
)
if mibBuilder.loadTexts:
    simEcmgCompliance.setStatus(
        "current"
    )

simEmOrPdCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 2, 1, 2)
)
simEmOrPdCompliance.setObjects(
      *(("SIM-MIB", "simIdentGroup"),
        ("SIM-MIB", "simEmOrPdGroup"),
        ("SIM-MIB", "simEmOrPdLapGGroup"))
)
if mibBuilder.loadTexts:
    simEmOrPdCompliance.setStatus(
        "current"
    )

simCpsigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 2, 1, 3)
)
simCpsigCompliance.setObjects(
      *(("SIM-MIB", "simIdentGroup"),
        ("SIM-MIB", "simCpsigGroup"))
)
if mibBuilder.loadTexts:
    simCpsigCompliance.setStatus(
        "current"
    )

simPsigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2696, 1, 1, 2, 1, 4)
)
simPsigCompliance.setObjects(
      *(("SIM-MIB", "simIdentGroup"),
        ("SIM-MIB", "simPsigGroup"))
)
if mibBuilder.loadTexts:
    simPsigCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIM-MIB",
    **{"ECMGCSuCasId": ECMGCSuCasId,
       "Signed16": Signed16,
       "AdministrativeState": AdministrativeState,
       "CaDescInsMode": CaDescInsMode,
       "DelayType": DelayType,
       "DescriptorStatus": DescriptorStatus,
       "ECMGChannelId": ECMGChannelId,
       "ECMGDelayValue": ECMGDelayValue,
       "ECMTriggerType": ECMTriggerType,
       "EMMGChannelId": EMMGChannelId,
       "EMMGCommCapability": EMMGCommCapability,
       "EMMGCommType": EMMGCommType,
       "EMMGDataType": EMMGDataType,
       "FlowId": FlowId,
       "FlowType": FlowType,
       "InsertLocation": InsertLocation,
       "ProvTableId": ProvTableId,
       "PsigType": PsigType,
       "SectionTSPktFlag": SectionTSPktFlag,
       "StreamId": StreamId,
       "SuperCasId": SuperCasId,
       "TriggerType": TriggerType,
       "simMIB": simMIB,
       "simMIBObjects": simMIBObjects,
       "simIdent": simIdent,
       "simSofwareVersion": simSofwareVersion,
       "simMIBVersion": simMIBVersion,
       "simMIBPrivateVersion": simMIBPrivateVersion,
       "simAgentVersion": simAgentVersion,
       "simECMG": simECMG,
       "simEcmgTable": simEcmgTable,
       "simEcmgEntry": simEcmgEntry,
       "simEcmgIndex": simEcmgIndex,
       "simEcmgIpAddress": simEcmgIpAddress,
       "simEcmgTcpPort": simEcmgTcpPort,
       "simEcmgSuCasId": simEcmgSuCasId,
       "simEcmgChannels": simEcmgChannels,
       "simEcmgCwPrs": simEcmgCwPrs,
       "simEcmgErrs": simEcmgErrs,
       "simEcmgTargetCpsig": simEcmgTargetCpsig,
       "simEcmgCaMib": simEcmgCaMib,
       "simEcmgCTable": simEcmgCTable,
       "simEcmgCEntry": simEcmgCEntry,
       "simEcmgChannelId": simEcmgChannelId,
       "simEcmgCScsIpAddress": simEcmgCScsIpAddress,
       "simEcmgCScsTcpPort": simEcmgCScsTcpPort,
       "simEcmgCStreams": simEcmgCStreams,
       "simEcmgCCwPrs": simEcmgCCwPrs,
       "simEcmgCErrs": simEcmgCErrs,
       "simEcmgCSuCasId": simEcmgCSuCasId,
       "simEcmgFormat": simEcmgFormat,
       "simACDelayStart": simACDelayStart,
       "simACDelayStop": simACDelayStop,
       "simDelayStart": simDelayStart,
       "simDelayStop": simDelayStop,
       "simTransitionDelayStart": simTransitionDelayStart,
       "simTransitionDelayStop": simTransitionDelayStop,
       "simECMRepPeriod": simECMRepPeriod,
       "simMaxStreams": simMaxStreams,
       "simMinCPDuration": simMinCPDuration,
       "simLeadCW": simLeadCW,
       "simCWPerMsg": simCWPerMsg,
       "simMaxCompTime": simMaxCompTime,
       "simEcmgSTable": simEcmgSTable,
       "simEcmgSEntry": simEcmgSEntry,
       "simEcmgStreamId": simEcmgStreamId,
       "simEcmgEcmId": simEcmgEcmId,
       "simEcmgSLastCp": simEcmgSLastCp,
       "simEcmgSCwPrs": simEcmgSCwPrs,
       "simEcmgSErrs": simEcmgSErrs,
       "simEMMG": simEMMG,
       "simEmOrPdTable": simEmOrPdTable,
       "simEmOrPdEntry": simEmOrPdEntry,
       "simEmOrPdIndex": simEmOrPdIndex,
       "simEmOrPdDataType": simEmOrPdDataType,
       "simEmOrPdClientId": simEmOrPdClientId,
       "simEmOrPdCommCapability": simEmOrPdCommCapability,
       "simEmOrPdErrs": simEmOrPdErrs,
       "simEmOrPdTargetCpsig": simEmOrPdTargetCpsig,
       "simEmOrPdCaMib": simEmOrPdCaMib,
       "simEmOrPdLapTable": simEmOrPdLapTable,
       "simEmOrPdLapEntry": simEmOrPdLapEntry,
       "simEmOrPdLapIndex": simEmOrPdLapIndex,
       "simEmOrPdLapAdminState": simEmOrPdLapAdminState,
       "simEmOrPdLapCommType": simEmOrPdLapCommType,
       "simEmOrPdLapMuxIpAddress": simEmOrPdLapMuxIpAddress,
       "simEmOrPdLapMuxPort": simEmOrPdLapMuxPort,
       "simEmOrPdLapStatus": simEmOrPdLapStatus,
       "simEmOrPdLapMuxUIpAddress": simEmOrPdLapMuxUIpAddress,
       "simEmOrPdLapMuxUPort": simEmOrPdLapMuxUPort,
       "simEmOrPdLapGTable": simEmOrPdLapGTable,
       "simEmOrPdLapGEntry": simEmOrPdLapGEntry,
       "simEmOrPdLapGroup": simEmOrPdLapGroup,
       "simEmOrPdLapGAdminState": simEmOrPdLapGAdminState,
       "simEmOrPdLapGStatus": simEmOrPdLapGStatus,
       "simEmOrPdCTable": simEmOrPdCTable,
       "simEmOrPdCEntry": simEmOrPdCEntry,
       "simEmOrPdChannelId": simEmOrPdChannelId,
       "simEmOrPdCommType": simEmOrPdCommType,
       "simEmOrPdCIpAddress": simEmOrPdCIpAddress,
       "simEmOrPdCPort": simEmOrPdCPort,
       "simEmOrPdCErrs": simEmOrPdCErrs,
       "simEmOrPdCFormat": simEmOrPdCFormat,
       "simEmOrPdCUIpAddress": simEmOrPdCUIpAddress,
       "simEmOrPdCUPort": simEmOrPdCUPort,
       "simEmOrPdSTable": simEmOrPdSTable,
       "simEmOrPdSEntry": simEmOrPdSEntry,
       "simEmOrPdDataId": simEmOrPdDataId,
       "simEmOrPdSChannelId": simEmOrPdSChannelId,
       "simEmOrPdBwidth": simEmOrPdBwidth,
       "simEmOrPdStreamId": simEmOrPdStreamId,
       "simEmOrPdSErrs": simEmOrPdSErrs,
       "simEmOrPdSBytes": simEmOrPdSBytes,
       "simEmOrPdSReqBwidth": simEmOrPdSReqBwidth,
       "simCPSI": simCPSI,
       "simCpsigTable": simCpsigTable,
       "simCpsigEntry": simCpsigEntry,
       "simCpsigIndex": simCpsigIndex,
       "simCpsigSuperCasId": simCpsigSuperCasId,
       "simCpsigErrs": simCpsigErrs,
       "simCpsigChannels": simCpsigChannels,
       "simCpsigCpsigIpAddress": simCpsigCpsigIpAddress,
       "simCpsigCpsigPort": simCpsigCpsigPort,
       "simCpsigCaMib": simCpsigCaMib,
       "simCpsigCTable": simCpsigCTable,
       "simCpsigCEntry": simCpsigCEntry,
       "simCpsigChannelId": simCpsigChannelId,
       "simCpsigPsigIpAddress": simCpsigPsigIpAddress,
       "simCpsigPsigPort": simCpsigPsigPort,
       "simCpsigCErrs": simCpsigCErrs,
       "simCpsigCTstrms": simCpsigCTstrms,
       "simCpsigCSstrms": simCpsigCSstrms,
       "simCpsigStreamTable": simCpsigStreamTable,
       "simCpsigStreamEntry": simCpsigStreamEntry,
       "simCpsigStreamId": simCpsigStreamId,
       "simCpsigStreamTStreamId": simCpsigStreamTStreamId,
       "simCpsigStreamNid": simCpsigStreamNid,
       "simCpsigStreamOnid": simCpsigStreamOnid,
       "simCpsigStreamMaxCompTime": simCpsigStreamMaxCompTime,
       "simCpsigStreamTriggerEnable": simCpsigStreamTriggerEnable,
       "simCpsigStreamLastTrigger": simCpsigStreamLastTrigger,
       "simCpsigStreamLastEventId": simCpsigStreamLastEventId,
       "simCpsigStreamLastServiceId": simCpsigStreamLastServiceId,
       "simCpsigStreamLastEsId": simCpsigStreamLastEsId,
       "simCpsigStreamLastEcmPid": simCpsigStreamLastEcmPid,
       "simCpsigStreamErrs": simCpsigStreamErrs,
       "simCpsigStreamBytes": simCpsigStreamBytes,
       "simPSI": simPSI,
       "simPsigTable": simPsigTable,
       "simPsigEntry": simPsigEntry,
       "simPsigIndex": simPsigIndex,
       "simPsigType": simPsigType,
       "simPsigTriggerSupport": simPsigTriggerSupport,
       "simPsigNetworkId": simPsigNetworkId,
       "simPsigONetworkId": simPsigONetworkId,
       "simPsigTransStreamId": simPsigTransStreamId,
       "simPsigTSServices": simPsigTSServices,
       "simPsigConfigTable": simPsigConfigTable,
       "simPsigConfigEntry": simPsigConfigEntry,
       "simPsigConfigIndex": simPsigConfigIndex,
       "simPsigConfigAdminState": simPsigConfigAdminState,
       "simPsigConfigCpsigType": simPsigConfigCpsigType,
       "simPsigConfigCustCasId": simPsigConfigCustCasId,
       "simPsigConfigMaxCompTime": simPsigConfigMaxCompTime,
       "simPsigConfigServiceId": simPsigConfigServiceId,
       "simPsigConfigTriggerEnable": simPsigConfigTriggerEnable,
       "simPsigConfigCADInsMode": simPsigConfigCADInsMode,
       "simPsigConfigEntryStatus": simPsigConfigEntryStatus,
       "simPsigEcmTrTable": simPsigEcmTrTable,
       "simPsigEcmTrEntry": simPsigEcmTrEntry,
       "simPsigEcmTrIndex": simPsigEcmTrIndex,
       "simPsigEcmTrNetworkId": simPsigEcmTrNetworkId,
       "simPsigEcmTrONetworkId": simPsigEcmTrONetworkId,
       "simPsigEcmTrTransStreamId": simPsigEcmTrTransStreamId,
       "simPsigEcmTrServiceId": simPsigEcmTrServiceId,
       "simPsigEcmTrEsId": simPsigEcmTrEsId,
       "simPsigEcmTrType": simPsigEcmTrType,
       "simPsigEcmTrSuCasId": simPsigEcmTrSuCasId,
       "simPsigEcmTrEcmId": simPsigEcmTrEcmId,
       "simPsigEcmTrEcmPid": simPsigEcmTrEcmPid,
       "simPsigEcmTrAccessCriteria": simPsigEcmTrAccessCriteria,
       "simPsigFlowTrTable": simPsigFlowTrTable,
       "simPsigFlowTrEntry": simPsigFlowTrEntry,
       "simPsigFlowTrIndex": simPsigFlowTrIndex,
       "simPsigFlowTrType": simPsigFlowTrType,
       "simPsigFlowTrSuCasId": simPsigFlowTrSuCasId,
       "simPsigFlowTrFlowId": simPsigFlowTrFlowId,
       "simPsigFlowTrFlowPID": simPsigFlowTrFlowPID,
       "simPsigEvntTrTable": simPsigEvntTrTable,
       "simPsigEvntTrEntry": simPsigEvntTrEntry,
       "simPsigEvntTrIndex": simPsigEvntTrIndex,
       "simPsigEvntTrNetworkId": simPsigEvntTrNetworkId,
       "simPsigEvntTrONetworkId": simPsigEvntTrONetworkId,
       "simPsigEvntTrTransStreamId": simPsigEvntTrTransStreamId,
       "simPsigEvntTrServiceId": simPsigEvntTrServiceId,
       "simPsigEvntTrEventId": simPsigEvntTrEventId,
       "simPsigEvntTrStartTime": simPsigEvntTrStartTime,
       "simPsigEvntTrDuration": simPsigEvntTrDuration,
       "simPsigEvntTrPrivateData": simPsigEvntTrPrivateData,
       "simPsigDescInsTable": simPsigDescInsTable,
       "simPsigDescInsEntry": simPsigDescInsEntry,
       "simPsigDescInsIndex": simPsigDescInsIndex,
       "simPsigDescInsAdminState": simPsigDescInsAdminState,
       "simPsigDescInsTrIndex": simPsigDescInsTrIndex,
       "simPsigDescInsTrType": simPsigDescInsTrType,
       "simPsigDescInsLocationId": simPsigDescInsLocationId,
       "simPsigDescInsNetworkId": simPsigDescInsNetworkId,
       "simPsigDescInsONetworkId": simPsigDescInsONetworkId,
       "simPsigDescInsTransStreamId": simPsigDescInsTransStreamId,
       "simPsigDescInsServiceId": simPsigDescInsServiceId,
       "simPsigDescInsElmStreamId": simPsigDescInsElmStreamId,
       "simPsigDescInsBouquetId": simPsigDescInsBouquetId,
       "simPsigDescInsEventId": simPsigDescInsEventId,
       "simPsigDescInsONetworkId2loop": simPsigDescInsONetworkId2loop,
       "simPsigDescInsNetworkIdOther": simPsigDescInsNetworkIdOther,
       "simPsigDescInsTransStreamId2OrO": simPsigDescInsTransStreamId2OrO,
       "simPsigDescInsDelayType": simPsigDescInsDelayType,
       "simPsigDescInsDelay": simPsigDescInsDelay,
       "simPsigDescPrivDataSpfier": simPsigDescPrivDataSpfier,
       "simPsigDescInsEntryStatus": simPsigDescInsEntryStatus,
       "simPsigDescInsDescTable": simPsigDescInsDescTable,
       "simPsigDescInsDescEntry": simPsigDescInsDescEntry,
       "simPsigDescInsDescIndex": simPsigDescInsDescIndex,
       "simPsigDescInsDescAdminState": simPsigDescInsDescAdminState,
       "simPsigDescInsDescriptor": simPsigDescInsDescriptor,
       "simPsigDescInsDescriptorStatus": simPsigDescInsDescriptorStatus,
       "simPsigDescInsDescEntryStatus": simPsigDescInsDescEntryStatus,
       "simPsigTblProvTable": simPsigTblProvTable,
       "simPsigTblProvEntry": simPsigTblProvEntry,
       "simPsigTblProvIndex": simPsigTblProvIndex,
       "simPsigTblProvTableId": simPsigTblProvTableId,
       "simPsigTblNetworkId": simPsigTblNetworkId,
       "simPsigTblONetworkId": simPsigTblONetworkId,
       "simPsigTblTransStreamId": simPsigTblTransStreamId,
       "simPsigTblServiceId": simPsigTblServiceId,
       "simPsigTblBouquetId": simPsigTblBouquetId,
       "simPsigTblEventId": simPsigTblEventId,
       "simPsigTblONetworkId2loop": simPsigTblONetworkId2loop,
       "simPsigTblNetworkIdOther": simPsigTblNetworkIdOther,
       "simPsigTblTransStreamId2OrO": simPsigTblTransStreamId2OrO,
       "simPsigTblSegmentNr": simPsigTblSegmentNr,
       "simPsigTblProvPart": simPsigTblProvPart,
       "simPsigTblProvPartNumber": simPsigTblProvPartNumber,
       "simPsigPIDProvTable": simPsigPIDProvTable,
       "simPsigPIDProvEntry": simPsigPIDProvEntry,
       "simPsigPIDProvFlowType": simPsigPIDProvFlowType,
       "simPsigPIDProvSuCasId": simPsigPIDProvSuCasId,
       "simPsigPIDProvFlowId": simPsigPIDProvFlowId,
       "simPsigPIDProvFlowPID": simPsigPIDProvFlowPID,
       "simPsigPdTrTable": simPsigPdTrTable,
       "simPsigPdTrEntry": simPsigPdTrEntry,
       "simPsigPdTrIndex": simPsigPdTrIndex,
       "simPsigPdTrNetworkId": simPsigPdTrNetworkId,
       "simPsigPdTrONetworkId": simPsigPdTrONetworkId,
       "simPsigPdTrTransStreamId": simPsigPdTrTransStreamId,
       "simPsigPdTrServiceId": simPsigPdTrServiceId,
       "simPsigPdTrEsId": simPsigPdTrEsId,
       "simPsigPdTrType": simPsigPdTrType,
       "simPsigPdTrSuCasId": simPsigPdTrSuCasId,
       "simPsigPdTrPdId": simPsigPdTrPdId,
       "simPsigPdTrPdPid": simPsigPdTrPdPid,
       "simPsigPdTrPdStreamType": simPsigPdTrPdStreamType,
       "simPsigPdTrPrivateData": simPsigPdTrPrivateData,
       "simMIBConformance": simMIBConformance,
       "simCompliances": simCompliances,
       "simEcmgCompliance": simEcmgCompliance,
       "simEmOrPdCompliance": simEmOrPdCompliance,
       "simCpsigCompliance": simCpsigCompliance,
       "simPsigCompliance": simPsigCompliance,
       "simGroups": simGroups,
       "simIdentGroup": simIdentGroup,
       "simEcmgGroup": simEcmgGroup,
       "simEmOrPdGroup": simEmOrPdGroup,
       "simEmOrPdLapGGroup": simEmOrPdLapGGroup,
       "simCpsigGroup": simCpsigGroup,
       "simPsigGroup": simPsigGroup}
)
