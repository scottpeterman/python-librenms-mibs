# SNMP MIB module (SLE-MLSQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-MLSQOS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:35 2025
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

(sleMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleMgmt")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleMlsQos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28)
)
if mibBuilder.loadTexts:
    sleMlsQos.setRevisions(
        ("2013-08-04 09:03",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MlsQosStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )



class MlsQosMappingType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("cosToCos", 1),
          ("cosToQueue", 2),
          ("dscpToDscp", 3),
          ("dscpToQueue", 4),
          ("expToExp", 5),
          ("expToQueue", 6),
          ("expToClass", 7))
    )



class ACLMatchType(TextualConvention, Integer32):
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
        *(("mac", 1),
          ("ethType", 2),
          ("l3Proto", 3))
    )



class ACLMatchActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1),
          ("remark", 2))
    )



class ACLEtherType(TextualConvention, OctetString):
    status = "current"


class AclTcpUdpPortActionType(TextualConvention, Integer32):
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
        *(("eq", 1),
          ("neq", 2),
          ("lt", 3),
          ("gt", 4))
    )



class ClassMapMatchType(TextualConvention, Integer32):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("cos", 1),
          ("innerCos", 2),
          ("ipDscp", 3),
          ("ipPrecedence", 4),
          ("ip6Dscp", 5),
          ("ip6Precedence", 6),
          ("tcpSrcPort", 7),
          ("tcpDstPort", 8),
          ("udpSrcPort", 9),
          ("udpDstPort", 10),
          ("vlanId", 11),
          ("innerVlanId", 12),
          ("layer4SrcPort", 13),
          ("layer4DstPort", 14))
    )



class ClassMapMatchRangeType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("tcpSrcPort", 1),
          ("tcpDstPort", 2),
          ("udpSrcPort", 3),
          ("udpDstPort", 4),
          ("vlanId", 5),
          ("layer4SrcPort", 6),
          ("layer4DstPort", 7))
    )



class PmapPriorityType(TextualConvention, Integer32):
    status = "current"
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
        *(("low", 0),
          ("medium", 1),
          ("high", 2),
          ("highest", 3))
    )



class PmapPoliceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("srtcm", 1),
          ("trtcm", 2))
    )



class PmapExceedActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("drop", 1),
          ("setDscpTransmit", 2),
          ("setTosTransmit", 3),
          ("setCosTransmit", 4),
          ("transmit", 7))
    )



class PmapViolateActionType(TextualConvention, Integer32):
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
        *(("none", 0),
          ("drop", 1),
          ("dscpTx", 2),
          ("cosTx", 3),
          ("tosTx", 4),
          ("transmit", 5))
    )



class PmapSetActionType(TextualConvention, Integer32):
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("cos", 1),
          ("cpuCos", 2),
          ("ipDscp", 3),
          ("ipPrecedence", 4),
          ("redirectToPort", 5),
          ("mirrorToPort", 6),
          ("vlan", 7),
          ("ip6Dscp", 8),
          ("ip6Precedence", 9),
          ("cpuCopy", 10),
          ("deny", 11),
          ("qosGroup", 12),
          ("none", 13),
          ("queue", 14),
          ("vlanCos", 15))
    )



class MlsQosIntfTrustState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cos", 1),
          ("dscp", 2))
    )



class MlsQosInterfaceMapingType(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("cos", 1),
          ("cosToCos", 2),
          ("cosToQueue", 3),
          ("dscp", 4),
          ("dscpToDscp", 5),
          ("dscpToQueue", 6),
          ("expToExp", 7),
          ("trust", 8),
          ("trustPassThrough", 9),
          ("cosToClass", 10),
          ("dscpToClass", 11))
    )



class MlsQosIntfQueProfilingType(TextualConvention, Integer32):
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
        *(("shaping", 1),
          ("wrrQWt", 2),
          ("wrrRandomDetect", 3),
          ("tailDrop", 4),
          ("strictQ", 5),
          ("reservedBandwidth", 6))
    )



class ACLMacType(TextualConvention, Integer32):
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
        *(("src", 1),
          ("dst", 2),
          ("srcWildcard", 3),
          ("dstWildcard", 4))
    )



class ACLIpType(TextualConvention, Integer32):
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
        *(("src", 1),
          ("dst", 2),
          ("srcWildcard", 3),
          ("dstWildcard", 4))
    )



class PolMapClassMatchPrioType(TextualConvention, Integer32):
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
        *(("high", 1),
          ("highest", 2),
          ("low", 3),
          ("medium", 4))
    )



class PoliceExceedActionType(TextualConvention, Integer32):
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
        *(("drop", 1),
          ("setCosTransmit", 2),
          ("setDscpTransmit", 3),
          ("setTosTransmit", 4),
          ("transmit", 5))
    )



# MIB Managed Objects in the order of their OIDs

_SleMlsQosGlobal_ObjectIdentity = ObjectIdentity
sleMlsQosGlobal = _SleMlsQosGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1)
)
_SleMlsQosGlobalInfo_ObjectIdentity = ObjectIdentity
sleMlsQosGlobalInfo = _SleMlsQosGlobalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1)
)
_SleMlsQosStatus_Type = MlsQosStatusType
_SleMlsQosStatus_Object = MibScalar
sleMlsQosStatus = _SleMlsQosStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 1),
    _SleMlsQosStatus_Type()
)
sleMlsQosStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosStatus.setStatus("current")
_SleMlsQosMapCosToCos_Type = OctetString
_SleMlsQosMapCosToCos_Object = MibScalar
sleMlsQosMapCosToCos = _SleMlsQosMapCosToCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 2),
    _SleMlsQosMapCosToCos_Type()
)
sleMlsQosMapCosToCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosMapCosToCos.setStatus("current")
_SleMlsQosMapCosToQueue_Type = OctetString
_SleMlsQosMapCosToQueue_Object = MibScalar
sleMlsQosMapCosToQueue = _SleMlsQosMapCosToQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 3),
    _SleMlsQosMapCosToQueue_Type()
)
sleMlsQosMapCosToQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosMapCosToQueue.setStatus("current")
_SleMlsQosMapDscpToDscp_Type = OctetString
_SleMlsQosMapDscpToDscp_Object = MibScalar
sleMlsQosMapDscpToDscp = _SleMlsQosMapDscpToDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 4),
    _SleMlsQosMapDscpToDscp_Type()
)
sleMlsQosMapDscpToDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosMapDscpToDscp.setStatus("current")
_SleMlsQosMapDscpToQueue_Type = OctetString
_SleMlsQosMapDscpToQueue_Object = MibScalar
sleMlsQosMapDscpToQueue = _SleMlsQosMapDscpToQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 5),
    _SleMlsQosMapDscpToQueue_Type()
)
sleMlsQosMapDscpToQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosMapDscpToQueue.setStatus("current")
_SleMlsQosMapExpToExp_Type = OctetString
_SleMlsQosMapExpToExp_Object = MibScalar
sleMlsQosMapExpToExp = _SleMlsQosMapExpToExp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 6),
    _SleMlsQosMapExpToExp_Type()
)
sleMlsQosMapExpToExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosMapExpToExp.setStatus("current")
_SleMlsQosMapExpToQueue_Type = OctetString
_SleMlsQosMapExpToQueue_Object = MibScalar
sleMlsQosMapExpToQueue = _SleMlsQosMapExpToQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 7),
    _SleMlsQosMapExpToQueue_Type()
)
sleMlsQosMapExpToQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosMapExpToQueue.setStatus("current")
_SleMlsQosMapStrictQueueId_Type = OctetString
_SleMlsQosMapStrictQueueId_Object = MibScalar
sleMlsQosMapStrictQueueId = _SleMlsQosMapStrictQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 8),
    _SleMlsQosMapStrictQueueId_Type()
)
sleMlsQosMapStrictQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosMapStrictQueueId.setStatus("current")
_SleMlsQosMapWrrQueueWeight_Type = OctetString
_SleMlsQosMapWrrQueueWeight_Object = MibScalar
sleMlsQosMapWrrQueueWeight = _SleMlsQosMapWrrQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 9),
    _SleMlsQosMapWrrQueueWeight_Type()
)
sleMlsQosMapWrrQueueWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosMapWrrQueueWeight.setStatus("current")
_SleMlsQosMapCpuMaxPpsRate_Type = OctetString
_SleMlsQosMapCpuMaxPpsRate_Object = MibScalar
sleMlsQosMapCpuMaxPpsRate = _SleMlsQosMapCpuMaxPpsRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 10),
    _SleMlsQosMapCpuMaxPpsRate_Type()
)
sleMlsQosMapCpuMaxPpsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosMapCpuMaxPpsRate.setStatus("current")
_SleMlsQosMapCpuQueueWeight_Type = OctetString
_SleMlsQosMapCpuQueueWeight_Object = MibScalar
sleMlsQosMapCpuQueueWeight = _SleMlsQosMapCpuQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 11),
    _SleMlsQosMapCpuQueueWeight_Type()
)
sleMlsQosMapCpuQueueWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosMapCpuQueueWeight.setStatus("current")
_SleMlsQosMapNodeCpuMaxPpsRate_Type = OctetString
_SleMlsQosMapNodeCpuMaxPpsRate_Object = MibScalar
sleMlsQosMapNodeCpuMaxPpsRate = _SleMlsQosMapNodeCpuMaxPpsRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 12),
    _SleMlsQosMapNodeCpuMaxPpsRate_Type()
)
sleMlsQosMapNodeCpuMaxPpsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosMapNodeCpuMaxPpsRate.setStatus("current")
_SleMlsQosMapNodeCpuQueueWeight_Type = OctetString
_SleMlsQosMapNodeCpuQueueWeight_Object = MibScalar
sleMlsQosMapNodeCpuQueueWeight = _SleMlsQosMapNodeCpuQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 13),
    _SleMlsQosMapNodeCpuQueueWeight_Type()
)
sleMlsQosMapNodeCpuQueueWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosMapNodeCpuQueueWeight.setStatus("current")
_SleMlsQosMapExpToClass_Type = OctetString
_SleMlsQosMapExpToClass_Object = MibScalar
sleMlsQosMapExpToClass = _SleMlsQosMapExpToClass_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 14),
    _SleMlsQosMapExpToClass_Type()
)
sleMlsQosMapExpToClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosMapExpToClass.setStatus("current")
_SleHQosStatistics_Type = MlsQosStatusType
_SleHQosStatistics_Object = MibScalar
sleHQosStatistics = _SleHQosStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 15),
    _SleHQosStatistics_Type()
)
sleHQosStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHQosStatistics.setStatus("current")
_SleQosPhbPriorityColor_Type = OctetString
_SleQosPhbPriorityColor_Object = MibScalar
sleQosPhbPriorityColor = _SleQosPhbPriorityColor_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 16),
    _SleQosPhbPriorityColor_Type()
)
sleQosPhbPriorityColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQosPhbPriorityColor.setStatus("current")
_SleHQosDefaultClassToDscp_Type = OctetString
_SleHQosDefaultClassToDscp_Object = MibScalar
sleHQosDefaultClassToDscp = _SleHQosDefaultClassToDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 17),
    _SleHQosDefaultClassToDscp_Type()
)
sleHQosDefaultClassToDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHQosDefaultClassToDscp.setStatus("current")
_SleQosDefaultCosToClassTrust_Type = OctetString
_SleQosDefaultCosToClassTrust_Object = MibScalar
sleQosDefaultCosToClassTrust = _SleQosDefaultCosToClassTrust_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 18),
    _SleQosDefaultCosToClassTrust_Type()
)
sleQosDefaultCosToClassTrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQosDefaultCosToClassTrust.setStatus("current")
_SleQosDefaultCosToClassNoTrust_Type = OctetString
_SleQosDefaultCosToClassNoTrust_Object = MibScalar
sleQosDefaultCosToClassNoTrust = _SleQosDefaultCosToClassNoTrust_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 19),
    _SleQosDefaultCosToClassNoTrust_Type()
)
sleQosDefaultCosToClassNoTrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQosDefaultCosToClassNoTrust.setStatus("current")
_SleQosDefaultDscpToClassTrust_Type = OctetString
_SleQosDefaultDscpToClassTrust_Object = MibScalar
sleQosDefaultDscpToClassTrust = _SleQosDefaultDscpToClassTrust_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 20),
    _SleQosDefaultDscpToClassTrust_Type()
)
sleQosDefaultDscpToClassTrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQosDefaultDscpToClassTrust.setStatus("current")
_SleQosDefaultDscpToClassNoTrust_Type = OctetString
_SleQosDefaultDscpToClassNoTrust_Object = MibScalar
sleQosDefaultDscpToClassNoTrust = _SleQosDefaultDscpToClassNoTrust_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 1, 21),
    _SleQosDefaultDscpToClassNoTrust_Type()
)
sleQosDefaultDscpToClassNoTrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQosDefaultDscpToClassNoTrust.setStatus("current")
_SleMlsQosGlobalControl_ObjectIdentity = ObjectIdentity
sleMlsQosGlobalControl = _SleMlsQosGlobalControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 2)
)


class _SleMlsQosGlobalControlRequest_Type(Integer32):
    """Custom type sleMlsQosGlobalControlRequest based on Integer32"""
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
        *(("setMlQosStatus", 1),
          ("setMlsQosMapping", 2),
          ("unSetMlsQosMapping", 3),
          ("setMlsQosStrictQueue", 4),
          ("unSetMlsQosStrictQueue", 5),
          ("setMlsQosWrr", 6),
          ("unSetMlsQosWrr", 7),
          ("setMlsQosCpuRate", 8),
          ("setMlsQosCpuQueueWt", 9),
          ("setMlsQosNodeCpuRate", 10),
          ("setMlsQosNodeCpuQueueWt", 11),
          ("setHQosStatistics", 12),
          ("unsetHQosStatistics", 13))
    )


_SleMlsQosGlobalControlRequest_Type.__name__ = "Integer32"
_SleMlsQosGlobalControlRequest_Object = MibScalar
sleMlsQosGlobalControlRequest = _SleMlsQosGlobalControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 2, 1),
    _SleMlsQosGlobalControlRequest_Type()
)
sleMlsQosGlobalControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosGlobalControlRequest.setStatus("current")
_SleMlsQosGlobalControlStatus_Type = SleControlStatusType
_SleMlsQosGlobalControlStatus_Object = MibScalar
sleMlsQosGlobalControlStatus = _SleMlsQosGlobalControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 2, 2),
    _SleMlsQosGlobalControlStatus_Type()
)
sleMlsQosGlobalControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosGlobalControlStatus.setStatus("current")
_SleMlsQosGlobalCtrlTimer_Type = Gauge32
_SleMlsQosGlobalCtrlTimer_Object = MibScalar
sleMlsQosGlobalCtrlTimer = _SleMlsQosGlobalCtrlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 2, 3),
    _SleMlsQosGlobalCtrlTimer_Type()
)
sleMlsQosGlobalCtrlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosGlobalCtrlTimer.setStatus("current")
_SleMlsQosGlobalControlTimeStamp_Type = TimeTicks
_SleMlsQosGlobalControlTimeStamp_Object = MibScalar
sleMlsQosGlobalControlTimeStamp = _SleMlsQosGlobalControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 2, 4),
    _SleMlsQosGlobalControlTimeStamp_Type()
)
sleMlsQosGlobalControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosGlobalControlTimeStamp.setStatus("current")
_SleMlsQosGlobalControlReqResult_Type = SleControlRequestResultType
_SleMlsQosGlobalControlReqResult_Object = MibScalar
sleMlsQosGlobalControlReqResult = _SleMlsQosGlobalControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 2, 5),
    _SleMlsQosGlobalControlReqResult_Type()
)
sleMlsQosGlobalControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosGlobalControlReqResult.setStatus("current")
_SleMlsQosCtrlGlobalStatus_Type = MlsQosStatusType
_SleMlsQosCtrlGlobalStatus_Object = MibScalar
sleMlsQosCtrlGlobalStatus = _SleMlsQosCtrlGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 2, 6),
    _SleMlsQosCtrlGlobalStatus_Type()
)
sleMlsQosCtrlGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosCtrlGlobalStatus.setStatus("current")
_SleMlsQosGlobalControlMappingType_Type = MlsQosMappingType
_SleMlsQosGlobalControlMappingType_Object = MibScalar
sleMlsQosGlobalControlMappingType = _SleMlsQosGlobalControlMappingType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 2, 7),
    _SleMlsQosGlobalControlMappingType_Type()
)
sleMlsQosGlobalControlMappingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosGlobalControlMappingType.setStatus("current")
_SleMlsQosGlobalControlMappingIngValue_Type = Integer32
_SleMlsQosGlobalControlMappingIngValue_Object = MibScalar
sleMlsQosGlobalControlMappingIngValue = _SleMlsQosGlobalControlMappingIngValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 2, 8),
    _SleMlsQosGlobalControlMappingIngValue_Type()
)
sleMlsQosGlobalControlMappingIngValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosGlobalControlMappingIngValue.setStatus("current")
_SleMlsQosGlobalControlMappingEgrValue_Type = Integer32
_SleMlsQosGlobalControlMappingEgrValue_Object = MibScalar
sleMlsQosGlobalControlMappingEgrValue = _SleMlsQosGlobalControlMappingEgrValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 2, 9),
    _SleMlsQosGlobalControlMappingEgrValue_Type()
)
sleMlsQosGlobalControlMappingEgrValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosGlobalControlMappingEgrValue.setStatus("current")
_SleMlsQosGlobalControlQueueId_Type = Integer32
_SleMlsQosGlobalControlQueueId_Object = MibScalar
sleMlsQosGlobalControlQueueId = _SleMlsQosGlobalControlQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 2, 10),
    _SleMlsQosGlobalControlQueueId_Type()
)
sleMlsQosGlobalControlQueueId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosGlobalControlQueueId.setStatus("current")
_SleMlsQosGlobalControlWrrQueueWeight_Type = Integer32
_SleMlsQosGlobalControlWrrQueueWeight_Object = MibScalar
sleMlsQosGlobalControlWrrQueueWeight = _SleMlsQosGlobalControlWrrQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 2, 11),
    _SleMlsQosGlobalControlWrrQueueWeight_Type()
)
sleMlsQosGlobalControlWrrQueueWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosGlobalControlWrrQueueWeight.setStatus("current")
_SleMlsQosGlobalControlCpuMaxPpsRate_Type = Integer32
_SleMlsQosGlobalControlCpuMaxPpsRate_Object = MibScalar
sleMlsQosGlobalControlCpuMaxPpsRate = _SleMlsQosGlobalControlCpuMaxPpsRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 2, 12),
    _SleMlsQosGlobalControlCpuMaxPpsRate_Type()
)
sleMlsQosGlobalControlCpuMaxPpsRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosGlobalControlCpuMaxPpsRate.setStatus("current")
_SleMlsQosGlobalControlCpuQueueWt_Type = Integer32
_SleMlsQosGlobalControlCpuQueueWt_Object = MibScalar
sleMlsQosGlobalControlCpuQueueWt = _SleMlsQosGlobalControlCpuQueueWt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 2, 13),
    _SleMlsQosGlobalControlCpuQueueWt_Type()
)
sleMlsQosGlobalControlCpuQueueWt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosGlobalControlCpuQueueWt.setStatus("current")


class _SleMlsQosGlobalControlNodeId_Type(Integer32):
    """Custom type sleMlsQosGlobalControlNodeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SleMlsQosGlobalControlNodeId_Type.__name__ = "Integer32"
_SleMlsQosGlobalControlNodeId_Object = MibScalar
sleMlsQosGlobalControlNodeId = _SleMlsQosGlobalControlNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 2, 14),
    _SleMlsQosGlobalControlNodeId_Type()
)
sleMlsQosGlobalControlNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosGlobalControlNodeId.setStatus("current")
_SleMlsQosGlobalControlMappingEgrClassValue_Type = OctetString
_SleMlsQosGlobalControlMappingEgrClassValue_Object = MibScalar
sleMlsQosGlobalControlMappingEgrClassValue = _SleMlsQosGlobalControlMappingEgrClassValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 1, 2, 15),
    _SleMlsQosGlobalControlMappingEgrClassValue_Type()
)
sleMlsQosGlobalControlMappingEgrClassValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosGlobalControlMappingEgrClassValue.setStatus("current")
_SleMlsQosAggPolice_ObjectIdentity = ObjectIdentity
sleMlsQosAggPolice = _SleMlsQosAggPolice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 2)
)
_SleMlsQosAggPoliceTable_Object = MibTable
sleMlsQosAggPoliceTable = _SleMlsQosAggPoliceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 2, 1)
)
if mibBuilder.loadTexts:
    sleMlsQosAggPoliceTable.setStatus("current")
_SleMlsQosAggPoliceEntry_Object = MibTableRow
sleMlsQosAggPoliceEntry = _SleMlsQosAggPoliceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 2, 1, 1)
)
sleMlsQosAggPoliceEntry.setIndexNames(
    (0, "SLE-MLSQOS-MIB", "sleMlsQosAggPoliceIndex"),
)
if mibBuilder.loadTexts:
    sleMlsQosAggPoliceEntry.setStatus("current")


class _SleMlsQosAggPoliceIndex_Type(Integer32):
    """Custom type sleMlsQosAggPoliceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleMlsQosAggPoliceIndex_Type.__name__ = "Integer32"
_SleMlsQosAggPoliceIndex_Object = MibTableColumn
sleMlsQosAggPoliceIndex = _SleMlsQosAggPoliceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 2, 1, 1, 1),
    _SleMlsQosAggPoliceIndex_Type()
)
sleMlsQosAggPoliceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMlsQosAggPoliceIndex.setStatus("current")
_SleMlsQosAggPoliceName_Type = OctetString
_SleMlsQosAggPoliceName_Object = MibTableColumn
sleMlsQosAggPoliceName = _SleMlsQosAggPoliceName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 2, 1, 1, 2),
    _SleMlsQosAggPoliceName_Type()
)
sleMlsQosAggPoliceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosAggPoliceName.setStatus("current")
_SleMlsQosAggPoliceTrafficRate_Type = Integer32
_SleMlsQosAggPoliceTrafficRate_Object = MibTableColumn
sleMlsQosAggPoliceTrafficRate = _SleMlsQosAggPoliceTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 2, 1, 1, 3),
    _SleMlsQosAggPoliceTrafficRate_Type()
)
sleMlsQosAggPoliceTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosAggPoliceTrafficRate.setStatus("current")
_SleMlsQosAggPoliceBurstSize_Type = Integer32
_SleMlsQosAggPoliceBurstSize_Object = MibTableColumn
sleMlsQosAggPoliceBurstSize = _SleMlsQosAggPoliceBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 2, 1, 1, 4),
    _SleMlsQosAggPoliceBurstSize_Type()
)
sleMlsQosAggPoliceBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosAggPoliceBurstSize.setStatus("current")
_SleMlsQosAggPoliceControl_ObjectIdentity = ObjectIdentity
sleMlsQosAggPoliceControl = _SleMlsQosAggPoliceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 2, 2)
)


class _SleMlsQosAggPoliceCtrlRequest_Type(Integer32):
    """Custom type sleMlsQosAggPoliceCtrlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createAggrPolice", 1),
          ("deleteAggrPolice", 2))
    )


_SleMlsQosAggPoliceCtrlRequest_Type.__name__ = "Integer32"
_SleMlsQosAggPoliceCtrlRequest_Object = MibScalar
sleMlsQosAggPoliceCtrlRequest = _SleMlsQosAggPoliceCtrlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 2, 2, 1),
    _SleMlsQosAggPoliceCtrlRequest_Type()
)
sleMlsQosAggPoliceCtrlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosAggPoliceCtrlRequest.setStatus("current")
_SleMlsQosAggPoliceCtrlStatus_Type = SleControlStatusType
_SleMlsQosAggPoliceCtrlStatus_Object = MibScalar
sleMlsQosAggPoliceCtrlStatus = _SleMlsQosAggPoliceCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 2, 2, 2),
    _SleMlsQosAggPoliceCtrlStatus_Type()
)
sleMlsQosAggPoliceCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosAggPoliceCtrlStatus.setStatus("current")
_SleMlsQosAggPoliceConfigCtrlTimer_Type = Gauge32
_SleMlsQosAggPoliceConfigCtrlTimer_Object = MibScalar
sleMlsQosAggPoliceConfigCtrlTimer = _SleMlsQosAggPoliceConfigCtrlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 2, 2, 3),
    _SleMlsQosAggPoliceConfigCtrlTimer_Type()
)
sleMlsQosAggPoliceConfigCtrlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosAggPoliceConfigCtrlTimer.setStatus("current")
_SleMlsQosAggPoliceCtrlTimeStamp_Type = TimeTicks
_SleMlsQosAggPoliceCtrlTimeStamp_Object = MibScalar
sleMlsQosAggPoliceCtrlTimeStamp = _SleMlsQosAggPoliceCtrlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 2, 2, 4),
    _SleMlsQosAggPoliceCtrlTimeStamp_Type()
)
sleMlsQosAggPoliceCtrlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosAggPoliceCtrlTimeStamp.setStatus("current")
_SleMlsQosAggPoliceCtrlReqResult_Type = SleControlRequestResultType
_SleMlsQosAggPoliceCtrlReqResult_Object = MibScalar
sleMlsQosAggPoliceCtrlReqResult = _SleMlsQosAggPoliceCtrlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 2, 2, 5),
    _SleMlsQosAggPoliceCtrlReqResult_Type()
)
sleMlsQosAggPoliceCtrlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosAggPoliceCtrlReqResult.setStatus("current")
_SleMlsQosAggPoliceCtrlName_Type = OctetString
_SleMlsQosAggPoliceCtrlName_Object = MibScalar
sleMlsQosAggPoliceCtrlName = _SleMlsQosAggPoliceCtrlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 2, 2, 6),
    _SleMlsQosAggPoliceCtrlName_Type()
)
sleMlsQosAggPoliceCtrlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosAggPoliceCtrlName.setStatus("current")
_SleMlsQosAggPoliceCtrlTrafficRate_Type = Integer32
_SleMlsQosAggPoliceCtrlTrafficRate_Object = MibScalar
sleMlsQosAggPoliceCtrlTrafficRate = _SleMlsQosAggPoliceCtrlTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 2, 2, 7),
    _SleMlsQosAggPoliceCtrlTrafficRate_Type()
)
sleMlsQosAggPoliceCtrlTrafficRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosAggPoliceCtrlTrafficRate.setStatus("current")
_SleMlsQosAggPoliceCtrlBurstSize_Type = Integer32
_SleMlsQosAggPoliceCtrlBurstSize_Object = MibScalar
sleMlsQosAggPoliceCtrlBurstSize = _SleMlsQosAggPoliceCtrlBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 2, 2, 8),
    _SleMlsQosAggPoliceCtrlBurstSize_Type()
)
sleMlsQosAggPoliceCtrlBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosAggPoliceCtrlBurstSize.setStatus("current")
_SleMlsQosACL_ObjectIdentity = ObjectIdentity
sleMlsQosACL = _SleMlsQosACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3)
)
_SleMlsQosACLTable_Object = MibTable
sleMlsQosACLTable = _SleMlsQosACLTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1)
)
if mibBuilder.loadTexts:
    sleMlsQosACLTable.setStatus("current")
_SleMlsQosACLEntry_Object = MibTableRow
sleMlsQosACLEntry = _SleMlsQosACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1)
)
sleMlsQosACLEntry.setIndexNames(
    (0, "SLE-MLSQOS-MIB", "sleMlsQosACLIndex"),
    (0, "SLE-MLSQOS-MIB", "sleMlsQosACLFilterIndex"),
)
if mibBuilder.loadTexts:
    sleMlsQosACLEntry.setStatus("current")


class _SleMlsQosACLIndex_Type(Integer32):
    """Custom type sleMlsQosACLIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleMlsQosACLIndex_Type.__name__ = "Integer32"
_SleMlsQosACLIndex_Object = MibTableColumn
sleMlsQosACLIndex = _SleMlsQosACLIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 1),
    _SleMlsQosACLIndex_Type()
)
sleMlsQosACLIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMlsQosACLIndex.setStatus("current")


class _SleMlsQosACLFilterIndex_Type(Integer32):
    """Custom type sleMlsQosACLFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleMlsQosACLFilterIndex_Type.__name__ = "Integer32"
_SleMlsQosACLFilterIndex_Object = MibTableColumn
sleMlsQosACLFilterIndex = _SleMlsQosACLFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 2),
    _SleMlsQosACLFilterIndex_Type()
)
sleMlsQosACLFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMlsQosACLFilterIndex.setStatus("current")
_SleMlsQosACLName_Type = OctetString
_SleMlsQosACLName_Object = MibTableColumn
sleMlsQosACLName = _SleMlsQosACLName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 3),
    _SleMlsQosACLName_Type()
)
sleMlsQosACLName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLName.setStatus("current")
_SleMlsQosACLMatchType_Type = ACLMatchType
_SleMlsQosACLMatchType_Object = MibTableColumn
sleMlsQosACLMatchType = _SleMlsQosACLMatchType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 4),
    _SleMlsQosACLMatchType_Type()
)
sleMlsQosACLMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLMatchType.setStatus("current")
_SleMlsQosACLMatchAction_Type = ACLMatchActionType
_SleMlsQosACLMatchAction_Object = MibTableColumn
sleMlsQosACLMatchAction = _SleMlsQosACLMatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 5),
    _SleMlsQosACLMatchAction_Type()
)
sleMlsQosACLMatchAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLMatchAction.setStatus("current")
_SleMlsQosACLEtherType_Type = ACLEtherType
_SleMlsQosACLEtherType_Object = MibTableColumn
sleMlsQosACLEtherType = _SleMlsQosACLEtherType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 6),
    _SleMlsQosACLEtherType_Type()
)
sleMlsQosACLEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLEtherType.setStatus("current")


class _SleMlsQosACLL3Protocol_Type(Integer32):
    """Custom type sleMlsQosACLL3Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SleMlsQosACLL3Protocol_Type.__name__ = "Integer32"
_SleMlsQosACLL3Protocol_Object = MibTableColumn
sleMlsQosACLL3Protocol = _SleMlsQosACLL3Protocol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 7),
    _SleMlsQosACLL3Protocol_Type()
)
sleMlsQosACLL3Protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLL3Protocol.setStatus("current")
_SleMlsQosACLSrcIpAddress_Type = OctetString
_SleMlsQosACLSrcIpAddress_Object = MibTableColumn
sleMlsQosACLSrcIpAddress = _SleMlsQosACLSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 8),
    _SleMlsQosACLSrcIpAddress_Type()
)
sleMlsQosACLSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLSrcIpAddress.setStatus("current")
_SleMlsQosACLDstIpAddress_Type = OctetString
_SleMlsQosACLDstIpAddress_Object = MibTableColumn
sleMlsQosACLDstIpAddress = _SleMlsQosACLDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 9),
    _SleMlsQosACLDstIpAddress_Type()
)
sleMlsQosACLDstIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLDstIpAddress.setStatus("current")
_SleMlsQosACLSrcIpAddrMask_Type = OctetString
_SleMlsQosACLSrcIpAddrMask_Object = MibTableColumn
sleMlsQosACLSrcIpAddrMask = _SleMlsQosACLSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 10),
    _SleMlsQosACLSrcIpAddrMask_Type()
)
sleMlsQosACLSrcIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLSrcIpAddrMask.setStatus("current")
_SleMlsQosACLDstIpAddrMask_Type = OctetString
_SleMlsQosACLDstIpAddrMask_Object = MibTableColumn
sleMlsQosACLDstIpAddrMask = _SleMlsQosACLDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 11),
    _SleMlsQosACLDstIpAddrMask_Type()
)
sleMlsQosACLDstIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLDstIpAddrMask.setStatus("current")
_SleMlsQosACLSrcMacAddress_Type = OctetString
_SleMlsQosACLSrcMacAddress_Object = MibTableColumn
sleMlsQosACLSrcMacAddress = _SleMlsQosACLSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 12),
    _SleMlsQosACLSrcMacAddress_Type()
)
sleMlsQosACLSrcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLSrcMacAddress.setStatus("current")
_SleMlsQosACLDstMacAddress_Type = OctetString
_SleMlsQosACLDstMacAddress_Object = MibTableColumn
sleMlsQosACLDstMacAddress = _SleMlsQosACLDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 13),
    _SleMlsQosACLDstMacAddress_Type()
)
sleMlsQosACLDstMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLDstMacAddress.setStatus("current")
_SleMlsQosACLSrcMacAddrMask_Type = OctetString
_SleMlsQosACLSrcMacAddrMask_Object = MibTableColumn
sleMlsQosACLSrcMacAddrMask = _SleMlsQosACLSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 14),
    _SleMlsQosACLSrcMacAddrMask_Type()
)
sleMlsQosACLSrcMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLSrcMacAddrMask.setStatus("current")
_SleMlsQosACLDstMacAddrMask_Type = OctetString
_SleMlsQosACLDstMacAddrMask_Object = MibTableColumn
sleMlsQosACLDstMacAddrMask = _SleMlsQosACLDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 15),
    _SleMlsQosACLDstMacAddrMask_Type()
)
sleMlsQosACLDstMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLDstMacAddrMask.setStatus("current")
_SleMlsQosACLTcpUdpSrcPortAction_Type = AclTcpUdpPortActionType
_SleMlsQosACLTcpUdpSrcPortAction_Object = MibTableColumn
sleMlsQosACLTcpUdpSrcPortAction = _SleMlsQosACLTcpUdpSrcPortAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 16),
    _SleMlsQosACLTcpUdpSrcPortAction_Type()
)
sleMlsQosACLTcpUdpSrcPortAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLTcpUdpSrcPortAction.setStatus("current")
_SleMlsQosACLTcpUdpDstPortAction_Type = AclTcpUdpPortActionType
_SleMlsQosACLTcpUdpDstPortAction_Object = MibTableColumn
sleMlsQosACLTcpUdpDstPortAction = _SleMlsQosACLTcpUdpDstPortAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 17),
    _SleMlsQosACLTcpUdpDstPortAction_Type()
)
sleMlsQosACLTcpUdpDstPortAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLTcpUdpDstPortAction.setStatus("current")
_SleMlsQosACLTcpUdpSrcPort_Type = Integer32
_SleMlsQosACLTcpUdpSrcPort_Object = MibTableColumn
sleMlsQosACLTcpUdpSrcPort = _SleMlsQosACLTcpUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 18),
    _SleMlsQosACLTcpUdpSrcPort_Type()
)
sleMlsQosACLTcpUdpSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLTcpUdpSrcPort.setStatus("current")
_SleMlsQosACLTcpUdpDstPort_Type = Integer32
_SleMlsQosACLTcpUdpDstPort_Object = MibTableColumn
sleMlsQosACLTcpUdpDstPort = _SleMlsQosACLTcpUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 19),
    _SleMlsQosACLTcpUdpDstPort_Type()
)
sleMlsQosACLTcpUdpDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLTcpUdpDstPort.setStatus("current")
_SleMlsQosACLNameSrcIpExactMatch_Type = Integer32
_SleMlsQosACLNameSrcIpExactMatch_Object = MibTableColumn
sleMlsQosACLNameSrcIpExactMatch = _SleMlsQosACLNameSrcIpExactMatch_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 20),
    _SleMlsQosACLNameSrcIpExactMatch_Type()
)
sleMlsQosACLNameSrcIpExactMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLNameSrcIpExactMatch.setStatus("current")
_SleMlsQosACLActionRemarkDesc_Type = OctetString
_SleMlsQosACLActionRemarkDesc_Object = MibTableColumn
sleMlsQosACLActionRemarkDesc = _SleMlsQosACLActionRemarkDesc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 21),
    _SleMlsQosACLActionRemarkDesc_Type()
)
sleMlsQosACLActionRemarkDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLActionRemarkDesc.setStatus("current")
_SleMlsQosACLIcmpType_Type = Integer32
_SleMlsQosACLIcmpType_Object = MibTableColumn
sleMlsQosACLIcmpType = _SleMlsQosACLIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 22),
    _SleMlsQosACLIcmpType_Type()
)
sleMlsQosACLIcmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLIcmpType.setStatus("current")
_SleMlsQosACLIcmpCode_Type = Integer32
_SleMlsQosACLIcmpCode_Object = MibTableColumn
sleMlsQosACLIcmpCode = _SleMlsQosACLIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 23),
    _SleMlsQosACLIcmpCode_Type()
)
sleMlsQosACLIcmpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLIcmpCode.setStatus("current")
_SleMlsQosACLTcpUdpSrcPortEnd_Type = Integer32
_SleMlsQosACLTcpUdpSrcPortEnd_Object = MibTableColumn
sleMlsQosACLTcpUdpSrcPortEnd = _SleMlsQosACLTcpUdpSrcPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 24),
    _SleMlsQosACLTcpUdpSrcPortEnd_Type()
)
sleMlsQosACLTcpUdpSrcPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLTcpUdpSrcPortEnd.setStatus("current")
_SleMlsQosACLTcpUdpDstPortEnd_Type = Integer32
_SleMlsQosACLTcpUdpDstPortEnd_Object = MibTableColumn
sleMlsQosACLTcpUdpDstPortEnd = _SleMlsQosACLTcpUdpDstPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 1, 1, 25),
    _SleMlsQosACLTcpUdpDstPortEnd_Type()
)
sleMlsQosACLTcpUdpDstPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLTcpUdpDstPortEnd.setStatus("current")
_SleMlsQosACLControl_ObjectIdentity = ObjectIdentity
sleMlsQosACLControl = _SleMlsQosACLControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2)
)


class _SleMlsQosACLControlRequest_Type(Integer32):
    """Custom type sleMlsQosACLControlRequest based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("setStandAclMatchSrcIp", 1),
          ("unSetStandAclMatchSrcIp", 2),
          ("setExtenAclMatchMac", 3),
          ("unSetExtenAclMatchMac", 4),
          ("setExtenAclMatchEthType", 5),
          ("unSetExtenAclMatchEthType", 6),
          ("setExtenAclMatchL3Proto", 7),
          ("unSetExtenAclMatchL3Proto", 8),
          ("setExtenAclMatchTcpUdp", 9),
          ("unSetExtenAclMatchTcpUdp", 10),
          ("setAclNameSrcIp", 11),
          ("unSetAclNameSrcIp", 12),
          ("setAclWithActionRemark", 13),
          ("unSetAclWithActionRemark", 14))
    )


_SleMlsQosACLControlRequest_Type.__name__ = "Integer32"
_SleMlsQosACLControlRequest_Object = MibScalar
sleMlsQosACLControlRequest = _SleMlsQosACLControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 1),
    _SleMlsQosACLControlRequest_Type()
)
sleMlsQosACLControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLControlRequest.setStatus("current")
_SleMlsQosACLControlStatus_Type = SleControlStatusType
_SleMlsQosACLControlStatus_Object = MibScalar
sleMlsQosACLControlStatus = _SleMlsQosACLControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 2),
    _SleMlsQosACLControlStatus_Type()
)
sleMlsQosACLControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLControlStatus.setStatus("current")
_SleMlsQosACLConfigControlTimer_Type = Gauge32
_SleMlsQosACLConfigControlTimer_Object = MibScalar
sleMlsQosACLConfigControlTimer = _SleMlsQosACLConfigControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 3),
    _SleMlsQosACLConfigControlTimer_Type()
)
sleMlsQosACLConfigControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLConfigControlTimer.setStatus("current")
_SleMlsQosACLControlTimeStamp_Type = TimeTicks
_SleMlsQosACLControlTimeStamp_Object = MibScalar
sleMlsQosACLControlTimeStamp = _SleMlsQosACLControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 4),
    _SleMlsQosACLControlTimeStamp_Type()
)
sleMlsQosACLControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLControlTimeStamp.setStatus("current")
_SleMlsQosACLControlReqResult_Type = SleControlRequestResultType
_SleMlsQosACLControlReqResult_Object = MibScalar
sleMlsQosACLControlReqResult = _SleMlsQosACLControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 5),
    _SleMlsQosACLControlReqResult_Type()
)
sleMlsQosACLControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosACLControlReqResult.setStatus("current")
_SleMlsQosACLCtrlName_Type = OctetString
_SleMlsQosACLCtrlName_Object = MibScalar
sleMlsQosACLCtrlName = _SleMlsQosACLCtrlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 6),
    _SleMlsQosACLCtrlName_Type()
)
sleMlsQosACLCtrlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlName.setStatus("current")
_SleMlsQosACLCtrlMatchType_Type = ACLMatchType
_SleMlsQosACLCtrlMatchType_Object = MibScalar
sleMlsQosACLCtrlMatchType = _SleMlsQosACLCtrlMatchType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 7),
    _SleMlsQosACLCtrlMatchType_Type()
)
sleMlsQosACLCtrlMatchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlMatchType.setStatus("current")
_SleMlsQosACLCtrlMatchAction_Type = ACLMatchActionType
_SleMlsQosACLCtrlMatchAction_Object = MibScalar
sleMlsQosACLCtrlMatchAction = _SleMlsQosACLCtrlMatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 8),
    _SleMlsQosACLCtrlMatchAction_Type()
)
sleMlsQosACLCtrlMatchAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlMatchAction.setStatus("current")
_SleMlsQosACLCtrlEtherType_Type = ACLEtherType
_SleMlsQosACLCtrlEtherType_Object = MibScalar
sleMlsQosACLCtrlEtherType = _SleMlsQosACLCtrlEtherType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 9),
    _SleMlsQosACLCtrlEtherType_Type()
)
sleMlsQosACLCtrlEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlEtherType.setStatus("current")


class _SleMlsQosACLCtrlL3Protocol_Type(Integer32):
    """Custom type sleMlsQosACLCtrlL3Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SleMlsQosACLCtrlL3Protocol_Type.__name__ = "Integer32"
_SleMlsQosACLCtrlL3Protocol_Object = MibScalar
sleMlsQosACLCtrlL3Protocol = _SleMlsQosACLCtrlL3Protocol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 10),
    _SleMlsQosACLCtrlL3Protocol_Type()
)
sleMlsQosACLCtrlL3Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlL3Protocol.setStatus("current")
_SleMlsQosACLCtrlSrcAddress_Type = OctetString
_SleMlsQosACLCtrlSrcAddress_Object = MibScalar
sleMlsQosACLCtrlSrcAddress = _SleMlsQosACLCtrlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 11),
    _SleMlsQosACLCtrlSrcAddress_Type()
)
sleMlsQosACLCtrlSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlSrcAddress.setStatus("current")
_SleMlsQosACLCtrlDstAddress_Type = OctetString
_SleMlsQosACLCtrlDstAddress_Object = MibScalar
sleMlsQosACLCtrlDstAddress = _SleMlsQosACLCtrlDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 12),
    _SleMlsQosACLCtrlDstAddress_Type()
)
sleMlsQosACLCtrlDstAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlDstAddress.setStatus("current")
_SleMlsQosACLCtrlSrcAddrMask_Type = OctetString
_SleMlsQosACLCtrlSrcAddrMask_Object = MibScalar
sleMlsQosACLCtrlSrcAddrMask = _SleMlsQosACLCtrlSrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 13),
    _SleMlsQosACLCtrlSrcAddrMask_Type()
)
sleMlsQosACLCtrlSrcAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlSrcAddrMask.setStatus("current")
_SleMlsQosACLCtrlDstAddrMask_Type = OctetString
_SleMlsQosACLCtrlDstAddrMask_Object = MibScalar
sleMlsQosACLCtrlDstAddrMask = _SleMlsQosACLCtrlDstAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 14),
    _SleMlsQosACLCtrlDstAddrMask_Type()
)
sleMlsQosACLCtrlDstAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlDstAddrMask.setStatus("current")
_SleMlsQosACLCtrlTcpUdpSrcPortAction_Type = AclTcpUdpPortActionType
_SleMlsQosACLCtrlTcpUdpSrcPortAction_Object = MibScalar
sleMlsQosACLCtrlTcpUdpSrcPortAction = _SleMlsQosACLCtrlTcpUdpSrcPortAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 15),
    _SleMlsQosACLCtrlTcpUdpSrcPortAction_Type()
)
sleMlsQosACLCtrlTcpUdpSrcPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlTcpUdpSrcPortAction.setStatus("current")
_SleMlsQosACLCtrlTcpUdpDstPortAction_Type = AclTcpUdpPortActionType
_SleMlsQosACLCtrlTcpUdpDstPortAction_Object = MibScalar
sleMlsQosACLCtrlTcpUdpDstPortAction = _SleMlsQosACLCtrlTcpUdpDstPortAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 16),
    _SleMlsQosACLCtrlTcpUdpDstPortAction_Type()
)
sleMlsQosACLCtrlTcpUdpDstPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlTcpUdpDstPortAction.setStatus("current")
_SleMlsQosACLCtrlTcpUdpSrcPort_Type = Integer32
_SleMlsQosACLCtrlTcpUdpSrcPort_Object = MibScalar
sleMlsQosACLCtrlTcpUdpSrcPort = _SleMlsQosACLCtrlTcpUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 17),
    _SleMlsQosACLCtrlTcpUdpSrcPort_Type()
)
sleMlsQosACLCtrlTcpUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlTcpUdpSrcPort.setStatus("current")
_SleMlsQosACLCtrlTcpUdpDstPort_Type = Integer32
_SleMlsQosACLCtrlTcpUdpDstPort_Object = MibScalar
sleMlsQosACLCtrlTcpUdpDstPort = _SleMlsQosACLCtrlTcpUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 18),
    _SleMlsQosACLCtrlTcpUdpDstPort_Type()
)
sleMlsQosACLCtrlTcpUdpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlTcpUdpDstPort.setStatus("current")
_SleMlsQosACLCtrlAclNameExactMatch_Type = Integer32
_SleMlsQosACLCtrlAclNameExactMatch_Object = MibScalar
sleMlsQosACLCtrlAclNameExactMatch = _SleMlsQosACLCtrlAclNameExactMatch_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 19),
    _SleMlsQosACLCtrlAclNameExactMatch_Type()
)
sleMlsQosACLCtrlAclNameExactMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlAclNameExactMatch.setStatus("current")
_SleMlsQosACLCtrlActionRemarkDesc_Type = OctetString
_SleMlsQosACLCtrlActionRemarkDesc_Object = MibScalar
sleMlsQosACLCtrlActionRemarkDesc = _SleMlsQosACLCtrlActionRemarkDesc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 20),
    _SleMlsQosACLCtrlActionRemarkDesc_Type()
)
sleMlsQosACLCtrlActionRemarkDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlActionRemarkDesc.setStatus("current")
_SleMlsQosACLCtrlIcmpType_Type = Integer32
_SleMlsQosACLCtrlIcmpType_Object = MibScalar
sleMlsQosACLCtrlIcmpType = _SleMlsQosACLCtrlIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 21),
    _SleMlsQosACLCtrlIcmpType_Type()
)
sleMlsQosACLCtrlIcmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlIcmpType.setStatus("current")
_SleMlsQosACLCtrlIcmpCode_Type = Integer32
_SleMlsQosACLCtrlIcmpCode_Object = MibScalar
sleMlsQosACLCtrlIcmpCode = _SleMlsQosACLCtrlIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 22),
    _SleMlsQosACLCtrlIcmpCode_Type()
)
sleMlsQosACLCtrlIcmpCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlIcmpCode.setStatus("current")
_SleMlsQosACLCtrlTcpUdpSrcPortEnd_Type = Integer32
_SleMlsQosACLCtrlTcpUdpSrcPortEnd_Object = MibScalar
sleMlsQosACLCtrlTcpUdpSrcPortEnd = _SleMlsQosACLCtrlTcpUdpSrcPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 23),
    _SleMlsQosACLCtrlTcpUdpSrcPortEnd_Type()
)
sleMlsQosACLCtrlTcpUdpSrcPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlTcpUdpSrcPortEnd.setStatus("current")
_SleMlsQosACLCtrlTcpUdpDstPortEnd_Type = Integer32
_SleMlsQosACLCtrlTcpUdpDstPortEnd_Object = MibScalar
sleMlsQosACLCtrlTcpUdpDstPortEnd = _SleMlsQosACLCtrlTcpUdpDstPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 2, 24),
    _SleMlsQosACLCtrlTcpUdpDstPortEnd_Type()
)
sleMlsQosACLCtrlTcpUdpDstPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosACLCtrlTcpUdpDstPortEnd.setStatus("current")
_SleMlsQosACLNotification_ObjectIdentity = ObjectIdentity
sleMlsQosACLNotification = _SleMlsQosACLNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 3, 3)
)
_SleMlsQosClassMap_ObjectIdentity = ObjectIdentity
sleMlsQosClassMap = _SleMlsQosClassMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4)
)
_SleMlsQosClassMapTable_Object = MibTable
sleMlsQosClassMapTable = _SleMlsQosClassMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1)
)
if mibBuilder.loadTexts:
    sleMlsQosClassMapTable.setStatus("current")
_SleMlsQosClassMapEntry_Object = MibTableRow
sleMlsQosClassMapEntry = _SleMlsQosClassMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1)
)
sleMlsQosClassMapEntry.setIndexNames(
    (0, "SLE-MLSQOS-MIB", "sleMlsQosClassMapName"),
)
if mibBuilder.loadTexts:
    sleMlsQosClassMapEntry.setStatus("current")
_SleMlsQosClassMapName_Type = OctetString
_SleMlsQosClassMapName_Object = MibTableColumn
sleMlsQosClassMapName = _SleMlsQosClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 1),
    _SleMlsQosClassMapName_Type()
)
sleMlsQosClassMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMlsQosClassMapName.setStatus("current")
_SleMlsQosClassMapMatchCosValue_Type = Integer32
_SleMlsQosClassMapMatchCosValue_Object = MibTableColumn
sleMlsQosClassMapMatchCosValue = _SleMlsQosClassMapMatchCosValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 2),
    _SleMlsQosClassMapMatchCosValue_Type()
)
sleMlsQosClassMapMatchCosValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchCosValue.setStatus("current")
_SleMlsQosClassMapMatchInnerCosValue_Type = Integer32
_SleMlsQosClassMapMatchInnerCosValue_Object = MibTableColumn
sleMlsQosClassMapMatchInnerCosValue = _SleMlsQosClassMapMatchInnerCosValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 3),
    _SleMlsQosClassMapMatchInnerCosValue_Type()
)
sleMlsQosClassMapMatchInnerCosValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchInnerCosValue.setStatus("current")
_SleMlsQosClassMapMatchEgressInterface_Type = OctetString
_SleMlsQosClassMapMatchEgressInterface_Object = MibTableColumn
sleMlsQosClassMapMatchEgressInterface = _SleMlsQosClassMapMatchEgressInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 4),
    _SleMlsQosClassMapMatchEgressInterface_Type()
)
sleMlsQosClassMapMatchEgressInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchEgressInterface.setStatus("current")
_SleMlsQosClassMapMatchEtherType_Type = OctetString
_SleMlsQosClassMapMatchEtherType_Object = MibTableColumn
sleMlsQosClassMapMatchEtherType = _SleMlsQosClassMapMatchEtherType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 5),
    _SleMlsQosClassMapMatchEtherType_Type()
)
sleMlsQosClassMapMatchEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchEtherType.setStatus("current")
_SleMlsQosClassMapMatchSrcIpAddr_Type = OctetString
_SleMlsQosClassMapMatchSrcIpAddr_Object = MibTableColumn
sleMlsQosClassMapMatchSrcIpAddr = _SleMlsQosClassMapMatchSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 6),
    _SleMlsQosClassMapMatchSrcIpAddr_Type()
)
sleMlsQosClassMapMatchSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchSrcIpAddr.setStatus("current")
_SleMlsQosClassMapMatchDstIpAddr_Type = OctetString
_SleMlsQosClassMapMatchDstIpAddr_Object = MibTableColumn
sleMlsQosClassMapMatchDstIpAddr = _SleMlsQosClassMapMatchDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 7),
    _SleMlsQosClassMapMatchDstIpAddr_Type()
)
sleMlsQosClassMapMatchDstIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchDstIpAddr.setStatus("current")
_SleMlsQosClassMapMatchSrcIpMaskLen_Type = Integer32
_SleMlsQosClassMapMatchSrcIpMaskLen_Object = MibTableColumn
sleMlsQosClassMapMatchSrcIpMaskLen = _SleMlsQosClassMapMatchSrcIpMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 8),
    _SleMlsQosClassMapMatchSrcIpMaskLen_Type()
)
sleMlsQosClassMapMatchSrcIpMaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchSrcIpMaskLen.setStatus("current")
_SleMlsQosClassMapMatchDstIpMaskLen_Type = Integer32
_SleMlsQosClassMapMatchDstIpMaskLen_Object = MibTableColumn
sleMlsQosClassMapMatchDstIpMaskLen = _SleMlsQosClassMapMatchDstIpMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 9),
    _SleMlsQosClassMapMatchDstIpMaskLen_Type()
)
sleMlsQosClassMapMatchDstIpMaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchDstIpMaskLen.setStatus("current")
_SleMlsQosClassMapMatchSrcIpV6Addr_Type = OctetString
_SleMlsQosClassMapMatchSrcIpV6Addr_Object = MibTableColumn
sleMlsQosClassMapMatchSrcIpV6Addr = _SleMlsQosClassMapMatchSrcIpV6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 10),
    _SleMlsQosClassMapMatchSrcIpV6Addr_Type()
)
sleMlsQosClassMapMatchSrcIpV6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchSrcIpV6Addr.setStatus("current")
_SleMlsQosClassMapMatchDstIpV6Addr_Type = OctetString
_SleMlsQosClassMapMatchDstIpV6Addr_Object = MibTableColumn
sleMlsQosClassMapMatchDstIpV6Addr = _SleMlsQosClassMapMatchDstIpV6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 11),
    _SleMlsQosClassMapMatchDstIpV6Addr_Type()
)
sleMlsQosClassMapMatchDstIpV6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchDstIpV6Addr.setStatus("current")
_SleMlsQosClassMapMatchSrcIpV6MaskLen_Type = Integer32
_SleMlsQosClassMapMatchSrcIpV6MaskLen_Object = MibTableColumn
sleMlsQosClassMapMatchSrcIpV6MaskLen = _SleMlsQosClassMapMatchSrcIpV6MaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 12),
    _SleMlsQosClassMapMatchSrcIpV6MaskLen_Type()
)
sleMlsQosClassMapMatchSrcIpV6MaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchSrcIpV6MaskLen.setStatus("current")
_SleMlsQosClassMapMatchDstIpV6MaskLen_Type = Integer32
_SleMlsQosClassMapMatchDstIpV6MaskLen_Object = MibTableColumn
sleMlsQosClassMapMatchDstIpV6MaskLen = _SleMlsQosClassMapMatchDstIpV6MaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 13),
    _SleMlsQosClassMapMatchDstIpV6MaskLen_Type()
)
sleMlsQosClassMapMatchDstIpV6MaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchDstIpV6MaskLen.setStatus("current")
_SleMlsQosClassMapMatchIpDscp_Type = Integer32
_SleMlsQosClassMapMatchIpDscp_Object = MibTableColumn
sleMlsQosClassMapMatchIpDscp = _SleMlsQosClassMapMatchIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 14),
    _SleMlsQosClassMapMatchIpDscp_Type()
)
sleMlsQosClassMapMatchIpDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchIpDscp.setStatus("current")
_SleMlsQosClassMapMatchIpPrecedence_Type = Integer32
_SleMlsQosClassMapMatchIpPrecedence_Object = MibTableColumn
sleMlsQosClassMapMatchIpPrecedence = _SleMlsQosClassMapMatchIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 15),
    _SleMlsQosClassMapMatchIpPrecedence_Type()
)
sleMlsQosClassMapMatchIpPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchIpPrecedence.setStatus("current")
_SleMlsQosClassMapMatchIp6Dscp_Type = Integer32
_SleMlsQosClassMapMatchIp6Dscp_Object = MibTableColumn
sleMlsQosClassMapMatchIp6Dscp = _SleMlsQosClassMapMatchIp6Dscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 16),
    _SleMlsQosClassMapMatchIp6Dscp_Type()
)
sleMlsQosClassMapMatchIp6Dscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchIp6Dscp.setStatus("current")
_SleMlsQosClassMapMatchIp6Precedence_Type = Integer32
_SleMlsQosClassMapMatchIp6Precedence_Object = MibTableColumn
sleMlsQosClassMapMatchIp6Precedence = _SleMlsQosClassMapMatchIp6Precedence_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 17),
    _SleMlsQosClassMapMatchIp6Precedence_Type()
)
sleMlsQosClassMapMatchIp6Precedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchIp6Precedence.setStatus("current")
_SleMlsQosClassMapMatchTcpSrcPort_Type = OctetString
_SleMlsQosClassMapMatchTcpSrcPort_Object = MibTableColumn
sleMlsQosClassMapMatchTcpSrcPort = _SleMlsQosClassMapMatchTcpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 18),
    _SleMlsQosClassMapMatchTcpSrcPort_Type()
)
sleMlsQosClassMapMatchTcpSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchTcpSrcPort.setStatus("current")
_SleMlsQosClassMapMatchTcpDstPort_Type = OctetString
_SleMlsQosClassMapMatchTcpDstPort_Object = MibTableColumn
sleMlsQosClassMapMatchTcpDstPort = _SleMlsQosClassMapMatchTcpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 19),
    _SleMlsQosClassMapMatchTcpDstPort_Type()
)
sleMlsQosClassMapMatchTcpDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchTcpDstPort.setStatus("current")
_SleMlsQosClassMapMatchTcpSrcPortRange_Type = OctetString
_SleMlsQosClassMapMatchTcpSrcPortRange_Object = MibTableColumn
sleMlsQosClassMapMatchTcpSrcPortRange = _SleMlsQosClassMapMatchTcpSrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 20),
    _SleMlsQosClassMapMatchTcpSrcPortRange_Type()
)
sleMlsQosClassMapMatchTcpSrcPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchTcpSrcPortRange.setStatus("current")
_SleMlsQosClassMapMatchTcpDstPortRange_Type = OctetString
_SleMlsQosClassMapMatchTcpDstPortRange_Object = MibTableColumn
sleMlsQosClassMapMatchTcpDstPortRange = _SleMlsQosClassMapMatchTcpDstPortRange_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 21),
    _SleMlsQosClassMapMatchTcpDstPortRange_Type()
)
sleMlsQosClassMapMatchTcpDstPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchTcpDstPortRange.setStatus("current")
_SleMlsQosClassMapMatchUdpSrcPort_Type = OctetString
_SleMlsQosClassMapMatchUdpSrcPort_Object = MibTableColumn
sleMlsQosClassMapMatchUdpSrcPort = _SleMlsQosClassMapMatchUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 22),
    _SleMlsQosClassMapMatchUdpSrcPort_Type()
)
sleMlsQosClassMapMatchUdpSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchUdpSrcPort.setStatus("current")
_SleMlsQosClassMapMatchUdpDstPort_Type = OctetString
_SleMlsQosClassMapMatchUdpDstPort_Object = MibTableColumn
sleMlsQosClassMapMatchUdpDstPort = _SleMlsQosClassMapMatchUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 23),
    _SleMlsQosClassMapMatchUdpDstPort_Type()
)
sleMlsQosClassMapMatchUdpDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchUdpDstPort.setStatus("current")
_SleMlsQosClassMapMatchUdpSrcPortRange_Type = OctetString
_SleMlsQosClassMapMatchUdpSrcPortRange_Object = MibTableColumn
sleMlsQosClassMapMatchUdpSrcPortRange = _SleMlsQosClassMapMatchUdpSrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 24),
    _SleMlsQosClassMapMatchUdpSrcPortRange_Type()
)
sleMlsQosClassMapMatchUdpSrcPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchUdpSrcPortRange.setStatus("current")
_SleMlsQosClassMapMatchUdpDstPortRange_Type = OctetString
_SleMlsQosClassMapMatchUdpDstPortRange_Object = MibTableColumn
sleMlsQosClassMapMatchUdpDstPortRange = _SleMlsQosClassMapMatchUdpDstPortRange_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 25),
    _SleMlsQosClassMapMatchUdpDstPortRange_Type()
)
sleMlsQosClassMapMatchUdpDstPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchUdpDstPortRange.setStatus("current")
_SleMlsQosClassMapMatchSrcMacAddr_Type = OctetString
_SleMlsQosClassMapMatchSrcMacAddr_Object = MibTableColumn
sleMlsQosClassMapMatchSrcMacAddr = _SleMlsQosClassMapMatchSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 26),
    _SleMlsQosClassMapMatchSrcMacAddr_Type()
)
sleMlsQosClassMapMatchSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchSrcMacAddr.setStatus("current")
_SleMlsQosClassMapMatchSrcMacMask_Type = OctetString
_SleMlsQosClassMapMatchSrcMacMask_Object = MibTableColumn
sleMlsQosClassMapMatchSrcMacMask = _SleMlsQosClassMapMatchSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 27),
    _SleMlsQosClassMapMatchSrcMacMask_Type()
)
sleMlsQosClassMapMatchSrcMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchSrcMacMask.setStatus("current")
_SleMlsQosClassMapMatchDstMacAddr_Type = OctetString
_SleMlsQosClassMapMatchDstMacAddr_Object = MibTableColumn
sleMlsQosClassMapMatchDstMacAddr = _SleMlsQosClassMapMatchDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 28),
    _SleMlsQosClassMapMatchDstMacAddr_Type()
)
sleMlsQosClassMapMatchDstMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchDstMacAddr.setStatus("current")
_SleMlsQosClassMapMatchDstMacMask_Type = OctetString
_SleMlsQosClassMapMatchDstMacMask_Object = MibTableColumn
sleMlsQosClassMapMatchDstMacMask = _SleMlsQosClassMapMatchDstMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 29),
    _SleMlsQosClassMapMatchDstMacMask_Type()
)
sleMlsQosClassMapMatchDstMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchDstMacMask.setStatus("current")
_SleMlsQosClassMapMatchVlanId_Type = OctetString
_SleMlsQosClassMapMatchVlanId_Object = MibTableColumn
sleMlsQosClassMapMatchVlanId = _SleMlsQosClassMapMatchVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 30),
    _SleMlsQosClassMapMatchVlanId_Type()
)
sleMlsQosClassMapMatchVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchVlanId.setStatus("current")
_SleMlsQosClassMapMatchVlanIdRange_Type = OctetString
_SleMlsQosClassMapMatchVlanIdRange_Object = MibTableColumn
sleMlsQosClassMapMatchVlanIdRange = _SleMlsQosClassMapMatchVlanIdRange_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 31),
    _SleMlsQosClassMapMatchVlanIdRange_Type()
)
sleMlsQosClassMapMatchVlanIdRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchVlanIdRange.setStatus("current")
_SleMlsQosClassMapMatchInnerVlanId_Type = Integer32
_SleMlsQosClassMapMatchInnerVlanId_Object = MibTableColumn
sleMlsQosClassMapMatchInnerVlanId = _SleMlsQosClassMapMatchInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 32),
    _SleMlsQosClassMapMatchInnerVlanId_Type()
)
sleMlsQosClassMapMatchInnerVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchInnerVlanId.setStatus("current")
_SleMlsQosClassMapMatchVlanTpid_Type = OctetString
_SleMlsQosClassMapMatchVlanTpid_Object = MibTableColumn
sleMlsQosClassMapMatchVlanTpid = _SleMlsQosClassMapMatchVlanTpid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 33),
    _SleMlsQosClassMapMatchVlanTpid_Type()
)
sleMlsQosClassMapMatchVlanTpid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchVlanTpid.setStatus("current")
_SleMlsQosClassMapMatchAccessGroup_Type = OctetString
_SleMlsQosClassMapMatchAccessGroup_Object = MibTableColumn
sleMlsQosClassMapMatchAccessGroup = _SleMlsQosClassMapMatchAccessGroup_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 34),
    _SleMlsQosClassMapMatchAccessGroup_Type()
)
sleMlsQosClassMapMatchAccessGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchAccessGroup.setStatus("current")
_SleMlsQosClassMapMatchLayer4SrcPort_Type = OctetString
_SleMlsQosClassMapMatchLayer4SrcPort_Object = MibTableColumn
sleMlsQosClassMapMatchLayer4SrcPort = _SleMlsQosClassMapMatchLayer4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 35),
    _SleMlsQosClassMapMatchLayer4SrcPort_Type()
)
sleMlsQosClassMapMatchLayer4SrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchLayer4SrcPort.setStatus("current")
_SleMlsQosClassMapMatchLayer4DstPort_Type = OctetString
_SleMlsQosClassMapMatchLayer4DstPort_Object = MibTableColumn
sleMlsQosClassMapMatchLayer4DstPort = _SleMlsQosClassMapMatchLayer4DstPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 36),
    _SleMlsQosClassMapMatchLayer4DstPort_Type()
)
sleMlsQosClassMapMatchLayer4DstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchLayer4DstPort.setStatus("current")
_SleMlsQosClassMapMatchLayer4SrcPortRange_Type = OctetString
_SleMlsQosClassMapMatchLayer4SrcPortRange_Object = MibTableColumn
sleMlsQosClassMapMatchLayer4SrcPortRange = _SleMlsQosClassMapMatchLayer4SrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 37),
    _SleMlsQosClassMapMatchLayer4SrcPortRange_Type()
)
sleMlsQosClassMapMatchLayer4SrcPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchLayer4SrcPortRange.setStatus("current")
_SleMlsQosClassMapMatchLayer4DstPortRange_Type = OctetString
_SleMlsQosClassMapMatchLayer4DstPortRange_Object = MibTableColumn
sleMlsQosClassMapMatchLayer4DstPortRange = _SleMlsQosClassMapMatchLayer4DstPortRange_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 38),
    _SleMlsQosClassMapMatchLayer4DstPortRange_Type()
)
sleMlsQosClassMapMatchLayer4DstPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapMatchLayer4DstPortRange.setStatus("current")


class _SleMplsQosClassMapMatchCriteria_Type(Integer32):
    """Custom type sleMplsQosClassMapMatchCriteria based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noMatch", 0),
          ("matchAll", 1),
          ("matchAny", 2))
    )


_SleMplsQosClassMapMatchCriteria_Type.__name__ = "Integer32"
_SleMplsQosClassMapMatchCriteria_Object = MibTableColumn
sleMplsQosClassMapMatchCriteria = _SleMplsQosClassMapMatchCriteria_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 1, 1, 39),
    _SleMplsQosClassMapMatchCriteria_Type()
)
sleMplsQosClassMapMatchCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsQosClassMapMatchCriteria.setStatus("current")
_SleMlsQosClassMapControl_ObjectIdentity = ObjectIdentity
sleMlsQosClassMapControl = _SleMlsQosClassMapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2)
)


class _SleMlsQosClassMapControlRequest_Type(Integer32):
    """Custom type sleMlsQosClassMapControlRequest based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("createClassMap", 1),
          ("deleteClassMap", 2),
          ("setClassMapMatch", 3),
          ("unSetClassMapMatch", 4),
          ("setClassMapMatchRange", 5),
          ("unSetClassMapMatchRange", 6),
          ("setClassMapMatchEtherType", 7),
          ("unSetClassMapMatchEtherType", 8),
          ("setClassMapMatchIpAddr", 9),
          ("unSetClassMapMatchIpAddr", 10),
          ("setClassMapMatchMac", 11),
          ("unSetClassMapMatchMac", 12),
          ("setClassMapMatchVlanTpid", 13),
          ("unSetClassMapMatchVlanTpid", 14),
          ("setClassMapMatchAccessGroup", 15),
          ("unSetClassMapMatchAccessGroup", 16),
          ("setClassMapMatchEgressIntf", 17),
          ("unSetClassMapMatchEgressIntf", 18))
    )


_SleMlsQosClassMapControlRequest_Type.__name__ = "Integer32"
_SleMlsQosClassMapControlRequest_Object = MibScalar
sleMlsQosClassMapControlRequest = _SleMlsQosClassMapControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 1),
    _SleMlsQosClassMapControlRequest_Type()
)
sleMlsQosClassMapControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapControlRequest.setStatus("current")
_SleMlsQosClassMapControlStatus_Type = SleControlStatusType
_SleMlsQosClassMapControlStatus_Object = MibScalar
sleMlsQosClassMapControlStatus = _SleMlsQosClassMapControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 2),
    _SleMlsQosClassMapControlStatus_Type()
)
sleMlsQosClassMapControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapControlStatus.setStatus("current")
_SleMlsQosClassMapControlTimer_Type = Gauge32
_SleMlsQosClassMapControlTimer_Object = MibScalar
sleMlsQosClassMapControlTimer = _SleMlsQosClassMapControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 3),
    _SleMlsQosClassMapControlTimer_Type()
)
sleMlsQosClassMapControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapControlTimer.setStatus("current")
_SleMlsQosClassMapontrolTimeStamp_Type = TimeTicks
_SleMlsQosClassMapontrolTimeStamp_Object = MibScalar
sleMlsQosClassMapontrolTimeStamp = _SleMlsQosClassMapontrolTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 4),
    _SleMlsQosClassMapontrolTimeStamp_Type()
)
sleMlsQosClassMapontrolTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapontrolTimeStamp.setStatus("current")
_SleMlsQosClassMapControlReqResult_Type = SleControlRequestResultType
_SleMlsQosClassMapControlReqResult_Object = MibScalar
sleMlsQosClassMapControlReqResult = _SleMlsQosClassMapControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 5),
    _SleMlsQosClassMapControlReqResult_Type()
)
sleMlsQosClassMapControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosClassMapControlReqResult.setStatus("current")
_SleMlsQosClassMapCtrlName_Type = OctetString
_SleMlsQosClassMapCtrlName_Object = MibScalar
sleMlsQosClassMapCtrlName = _SleMlsQosClassMapCtrlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 6),
    _SleMlsQosClassMapCtrlName_Type()
)
sleMlsQosClassMapCtrlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapCtrlName.setStatus("current")
_SleMlsQosClassMapCtrlMatchType_Type = ClassMapMatchType
_SleMlsQosClassMapCtrlMatchType_Object = MibScalar
sleMlsQosClassMapCtrlMatchType = _SleMlsQosClassMapCtrlMatchType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 7),
    _SleMlsQosClassMapCtrlMatchType_Type()
)
sleMlsQosClassMapCtrlMatchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapCtrlMatchType.setStatus("current")
_SleMlsQosClassMapCtrlMatchVal_Type = Integer32
_SleMlsQosClassMapCtrlMatchVal_Object = MibScalar
sleMlsQosClassMapCtrlMatchVal = _SleMlsQosClassMapCtrlMatchVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 8),
    _SleMlsQosClassMapCtrlMatchVal_Type()
)
sleMlsQosClassMapCtrlMatchVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapCtrlMatchVal.setStatus("current")
_SleMlsQosClassMapCtrlMatchRangeType_Type = ClassMapMatchRangeType
_SleMlsQosClassMapCtrlMatchRangeType_Object = MibScalar
sleMlsQosClassMapCtrlMatchRangeType = _SleMlsQosClassMapCtrlMatchRangeType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 9),
    _SleMlsQosClassMapCtrlMatchRangeType_Type()
)
sleMlsQosClassMapCtrlMatchRangeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapCtrlMatchRangeType.setStatus("current")
_SleMlsQosClassMapCtrlMatchRangeLow_Type = Integer32
_SleMlsQosClassMapCtrlMatchRangeLow_Object = MibScalar
sleMlsQosClassMapCtrlMatchRangeLow = _SleMlsQosClassMapCtrlMatchRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 10),
    _SleMlsQosClassMapCtrlMatchRangeLow_Type()
)
sleMlsQosClassMapCtrlMatchRangeLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapCtrlMatchRangeLow.setStatus("current")
_SleMlsQosClassMapCtrlMatchRangeHigh_Type = Integer32
_SleMlsQosClassMapCtrlMatchRangeHigh_Object = MibScalar
sleMlsQosClassMapCtrlMatchRangeHigh = _SleMlsQosClassMapCtrlMatchRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 11),
    _SleMlsQosClassMapCtrlMatchRangeHigh_Type()
)
sleMlsQosClassMapCtrlMatchRangeHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapCtrlMatchRangeHigh.setStatus("current")
_SleMlsQosClassMapCtrlMatchEtherType_Type = OctetString
_SleMlsQosClassMapCtrlMatchEtherType_Object = MibScalar
sleMlsQosClassMapCtrlMatchEtherType = _SleMlsQosClassMapCtrlMatchEtherType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 12),
    _SleMlsQosClassMapCtrlMatchEtherType_Type()
)
sleMlsQosClassMapCtrlMatchEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapCtrlMatchEtherType.setStatus("current")


class _SleMlsQosClassMapCtrlMatchSrcType_Type(Integer32):
    """Custom type sleMlsQosClassMapCtrlMatchSrcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("mac", 3))
    )


_SleMlsQosClassMapCtrlMatchSrcType_Type.__name__ = "Integer32"
_SleMlsQosClassMapCtrlMatchSrcType_Object = MibScalar
sleMlsQosClassMapCtrlMatchSrcType = _SleMlsQosClassMapCtrlMatchSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 13),
    _SleMlsQosClassMapCtrlMatchSrcType_Type()
)
sleMlsQosClassMapCtrlMatchSrcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapCtrlMatchSrcType.setStatus("current")
_SleMlsQosClassMapCtrlMatchSrcAddr_Type = OctetString
_SleMlsQosClassMapCtrlMatchSrcAddr_Object = MibScalar
sleMlsQosClassMapCtrlMatchSrcAddr = _SleMlsQosClassMapCtrlMatchSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 14),
    _SleMlsQosClassMapCtrlMatchSrcAddr_Type()
)
sleMlsQosClassMapCtrlMatchSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapCtrlMatchSrcAddr.setStatus("current")
_SleMlsQosClassMapCtrlMatchDstAddr_Type = OctetString
_SleMlsQosClassMapCtrlMatchDstAddr_Object = MibScalar
sleMlsQosClassMapCtrlMatchDstAddr = _SleMlsQosClassMapCtrlMatchDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 15),
    _SleMlsQosClassMapCtrlMatchDstAddr_Type()
)
sleMlsQosClassMapCtrlMatchDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapCtrlMatchDstAddr.setStatus("current")
_SleMlsQosClassMapCtrlMatchSrcIpMaskLen_Type = Integer32
_SleMlsQosClassMapCtrlMatchSrcIpMaskLen_Object = MibScalar
sleMlsQosClassMapCtrlMatchSrcIpMaskLen = _SleMlsQosClassMapCtrlMatchSrcIpMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 16),
    _SleMlsQosClassMapCtrlMatchSrcIpMaskLen_Type()
)
sleMlsQosClassMapCtrlMatchSrcIpMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapCtrlMatchSrcIpMaskLen.setStatus("current")
_SleMlsQosClassMapCtrlMatchDstIpMaskLen_Type = Integer32
_SleMlsQosClassMapCtrlMatchDstIpMaskLen_Object = MibScalar
sleMlsQosClassMapCtrlMatchDstIpMaskLen = _SleMlsQosClassMapCtrlMatchDstIpMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 17),
    _SleMlsQosClassMapCtrlMatchDstIpMaskLen_Type()
)
sleMlsQosClassMapCtrlMatchDstIpMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapCtrlMatchDstIpMaskLen.setStatus("current")
_SleMlsQosClassMapCtrlMatchSrcMacMask_Type = OctetString
_SleMlsQosClassMapCtrlMatchSrcMacMask_Object = MibScalar
sleMlsQosClassMapCtrlMatchSrcMacMask = _SleMlsQosClassMapCtrlMatchSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 18),
    _SleMlsQosClassMapCtrlMatchSrcMacMask_Type()
)
sleMlsQosClassMapCtrlMatchSrcMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapCtrlMatchSrcMacMask.setStatus("current")
_SleMlsQosClassMapCtrlMatchDstMacMask_Type = OctetString
_SleMlsQosClassMapCtrlMatchDstMacMask_Object = MibScalar
sleMlsQosClassMapCtrlMatchDstMacMask = _SleMlsQosClassMapCtrlMatchDstMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 19),
    _SleMlsQosClassMapCtrlMatchDstMacMask_Type()
)
sleMlsQosClassMapCtrlMatchDstMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapCtrlMatchDstMacMask.setStatus("current")
_SleMlsQosClassMapCtrlMatchAcessGroup_Type = OctetString
_SleMlsQosClassMapCtrlMatchAcessGroup_Object = MibScalar
sleMlsQosClassMapCtrlMatchAcessGroup = _SleMlsQosClassMapCtrlMatchAcessGroup_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 20),
    _SleMlsQosClassMapCtrlMatchAcessGroup_Type()
)
sleMlsQosClassMapCtrlMatchAcessGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapCtrlMatchAcessGroup.setStatus("current")
_SleMlsQosClassMapCtrlMatchVlanTpid_Type = OctetString
_SleMlsQosClassMapCtrlMatchVlanTpid_Object = MibScalar
sleMlsQosClassMapCtrlMatchVlanTpid = _SleMlsQosClassMapCtrlMatchVlanTpid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 21),
    _SleMlsQosClassMapCtrlMatchVlanTpid_Type()
)
sleMlsQosClassMapCtrlMatchVlanTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapCtrlMatchVlanTpid.setStatus("current")
_SleMlsQosClassMapCtrlMatchEgressInterface_Type = OctetString
_SleMlsQosClassMapCtrlMatchEgressInterface_Object = MibScalar
sleMlsQosClassMapCtrlMatchEgressInterface = _SleMlsQosClassMapCtrlMatchEgressInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 22),
    _SleMlsQosClassMapCtrlMatchEgressInterface_Type()
)
sleMlsQosClassMapCtrlMatchEgressInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosClassMapCtrlMatchEgressInterface.setStatus("current")


class _SleMplsQosClassMapCtrlMatchCriteria_Type(Integer32):
    """Custom type sleMplsQosClassMapCtrlMatchCriteria based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("matchAll", 1),
          ("matchAny", 2))
    )


_SleMplsQosClassMapCtrlMatchCriteria_Type.__name__ = "Integer32"
_SleMplsQosClassMapCtrlMatchCriteria_Object = MibScalar
sleMplsQosClassMapCtrlMatchCriteria = _SleMplsQosClassMapCtrlMatchCriteria_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 2, 23),
    _SleMplsQosClassMapCtrlMatchCriteria_Type()
)
sleMplsQosClassMapCtrlMatchCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsQosClassMapCtrlMatchCriteria.setStatus("current")
_SleMlsQosClassMapNotification_ObjectIdentity = ObjectIdentity
sleMlsQosClassMapNotification = _SleMlsQosClassMapNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 4, 3)
)
_SleMlsQosPolicyMap_ObjectIdentity = ObjectIdentity
sleMlsQosPolicyMap = _SleMlsQosPolicyMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5)
)
_SleMlsQosPolicyMapTable_Object = MibTable
sleMlsQosPolicyMapTable = _SleMlsQosPolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1)
)
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapTable.setStatus("current")
_SleMlsQosPolicyMapEntry_Object = MibTableRow
sleMlsQosPolicyMapEntry = _SleMlsQosPolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1)
)
sleMlsQosPolicyMapEntry.setIndexNames(
    (0, "SLE-MLSQOS-MIB", "sleMlsQosPmapName"),
    (0, "SLE-MLSQOS-MIB", "sleMlsQosPmapClassName"),
)
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapEntry.setStatus("current")
_SleMlsQosPmapName_Type = OctetString
_SleMlsQosPmapName_Object = MibTableColumn
sleMlsQosPmapName = _SleMlsQosPmapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 1),
    _SleMlsQosPmapName_Type()
)
sleMlsQosPmapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapName.setStatus("current")
_SleMlsQosPmapClassName_Type = OctetString
_SleMlsQosPmapClassName_Object = MibTableColumn
sleMlsQosPmapClassName = _SleMlsQosPmapClassName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 2),
    _SleMlsQosPmapClassName_Type()
)
sleMlsQosPmapClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassName.setStatus("current")
_SleMlsQosPmapClassMatchPriority_Type = PmapPriorityType
_SleMlsQosPmapClassMatchPriority_Object = MibTableColumn
sleMlsQosPmapClassMatchPriority = _SleMlsQosPmapClassMatchPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 3),
    _SleMlsQosPmapClassMatchPriority_Type()
)
sleMlsQosPmapClassMatchPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassMatchPriority.setStatus("current")


class _SleMlsQosPmapClassOperMode_Type(Integer32):
    """Custom type sleMlsQosPmapClassOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("allow", 1),
          ("deny", 2))
    )


_SleMlsQosPmapClassOperMode_Type.__name__ = "Integer32"
_SleMlsQosPmapClassOperMode_Object = MibTableColumn
sleMlsQosPmapClassOperMode = _SleMlsQosPmapClassOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 4),
    _SleMlsQosPmapClassOperMode_Type()
)
sleMlsQosPmapClassOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassOperMode.setStatus("current")
_SleMlsQosPmapClassPoliceType_Type = PmapPoliceType
_SleMlsQosPmapClassPoliceType_Object = MibTableColumn
sleMlsQosPmapClassPoliceType = _SleMlsQosPmapClassPoliceType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 5),
    _SleMlsQosPmapClassPoliceType_Type()
)
sleMlsQosPmapClassPoliceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassPoliceType.setStatus("current")
_SleMlsQosPmapClassPoliceCIR_Type = Integer32
_SleMlsQosPmapClassPoliceCIR_Object = MibTableColumn
sleMlsQosPmapClassPoliceCIR = _SleMlsQosPmapClassPoliceCIR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 6),
    _SleMlsQosPmapClassPoliceCIR_Type()
)
sleMlsQosPmapClassPoliceCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassPoliceCIR.setStatus("current")
_SleMlsQosPmapClassPolicePIR_Type = Integer32
_SleMlsQosPmapClassPolicePIR_Object = MibTableColumn
sleMlsQosPmapClassPolicePIR = _SleMlsQosPmapClassPolicePIR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 7),
    _SleMlsQosPmapClassPolicePIR_Type()
)
sleMlsQosPmapClassPolicePIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassPolicePIR.setStatus("current")
_SleMlsQosPmapClassPoliceCBS_Type = Integer32
_SleMlsQosPmapClassPoliceCBS_Object = MibTableColumn
sleMlsQosPmapClassPoliceCBS = _SleMlsQosPmapClassPoliceCBS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 8),
    _SleMlsQosPmapClassPoliceCBS_Type()
)
sleMlsQosPmapClassPoliceCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassPoliceCBS.setStatus("current")
_SleMlsQosPmapClassPoliceEBS_Type = Integer32
_SleMlsQosPmapClassPoliceEBS_Object = MibTableColumn
sleMlsQosPmapClassPoliceEBS = _SleMlsQosPmapClassPoliceEBS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 9),
    _SleMlsQosPmapClassPoliceEBS_Type()
)
sleMlsQosPmapClassPoliceEBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassPoliceEBS.setStatus("current")
_SleMlsQosPmapClassPoliceExdAction_Type = PmapExceedActionType
_SleMlsQosPmapClassPoliceExdAction_Object = MibTableColumn
sleMlsQosPmapClassPoliceExdAction = _SleMlsQosPmapClassPoliceExdAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 10),
    _SleMlsQosPmapClassPoliceExdAction_Type()
)
sleMlsQosPmapClassPoliceExdAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassPoliceExdAction.setStatus("current")
_SleMlsQosPmapClassPoliceExdActionCos_Type = Integer32
_SleMlsQosPmapClassPoliceExdActionCos_Object = MibTableColumn
sleMlsQosPmapClassPoliceExdActionCos = _SleMlsQosPmapClassPoliceExdActionCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 11),
    _SleMlsQosPmapClassPoliceExdActionCos_Type()
)
sleMlsQosPmapClassPoliceExdActionCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassPoliceExdActionCos.setStatus("current")
_SleMlsQosPmapClassPoliceExdActionDscp_Type = Integer32
_SleMlsQosPmapClassPoliceExdActionDscp_Object = MibTableColumn
sleMlsQosPmapClassPoliceExdActionDscp = _SleMlsQosPmapClassPoliceExdActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 12),
    _SleMlsQosPmapClassPoliceExdActionDscp_Type()
)
sleMlsQosPmapClassPoliceExdActionDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassPoliceExdActionDscp.setStatus("current")
_SleMlsQosPmapClassPoliceExdActionTos_Type = Integer32
_SleMlsQosPmapClassPoliceExdActionTos_Object = MibTableColumn
sleMlsQosPmapClassPoliceExdActionTos = _SleMlsQosPmapClassPoliceExdActionTos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 13),
    _SleMlsQosPmapClassPoliceExdActionTos_Type()
)
sleMlsQosPmapClassPoliceExdActionTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassPoliceExdActionTos.setStatus("current")
_SleMlsQosPmapClassPoliceExdActionViolateAction_Type = PmapViolateActionType
_SleMlsQosPmapClassPoliceExdActionViolateAction_Object = MibTableColumn
sleMlsQosPmapClassPoliceExdActionViolateAction = _SleMlsQosPmapClassPoliceExdActionViolateAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 14),
    _SleMlsQosPmapClassPoliceExdActionViolateAction_Type()
)
sleMlsQosPmapClassPoliceExdActionViolateAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassPoliceExdActionViolateAction.setStatus("current")
_SleMlsQosPmapClassPoliceExdActionViolateValue_Type = Integer32
_SleMlsQosPmapClassPoliceExdActionViolateValue_Object = MibTableColumn
sleMlsQosPmapClassPoliceExdActionViolateValue = _SleMlsQosPmapClassPoliceExdActionViolateValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 15),
    _SleMlsQosPmapClassPoliceExdActionViolateValue_Type()
)
sleMlsQosPmapClassPoliceExdActionViolateValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassPoliceExdActionViolateValue.setStatus("current")
_SleMlsQosPmapClassPoliceAggregateName_Type = OctetString
_SleMlsQosPmapClassPoliceAggregateName_Object = MibTableColumn
sleMlsQosPmapClassPoliceAggregateName = _SleMlsQosPmapClassPoliceAggregateName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 16),
    _SleMlsQosPmapClassPoliceAggregateName_Type()
)
sleMlsQosPmapClassPoliceAggregateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassPoliceAggregateName.setStatus("current")
_SleMlsQosPmapClassSetActionDeny_Type = Integer32
_SleMlsQosPmapClassSetActionDeny_Object = MibTableColumn
sleMlsQosPmapClassSetActionDeny = _SleMlsQosPmapClassSetActionDeny_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 17),
    _SleMlsQosPmapClassSetActionDeny_Type()
)
sleMlsQosPmapClassSetActionDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassSetActionDeny.setStatus("current")
_SleMlsQosPmapClassSetActionCos_Type = Integer32
_SleMlsQosPmapClassSetActionCos_Object = MibTableColumn
sleMlsQosPmapClassSetActionCos = _SleMlsQosPmapClassSetActionCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 18),
    _SleMlsQosPmapClassSetActionCos_Type()
)
sleMlsQosPmapClassSetActionCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassSetActionCos.setStatus("current")
_SleMlsQosPmapClassSetActionCpuCos_Type = Integer32
_SleMlsQosPmapClassSetActionCpuCos_Object = MibTableColumn
sleMlsQosPmapClassSetActionCpuCos = _SleMlsQosPmapClassSetActionCpuCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 19),
    _SleMlsQosPmapClassSetActionCpuCos_Type()
)
sleMlsQosPmapClassSetActionCpuCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassSetActionCpuCos.setStatus("current")
_SleMlsQosPmapClassSetActionIpDscp_Type = Integer32
_SleMlsQosPmapClassSetActionIpDscp_Object = MibTableColumn
sleMlsQosPmapClassSetActionIpDscp = _SleMlsQosPmapClassSetActionIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 20),
    _SleMlsQosPmapClassSetActionIpDscp_Type()
)
sleMlsQosPmapClassSetActionIpDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassSetActionIpDscp.setStatus("current")
_SleMlsQosPmapClassSetActionIp6Dscp_Type = Integer32
_SleMlsQosPmapClassSetActionIp6Dscp_Object = MibTableColumn
sleMlsQosPmapClassSetActionIp6Dscp = _SleMlsQosPmapClassSetActionIp6Dscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 21),
    _SleMlsQosPmapClassSetActionIp6Dscp_Type()
)
sleMlsQosPmapClassSetActionIp6Dscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassSetActionIp6Dscp.setStatus("current")
_SleMlsQosPmapClassSetActionIpPrecedence_Type = Integer32
_SleMlsQosPmapClassSetActionIpPrecedence_Object = MibTableColumn
sleMlsQosPmapClassSetActionIpPrecedence = _SleMlsQosPmapClassSetActionIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 22),
    _SleMlsQosPmapClassSetActionIpPrecedence_Type()
)
sleMlsQosPmapClassSetActionIpPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassSetActionIpPrecedence.setStatus("current")
_SleMlsQosPmapClassSetActionIp6Precedence_Type = Integer32
_SleMlsQosPmapClassSetActionIp6Precedence_Object = MibTableColumn
sleMlsQosPmapClassSetActionIp6Precedence = _SleMlsQosPmapClassSetActionIp6Precedence_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 23),
    _SleMlsQosPmapClassSetActionIp6Precedence_Type()
)
sleMlsQosPmapClassSetActionIp6Precedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassSetActionIp6Precedence.setStatus("current")
_SleMlsQosPmapClassSetActionMirrorToPortVal_Type = OctetString
_SleMlsQosPmapClassSetActionMirrorToPortVal_Object = MibTableColumn
sleMlsQosPmapClassSetActionMirrorToPortVal = _SleMlsQosPmapClassSetActionMirrorToPortVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 24),
    _SleMlsQosPmapClassSetActionMirrorToPortVal_Type()
)
sleMlsQosPmapClassSetActionMirrorToPortVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassSetActionMirrorToPortVal.setStatus("current")
_SleMlsQosPmapClassSetActionRedirectToPortVal_Type = OctetString
_SleMlsQosPmapClassSetActionRedirectToPortVal_Object = MibTableColumn
sleMlsQosPmapClassSetActionRedirectToPortVal = _SleMlsQosPmapClassSetActionRedirectToPortVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 25),
    _SleMlsQosPmapClassSetActionRedirectToPortVal_Type()
)
sleMlsQosPmapClassSetActionRedirectToPortVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassSetActionRedirectToPortVal.setStatus("current")
_SleMlsQosPmapClassSetActionVlanId_Type = Integer32
_SleMlsQosPmapClassSetActionVlanId_Object = MibTableColumn
sleMlsQosPmapClassSetActionVlanId = _SleMlsQosPmapClassSetActionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 26),
    _SleMlsQosPmapClassSetActionVlanId_Type()
)
sleMlsQosPmapClassSetActionVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassSetActionVlanId.setStatus("current")
_SleMlsQosPmapClassSetActionVlanCos_Type = Integer32
_SleMlsQosPmapClassSetActionVlanCos_Object = MibTableColumn
sleMlsQosPmapClassSetActionVlanCos = _SleMlsQosPmapClassSetActionVlanCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 27),
    _SleMlsQosPmapClassSetActionVlanCos_Type()
)
sleMlsQosPmapClassSetActionVlanCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassSetActionVlanCos.setStatus("current")
_SleMlsQosPmapClassSetActionQosGroup_Type = Integer32
_SleMlsQosPmapClassSetActionQosGroup_Object = MibTableColumn
sleMlsQosPmapClassSetActionQosGroup = _SleMlsQosPmapClassSetActionQosGroup_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 28),
    _SleMlsQosPmapClassSetActionQosGroup_Type()
)
sleMlsQosPmapClassSetActionQosGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPmapClassSetActionQosGroup.setStatus("current")


class _SleMplsQosPmapClassSetActionQueue_Type(Integer32):
    """Custom type sleMplsQosPmapClassSetActionQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleMplsQosPmapClassSetActionQueue_Type.__name__ = "Integer32"
_SleMplsQosPmapClassSetActionQueue_Object = MibTableColumn
sleMplsQosPmapClassSetActionQueue = _SleMplsQosPmapClassSetActionQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 29),
    _SleMplsQosPmapClassSetActionQueue_Type()
)
sleMplsQosPmapClassSetActionQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsQosPmapClassSetActionQueue.setStatus("current")
_SleMplsQosPmapClassSetActionCopyCpu_Type = Integer32
_SleMplsQosPmapClassSetActionCopyCpu_Object = MibTableColumn
sleMplsQosPmapClassSetActionCopyCpu = _SleMplsQosPmapClassSetActionCopyCpu_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 1, 1, 30),
    _SleMplsQosPmapClassSetActionCopyCpu_Type()
)
sleMplsQosPmapClassSetActionCopyCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsQosPmapClassSetActionCopyCpu.setStatus("current")
_SleMlsQosPolicyMapControl_ObjectIdentity = ObjectIdentity
sleMlsQosPolicyMapControl = _SleMlsQosPolicyMapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2)
)


class _SleMlsQosPolicyMapControlRequest_Type(Integer32):
    """Custom type sleMlsQosPolicyMapControlRequest based on Integer32"""
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
        *(("createPolicyMapClass", 1),
          ("deletePolicyMapClass", 2),
          ("setPolicyMapClassMatchPriority", 3),
          ("setPolicyMapClassOperMode", 4),
          ("unSetPolicyMapClassOperMode", 5),
          ("setPolicyMapClassPolicer", 6),
          ("unSetPolicyMapClassPolicer", 7),
          ("setPolicyMapClassPolicerAggregate", 8),
          ("unSetPolicyMapClassPolicerAggregate", 9),
          ("setPolicyMapClassSet", 10),
          ("unSetPolicyMapClassSet", 11),
          ("deletePolicyMap", 12))
    )


_SleMlsQosPolicyMapControlRequest_Type.__name__ = "Integer32"
_SleMlsQosPolicyMapControlRequest_Object = MibScalar
sleMlsQosPolicyMapControlRequest = _SleMlsQosPolicyMapControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 1),
    _SleMlsQosPolicyMapControlRequest_Type()
)
sleMlsQosPolicyMapControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapControlRequest.setStatus("current")
_SleMlsQosPolicyMapControlStatus_Type = SleControlStatusType
_SleMlsQosPolicyMapControlStatus_Object = MibScalar
sleMlsQosPolicyMapControlStatus = _SleMlsQosPolicyMapControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 2),
    _SleMlsQosPolicyMapControlStatus_Type()
)
sleMlsQosPolicyMapControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapControlStatus.setStatus("current")
_SleMlsQosPolicyMapControlTimer_Type = Gauge32
_SleMlsQosPolicyMapControlTimer_Object = MibScalar
sleMlsQosPolicyMapControlTimer = _SleMlsQosPolicyMapControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 3),
    _SleMlsQosPolicyMapControlTimer_Type()
)
sleMlsQosPolicyMapControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapControlTimer.setStatus("current")
_SleMlsQosPolicyMapontrolTimeStamp_Type = TimeTicks
_SleMlsQosPolicyMapontrolTimeStamp_Object = MibScalar
sleMlsQosPolicyMapontrolTimeStamp = _SleMlsQosPolicyMapontrolTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 4),
    _SleMlsQosPolicyMapontrolTimeStamp_Type()
)
sleMlsQosPolicyMapontrolTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapontrolTimeStamp.setStatus("current")
_SleMlsQosPolicyMapControlReqResult_Type = SleControlRequestResultType
_SleMlsQosPolicyMapControlReqResult_Object = MibScalar
sleMlsQosPolicyMapControlReqResult = _SleMlsQosPolicyMapControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 5),
    _SleMlsQosPolicyMapControlReqResult_Type()
)
sleMlsQosPolicyMapControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapControlReqResult.setStatus("current")
_SleMlsQosPolicyMapCtrlName_Type = OctetString
_SleMlsQosPolicyMapCtrlName_Object = MibScalar
sleMlsQosPolicyMapCtrlName = _SleMlsQosPolicyMapCtrlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 6),
    _SleMlsQosPolicyMapCtrlName_Type()
)
sleMlsQosPolicyMapCtrlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlName.setStatus("current")
_SleMlsQosPolicyMapCtrlClassName_Type = OctetString
_SleMlsQosPolicyMapCtrlClassName_Object = MibScalar
sleMlsQosPolicyMapCtrlClassName = _SleMlsQosPolicyMapCtrlClassName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 7),
    _SleMlsQosPolicyMapCtrlClassName_Type()
)
sleMlsQosPolicyMapCtrlClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassName.setStatus("current")
_SleMlsQosPolicyMapCtrlClassMatchPriority_Type = PmapPriorityType
_SleMlsQosPolicyMapCtrlClassMatchPriority_Object = MibScalar
sleMlsQosPolicyMapCtrlClassMatchPriority = _SleMlsQosPolicyMapCtrlClassMatchPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 8),
    _SleMlsQosPolicyMapCtrlClassMatchPriority_Type()
)
sleMlsQosPolicyMapCtrlClassMatchPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassMatchPriority.setStatus("current")


class _SleMlsQosPolicyMapCtrlClassOperMode_Type(Integer32):
    """Custom type sleMlsQosPolicyMapCtrlClassOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("allow", 1),
          ("deny", 2))
    )


_SleMlsQosPolicyMapCtrlClassOperMode_Type.__name__ = "Integer32"
_SleMlsQosPolicyMapCtrlClassOperMode_Object = MibScalar
sleMlsQosPolicyMapCtrlClassOperMode = _SleMlsQosPolicyMapCtrlClassOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 9),
    _SleMlsQosPolicyMapCtrlClassOperMode_Type()
)
sleMlsQosPolicyMapCtrlClassOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassOperMode.setStatus("current")
_SleMlsQosPolicyMapCtrlClassPoliceType_Type = PmapPoliceType
_SleMlsQosPolicyMapCtrlClassPoliceType_Object = MibScalar
sleMlsQosPolicyMapCtrlClassPoliceType = _SleMlsQosPolicyMapCtrlClassPoliceType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 10),
    _SleMlsQosPolicyMapCtrlClassPoliceType_Type()
)
sleMlsQosPolicyMapCtrlClassPoliceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassPoliceType.setStatus("current")
_SleMlsQosPolicyMapCtrlClassPoliceCIR_Type = Integer32
_SleMlsQosPolicyMapCtrlClassPoliceCIR_Object = MibScalar
sleMlsQosPolicyMapCtrlClassPoliceCIR = _SleMlsQosPolicyMapCtrlClassPoliceCIR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 11),
    _SleMlsQosPolicyMapCtrlClassPoliceCIR_Type()
)
sleMlsQosPolicyMapCtrlClassPoliceCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassPoliceCIR.setStatus("current")
_SleMlsQosPolicyMapCtrlClassPolicePIR_Type = Integer32
_SleMlsQosPolicyMapCtrlClassPolicePIR_Object = MibScalar
sleMlsQosPolicyMapCtrlClassPolicePIR = _SleMlsQosPolicyMapCtrlClassPolicePIR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 12),
    _SleMlsQosPolicyMapCtrlClassPolicePIR_Type()
)
sleMlsQosPolicyMapCtrlClassPolicePIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassPolicePIR.setStatus("current")
_SleMlsQosPolicyMapCtrlClassPoliceCBS_Type = Integer32
_SleMlsQosPolicyMapCtrlClassPoliceCBS_Object = MibScalar
sleMlsQosPolicyMapCtrlClassPoliceCBS = _SleMlsQosPolicyMapCtrlClassPoliceCBS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 13),
    _SleMlsQosPolicyMapCtrlClassPoliceCBS_Type()
)
sleMlsQosPolicyMapCtrlClassPoliceCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassPoliceCBS.setStatus("current")
_SleMlsQosPolicyMapCtrlClassPoliceEBS_Type = Integer32
_SleMlsQosPolicyMapCtrlClassPoliceEBS_Object = MibScalar
sleMlsQosPolicyMapCtrlClassPoliceEBS = _SleMlsQosPolicyMapCtrlClassPoliceEBS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 14),
    _SleMlsQosPolicyMapCtrlClassPoliceEBS_Type()
)
sleMlsQosPolicyMapCtrlClassPoliceEBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassPoliceEBS.setStatus("current")
_SleMlsQosPolicyMapCtrlClassPoliceExdAction_Type = PmapExceedActionType
_SleMlsQosPolicyMapCtrlClassPoliceExdAction_Object = MibScalar
sleMlsQosPolicyMapCtrlClassPoliceExdAction = _SleMlsQosPolicyMapCtrlClassPoliceExdAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 15),
    _SleMlsQosPolicyMapCtrlClassPoliceExdAction_Type()
)
sleMlsQosPolicyMapCtrlClassPoliceExdAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassPoliceExdAction.setStatus("current")
_SleMlsQosPolicyMapCtrlClassPoliceExdActionCos_Type = Integer32
_SleMlsQosPolicyMapCtrlClassPoliceExdActionCos_Object = MibScalar
sleMlsQosPolicyMapCtrlClassPoliceExdActionCos = _SleMlsQosPolicyMapCtrlClassPoliceExdActionCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 16),
    _SleMlsQosPolicyMapCtrlClassPoliceExdActionCos_Type()
)
sleMlsQosPolicyMapCtrlClassPoliceExdActionCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassPoliceExdActionCos.setStatus("current")
_SleMlsQosPolicyMapCtrlClassPoliceExdActionDscp_Type = Integer32
_SleMlsQosPolicyMapCtrlClassPoliceExdActionDscp_Object = MibScalar
sleMlsQosPolicyMapCtrlClassPoliceExdActionDscp = _SleMlsQosPolicyMapCtrlClassPoliceExdActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 17),
    _SleMlsQosPolicyMapCtrlClassPoliceExdActionDscp_Type()
)
sleMlsQosPolicyMapCtrlClassPoliceExdActionDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassPoliceExdActionDscp.setStatus("current")
_SleMlsQosPolicyMapCtrlClassPoliceExdActionTos_Type = Integer32
_SleMlsQosPolicyMapCtrlClassPoliceExdActionTos_Object = MibScalar
sleMlsQosPolicyMapCtrlClassPoliceExdActionTos = _SleMlsQosPolicyMapCtrlClassPoliceExdActionTos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 18),
    _SleMlsQosPolicyMapCtrlClassPoliceExdActionTos_Type()
)
sleMlsQosPolicyMapCtrlClassPoliceExdActionTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassPoliceExdActionTos.setStatus("current")
_SleMlsQosPolicyMapCtrlClassPoliceExdActionViolateAction_Type = PmapViolateActionType
_SleMlsQosPolicyMapCtrlClassPoliceExdActionViolateAction_Object = MibScalar
sleMlsQosPolicyMapCtrlClassPoliceExdActionViolateAction = _SleMlsQosPolicyMapCtrlClassPoliceExdActionViolateAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 19),
    _SleMlsQosPolicyMapCtrlClassPoliceExdActionViolateAction_Type()
)
sleMlsQosPolicyMapCtrlClassPoliceExdActionViolateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassPoliceExdActionViolateAction.setStatus("current")
_SleMlsQosPolicyMapCtrlClassPoliceExdActionViolateValue_Type = Integer32
_SleMlsQosPolicyMapCtrlClassPoliceExdActionViolateValue_Object = MibScalar
sleMlsQosPolicyMapCtrlClassPoliceExdActionViolateValue = _SleMlsQosPolicyMapCtrlClassPoliceExdActionViolateValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 20),
    _SleMlsQosPolicyMapCtrlClassPoliceExdActionViolateValue_Type()
)
sleMlsQosPolicyMapCtrlClassPoliceExdActionViolateValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassPoliceExdActionViolateValue.setStatus("current")
_SleMlsQosPolicyMapCtrlClassPoliceAggregateName_Type = OctetString
_SleMlsQosPolicyMapCtrlClassPoliceAggregateName_Object = MibScalar
sleMlsQosPolicyMapCtrlClassPoliceAggregateName = _SleMlsQosPolicyMapCtrlClassPoliceAggregateName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 21),
    _SleMlsQosPolicyMapCtrlClassPoliceAggregateName_Type()
)
sleMlsQosPolicyMapCtrlClassPoliceAggregateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassPoliceAggregateName.setStatus("current")
_SleMlsQosPolicyMapCtrlClassSetAction_Type = PmapSetActionType
_SleMlsQosPolicyMapCtrlClassSetAction_Object = MibScalar
sleMlsQosPolicyMapCtrlClassSetAction = _SleMlsQosPolicyMapCtrlClassSetAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 22),
    _SleMlsQosPolicyMapCtrlClassSetAction_Type()
)
sleMlsQosPolicyMapCtrlClassSetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassSetAction.setStatus("current")
_SleMlsQosPolicyMapCtrlClassSetActionCos_Type = Integer32
_SleMlsQosPolicyMapCtrlClassSetActionCos_Object = MibScalar
sleMlsQosPolicyMapCtrlClassSetActionCos = _SleMlsQosPolicyMapCtrlClassSetActionCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 23),
    _SleMlsQosPolicyMapCtrlClassSetActionCos_Type()
)
sleMlsQosPolicyMapCtrlClassSetActionCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassSetActionCos.setStatus("current")
_SleMlsQosPolicyMapCtrlClassSetActionCpuCos_Type = Integer32
_SleMlsQosPolicyMapCtrlClassSetActionCpuCos_Object = MibScalar
sleMlsQosPolicyMapCtrlClassSetActionCpuCos = _SleMlsQosPolicyMapCtrlClassSetActionCpuCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 24),
    _SleMlsQosPolicyMapCtrlClassSetActionCpuCos_Type()
)
sleMlsQosPolicyMapCtrlClassSetActionCpuCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassSetActionCpuCos.setStatus("current")
_SleMlsQosPolicyMapCtrlClassSetActionIpDscp_Type = Integer32
_SleMlsQosPolicyMapCtrlClassSetActionIpDscp_Object = MibScalar
sleMlsQosPolicyMapCtrlClassSetActionIpDscp = _SleMlsQosPolicyMapCtrlClassSetActionIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 25),
    _SleMlsQosPolicyMapCtrlClassSetActionIpDscp_Type()
)
sleMlsQosPolicyMapCtrlClassSetActionIpDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassSetActionIpDscp.setStatus("current")
_SleMlsQosPolicyMapCtrlClassSetActionIp6Dscp_Type = Integer32
_SleMlsQosPolicyMapCtrlClassSetActionIp6Dscp_Object = MibScalar
sleMlsQosPolicyMapCtrlClassSetActionIp6Dscp = _SleMlsQosPolicyMapCtrlClassSetActionIp6Dscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 26),
    _SleMlsQosPolicyMapCtrlClassSetActionIp6Dscp_Type()
)
sleMlsQosPolicyMapCtrlClassSetActionIp6Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassSetActionIp6Dscp.setStatus("current")
_SleMlsQosPolicyMapCtrlClassSetActionIpPrecedence_Type = Integer32
_SleMlsQosPolicyMapCtrlClassSetActionIpPrecedence_Object = MibScalar
sleMlsQosPolicyMapCtrlClassSetActionIpPrecedence = _SleMlsQosPolicyMapCtrlClassSetActionIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 27),
    _SleMlsQosPolicyMapCtrlClassSetActionIpPrecedence_Type()
)
sleMlsQosPolicyMapCtrlClassSetActionIpPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassSetActionIpPrecedence.setStatus("current")
_SleMlsQosPolicyMapCtrlClassSetActionIp6Precedence_Type = Integer32
_SleMlsQosPolicyMapCtrlClassSetActionIp6Precedence_Object = MibScalar
sleMlsQosPolicyMapCtrlClassSetActionIp6Precedence = _SleMlsQosPolicyMapCtrlClassSetActionIp6Precedence_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 28),
    _SleMlsQosPolicyMapCtrlClassSetActionIp6Precedence_Type()
)
sleMlsQosPolicyMapCtrlClassSetActionIp6Precedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassSetActionIp6Precedence.setStatus("current")
_SleMlsQosPolicyMapCtrlClassSetActionMirrorToPort_Type = OctetString
_SleMlsQosPolicyMapCtrlClassSetActionMirrorToPort_Object = MibScalar
sleMlsQosPolicyMapCtrlClassSetActionMirrorToPort = _SleMlsQosPolicyMapCtrlClassSetActionMirrorToPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 29),
    _SleMlsQosPolicyMapCtrlClassSetActionMirrorToPort_Type()
)
sleMlsQosPolicyMapCtrlClassSetActionMirrorToPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassSetActionMirrorToPort.setStatus("current")
_SleMlsQosPolicyMapCtrlClassSetActionRedirectToPort_Type = OctetString
_SleMlsQosPolicyMapCtrlClassSetActionRedirectToPort_Object = MibScalar
sleMlsQosPolicyMapCtrlClassSetActionRedirectToPort = _SleMlsQosPolicyMapCtrlClassSetActionRedirectToPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 30),
    _SleMlsQosPolicyMapCtrlClassSetActionRedirectToPort_Type()
)
sleMlsQosPolicyMapCtrlClassSetActionRedirectToPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassSetActionRedirectToPort.setStatus("current")
_SleMlsQosPolicyMapCtrlClassSetActionVlanId_Type = Integer32
_SleMlsQosPolicyMapCtrlClassSetActionVlanId_Object = MibScalar
sleMlsQosPolicyMapCtrlClassSetActionVlanId = _SleMlsQosPolicyMapCtrlClassSetActionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 31),
    _SleMlsQosPolicyMapCtrlClassSetActionVlanId_Type()
)
sleMlsQosPolicyMapCtrlClassSetActionVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassSetActionVlanId.setStatus("current")
_SleMlsQosPolicyMapCtrlClassSetActionVlanCos_Type = Integer32
_SleMlsQosPolicyMapCtrlClassSetActionVlanCos_Object = MibScalar
sleMlsQosPolicyMapCtrlClassSetActionVlanCos = _SleMlsQosPolicyMapCtrlClassSetActionVlanCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 32),
    _SleMlsQosPolicyMapCtrlClassSetActionVlanCos_Type()
)
sleMlsQosPolicyMapCtrlClassSetActionVlanCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassSetActionVlanCos.setStatus("current")
_SleMlsQosPolicyMapCtrlClassSetActionQosGroup_Type = Integer32
_SleMlsQosPolicyMapCtrlClassSetActionQosGroup_Object = MibScalar
sleMlsQosPolicyMapCtrlClassSetActionQosGroup = _SleMlsQosPolicyMapCtrlClassSetActionQosGroup_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 33),
    _SleMlsQosPolicyMapCtrlClassSetActionQosGroup_Type()
)
sleMlsQosPolicyMapCtrlClassSetActionQosGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassSetActionQosGroup.setStatus("current")


class _SleMlsQosPolicyMapCtrlClassSetActionQueue_Type(Integer32):
    """Custom type sleMlsQosPolicyMapCtrlClassSetActionQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleMlsQosPolicyMapCtrlClassSetActionQueue_Type.__name__ = "Integer32"
_SleMlsQosPolicyMapCtrlClassSetActionQueue_Object = MibScalar
sleMlsQosPolicyMapCtrlClassSetActionQueue = _SleMlsQosPolicyMapCtrlClassSetActionQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 5, 2, 34),
    _SleMlsQosPolicyMapCtrlClassSetActionQueue_Type()
)
sleMlsQosPolicyMapCtrlClassSetActionQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosPolicyMapCtrlClassSetActionQueue.setStatus("current")
_SleMlsQosInterface_ObjectIdentity = ObjectIdentity
sleMlsQosInterface = _SleMlsQosInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6)
)
_SleMlsQosInterfaceTable_Object = MibTable
sleMlsQosInterfaceTable = _SleMlsQosInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1)
)
if mibBuilder.loadTexts:
    sleMlsQosInterfaceTable.setStatus("current")
_SleMlsQosInterfaceEntry_Object = MibTableRow
sleMlsQosInterfaceEntry = _SleMlsQosInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1)
)
sleMlsQosInterfaceEntry.setIndexNames(
    (0, "SLE-MLSQOS-MIB", "sleMlsQosInterfaceIndex"),
)
if mibBuilder.loadTexts:
    sleMlsQosInterfaceEntry.setStatus("current")


class _SleMlsQosInterfaceIndex_Type(Integer32):
    """Custom type sleMlsQosInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SleMlsQosInterfaceIndex_Type.__name__ = "Integer32"
_SleMlsQosInterfaceIndex_Object = MibTableColumn
sleMlsQosInterfaceIndex = _SleMlsQosInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 1),
    _SleMlsQosInterfaceIndex_Type()
)
sleMlsQosInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceIndex.setStatus("current")
_SleMlsQosInterfaceName_Type = OctetString
_SleMlsQosInterfaceName_Object = MibTableColumn
sleMlsQosInterfaceName = _SleMlsQosInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 2),
    _SleMlsQosInterfaceName_Type()
)
sleMlsQosInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceName.setStatus("current")
_SleMlsQosInterfaceTrustState_Type = MlsQosIntfTrustState
_SleMlsQosInterfaceTrustState_Object = MibTableColumn
sleMlsQosInterfaceTrustState = _SleMlsQosInterfaceTrustState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 3),
    _SleMlsQosInterfaceTrustState_Type()
)
sleMlsQosInterfaceTrustState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceTrustState.setStatus("current")
_SleMlsQosInterfaceCos_Type = Integer32
_SleMlsQosInterfaceCos_Object = MibTableColumn
sleMlsQosInterfaceCos = _SleMlsQosInterfaceCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 4),
    _SleMlsQosInterfaceCos_Type()
)
sleMlsQosInterfaceCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceCos.setStatus("current")
_SleMlsQosInterfaceCosOverride_Type = Integer32
_SleMlsQosInterfaceCosOverride_Object = MibTableColumn
sleMlsQosInterfaceCosOverride = _SleMlsQosInterfaceCosOverride_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 5),
    _SleMlsQosInterfaceCosOverride_Type()
)
sleMlsQosInterfaceCosOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceCosOverride.setStatus("current")
_SleMlsQosInterfaceCosToCos_Type = OctetString
_SleMlsQosInterfaceCosToCos_Object = MibTableColumn
sleMlsQosInterfaceCosToCos = _SleMlsQosInterfaceCosToCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 6),
    _SleMlsQosInterfaceCosToCos_Type()
)
sleMlsQosInterfaceCosToCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceCosToCos.setStatus("current")
_SleMlsQosInterfaceCosToQueue_Type = OctetString
_SleMlsQosInterfaceCosToQueue_Object = MibTableColumn
sleMlsQosInterfaceCosToQueue = _SleMlsQosInterfaceCosToQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 7),
    _SleMlsQosInterfaceCosToQueue_Type()
)
sleMlsQosInterfaceCosToQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceCosToQueue.setStatus("current")
_SleMlsQosInterfaceDscp_Type = Integer32
_SleMlsQosInterfaceDscp_Object = MibTableColumn
sleMlsQosInterfaceDscp = _SleMlsQosInterfaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 8),
    _SleMlsQosInterfaceDscp_Type()
)
sleMlsQosInterfaceDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceDscp.setStatus("current")
_SleMlsQosInterfaceDscpToDscp_Type = OctetString
_SleMlsQosInterfaceDscpToDscp_Object = MibTableColumn
sleMlsQosInterfaceDscpToDscp = _SleMlsQosInterfaceDscpToDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 9),
    _SleMlsQosInterfaceDscpToDscp_Type()
)
sleMlsQosInterfaceDscpToDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceDscpToDscp.setStatus("current")
_SleMlsQosInterfaceDscpToQueue_Type = OctetString
_SleMlsQosInterfaceDscpToQueue_Object = MibTableColumn
sleMlsQosInterfaceDscpToQueue = _SleMlsQosInterfaceDscpToQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 10),
    _SleMlsQosInterfaceDscpToQueue_Type()
)
sleMlsQosInterfaceDscpToQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceDscpToQueue.setStatus("current")
_SleMlsQosInterfaceExpToExp_Type = OctetString
_SleMlsQosInterfaceExpToExp_Object = MibTableColumn
sleMlsQosInterfaceExpToExp = _SleMlsQosInterfaceExpToExp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 11),
    _SleMlsQosInterfaceExpToExp_Type()
)
sleMlsQosInterfaceExpToExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceExpToExp.setStatus("current")
_SleMlsQosInterfaceTrafficShapeRate_Type = Integer32
_SleMlsQosInterfaceTrafficShapeRate_Object = MibTableColumn
sleMlsQosInterfaceTrafficShapeRate = _SleMlsQosInterfaceTrafficShapeRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 12),
    _SleMlsQosInterfaceTrafficShapeRate_Type()
)
sleMlsQosInterfaceTrafficShapeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceTrafficShapeRate.setStatus("current")
_SleMlsQosInterfaceTrafficShapeBurst_Type = Integer32
_SleMlsQosInterfaceTrafficShapeBurst_Object = MibTableColumn
sleMlsQosInterfaceTrafficShapeBurst = _SleMlsQosInterfaceTrafficShapeBurst_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 13),
    _SleMlsQosInterfaceTrafficShapeBurst_Type()
)
sleMlsQosInterfaceTrafficShapeBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceTrafficShapeBurst.setStatus("current")
_SleMlsQosInterfaceInputPolicyMap_Type = OctetString
_SleMlsQosInterfaceInputPolicyMap_Object = MibTableColumn
sleMlsQosInterfaceInputPolicyMap = _SleMlsQosInterfaceInputPolicyMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 14),
    _SleMlsQosInterfaceInputPolicyMap_Type()
)
sleMlsQosInterfaceInputPolicyMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceInputPolicyMap.setStatus("current")
_SleMlsQosInterfaceOutputPolicyMap_Type = OctetString
_SleMlsQosInterfaceOutputPolicyMap_Object = MibTableColumn
sleMlsQosInterfaceOutputPolicyMap = _SleMlsQosInterfaceOutputPolicyMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 15),
    _SleMlsQosInterfaceOutputPolicyMap_Type()
)
sleMlsQosInterfaceOutputPolicyMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceOutputPolicyMap.setStatus("current")
_SleMlsQosInterfaceTrustPassthroughCos_Type = Integer32
_SleMlsQosInterfaceTrustPassthroughCos_Object = MibTableColumn
sleMlsQosInterfaceTrustPassthroughCos = _SleMlsQosInterfaceTrustPassthroughCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 16),
    _SleMlsQosInterfaceTrustPassthroughCos_Type()
)
sleMlsQosInterfaceTrustPassthroughCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceTrustPassthroughCos.setStatus("current")
_SleMlsQosInterfaceTrustPassthroughDscp_Type = Integer32
_SleMlsQosInterfaceTrustPassthroughDscp_Object = MibTableColumn
sleMlsQosInterfaceTrustPassthroughDscp = _SleMlsQosInterfaceTrustPassthroughDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 17),
    _SleMlsQosInterfaceTrustPassthroughDscp_Type()
)
sleMlsQosInterfaceTrustPassthroughDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceTrustPassthroughDscp.setStatus("current")
_SleHQosInterfaceCosToClass_Type = OctetString
_SleHQosInterfaceCosToClass_Object = MibTableColumn
sleHQosInterfaceCosToClass = _SleHQosInterfaceCosToClass_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 18),
    _SleHQosInterfaceCosToClass_Type()
)
sleHQosInterfaceCosToClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHQosInterfaceCosToClass.setStatus("current")
_SleHQosInterfaceDscpToClass_Type = OctetString
_SleHQosInterfaceDscpToClass_Object = MibTableColumn
sleHQosInterfaceDscpToClass = _SleHQosInterfaceDscpToClass_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 19),
    _SleHQosInterfaceDscpToClass_Type()
)
sleHQosInterfaceDscpToClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHQosInterfaceDscpToClass.setStatus("current")


class _SleHQosInterfaceReplace_Type(Integer32):
    """Custom type sleHQosInterfaceReplace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("cos", 1),
          ("dscp", 2))
    )


_SleHQosInterfaceReplace_Type.__name__ = "Integer32"
_SleHQosInterfaceReplace_Object = MibTableColumn
sleHQosInterfaceReplace = _SleHQosInterfaceReplace_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 20),
    _SleHQosInterfaceReplace_Type()
)
sleHQosInterfaceReplace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHQosInterfaceReplace.setStatus("current")
_SleMlsQosInterfaceTrafficIfgExclude_Type = Integer32
_SleMlsQosInterfaceTrafficIfgExclude_Object = MibTableColumn
sleMlsQosInterfaceTrafficIfgExclude = _SleMlsQosInterfaceTrafficIfgExclude_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 21),
    _SleMlsQosInterfaceTrafficIfgExclude_Type()
)
sleMlsQosInterfaceTrafficIfgExclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceTrafficIfgExclude.setStatus("current")
_SleMlsQosInterfaceTrafficPolicingRate_Type = Integer32
_SleMlsQosInterfaceTrafficPolicingRate_Object = MibTableColumn
sleMlsQosInterfaceTrafficPolicingRate = _SleMlsQosInterfaceTrafficPolicingRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 22),
    _SleMlsQosInterfaceTrafficPolicingRate_Type()
)
sleMlsQosInterfaceTrafficPolicingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceTrafficPolicingRate.setStatus("current")
_SleMlsQosInterfaceTrafficPolicingBurst_Type = Integer32
_SleMlsQosInterfaceTrafficPolicingBurst_Object = MibTableColumn
sleMlsQosInterfaceTrafficPolicingBurst = _SleMlsQosInterfaceTrafficPolicingBurst_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 1, 1, 23),
    _SleMlsQosInterfaceTrafficPolicingBurst_Type()
)
sleMlsQosInterfaceTrafficPolicingBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceTrafficPolicingBurst.setStatus("current")
_SleMlsQosInterfaceControl_ObjectIdentity = ObjectIdentity
sleMlsQosInterfaceControl = _SleMlsQosInterfaceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2)
)


class _SleMlsQosInterfaceControlRequest_Type(Integer32):
    """Custom type sleMlsQosInterfaceControlRequest based on Integer32"""
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
        *(("setInterfaceQosMapping", 1),
          ("unSetInterfaceQosMapping", 2),
          ("setInterfaceTrafficShaping", 3),
          ("unSetInterfaceTrafficShaping", 4),
          ("setInterfaceInputPolicyMap", 5),
          ("unSetInterfaceInputPolicyMap", 6),
          ("setInterfaceOutputPolicyMap", 7),
          ("unSetInterfaceOutputPolicyMap", 8),
          ("setInterfaceOveride", 9),
          ("unsetInterfaceOveride", 10),
          ("setInterfaceReplace", 11),
          ("unsetInterfaceReplace", 12),
          ("setInterfaceTrafficIfgExclude", 13),
          ("unsetInterfaceTrafficIfgExclude", 14),
          ("setInterfaceTrafficPolicingDot3x", 15),
          ("unsetInterfaceTrafficPolicingDot3x", 16))
    )


_SleMlsQosInterfaceControlRequest_Type.__name__ = "Integer32"
_SleMlsQosInterfaceControlRequest_Object = MibScalar
sleMlsQosInterfaceControlRequest = _SleMlsQosInterfaceControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2, 1),
    _SleMlsQosInterfaceControlRequest_Type()
)
sleMlsQosInterfaceControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceControlRequest.setStatus("current")
_SleMlsQosInterfaceControlStatus_Type = SleControlStatusType
_SleMlsQosInterfaceControlStatus_Object = MibScalar
sleMlsQosInterfaceControlStatus = _SleMlsQosInterfaceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2, 2),
    _SleMlsQosInterfaceControlStatus_Type()
)
sleMlsQosInterfaceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceControlStatus.setStatus("current")
_SleMlsQosInterfaceControlTimer_Type = Gauge32
_SleMlsQosInterfaceControlTimer_Object = MibScalar
sleMlsQosInterfaceControlTimer = _SleMlsQosInterfaceControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2, 3),
    _SleMlsQosInterfaceControlTimer_Type()
)
sleMlsQosInterfaceControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceControlTimer.setStatus("current")
_SleMlsQosInterfaceontrolTimeStamp_Type = TimeTicks
_SleMlsQosInterfaceontrolTimeStamp_Object = MibScalar
sleMlsQosInterfaceontrolTimeStamp = _SleMlsQosInterfaceontrolTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2, 4),
    _SleMlsQosInterfaceontrolTimeStamp_Type()
)
sleMlsQosInterfaceontrolTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceontrolTimeStamp.setStatus("current")
_SleMlsQosInterfaceControlReqResult_Type = SleControlRequestResultType
_SleMlsQosInterfaceControlReqResult_Object = MibScalar
sleMlsQosInterfaceControlReqResult = _SleMlsQosInterfaceControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2, 5),
    _SleMlsQosInterfaceControlReqResult_Type()
)
sleMlsQosInterfaceControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceControlReqResult.setStatus("current")
_SleMlsQosInterfaceCtrlIndex_Type = Integer32
_SleMlsQosInterfaceCtrlIndex_Object = MibScalar
sleMlsQosInterfaceCtrlIndex = _SleMlsQosInterfaceCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2, 6),
    _SleMlsQosInterfaceCtrlIndex_Type()
)
sleMlsQosInterfaceCtrlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceCtrlIndex.setStatus("current")
_SleMlsQosInterfaceCtrlMapingType_Type = MlsQosInterfaceMapingType
_SleMlsQosInterfaceCtrlMapingType_Object = MibScalar
sleMlsQosInterfaceCtrlMapingType = _SleMlsQosInterfaceCtrlMapingType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2, 7),
    _SleMlsQosInterfaceCtrlMapingType_Type()
)
sleMlsQosInterfaceCtrlMapingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceCtrlMapingType.setStatus("current")
_SleMlsQosInterfaceCtrlMapingIngVal_Type = Integer32
_SleMlsQosInterfaceCtrlMapingIngVal_Object = MibScalar
sleMlsQosInterfaceCtrlMapingIngVal = _SleMlsQosInterfaceCtrlMapingIngVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2, 8),
    _SleMlsQosInterfaceCtrlMapingIngVal_Type()
)
sleMlsQosInterfaceCtrlMapingIngVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceCtrlMapingIngVal.setStatus("current")
_SleMlsQosInterfaceCtrlMapingEgrVal_Type = Integer32
_SleMlsQosInterfaceCtrlMapingEgrVal_Object = MibScalar
sleMlsQosInterfaceCtrlMapingEgrVal = _SleMlsQosInterfaceCtrlMapingEgrVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2, 9),
    _SleMlsQosInterfaceCtrlMapingEgrVal_Type()
)
sleMlsQosInterfaceCtrlMapingEgrVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceCtrlMapingEgrVal.setStatus("current")
_SleMlsQosInterfaceCtrlMapingCosOverride_Type = Integer32
_SleMlsQosInterfaceCtrlMapingCosOverride_Object = MibScalar
sleMlsQosInterfaceCtrlMapingCosOverride = _SleMlsQosInterfaceCtrlMapingCosOverride_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2, 10),
    _SleMlsQosInterfaceCtrlMapingCosOverride_Type()
)
sleMlsQosInterfaceCtrlMapingCosOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceCtrlMapingCosOverride.setStatus("current")
_SleMlsQosInterfaceCtrlMapingTrustState_Type = MlsQosIntfTrustState
_SleMlsQosInterfaceCtrlMapingTrustState_Object = MibScalar
sleMlsQosInterfaceCtrlMapingTrustState = _SleMlsQosInterfaceCtrlMapingTrustState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2, 11),
    _SleMlsQosInterfaceCtrlMapingTrustState_Type()
)
sleMlsQosInterfaceCtrlMapingTrustState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceCtrlMapingTrustState.setStatus("current")
_SleMlsQosInterfaceCtrlTrafficShapeRate_Type = Integer32
_SleMlsQosInterfaceCtrlTrafficShapeRate_Object = MibScalar
sleMlsQosInterfaceCtrlTrafficShapeRate = _SleMlsQosInterfaceCtrlTrafficShapeRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2, 12),
    _SleMlsQosInterfaceCtrlTrafficShapeRate_Type()
)
sleMlsQosInterfaceCtrlTrafficShapeRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceCtrlTrafficShapeRate.setStatus("current")
_SleMlsQosInterfaceCtrlTrafficShapeBurst_Type = Integer32
_SleMlsQosInterfaceCtrlTrafficShapeBurst_Object = MibScalar
sleMlsQosInterfaceCtrlTrafficShapeBurst = _SleMlsQosInterfaceCtrlTrafficShapeBurst_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2, 13),
    _SleMlsQosInterfaceCtrlTrafficShapeBurst_Type()
)
sleMlsQosInterfaceCtrlTrafficShapeBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceCtrlTrafficShapeBurst.setStatus("current")
_SleMlsQosInterfaceCtrlInputPolicyMap_Type = OctetString
_SleMlsQosInterfaceCtrlInputPolicyMap_Object = MibScalar
sleMlsQosInterfaceCtrlInputPolicyMap = _SleMlsQosInterfaceCtrlInputPolicyMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2, 14),
    _SleMlsQosInterfaceCtrlInputPolicyMap_Type()
)
sleMlsQosInterfaceCtrlInputPolicyMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceCtrlInputPolicyMap.setStatus("current")
_SleMlsQosInterfaceCtrlOutputPolicyMap_Type = OctetString
_SleMlsQosInterfaceCtrlOutputPolicyMap_Object = MibScalar
sleMlsQosInterfaceCtrlOutputPolicyMap = _SleMlsQosInterfaceCtrlOutputPolicyMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2, 15),
    _SleMlsQosInterfaceCtrlOutputPolicyMap_Type()
)
sleMlsQosInterfaceCtrlOutputPolicyMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceCtrlOutputPolicyMap.setStatus("current")


class _SleMlsQosInterfaceCtrlMapingCNGValue_Type(Integer32):
    """Custom type sleMlsQosInterfaceCtrlMapingCNGValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SleMlsQosInterfaceCtrlMapingCNGValue_Type.__name__ = "Integer32"
_SleMlsQosInterfaceCtrlMapingCNGValue_Object = MibScalar
sleMlsQosInterfaceCtrlMapingCNGValue = _SleMlsQosInterfaceCtrlMapingCNGValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2, 16),
    _SleMlsQosInterfaceCtrlMapingCNGValue_Type()
)
sleMlsQosInterfaceCtrlMapingCNGValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceCtrlMapingCNGValue.setStatus("current")
_SleMlsQosInterfaceCtrlMapingEgrClassVal_Type = OctetString
_SleMlsQosInterfaceCtrlMapingEgrClassVal_Object = MibScalar
sleMlsQosInterfaceCtrlMapingEgrClassVal = _SleMlsQosInterfaceCtrlMapingEgrClassVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2, 17),
    _SleMlsQosInterfaceCtrlMapingEgrClassVal_Type()
)
sleMlsQosInterfaceCtrlMapingEgrClassVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceCtrlMapingEgrClassVal.setStatus("current")


class _SleMlsQosInterfaceCtrlReplace_Type(Integer32):
    """Custom type sleMlsQosInterfaceCtrlReplace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("cos", 1),
          ("dscp", 2))
    )


_SleMlsQosInterfaceCtrlReplace_Type.__name__ = "Integer32"
_SleMlsQosInterfaceCtrlReplace_Object = MibScalar
sleMlsQosInterfaceCtrlReplace = _SleMlsQosInterfaceCtrlReplace_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 6, 2, 18),
    _SleMlsQosInterfaceCtrlReplace_Type()
)
sleMlsQosInterfaceCtrlReplace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosInterfaceCtrlReplace.setStatus("current")
_SleMlsQosIntfQue_ObjectIdentity = ObjectIdentity
sleMlsQosIntfQue = _SleMlsQosIntfQue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7)
)
_SleMlsQosIntfQueTable_Object = MibTable
sleMlsQosIntfQueTable = _SleMlsQosIntfQueTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 1)
)
if mibBuilder.loadTexts:
    sleMlsQosIntfQueTable.setStatus("current")
_SleMlsQosIntfQueEntry_Object = MibTableRow
sleMlsQosIntfQueEntry = _SleMlsQosIntfQueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 1, 1)
)
sleMlsQosIntfQueEntry.setIndexNames(
    (0, "SLE-MLSQOS-MIB", "sleMlsQosIntfQueIntfIndex"),
    (0, "SLE-MLSQOS-MIB", "sleMlsQosIntfQueId"),
)
if mibBuilder.loadTexts:
    sleMlsQosIntfQueEntry.setStatus("current")


class _SleMlsQosIntfQueIntfIndex_Type(Integer32):
    """Custom type sleMlsQosIntfQueIntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleMlsQosIntfQueIntfIndex_Type.__name__ = "Integer32"
_SleMlsQosIntfQueIntfIndex_Object = MibTableColumn
sleMlsQosIntfQueIntfIndex = _SleMlsQosIntfQueIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 1, 1, 1),
    _SleMlsQosIntfQueIntfIndex_Type()
)
sleMlsQosIntfQueIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueIntfIndex.setStatus("current")


class _SleMlsQosIntfQueId_Type(Integer32):
    """Custom type sleMlsQosIntfQueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleMlsQosIntfQueId_Type.__name__ = "Integer32"
_SleMlsQosIntfQueId_Object = MibTableColumn
sleMlsQosIntfQueId = _SleMlsQosIntfQueId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 1, 1, 2),
    _SleMlsQosIntfQueId_Type()
)
sleMlsQosIntfQueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueId.setStatus("current")
_SleMlsQosIntfQueShapeQueueRate_Type = Integer32
_SleMlsQosIntfQueShapeQueueRate_Object = MibTableColumn
sleMlsQosIntfQueShapeQueueRate = _SleMlsQosIntfQueShapeQueueRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 1, 1, 3),
    _SleMlsQosIntfQueShapeQueueRate_Type()
)
sleMlsQosIntfQueShapeQueueRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueShapeQueueRate.setStatus("current")
_SleMlsQosIntfQueWrrQueueWeight_Type = Integer32
_SleMlsQosIntfQueWrrQueueWeight_Object = MibTableColumn
sleMlsQosIntfQueWrrQueueWeight = _SleMlsQosIntfQueWrrQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 1, 1, 4),
    _SleMlsQosIntfQueWrrQueueWeight_Type()
)
sleMlsQosIntfQueWrrQueueWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueWrrQueueWeight.setStatus("current")
_SleMlsQosIntfQueWrrRandomDetectMinThr_Type = Integer32
_SleMlsQosIntfQueWrrRandomDetectMinThr_Object = MibTableColumn
sleMlsQosIntfQueWrrRandomDetectMinThr = _SleMlsQosIntfQueWrrRandomDetectMinThr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 1, 1, 5),
    _SleMlsQosIntfQueWrrRandomDetectMinThr_Type()
)
sleMlsQosIntfQueWrrRandomDetectMinThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueWrrRandomDetectMinThr.setStatus("current")
_SleMlsQosIntfQueWrrRandomDetectMaxThr_Type = Integer32
_SleMlsQosIntfQueWrrRandomDetectMaxThr_Object = MibTableColumn
sleMlsQosIntfQueWrrRandomDetectMaxThr = _SleMlsQosIntfQueWrrRandomDetectMaxThr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 1, 1, 6),
    _SleMlsQosIntfQueWrrRandomDetectMaxThr_Type()
)
sleMlsQosIntfQueWrrRandomDetectMaxThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueWrrRandomDetectMaxThr.setStatus("current")
_SleMlsQosIntfQueWrrRandomDetectExpWt_Type = Integer32
_SleMlsQosIntfQueWrrRandomDetectExpWt_Object = MibTableColumn
sleMlsQosIntfQueWrrRandomDetectExpWt = _SleMlsQosIntfQueWrrRandomDetectExpWt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 1, 1, 7),
    _SleMlsQosIntfQueWrrRandomDetectExpWt_Type()
)
sleMlsQosIntfQueWrrRandomDetectExpWt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueWrrRandomDetectExpWt.setStatus("current")
_SleMlsQosIntfQueTailDropThr_Type = Integer32
_SleMlsQosIntfQueTailDropThr_Object = MibTableColumn
sleMlsQosIntfQueTailDropThr = _SleMlsQosIntfQueTailDropThr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 1, 1, 8),
    _SleMlsQosIntfQueTailDropThr_Type()
)
sleMlsQosIntfQueTailDropThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueTailDropThr.setStatus("current")
_SleMlsQosIntfQueStrictQueue_Type = Integer32
_SleMlsQosIntfQueStrictQueue_Object = MibTableColumn
sleMlsQosIntfQueStrictQueue = _SleMlsQosIntfQueStrictQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 1, 1, 9),
    _SleMlsQosIntfQueStrictQueue_Type()
)
sleMlsQosIntfQueStrictQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueStrictQueue.setStatus("current")
_SleMlsQosIntfQueRandomDetectDropStart_Type = Integer32
_SleMlsQosIntfQueRandomDetectDropStart_Object = MibTableColumn
sleMlsQosIntfQueRandomDetectDropStart = _SleMlsQosIntfQueRandomDetectDropStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 1, 1, 10),
    _SleMlsQosIntfQueRandomDetectDropStart_Type()
)
sleMlsQosIntfQueRandomDetectDropStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueRandomDetectDropStart.setStatus("current")
_SleMlsQosIntfQueRandomDetectDropSlope_Type = Integer32
_SleMlsQosIntfQueRandomDetectDropSlope_Object = MibTableColumn
sleMlsQosIntfQueRandomDetectDropSlope = _SleMlsQosIntfQueRandomDetectDropSlope_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 1, 1, 11),
    _SleMlsQosIntfQueRandomDetectDropSlope_Type()
)
sleMlsQosIntfQueRandomDetectDropSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueRandomDetectDropSlope.setStatus("current")


class _SleMlsQosIntfQueRandomDetectColor_Type(Integer32):
    """Custom type sleMlsQosIntfQueRandomDetectColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yellow", 1),
          ("red", 2))
    )


_SleMlsQosIntfQueRandomDetectColor_Type.__name__ = "Integer32"
_SleMlsQosIntfQueRandomDetectColor_Object = MibTableColumn
sleMlsQosIntfQueRandomDetectColor = _SleMlsQosIntfQueRandomDetectColor_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 1, 1, 12),
    _SleMlsQosIntfQueRandomDetectColor_Type()
)
sleMlsQosIntfQueRandomDetectColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueRandomDetectColor.setStatus("current")


class _SleMlsQosIntfQueReservedBandwidth_Type(Integer32):
    """Custom type sleMlsQosIntfQueReservedBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 1000000),
    )


_SleMlsQosIntfQueReservedBandwidth_Type.__name__ = "Integer32"
_SleMlsQosIntfQueReservedBandwidth_Object = MibTableColumn
sleMlsQosIntfQueReservedBandwidth = _SleMlsQosIntfQueReservedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 1, 1, 13),
    _SleMlsQosIntfQueReservedBandwidth_Type()
)
sleMlsQosIntfQueReservedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueReservedBandwidth.setStatus("current")
_SleMlsQosIntfQueControl_ObjectIdentity = ObjectIdentity
sleMlsQosIntfQueControl = _SleMlsQosIntfQueControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2)
)


class _SleMlsQosIntfQueControlRequest_Type(Integer32):
    """Custom type sleMlsQosIntfQueControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setQueueProfile", 1),
          ("unSetQueueProfile", 2))
    )


_SleMlsQosIntfQueControlRequest_Type.__name__ = "Integer32"
_SleMlsQosIntfQueControlRequest_Object = MibScalar
sleMlsQosIntfQueControlRequest = _SleMlsQosIntfQueControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2, 1),
    _SleMlsQosIntfQueControlRequest_Type()
)
sleMlsQosIntfQueControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueControlRequest.setStatus("current")
_SleMlsQosIntfQueControlStatus_Type = SleControlStatusType
_SleMlsQosIntfQueControlStatus_Object = MibScalar
sleMlsQosIntfQueControlStatus = _SleMlsQosIntfQueControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2, 2),
    _SleMlsQosIntfQueControlStatus_Type()
)
sleMlsQosIntfQueControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueControlStatus.setStatus("current")
_SleMlsQosIntfQueControlTimer_Type = Gauge32
_SleMlsQosIntfQueControlTimer_Object = MibScalar
sleMlsQosIntfQueControlTimer = _SleMlsQosIntfQueControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2, 3),
    _SleMlsQosIntfQueControlTimer_Type()
)
sleMlsQosIntfQueControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueControlTimer.setStatus("current")
_SleMlsQosIntfQueontrolTimeStamp_Type = TimeTicks
_SleMlsQosIntfQueontrolTimeStamp_Object = MibScalar
sleMlsQosIntfQueontrolTimeStamp = _SleMlsQosIntfQueontrolTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2, 4),
    _SleMlsQosIntfQueontrolTimeStamp_Type()
)
sleMlsQosIntfQueontrolTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueontrolTimeStamp.setStatus("current")
_SleMlsQosIntfQueControlReqResult_Type = SleControlRequestResultType
_SleMlsQosIntfQueControlReqResult_Object = MibScalar
sleMlsQosIntfQueControlReqResult = _SleMlsQosIntfQueControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2, 5),
    _SleMlsQosIntfQueControlReqResult_Type()
)
sleMlsQosIntfQueControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueControlReqResult.setStatus("current")
_SleMlsQosIntfQueCtrlInterfaceIndex_Type = Integer32
_SleMlsQosIntfQueCtrlInterfaceIndex_Object = MibScalar
sleMlsQosIntfQueCtrlInterfaceIndex = _SleMlsQosIntfQueCtrlInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2, 6),
    _SleMlsQosIntfQueCtrlInterfaceIndex_Type()
)
sleMlsQosIntfQueCtrlInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueCtrlInterfaceIndex.setStatus("current")
_SleMlsQosIntfQueCtrlQueueId_Type = Integer32
_SleMlsQosIntfQueCtrlQueueId_Object = MibScalar
sleMlsQosIntfQueCtrlQueueId = _SleMlsQosIntfQueCtrlQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2, 7),
    _SleMlsQosIntfQueCtrlQueueId_Type()
)
sleMlsQosIntfQueCtrlQueueId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueCtrlQueueId.setStatus("current")
_SleMlsQosIntfQueCtrlProfileType_Type = MlsQosIntfQueProfilingType
_SleMlsQosIntfQueCtrlProfileType_Object = MibScalar
sleMlsQosIntfQueCtrlProfileType = _SleMlsQosIntfQueCtrlProfileType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2, 8),
    _SleMlsQosIntfQueCtrlProfileType_Type()
)
sleMlsQosIntfQueCtrlProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueCtrlProfileType.setStatus("current")
_SleMlsQosIntfQueCtrlShapeQueueRate_Type = Integer32
_SleMlsQosIntfQueCtrlShapeQueueRate_Object = MibScalar
sleMlsQosIntfQueCtrlShapeQueueRate = _SleMlsQosIntfQueCtrlShapeQueueRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2, 9),
    _SleMlsQosIntfQueCtrlShapeQueueRate_Type()
)
sleMlsQosIntfQueCtrlShapeQueueRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueCtrlShapeQueueRate.setStatus("current")
_SleMlsQosIntfQueCtrlWrrQueueWeight_Type = Integer32
_SleMlsQosIntfQueCtrlWrrQueueWeight_Object = MibScalar
sleMlsQosIntfQueCtrlWrrQueueWeight = _SleMlsQosIntfQueCtrlWrrQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2, 10),
    _SleMlsQosIntfQueCtrlWrrQueueWeight_Type()
)
sleMlsQosIntfQueCtrlWrrQueueWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueCtrlWrrQueueWeight.setStatus("current")
_SleMlsQosIntfQueCtrlWrrRandomDetectMinThr_Type = Integer32
_SleMlsQosIntfQueCtrlWrrRandomDetectMinThr_Object = MibScalar
sleMlsQosIntfQueCtrlWrrRandomDetectMinThr = _SleMlsQosIntfQueCtrlWrrRandomDetectMinThr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2, 11),
    _SleMlsQosIntfQueCtrlWrrRandomDetectMinThr_Type()
)
sleMlsQosIntfQueCtrlWrrRandomDetectMinThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueCtrlWrrRandomDetectMinThr.setStatus("current")
_SleMlsQosIntfQueCtrlWrrRandomDetectMaxThr_Type = Integer32
_SleMlsQosIntfQueCtrlWrrRandomDetectMaxThr_Object = MibScalar
sleMlsQosIntfQueCtrlWrrRandomDetectMaxThr = _SleMlsQosIntfQueCtrlWrrRandomDetectMaxThr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2, 12),
    _SleMlsQosIntfQueCtrlWrrRandomDetectMaxThr_Type()
)
sleMlsQosIntfQueCtrlWrrRandomDetectMaxThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueCtrlWrrRandomDetectMaxThr.setStatus("current")
_SleMlsQosIntfQueCtrlWrrRandomDetectExpWt_Type = Integer32
_SleMlsQosIntfQueCtrlWrrRandomDetectExpWt_Object = MibScalar
sleMlsQosIntfQueCtrlWrrRandomDetectExpWt = _SleMlsQosIntfQueCtrlWrrRandomDetectExpWt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2, 13),
    _SleMlsQosIntfQueCtrlWrrRandomDetectExpWt_Type()
)
sleMlsQosIntfQueCtrlWrrRandomDetectExpWt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueCtrlWrrRandomDetectExpWt.setStatus("current")
_SleMlsQosIntfQueCtrlTailDropThr_Type = Integer32
_SleMlsQosIntfQueCtrlTailDropThr_Object = MibScalar
sleMlsQosIntfQueCtrlTailDropThr = _SleMlsQosIntfQueCtrlTailDropThr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2, 14),
    _SleMlsQosIntfQueCtrlTailDropThr_Type()
)
sleMlsQosIntfQueCtrlTailDropThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueCtrlTailDropThr.setStatus("current")
_SleMlsQosIntfQueCtrlRandomDetectDropStart_Type = Integer32
_SleMlsQosIntfQueCtrlRandomDetectDropStart_Object = MibScalar
sleMlsQosIntfQueCtrlRandomDetectDropStart = _SleMlsQosIntfQueCtrlRandomDetectDropStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2, 15),
    _SleMlsQosIntfQueCtrlRandomDetectDropStart_Type()
)
sleMlsQosIntfQueCtrlRandomDetectDropStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueCtrlRandomDetectDropStart.setStatus("current")
_SleMlsQosIntfQueCtrlRandomDetectDropSlope_Type = Integer32
_SleMlsQosIntfQueCtrlRandomDetectDropSlope_Object = MibScalar
sleMlsQosIntfQueCtrlRandomDetectDropSlope = _SleMlsQosIntfQueCtrlRandomDetectDropSlope_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2, 16),
    _SleMlsQosIntfQueCtrlRandomDetectDropSlope_Type()
)
sleMlsQosIntfQueCtrlRandomDetectDropSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueCtrlRandomDetectDropSlope.setStatus("current")


class _SleMlsQosIntfQueCtrlRandomDetectColor_Type(Integer32):
    """Custom type sleMlsQosIntfQueCtrlRandomDetectColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yellow", 1),
          ("red", 2))
    )


_SleMlsQosIntfQueCtrlRandomDetectColor_Type.__name__ = "Integer32"
_SleMlsQosIntfQueCtrlRandomDetectColor_Object = MibScalar
sleMlsQosIntfQueCtrlRandomDetectColor = _SleMlsQosIntfQueCtrlRandomDetectColor_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2, 17),
    _SleMlsQosIntfQueCtrlRandomDetectColor_Type()
)
sleMlsQosIntfQueCtrlRandomDetectColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueCtrlRandomDetectColor.setStatus("current")


class _SleMlsQosIntfQueCtrlReservedBandwidth_Type(Integer32):
    """Custom type sleMlsQosIntfQueCtrlReservedBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 1000000),
    )


_SleMlsQosIntfQueCtrlReservedBandwidth_Type.__name__ = "Integer32"
_SleMlsQosIntfQueCtrlReservedBandwidth_Object = MibScalar
sleMlsQosIntfQueCtrlReservedBandwidth = _SleMlsQosIntfQueCtrlReservedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 7, 2, 18),
    _SleMlsQosIntfQueCtrlReservedBandwidth_Type()
)
sleMlsQosIntfQueCtrlReservedBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosIntfQueCtrlReservedBandwidth.setStatus("current")
_SleMlsQosQStats_ObjectIdentity = ObjectIdentity
sleMlsQosQStats = _SleMlsQosQStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8)
)
_SleMlsQosQStatsTable_Object = MibTable
sleMlsQosQStatsTable = _SleMlsQosQStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1)
)
if mibBuilder.loadTexts:
    sleMlsQosQStatsTable.setStatus("current")
_SleMlsQosQStatsEntry_Object = MibTableRow
sleMlsQosQStatsEntry = _SleMlsQosQStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1, 1)
)
sleMlsQosQStatsEntry.setIndexNames(
    (0, "SLE-MLSQOS-MIB", "sleMlsQosQstatsIfIndex"),
    (0, "SLE-MLSQOS-MIB", "sleMlsQosQId"),
)
if mibBuilder.loadTexts:
    sleMlsQosQStatsEntry.setStatus("current")


class _SleMlsQosQstatsIfIndex_Type(Integer32):
    """Custom type sleMlsQosQstatsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleMlsQosQstatsIfIndex_Type.__name__ = "Integer32"
_SleMlsQosQstatsIfIndex_Object = MibTableColumn
sleMlsQosQstatsIfIndex = _SleMlsQosQstatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1, 1, 1),
    _SleMlsQosQstatsIfIndex_Type()
)
sleMlsQosQstatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMlsQosQstatsIfIndex.setStatus("current")


class _SleMlsQosQId_Type(Integer32):
    """Custom type sleMlsQosQId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleMlsQosQId_Type.__name__ = "Integer32"
_SleMlsQosQId_Object = MibTableColumn
sleMlsQosQId = _SleMlsQosQId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1, 1, 2),
    _SleMlsQosQId_Type()
)
sleMlsQosQId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMlsQosQId.setStatus("current")
_SleMlsQosWredGreenDropPkts_Type = Counter64
_SleMlsQosWredGreenDropPkts_Object = MibTableColumn
sleMlsQosWredGreenDropPkts = _SleMlsQosWredGreenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1, 1, 3),
    _SleMlsQosWredGreenDropPkts_Type()
)
sleMlsQosWredGreenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosWredGreenDropPkts.setStatus("current")
_SleMlsQosWredYellowDropPkts_Type = Counter64
_SleMlsQosWredYellowDropPkts_Object = MibTableColumn
sleMlsQosWredYellowDropPkts = _SleMlsQosWredYellowDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1, 1, 4),
    _SleMlsQosWredYellowDropPkts_Type()
)
sleMlsQosWredYellowDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosWredYellowDropPkts.setStatus("current")
_SleMlsQosWredRedDropPkts_Type = Counter64
_SleMlsQosWredRedDropPkts_Object = MibTableColumn
sleMlsQosWredRedDropPkts = _SleMlsQosWredRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1, 1, 5),
    _SleMlsQosWredRedDropPkts_Type()
)
sleMlsQosWredRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosWredRedDropPkts.setStatus("current")
_SleMlsQosTailDropPkts_Type = Counter64
_SleMlsQosTailDropPkts_Object = MibTableColumn
sleMlsQosTailDropPkts = _SleMlsQosTailDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1, 1, 6),
    _SleMlsQosTailDropPkts_Type()
)
sleMlsQosTailDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosTailDropPkts.setStatus("current")
_SleMlsQosTailDropBytes_Type = Counter64
_SleMlsQosTailDropBytes_Object = MibTableColumn
sleMlsQosTailDropBytes = _SleMlsQosTailDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1, 1, 7),
    _SleMlsQosTailDropBytes_Type()
)
sleMlsQosTailDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosTailDropBytes.setStatus("current")
_SleMlsQosQStatsOutPkts_Type = Counter64
_SleMlsQosQStatsOutPkts_Object = MibTableColumn
sleMlsQosQStatsOutPkts = _SleMlsQosQStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1, 1, 8),
    _SleMlsQosQStatsOutPkts_Type()
)
sleMlsQosQStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosQStatsOutPkts.setStatus("current")
_SleMlsQosQStatsOutBytes_Type = Counter64
_SleMlsQosQStatsOutBytes_Object = MibTableColumn
sleMlsQosQStatsOutBytes = _SleMlsQosQStatsOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1, 1, 9),
    _SleMlsQosQStatsOutBytes_Type()
)
sleMlsQosQStatsOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosQStatsOutBytes.setStatus("current")
_SleMlsQosQStatsMcastOutPkts_Type = Counter64
_SleMlsQosQStatsMcastOutPkts_Object = MibTableColumn
sleMlsQosQStatsMcastOutPkts = _SleMlsQosQStatsMcastOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1, 1, 10),
    _SleMlsQosQStatsMcastOutPkts_Type()
)
sleMlsQosQStatsMcastOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosQStatsMcastOutPkts.setStatus("current")
_SleMlsQosQStatsMcastOutBytes_Type = Counter64
_SleMlsQosQStatsMcastOutBytes_Object = MibTableColumn
sleMlsQosQStatsMcastOutBytes = _SleMlsQosQStatsMcastOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1, 1, 11),
    _SleMlsQosQStatsMcastOutBytes_Type()
)
sleMlsQosQStatsMcastOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosQStatsMcastOutBytes.setStatus("current")
_SleMlsQosQStatsDropPkts_Type = Counter64
_SleMlsQosQStatsDropPkts_Object = MibTableColumn
sleMlsQosQStatsDropPkts = _SleMlsQosQStatsDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1, 1, 12),
    _SleMlsQosQStatsDropPkts_Type()
)
sleMlsQosQStatsDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosQStatsDropPkts.setStatus("current")
_SleMlsQosQStatsDropBytes_Type = Counter64
_SleMlsQosQStatsDropBytes_Object = MibTableColumn
sleMlsQosQStatsDropBytes = _SleMlsQosQStatsDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1, 1, 13),
    _SleMlsQosQStatsDropBytes_Type()
)
sleMlsQosQStatsDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosQStatsDropBytes.setStatus("current")
_SleMlsQosQStatsMcastDropPkts_Type = Counter64
_SleMlsQosQStatsMcastDropPkts_Object = MibTableColumn
sleMlsQosQStatsMcastDropPkts = _SleMlsQosQStatsMcastDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1, 1, 14),
    _SleMlsQosQStatsMcastDropPkts_Type()
)
sleMlsQosQStatsMcastDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosQStatsMcastDropPkts.setStatus("current")
_SleMlsQosQStatsMcastDropBytes_Type = Counter64
_SleMlsQosQStatsMcastDropBytes_Object = MibTableColumn
sleMlsQosQStatsMcastDropBytes = _SleMlsQosQStatsMcastDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1, 1, 15),
    _SleMlsQosQStatsMcastDropBytes_Type()
)
sleMlsQosQStatsMcastDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosQStatsMcastDropBytes.setStatus("current")
_SleMlsQosQStatsEnqueuedPkts_Type = Counter64
_SleMlsQosQStatsEnqueuedPkts_Object = MibTableColumn
sleMlsQosQStatsEnqueuedPkts = _SleMlsQosQStatsEnqueuedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1, 1, 16),
    _SleMlsQosQStatsEnqueuedPkts_Type()
)
sleMlsQosQStatsEnqueuedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosQStatsEnqueuedPkts.setStatus("current")
_SleMlsQosQStatsEnqueuedBytes_Type = Counter64
_SleMlsQosQStatsEnqueuedBytes_Object = MibTableColumn
sleMlsQosQStatsEnqueuedBytes = _SleMlsQosQStatsEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 1, 1, 17),
    _SleMlsQosQStatsEnqueuedBytes_Type()
)
sleMlsQosQStatsEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosQStatsEnqueuedBytes.setStatus("current")
_SleMlsQosQStatsControl_ObjectIdentity = ObjectIdentity
sleMlsQosQStatsControl = _SleMlsQosQStatsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 2)
)


class _SleMlsQosQStatsControlRequest_Type(Integer32):
    """Custom type sleMlsQosQStatsControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearWredStats", 1),
          ("clearTailDropStats", 2),
          ("clearQueueStats", 3))
    )


_SleMlsQosQStatsControlRequest_Type.__name__ = "Integer32"
_SleMlsQosQStatsControlRequest_Object = MibScalar
sleMlsQosQStatsControlRequest = _SleMlsQosQStatsControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 2, 1),
    _SleMlsQosQStatsControlRequest_Type()
)
sleMlsQosQStatsControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosQStatsControlRequest.setStatus("current")
_SleMlsQosQStatsControlStatus_Type = SleControlStatusType
_SleMlsQosQStatsControlStatus_Object = MibScalar
sleMlsQosQStatsControlStatus = _SleMlsQosQStatsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 2, 2),
    _SleMlsQosQStatsControlStatus_Type()
)
sleMlsQosQStatsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosQStatsControlStatus.setStatus("current")
_SleMlsQosQStatsControlTimer_Type = Gauge32
_SleMlsQosQStatsControlTimer_Object = MibScalar
sleMlsQosQStatsControlTimer = _SleMlsQosQStatsControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 2, 3),
    _SleMlsQosQStatsControlTimer_Type()
)
sleMlsQosQStatsControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosQStatsControlTimer.setStatus("current")
_SleMlsQosQStatsontrolTimeStamp_Type = TimeTicks
_SleMlsQosQStatsontrolTimeStamp_Object = MibScalar
sleMlsQosQStatsontrolTimeStamp = _SleMlsQosQStatsontrolTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 2, 4),
    _SleMlsQosQStatsontrolTimeStamp_Type()
)
sleMlsQosQStatsontrolTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosQStatsontrolTimeStamp.setStatus("current")
_SleMlsQosQStatsControlReqResult_Type = SleControlRequestResultType
_SleMlsQosQStatsControlReqResult_Object = MibScalar
sleMlsQosQStatsControlReqResult = _SleMlsQosQStatsControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 2, 5),
    _SleMlsQosQStatsControlReqResult_Type()
)
sleMlsQosQStatsControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosQStatsControlReqResult.setStatus("current")
_SleMlsQosQstatsCtrlIfIndex_Type = Integer32
_SleMlsQosQstatsCtrlIfIndex_Object = MibScalar
sleMlsQosQstatsCtrlIfIndex = _SleMlsQosQstatsCtrlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 2, 6),
    _SleMlsQosQstatsCtrlIfIndex_Type()
)
sleMlsQosQstatsCtrlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosQstatsCtrlIfIndex.setStatus("current")
_SleMlsQosQstatsCtrlQId_Type = Integer32
_SleMlsQosQstatsCtrlQId_Object = MibScalar
sleMlsQosQstatsCtrlQId = _SleMlsQosQstatsCtrlQId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 8, 2, 7),
    _SleMlsQosQstatsCtrlQId_Type()
)
sleMlsQosQstatsCtrlQId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosQstatsCtrlQId.setStatus("current")
_SleHqosClassMapQueue_ObjectIdentity = ObjectIdentity
sleHqosClassMapQueue = _SleHqosClassMapQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 9)
)
_SleHqosClassMapQueueInfoTable_Object = MibTable
sleHqosClassMapQueueInfoTable = _SleHqosClassMapQueueInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 9, 1)
)
if mibBuilder.loadTexts:
    sleHqosClassMapQueueInfoTable.setStatus("current")
_SleHqosClassMapQueueInfoEntry_Object = MibTableRow
sleHqosClassMapQueueInfoEntry = _SleHqosClassMapQueueInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 9, 1, 1)
)
sleHqosClassMapQueueInfoEntry.setIndexNames(
    (0, "SLE-MLSQOS-MIB", "sleHqosClassMapQueueInfoName"),
)
if mibBuilder.loadTexts:
    sleHqosClassMapQueueInfoEntry.setStatus("current")
_SleHqosClassMapQueueInfoName_Type = OctetString
_SleHqosClassMapQueueInfoName_Object = MibTableColumn
sleHqosClassMapQueueInfoName = _SleHqosClassMapQueueInfoName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 9, 1, 1, 1),
    _SleHqosClassMapQueueInfoName_Type()
)
sleHqosClassMapQueueInfoName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleHqosClassMapQueueInfoName.setStatus("current")
_SleHqosClassMapQueueInfoMatchGroup_Type = Integer32
_SleHqosClassMapQueueInfoMatchGroup_Object = MibTableColumn
sleHqosClassMapQueueInfoMatchGroup = _SleHqosClassMapQueueInfoMatchGroup_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 9, 1, 1, 2),
    _SleHqosClassMapQueueInfoMatchGroup_Type()
)
sleHqosClassMapQueueInfoMatchGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHqosClassMapQueueInfoMatchGroup.setStatus("current")
_SleHqosClassMapQueueControl_ObjectIdentity = ObjectIdentity
sleHqosClassMapQueueControl = _SleHqosClassMapQueueControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 9, 2)
)


class _SleHqosClassMapQueueControlRequest_Type(Integer32):
    """Custom type sleHqosClassMapQueueControlRequest based on Integer32"""
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
        *(("createSleHqosClassMapQueueControlEntry", 1),
          ("deleteSleHqosClassMapQueueControlEntry", 2),
          ("setSleHqosClassMapQueueControlMatchGroup", 3),
          ("unsetSleHqosClassMapQueueControlMatchGroup", 4))
    )


_SleHqosClassMapQueueControlRequest_Type.__name__ = "Integer32"
_SleHqosClassMapQueueControlRequest_Object = MibScalar
sleHqosClassMapQueueControlRequest = _SleHqosClassMapQueueControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 9, 2, 1),
    _SleHqosClassMapQueueControlRequest_Type()
)
sleHqosClassMapQueueControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHqosClassMapQueueControlRequest.setStatus("current")
_SleHqosClassMapQueueControlStatus_Type = SleControlStatusType
_SleHqosClassMapQueueControlStatus_Object = MibScalar
sleHqosClassMapQueueControlStatus = _SleHqosClassMapQueueControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 9, 2, 2),
    _SleHqosClassMapQueueControlStatus_Type()
)
sleHqosClassMapQueueControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHqosClassMapQueueControlStatus.setStatus("current")
_SleHqosClassMapQueueControlTimer_Type = Gauge32
_SleHqosClassMapQueueControlTimer_Object = MibScalar
sleHqosClassMapQueueControlTimer = _SleHqosClassMapQueueControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 9, 2, 3),
    _SleHqosClassMapQueueControlTimer_Type()
)
sleHqosClassMapQueueControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHqosClassMapQueueControlTimer.setStatus("current")
_SleHqosClassMapQueueControlTimeStamp_Type = TimeTicks
_SleHqosClassMapQueueControlTimeStamp_Object = MibScalar
sleHqosClassMapQueueControlTimeStamp = _SleHqosClassMapQueueControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 9, 2, 4),
    _SleHqosClassMapQueueControlTimeStamp_Type()
)
sleHqosClassMapQueueControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHqosClassMapQueueControlTimeStamp.setStatus("current")
_SleHqosClassMapQueueControlReqResult_Type = SleControlRequestResultType
_SleHqosClassMapQueueControlReqResult_Object = MibScalar
sleHqosClassMapQueueControlReqResult = _SleHqosClassMapQueueControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 9, 2, 5),
    _SleHqosClassMapQueueControlReqResult_Type()
)
sleHqosClassMapQueueControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHqosClassMapQueueControlReqResult.setStatus("current")
_SleHqosClassMapQueueControlName_Type = OctetString
_SleHqosClassMapQueueControlName_Object = MibScalar
sleHqosClassMapQueueControlName = _SleHqosClassMapQueueControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 9, 2, 6),
    _SleHqosClassMapQueueControlName_Type()
)
sleHqosClassMapQueueControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHqosClassMapQueueControlName.setStatus("current")
_SleHqosClassMapQueueControlMatchGroup_Type = Integer32
_SleHqosClassMapQueueControlMatchGroup_Object = MibScalar
sleHqosClassMapQueueControlMatchGroup = _SleHqosClassMapQueueControlMatchGroup_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 9, 2, 7),
    _SleHqosClassMapQueueControlMatchGroup_Type()
)
sleHqosClassMapQueueControlMatchGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHqosClassMapQueueControlMatchGroup.setStatus("current")
_SleHqosPolicyMapQueue_ObjectIdentity = ObjectIdentity
sleHqosPolicyMapQueue = _SleHqosPolicyMapQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10)
)
_SleHqosPolicyMapQueueInfoTable_Object = MibTable
sleHqosPolicyMapQueueInfoTable = _SleHqosPolicyMapQueueInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 1)
)
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueInfoTable.setStatus("current")
_SleHqosPolicyMapQueueInfoEntry_Object = MibTableRow
sleHqosPolicyMapQueueInfoEntry = _SleHqosPolicyMapQueueInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 1, 1)
)
sleHqosPolicyMapQueueInfoEntry.setIndexNames(
    (0, "SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueInfoName"),
    (0, "SLE-MLSQOS-MIB", "sleHqosClassMapQueueInfoName"),
)
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueInfoEntry.setStatus("current")
_SleHqosPolicyMapQueueInfoName_Type = OctetString
_SleHqosPolicyMapQueueInfoName_Object = MibTableColumn
sleHqosPolicyMapQueueInfoName = _SleHqosPolicyMapQueueInfoName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 1, 1, 1),
    _SleHqosPolicyMapQueueInfoName_Type()
)
sleHqosPolicyMapQueueInfoName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueInfoName.setStatus("current")


class _SleHqosPolicyMapQueueInfoShape_Type(SnmpAdminString):
    """Custom type sleHqosPolicyMapQueueInfoShape based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SleHqosPolicyMapQueueInfoShape_Type.__name__ = "SnmpAdminString"
_SleHqosPolicyMapQueueInfoShape_Object = MibTableColumn
sleHqosPolicyMapQueueInfoShape = _SleHqosPolicyMapQueueInfoShape_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 1, 1, 2),
    _SleHqosPolicyMapQueueInfoShape_Type()
)
sleHqosPolicyMapQueueInfoShape.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueInfoShape.setStatus("current")


class _SleHqosPolicyMapQueueInfoBandwidth_Type(SnmpAdminString):
    """Custom type sleHqosPolicyMapQueueInfoBandwidth based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SleHqosPolicyMapQueueInfoBandwidth_Type.__name__ = "SnmpAdminString"
_SleHqosPolicyMapQueueInfoBandwidth_Object = MibTableColumn
sleHqosPolicyMapQueueInfoBandwidth = _SleHqosPolicyMapQueueInfoBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 1, 1, 3),
    _SleHqosPolicyMapQueueInfoBandwidth_Type()
)
sleHqosPolicyMapQueueInfoBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueInfoBandwidth.setStatus("current")


class _SleHqosPolicyMapQueueInfoBandwidthRemainingPercent_Type(Integer32):
    """Custom type sleHqosPolicyMapQueueInfoBandwidthRemainingPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleHqosPolicyMapQueueInfoBandwidthRemainingPercent_Type.__name__ = "Integer32"
_SleHqosPolicyMapQueueInfoBandwidthRemainingPercent_Object = MibTableColumn
sleHqosPolicyMapQueueInfoBandwidthRemainingPercent = _SleHqosPolicyMapQueueInfoBandwidthRemainingPercent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 1, 1, 4),
    _SleHqosPolicyMapQueueInfoBandwidthRemainingPercent_Type()
)
sleHqosPolicyMapQueueInfoBandwidthRemainingPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueInfoBandwidthRemainingPercent.setStatus("current")


class _SleHqosPolicyMapQueueInfoQueueLimit_Type(SnmpAdminString):
    """Custom type sleHqosPolicyMapQueueInfoQueueLimit based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SleHqosPolicyMapQueueInfoQueueLimit_Type.__name__ = "SnmpAdminString"
_SleHqosPolicyMapQueueInfoQueueLimit_Object = MibTableColumn
sleHqosPolicyMapQueueInfoQueueLimit = _SleHqosPolicyMapQueueInfoQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 1, 1, 5),
    _SleHqosPolicyMapQueueInfoQueueLimit_Type()
)
sleHqosPolicyMapQueueInfoQueueLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueInfoQueueLimit.setStatus("current")


class _SleHqosPolicyMapQueueInfoServicePolicyName_Type(SnmpAdminString):
    """Custom type sleHqosPolicyMapQueueInfoServicePolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SleHqosPolicyMapQueueInfoServicePolicyName_Type.__name__ = "SnmpAdminString"
_SleHqosPolicyMapQueueInfoServicePolicyName_Object = MibTableColumn
sleHqosPolicyMapQueueInfoServicePolicyName = _SleHqosPolicyMapQueueInfoServicePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 1, 1, 6),
    _SleHqosPolicyMapQueueInfoServicePolicyName_Type()
)
sleHqosPolicyMapQueueInfoServicePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueInfoServicePolicyName.setStatus("current")
_SleHqosPolicyMapQueueInfoPriority_Type = Integer32
_SleHqosPolicyMapQueueInfoPriority_Object = MibTableColumn
sleHqosPolicyMapQueueInfoPriority = _SleHqosPolicyMapQueueInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 1, 1, 7),
    _SleHqosPolicyMapQueueInfoPriority_Type()
)
sleHqosPolicyMapQueueInfoPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueInfoPriority.setStatus("current")


class _SleHqosPolicyMapQueueInfoRDMinThreshold_Type(SnmpAdminString):
    """Custom type sleHqosPolicyMapQueueInfoRDMinThreshold based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SleHqosPolicyMapQueueInfoRDMinThreshold_Type.__name__ = "SnmpAdminString"
_SleHqosPolicyMapQueueInfoRDMinThreshold_Object = MibTableColumn
sleHqosPolicyMapQueueInfoRDMinThreshold = _SleHqosPolicyMapQueueInfoRDMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 1, 1, 8),
    _SleHqosPolicyMapQueueInfoRDMinThreshold_Type()
)
sleHqosPolicyMapQueueInfoRDMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueInfoRDMinThreshold.setStatus("current")


class _SleHqosPolicyMapQueueInfoRDMaxThreshold_Type(SnmpAdminString):
    """Custom type sleHqosPolicyMapQueueInfoRDMaxThreshold based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SleHqosPolicyMapQueueInfoRDMaxThreshold_Type.__name__ = "SnmpAdminString"
_SleHqosPolicyMapQueueInfoRDMaxThreshold_Object = MibTableColumn
sleHqosPolicyMapQueueInfoRDMaxThreshold = _SleHqosPolicyMapQueueInfoRDMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 1, 1, 9),
    _SleHqosPolicyMapQueueInfoRDMaxThreshold_Type()
)
sleHqosPolicyMapQueueInfoRDMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueInfoRDMaxThreshold.setStatus("current")
_SleHqosPolicyMapQueueControl_ObjectIdentity = ObjectIdentity
sleHqosPolicyMapQueueControl = _SleHqosPolicyMapQueueControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 2)
)


class _SleHqosPolicyMapQueueControlRequest_Type(Integer32):
    """Custom type sleHqosPolicyMapQueueControlRequest based on Integer32"""
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
        *(("createPolicyMapQueueEntry", 1),
          ("deletePolicyMapQueueEntry", 2),
          ("setPolicyMapQueueParameters", 3),
          ("unsetPolicyMapQueueParameters", 4),
          ("setPolicyMapQueueServicePolicy", 5),
          ("unsetPolicyMapQueueServicePolicy", 6),
          ("setPolicyMapQueueRandomDetect", 7),
          ("unsetPolicyMapQueueRandomDetect", 8))
    )


_SleHqosPolicyMapQueueControlRequest_Type.__name__ = "Integer32"
_SleHqosPolicyMapQueueControlRequest_Object = MibScalar
sleHqosPolicyMapQueueControlRequest = _SleHqosPolicyMapQueueControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 2, 1),
    _SleHqosPolicyMapQueueControlRequest_Type()
)
sleHqosPolicyMapQueueControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueControlRequest.setStatus("current")
_SleHqosPolicyMapQueueControlStatus_Type = SleControlStatusType
_SleHqosPolicyMapQueueControlStatus_Object = MibScalar
sleHqosPolicyMapQueueControlStatus = _SleHqosPolicyMapQueueControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 2, 2),
    _SleHqosPolicyMapQueueControlStatus_Type()
)
sleHqosPolicyMapQueueControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueControlStatus.setStatus("current")
_SleHqosPolicyMapQueueControlTimer_Type = Gauge32
_SleHqosPolicyMapQueueControlTimer_Object = MibScalar
sleHqosPolicyMapQueueControlTimer = _SleHqosPolicyMapQueueControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 2, 3),
    _SleHqosPolicyMapQueueControlTimer_Type()
)
sleHqosPolicyMapQueueControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueControlTimer.setStatus("current")
_SleHqosPolicyMapQueueControlTimeStamp_Type = TimeTicks
_SleHqosPolicyMapQueueControlTimeStamp_Object = MibScalar
sleHqosPolicyMapQueueControlTimeStamp = _SleHqosPolicyMapQueueControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 2, 4),
    _SleHqosPolicyMapQueueControlTimeStamp_Type()
)
sleHqosPolicyMapQueueControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueControlTimeStamp.setStatus("current")
_SleHqosPolicyMapQueueControlReqResult_Type = SleControlRequestResultType
_SleHqosPolicyMapQueueControlReqResult_Object = MibScalar
sleHqosPolicyMapQueueControlReqResult = _SleHqosPolicyMapQueueControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 2, 5),
    _SleHqosPolicyMapQueueControlReqResult_Type()
)
sleHqosPolicyMapQueueControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueControlReqResult.setStatus("current")
_SleHqosPolicyMapQueueControlName_Type = OctetString
_SleHqosPolicyMapQueueControlName_Object = MibScalar
sleHqosPolicyMapQueueControlName = _SleHqosPolicyMapQueueControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 2, 6),
    _SleHqosPolicyMapQueueControlName_Type()
)
sleHqosPolicyMapQueueControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueControlName.setStatus("current")
_SleHqosPolicyMapQueueControlClassMapQueueName_Type = OctetString
_SleHqosPolicyMapQueueControlClassMapQueueName_Object = MibScalar
sleHqosPolicyMapQueueControlClassMapQueueName = _SleHqosPolicyMapQueueControlClassMapQueueName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 2, 7),
    _SleHqosPolicyMapQueueControlClassMapQueueName_Type()
)
sleHqosPolicyMapQueueControlClassMapQueueName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueControlClassMapQueueName.setStatus("current")


class _SleHqosPolicyMapQueueControlParams_Type(Integer32):
    """Custom type sleHqosPolicyMapQueueControlParams based on Integer32"""
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
        *(("shape", 1),
          ("queueLimit", 2),
          ("bandwidth", 3),
          ("bandwidthRemain", 4),
          ("priority", 5))
    )


_SleHqosPolicyMapQueueControlParams_Type.__name__ = "Integer32"
_SleHqosPolicyMapQueueControlParams_Object = MibScalar
sleHqosPolicyMapQueueControlParams = _SleHqosPolicyMapQueueControlParams_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 2, 8),
    _SleHqosPolicyMapQueueControlParams_Type()
)
sleHqosPolicyMapQueueControlParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueControlParams.setStatus("current")
_SleHqosPolicyMapQueueControlParamsValue_Type = Integer32
_SleHqosPolicyMapQueueControlParamsValue_Object = MibScalar
sleHqosPolicyMapQueueControlParamsValue = _SleHqosPolicyMapQueueControlParamsValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 2, 9),
    _SleHqosPolicyMapQueueControlParamsValue_Type()
)
sleHqosPolicyMapQueueControlParamsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueControlParamsValue.setStatus("current")


class _SleHqosPolicyMapQueueControlUnits_Type(Integer32):
    """Custom type sleHqosPolicyMapQueueControlUnits based on Integer32"""
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
        *(("bps", 1),
          ("kbps", 2),
          ("mbps", 3),
          ("gbps", 4),
          ("packets", 5),
          ("bytes", 6),
          ("kbytes", 7),
          ("average", 8),
          ("percent", 9))
    )


_SleHqosPolicyMapQueueControlUnits_Type.__name__ = "Integer32"
_SleHqosPolicyMapQueueControlUnits_Object = MibScalar
sleHqosPolicyMapQueueControlUnits = _SleHqosPolicyMapQueueControlUnits_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 2, 10),
    _SleHqosPolicyMapQueueControlUnits_Type()
)
sleHqosPolicyMapQueueControlUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueControlUnits.setStatus("current")


class _SleHqosPolicyMapQueueControlRDMiniThreshold_Type(Integer32):
    """Custom type sleHqosPolicyMapQueueControlRDMiniThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 131072),
    )


_SleHqosPolicyMapQueueControlRDMiniThreshold_Type.__name__ = "Integer32"
_SleHqosPolicyMapQueueControlRDMiniThreshold_Object = MibScalar
sleHqosPolicyMapQueueControlRDMiniThreshold = _SleHqosPolicyMapQueueControlRDMiniThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 2, 11),
    _SleHqosPolicyMapQueueControlRDMiniThreshold_Type()
)
sleHqosPolicyMapQueueControlRDMiniThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueControlRDMiniThreshold.setStatus("current")


class _SleHqosPolicyMapQueueControlRDMaxThreshold_Type(Integer32):
    """Custom type sleHqosPolicyMapQueueControlRDMaxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 131072),
    )


_SleHqosPolicyMapQueueControlRDMaxThreshold_Type.__name__ = "Integer32"
_SleHqosPolicyMapQueueControlRDMaxThreshold_Object = MibScalar
sleHqosPolicyMapQueueControlRDMaxThreshold = _SleHqosPolicyMapQueueControlRDMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 2, 12),
    _SleHqosPolicyMapQueueControlRDMaxThreshold_Type()
)
sleHqosPolicyMapQueueControlRDMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueControlRDMaxThreshold.setStatus("current")


class _SleHqosPolicyMapQueueControlRDMinimumUnits_Type(Integer32):
    """Custom type sleHqosPolicyMapQueueControlRDMinimumUnits based on Integer32"""
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
        *(("bytes", 1),
          ("kbytes", 2),
          ("packets", 3),
          ("percent", 4))
    )


_SleHqosPolicyMapQueueControlRDMinimumUnits_Type.__name__ = "Integer32"
_SleHqosPolicyMapQueueControlRDMinimumUnits_Object = MibScalar
sleHqosPolicyMapQueueControlRDMinimumUnits = _SleHqosPolicyMapQueueControlRDMinimumUnits_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 2, 13),
    _SleHqosPolicyMapQueueControlRDMinimumUnits_Type()
)
sleHqosPolicyMapQueueControlRDMinimumUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueControlRDMinimumUnits.setStatus("current")


class _SleHqosPolicyMapQueueControlRDMaximumUnits_Type(Integer32):
    """Custom type sleHqosPolicyMapQueueControlRDMaximumUnits based on Integer32"""
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
        *(("bytes", 1),
          ("kbytes", 2),
          ("packets", 3),
          ("percent", 4))
    )


_SleHqosPolicyMapQueueControlRDMaximumUnits_Type.__name__ = "Integer32"
_SleHqosPolicyMapQueueControlRDMaximumUnits_Object = MibScalar
sleHqosPolicyMapQueueControlRDMaximumUnits = _SleHqosPolicyMapQueueControlRDMaximumUnits_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 2, 14),
    _SleHqosPolicyMapQueueControlRDMaximumUnits_Type()
)
sleHqosPolicyMapQueueControlRDMaximumUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueControlRDMaximumUnits.setStatus("current")


class _SleHqosPolicyMapQueueControlServicePolicyName_Type(SnmpAdminString):
    """Custom type sleHqosPolicyMapQueueControlServicePolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SleHqosPolicyMapQueueControlServicePolicyName_Type.__name__ = "SnmpAdminString"
_SleHqosPolicyMapQueueControlServicePolicyName_Object = MibScalar
sleHqosPolicyMapQueueControlServicePolicyName = _SleHqosPolicyMapQueueControlServicePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 10, 2, 15),
    _SleHqosPolicyMapQueueControlServicePolicyName_Type()
)
sleHqosPolicyMapQueueControlServicePolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHqosPolicyMapQueueControlServicePolicyName.setStatus("current")
_SleMlsQosAclGlobal_ObjectIdentity = ObjectIdentity
sleMlsQosAclGlobal = _SleMlsQosAclGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 11)
)
_SleMlsQosAclGlobalInfo_ObjectIdentity = ObjectIdentity
sleMlsQosAclGlobalInfo = _SleMlsQosAclGlobalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 11, 1)
)
_SleMlsQosAclGlobalInfoMaxAccessList_Type = Unsigned32
_SleMlsQosAclGlobalInfoMaxAccessList_Object = MibScalar
sleMlsQosAclGlobalInfoMaxAccessList = _SleMlsQosAclGlobalInfoMaxAccessList_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 11, 1, 1),
    _SleMlsQosAclGlobalInfoMaxAccessList_Type()
)
sleMlsQosAclGlobalInfoMaxAccessList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosAclGlobalInfoMaxAccessList.setStatus("current")
_SleMlsQosAclGlobalControl_ObjectIdentity = ObjectIdentity
sleMlsQosAclGlobalControl = _SleMlsQosAclGlobalControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 11, 2)
)


class _SleMlsQosAclGlobalControlRequest_Type(Integer32):
    """Custom type sleMlsQosAclGlobalControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setMaxAccessList", 1),
          ("unsetMaxAccessList", 2))
    )


_SleMlsQosAclGlobalControlRequest_Type.__name__ = "Integer32"
_SleMlsQosAclGlobalControlRequest_Object = MibScalar
sleMlsQosAclGlobalControlRequest = _SleMlsQosAclGlobalControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 11, 2, 1),
    _SleMlsQosAclGlobalControlRequest_Type()
)
sleMlsQosAclGlobalControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosAclGlobalControlRequest.setStatus("current")
_SleMlsQosAclGlobalControlStatus_Type = SleControlStatusType
_SleMlsQosAclGlobalControlStatus_Object = MibScalar
sleMlsQosAclGlobalControlStatus = _SleMlsQosAclGlobalControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 11, 2, 2),
    _SleMlsQosAclGlobalControlStatus_Type()
)
sleMlsQosAclGlobalControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosAclGlobalControlStatus.setStatus("current")
_SleMlsQosAclGlobalControlTimer_Type = Gauge32
_SleMlsQosAclGlobalControlTimer_Object = MibScalar
sleMlsQosAclGlobalControlTimer = _SleMlsQosAclGlobalControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 11, 2, 3),
    _SleMlsQosAclGlobalControlTimer_Type()
)
sleMlsQosAclGlobalControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosAclGlobalControlTimer.setStatus("current")
_SleMlsQosAclGlobalControlTimeStamp_Type = TimeTicks
_SleMlsQosAclGlobalControlTimeStamp_Object = MibScalar
sleMlsQosAclGlobalControlTimeStamp = _SleMlsQosAclGlobalControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 11, 2, 4),
    _SleMlsQosAclGlobalControlTimeStamp_Type()
)
sleMlsQosAclGlobalControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosAclGlobalControlTimeStamp.setStatus("current")
_SleMlsQosAclGlobalControlReqResult_Type = SleControlRequestResultType
_SleMlsQosAclGlobalControlReqResult_Object = MibScalar
sleMlsQosAclGlobalControlReqResult = _SleMlsQosAclGlobalControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 11, 2, 5),
    _SleMlsQosAclGlobalControlReqResult_Type()
)
sleMlsQosAclGlobalControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMlsQosAclGlobalControlReqResult.setStatus("current")
_SleMlsQosAclGlobalControlMaxAccessList_Type = Unsigned32
_SleMlsQosAclGlobalControlMaxAccessList_Object = MibScalar
sleMlsQosAclGlobalControlMaxAccessList = _SleMlsQosAclGlobalControlMaxAccessList_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 11, 2, 6),
    _SleMlsQosAclGlobalControlMaxAccessList_Type()
)
sleMlsQosAclGlobalControlMaxAccessList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMlsQosAclGlobalControlMaxAccessList.setStatus("current")

# Managed Objects groups

sleMlsQosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 28, 12)
)
sleMlsQosGroup.setObjects(
      *(("SLE-MLSQOS-MIB", "sleMlsQosStatus"),
        ("SLE-MLSQOS-MIB", "sleMlsQosMapCosToCos"),
        ("SLE-MLSQOS-MIB", "sleMlsQosMapCosToQueue"),
        ("SLE-MLSQOS-MIB", "sleMlsQosMapDscpToDscp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosMapDscpToQueue"),
        ("SLE-MLSQOS-MIB", "sleMlsQosMapExpToExp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosMapExpToQueue"),
        ("SLE-MLSQOS-MIB", "sleMlsQosMapStrictQueueId"),
        ("SLE-MLSQOS-MIB", "sleMlsQosMapWrrQueueWeight"),
        ("SLE-MLSQOS-MIB", "sleMlsQosMapCpuMaxPpsRate"),
        ("SLE-MLSQOS-MIB", "sleMlsQosMapCpuQueueWeight"),
        ("SLE-MLSQOS-MIB", "sleMlsQosMapNodeCpuMaxPpsRate"),
        ("SLE-MLSQOS-MIB", "sleMlsQosMapNodeCpuQueueWeight"),
        ("SLE-MLSQOS-MIB", "sleMlsQosMapExpToClass"),
        ("SLE-MLSQOS-MIB", "sleHQosStatistics"),
        ("SLE-MLSQOS-MIB", "sleQosPhbPriorityColor"),
        ("SLE-MLSQOS-MIB", "sleHQosDefaultClassToDscp"),
        ("SLE-MLSQOS-MIB", "sleQosDefaultCosToClassTrust"),
        ("SLE-MLSQOS-MIB", "sleQosDefaultCosToClassNoTrust"),
        ("SLE-MLSQOS-MIB", "sleQosDefaultDscpToClassTrust"),
        ("SLE-MLSQOS-MIB", "sleQosDefaultDscpToClassNoTrust"),
        ("SLE-MLSQOS-MIB", "sleMlsQosGlobalControlRequest"),
        ("SLE-MLSQOS-MIB", "sleMlsQosGlobalControlStatus"),
        ("SLE-MLSQOS-MIB", "sleMlsQosGlobalCtrlTimer"),
        ("SLE-MLSQOS-MIB", "sleMlsQosGlobalControlTimeStamp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosGlobalControlReqResult"),
        ("SLE-MLSQOS-MIB", "sleMlsQosCtrlGlobalStatus"),
        ("SLE-MLSQOS-MIB", "sleMlsQosGlobalControlMappingType"),
        ("SLE-MLSQOS-MIB", "sleMlsQosGlobalControlMappingIngValue"),
        ("SLE-MLSQOS-MIB", "sleMlsQosGlobalControlMappingEgrValue"),
        ("SLE-MLSQOS-MIB", "sleMlsQosGlobalControlQueueId"),
        ("SLE-MLSQOS-MIB", "sleMlsQosGlobalControlWrrQueueWeight"),
        ("SLE-MLSQOS-MIB", "sleMlsQosGlobalControlCpuMaxPpsRate"),
        ("SLE-MLSQOS-MIB", "sleMlsQosGlobalControlCpuQueueWt"),
        ("SLE-MLSQOS-MIB", "sleMlsQosGlobalControlNodeId"),
        ("SLE-MLSQOS-MIB", "sleMlsQosGlobalControlMappingEgrClassValue"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAggPoliceIndex"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAggPoliceName"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAggPoliceTrafficRate"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAggPoliceBurstSize"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAggPoliceCtrlRequest"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAggPoliceCtrlStatus"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAggPoliceConfigCtrlTimer"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAggPoliceCtrlTimeStamp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAggPoliceCtrlReqResult"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAggPoliceCtrlName"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAggPoliceCtrlTrafficRate"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAggPoliceCtrlBurstSize"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLIndex"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLFilterIndex"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLName"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLMatchType"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLMatchAction"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLEtherType"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLL3Protocol"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLSrcIpAddress"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLDstIpAddress"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLSrcIpAddrMask"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLDstIpAddrMask"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLSrcMacAddress"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLDstMacAddress"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLSrcMacAddrMask"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLDstMacAddrMask"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLTcpUdpSrcPortAction"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLTcpUdpDstPortAction"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLTcpUdpSrcPort"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLTcpUdpDstPort"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLNameSrcIpExactMatch"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLActionRemarkDesc"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLIcmpType"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLIcmpCode"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLTcpUdpSrcPortEnd"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLTcpUdpDstPortEnd"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLControlRequest"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLControlStatus"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLConfigControlTimer"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLControlTimeStamp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLControlReqResult"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlName"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlMatchType"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlMatchAction"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlEtherType"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlL3Protocol"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlSrcAddress"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlDstAddress"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlSrcAddrMask"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlDstAddrMask"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlTcpUdpSrcPortAction"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlTcpUdpDstPortAction"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlTcpUdpSrcPort"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlTcpUdpDstPort"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlAclNameExactMatch"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlActionRemarkDesc"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlIcmpType"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlIcmpCode"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlTcpUdpSrcPortEnd"),
        ("SLE-MLSQOS-MIB", "sleMlsQosACLCtrlTcpUdpDstPortEnd"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapName"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchCosValue"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchInnerCosValue"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchEgressInterface"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchEtherType"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchSrcIpAddr"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchDstIpAddr"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchSrcIpMaskLen"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchDstIpMaskLen"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchSrcIpV6Addr"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchDstIpV6Addr"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchSrcIpV6MaskLen"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchDstIpV6MaskLen"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchIpDscp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchIpPrecedence"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchIp6Dscp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchIp6Precedence"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchTcpSrcPort"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchTcpDstPort"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchTcpSrcPortRange"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchTcpDstPortRange"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchUdpSrcPort"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchUdpDstPort"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchUdpSrcPortRange"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchUdpDstPortRange"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchSrcMacAddr"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchSrcMacMask"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchDstMacAddr"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchDstMacMask"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchVlanId"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchVlanIdRange"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchInnerVlanId"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchVlanTpid"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchAccessGroup"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchLayer4SrcPort"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchLayer4DstPort"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchLayer4SrcPortRange"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapMatchLayer4DstPortRange"),
        ("SLE-MLSQOS-MIB", "sleMplsQosClassMapMatchCriteria"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapControlRequest"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapControlStatus"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapControlTimer"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapontrolTimeStamp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapControlReqResult"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapCtrlName"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapCtrlMatchType"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapCtrlMatchVal"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapCtrlMatchRangeType"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapCtrlMatchRangeLow"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapCtrlMatchRangeHigh"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapCtrlMatchEtherType"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapCtrlMatchSrcType"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapCtrlMatchSrcAddr"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapCtrlMatchDstAddr"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapCtrlMatchSrcIpMaskLen"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapCtrlMatchDstIpMaskLen"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapCtrlMatchSrcMacMask"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapCtrlMatchDstMacMask"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapCtrlMatchAcessGroup"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapCtrlMatchVlanTpid"),
        ("SLE-MLSQOS-MIB", "sleMlsQosClassMapCtrlMatchEgressInterface"),
        ("SLE-MLSQOS-MIB", "sleMplsQosClassMapCtrlMatchCriteria"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapName"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassName"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassMatchPriority"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassOperMode"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassPoliceType"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassPoliceCIR"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassPolicePIR"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassPoliceCBS"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassPoliceEBS"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassPoliceExdAction"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassPoliceExdActionCos"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassPoliceExdActionDscp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassPoliceExdActionTos"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassPoliceExdActionViolateAction"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassPoliceExdActionViolateValue"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassPoliceAggregateName"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassSetActionDeny"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassSetActionCos"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassSetActionCpuCos"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassSetActionIpDscp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassSetActionIp6Dscp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassSetActionIpPrecedence"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassSetActionIp6Precedence"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassSetActionMirrorToPortVal"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassSetActionRedirectToPortVal"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassSetActionVlanId"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassSetActionVlanCos"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPmapClassSetActionQosGroup"),
        ("SLE-MLSQOS-MIB", "sleMplsQosPmapClassSetActionQueue"),
        ("SLE-MLSQOS-MIB", "sleMplsQosPmapClassSetActionCopyCpu"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapControlRequest"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapControlStatus"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapControlTimer"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapontrolTimeStamp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapControlReqResult"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlName"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassName"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassMatchPriority"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassOperMode"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassPoliceType"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassPoliceCIR"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassPolicePIR"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassPoliceCBS"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassPoliceEBS"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassPoliceExdAction"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassPoliceExdActionCos"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassPoliceExdActionDscp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassPoliceExdActionTos"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassPoliceExdActionViolateAction"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassPoliceExdActionViolateValue"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassPoliceAggregateName"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassSetAction"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassSetActionCos"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassSetActionCpuCos"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassSetActionIpDscp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassSetActionIp6Dscp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassSetActionIpPrecedence"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassSetActionIp6Precedence"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassSetActionMirrorToPort"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassSetActionRedirectToPort"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassSetActionVlanId"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassSetActionVlanCos"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassSetActionQosGroup"),
        ("SLE-MLSQOS-MIB", "sleMlsQosPolicyMapCtrlClassSetActionQueue"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceIndex"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceName"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceTrustState"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceCos"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceCosOverride"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceCosToCos"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceCosToQueue"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceDscp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceDscpToDscp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceDscpToQueue"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceExpToExp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceTrafficShapeRate"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceTrafficShapeBurst"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceInputPolicyMap"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceOutputPolicyMap"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceTrustPassthroughCos"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceTrustPassthroughDscp"),
        ("SLE-MLSQOS-MIB", "sleHQosInterfaceCosToClass"),
        ("SLE-MLSQOS-MIB", "sleHQosInterfaceDscpToClass"),
        ("SLE-MLSQOS-MIB", "sleHQosInterfaceReplace"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceTrafficIfgExclude"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceTrafficPolicingRate"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceTrafficPolicingBurst"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceControlRequest"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceControlStatus"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceControlTimer"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceontrolTimeStamp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceControlReqResult"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceCtrlIndex"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceCtrlMapingType"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceCtrlMapingIngVal"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceCtrlMapingEgrVal"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceCtrlMapingCosOverride"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceCtrlMapingTrustState"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceCtrlTrafficShapeRate"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceCtrlTrafficShapeBurst"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceCtrlInputPolicyMap"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceCtrlOutputPolicyMap"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceCtrlMapingCNGValue"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceCtrlMapingEgrClassVal"),
        ("SLE-MLSQOS-MIB", "sleMlsQosInterfaceCtrlReplace"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueIntfIndex"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueId"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueShapeQueueRate"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueWrrQueueWeight"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueWrrRandomDetectMinThr"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueWrrRandomDetectMaxThr"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueWrrRandomDetectExpWt"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueTailDropThr"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueStrictQueue"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueRandomDetectDropStart"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueRandomDetectDropSlope"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueRandomDetectColor"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueReservedBandwidth"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueControlRequest"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueControlStatus"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueControlTimer"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueontrolTimeStamp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueControlReqResult"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueCtrlInterfaceIndex"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueCtrlQueueId"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueCtrlProfileType"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueCtrlShapeQueueRate"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueCtrlWrrQueueWeight"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueCtrlWrrRandomDetectMinThr"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueCtrlWrrRandomDetectMaxThr"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueCtrlWrrRandomDetectExpWt"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueCtrlTailDropThr"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueCtrlRandomDetectDropStart"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueCtrlRandomDetectDropSlope"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueCtrlRandomDetectColor"),
        ("SLE-MLSQOS-MIB", "sleMlsQosIntfQueCtrlReservedBandwidth"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQstatsIfIndex"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQId"),
        ("SLE-MLSQOS-MIB", "sleMlsQosWredGreenDropPkts"),
        ("SLE-MLSQOS-MIB", "sleMlsQosWredYellowDropPkts"),
        ("SLE-MLSQOS-MIB", "sleMlsQosWredRedDropPkts"),
        ("SLE-MLSQOS-MIB", "sleMlsQosTailDropPkts"),
        ("SLE-MLSQOS-MIB", "sleMlsQosTailDropBytes"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQStatsOutPkts"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQStatsOutBytes"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQStatsMcastOutPkts"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQStatsMcastOutBytes"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQStatsDropPkts"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQStatsDropBytes"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQStatsMcastDropPkts"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQStatsMcastDropBytes"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQStatsEnqueuedPkts"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQStatsEnqueuedBytes"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQStatsControlRequest"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQStatsControlStatus"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQStatsControlTimer"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQStatsontrolTimeStamp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQStatsControlReqResult"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQstatsCtrlIfIndex"),
        ("SLE-MLSQOS-MIB", "sleMlsQosQstatsCtrlQId"),
        ("SLE-MLSQOS-MIB", "sleHqosClassMapQueueInfoName"),
        ("SLE-MLSQOS-MIB", "sleHqosClassMapQueueInfoMatchGroup"),
        ("SLE-MLSQOS-MIB", "sleHqosClassMapQueueControlRequest"),
        ("SLE-MLSQOS-MIB", "sleHqosClassMapQueueControlStatus"),
        ("SLE-MLSQOS-MIB", "sleHqosClassMapQueueControlTimer"),
        ("SLE-MLSQOS-MIB", "sleHqosClassMapQueueControlTimeStamp"),
        ("SLE-MLSQOS-MIB", "sleHqosClassMapQueueControlReqResult"),
        ("SLE-MLSQOS-MIB", "sleHqosClassMapQueueControlName"),
        ("SLE-MLSQOS-MIB", "sleHqosClassMapQueueControlMatchGroup"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueInfoName"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueInfoShape"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueInfoBandwidth"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueInfoBandwidthRemainingPercent"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueInfoQueueLimit"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueInfoServicePolicyName"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueInfoPriority"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueInfoRDMinThreshold"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueInfoRDMaxThreshold"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueControlRequest"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueControlStatus"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueControlTimer"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueControlTimeStamp"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueControlReqResult"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueControlName"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueControlClassMapQueueName"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueControlParams"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueControlParamsValue"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueControlUnits"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueControlRDMiniThreshold"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueControlRDMaxThreshold"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueControlRDMinimumUnits"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueControlRDMaximumUnits"),
        ("SLE-MLSQOS-MIB", "sleHqosPolicyMapQueueControlServicePolicyName"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAclGlobalInfoMaxAccessList"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAclGlobalControlRequest"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAclGlobalControlStatus"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAclGlobalControlTimer"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAclGlobalControlTimeStamp"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAclGlobalControlReqResult"),
        ("SLE-MLSQOS-MIB", "sleMlsQosAclGlobalControlMaxAccessList"))
)
if mibBuilder.loadTexts:
    sleMlsQosGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-MLSQOS-MIB",
    **{"MlsQosStatusType": MlsQosStatusType,
       "MlsQosMappingType": MlsQosMappingType,
       "ACLMatchType": ACLMatchType,
       "ACLMatchActionType": ACLMatchActionType,
       "ACLEtherType": ACLEtherType,
       "AclTcpUdpPortActionType": AclTcpUdpPortActionType,
       "ClassMapMatchType": ClassMapMatchType,
       "ClassMapMatchRangeType": ClassMapMatchRangeType,
       "PmapPriorityType": PmapPriorityType,
       "PmapPoliceType": PmapPoliceType,
       "PmapExceedActionType": PmapExceedActionType,
       "PmapViolateActionType": PmapViolateActionType,
       "PmapSetActionType": PmapSetActionType,
       "MlsQosIntfTrustState": MlsQosIntfTrustState,
       "MlsQosInterfaceMapingType": MlsQosInterfaceMapingType,
       "MlsQosIntfQueProfilingType": MlsQosIntfQueProfilingType,
       "ACLMacType": ACLMacType,
       "ACLIpType": ACLIpType,
       "PolMapClassMatchPrioType": PolMapClassMatchPrioType,
       "PoliceExceedActionType": PoliceExceedActionType,
       "sleMlsQos": sleMlsQos,
       "sleMlsQosGlobal": sleMlsQosGlobal,
       "sleMlsQosGlobalInfo": sleMlsQosGlobalInfo,
       "sleMlsQosStatus": sleMlsQosStatus,
       "sleMlsQosMapCosToCos": sleMlsQosMapCosToCos,
       "sleMlsQosMapCosToQueue": sleMlsQosMapCosToQueue,
       "sleMlsQosMapDscpToDscp": sleMlsQosMapDscpToDscp,
       "sleMlsQosMapDscpToQueue": sleMlsQosMapDscpToQueue,
       "sleMlsQosMapExpToExp": sleMlsQosMapExpToExp,
       "sleMlsQosMapExpToQueue": sleMlsQosMapExpToQueue,
       "sleMlsQosMapStrictQueueId": sleMlsQosMapStrictQueueId,
       "sleMlsQosMapWrrQueueWeight": sleMlsQosMapWrrQueueWeight,
       "sleMlsQosMapCpuMaxPpsRate": sleMlsQosMapCpuMaxPpsRate,
       "sleMlsQosMapCpuQueueWeight": sleMlsQosMapCpuQueueWeight,
       "sleMlsQosMapNodeCpuMaxPpsRate": sleMlsQosMapNodeCpuMaxPpsRate,
       "sleMlsQosMapNodeCpuQueueWeight": sleMlsQosMapNodeCpuQueueWeight,
       "sleMlsQosMapExpToClass": sleMlsQosMapExpToClass,
       "sleHQosStatistics": sleHQosStatistics,
       "sleQosPhbPriorityColor": sleQosPhbPriorityColor,
       "sleHQosDefaultClassToDscp": sleHQosDefaultClassToDscp,
       "sleQosDefaultCosToClassTrust": sleQosDefaultCosToClassTrust,
       "sleQosDefaultCosToClassNoTrust": sleQosDefaultCosToClassNoTrust,
       "sleQosDefaultDscpToClassTrust": sleQosDefaultDscpToClassTrust,
       "sleQosDefaultDscpToClassNoTrust": sleQosDefaultDscpToClassNoTrust,
       "sleMlsQosGlobalControl": sleMlsQosGlobalControl,
       "sleMlsQosGlobalControlRequest": sleMlsQosGlobalControlRequest,
       "sleMlsQosGlobalControlStatus": sleMlsQosGlobalControlStatus,
       "sleMlsQosGlobalCtrlTimer": sleMlsQosGlobalCtrlTimer,
       "sleMlsQosGlobalControlTimeStamp": sleMlsQosGlobalControlTimeStamp,
       "sleMlsQosGlobalControlReqResult": sleMlsQosGlobalControlReqResult,
       "sleMlsQosCtrlGlobalStatus": sleMlsQosCtrlGlobalStatus,
       "sleMlsQosGlobalControlMappingType": sleMlsQosGlobalControlMappingType,
       "sleMlsQosGlobalControlMappingIngValue": sleMlsQosGlobalControlMappingIngValue,
       "sleMlsQosGlobalControlMappingEgrValue": sleMlsQosGlobalControlMappingEgrValue,
       "sleMlsQosGlobalControlQueueId": sleMlsQosGlobalControlQueueId,
       "sleMlsQosGlobalControlWrrQueueWeight": sleMlsQosGlobalControlWrrQueueWeight,
       "sleMlsQosGlobalControlCpuMaxPpsRate": sleMlsQosGlobalControlCpuMaxPpsRate,
       "sleMlsQosGlobalControlCpuQueueWt": sleMlsQosGlobalControlCpuQueueWt,
       "sleMlsQosGlobalControlNodeId": sleMlsQosGlobalControlNodeId,
       "sleMlsQosGlobalControlMappingEgrClassValue": sleMlsQosGlobalControlMappingEgrClassValue,
       "sleMlsQosAggPolice": sleMlsQosAggPolice,
       "sleMlsQosAggPoliceTable": sleMlsQosAggPoliceTable,
       "sleMlsQosAggPoliceEntry": sleMlsQosAggPoliceEntry,
       "sleMlsQosAggPoliceIndex": sleMlsQosAggPoliceIndex,
       "sleMlsQosAggPoliceName": sleMlsQosAggPoliceName,
       "sleMlsQosAggPoliceTrafficRate": sleMlsQosAggPoliceTrafficRate,
       "sleMlsQosAggPoliceBurstSize": sleMlsQosAggPoliceBurstSize,
       "sleMlsQosAggPoliceControl": sleMlsQosAggPoliceControl,
       "sleMlsQosAggPoliceCtrlRequest": sleMlsQosAggPoliceCtrlRequest,
       "sleMlsQosAggPoliceCtrlStatus": sleMlsQosAggPoliceCtrlStatus,
       "sleMlsQosAggPoliceConfigCtrlTimer": sleMlsQosAggPoliceConfigCtrlTimer,
       "sleMlsQosAggPoliceCtrlTimeStamp": sleMlsQosAggPoliceCtrlTimeStamp,
       "sleMlsQosAggPoliceCtrlReqResult": sleMlsQosAggPoliceCtrlReqResult,
       "sleMlsQosAggPoliceCtrlName": sleMlsQosAggPoliceCtrlName,
       "sleMlsQosAggPoliceCtrlTrafficRate": sleMlsQosAggPoliceCtrlTrafficRate,
       "sleMlsQosAggPoliceCtrlBurstSize": sleMlsQosAggPoliceCtrlBurstSize,
       "sleMlsQosACL": sleMlsQosACL,
       "sleMlsQosACLTable": sleMlsQosACLTable,
       "sleMlsQosACLEntry": sleMlsQosACLEntry,
       "sleMlsQosACLIndex": sleMlsQosACLIndex,
       "sleMlsQosACLFilterIndex": sleMlsQosACLFilterIndex,
       "sleMlsQosACLName": sleMlsQosACLName,
       "sleMlsQosACLMatchType": sleMlsQosACLMatchType,
       "sleMlsQosACLMatchAction": sleMlsQosACLMatchAction,
       "sleMlsQosACLEtherType": sleMlsQosACLEtherType,
       "sleMlsQosACLL3Protocol": sleMlsQosACLL3Protocol,
       "sleMlsQosACLSrcIpAddress": sleMlsQosACLSrcIpAddress,
       "sleMlsQosACLDstIpAddress": sleMlsQosACLDstIpAddress,
       "sleMlsQosACLSrcIpAddrMask": sleMlsQosACLSrcIpAddrMask,
       "sleMlsQosACLDstIpAddrMask": sleMlsQosACLDstIpAddrMask,
       "sleMlsQosACLSrcMacAddress": sleMlsQosACLSrcMacAddress,
       "sleMlsQosACLDstMacAddress": sleMlsQosACLDstMacAddress,
       "sleMlsQosACLSrcMacAddrMask": sleMlsQosACLSrcMacAddrMask,
       "sleMlsQosACLDstMacAddrMask": sleMlsQosACLDstMacAddrMask,
       "sleMlsQosACLTcpUdpSrcPortAction": sleMlsQosACLTcpUdpSrcPortAction,
       "sleMlsQosACLTcpUdpDstPortAction": sleMlsQosACLTcpUdpDstPortAction,
       "sleMlsQosACLTcpUdpSrcPort": sleMlsQosACLTcpUdpSrcPort,
       "sleMlsQosACLTcpUdpDstPort": sleMlsQosACLTcpUdpDstPort,
       "sleMlsQosACLNameSrcIpExactMatch": sleMlsQosACLNameSrcIpExactMatch,
       "sleMlsQosACLActionRemarkDesc": sleMlsQosACLActionRemarkDesc,
       "sleMlsQosACLIcmpType": sleMlsQosACLIcmpType,
       "sleMlsQosACLIcmpCode": sleMlsQosACLIcmpCode,
       "sleMlsQosACLTcpUdpSrcPortEnd": sleMlsQosACLTcpUdpSrcPortEnd,
       "sleMlsQosACLTcpUdpDstPortEnd": sleMlsQosACLTcpUdpDstPortEnd,
       "sleMlsQosACLControl": sleMlsQosACLControl,
       "sleMlsQosACLControlRequest": sleMlsQosACLControlRequest,
       "sleMlsQosACLControlStatus": sleMlsQosACLControlStatus,
       "sleMlsQosACLConfigControlTimer": sleMlsQosACLConfigControlTimer,
       "sleMlsQosACLControlTimeStamp": sleMlsQosACLControlTimeStamp,
       "sleMlsQosACLControlReqResult": sleMlsQosACLControlReqResult,
       "sleMlsQosACLCtrlName": sleMlsQosACLCtrlName,
       "sleMlsQosACLCtrlMatchType": sleMlsQosACLCtrlMatchType,
       "sleMlsQosACLCtrlMatchAction": sleMlsQosACLCtrlMatchAction,
       "sleMlsQosACLCtrlEtherType": sleMlsQosACLCtrlEtherType,
       "sleMlsQosACLCtrlL3Protocol": sleMlsQosACLCtrlL3Protocol,
       "sleMlsQosACLCtrlSrcAddress": sleMlsQosACLCtrlSrcAddress,
       "sleMlsQosACLCtrlDstAddress": sleMlsQosACLCtrlDstAddress,
       "sleMlsQosACLCtrlSrcAddrMask": sleMlsQosACLCtrlSrcAddrMask,
       "sleMlsQosACLCtrlDstAddrMask": sleMlsQosACLCtrlDstAddrMask,
       "sleMlsQosACLCtrlTcpUdpSrcPortAction": sleMlsQosACLCtrlTcpUdpSrcPortAction,
       "sleMlsQosACLCtrlTcpUdpDstPortAction": sleMlsQosACLCtrlTcpUdpDstPortAction,
       "sleMlsQosACLCtrlTcpUdpSrcPort": sleMlsQosACLCtrlTcpUdpSrcPort,
       "sleMlsQosACLCtrlTcpUdpDstPort": sleMlsQosACLCtrlTcpUdpDstPort,
       "sleMlsQosACLCtrlAclNameExactMatch": sleMlsQosACLCtrlAclNameExactMatch,
       "sleMlsQosACLCtrlActionRemarkDesc": sleMlsQosACLCtrlActionRemarkDesc,
       "sleMlsQosACLCtrlIcmpType": sleMlsQosACLCtrlIcmpType,
       "sleMlsQosACLCtrlIcmpCode": sleMlsQosACLCtrlIcmpCode,
       "sleMlsQosACLCtrlTcpUdpSrcPortEnd": sleMlsQosACLCtrlTcpUdpSrcPortEnd,
       "sleMlsQosACLCtrlTcpUdpDstPortEnd": sleMlsQosACLCtrlTcpUdpDstPortEnd,
       "sleMlsQosACLNotification": sleMlsQosACLNotification,
       "sleMlsQosClassMap": sleMlsQosClassMap,
       "sleMlsQosClassMapTable": sleMlsQosClassMapTable,
       "sleMlsQosClassMapEntry": sleMlsQosClassMapEntry,
       "sleMlsQosClassMapName": sleMlsQosClassMapName,
       "sleMlsQosClassMapMatchCosValue": sleMlsQosClassMapMatchCosValue,
       "sleMlsQosClassMapMatchInnerCosValue": sleMlsQosClassMapMatchInnerCosValue,
       "sleMlsQosClassMapMatchEgressInterface": sleMlsQosClassMapMatchEgressInterface,
       "sleMlsQosClassMapMatchEtherType": sleMlsQosClassMapMatchEtherType,
       "sleMlsQosClassMapMatchSrcIpAddr": sleMlsQosClassMapMatchSrcIpAddr,
       "sleMlsQosClassMapMatchDstIpAddr": sleMlsQosClassMapMatchDstIpAddr,
       "sleMlsQosClassMapMatchSrcIpMaskLen": sleMlsQosClassMapMatchSrcIpMaskLen,
       "sleMlsQosClassMapMatchDstIpMaskLen": sleMlsQosClassMapMatchDstIpMaskLen,
       "sleMlsQosClassMapMatchSrcIpV6Addr": sleMlsQosClassMapMatchSrcIpV6Addr,
       "sleMlsQosClassMapMatchDstIpV6Addr": sleMlsQosClassMapMatchDstIpV6Addr,
       "sleMlsQosClassMapMatchSrcIpV6MaskLen": sleMlsQosClassMapMatchSrcIpV6MaskLen,
       "sleMlsQosClassMapMatchDstIpV6MaskLen": sleMlsQosClassMapMatchDstIpV6MaskLen,
       "sleMlsQosClassMapMatchIpDscp": sleMlsQosClassMapMatchIpDscp,
       "sleMlsQosClassMapMatchIpPrecedence": sleMlsQosClassMapMatchIpPrecedence,
       "sleMlsQosClassMapMatchIp6Dscp": sleMlsQosClassMapMatchIp6Dscp,
       "sleMlsQosClassMapMatchIp6Precedence": sleMlsQosClassMapMatchIp6Precedence,
       "sleMlsQosClassMapMatchTcpSrcPort": sleMlsQosClassMapMatchTcpSrcPort,
       "sleMlsQosClassMapMatchTcpDstPort": sleMlsQosClassMapMatchTcpDstPort,
       "sleMlsQosClassMapMatchTcpSrcPortRange": sleMlsQosClassMapMatchTcpSrcPortRange,
       "sleMlsQosClassMapMatchTcpDstPortRange": sleMlsQosClassMapMatchTcpDstPortRange,
       "sleMlsQosClassMapMatchUdpSrcPort": sleMlsQosClassMapMatchUdpSrcPort,
       "sleMlsQosClassMapMatchUdpDstPort": sleMlsQosClassMapMatchUdpDstPort,
       "sleMlsQosClassMapMatchUdpSrcPortRange": sleMlsQosClassMapMatchUdpSrcPortRange,
       "sleMlsQosClassMapMatchUdpDstPortRange": sleMlsQosClassMapMatchUdpDstPortRange,
       "sleMlsQosClassMapMatchSrcMacAddr": sleMlsQosClassMapMatchSrcMacAddr,
       "sleMlsQosClassMapMatchSrcMacMask": sleMlsQosClassMapMatchSrcMacMask,
       "sleMlsQosClassMapMatchDstMacAddr": sleMlsQosClassMapMatchDstMacAddr,
       "sleMlsQosClassMapMatchDstMacMask": sleMlsQosClassMapMatchDstMacMask,
       "sleMlsQosClassMapMatchVlanId": sleMlsQosClassMapMatchVlanId,
       "sleMlsQosClassMapMatchVlanIdRange": sleMlsQosClassMapMatchVlanIdRange,
       "sleMlsQosClassMapMatchInnerVlanId": sleMlsQosClassMapMatchInnerVlanId,
       "sleMlsQosClassMapMatchVlanTpid": sleMlsQosClassMapMatchVlanTpid,
       "sleMlsQosClassMapMatchAccessGroup": sleMlsQosClassMapMatchAccessGroup,
       "sleMlsQosClassMapMatchLayer4SrcPort": sleMlsQosClassMapMatchLayer4SrcPort,
       "sleMlsQosClassMapMatchLayer4DstPort": sleMlsQosClassMapMatchLayer4DstPort,
       "sleMlsQosClassMapMatchLayer4SrcPortRange": sleMlsQosClassMapMatchLayer4SrcPortRange,
       "sleMlsQosClassMapMatchLayer4DstPortRange": sleMlsQosClassMapMatchLayer4DstPortRange,
       "sleMplsQosClassMapMatchCriteria": sleMplsQosClassMapMatchCriteria,
       "sleMlsQosClassMapControl": sleMlsQosClassMapControl,
       "sleMlsQosClassMapControlRequest": sleMlsQosClassMapControlRequest,
       "sleMlsQosClassMapControlStatus": sleMlsQosClassMapControlStatus,
       "sleMlsQosClassMapControlTimer": sleMlsQosClassMapControlTimer,
       "sleMlsQosClassMapontrolTimeStamp": sleMlsQosClassMapontrolTimeStamp,
       "sleMlsQosClassMapControlReqResult": sleMlsQosClassMapControlReqResult,
       "sleMlsQosClassMapCtrlName": sleMlsQosClassMapCtrlName,
       "sleMlsQosClassMapCtrlMatchType": sleMlsQosClassMapCtrlMatchType,
       "sleMlsQosClassMapCtrlMatchVal": sleMlsQosClassMapCtrlMatchVal,
       "sleMlsQosClassMapCtrlMatchRangeType": sleMlsQosClassMapCtrlMatchRangeType,
       "sleMlsQosClassMapCtrlMatchRangeLow": sleMlsQosClassMapCtrlMatchRangeLow,
       "sleMlsQosClassMapCtrlMatchRangeHigh": sleMlsQosClassMapCtrlMatchRangeHigh,
       "sleMlsQosClassMapCtrlMatchEtherType": sleMlsQosClassMapCtrlMatchEtherType,
       "sleMlsQosClassMapCtrlMatchSrcType": sleMlsQosClassMapCtrlMatchSrcType,
       "sleMlsQosClassMapCtrlMatchSrcAddr": sleMlsQosClassMapCtrlMatchSrcAddr,
       "sleMlsQosClassMapCtrlMatchDstAddr": sleMlsQosClassMapCtrlMatchDstAddr,
       "sleMlsQosClassMapCtrlMatchSrcIpMaskLen": sleMlsQosClassMapCtrlMatchSrcIpMaskLen,
       "sleMlsQosClassMapCtrlMatchDstIpMaskLen": sleMlsQosClassMapCtrlMatchDstIpMaskLen,
       "sleMlsQosClassMapCtrlMatchSrcMacMask": sleMlsQosClassMapCtrlMatchSrcMacMask,
       "sleMlsQosClassMapCtrlMatchDstMacMask": sleMlsQosClassMapCtrlMatchDstMacMask,
       "sleMlsQosClassMapCtrlMatchAcessGroup": sleMlsQosClassMapCtrlMatchAcessGroup,
       "sleMlsQosClassMapCtrlMatchVlanTpid": sleMlsQosClassMapCtrlMatchVlanTpid,
       "sleMlsQosClassMapCtrlMatchEgressInterface": sleMlsQosClassMapCtrlMatchEgressInterface,
       "sleMplsQosClassMapCtrlMatchCriteria": sleMplsQosClassMapCtrlMatchCriteria,
       "sleMlsQosClassMapNotification": sleMlsQosClassMapNotification,
       "sleMlsQosPolicyMap": sleMlsQosPolicyMap,
       "sleMlsQosPolicyMapTable": sleMlsQosPolicyMapTable,
       "sleMlsQosPolicyMapEntry": sleMlsQosPolicyMapEntry,
       "sleMlsQosPmapName": sleMlsQosPmapName,
       "sleMlsQosPmapClassName": sleMlsQosPmapClassName,
       "sleMlsQosPmapClassMatchPriority": sleMlsQosPmapClassMatchPriority,
       "sleMlsQosPmapClassOperMode": sleMlsQosPmapClassOperMode,
       "sleMlsQosPmapClassPoliceType": sleMlsQosPmapClassPoliceType,
       "sleMlsQosPmapClassPoliceCIR": sleMlsQosPmapClassPoliceCIR,
       "sleMlsQosPmapClassPolicePIR": sleMlsQosPmapClassPolicePIR,
       "sleMlsQosPmapClassPoliceCBS": sleMlsQosPmapClassPoliceCBS,
       "sleMlsQosPmapClassPoliceEBS": sleMlsQosPmapClassPoliceEBS,
       "sleMlsQosPmapClassPoliceExdAction": sleMlsQosPmapClassPoliceExdAction,
       "sleMlsQosPmapClassPoliceExdActionCos": sleMlsQosPmapClassPoliceExdActionCos,
       "sleMlsQosPmapClassPoliceExdActionDscp": sleMlsQosPmapClassPoliceExdActionDscp,
       "sleMlsQosPmapClassPoliceExdActionTos": sleMlsQosPmapClassPoliceExdActionTos,
       "sleMlsQosPmapClassPoliceExdActionViolateAction": sleMlsQosPmapClassPoliceExdActionViolateAction,
       "sleMlsQosPmapClassPoliceExdActionViolateValue": sleMlsQosPmapClassPoliceExdActionViolateValue,
       "sleMlsQosPmapClassPoliceAggregateName": sleMlsQosPmapClassPoliceAggregateName,
       "sleMlsQosPmapClassSetActionDeny": sleMlsQosPmapClassSetActionDeny,
       "sleMlsQosPmapClassSetActionCos": sleMlsQosPmapClassSetActionCos,
       "sleMlsQosPmapClassSetActionCpuCos": sleMlsQosPmapClassSetActionCpuCos,
       "sleMlsQosPmapClassSetActionIpDscp": sleMlsQosPmapClassSetActionIpDscp,
       "sleMlsQosPmapClassSetActionIp6Dscp": sleMlsQosPmapClassSetActionIp6Dscp,
       "sleMlsQosPmapClassSetActionIpPrecedence": sleMlsQosPmapClassSetActionIpPrecedence,
       "sleMlsQosPmapClassSetActionIp6Precedence": sleMlsQosPmapClassSetActionIp6Precedence,
       "sleMlsQosPmapClassSetActionMirrorToPortVal": sleMlsQosPmapClassSetActionMirrorToPortVal,
       "sleMlsQosPmapClassSetActionRedirectToPortVal": sleMlsQosPmapClassSetActionRedirectToPortVal,
       "sleMlsQosPmapClassSetActionVlanId": sleMlsQosPmapClassSetActionVlanId,
       "sleMlsQosPmapClassSetActionVlanCos": sleMlsQosPmapClassSetActionVlanCos,
       "sleMlsQosPmapClassSetActionQosGroup": sleMlsQosPmapClassSetActionQosGroup,
       "sleMplsQosPmapClassSetActionQueue": sleMplsQosPmapClassSetActionQueue,
       "sleMplsQosPmapClassSetActionCopyCpu": sleMplsQosPmapClassSetActionCopyCpu,
       "sleMlsQosPolicyMapControl": sleMlsQosPolicyMapControl,
       "sleMlsQosPolicyMapControlRequest": sleMlsQosPolicyMapControlRequest,
       "sleMlsQosPolicyMapControlStatus": sleMlsQosPolicyMapControlStatus,
       "sleMlsQosPolicyMapControlTimer": sleMlsQosPolicyMapControlTimer,
       "sleMlsQosPolicyMapontrolTimeStamp": sleMlsQosPolicyMapontrolTimeStamp,
       "sleMlsQosPolicyMapControlReqResult": sleMlsQosPolicyMapControlReqResult,
       "sleMlsQosPolicyMapCtrlName": sleMlsQosPolicyMapCtrlName,
       "sleMlsQosPolicyMapCtrlClassName": sleMlsQosPolicyMapCtrlClassName,
       "sleMlsQosPolicyMapCtrlClassMatchPriority": sleMlsQosPolicyMapCtrlClassMatchPriority,
       "sleMlsQosPolicyMapCtrlClassOperMode": sleMlsQosPolicyMapCtrlClassOperMode,
       "sleMlsQosPolicyMapCtrlClassPoliceType": sleMlsQosPolicyMapCtrlClassPoliceType,
       "sleMlsQosPolicyMapCtrlClassPoliceCIR": sleMlsQosPolicyMapCtrlClassPoliceCIR,
       "sleMlsQosPolicyMapCtrlClassPolicePIR": sleMlsQosPolicyMapCtrlClassPolicePIR,
       "sleMlsQosPolicyMapCtrlClassPoliceCBS": sleMlsQosPolicyMapCtrlClassPoliceCBS,
       "sleMlsQosPolicyMapCtrlClassPoliceEBS": sleMlsQosPolicyMapCtrlClassPoliceEBS,
       "sleMlsQosPolicyMapCtrlClassPoliceExdAction": sleMlsQosPolicyMapCtrlClassPoliceExdAction,
       "sleMlsQosPolicyMapCtrlClassPoliceExdActionCos": sleMlsQosPolicyMapCtrlClassPoliceExdActionCos,
       "sleMlsQosPolicyMapCtrlClassPoliceExdActionDscp": sleMlsQosPolicyMapCtrlClassPoliceExdActionDscp,
       "sleMlsQosPolicyMapCtrlClassPoliceExdActionTos": sleMlsQosPolicyMapCtrlClassPoliceExdActionTos,
       "sleMlsQosPolicyMapCtrlClassPoliceExdActionViolateAction": sleMlsQosPolicyMapCtrlClassPoliceExdActionViolateAction,
       "sleMlsQosPolicyMapCtrlClassPoliceExdActionViolateValue": sleMlsQosPolicyMapCtrlClassPoliceExdActionViolateValue,
       "sleMlsQosPolicyMapCtrlClassPoliceAggregateName": sleMlsQosPolicyMapCtrlClassPoliceAggregateName,
       "sleMlsQosPolicyMapCtrlClassSetAction": sleMlsQosPolicyMapCtrlClassSetAction,
       "sleMlsQosPolicyMapCtrlClassSetActionCos": sleMlsQosPolicyMapCtrlClassSetActionCos,
       "sleMlsQosPolicyMapCtrlClassSetActionCpuCos": sleMlsQosPolicyMapCtrlClassSetActionCpuCos,
       "sleMlsQosPolicyMapCtrlClassSetActionIpDscp": sleMlsQosPolicyMapCtrlClassSetActionIpDscp,
       "sleMlsQosPolicyMapCtrlClassSetActionIp6Dscp": sleMlsQosPolicyMapCtrlClassSetActionIp6Dscp,
       "sleMlsQosPolicyMapCtrlClassSetActionIpPrecedence": sleMlsQosPolicyMapCtrlClassSetActionIpPrecedence,
       "sleMlsQosPolicyMapCtrlClassSetActionIp6Precedence": sleMlsQosPolicyMapCtrlClassSetActionIp6Precedence,
       "sleMlsQosPolicyMapCtrlClassSetActionMirrorToPort": sleMlsQosPolicyMapCtrlClassSetActionMirrorToPort,
       "sleMlsQosPolicyMapCtrlClassSetActionRedirectToPort": sleMlsQosPolicyMapCtrlClassSetActionRedirectToPort,
       "sleMlsQosPolicyMapCtrlClassSetActionVlanId": sleMlsQosPolicyMapCtrlClassSetActionVlanId,
       "sleMlsQosPolicyMapCtrlClassSetActionVlanCos": sleMlsQosPolicyMapCtrlClassSetActionVlanCos,
       "sleMlsQosPolicyMapCtrlClassSetActionQosGroup": sleMlsQosPolicyMapCtrlClassSetActionQosGroup,
       "sleMlsQosPolicyMapCtrlClassSetActionQueue": sleMlsQosPolicyMapCtrlClassSetActionQueue,
       "sleMlsQosInterface": sleMlsQosInterface,
       "sleMlsQosInterfaceTable": sleMlsQosInterfaceTable,
       "sleMlsQosInterfaceEntry": sleMlsQosInterfaceEntry,
       "sleMlsQosInterfaceIndex": sleMlsQosInterfaceIndex,
       "sleMlsQosInterfaceName": sleMlsQosInterfaceName,
       "sleMlsQosInterfaceTrustState": sleMlsQosInterfaceTrustState,
       "sleMlsQosInterfaceCos": sleMlsQosInterfaceCos,
       "sleMlsQosInterfaceCosOverride": sleMlsQosInterfaceCosOverride,
       "sleMlsQosInterfaceCosToCos": sleMlsQosInterfaceCosToCos,
       "sleMlsQosInterfaceCosToQueue": sleMlsQosInterfaceCosToQueue,
       "sleMlsQosInterfaceDscp": sleMlsQosInterfaceDscp,
       "sleMlsQosInterfaceDscpToDscp": sleMlsQosInterfaceDscpToDscp,
       "sleMlsQosInterfaceDscpToQueue": sleMlsQosInterfaceDscpToQueue,
       "sleMlsQosInterfaceExpToExp": sleMlsQosInterfaceExpToExp,
       "sleMlsQosInterfaceTrafficShapeRate": sleMlsQosInterfaceTrafficShapeRate,
       "sleMlsQosInterfaceTrafficShapeBurst": sleMlsQosInterfaceTrafficShapeBurst,
       "sleMlsQosInterfaceInputPolicyMap": sleMlsQosInterfaceInputPolicyMap,
       "sleMlsQosInterfaceOutputPolicyMap": sleMlsQosInterfaceOutputPolicyMap,
       "sleMlsQosInterfaceTrustPassthroughCos": sleMlsQosInterfaceTrustPassthroughCos,
       "sleMlsQosInterfaceTrustPassthroughDscp": sleMlsQosInterfaceTrustPassthroughDscp,
       "sleHQosInterfaceCosToClass": sleHQosInterfaceCosToClass,
       "sleHQosInterfaceDscpToClass": sleHQosInterfaceDscpToClass,
       "sleHQosInterfaceReplace": sleHQosInterfaceReplace,
       "sleMlsQosInterfaceTrafficIfgExclude": sleMlsQosInterfaceTrafficIfgExclude,
       "sleMlsQosInterfaceTrafficPolicingRate": sleMlsQosInterfaceTrafficPolicingRate,
       "sleMlsQosInterfaceTrafficPolicingBurst": sleMlsQosInterfaceTrafficPolicingBurst,
       "sleMlsQosInterfaceControl": sleMlsQosInterfaceControl,
       "sleMlsQosInterfaceControlRequest": sleMlsQosInterfaceControlRequest,
       "sleMlsQosInterfaceControlStatus": sleMlsQosInterfaceControlStatus,
       "sleMlsQosInterfaceControlTimer": sleMlsQosInterfaceControlTimer,
       "sleMlsQosInterfaceontrolTimeStamp": sleMlsQosInterfaceontrolTimeStamp,
       "sleMlsQosInterfaceControlReqResult": sleMlsQosInterfaceControlReqResult,
       "sleMlsQosInterfaceCtrlIndex": sleMlsQosInterfaceCtrlIndex,
       "sleMlsQosInterfaceCtrlMapingType": sleMlsQosInterfaceCtrlMapingType,
       "sleMlsQosInterfaceCtrlMapingIngVal": sleMlsQosInterfaceCtrlMapingIngVal,
       "sleMlsQosInterfaceCtrlMapingEgrVal": sleMlsQosInterfaceCtrlMapingEgrVal,
       "sleMlsQosInterfaceCtrlMapingCosOverride": sleMlsQosInterfaceCtrlMapingCosOverride,
       "sleMlsQosInterfaceCtrlMapingTrustState": sleMlsQosInterfaceCtrlMapingTrustState,
       "sleMlsQosInterfaceCtrlTrafficShapeRate": sleMlsQosInterfaceCtrlTrafficShapeRate,
       "sleMlsQosInterfaceCtrlTrafficShapeBurst": sleMlsQosInterfaceCtrlTrafficShapeBurst,
       "sleMlsQosInterfaceCtrlInputPolicyMap": sleMlsQosInterfaceCtrlInputPolicyMap,
       "sleMlsQosInterfaceCtrlOutputPolicyMap": sleMlsQosInterfaceCtrlOutputPolicyMap,
       "sleMlsQosInterfaceCtrlMapingCNGValue": sleMlsQosInterfaceCtrlMapingCNGValue,
       "sleMlsQosInterfaceCtrlMapingEgrClassVal": sleMlsQosInterfaceCtrlMapingEgrClassVal,
       "sleMlsQosInterfaceCtrlReplace": sleMlsQosInterfaceCtrlReplace,
       "sleMlsQosIntfQue": sleMlsQosIntfQue,
       "sleMlsQosIntfQueTable": sleMlsQosIntfQueTable,
       "sleMlsQosIntfQueEntry": sleMlsQosIntfQueEntry,
       "sleMlsQosIntfQueIntfIndex": sleMlsQosIntfQueIntfIndex,
       "sleMlsQosIntfQueId": sleMlsQosIntfQueId,
       "sleMlsQosIntfQueShapeQueueRate": sleMlsQosIntfQueShapeQueueRate,
       "sleMlsQosIntfQueWrrQueueWeight": sleMlsQosIntfQueWrrQueueWeight,
       "sleMlsQosIntfQueWrrRandomDetectMinThr": sleMlsQosIntfQueWrrRandomDetectMinThr,
       "sleMlsQosIntfQueWrrRandomDetectMaxThr": sleMlsQosIntfQueWrrRandomDetectMaxThr,
       "sleMlsQosIntfQueWrrRandomDetectExpWt": sleMlsQosIntfQueWrrRandomDetectExpWt,
       "sleMlsQosIntfQueTailDropThr": sleMlsQosIntfQueTailDropThr,
       "sleMlsQosIntfQueStrictQueue": sleMlsQosIntfQueStrictQueue,
       "sleMlsQosIntfQueRandomDetectDropStart": sleMlsQosIntfQueRandomDetectDropStart,
       "sleMlsQosIntfQueRandomDetectDropSlope": sleMlsQosIntfQueRandomDetectDropSlope,
       "sleMlsQosIntfQueRandomDetectColor": sleMlsQosIntfQueRandomDetectColor,
       "sleMlsQosIntfQueReservedBandwidth": sleMlsQosIntfQueReservedBandwidth,
       "sleMlsQosIntfQueControl": sleMlsQosIntfQueControl,
       "sleMlsQosIntfQueControlRequest": sleMlsQosIntfQueControlRequest,
       "sleMlsQosIntfQueControlStatus": sleMlsQosIntfQueControlStatus,
       "sleMlsQosIntfQueControlTimer": sleMlsQosIntfQueControlTimer,
       "sleMlsQosIntfQueontrolTimeStamp": sleMlsQosIntfQueontrolTimeStamp,
       "sleMlsQosIntfQueControlReqResult": sleMlsQosIntfQueControlReqResult,
       "sleMlsQosIntfQueCtrlInterfaceIndex": sleMlsQosIntfQueCtrlInterfaceIndex,
       "sleMlsQosIntfQueCtrlQueueId": sleMlsQosIntfQueCtrlQueueId,
       "sleMlsQosIntfQueCtrlProfileType": sleMlsQosIntfQueCtrlProfileType,
       "sleMlsQosIntfQueCtrlShapeQueueRate": sleMlsQosIntfQueCtrlShapeQueueRate,
       "sleMlsQosIntfQueCtrlWrrQueueWeight": sleMlsQosIntfQueCtrlWrrQueueWeight,
       "sleMlsQosIntfQueCtrlWrrRandomDetectMinThr": sleMlsQosIntfQueCtrlWrrRandomDetectMinThr,
       "sleMlsQosIntfQueCtrlWrrRandomDetectMaxThr": sleMlsQosIntfQueCtrlWrrRandomDetectMaxThr,
       "sleMlsQosIntfQueCtrlWrrRandomDetectExpWt": sleMlsQosIntfQueCtrlWrrRandomDetectExpWt,
       "sleMlsQosIntfQueCtrlTailDropThr": sleMlsQosIntfQueCtrlTailDropThr,
       "sleMlsQosIntfQueCtrlRandomDetectDropStart": sleMlsQosIntfQueCtrlRandomDetectDropStart,
       "sleMlsQosIntfQueCtrlRandomDetectDropSlope": sleMlsQosIntfQueCtrlRandomDetectDropSlope,
       "sleMlsQosIntfQueCtrlRandomDetectColor": sleMlsQosIntfQueCtrlRandomDetectColor,
       "sleMlsQosIntfQueCtrlReservedBandwidth": sleMlsQosIntfQueCtrlReservedBandwidth,
       "sleMlsQosQStats": sleMlsQosQStats,
       "sleMlsQosQStatsTable": sleMlsQosQStatsTable,
       "sleMlsQosQStatsEntry": sleMlsQosQStatsEntry,
       "sleMlsQosQstatsIfIndex": sleMlsQosQstatsIfIndex,
       "sleMlsQosQId": sleMlsQosQId,
       "sleMlsQosWredGreenDropPkts": sleMlsQosWredGreenDropPkts,
       "sleMlsQosWredYellowDropPkts": sleMlsQosWredYellowDropPkts,
       "sleMlsQosWredRedDropPkts": sleMlsQosWredRedDropPkts,
       "sleMlsQosTailDropPkts": sleMlsQosTailDropPkts,
       "sleMlsQosTailDropBytes": sleMlsQosTailDropBytes,
       "sleMlsQosQStatsOutPkts": sleMlsQosQStatsOutPkts,
       "sleMlsQosQStatsOutBytes": sleMlsQosQStatsOutBytes,
       "sleMlsQosQStatsMcastOutPkts": sleMlsQosQStatsMcastOutPkts,
       "sleMlsQosQStatsMcastOutBytes": sleMlsQosQStatsMcastOutBytes,
       "sleMlsQosQStatsDropPkts": sleMlsQosQStatsDropPkts,
       "sleMlsQosQStatsDropBytes": sleMlsQosQStatsDropBytes,
       "sleMlsQosQStatsMcastDropPkts": sleMlsQosQStatsMcastDropPkts,
       "sleMlsQosQStatsMcastDropBytes": sleMlsQosQStatsMcastDropBytes,
       "sleMlsQosQStatsEnqueuedPkts": sleMlsQosQStatsEnqueuedPkts,
       "sleMlsQosQStatsEnqueuedBytes": sleMlsQosQStatsEnqueuedBytes,
       "sleMlsQosQStatsControl": sleMlsQosQStatsControl,
       "sleMlsQosQStatsControlRequest": sleMlsQosQStatsControlRequest,
       "sleMlsQosQStatsControlStatus": sleMlsQosQStatsControlStatus,
       "sleMlsQosQStatsControlTimer": sleMlsQosQStatsControlTimer,
       "sleMlsQosQStatsontrolTimeStamp": sleMlsQosQStatsontrolTimeStamp,
       "sleMlsQosQStatsControlReqResult": sleMlsQosQStatsControlReqResult,
       "sleMlsQosQstatsCtrlIfIndex": sleMlsQosQstatsCtrlIfIndex,
       "sleMlsQosQstatsCtrlQId": sleMlsQosQstatsCtrlQId,
       "sleHqosClassMapQueue": sleHqosClassMapQueue,
       "sleHqosClassMapQueueInfoTable": sleHqosClassMapQueueInfoTable,
       "sleHqosClassMapQueueInfoEntry": sleHqosClassMapQueueInfoEntry,
       "sleHqosClassMapQueueInfoName": sleHqosClassMapQueueInfoName,
       "sleHqosClassMapQueueInfoMatchGroup": sleHqosClassMapQueueInfoMatchGroup,
       "sleHqosClassMapQueueControl": sleHqosClassMapQueueControl,
       "sleHqosClassMapQueueControlRequest": sleHqosClassMapQueueControlRequest,
       "sleHqosClassMapQueueControlStatus": sleHqosClassMapQueueControlStatus,
       "sleHqosClassMapQueueControlTimer": sleHqosClassMapQueueControlTimer,
       "sleHqosClassMapQueueControlTimeStamp": sleHqosClassMapQueueControlTimeStamp,
       "sleHqosClassMapQueueControlReqResult": sleHqosClassMapQueueControlReqResult,
       "sleHqosClassMapQueueControlName": sleHqosClassMapQueueControlName,
       "sleHqosClassMapQueueControlMatchGroup": sleHqosClassMapQueueControlMatchGroup,
       "sleHqosPolicyMapQueue": sleHqosPolicyMapQueue,
       "sleHqosPolicyMapQueueInfoTable": sleHqosPolicyMapQueueInfoTable,
       "sleHqosPolicyMapQueueInfoEntry": sleHqosPolicyMapQueueInfoEntry,
       "sleHqosPolicyMapQueueInfoName": sleHqosPolicyMapQueueInfoName,
       "sleHqosPolicyMapQueueInfoShape": sleHqosPolicyMapQueueInfoShape,
       "sleHqosPolicyMapQueueInfoBandwidth": sleHqosPolicyMapQueueInfoBandwidth,
       "sleHqosPolicyMapQueueInfoBandwidthRemainingPercent": sleHqosPolicyMapQueueInfoBandwidthRemainingPercent,
       "sleHqosPolicyMapQueueInfoQueueLimit": sleHqosPolicyMapQueueInfoQueueLimit,
       "sleHqosPolicyMapQueueInfoServicePolicyName": sleHqosPolicyMapQueueInfoServicePolicyName,
       "sleHqosPolicyMapQueueInfoPriority": sleHqosPolicyMapQueueInfoPriority,
       "sleHqosPolicyMapQueueInfoRDMinThreshold": sleHqosPolicyMapQueueInfoRDMinThreshold,
       "sleHqosPolicyMapQueueInfoRDMaxThreshold": sleHqosPolicyMapQueueInfoRDMaxThreshold,
       "sleHqosPolicyMapQueueControl": sleHqosPolicyMapQueueControl,
       "sleHqosPolicyMapQueueControlRequest": sleHqosPolicyMapQueueControlRequest,
       "sleHqosPolicyMapQueueControlStatus": sleHqosPolicyMapQueueControlStatus,
       "sleHqosPolicyMapQueueControlTimer": sleHqosPolicyMapQueueControlTimer,
       "sleHqosPolicyMapQueueControlTimeStamp": sleHqosPolicyMapQueueControlTimeStamp,
       "sleHqosPolicyMapQueueControlReqResult": sleHqosPolicyMapQueueControlReqResult,
       "sleHqosPolicyMapQueueControlName": sleHqosPolicyMapQueueControlName,
       "sleHqosPolicyMapQueueControlClassMapQueueName": sleHqosPolicyMapQueueControlClassMapQueueName,
       "sleHqosPolicyMapQueueControlParams": sleHqosPolicyMapQueueControlParams,
       "sleHqosPolicyMapQueueControlParamsValue": sleHqosPolicyMapQueueControlParamsValue,
       "sleHqosPolicyMapQueueControlUnits": sleHqosPolicyMapQueueControlUnits,
       "sleHqosPolicyMapQueueControlRDMiniThreshold": sleHqosPolicyMapQueueControlRDMiniThreshold,
       "sleHqosPolicyMapQueueControlRDMaxThreshold": sleHqosPolicyMapQueueControlRDMaxThreshold,
       "sleHqosPolicyMapQueueControlRDMinimumUnits": sleHqosPolicyMapQueueControlRDMinimumUnits,
       "sleHqosPolicyMapQueueControlRDMaximumUnits": sleHqosPolicyMapQueueControlRDMaximumUnits,
       "sleHqosPolicyMapQueueControlServicePolicyName": sleHqosPolicyMapQueueControlServicePolicyName,
       "sleMlsQosAclGlobal": sleMlsQosAclGlobal,
       "sleMlsQosAclGlobalInfo": sleMlsQosAclGlobalInfo,
       "sleMlsQosAclGlobalInfoMaxAccessList": sleMlsQosAclGlobalInfoMaxAccessList,
       "sleMlsQosAclGlobalControl": sleMlsQosAclGlobalControl,
       "sleMlsQosAclGlobalControlRequest": sleMlsQosAclGlobalControlRequest,
       "sleMlsQosAclGlobalControlStatus": sleMlsQosAclGlobalControlStatus,
       "sleMlsQosAclGlobalControlTimer": sleMlsQosAclGlobalControlTimer,
       "sleMlsQosAclGlobalControlTimeStamp": sleMlsQosAclGlobalControlTimeStamp,
       "sleMlsQosAclGlobalControlReqResult": sleMlsQosAclGlobalControlReqResult,
       "sleMlsQosAclGlobalControlMaxAccessList": sleMlsQosAclGlobalControlMaxAccessList,
       "sleMlsQosGroup": sleMlsQosGroup}
)
