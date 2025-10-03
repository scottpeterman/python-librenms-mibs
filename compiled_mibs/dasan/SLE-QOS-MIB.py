# SNMP MIB module (SLE-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-QOS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:58 2025
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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleQoS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10)
)


# Types definitions



class SleTrafficProfileControlRequestType(Integer32):
    """Custom type SleTrafficProfileControlRequestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setTrafficProfile", 1)
    )





class SleUserFlowMatchType(Bits):
    """Custom type SleUserFlowMatchType based on Bits"""
    namedValues = NamedValues(
        *(("ufIngressPort", 0),
          ("ufEgressPort", 1),
          ("ufEthernetType", 2),
          ("ufSrcMacAddress", 3),
          ("ufDstMacAddress", 4),
          ("ufVlanId", 5),
          ("uf8021p", 6),
          ("ufSrcIpAddress", 7),
          ("ufSrcPrefixLength", 8),
          ("ufDstIpAddress", 9),
          ("ufDstPrefixLength", 10),
          ("ufDscp", 11),
          ("ufProtocolType", 12),
          ("ufTcpFlag", 13),
          ("ufSrcL4Port", 14),
          ("ufDstL4Port", 15),
          ("ufPacketLength", 16))
    )




class SleUserFlowActionType(Bits):
    """Custom type SleUserFlowActionType based on Bits"""
    namedValues = NamedValues(
        *(("ufActPermit", 0),
          ("ufActCopyCpu", 1),
          ("ufActSameAsTos", 2),
          ("ufActSameAsCos", 3),
          ("ufActMirror", 4))
    )




class SleBooleanType(Integer32):
    """Custom type SleBooleanType based on Integer32"""
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





class SlePortScheduleControlRequestType(Integer32):
    """Custom type SlePortScheduleControlRequestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setPortScheduleMode", 1)
    )





class SleQueueControlRequestType(Integer32):
    """Custom type SleQueueControlRequestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setQueueProfile", 1)
    )





class SleUserFlowControlRequestType(Integer32):
    """Custom type SleUserFlowControlRequestType based on Integer32"""
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
        *(("createUserFlow", 1),
          ("destroyUserFlow", 2),
          ("setUserFlowClassifierProfile", 3),
          ("setUserFlowMatchActionProfile", 4),
          ("setUserFlowNomatchActionProfile", 5))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleQoSBase_ObjectIdentity = ObjectIdentity
sleQoSBase = _SleQoSBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 1)
)
_SleQoSBaseInfo_ObjectIdentity = ObjectIdentity
sleQoSBaseInfo = _SleQoSBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 1, 1)
)
_SleQosUserFlowNum_Type = Unsigned32
_SleQosUserFlowNum_Object = MibScalar
sleQosUserFlowNum = _SleQosUserFlowNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 1, 1, 1),
    _SleQosUserFlowNum_Type()
)
sleQosUserFlowNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQosUserFlowNum.setStatus("current")
_SleQosTrafficProfileNum_Type = Unsigned32
_SleQosTrafficProfileNum_Object = MibScalar
sleQosTrafficProfileNum = _SleQosTrafficProfileNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 1, 1, 2),
    _SleQosTrafficProfileNum_Type()
)
sleQosTrafficProfileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQosTrafficProfileNum.setStatus("current")
_SleQosCounterNum_Type = Unsigned32
_SleQosCounterNum_Object = MibScalar
sleQosCounterNum = _SleQosCounterNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 1, 1, 3),
    _SleQosCounterNum_Type()
)
sleQosCounterNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQosCounterNum.setStatus("current")
_SleQosQueueNum_Type = Unsigned32
_SleQosQueueNum_Object = MibScalar
sleQosQueueNum = _SleQosQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 1, 1, 4),
    _SleQosQueueNum_Type()
)
sleQosQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQosQueueNum.setStatus("current")
_SleQosColorMarkingProfileNum_Type = Integer32
_SleQosColorMarkingProfileNum_Object = MibScalar
sleQosColorMarkingProfileNum = _SleQosColorMarkingProfileNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 1, 1, 5),
    _SleQosColorMarkingProfileNum_Type()
)
sleQosColorMarkingProfileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQosColorMarkingProfileNum.setStatus("current")


class _SleQosRuleMode_Type(Integer32):
    """Custom type sleQosRuleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("extension", 1))
    )


_SleQosRuleMode_Type.__name__ = "Integer32"
_SleQosRuleMode_Object = MibScalar
sleQosRuleMode = _SleQosRuleMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 1, 1, 6),
    _SleQosRuleMode_Type()
)
sleQosRuleMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQosRuleMode.setStatus("current")
_SleQoSBaseControl_ObjectIdentity = ObjectIdentity
sleQoSBaseControl = _SleQoSBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 1, 2)
)


class _SleQoSBaseControlRequest_Type(Integer32):
    """Custom type sleQoSBaseControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setQoSBaseRuleMode", 1)
    )


_SleQoSBaseControlRequest_Type.__name__ = "Integer32"
_SleQoSBaseControlRequest_Object = MibScalar
sleQoSBaseControlRequest = _SleQoSBaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 1, 2, 1),
    _SleQoSBaseControlRequest_Type()
)
sleQoSBaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleQoSBaseControlRequest.setStatus("current")
_SleQoSBaseControlStatus_Type = SleControlStatusType
_SleQoSBaseControlStatus_Object = MibScalar
sleQoSBaseControlStatus = _SleQoSBaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 1, 2, 2),
    _SleQoSBaseControlStatus_Type()
)
sleQoSBaseControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQoSBaseControlStatus.setStatus("current")
_SleQoSBaseControlTimer_Type = Gauge32
_SleQoSBaseControlTimer_Object = MibScalar
sleQoSBaseControlTimer = _SleQoSBaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 1, 2, 3),
    _SleQoSBaseControlTimer_Type()
)
sleQoSBaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleQoSBaseControlTimer.setStatus("current")
_SleQoSBaseControlTimeStamp_Type = TimeTicks
_SleQoSBaseControlTimeStamp_Object = MibScalar
sleQoSBaseControlTimeStamp = _SleQoSBaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 1, 2, 4),
    _SleQoSBaseControlTimeStamp_Type()
)
sleQoSBaseControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQoSBaseControlTimeStamp.setStatus("current")
_SleQoSBaseControlReqResult_Type = SleControlRequestResultType
_SleQoSBaseControlReqResult_Object = MibScalar
sleQoSBaseControlReqResult = _SleQoSBaseControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 1, 2, 5),
    _SleQoSBaseControlReqResult_Type()
)
sleQoSBaseControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQoSBaseControlReqResult.setStatus("current")


class _SleQoSBaseControlRuleMode_Type(Integer32):
    """Custom type sleQoSBaseControlRuleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("extension", 1))
    )


_SleQoSBaseControlRuleMode_Type.__name__ = "Integer32"
_SleQoSBaseControlRuleMode_Object = MibScalar
sleQoSBaseControlRuleMode = _SleQoSBaseControlRuleMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 1, 2, 6),
    _SleQoSBaseControlRuleMode_Type()
)
sleQoSBaseControlRuleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleQoSBaseControlRuleMode.setStatus("current")
_SleQoSBaseNotification_ObjectIdentity = ObjectIdentity
sleQoSBaseNotification = _SleQoSBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 1, 3)
)
_SleTrafficProfile_ObjectIdentity = ObjectIdentity
sleTrafficProfile = _SleTrafficProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2)
)
_SleTrafficProfileTable_Object = MibTable
sleTrafficProfileTable = _SleTrafficProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 1)
)
if mibBuilder.loadTexts:
    sleTrafficProfileTable.setStatus("current")
_SleTrafficProfileEntry_Object = MibTableRow
sleTrafficProfileEntry = _SleTrafficProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 1, 1)
)
sleTrafficProfileEntry.setIndexNames(
    (0, "SLE-QOS-MIB", "sleTrafficProfileIndex"),
)
if mibBuilder.loadTexts:
    sleTrafficProfileEntry.setStatus("current")


class _SleTrafficProfileIndex_Type(Unsigned32):
    """Custom type sleTrafficProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleTrafficProfileIndex_Type.__name__ = "Unsigned32"
_SleTrafficProfileIndex_Object = MibTableColumn
sleTrafficProfileIndex = _SleTrafficProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 1, 1, 1),
    _SleTrafficProfileIndex_Type()
)
sleTrafficProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrafficProfileIndex.setStatus("current")
_SleTrafficProfileMinBandwidth_Type = Integer32
_SleTrafficProfileMinBandwidth_Object = MibTableColumn
sleTrafficProfileMinBandwidth = _SleTrafficProfileMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 1, 1, 2),
    _SleTrafficProfileMinBandwidth_Type()
)
sleTrafficProfileMinBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrafficProfileMinBandwidth.setStatus("current")
_SleTrafficProfileMaxBandwidth_Type = Integer32
_SleTrafficProfileMaxBandwidth_Object = MibTableColumn
sleTrafficProfileMaxBandwidth = _SleTrafficProfileMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 1, 1, 3),
    _SleTrafficProfileMaxBandwidth_Type()
)
sleTrafficProfileMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrafficProfileMaxBandwidth.setStatus("current")
_SleTrafficProfileMaxBurstSize_Type = Integer32
_SleTrafficProfileMaxBurstSize_Object = MibTableColumn
sleTrafficProfileMaxBurstSize = _SleTrafficProfileMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 1, 1, 4),
    _SleTrafficProfileMaxBurstSize_Type()
)
sleTrafficProfileMaxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrafficProfileMaxBurstSize.setStatus("current")
_SleTrafficProfileUseCount_Type = Integer32
_SleTrafficProfileUseCount_Object = MibTableColumn
sleTrafficProfileUseCount = _SleTrafficProfileUseCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 1, 1, 5),
    _SleTrafficProfileUseCount_Type()
)
sleTrafficProfileUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrafficProfileUseCount.setStatus("current")
_SleTrafficProfileControl_ObjectIdentity = ObjectIdentity
sleTrafficProfileControl = _SleTrafficProfileControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 2)
)
_SleTrafficProfileControlRequest_Type = SleTrafficProfileControlRequestType
_SleTrafficProfileControlRequest_Object = MibScalar
sleTrafficProfileControlRequest = _SleTrafficProfileControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 2, 1),
    _SleTrafficProfileControlRequest_Type()
)
sleTrafficProfileControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrafficProfileControlRequest.setStatus("current")
_SleTrafficProfileControlStatus_Type = SleControlStatusType
_SleTrafficProfileControlStatus_Object = MibScalar
sleTrafficProfileControlStatus = _SleTrafficProfileControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 2, 2),
    _SleTrafficProfileControlStatus_Type()
)
sleTrafficProfileControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrafficProfileControlStatus.setStatus("current")
_SleTrafficProfileControlTimer_Type = Gauge32
_SleTrafficProfileControlTimer_Object = MibScalar
sleTrafficProfileControlTimer = _SleTrafficProfileControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 2, 3),
    _SleTrafficProfileControlTimer_Type()
)
sleTrafficProfileControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrafficProfileControlTimer.setStatus("current")
_SleTrafficProfileControlTimeStamp_Type = TimeTicks
_SleTrafficProfileControlTimeStamp_Object = MibScalar
sleTrafficProfileControlTimeStamp = _SleTrafficProfileControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 2, 4),
    _SleTrafficProfileControlTimeStamp_Type()
)
sleTrafficProfileControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrafficProfileControlTimeStamp.setStatus("current")
_SleTrafficProfileControlReqResult_Type = SleControlRequestResultType
_SleTrafficProfileControlReqResult_Object = MibScalar
sleTrafficProfileControlReqResult = _SleTrafficProfileControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 2, 5),
    _SleTrafficProfileControlReqResult_Type()
)
sleTrafficProfileControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrafficProfileControlReqResult.setStatus("current")
_SleTrafficProfileControlIndex_Type = Integer32
_SleTrafficProfileControlIndex_Object = MibScalar
sleTrafficProfileControlIndex = _SleTrafficProfileControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 2, 6),
    _SleTrafficProfileControlIndex_Type()
)
sleTrafficProfileControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrafficProfileControlIndex.setStatus("current")
_SleTrafficProfileControlMinBandwidth_Type = Integer32
_SleTrafficProfileControlMinBandwidth_Object = MibScalar
sleTrafficProfileControlMinBandwidth = _SleTrafficProfileControlMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 2, 7),
    _SleTrafficProfileControlMinBandwidth_Type()
)
sleTrafficProfileControlMinBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrafficProfileControlMinBandwidth.setStatus("current")
_SleTrafficProfileControlMaxBandwidth_Type = Integer32
_SleTrafficProfileControlMaxBandwidth_Object = MibScalar
sleTrafficProfileControlMaxBandwidth = _SleTrafficProfileControlMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 2, 8),
    _SleTrafficProfileControlMaxBandwidth_Type()
)
sleTrafficProfileControlMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrafficProfileControlMaxBandwidth.setStatus("current")
_SleTrafficProfileControlMaxBurstSize_Type = Integer32
_SleTrafficProfileControlMaxBurstSize_Object = MibScalar
sleTrafficProfileControlMaxBurstSize = _SleTrafficProfileControlMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 2, 9),
    _SleTrafficProfileControlMaxBurstSize_Type()
)
sleTrafficProfileControlMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrafficProfileControlMaxBurstSize.setStatus("current")
_SleTrafficProfileNotification_ObjectIdentity = ObjectIdentity
sleTrafficProfileNotification = _SleTrafficProfileNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 3)
)
_SleUserFlow_ObjectIdentity = ObjectIdentity
sleUserFlow = _SleUserFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3)
)
_SleUserFlowTable_Object = MibTable
sleUserFlowTable = _SleUserFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1)
)
if mibBuilder.loadTexts:
    sleUserFlowTable.setStatus("current")
_SleUserFlowEntry_Object = MibTableRow
sleUserFlowEntry = _SleUserFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1)
)
sleUserFlowEntry.setIndexNames(
    (0, "SLE-QOS-MIB", "sleUserFlowName"),
)
if mibBuilder.loadTexts:
    sleUserFlowEntry.setStatus("current")


class _SleUserFlowName_Type(OctetString):
    """Custom type sleUserFlowName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_SleUserFlowName_Type.__name__ = "OctetString"
_SleUserFlowName_Object = MibTableColumn
sleUserFlowName = _SleUserFlowName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 1),
    _SleUserFlowName_Type()
)
sleUserFlowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowName.setStatus("current")
_SleUserFlowIngressPorts_Type = OctetString
_SleUserFlowIngressPorts_Object = MibTableColumn
sleUserFlowIngressPorts = _SleUserFlowIngressPorts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 2),
    _SleUserFlowIngressPorts_Type()
)
sleUserFlowIngressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowIngressPorts.setStatus("current")
_SleUserFlowEgressPorts_Type = OctetString
_SleUserFlowEgressPorts_Object = MibTableColumn
sleUserFlowEgressPorts = _SleUserFlowEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 3),
    _SleUserFlowEgressPorts_Type()
)
sleUserFlowEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowEgressPorts.setStatus("current")


class _SleUserFlowEthernetType_Type(Integer32):
    """Custom type sleUserFlowEthernetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleUserFlowEthernetType_Type.__name__ = "Integer32"
_SleUserFlowEthernetType_Object = MibTableColumn
sleUserFlowEthernetType = _SleUserFlowEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 4),
    _SleUserFlowEthernetType_Type()
)
sleUserFlowEthernetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowEthernetType.setStatus("current")


class _SleUserFlowSrcMacAddr_Type(OctetString):
    """Custom type sleUserFlowSrcMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_SleUserFlowSrcMacAddr_Type.__name__ = "OctetString"
_SleUserFlowSrcMacAddr_Object = MibTableColumn
sleUserFlowSrcMacAddr = _SleUserFlowSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 5),
    _SleUserFlowSrcMacAddr_Type()
)
sleUserFlowSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowSrcMacAddr.setStatus("current")


class _SleUserFlowDstMacAddr_Type(OctetString):
    """Custom type sleUserFlowDstMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_SleUserFlowDstMacAddr_Type.__name__ = "OctetString"
_SleUserFlowDstMacAddr_Object = MibTableColumn
sleUserFlowDstMacAddr = _SleUserFlowDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 6),
    _SleUserFlowDstMacAddr_Type()
)
sleUserFlowDstMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowDstMacAddr.setStatus("current")


class _SleUserFlowVlan_Type(Integer32):
    """Custom type sleUserFlowVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_SleUserFlowVlan_Type.__name__ = "Integer32"
_SleUserFlowVlan_Object = MibTableColumn
sleUserFlowVlan = _SleUserFlowVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 7),
    _SleUserFlowVlan_Type()
)
sleUserFlowVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowVlan.setStatus("current")


class _SleUserFlow8021p_Type(Integer32):
    """Custom type sleUserFlow8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleUserFlow8021p_Type.__name__ = "Integer32"
_SleUserFlow8021p_Object = MibTableColumn
sleUserFlow8021p = _SleUserFlow8021p_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 8),
    _SleUserFlow8021p_Type()
)
sleUserFlow8021p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlow8021p.setStatus("current")
_SleUserFlowSrcIpAddr_Type = IpAddress
_SleUserFlowSrcIpAddr_Object = MibTableColumn
sleUserFlowSrcIpAddr = _SleUserFlowSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 9),
    _SleUserFlowSrcIpAddr_Type()
)
sleUserFlowSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowSrcIpAddr.setStatus("current")


class _SleUserFlowSrcPrefixLength_Type(Integer32):
    """Custom type sleUserFlowSrcPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SleUserFlowSrcPrefixLength_Type.__name__ = "Integer32"
_SleUserFlowSrcPrefixLength_Object = MibTableColumn
sleUserFlowSrcPrefixLength = _SleUserFlowSrcPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 10),
    _SleUserFlowSrcPrefixLength_Type()
)
sleUserFlowSrcPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowSrcPrefixLength.setStatus("current")
_SleUserFlowDstIpAddr_Type = IpAddress
_SleUserFlowDstIpAddr_Object = MibTableColumn
sleUserFlowDstIpAddr = _SleUserFlowDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 11),
    _SleUserFlowDstIpAddr_Type()
)
sleUserFlowDstIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowDstIpAddr.setStatus("current")


class _SleUserFlowDstPrefixLength_Type(Integer32):
    """Custom type sleUserFlowDstPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleUserFlowDstPrefixLength_Type.__name__ = "Integer32"
_SleUserFlowDstPrefixLength_Object = MibTableColumn
sleUserFlowDstPrefixLength = _SleUserFlowDstPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 12),
    _SleUserFlowDstPrefixLength_Type()
)
sleUserFlowDstPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowDstPrefixLength.setStatus("current")


class _SleUserFlowIpPktPriorityType_Type(Integer32):
    """Custom type sleUserFlowIpPktPriorityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipPrecedence", 1),
          ("diffServ", 2),
          ("ipToS", 3))
    )


_SleUserFlowIpPktPriorityType_Type.__name__ = "Integer32"
_SleUserFlowIpPktPriorityType_Object = MibTableColumn
sleUserFlowIpPktPriorityType = _SleUserFlowIpPktPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 13),
    _SleUserFlowIpPktPriorityType_Type()
)
sleUserFlowIpPktPriorityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowIpPktPriorityType.setStatus("current")


class _SleUserFlowIpPktPriority_Type(Integer32):
    """Custom type sleUserFlowIpPktPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleUserFlowIpPktPriority_Type.__name__ = "Integer32"
_SleUserFlowIpPktPriority_Object = MibTableColumn
sleUserFlowIpPktPriority = _SleUserFlowIpPktPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 14),
    _SleUserFlowIpPktPriority_Type()
)
sleUserFlowIpPktPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowIpPktPriority.setStatus("current")


class _SleUserFlowProtocolType_Type(Integer32):
    """Custom type sleUserFlowProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleUserFlowProtocolType_Type.__name__ = "Integer32"
_SleUserFlowProtocolType_Object = MibTableColumn
sleUserFlowProtocolType = _SleUserFlowProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 15),
    _SleUserFlowProtocolType_Type()
)
sleUserFlowProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowProtocolType.setStatus("current")


class _SleUserFlowTcpFlag_Type(Bits):
    """Custom type sleUserFlowTcpFlag based on Bits"""
    namedValues = NamedValues(
        *(("reserv0", 0),
          ("reserv1", 1),
          ("urg", 2),
          ("ack", 3),
          ("psh", 4),
          ("rst", 5),
          ("syn", 6),
          ("fin", 7))
    )

_SleUserFlowTcpFlag_Type.__name__ = "Bits"
_SleUserFlowTcpFlag_Object = MibTableColumn
sleUserFlowTcpFlag = _SleUserFlowTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 16),
    _SleUserFlowTcpFlag_Type()
)
sleUserFlowTcpFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowTcpFlag.setStatus("current")


class _SleUserFlowSrcL4Port_Type(Integer32):
    """Custom type sleUserFlowSrcL4Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleUserFlowSrcL4Port_Type.__name__ = "Integer32"
_SleUserFlowSrcL4Port_Object = MibTableColumn
sleUserFlowSrcL4Port = _SleUserFlowSrcL4Port_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 17),
    _SleUserFlowSrcL4Port_Type()
)
sleUserFlowSrcL4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowSrcL4Port.setStatus("current")


class _SleUserFlowDstL4Port_Type(Integer32):
    """Custom type sleUserFlowDstL4Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleUserFlowDstL4Port_Type.__name__ = "Integer32"
_SleUserFlowDstL4Port_Object = MibTableColumn
sleUserFlowDstL4Port = _SleUserFlowDstL4Port_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 18),
    _SleUserFlowDstL4Port_Type()
)
sleUserFlowDstL4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowDstL4Port.setStatus("current")


class _SleUserFlowPktLen_Type(Integer32):
    """Custom type sleUserFlowPktLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(21, 65535),
    )


_SleUserFlowPktLen_Type.__name__ = "Integer32"
_SleUserFlowPktLen_Object = MibTableColumn
sleUserFlowPktLen = _SleUserFlowPktLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 19),
    _SleUserFlowPktLen_Type()
)
sleUserFlowPktLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowPktLen.setStatus("current")


class _SleUserFlowValidFlags_Type(Bits):
    """Custom type sleUserFlowValidFlags based on Bits"""
    namedValues = NamedValues(
        *(("ufIngressPort", 0),
          ("ufEgressPort", 1),
          ("ufEthernetType", 2),
          ("ufSrcMacAddress", 3),
          ("ufDstMacAddress", 4),
          ("ufVlanId", 5),
          ("uf8021p", 6),
          ("ufSrcIpAddress", 7),
          ("ufSrcPrefixLength", 8),
          ("ufDstIpAddress", 9),
          ("ufDstPrefixLength", 10),
          ("ufIpPktPriority", 11),
          ("ufProtocolType", 12),
          ("ufTcpFlag", 13),
          ("ufSrcL4Port", 14),
          ("ufDstL4Port", 15),
          ("ufPacketLength", 16),
          ("ufPriority", 17),
          ("ufInnerVlanId", 18),
          ("ufInner8021p", 19))
    )

_SleUserFlowValidFlags_Type.__name__ = "Bits"
_SleUserFlowValidFlags_Object = MibTableColumn
sleUserFlowValidFlags = _SleUserFlowValidFlags_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 20),
    _SleUserFlowValidFlags_Type()
)
sleUserFlowValidFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowValidFlags.setStatus("current")


class _SleUserFlowMatchFlags_Type(Bits):
    """Custom type sleUserFlowMatchFlags based on Bits"""
    namedValues = NamedValues(
        *(("ufIngressPort", 0),
          ("ufEgressPort", 1),
          ("ufEthernetType", 2),
          ("ufSrcMacAddress", 3),
          ("ufDstMacAddress", 4),
          ("ufVlanId", 5),
          ("uf8021p", 6),
          ("ufSrcIpAddress", 7),
          ("ufSrcPrefixLength", 8),
          ("ufDstIpAddress", 9),
          ("ufDstPrefixLength", 10),
          ("ufIpPktPriority", 11),
          ("ufProtocolType", 12),
          ("ufTcpFlag", 13),
          ("ufSrcL4Port", 14),
          ("ufDstL4Port", 15),
          ("ufPacketLength", 16),
          ("ufPriority", 17))
    )

_SleUserFlowMatchFlags_Type.__name__ = "Bits"
_SleUserFlowMatchFlags_Object = MibTableColumn
sleUserFlowMatchFlags = _SleUserFlowMatchFlags_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 21),
    _SleUserFlowMatchFlags_Type()
)
sleUserFlowMatchFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowMatchFlags.setStatus("current")


class _SleUserFlowPriority_Type(Integer32):
    """Custom type sleUserFlowPriority based on Integer32"""
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
          ("highest", 4))
    )


_SleUserFlowPriority_Type.__name__ = "Integer32"
_SleUserFlowPriority_Object = MibTableColumn
sleUserFlowPriority = _SleUserFlowPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 22),
    _SleUserFlowPriority_Type()
)
sleUserFlowPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowPriority.setStatus("current")
_SleUserFlowMatchCounterId_Type = Integer32
_SleUserFlowMatchCounterId_Object = MibTableColumn
sleUserFlowMatchCounterId = _SleUserFlowMatchCounterId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 23),
    _SleUserFlowMatchCounterId_Type()
)
sleUserFlowMatchCounterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowMatchCounterId.setStatus("current")
_SleUserFlowMatchTrafficProfileId_Type = Integer32
_SleUserFlowMatchTrafficProfileId_Object = MibTableColumn
sleUserFlowMatchTrafficProfileId = _SleUserFlowMatchTrafficProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 24),
    _SleUserFlowMatchTrafficProfileId_Type()
)
sleUserFlowMatchTrafficProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowMatchTrafficProfileId.setStatus("current")


class _SleUserFlowMatchQueue_Type(Integer32):
    """Custom type sleUserFlowMatchQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleUserFlowMatchQueue_Type.__name__ = "Integer32"
_SleUserFlowMatchQueue_Object = MibTableColumn
sleUserFlowMatchQueue = _SleUserFlowMatchQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 25),
    _SleUserFlowMatchQueue_Type()
)
sleUserFlowMatchQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowMatchQueue.setStatus("current")


class _SleUserFlowMatchIpPktPriorityType_Type(Integer32):
    """Custom type sleUserFlowMatchIpPktPriorityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipPrecedence", 1),
          ("diffServ", 2),
          ("ipToS", 3))
    )


_SleUserFlowMatchIpPktPriorityType_Type.__name__ = "Integer32"
_SleUserFlowMatchIpPktPriorityType_Object = MibTableColumn
sleUserFlowMatchIpPktPriorityType = _SleUserFlowMatchIpPktPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 26),
    _SleUserFlowMatchIpPktPriorityType_Type()
)
sleUserFlowMatchIpPktPriorityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowMatchIpPktPriorityType.setStatus("current")


class _SleUserFlowMatchIpPktPriority_Type(Integer32):
    """Custom type sleUserFlowMatchIpPktPriority based on Integer32"""
    defaultValue = -1


_SleUserFlowMatchIpPktPriority_Type.__name__ = "Integer32"
_SleUserFlowMatchIpPktPriority_Object = MibTableColumn
sleUserFlowMatchIpPktPriority = _SleUserFlowMatchIpPktPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 27),
    _SleUserFlowMatchIpPktPriority_Type()
)
sleUserFlowMatchIpPktPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowMatchIpPktPriority.setStatus("current")
_SleUserFlowMatchRedirPort_Type = Integer32
_SleUserFlowMatchRedirPort_Object = MibTableColumn
sleUserFlowMatchRedirPort = _SleUserFlowMatchRedirPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 28),
    _SleUserFlowMatchRedirPort_Type()
)
sleUserFlowMatchRedirPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowMatchRedirPort.setStatus("current")


class _SleUserFlowMatchVid_Type(Integer32):
    """Custom type sleUserFlowMatchVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_SleUserFlowMatchVid_Type.__name__ = "Integer32"
_SleUserFlowMatchVid_Object = MibTableColumn
sleUserFlowMatchVid = _SleUserFlowMatchVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 29),
    _SleUserFlowMatchVid_Type()
)
sleUserFlowMatchVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowMatchVid.setStatus("current")
_SleUserFlowMatchDstMac_Type = OctetString
_SleUserFlowMatchDstMac_Object = MibTableColumn
sleUserFlowMatchDstMac = _SleUserFlowMatchDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 30),
    _SleUserFlowMatchDstMac_Type()
)
sleUserFlowMatchDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowMatchDstMac.setStatus("current")
_SleUserFlowMatchPortMap_Type = OctetString
_SleUserFlowMatchPortMap_Object = MibTableColumn
sleUserFlowMatchPortMap = _SleUserFlowMatchPortMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 31),
    _SleUserFlowMatchPortMap_Type()
)
sleUserFlowMatchPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowMatchPortMap.setStatus("current")


class _SleUserFlowMatchEgressType_Type(Integer32):
    """Custom type sleUserFlowMatchEgressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dmac", 0),
          ("egressPorts", 1),
          ("filterPorts", 2))
    )


_SleUserFlowMatchEgressType_Type.__name__ = "Integer32"
_SleUserFlowMatchEgressType_Object = MibTableColumn
sleUserFlowMatchEgressType = _SleUserFlowMatchEgressType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 32),
    _SleUserFlowMatchEgressType_Type()
)
sleUserFlowMatchEgressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowMatchEgressType.setStatus("current")


class _SleUserFlowMatchAction_Type(Bits):
    """Custom type sleUserFlowMatchAction based on Bits"""
    namedValues = NamedValues(
        *(("ufActDeny", 0),
          ("ufActCopytoCpu", 1),
          ("ufActSameAsTos", 2),
          ("ufActSameAsCos", 3),
          ("ufActMirror", 4),
          ("ufActCounter", 5),
          ("ufActTrafficeProfile", 6),
          ("ufActQueue", 7),
          ("ufActIpPktPriority", 8),
          ("ufActRedirPort", 9),
          ("ufAct8021p", 10),
          ("ufActVid", 11),
          ("ufActEgress", 12),
          ("ufActColorMarking", 13),
          ("ufActRoute", 14),
          ("ufActRouteReachability", 15))
    )

_SleUserFlowMatchAction_Type.__name__ = "Bits"
_SleUserFlowMatchAction_Object = MibTableColumn
sleUserFlowMatchAction = _SleUserFlowMatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 33),
    _SleUserFlowMatchAction_Type()
)
sleUserFlowMatchAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowMatchAction.setStatus("current")
_SleUserFlowNomatchCounterId_Type = Integer32
_SleUserFlowNomatchCounterId_Object = MibTableColumn
sleUserFlowNomatchCounterId = _SleUserFlowNomatchCounterId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 34),
    _SleUserFlowNomatchCounterId_Type()
)
sleUserFlowNomatchCounterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowNomatchCounterId.setStatus("current")
_SleUserFlowNomatchTrafficProfileId_Type = Integer32
_SleUserFlowNomatchTrafficProfileId_Object = MibTableColumn
sleUserFlowNomatchTrafficProfileId = _SleUserFlowNomatchTrafficProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 35),
    _SleUserFlowNomatchTrafficProfileId_Type()
)
sleUserFlowNomatchTrafficProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowNomatchTrafficProfileId.setStatus("current")


class _SleUserFlowNomatchQueue_Type(Integer32):
    """Custom type sleUserFlowNomatchQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleUserFlowNomatchQueue_Type.__name__ = "Integer32"
_SleUserFlowNomatchQueue_Object = MibTableColumn
sleUserFlowNomatchQueue = _SleUserFlowNomatchQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 36),
    _SleUserFlowNomatchQueue_Type()
)
sleUserFlowNomatchQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowNomatchQueue.setStatus("current")


class _SleUserFlowNomatchIpPktPriorityType_Type(Integer32):
    """Custom type sleUserFlowNomatchIpPktPriorityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipPrecedence", 1),
          ("diffServ", 2),
          ("ipToS", 3))
    )


_SleUserFlowNomatchIpPktPriorityType_Type.__name__ = "Integer32"
_SleUserFlowNomatchIpPktPriorityType_Object = MibTableColumn
sleUserFlowNomatchIpPktPriorityType = _SleUserFlowNomatchIpPktPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 37),
    _SleUserFlowNomatchIpPktPriorityType_Type()
)
sleUserFlowNomatchIpPktPriorityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowNomatchIpPktPriorityType.setStatus("current")


class _SleUserFlowNomatchIpPktPriority_Type(Integer32):
    """Custom type sleUserFlowNomatchIpPktPriority based on Integer32"""
    defaultValue = -1


_SleUserFlowNomatchIpPktPriority_Type.__name__ = "Integer32"
_SleUserFlowNomatchIpPktPriority_Object = MibTableColumn
sleUserFlowNomatchIpPktPriority = _SleUserFlowNomatchIpPktPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 38),
    _SleUserFlowNomatchIpPktPriority_Type()
)
sleUserFlowNomatchIpPktPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowNomatchIpPktPriority.setStatus("current")
_SleUserFlowNomatchRedirPort_Type = Integer32
_SleUserFlowNomatchRedirPort_Object = MibTableColumn
sleUserFlowNomatchRedirPort = _SleUserFlowNomatchRedirPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 39),
    _SleUserFlowNomatchRedirPort_Type()
)
sleUserFlowNomatchRedirPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowNomatchRedirPort.setStatus("current")


class _SleUserFlowNomatchVid_Type(Integer32):
    """Custom type sleUserFlowNomatchVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_SleUserFlowNomatchVid_Type.__name__ = "Integer32"
_SleUserFlowNomatchVid_Object = MibTableColumn
sleUserFlowNomatchVid = _SleUserFlowNomatchVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 40),
    _SleUserFlowNomatchVid_Type()
)
sleUserFlowNomatchVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowNomatchVid.setStatus("current")


class _SleUserFlowNomatchAction_Type(Bits):
    """Custom type sleUserFlowNomatchAction based on Bits"""
    namedValues = NamedValues(
        *(("ufActDeny", 0),
          ("ufActCopytoCpu", 1),
          ("ufActSameAsTos", 2),
          ("ufActSameAsCos", 3),
          ("ufActMirror", 4),
          ("ufActCounter", 5),
          ("ufActTrafficeProfile", 6),
          ("ufActQueue", 7),
          ("ufActIpPktPriority", 8),
          ("ufActRedirPort", 9),
          ("ufAct8021p", 10),
          ("ufActVid", 11),
          ("ufActEgress", 12))
    )

_SleUserFlowNomatchAction_Type.__name__ = "Bits"
_SleUserFlowNomatchAction_Object = MibTableColumn
sleUserFlowNomatchAction = _SleUserFlowNomatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 41),
    _SleUserFlowNomatchAction_Type()
)
sleUserFlowNomatchAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowNomatchAction.setStatus("current")
_SleUserFlowMatchColorMarkingId_Type = Integer32
_SleUserFlowMatchColorMarkingId_Object = MibTableColumn
sleUserFlowMatchColorMarkingId = _SleUserFlowMatchColorMarkingId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 42),
    _SleUserFlowMatchColorMarkingId_Type()
)
sleUserFlowMatchColorMarkingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowMatchColorMarkingId.setStatus("current")
_SleUserFlowNomatchColorMarkingId_Type = Integer32
_SleUserFlowNomatchColorMarkingId_Object = MibTableColumn
sleUserFlowNomatchColorMarkingId = _SleUserFlowNomatchColorMarkingId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 43),
    _SleUserFlowNomatchColorMarkingId_Type()
)
sleUserFlowNomatchColorMarkingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowNomatchColorMarkingId.setStatus("current")


class _SleUserFlowInnerVlan_Type(Integer32):
    """Custom type sleUserFlowInnerVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleUserFlowInnerVlan_Type.__name__ = "Integer32"
_SleUserFlowInnerVlan_Object = MibTableColumn
sleUserFlowInnerVlan = _SleUserFlowInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 44),
    _SleUserFlowInnerVlan_Type()
)
sleUserFlowInnerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowInnerVlan.setStatus("current")


class _SleUserFlowInner8021p_Type(Integer32):
    """Custom type sleUserFlowInner8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleUserFlowInner8021p_Type.__name__ = "Integer32"
_SleUserFlowInner8021p_Object = MibTableColumn
sleUserFlowInner8021p = _SleUserFlowInner8021p_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 45),
    _SleUserFlowInner8021p_Type()
)
sleUserFlowInner8021p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowInner8021p.setStatus("current")
_SleUserFlowMatchRoutePrimary_Type = IpAddress
_SleUserFlowMatchRoutePrimary_Object = MibTableColumn
sleUserFlowMatchRoutePrimary = _SleUserFlowMatchRoutePrimary_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 46),
    _SleUserFlowMatchRoutePrimary_Type()
)
sleUserFlowMatchRoutePrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowMatchRoutePrimary.setStatus("current")
_SleUserFlowMatchRouteSecondary_Type = IpAddress
_SleUserFlowMatchRouteSecondary_Object = MibTableColumn
sleUserFlowMatchRouteSecondary = _SleUserFlowMatchRouteSecondary_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 1, 1, 47),
    _SleUserFlowMatchRouteSecondary_Type()
)
sleUserFlowMatchRouteSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowMatchRouteSecondary.setStatus("current")
_SleUserFlowControl_ObjectIdentity = ObjectIdentity
sleUserFlowControl = _SleUserFlowControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2)
)
_SleUserFlowControlReqest_Type = SleUserFlowControlRequestType
_SleUserFlowControlReqest_Object = MibScalar
sleUserFlowControlReqest = _SleUserFlowControlReqest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 1),
    _SleUserFlowControlReqest_Type()
)
sleUserFlowControlReqest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlReqest.setStatus("current")
_SleUserFlowControlStatus_Type = SleControlStatusType
_SleUserFlowControlStatus_Object = MibScalar
sleUserFlowControlStatus = _SleUserFlowControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 2),
    _SleUserFlowControlStatus_Type()
)
sleUserFlowControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowControlStatus.setStatus("current")
_SleUserFlowControlTimer_Type = Gauge32
_SleUserFlowControlTimer_Object = MibScalar
sleUserFlowControlTimer = _SleUserFlowControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 3),
    _SleUserFlowControlTimer_Type()
)
sleUserFlowControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlTimer.setStatus("current")
_SleUserFlowControlTimeStamp_Type = TimeTicks
_SleUserFlowControlTimeStamp_Object = MibScalar
sleUserFlowControlTimeStamp = _SleUserFlowControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 4),
    _SleUserFlowControlTimeStamp_Type()
)
sleUserFlowControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowControlTimeStamp.setStatus("current")
_SleUserFlowControlReqResult_Type = SleControlRequestResultType
_SleUserFlowControlReqResult_Object = MibScalar
sleUserFlowControlReqResult = _SleUserFlowControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 5),
    _SleUserFlowControlReqResult_Type()
)
sleUserFlowControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserFlowControlReqResult.setStatus("current")


class _SleUserFlowControlName_Type(OctetString):
    """Custom type sleUserFlowControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_SleUserFlowControlName_Type.__name__ = "OctetString"
_SleUserFlowControlName_Object = MibScalar
sleUserFlowControlName = _SleUserFlowControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 6),
    _SleUserFlowControlName_Type()
)
sleUserFlowControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlName.setStatus("current")
_SleUserFlowControlIngressPorts_Type = OctetString
_SleUserFlowControlIngressPorts_Object = MibScalar
sleUserFlowControlIngressPorts = _SleUserFlowControlIngressPorts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 7),
    _SleUserFlowControlIngressPorts_Type()
)
sleUserFlowControlIngressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlIngressPorts.setStatus("current")
_SleUserFlowControlEgressPorts_Type = OctetString
_SleUserFlowControlEgressPorts_Object = MibScalar
sleUserFlowControlEgressPorts = _SleUserFlowControlEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 8),
    _SleUserFlowControlEgressPorts_Type()
)
sleUserFlowControlEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlEgressPorts.setStatus("current")


class _SleUserFlowControlEthernetType_Type(Integer32):
    """Custom type sleUserFlowControlEthernetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleUserFlowControlEthernetType_Type.__name__ = "Integer32"
_SleUserFlowControlEthernetType_Object = MibScalar
sleUserFlowControlEthernetType = _SleUserFlowControlEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 9),
    _SleUserFlowControlEthernetType_Type()
)
sleUserFlowControlEthernetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlEthernetType.setStatus("current")


class _SleUserFlowControlSrcMacAddr_Type(OctetString):
    """Custom type sleUserFlowControlSrcMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_SleUserFlowControlSrcMacAddr_Type.__name__ = "OctetString"
_SleUserFlowControlSrcMacAddr_Object = MibScalar
sleUserFlowControlSrcMacAddr = _SleUserFlowControlSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 10),
    _SleUserFlowControlSrcMacAddr_Type()
)
sleUserFlowControlSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlSrcMacAddr.setStatus("current")


class _SleUserFlowControlDstMacAddr_Type(OctetString):
    """Custom type sleUserFlowControlDstMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_SleUserFlowControlDstMacAddr_Type.__name__ = "OctetString"
_SleUserFlowControlDstMacAddr_Object = MibScalar
sleUserFlowControlDstMacAddr = _SleUserFlowControlDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 11),
    _SleUserFlowControlDstMacAddr_Type()
)
sleUserFlowControlDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlDstMacAddr.setStatus("current")


class _SleUserFlowControlVlan_Type(Integer32):
    """Custom type sleUserFlowControlVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_SleUserFlowControlVlan_Type.__name__ = "Integer32"
_SleUserFlowControlVlan_Object = MibScalar
sleUserFlowControlVlan = _SleUserFlowControlVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 12),
    _SleUserFlowControlVlan_Type()
)
sleUserFlowControlVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlVlan.setStatus("current")


class _SleUserFlowControl8021p_Type(Integer32):
    """Custom type sleUserFlowControl8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleUserFlowControl8021p_Type.__name__ = "Integer32"
_SleUserFlowControl8021p_Object = MibScalar
sleUserFlowControl8021p = _SleUserFlowControl8021p_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 13),
    _SleUserFlowControl8021p_Type()
)
sleUserFlowControl8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControl8021p.setStatus("current")
_SleUserFlowControlSrcIpAddr_Type = IpAddress
_SleUserFlowControlSrcIpAddr_Object = MibScalar
sleUserFlowControlSrcIpAddr = _SleUserFlowControlSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 14),
    _SleUserFlowControlSrcIpAddr_Type()
)
sleUserFlowControlSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlSrcIpAddr.setStatus("current")
_SleUserFlowControlSrcPrefixLength_Type = Integer32
_SleUserFlowControlSrcPrefixLength_Object = MibScalar
sleUserFlowControlSrcPrefixLength = _SleUserFlowControlSrcPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 15),
    _SleUserFlowControlSrcPrefixLength_Type()
)
sleUserFlowControlSrcPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlSrcPrefixLength.setStatus("current")
_SleUserFlowControlDstIpAddr_Type = IpAddress
_SleUserFlowControlDstIpAddr_Object = MibScalar
sleUserFlowControlDstIpAddr = _SleUserFlowControlDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 16),
    _SleUserFlowControlDstIpAddr_Type()
)
sleUserFlowControlDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlDstIpAddr.setStatus("current")
_SleUserFlowControlDstPrefixLength_Type = Integer32
_SleUserFlowControlDstPrefixLength_Object = MibScalar
sleUserFlowControlDstPrefixLength = _SleUserFlowControlDstPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 17),
    _SleUserFlowControlDstPrefixLength_Type()
)
sleUserFlowControlDstPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlDstPrefixLength.setStatus("current")


class _SleUserFlowControlIpPktPriorityType_Type(Integer32):
    """Custom type sleUserFlowControlIpPktPriorityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipPrecedence", 1),
          ("diffServ", 2),
          ("ipToS", 3))
    )


_SleUserFlowControlIpPktPriorityType_Type.__name__ = "Integer32"
_SleUserFlowControlIpPktPriorityType_Object = MibScalar
sleUserFlowControlIpPktPriorityType = _SleUserFlowControlIpPktPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 18),
    _SleUserFlowControlIpPktPriorityType_Type()
)
sleUserFlowControlIpPktPriorityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlIpPktPriorityType.setStatus("current")
_SleUserFlowControlIpPktPriority_Type = Integer32
_SleUserFlowControlIpPktPriority_Object = MibScalar
sleUserFlowControlIpPktPriority = _SleUserFlowControlIpPktPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 19),
    _SleUserFlowControlIpPktPriority_Type()
)
sleUserFlowControlIpPktPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlIpPktPriority.setStatus("current")


class _SleUserFlowControlProtocolType_Type(Integer32):
    """Custom type sleUserFlowControlProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleUserFlowControlProtocolType_Type.__name__ = "Integer32"
_SleUserFlowControlProtocolType_Object = MibScalar
sleUserFlowControlProtocolType = _SleUserFlowControlProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 20),
    _SleUserFlowControlProtocolType_Type()
)
sleUserFlowControlProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlProtocolType.setStatus("current")


class _SleUserFlowControlTcpFlag_Type(Bits):
    """Custom type sleUserFlowControlTcpFlag based on Bits"""
    namedValues = NamedValues(
        *(("reserv0", 0),
          ("reserv1", 1),
          ("urg", 2),
          ("ack", 3),
          ("psh", 4),
          ("rst", 5),
          ("syn", 6),
          ("fin", 7))
    )

_SleUserFlowControlTcpFlag_Type.__name__ = "Bits"
_SleUserFlowControlTcpFlag_Object = MibScalar
sleUserFlowControlTcpFlag = _SleUserFlowControlTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 21),
    _SleUserFlowControlTcpFlag_Type()
)
sleUserFlowControlTcpFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlTcpFlag.setStatus("current")


class _SleUserFlowControlSrcL4Port_Type(Integer32):
    """Custom type sleUserFlowControlSrcL4Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleUserFlowControlSrcL4Port_Type.__name__ = "Integer32"
_SleUserFlowControlSrcL4Port_Object = MibScalar
sleUserFlowControlSrcL4Port = _SleUserFlowControlSrcL4Port_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 22),
    _SleUserFlowControlSrcL4Port_Type()
)
sleUserFlowControlSrcL4Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlSrcL4Port.setStatus("current")


class _SleUserFlowControlDstL4Port_Type(Integer32):
    """Custom type sleUserFlowControlDstL4Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleUserFlowControlDstL4Port_Type.__name__ = "Integer32"
_SleUserFlowControlDstL4Port_Object = MibScalar
sleUserFlowControlDstL4Port = _SleUserFlowControlDstL4Port_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 23),
    _SleUserFlowControlDstL4Port_Type()
)
sleUserFlowControlDstL4Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlDstL4Port.setStatus("current")


class _SleUserFlowControlPktLen_Type(Integer32):
    """Custom type sleUserFlowControlPktLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(21, 65535),
    )


_SleUserFlowControlPktLen_Type.__name__ = "Integer32"
_SleUserFlowControlPktLen_Object = MibScalar
sleUserFlowControlPktLen = _SleUserFlowControlPktLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 24),
    _SleUserFlowControlPktLen_Type()
)
sleUserFlowControlPktLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlPktLen.setStatus("current")


class _SleUserFlowControlValidFlag_Type(Bits):
    """Custom type sleUserFlowControlValidFlag based on Bits"""
    namedValues = NamedValues(
        *(("ufIngressPort", 0),
          ("ufEgressPort", 1),
          ("ufEthernetType", 2),
          ("ufSrcMacAddress", 3),
          ("ufDstMacAddress", 4),
          ("ufVlanId", 5),
          ("uf8021p", 6),
          ("ufSrcIpAddress", 7),
          ("ufSrcPrefixLength", 8),
          ("ufDstIpAddress", 9),
          ("ufDstPrefixLength", 10),
          ("ufIpPktPriority", 11),
          ("ufProtocolType", 12),
          ("ufTcpFlag", 13),
          ("ufSrcL4Port", 14),
          ("ufDstL4Port", 15),
          ("ufPacketLength", 16),
          ("ufPriority", 17),
          ("ufInnerVlanId", 18),
          ("ufInner8021p", 19))
    )

_SleUserFlowControlValidFlag_Type.__name__ = "Bits"
_SleUserFlowControlValidFlag_Object = MibScalar
sleUserFlowControlValidFlag = _SleUserFlowControlValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 25),
    _SleUserFlowControlValidFlag_Type()
)
sleUserFlowControlValidFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlValidFlag.setStatus("current")


class _SleUserFlowControlMatchFlag_Type(Bits):
    """Custom type sleUserFlowControlMatchFlag based on Bits"""
    namedValues = NamedValues(
        *(("ufIngressPort", 0),
          ("ufEgressPort", 1),
          ("ufEthernetType", 2),
          ("ufSrcMacAddress", 3),
          ("ufDstMacAddress", 4),
          ("ufVlanId", 5),
          ("uf8021p", 6),
          ("ufSrcIpAddress", 7),
          ("ufSrcPrefixLength", 8),
          ("ufDstIpAddress", 9),
          ("ufDstPrefixLength", 10),
          ("ufIpPktPriority", 11),
          ("ufProtocolType", 12),
          ("ufTcpFlag", 13),
          ("ufSrcL4Port", 14),
          ("ufDstL4Port", 15),
          ("ufPacketLength", 16),
          ("ufPriority", 17))
    )

_SleUserFlowControlMatchFlag_Type.__name__ = "Bits"
_SleUserFlowControlMatchFlag_Object = MibScalar
sleUserFlowControlMatchFlag = _SleUserFlowControlMatchFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 26),
    _SleUserFlowControlMatchFlag_Type()
)
sleUserFlowControlMatchFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlMatchFlag.setStatus("current")


class _SleUserFlowControlPriority_Type(Integer32):
    """Custom type sleUserFlowControlPriority based on Integer32"""
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
          ("highest", 4))
    )


_SleUserFlowControlPriority_Type.__name__ = "Integer32"
_SleUserFlowControlPriority_Object = MibScalar
sleUserFlowControlPriority = _SleUserFlowControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 27),
    _SleUserFlowControlPriority_Type()
)
sleUserFlowControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlPriority.setStatus("current")
_SleUserFlowControlMatchCounterId_Type = Integer32
_SleUserFlowControlMatchCounterId_Object = MibScalar
sleUserFlowControlMatchCounterId = _SleUserFlowControlMatchCounterId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 28),
    _SleUserFlowControlMatchCounterId_Type()
)
sleUserFlowControlMatchCounterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlMatchCounterId.setStatus("current")
_SleUserFlowControlMatchTrafficProfileId_Type = Integer32
_SleUserFlowControlMatchTrafficProfileId_Object = MibScalar
sleUserFlowControlMatchTrafficProfileId = _SleUserFlowControlMatchTrafficProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 29),
    _SleUserFlowControlMatchTrafficProfileId_Type()
)
sleUserFlowControlMatchTrafficProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlMatchTrafficProfileId.setStatus("current")


class _SleUserFlowControlMatchQueue_Type(Integer32):
    """Custom type sleUserFlowControlMatchQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleUserFlowControlMatchQueue_Type.__name__ = "Integer32"
_SleUserFlowControlMatchQueue_Object = MibScalar
sleUserFlowControlMatchQueue = _SleUserFlowControlMatchQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 30),
    _SleUserFlowControlMatchQueue_Type()
)
sleUserFlowControlMatchQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlMatchQueue.setStatus("current")


class _SleUserFlowControlMatchIpPktPriorityType_Type(Integer32):
    """Custom type sleUserFlowControlMatchIpPktPriorityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipPrecedence", 1),
          ("diffServ", 2),
          ("ipToS", 3))
    )


_SleUserFlowControlMatchIpPktPriorityType_Type.__name__ = "Integer32"
_SleUserFlowControlMatchIpPktPriorityType_Object = MibScalar
sleUserFlowControlMatchIpPktPriorityType = _SleUserFlowControlMatchIpPktPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 31),
    _SleUserFlowControlMatchIpPktPriorityType_Type()
)
sleUserFlowControlMatchIpPktPriorityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlMatchIpPktPriorityType.setStatus("current")


class _SleUserFlowControlMatchIpPktPriority_Type(Integer32):
    """Custom type sleUserFlowControlMatchIpPktPriority based on Integer32"""
    defaultValue = -1


_SleUserFlowControlMatchIpPktPriority_Type.__name__ = "Integer32"
_SleUserFlowControlMatchIpPktPriority_Object = MibScalar
sleUserFlowControlMatchIpPktPriority = _SleUserFlowControlMatchIpPktPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 32),
    _SleUserFlowControlMatchIpPktPriority_Type()
)
sleUserFlowControlMatchIpPktPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlMatchIpPktPriority.setStatus("current")
_SleUserFlowControlMatchRedirPort_Type = Integer32
_SleUserFlowControlMatchRedirPort_Object = MibScalar
sleUserFlowControlMatchRedirPort = _SleUserFlowControlMatchRedirPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 33),
    _SleUserFlowControlMatchRedirPort_Type()
)
sleUserFlowControlMatchRedirPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlMatchRedirPort.setStatus("current")


class _SleUserFlowControlMatchVid_Type(Integer32):
    """Custom type sleUserFlowControlMatchVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_SleUserFlowControlMatchVid_Type.__name__ = "Integer32"
_SleUserFlowControlMatchVid_Object = MibScalar
sleUserFlowControlMatchVid = _SleUserFlowControlMatchVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 34),
    _SleUserFlowControlMatchVid_Type()
)
sleUserFlowControlMatchVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlMatchVid.setStatus("current")
_SleUserFlowControlMatchDstMac_Type = OctetString
_SleUserFlowControlMatchDstMac_Object = MibScalar
sleUserFlowControlMatchDstMac = _SleUserFlowControlMatchDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 35),
    _SleUserFlowControlMatchDstMac_Type()
)
sleUserFlowControlMatchDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlMatchDstMac.setStatus("current")
_SleUserFlowControlMatchPortMap_Type = OctetString
_SleUserFlowControlMatchPortMap_Object = MibScalar
sleUserFlowControlMatchPortMap = _SleUserFlowControlMatchPortMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 36),
    _SleUserFlowControlMatchPortMap_Type()
)
sleUserFlowControlMatchPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlMatchPortMap.setStatus("current")


class _SleUserFlowControlMatchEgressType_Type(Integer32):
    """Custom type sleUserFlowControlMatchEgressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dmac", 0),
          ("egressPorts", 1),
          ("filterPorts", 2))
    )


_SleUserFlowControlMatchEgressType_Type.__name__ = "Integer32"
_SleUserFlowControlMatchEgressType_Object = MibScalar
sleUserFlowControlMatchEgressType = _SleUserFlowControlMatchEgressType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 37),
    _SleUserFlowControlMatchEgressType_Type()
)
sleUserFlowControlMatchEgressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlMatchEgressType.setStatus("current")


class _SleUserFlowControlMatchAction_Type(Bits):
    """Custom type sleUserFlowControlMatchAction based on Bits"""
    namedValues = NamedValues(
        *(("ufActDeny", 0),
          ("ufActCopytoCpu", 1),
          ("ufActSameAsTos", 2),
          ("ufActSameAsCos", 3),
          ("ufActMirror", 4),
          ("ufActCounter", 5),
          ("ufActTrafficeProfile", 6),
          ("ufActQueue", 7),
          ("ufActIpPktPriority", 8),
          ("ufActRedirPort", 9),
          ("ufAct8021p", 10),
          ("ufActVid", 11),
          ("ufActEgress", 12),
          ("ufActColorMarking", 13),
          ("ufActRoute", 14),
          ("ufActRouteReachability", 15))
    )

_SleUserFlowControlMatchAction_Type.__name__ = "Bits"
_SleUserFlowControlMatchAction_Object = MibScalar
sleUserFlowControlMatchAction = _SleUserFlowControlMatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 38),
    _SleUserFlowControlMatchAction_Type()
)
sleUserFlowControlMatchAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlMatchAction.setStatus("current")
_SleUserFlowControlNomatchCounterId_Type = Integer32
_SleUserFlowControlNomatchCounterId_Object = MibScalar
sleUserFlowControlNomatchCounterId = _SleUserFlowControlNomatchCounterId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 39),
    _SleUserFlowControlNomatchCounterId_Type()
)
sleUserFlowControlNomatchCounterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlNomatchCounterId.setStatus("current")
_SleUserFlowControlNomatchTrafficProfileId_Type = Integer32
_SleUserFlowControlNomatchTrafficProfileId_Object = MibScalar
sleUserFlowControlNomatchTrafficProfileId = _SleUserFlowControlNomatchTrafficProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 40),
    _SleUserFlowControlNomatchTrafficProfileId_Type()
)
sleUserFlowControlNomatchTrafficProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlNomatchTrafficProfileId.setStatus("current")


class _SleUserFlowControlNomatchQueue_Type(Integer32):
    """Custom type sleUserFlowControlNomatchQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleUserFlowControlNomatchQueue_Type.__name__ = "Integer32"
_SleUserFlowControlNomatchQueue_Object = MibScalar
sleUserFlowControlNomatchQueue = _SleUserFlowControlNomatchQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 41),
    _SleUserFlowControlNomatchQueue_Type()
)
sleUserFlowControlNomatchQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlNomatchQueue.setStatus("current")


class _SleUserFlowControlNomatchIpPktPriorityType_Type(Integer32):
    """Custom type sleUserFlowControlNomatchIpPktPriorityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipPrecedence", 1),
          ("diffServ", 2),
          ("ipToS", 3))
    )


_SleUserFlowControlNomatchIpPktPriorityType_Type.__name__ = "Integer32"
_SleUserFlowControlNomatchIpPktPriorityType_Object = MibScalar
sleUserFlowControlNomatchIpPktPriorityType = _SleUserFlowControlNomatchIpPktPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 42),
    _SleUserFlowControlNomatchIpPktPriorityType_Type()
)
sleUserFlowControlNomatchIpPktPriorityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlNomatchIpPktPriorityType.setStatus("current")


class _SleUserFlowControlNomatchIpPktPriority_Type(Integer32):
    """Custom type sleUserFlowControlNomatchIpPktPriority based on Integer32"""
    defaultValue = -1


_SleUserFlowControlNomatchIpPktPriority_Type.__name__ = "Integer32"
_SleUserFlowControlNomatchIpPktPriority_Object = MibScalar
sleUserFlowControlNomatchIpPktPriority = _SleUserFlowControlNomatchIpPktPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 43),
    _SleUserFlowControlNomatchIpPktPriority_Type()
)
sleUserFlowControlNomatchIpPktPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlNomatchIpPktPriority.setStatus("current")
_SleUserFlowControlNomatchRedirPort_Type = Integer32
_SleUserFlowControlNomatchRedirPort_Object = MibScalar
sleUserFlowControlNomatchRedirPort = _SleUserFlowControlNomatchRedirPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 44),
    _SleUserFlowControlNomatchRedirPort_Type()
)
sleUserFlowControlNomatchRedirPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlNomatchRedirPort.setStatus("current")


class _SleUserFlowControlNomatchVid_Type(Integer32):
    """Custom type sleUserFlowControlNomatchVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_SleUserFlowControlNomatchVid_Type.__name__ = "Integer32"
_SleUserFlowControlNomatchVid_Object = MibScalar
sleUserFlowControlNomatchVid = _SleUserFlowControlNomatchVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 45),
    _SleUserFlowControlNomatchVid_Type()
)
sleUserFlowControlNomatchVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlNomatchVid.setStatus("current")


class _SleUserFlowControlNomatchAction_Type(Bits):
    """Custom type sleUserFlowControlNomatchAction based on Bits"""
    namedValues = NamedValues(
        *(("ufActDeny", 0),
          ("ufActCopytoCpu", 1),
          ("ufActSameAsTos", 2),
          ("ufActSameAsCos", 3),
          ("ufActMirror", 4),
          ("ufActCounter", 5),
          ("ufActTrafficeProfile", 6),
          ("ufActQueue", 7),
          ("ufActIpPktPriority", 8),
          ("ufActRedirPort", 9),
          ("ufAct8021p", 10),
          ("ufActVid", 11),
          ("ufActEgress", 12))
    )

_SleUserFlowControlNomatchAction_Type.__name__ = "Bits"
_SleUserFlowControlNomatchAction_Object = MibScalar
sleUserFlowControlNomatchAction = _SleUserFlowControlNomatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 46),
    _SleUserFlowControlNomatchAction_Type()
)
sleUserFlowControlNomatchAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlNomatchAction.setStatus("current")
_SleUserFlowControlMatchColorMarkingId_Type = Integer32
_SleUserFlowControlMatchColorMarkingId_Object = MibScalar
sleUserFlowControlMatchColorMarkingId = _SleUserFlowControlMatchColorMarkingId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 47),
    _SleUserFlowControlMatchColorMarkingId_Type()
)
sleUserFlowControlMatchColorMarkingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlMatchColorMarkingId.setStatus("current")
_SleUserFlowControlNomatchColorMarkingId_Type = Integer32
_SleUserFlowControlNomatchColorMarkingId_Object = MibScalar
sleUserFlowControlNomatchColorMarkingId = _SleUserFlowControlNomatchColorMarkingId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 48),
    _SleUserFlowControlNomatchColorMarkingId_Type()
)
sleUserFlowControlNomatchColorMarkingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlNomatchColorMarkingId.setStatus("current")


class _SleUserFlowControlInnerVlan_Type(Integer32):
    """Custom type sleUserFlowControlInnerVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleUserFlowControlInnerVlan_Type.__name__ = "Integer32"
_SleUserFlowControlInnerVlan_Object = MibScalar
sleUserFlowControlInnerVlan = _SleUserFlowControlInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 49),
    _SleUserFlowControlInnerVlan_Type()
)
sleUserFlowControlInnerVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlInnerVlan.setStatus("current")


class _SleUserFlowControlInner8021p_Type(Integer32):
    """Custom type sleUserFlowControlInner8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleUserFlowControlInner8021p_Type.__name__ = "Integer32"
_SleUserFlowControlInner8021p_Object = MibScalar
sleUserFlowControlInner8021p = _SleUserFlowControlInner8021p_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 50),
    _SleUserFlowControlInner8021p_Type()
)
sleUserFlowControlInner8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlInner8021p.setStatus("current")
_SleUserFlowControlMatchRoutePrimary_Type = IpAddress
_SleUserFlowControlMatchRoutePrimary_Object = MibScalar
sleUserFlowControlMatchRoutePrimary = _SleUserFlowControlMatchRoutePrimary_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 51),
    _SleUserFlowControlMatchRoutePrimary_Type()
)
sleUserFlowControlMatchRoutePrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlMatchRoutePrimary.setStatus("current")
_SleUserFlowControlMatchRouteSecondary_Type = IpAddress
_SleUserFlowControlMatchRouteSecondary_Object = MibScalar
sleUserFlowControlMatchRouteSecondary = _SleUserFlowControlMatchRouteSecondary_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 2, 52),
    _SleUserFlowControlMatchRouteSecondary_Type()
)
sleUserFlowControlMatchRouteSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserFlowControlMatchRouteSecondary.setStatus("current")
_SleUserFlowNotification_ObjectIdentity = ObjectIdentity
sleUserFlowNotification = _SleUserFlowNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 3)
)
_SlePortSchedule_ObjectIdentity = ObjectIdentity
slePortSchedule = _SlePortSchedule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 4)
)
_SlePortSchedultTable_Object = MibTable
slePortSchedultTable = _SlePortSchedultTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 4, 1)
)
if mibBuilder.loadTexts:
    slePortSchedultTable.setStatus("current")
_SlePortSchedultEntry_Object = MibTableRow
slePortSchedultEntry = _SlePortSchedultEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 4, 1, 1)
)
slePortSchedultEntry.setIndexNames(
    (0, "SLE-QOS-MIB", "slePortSchedulInterfaceIndex"),
)
if mibBuilder.loadTexts:
    slePortSchedultEntry.setStatus("current")


class _SlePortSchedulInterfaceIndex_Type(Integer32):
    """Custom type slePortSchedulInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SlePortSchedulInterfaceIndex_Type.__name__ = "Integer32"
_SlePortSchedulInterfaceIndex_Object = MibTableColumn
slePortSchedulInterfaceIndex = _SlePortSchedulInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 4, 1, 1, 1),
    _SlePortSchedulInterfaceIndex_Type()
)
slePortSchedulInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePortSchedulInterfaceIndex.setStatus("current")


class _SlePortScheduleMode_Type(Integer32):
    """Custom type slePortScheduleMode based on Integer32"""
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
        *(("strictqueueing", 1),
          ("wrr", 2),
          ("wfq", 3),
          ("rr", 4),
          ("drr", 5))
    )


_SlePortScheduleMode_Type.__name__ = "Integer32"
_SlePortScheduleMode_Object = MibTableColumn
slePortScheduleMode = _SlePortScheduleMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 4, 1, 1, 2),
    _SlePortScheduleMode_Type()
)
slePortScheduleMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePortScheduleMode.setStatus("current")
_SlePortScheduleControl_ObjectIdentity = ObjectIdentity
slePortScheduleControl = _SlePortScheduleControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 4, 2)
)
_SlePortScheduleControlRequest_Type = SlePortScheduleControlRequestType
_SlePortScheduleControlRequest_Object = MibScalar
slePortScheduleControlRequest = _SlePortScheduleControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 4, 2, 1),
    _SlePortScheduleControlRequest_Type()
)
slePortScheduleControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePortScheduleControlRequest.setStatus("current")
_SleScheduleControlStatus_Type = SleControlStatusType
_SleScheduleControlStatus_Object = MibScalar
sleScheduleControlStatus = _SleScheduleControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 4, 2, 2),
    _SleScheduleControlStatus_Type()
)
sleScheduleControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleScheduleControlStatus.setStatus("current")
_SlePortScheduleControlTimer_Type = Gauge32
_SlePortScheduleControlTimer_Object = MibScalar
slePortScheduleControlTimer = _SlePortScheduleControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 4, 2, 3),
    _SlePortScheduleControlTimer_Type()
)
slePortScheduleControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePortScheduleControlTimer.setStatus("current")
_SlePortScheduleControlTimeStamp_Type = TimeTicks
_SlePortScheduleControlTimeStamp_Object = MibScalar
slePortScheduleControlTimeStamp = _SlePortScheduleControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 4, 2, 4),
    _SlePortScheduleControlTimeStamp_Type()
)
slePortScheduleControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePortScheduleControlTimeStamp.setStatus("current")
_SlePortScheduleControlReqResult_Type = SleControlRequestResultType
_SlePortScheduleControlReqResult_Object = MibScalar
slePortScheduleControlReqResult = _SlePortScheduleControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 4, 2, 5),
    _SlePortScheduleControlReqResult_Type()
)
slePortScheduleControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePortScheduleControlReqResult.setStatus("current")
_SlePortScheduleControlInterfaceIndex_Type = Integer32
_SlePortScheduleControlInterfaceIndex_Object = MibScalar
slePortScheduleControlInterfaceIndex = _SlePortScheduleControlInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 4, 2, 6),
    _SlePortScheduleControlInterfaceIndex_Type()
)
slePortScheduleControlInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePortScheduleControlInterfaceIndex.setStatus("current")


class _SlePortScheduleControlMode_Type(Integer32):
    """Custom type slePortScheduleControlMode based on Integer32"""
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
        *(("strictqueueing", 1),
          ("wrr", 2),
          ("wfq", 3),
          ("rr", 4),
          ("drr", 5))
    )


_SlePortScheduleControlMode_Type.__name__ = "Integer32"
_SlePortScheduleControlMode_Object = MibScalar
slePortScheduleControlMode = _SlePortScheduleControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 4, 2, 7),
    _SlePortScheduleControlMode_Type()
)
slePortScheduleControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePortScheduleControlMode.setStatus("current")
_SlePortScheduleNotification_ObjectIdentity = ObjectIdentity
slePortScheduleNotification = _SlePortScheduleNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 4, 3)
)
_SleQueue_ObjectIdentity = ObjectIdentity
sleQueue = _SleQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5)
)
_SleQueueTable_Object = MibTable
sleQueueTable = _SleQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 1)
)
if mibBuilder.loadTexts:
    sleQueueTable.setStatus("current")
_SleQueueEntry_Object = MibTableRow
sleQueueEntry = _SleQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 1, 1)
)
sleQueueEntry.setIndexNames(
    (0, "SLE-QOS-MIB", "slePortSchedulInterfaceIndex"),
    (0, "SLE-QOS-MIB", "sleQueueId"),
)
if mibBuilder.loadTexts:
    sleQueueEntry.setStatus("current")


class _SleQueueId_Type(Integer32):
    """Custom type sleQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleQueueId_Type.__name__ = "Integer32"
_SleQueueId_Object = MibTableColumn
sleQueueId = _SleQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 1, 1, 1),
    _SleQueueId_Type()
)
sleQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQueueId.setStatus("current")


class _SleQueueREDEnable_Type(Integer32):
    """Custom type sleQueueREDEnable based on Integer32"""
    defaultValue = 0

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


_SleQueueREDEnable_Type.__name__ = "Integer32"
_SleQueueREDEnable_Object = MibTableColumn
sleQueueREDEnable = _SleQueueREDEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 1, 1, 2),
    _SleQueueREDEnable_Type()
)
sleQueueREDEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQueueREDEnable.setStatus("current")


class _SleQueueMappedCoS_Type(Bits):
    """Custom type sleQueueMappedCoS based on Bits"""
    namedValues = NamedValues(
        *(("cos0", 0),
          ("cos1", 1),
          ("cos2", 2),
          ("cos3", 3),
          ("cos4", 4),
          ("cos5", 5),
          ("cos6", 6),
          ("cos7", 7))
    )

_SleQueueMappedCoS_Type.__name__ = "Bits"
_SleQueueMappedCoS_Object = MibTableColumn
sleQueueMappedCoS = _SleQueueMappedCoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 1, 1, 3),
    _SleQueueMappedCoS_Type()
)
sleQueueMappedCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQueueMappedCoS.setStatus("current")
_SleQueueWREDMinThreshold_Type = Integer32
_SleQueueWREDMinThreshold_Object = MibTableColumn
sleQueueWREDMinThreshold = _SleQueueWREDMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 1, 1, 4),
    _SleQueueWREDMinThreshold_Type()
)
sleQueueWREDMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQueueWREDMinThreshold.setStatus("current")
_SleQueueWREDMaxThreshold_Type = Integer32
_SleQueueWREDMaxThreshold_Object = MibTableColumn
sleQueueWREDMaxThreshold = _SleQueueWREDMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 1, 1, 5),
    _SleQueueWREDMaxThreshold_Type()
)
sleQueueWREDMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQueueWREDMaxThreshold.setStatus("current")


class _SleQueueWREDProbMax_Type(Integer32):
    """Custom type sleQueueWREDProbMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SleQueueWREDProbMax_Type.__name__ = "Integer32"
_SleQueueWREDProbMax_Object = MibTableColumn
sleQueueWREDProbMax = _SleQueueWREDProbMax_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 1, 1, 6),
    _SleQueueWREDProbMax_Type()
)
sleQueueWREDProbMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQueueWREDProbMax.setStatus("current")
_SleQueueMinBandwidth_Type = Integer32
_SleQueueMinBandwidth_Object = MibTableColumn
sleQueueMinBandwidth = _SleQueueMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 1, 1, 7),
    _SleQueueMinBandwidth_Type()
)
sleQueueMinBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQueueMinBandwidth.setStatus("current")
_SleQueueMaxBandwidth_Type = Integer32
_SleQueueMaxBandwidth_Object = MibTableColumn
sleQueueMaxBandwidth = _SleQueueMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 1, 1, 8),
    _SleQueueMaxBandwidth_Type()
)
sleQueueMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQueueMaxBandwidth.setStatus("current")


class _SleQueueWeight_Type(Integer32):
    """Custom type sleQueueWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 255),
    )


_SleQueueWeight_Type.__name__ = "Integer32"
_SleQueueWeight_Object = MibTableColumn
sleQueueWeight = _SleQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 1, 1, 9),
    _SleQueueWeight_Type()
)
sleQueueWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQueueWeight.setStatus("current")
_SleQueueMaxLatency_Type = Integer32
_SleQueueMaxLatency_Object = MibTableColumn
sleQueueMaxLatency = _SleQueueMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 1, 1, 10),
    _SleQueueMaxLatency_Type()
)
sleQueueMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQueueMaxLatency.setStatus("current")
_SleQueueMaxPackets_Type = Integer32
_SleQueueMaxPackets_Object = MibTableColumn
sleQueueMaxPackets = _SleQueueMaxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 1, 1, 11),
    _SleQueueMaxPackets_Type()
)
sleQueueMaxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQueueMaxPackets.setStatus("current")


class _SleQueueQuantum_Type(Integer32):
    """Custom type sleQueueQuantum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 127),
    )


_SleQueueQuantum_Type.__name__ = "Integer32"
_SleQueueQuantum_Object = MibTableColumn
sleQueueQuantum = _SleQueueQuantum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 1, 1, 12),
    _SleQueueQuantum_Type()
)
sleQueueQuantum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQueueQuantum.setStatus("current")
_SleQueueUsedPkts_Type = Counter32
_SleQueueUsedPkts_Object = MibTableColumn
sleQueueUsedPkts = _SleQueueUsedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 1, 1, 13),
    _SleQueueUsedPkts_Type()
)
sleQueueUsedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQueueUsedPkts.setStatus("current")
_SleQueueUsedBytes_Type = Counter32
_SleQueueUsedBytes_Object = MibTableColumn
sleQueueUsedBytes = _SleQueueUsedBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 1, 1, 14),
    _SleQueueUsedBytes_Type()
)
sleQueueUsedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQueueUsedBytes.setStatus("current")
_SleQueueControl_ObjectIdentity = ObjectIdentity
sleQueueControl = _SleQueueControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2)
)


class _SleQueueControlRequest_Type(Integer32):
    """Custom type sleQueueControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setQueueProfile", 1),
          ("setQuantum", 2))
    )


_SleQueueControlRequest_Type.__name__ = "Integer32"
_SleQueueControlRequest_Object = MibScalar
sleQueueControlRequest = _SleQueueControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2, 1),
    _SleQueueControlRequest_Type()
)
sleQueueControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleQueueControlRequest.setStatus("current")
_SleQueueControlStatus_Type = Integer32
_SleQueueControlStatus_Object = MibScalar
sleQueueControlStatus = _SleQueueControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2, 2),
    _SleQueueControlStatus_Type()
)
sleQueueControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQueueControlStatus.setStatus("current")
_SleQueueControlTimer_Type = Gauge32
_SleQueueControlTimer_Object = MibScalar
sleQueueControlTimer = _SleQueueControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2, 3),
    _SleQueueControlTimer_Type()
)
sleQueueControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleQueueControlTimer.setStatus("current")
_SleQueueControlTimeStamp_Type = Integer32
_SleQueueControlTimeStamp_Object = MibScalar
sleQueueControlTimeStamp = _SleQueueControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2, 4),
    _SleQueueControlTimeStamp_Type()
)
sleQueueControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQueueControlTimeStamp.setStatus("current")
_SleQueueControlReqResult_Type = SleControlRequestResultType
_SleQueueControlReqResult_Object = MibScalar
sleQueueControlReqResult = _SleQueueControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2, 5),
    _SleQueueControlReqResult_Type()
)
sleQueueControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQueueControlReqResult.setStatus("current")
_SleQueueControlInterfaceIndex_Type = Integer32
_SleQueueControlInterfaceIndex_Object = MibScalar
sleQueueControlInterfaceIndex = _SleQueueControlInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2, 6),
    _SleQueueControlInterfaceIndex_Type()
)
sleQueueControlInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleQueueControlInterfaceIndex.setStatus("current")


class _SleQueueControlId_Type(Integer32):
    """Custom type sleQueueControlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleQueueControlId_Type.__name__ = "Integer32"
_SleQueueControlId_Object = MibScalar
sleQueueControlId = _SleQueueControlId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2, 7),
    _SleQueueControlId_Type()
)
sleQueueControlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleQueueControlId.setStatus("current")


class _SleQueueControlREDEnable_Type(Integer32):
    """Custom type sleQueueControlREDEnable based on Integer32"""
    defaultValue = 0

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


_SleQueueControlREDEnable_Type.__name__ = "Integer32"
_SleQueueControlREDEnable_Object = MibScalar
sleQueueControlREDEnable = _SleQueueControlREDEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2, 8),
    _SleQueueControlREDEnable_Type()
)
sleQueueControlREDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleQueueControlREDEnable.setStatus("current")


class _SleQueueControlMappedCoS_Type(Bits):
    """Custom type sleQueueControlMappedCoS based on Bits"""
    namedValues = NamedValues(
        *(("cos0", 0),
          ("cos1", 1),
          ("cos2", 2),
          ("cos3", 3),
          ("cos4", 4),
          ("cos5", 5),
          ("cos6", 6),
          ("cos7", 7))
    )

_SleQueueControlMappedCoS_Type.__name__ = "Bits"
_SleQueueControlMappedCoS_Object = MibScalar
sleQueueControlMappedCoS = _SleQueueControlMappedCoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2, 9),
    _SleQueueControlMappedCoS_Type()
)
sleQueueControlMappedCoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleQueueControlMappedCoS.setStatus("current")
_SleQueueControlWREDMinThreshold_Type = Integer32
_SleQueueControlWREDMinThreshold_Object = MibScalar
sleQueueControlWREDMinThreshold = _SleQueueControlWREDMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2, 10),
    _SleQueueControlWREDMinThreshold_Type()
)
sleQueueControlWREDMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleQueueControlWREDMinThreshold.setStatus("current")
_SleQueueControlWREDMaxThreshold_Type = Integer32
_SleQueueControlWREDMaxThreshold_Object = MibScalar
sleQueueControlWREDMaxThreshold = _SleQueueControlWREDMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2, 11),
    _SleQueueControlWREDMaxThreshold_Type()
)
sleQueueControlWREDMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleQueueControlWREDMaxThreshold.setStatus("current")


class _SleQueueControlWREDProbMax_Type(Integer32):
    """Custom type sleQueueControlWREDProbMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SleQueueControlWREDProbMax_Type.__name__ = "Integer32"
_SleQueueControlWREDProbMax_Object = MibScalar
sleQueueControlWREDProbMax = _SleQueueControlWREDProbMax_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2, 12),
    _SleQueueControlWREDProbMax_Type()
)
sleQueueControlWREDProbMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleQueueControlWREDProbMax.setStatus("current")
_SleQueueControlMinBandwidth_Type = Integer32
_SleQueueControlMinBandwidth_Object = MibScalar
sleQueueControlMinBandwidth = _SleQueueControlMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2, 13),
    _SleQueueControlMinBandwidth_Type()
)
sleQueueControlMinBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleQueueControlMinBandwidth.setStatus("current")
_SleQueueControlMaxBandwidth_Type = Integer32
_SleQueueControlMaxBandwidth_Object = MibScalar
sleQueueControlMaxBandwidth = _SleQueueControlMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2, 14),
    _SleQueueControlMaxBandwidth_Type()
)
sleQueueControlMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleQueueControlMaxBandwidth.setStatus("current")


class _SleQueueControlWeight_Type(Integer32):
    """Custom type sleQueueControlWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 255),
    )


_SleQueueControlWeight_Type.__name__ = "Integer32"
_SleQueueControlWeight_Object = MibScalar
sleQueueControlWeight = _SleQueueControlWeight_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2, 15),
    _SleQueueControlWeight_Type()
)
sleQueueControlWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleQueueControlWeight.setStatus("current")
_SleQueueControlMaxLatency_Type = Integer32
_SleQueueControlMaxLatency_Object = MibScalar
sleQueueControlMaxLatency = _SleQueueControlMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2, 16),
    _SleQueueControlMaxLatency_Type()
)
sleQueueControlMaxLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleQueueControlMaxLatency.setStatus("current")
_SleQueueControlMaxPackets_Type = Integer32
_SleQueueControlMaxPackets_Object = MibScalar
sleQueueControlMaxPackets = _SleQueueControlMaxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2, 17),
    _SleQueueControlMaxPackets_Type()
)
sleQueueControlMaxPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleQueueControlMaxPackets.setStatus("current")


class _SleQueueControlQuantum_Type(Integer32):
    """Custom type sleQueueControlQuantum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 127),
    )


_SleQueueControlQuantum_Type.__name__ = "Integer32"
_SleQueueControlQuantum_Object = MibScalar
sleQueueControlQuantum = _SleQueueControlQuantum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 2, 18),
    _SleQueueControlQuantum_Type()
)
sleQueueControlQuantum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleQueueControlQuantum.setStatus("current")
_SleQueueNotification_ObjectIdentity = ObjectIdentity
sleQueueNotification = _SleQueueNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 3)
)
_SleCounter_ObjectIdentity = ObjectIdentity
sleCounter = _SleCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 6)
)
_SleCounterTable_Object = MibTable
sleCounterTable = _SleCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 6, 1)
)
if mibBuilder.loadTexts:
    sleCounterTable.setStatus("current")
_SleCounterEntry_Object = MibTableRow
sleCounterEntry = _SleCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 6, 1, 1)
)
sleCounterEntry.setIndexNames(
    (0, "SLE-QOS-MIB", "sleCounterIndex"),
)
if mibBuilder.loadTexts:
    sleCounterEntry.setStatus("current")


class _SleCounterIndex_Type(Integer32):
    """Custom type sleCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleCounterIndex_Type.__name__ = "Integer32"
_SleCounterIndex_Object = MibTableColumn
sleCounterIndex = _SleCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 6, 1, 1, 1),
    _SleCounterIndex_Type()
)
sleCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCounterIndex.setStatus("current")
_SleCounterPackets_Type = Unsigned32
_SleCounterPackets_Object = MibTableColumn
sleCounterPackets = _SleCounterPackets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 6, 1, 1, 2),
    _SleCounterPackets_Type()
)
sleCounterPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCounterPackets.setStatus("current")
_SleCounterControl_ObjectIdentity = ObjectIdentity
sleCounterControl = _SleCounterControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 6, 2)
)


class _SleCounterControlRequest_Type(Integer32):
    """Custom type sleCounterControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearCounter", 1)
    )


_SleCounterControlRequest_Type.__name__ = "Integer32"
_SleCounterControlRequest_Object = MibScalar
sleCounterControlRequest = _SleCounterControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 6, 2, 1),
    _SleCounterControlRequest_Type()
)
sleCounterControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCounterControlRequest.setStatus("current")
_SleCounterControlStatus_Type = SleControlStatusType
_SleCounterControlStatus_Object = MibScalar
sleCounterControlStatus = _SleCounterControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 6, 2, 2),
    _SleCounterControlStatus_Type()
)
sleCounterControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCounterControlStatus.setStatus("current")
_SleCounterControlTimer_Type = Gauge32
_SleCounterControlTimer_Object = MibScalar
sleCounterControlTimer = _SleCounterControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 6, 2, 3),
    _SleCounterControlTimer_Type()
)
sleCounterControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCounterControlTimer.setStatus("current")
_SleCounterControlTimeStamp_Type = TimeTicks
_SleCounterControlTimeStamp_Object = MibScalar
sleCounterControlTimeStamp = _SleCounterControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 6, 2, 4),
    _SleCounterControlTimeStamp_Type()
)
sleCounterControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCounterControlTimeStamp.setStatus("current")
_SleCounterControlReqResult_Type = SleControlRequestResultType
_SleCounterControlReqResult_Object = MibScalar
sleCounterControlReqResult = _SleCounterControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 6, 2, 5),
    _SleCounterControlReqResult_Type()
)
sleCounterControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCounterControlReqResult.setStatus("current")


class _SleCounterControlIndex_Type(Unsigned32):
    """Custom type sleCounterControlIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleCounterControlIndex_Type.__name__ = "Unsigned32"
_SleCounterControlIndex_Object = MibScalar
sleCounterControlIndex = _SleCounterControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 6, 2, 6),
    _SleCounterControlIndex_Type()
)
sleCounterControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCounterControlIndex.setStatus("current")
_SleCounterNotification_ObjectIdentity = ObjectIdentity
sleCounterNotification = _SleCounterNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 6, 3)
)
_SleColorMarking_ObjectIdentity = ObjectIdentity
sleColorMarking = _SleColorMarking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7)
)
_SleColorMarkingTable_Object = MibTable
sleColorMarkingTable = _SleColorMarkingTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 1)
)
if mibBuilder.loadTexts:
    sleColorMarkingTable.setStatus("current")
_SleColorMarkingEntry_Object = MibTableRow
sleColorMarkingEntry = _SleColorMarkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 1, 1)
)
sleColorMarkingEntry.setIndexNames(
    (0, "SLE-QOS-MIB", "sleColorMarkingIndex"),
)
if mibBuilder.loadTexts:
    sleColorMarkingEntry.setStatus("current")


class _SleColorMarkingIndex_Type(Integer32):
    """Custom type sleColorMarkingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_SleColorMarkingIndex_Type.__name__ = "Integer32"
_SleColorMarkingIndex_Object = MibTableColumn
sleColorMarkingIndex = _SleColorMarkingIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 1, 1, 1),
    _SleColorMarkingIndex_Type()
)
sleColorMarkingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleColorMarkingIndex.setStatus("current")


class _SleColorMarkingType_Type(Integer32):
    """Custom type sleColorMarkingType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("srTCM", 0),
          ("trTCM", 1))
    )


_SleColorMarkingType_Type.__name__ = "Integer32"
_SleColorMarkingType_Object = MibTableColumn
sleColorMarkingType = _SleColorMarkingType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 1, 1, 2),
    _SleColorMarkingType_Type()
)
sleColorMarkingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleColorMarkingType.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingType.setUnits("Enum")


class _SleColorMarkingMode_Type(Integer32):
    """Custom type sleColorMarkingMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("blind", 0),
          ("aware", 1))
    )


_SleColorMarkingMode_Type.__name__ = "Integer32"
_SleColorMarkingMode_Object = MibTableColumn
sleColorMarkingMode = _SleColorMarkingMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 1, 1, 3),
    _SleColorMarkingMode_Type()
)
sleColorMarkingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleColorMarkingMode.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingMode.setUnits("Enum")


class _SleColorMarkingAwareMode_Type(Integer32):
    """Custom type sleColorMarkingAwareMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unprotected", 1),
          ("protected", 2))
    )


_SleColorMarkingAwareMode_Type.__name__ = "Integer32"
_SleColorMarkingAwareMode_Object = MibTableColumn
sleColorMarkingAwareMode = _SleColorMarkingAwareMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 1, 1, 4),
    _SleColorMarkingAwareMode_Type()
)
sleColorMarkingAwareMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleColorMarkingAwareMode.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingAwareMode.setUnits("Enum")


class _SleColorMarkingCIR_Type(Integer32):
    """Custom type sleColorMarkingCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_SleColorMarkingCIR_Type.__name__ = "Integer32"
_SleColorMarkingCIR_Object = MibTableColumn
sleColorMarkingCIR = _SleColorMarkingCIR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 1, 1, 5),
    _SleColorMarkingCIR_Type()
)
sleColorMarkingCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleColorMarkingCIR.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingCIR.setUnits("Integer")


class _SleColorMarkingCBS_Type(Integer32):
    """Custom type sleColorMarkingCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_SleColorMarkingCBS_Type.__name__ = "Integer32"
_SleColorMarkingCBS_Object = MibTableColumn
sleColorMarkingCBS = _SleColorMarkingCBS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 1, 1, 6),
    _SleColorMarkingCBS_Type()
)
sleColorMarkingCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleColorMarkingCBS.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingCBS.setUnits("Integer")


class _SleColorMarkingPIR_Type(Integer32):
    """Custom type sleColorMarkingPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_SleColorMarkingPIR_Type.__name__ = "Integer32"
_SleColorMarkingPIR_Object = MibTableColumn
sleColorMarkingPIR = _SleColorMarkingPIR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 1, 1, 7),
    _SleColorMarkingPIR_Type()
)
sleColorMarkingPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleColorMarkingPIR.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingPIR.setUnits("Integer ")


class _SleColorMarkingPBS_Type(Integer32):
    """Custom type sleColorMarkingPBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_SleColorMarkingPBS_Type.__name__ = "Integer32"
_SleColorMarkingPBS_Object = MibTableColumn
sleColorMarkingPBS = _SleColorMarkingPBS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 1, 1, 8),
    _SleColorMarkingPBS_Type()
)
sleColorMarkingPBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleColorMarkingPBS.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingPBS.setUnits("Integer ")


class _SleColorMarkingEBS_Type(Integer32):
    """Custom type sleColorMarkingEBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_SleColorMarkingEBS_Type.__name__ = "Integer32"
_SleColorMarkingEBS_Object = MibTableColumn
sleColorMarkingEBS = _SleColorMarkingEBS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 1, 1, 9),
    _SleColorMarkingEBS_Type()
)
sleColorMarkingEBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleColorMarkingEBS.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingEBS.setUnits("Integer ")


class _SleColorMarkingRedAction_Type(Bits):
    """Custom type sleColorMarkingRedAction based on Bits"""
    namedValues = NamedValues(
        *(("reserve0", 0),
          ("reserve1", 1),
          ("reserve2", 2),
          ("reserve3", 3),
          ("reserve4", 4),
          ("dropProcedence", 5),
          ("marking", 6),
          ("drop", 7),
          ("dropPrecedenceGreen", 8),
          ("dropPrecedenceYellow", 9),
          ("dropPrecedenceRed", 10))
    )

_SleColorMarkingRedAction_Type.__name__ = "Bits"
_SleColorMarkingRedAction_Object = MibTableColumn
sleColorMarkingRedAction = _SleColorMarkingRedAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 1, 1, 10),
    _SleColorMarkingRedAction_Type()
)
sleColorMarkingRedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleColorMarkingRedAction.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingRedAction.setUnits("bits")


class _SleColorMarkingYellowAction_Type(Bits):
    """Custom type sleColorMarkingYellowAction based on Bits"""
    namedValues = NamedValues(
        *(("reserve0", 0),
          ("reserve1", 1),
          ("reserve2", 2),
          ("reserve3", 3),
          ("reserve4", 4),
          ("dropProcedence", 5),
          ("marking", 6),
          ("drop", 7),
          ("dropPrecedenceGreen", 8),
          ("dropPrecedenceYellow", 9),
          ("dropPrecedenceRed", 10))
    )

_SleColorMarkingYellowAction_Type.__name__ = "Bits"
_SleColorMarkingYellowAction_Object = MibTableColumn
sleColorMarkingYellowAction = _SleColorMarkingYellowAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 1, 1, 11),
    _SleColorMarkingYellowAction_Type()
)
sleColorMarkingYellowAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleColorMarkingYellowAction.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingYellowAction.setUnits("bits")


class _SleColorMarkingGreenAction_Type(Bits):
    """Custom type sleColorMarkingGreenAction based on Bits"""
    namedValues = NamedValues(
        *(("reserve0", 0),
          ("reserve1", 1),
          ("reserve2", 2),
          ("reserve3", 3),
          ("reserve4", 4),
          ("dropProcedence", 5),
          ("marking", 6),
          ("drop", 7),
          ("dropPrecedenceGreen", 8),
          ("dropPrecedenceYellow", 9),
          ("dropPrecedenceRed", 10))
    )

_SleColorMarkingGreenAction_Type.__name__ = "Bits"
_SleColorMarkingGreenAction_Object = MibTableColumn
sleColorMarkingGreenAction = _SleColorMarkingGreenAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 1, 1, 12),
    _SleColorMarkingGreenAction_Type()
)
sleColorMarkingGreenAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleColorMarkingGreenAction.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingGreenAction.setUnits("bits")


class _SleColorMarkingRedDscp_Type(Integer32):
    """Custom type sleColorMarkingRedDscp based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleColorMarkingRedDscp_Type.__name__ = "Integer32"
_SleColorMarkingRedDscp_Object = MibTableColumn
sleColorMarkingRedDscp = _SleColorMarkingRedDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 1, 1, 13),
    _SleColorMarkingRedDscp_Type()
)
sleColorMarkingRedDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleColorMarkingRedDscp.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingRedDscp.setUnits("Integer ")


class _SleColorMarkingYellowDscp_Type(Integer32):
    """Custom type sleColorMarkingYellowDscp based on Integer32"""
    defaultValue = 28

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleColorMarkingYellowDscp_Type.__name__ = "Integer32"
_SleColorMarkingYellowDscp_Object = MibTableColumn
sleColorMarkingYellowDscp = _SleColorMarkingYellowDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 1, 1, 14),
    _SleColorMarkingYellowDscp_Type()
)
sleColorMarkingYellowDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleColorMarkingYellowDscp.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingYellowDscp.setUnits("Integer ")


class _SleColorMarkingGreenDscp_Type(Integer32):
    """Custom type sleColorMarkingGreenDscp based on Integer32"""
    defaultValue = 26

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleColorMarkingGreenDscp_Type.__name__ = "Integer32"
_SleColorMarkingGreenDscp_Object = MibTableColumn
sleColorMarkingGreenDscp = _SleColorMarkingGreenDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 1, 1, 15),
    _SleColorMarkingGreenDscp_Type()
)
sleColorMarkingGreenDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleColorMarkingGreenDscp.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingGreenDscp.setUnits("Integer ")


class _SleColorMarkingUseCount_Type(Integer32):
    """Custom type sleColorMarkingUseCount based on Integer32"""
    defaultValue = 0


_SleColorMarkingUseCount_Type.__name__ = "Integer32"
_SleColorMarkingUseCount_Object = MibTableColumn
sleColorMarkingUseCount = _SleColorMarkingUseCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 1, 1, 16),
    _SleColorMarkingUseCount_Type()
)
sleColorMarkingUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleColorMarkingUseCount.setStatus("current")
_SleColorMarkingControl_ObjectIdentity = ObjectIdentity
sleColorMarkingControl = _SleColorMarkingControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2)
)


class _SleColorMarkingControlReqest_Type(Integer32):
    """Custom type sleColorMarkingControlReqest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setColorMarkingProfile", 1)
    )


_SleColorMarkingControlReqest_Type.__name__ = "Integer32"
_SleColorMarkingControlReqest_Object = MibScalar
sleColorMarkingControlReqest = _SleColorMarkingControlReqest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 1),
    _SleColorMarkingControlReqest_Type()
)
sleColorMarkingControlReqest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlReqest.setStatus("current")
_SleColorMarkingControlStatus_Type = SleControlStatusType
_SleColorMarkingControlStatus_Object = MibScalar
sleColorMarkingControlStatus = _SleColorMarkingControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 2),
    _SleColorMarkingControlStatus_Type()
)
sleColorMarkingControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlStatus.setStatus("current")
_SleColorMarkingControlTimer_Type = Gauge32
_SleColorMarkingControlTimer_Object = MibScalar
sleColorMarkingControlTimer = _SleColorMarkingControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 3),
    _SleColorMarkingControlTimer_Type()
)
sleColorMarkingControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlTimer.setStatus("current")
_SleColorMarkingControlTimeStamp_Type = TimeTicks
_SleColorMarkingControlTimeStamp_Object = MibScalar
sleColorMarkingControlTimeStamp = _SleColorMarkingControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 4),
    _SleColorMarkingControlTimeStamp_Type()
)
sleColorMarkingControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleColorMarkingControlTimeStamp.setStatus("current")
_SleColorMarkingControlReqResult_Type = SleControlRequestResultType
_SleColorMarkingControlReqResult_Object = MibScalar
sleColorMarkingControlReqResult = _SleColorMarkingControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 5),
    _SleColorMarkingControlReqResult_Type()
)
sleColorMarkingControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlReqResult.setStatus("current")


class _SleColorMarkingControlIndex_Type(Integer32):
    """Custom type sleColorMarkingControlIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_SleColorMarkingControlIndex_Type.__name__ = "Integer32"
_SleColorMarkingControlIndex_Object = MibScalar
sleColorMarkingControlIndex = _SleColorMarkingControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 6),
    _SleColorMarkingControlIndex_Type()
)
sleColorMarkingControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlIndex.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingControlIndex.setUnits("index")


class _SleColorMarkingControlType_Type(Integer32):
    """Custom type sleColorMarkingControlType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("srTCM", 0),
          ("trTCM", 1))
    )


_SleColorMarkingControlType_Type.__name__ = "Integer32"
_SleColorMarkingControlType_Object = MibScalar
sleColorMarkingControlType = _SleColorMarkingControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 7),
    _SleColorMarkingControlType_Type()
)
sleColorMarkingControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlType.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingControlType.setUnits("enum")


class _SleColorMarkingControlMode_Type(Integer32):
    """Custom type sleColorMarkingControlMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("blind", 0),
          ("aware", 1))
    )


_SleColorMarkingControlMode_Type.__name__ = "Integer32"
_SleColorMarkingControlMode_Object = MibScalar
sleColorMarkingControlMode = _SleColorMarkingControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 8),
    _SleColorMarkingControlMode_Type()
)
sleColorMarkingControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlMode.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingControlMode.setUnits("enum")


class _SleColorMarkingControlAwareMode_Type(Integer32):
    """Custom type sleColorMarkingControlAwareMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unprotected", 1),
          ("protected", 2))
    )


_SleColorMarkingControlAwareMode_Type.__name__ = "Integer32"
_SleColorMarkingControlAwareMode_Object = MibScalar
sleColorMarkingControlAwareMode = _SleColorMarkingControlAwareMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 9),
    _SleColorMarkingControlAwareMode_Type()
)
sleColorMarkingControlAwareMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlAwareMode.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingControlAwareMode.setUnits("enum")


class _SleColorMarkingControlCIR_Type(Integer32):
    """Custom type sleColorMarkingControlCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_SleColorMarkingControlCIR_Type.__name__ = "Integer32"
_SleColorMarkingControlCIR_Object = MibScalar
sleColorMarkingControlCIR = _SleColorMarkingControlCIR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 10),
    _SleColorMarkingControlCIR_Type()
)
sleColorMarkingControlCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlCIR.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingControlCIR.setUnits("Integer")


class _SleColorMarkingControlCBS_Type(Integer32):
    """Custom type sleColorMarkingControlCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_SleColorMarkingControlCBS_Type.__name__ = "Integer32"
_SleColorMarkingControlCBS_Object = MibScalar
sleColorMarkingControlCBS = _SleColorMarkingControlCBS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 11),
    _SleColorMarkingControlCBS_Type()
)
sleColorMarkingControlCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlCBS.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingControlCBS.setUnits("Integer ")


class _SleColorMarkingControlPIR_Type(Integer32):
    """Custom type sleColorMarkingControlPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_SleColorMarkingControlPIR_Type.__name__ = "Integer32"
_SleColorMarkingControlPIR_Object = MibScalar
sleColorMarkingControlPIR = _SleColorMarkingControlPIR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 12),
    _SleColorMarkingControlPIR_Type()
)
sleColorMarkingControlPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlPIR.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingControlPIR.setUnits("Integer ")


class _SleColorMarkingControlPBS_Type(Integer32):
    """Custom type sleColorMarkingControlPBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_SleColorMarkingControlPBS_Type.__name__ = "Integer32"
_SleColorMarkingControlPBS_Object = MibScalar
sleColorMarkingControlPBS = _SleColorMarkingControlPBS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 13),
    _SleColorMarkingControlPBS_Type()
)
sleColorMarkingControlPBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlPBS.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingControlPBS.setUnits("Integer ")


class _SleColorMarkingControlEBS_Type(Integer32):
    """Custom type sleColorMarkingControlEBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_SleColorMarkingControlEBS_Type.__name__ = "Integer32"
_SleColorMarkingControlEBS_Object = MibScalar
sleColorMarkingControlEBS = _SleColorMarkingControlEBS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 14),
    _SleColorMarkingControlEBS_Type()
)
sleColorMarkingControlEBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlEBS.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingControlEBS.setUnits("Integer ")


class _SleColorMarkingControlRedAction_Type(Bits):
    """Custom type sleColorMarkingControlRedAction based on Bits"""
    namedValues = NamedValues(
        *(("reserve0", 0),
          ("reserve1", 1),
          ("reserve2", 2),
          ("reserve3", 3),
          ("reserve4", 4),
          ("dropProcedence", 5),
          ("marking", 6),
          ("drop", 7),
          ("dropPrecedenceGreen", 8),
          ("dropPrecedenceYellow", 9),
          ("dropPrecedenceRed", 10))
    )

_SleColorMarkingControlRedAction_Type.__name__ = "Bits"
_SleColorMarkingControlRedAction_Object = MibScalar
sleColorMarkingControlRedAction = _SleColorMarkingControlRedAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 15),
    _SleColorMarkingControlRedAction_Type()
)
sleColorMarkingControlRedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlRedAction.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingControlRedAction.setUnits("bits")


class _SleColorMarkingControlYellowAction_Type(Bits):
    """Custom type sleColorMarkingControlYellowAction based on Bits"""
    namedValues = NamedValues(
        *(("reserve0", 0),
          ("reserve1", 1),
          ("reserve2", 2),
          ("reserve3", 3),
          ("reserve4", 4),
          ("dropProcedence", 5),
          ("marking", 6),
          ("drop", 7),
          ("dropPrecedenceGreen", 8),
          ("dropPrecedenceYellow", 9),
          ("dropPrecedenceRed", 10))
    )

_SleColorMarkingControlYellowAction_Type.__name__ = "Bits"
_SleColorMarkingControlYellowAction_Object = MibScalar
sleColorMarkingControlYellowAction = _SleColorMarkingControlYellowAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 16),
    _SleColorMarkingControlYellowAction_Type()
)
sleColorMarkingControlYellowAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlYellowAction.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingControlYellowAction.setUnits("bits")


class _SleColorMarkingControlGreenAction_Type(Bits):
    """Custom type sleColorMarkingControlGreenAction based on Bits"""
    namedValues = NamedValues(
        *(("reserve0", 0),
          ("reserve1", 1),
          ("reserve2", 2),
          ("reserve3", 3),
          ("reserve4", 4),
          ("dropProcedence", 5),
          ("marking", 6),
          ("drop", 7),
          ("dropPrecedenceGreen", 8),
          ("dropPrecedenceYellow", 9),
          ("dropPrecedenceRed", 10))
    )

_SleColorMarkingControlGreenAction_Type.__name__ = "Bits"
_SleColorMarkingControlGreenAction_Object = MibScalar
sleColorMarkingControlGreenAction = _SleColorMarkingControlGreenAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 17),
    _SleColorMarkingControlGreenAction_Type()
)
sleColorMarkingControlGreenAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlGreenAction.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingControlGreenAction.setUnits("bits")


class _SleColorMarkingControlRedDscp_Type(Integer32):
    """Custom type sleColorMarkingControlRedDscp based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleColorMarkingControlRedDscp_Type.__name__ = "Integer32"
_SleColorMarkingControlRedDscp_Object = MibScalar
sleColorMarkingControlRedDscp = _SleColorMarkingControlRedDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 18),
    _SleColorMarkingControlRedDscp_Type()
)
sleColorMarkingControlRedDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlRedDscp.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingControlRedDscp.setUnits("Integer")


class _SleColorMarkingControlYellowDscp_Type(Integer32):
    """Custom type sleColorMarkingControlYellowDscp based on Integer32"""
    defaultValue = 28

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleColorMarkingControlYellowDscp_Type.__name__ = "Integer32"
_SleColorMarkingControlYellowDscp_Object = MibScalar
sleColorMarkingControlYellowDscp = _SleColorMarkingControlYellowDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 19),
    _SleColorMarkingControlYellowDscp_Type()
)
sleColorMarkingControlYellowDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlYellowDscp.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingControlYellowDscp.setUnits("Integer ")


class _SleColorMarkingControlGreenDscp_Type(Integer32):
    """Custom type sleColorMarkingControlGreenDscp based on Integer32"""
    defaultValue = 26

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleColorMarkingControlGreenDscp_Type.__name__ = "Integer32"
_SleColorMarkingControlGreenDscp_Object = MibScalar
sleColorMarkingControlGreenDscp = _SleColorMarkingControlGreenDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 2, 20),
    _SleColorMarkingControlGreenDscp_Type()
)
sleColorMarkingControlGreenDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleColorMarkingControlGreenDscp.setStatus("current")
if mibBuilder.loadTexts:
    sleColorMarkingControlGreenDscp.setUnits("Integer ")
_SleColorMarkingNotification_ObjectIdentity = ObjectIdentity
sleColorMarkingNotification = _SleColorMarkingNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 3)
)

# Managed Objects groups

sleQoSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 8)
)
sleQoSGroup.setObjects(
      *(("SLE-QOS-MIB", "sleQosUserFlowNum"),
        ("SLE-QOS-MIB", "sleQosTrafficProfileNum"),
        ("SLE-QOS-MIB", "sleQosCounterNum"),
        ("SLE-QOS-MIB", "sleQosQueueNum"),
        ("SLE-QOS-MIB", "sleTrafficProfileIndex"),
        ("SLE-QOS-MIB", "sleTrafficProfileMinBandwidth"),
        ("SLE-QOS-MIB", "sleTrafficProfileMaxBandwidth"),
        ("SLE-QOS-MIB", "sleTrafficProfileMaxBurstSize"),
        ("SLE-QOS-MIB", "sleTrafficProfileUseCount"),
        ("SLE-QOS-MIB", "sleUserFlowName"),
        ("SLE-QOS-MIB", "sleUserFlowIngressPorts"),
        ("SLE-QOS-MIB", "sleUserFlowEgressPorts"),
        ("SLE-QOS-MIB", "sleUserFlowEthernetType"),
        ("SLE-QOS-MIB", "sleUserFlowSrcMacAddr"),
        ("SLE-QOS-MIB", "sleUserFlowDstMacAddr"),
        ("SLE-QOS-MIB", "sleUserFlowVlan"),
        ("SLE-QOS-MIB", "sleUserFlow8021p"),
        ("SLE-QOS-MIB", "sleUserFlowSrcIpAddr"),
        ("SLE-QOS-MIB", "sleUserFlowSrcPrefixLength"),
        ("SLE-QOS-MIB", "sleUserFlowDstIpAddr"),
        ("SLE-QOS-MIB", "sleUserFlowDstPrefixLength"),
        ("SLE-QOS-MIB", "sleUserFlowIpPktPriorityType"),
        ("SLE-QOS-MIB", "sleUserFlowIpPktPriority"),
        ("SLE-QOS-MIB", "sleUserFlowProtocolType"),
        ("SLE-QOS-MIB", "sleUserFlowTcpFlag"),
        ("SLE-QOS-MIB", "sleUserFlowSrcL4Port"),
        ("SLE-QOS-MIB", "sleUserFlowDstL4Port"),
        ("SLE-QOS-MIB", "sleUserFlowPktLen"),
        ("SLE-QOS-MIB", "sleUserFlowValidFlags"),
        ("SLE-QOS-MIB", "sleUserFlowMatchFlags"),
        ("SLE-QOS-MIB", "sleUserFlowPriority"),
        ("SLE-QOS-MIB", "sleUserFlowMatchCounterId"),
        ("SLE-QOS-MIB", "sleUserFlowMatchTrafficProfileId"),
        ("SLE-QOS-MIB", "sleUserFlowMatchQueue"),
        ("SLE-QOS-MIB", "sleUserFlowMatchIpPktPriorityType"),
        ("SLE-QOS-MIB", "sleUserFlowMatchIpPktPriority"),
        ("SLE-QOS-MIB", "sleUserFlowMatchRedirPort"),
        ("SLE-QOS-MIB", "sleUserFlowMatchVid"),
        ("SLE-QOS-MIB", "sleUserFlowMatchDstMac"),
        ("SLE-QOS-MIB", "sleUserFlowMatchPortMap"),
        ("SLE-QOS-MIB", "sleUserFlowMatchEgressType"),
        ("SLE-QOS-MIB", "sleUserFlowMatchAction"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchCounterId"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchTrafficProfileId"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchQueue"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchIpPktPriorityType"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchIpPktPriority"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchRedirPort"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchVid"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchAction"),
        ("SLE-QOS-MIB", "sleUserFlowMatchColorMarkingId"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchColorMarkingId"),
        ("SLE-QOS-MIB", "slePortSchedulInterfaceIndex"),
        ("SLE-QOS-MIB", "slePortScheduleMode"),
        ("SLE-QOS-MIB", "sleQueueId"),
        ("SLE-QOS-MIB", "sleQueueREDEnable"),
        ("SLE-QOS-MIB", "sleQueueMappedCoS"),
        ("SLE-QOS-MIB", "sleQueueWREDMinThreshold"),
        ("SLE-QOS-MIB", "sleQueueWREDMaxThreshold"),
        ("SLE-QOS-MIB", "sleQueueWREDProbMax"),
        ("SLE-QOS-MIB", "sleQueueMinBandwidth"),
        ("SLE-QOS-MIB", "sleQueueMaxBandwidth"),
        ("SLE-QOS-MIB", "sleQueueWeight"),
        ("SLE-QOS-MIB", "sleQueueMaxLatency"),
        ("SLE-QOS-MIB", "sleQueueMaxPackets"),
        ("SLE-QOS-MIB", "sleCounterIndex"),
        ("SLE-QOS-MIB", "sleCounterPackets"),
        ("SLE-QOS-MIB", "sleColorMarkingIndex"),
        ("SLE-QOS-MIB", "sleColorMarkingType"),
        ("SLE-QOS-MIB", "sleColorMarkingMode"),
        ("SLE-QOS-MIB", "sleColorMarkingAwareMode"),
        ("SLE-QOS-MIB", "sleColorMarkingCIR"),
        ("SLE-QOS-MIB", "sleColorMarkingCBS"),
        ("SLE-QOS-MIB", "sleColorMarkingPIR"),
        ("SLE-QOS-MIB", "sleColorMarkingPBS"),
        ("SLE-QOS-MIB", "sleColorMarkingEBS"),
        ("SLE-QOS-MIB", "sleColorMarkingRedAction"),
        ("SLE-QOS-MIB", "sleColorMarkingYellowAction"),
        ("SLE-QOS-MIB", "sleColorMarkingGreenAction"),
        ("SLE-QOS-MIB", "sleColorMarkingRedDscp"),
        ("SLE-QOS-MIB", "sleColorMarkingYellowDscp"),
        ("SLE-QOS-MIB", "sleColorMarkingGreenDscp"),
        ("SLE-QOS-MIB", "sleQosRuleMode"),
        ("SLE-QOS-MIB", "sleQoSBaseControlRequest"),
        ("SLE-QOS-MIB", "sleQoSBaseControlStatus"),
        ("SLE-QOS-MIB", "sleQoSBaseControlTimer"),
        ("SLE-QOS-MIB", "sleQoSBaseControlTimeStamp"),
        ("SLE-QOS-MIB", "sleQoSBaseControlReqResult"),
        ("SLE-QOS-MIB", "sleQoSBaseControlRuleMode"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlRequest"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlStatus"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlTimer"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlTimeStamp"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlReqResult"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlIndex"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlMinBandwidth"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlMaxBandwidth"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlMaxBurstSize"),
        ("SLE-QOS-MIB", "sleUserFlowMatchRoutePrimary"),
        ("SLE-QOS-MIB", "sleUserFlowMatchRouteSecondary"),
        ("SLE-QOS-MIB", "sleUserFlowControlReqest"),
        ("SLE-QOS-MIB", "sleUserFlowControlStatus"),
        ("SLE-QOS-MIB", "sleUserFlowControlTimer"),
        ("SLE-QOS-MIB", "sleUserFlowControlTimeStamp"),
        ("SLE-QOS-MIB", "sleUserFlowControlReqResult"),
        ("SLE-QOS-MIB", "sleUserFlowControlName"),
        ("SLE-QOS-MIB", "sleUserFlowControlIngressPorts"),
        ("SLE-QOS-MIB", "sleUserFlowControlEgressPorts"),
        ("SLE-QOS-MIB", "sleUserFlowControlEthernetType"),
        ("SLE-QOS-MIB", "sleUserFlowControlSrcMacAddr"),
        ("SLE-QOS-MIB", "sleUserFlowControlDstMacAddr"),
        ("SLE-QOS-MIB", "sleUserFlowControlVlan"),
        ("SLE-QOS-MIB", "sleUserFlowControl8021p"),
        ("SLE-QOS-MIB", "sleUserFlowControlSrcIpAddr"),
        ("SLE-QOS-MIB", "sleUserFlowControlSrcPrefixLength"),
        ("SLE-QOS-MIB", "sleUserFlowControlDstIpAddr"),
        ("SLE-QOS-MIB", "sleUserFlowControlDstPrefixLength"),
        ("SLE-QOS-MIB", "sleUserFlowControlIpPktPriorityType"),
        ("SLE-QOS-MIB", "sleUserFlowControlIpPktPriority"),
        ("SLE-QOS-MIB", "sleUserFlowControlProtocolType"),
        ("SLE-QOS-MIB", "sleUserFlowControlTcpFlag"),
        ("SLE-QOS-MIB", "sleUserFlowControlSrcL4Port"),
        ("SLE-QOS-MIB", "sleUserFlowControlDstL4Port"),
        ("SLE-QOS-MIB", "sleUserFlowControlPktLen"),
        ("SLE-QOS-MIB", "sleUserFlowControlValidFlag"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchFlag"),
        ("SLE-QOS-MIB", "sleUserFlowControlPriority"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchCounterId"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchTrafficProfileId"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchQueue"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchIpPktPriorityType"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchIpPktPriority"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchRedirPort"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchVid"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchDstMac"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchPortMap"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchEgressType"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchAction"),
        ("SLE-QOS-MIB", "sleUserFlowControlNomatchCounterId"),
        ("SLE-QOS-MIB", "sleUserFlowControlNomatchTrafficProfileId"),
        ("SLE-QOS-MIB", "sleUserFlowControlNomatchQueue"),
        ("SLE-QOS-MIB", "sleUserFlowControlNomatchIpPktPriorityType"),
        ("SLE-QOS-MIB", "sleUserFlowControlNomatchIpPktPriority"),
        ("SLE-QOS-MIB", "sleUserFlowControlNomatchRedirPort"),
        ("SLE-QOS-MIB", "sleUserFlowControlNomatchVid"),
        ("SLE-QOS-MIB", "sleUserFlowControlNomatchAction"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchColorMarkingId"),
        ("SLE-QOS-MIB", "sleUserFlowControlNomatchColorMarkingId"),
        ("SLE-QOS-MIB", "sleUserFlowControlInnerVlan"),
        ("SLE-QOS-MIB", "sleUserFlowControlInner8021p"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchRoutePrimary"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchRouteSecondary"),
        ("SLE-QOS-MIB", "slePortScheduleControlRequest"),
        ("SLE-QOS-MIB", "sleScheduleControlStatus"),
        ("SLE-QOS-MIB", "slePortScheduleControlTimer"),
        ("SLE-QOS-MIB", "slePortScheduleControlTimeStamp"),
        ("SLE-QOS-MIB", "slePortScheduleControlReqResult"),
        ("SLE-QOS-MIB", "slePortScheduleControlInterfaceIndex"),
        ("SLE-QOS-MIB", "slePortScheduleControlMode"),
        ("SLE-QOS-MIB", "sleQueueQuantum"),
        ("SLE-QOS-MIB", "sleQueueControlRequest"),
        ("SLE-QOS-MIB", "sleQueueControlStatus"),
        ("SLE-QOS-MIB", "sleQueueControlTimer"),
        ("SLE-QOS-MIB", "sleQueueControlTimeStamp"),
        ("SLE-QOS-MIB", "sleQueueControlReqResult"),
        ("SLE-QOS-MIB", "sleQueueControlInterfaceIndex"),
        ("SLE-QOS-MIB", "sleQueueControlId"),
        ("SLE-QOS-MIB", "sleQueueControlREDEnable"),
        ("SLE-QOS-MIB", "sleQueueControlMappedCoS"),
        ("SLE-QOS-MIB", "sleQueueControlWREDMinThreshold"),
        ("SLE-QOS-MIB", "sleQueueControlWREDMaxThreshold"),
        ("SLE-QOS-MIB", "sleQueueControlWREDProbMax"),
        ("SLE-QOS-MIB", "sleQueueControlMinBandwidth"),
        ("SLE-QOS-MIB", "sleQueueControlMaxBandwidth"),
        ("SLE-QOS-MIB", "sleQueueControlWeight"),
        ("SLE-QOS-MIB", "sleQueueControlMaxLatency"),
        ("SLE-QOS-MIB", "sleQueueControlMaxPackets"),
        ("SLE-QOS-MIB", "sleQueueControlQuantum"),
        ("SLE-QOS-MIB", "sleCounterControlRequest"),
        ("SLE-QOS-MIB", "sleCounterControlStatus"),
        ("SLE-QOS-MIB", "sleCounterControlTimer"),
        ("SLE-QOS-MIB", "sleCounterControlTimeStamp"),
        ("SLE-QOS-MIB", "sleCounterControlReqResult"),
        ("SLE-QOS-MIB", "sleCounterControlIndex"),
        ("SLE-QOS-MIB", "sleColorMarkingControlReqest"),
        ("SLE-QOS-MIB", "sleColorMarkingControlStatus"),
        ("SLE-QOS-MIB", "sleColorMarkingControlTimer"),
        ("SLE-QOS-MIB", "sleColorMarkingControlTimeStamp"),
        ("SLE-QOS-MIB", "sleColorMarkingControlReqResult"),
        ("SLE-QOS-MIB", "sleColorMarkingControlIndex"),
        ("SLE-QOS-MIB", "sleColorMarkingControlType"),
        ("SLE-QOS-MIB", "sleColorMarkingControlMode"),
        ("SLE-QOS-MIB", "sleColorMarkingControlAwareMode"),
        ("SLE-QOS-MIB", "sleColorMarkingControlCIR"),
        ("SLE-QOS-MIB", "sleColorMarkingControlCBS"),
        ("SLE-QOS-MIB", "sleColorMarkingControlPIR"),
        ("SLE-QOS-MIB", "sleColorMarkingControlPBS"),
        ("SLE-QOS-MIB", "sleColorMarkingControlEBS"),
        ("SLE-QOS-MIB", "sleColorMarkingControlRedAction"),
        ("SLE-QOS-MIB", "sleColorMarkingControlYellowAction"),
        ("SLE-QOS-MIB", "sleColorMarkingControlGreenAction"),
        ("SLE-QOS-MIB", "sleColorMarkingControlRedDscp"),
        ("SLE-QOS-MIB", "sleColorMarkingControlYellowDscp"),
        ("SLE-QOS-MIB", "sleColorMarkingControlGreenDscp"),
        ("SLE-QOS-MIB", "sleQueueUsedPkts"),
        ("SLE-QOS-MIB", "sleQueueUsedBytes"),
        ("SLE-QOS-MIB", "sleColorMarkingUseCount"),
        ("SLE-QOS-MIB", "sleQosColorMarkingProfileNum"),
        ("SLE-QOS-MIB", "sleUserFlowInnerVlan"),
        ("SLE-QOS-MIB", "sleUserFlowInner8021p"))
)
if mibBuilder.loadTexts:
    sleQoSGroup.setStatus("current")

sleQoSControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 9)
)
sleQoSControlGroup.setObjects(
      *(("SLE-QOS-MIB", "sleTrafficProfileControlRequest"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlStatus"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlTimer"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlTimeStamp"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlReqResult"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlIndex"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlMinBandwidth"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlMaxBandwidth"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlMaxBurstSize"),
        ("SLE-QOS-MIB", "sleUserFlowControlReqest"),
        ("SLE-QOS-MIB", "sleUserFlowControlStatus"),
        ("SLE-QOS-MIB", "sleUserFlowControlTimer"),
        ("SLE-QOS-MIB", "sleUserFlowControlTimeStamp"),
        ("SLE-QOS-MIB", "sleUserFlowControlReqResult"),
        ("SLE-QOS-MIB", "sleUserFlowControlName"),
        ("SLE-QOS-MIB", "sleUserFlowControlIngressPorts"),
        ("SLE-QOS-MIB", "sleUserFlowControlEgressPorts"),
        ("SLE-QOS-MIB", "sleUserFlowControlEthernetType"),
        ("SLE-QOS-MIB", "sleUserFlowControlSrcMacAddr"),
        ("SLE-QOS-MIB", "sleUserFlowControlDstMacAddr"),
        ("SLE-QOS-MIB", "sleUserFlowControlVlan"),
        ("SLE-QOS-MIB", "sleUserFlowControl8021p"),
        ("SLE-QOS-MIB", "sleUserFlowControlSrcIpAddr"),
        ("SLE-QOS-MIB", "sleUserFlowControlSrcPrefixLength"),
        ("SLE-QOS-MIB", "sleUserFlowControlDstIpAddr"),
        ("SLE-QOS-MIB", "sleUserFlowControlDstPrefixLength"),
        ("SLE-QOS-MIB", "sleUserFlowControlIpPktPriorityType"),
        ("SLE-QOS-MIB", "sleUserFlowControlIpPktPriority"),
        ("SLE-QOS-MIB", "sleUserFlowControlProtocolType"),
        ("SLE-QOS-MIB", "sleUserFlowControlTcpFlag"),
        ("SLE-QOS-MIB", "sleUserFlowControlSrcL4Port"),
        ("SLE-QOS-MIB", "sleUserFlowControlDstL4Port"),
        ("SLE-QOS-MIB", "sleUserFlowControlPktLen"),
        ("SLE-QOS-MIB", "sleUserFlowControlValidFlag"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchFlag"),
        ("SLE-QOS-MIB", "sleUserFlowControlPriority"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchCounterId"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchTrafficProfileId"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchQueue"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchIpPktPriorityType"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchIpPktPriority"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchRedirPort"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchVid"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchDstMac"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchPortMap"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchEgressType"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchAction"),
        ("SLE-QOS-MIB", "sleUserFlowControlNomatchCounterId"),
        ("SLE-QOS-MIB", "sleUserFlowControlNomatchTrafficProfileId"),
        ("SLE-QOS-MIB", "sleUserFlowControlNomatchQueue"),
        ("SLE-QOS-MIB", "sleUserFlowControlNomatchIpPktPriorityType"),
        ("SLE-QOS-MIB", "sleUserFlowControlNomatchIpPktPriority"),
        ("SLE-QOS-MIB", "sleUserFlowControlNomatchRedirPort"),
        ("SLE-QOS-MIB", "sleUserFlowControlNomatchVid"),
        ("SLE-QOS-MIB", "sleUserFlowControlNomatchAction"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchColorMarkingId"),
        ("SLE-QOS-MIB", "sleUserFlowControlNomatchColorMarkingId"),
        ("SLE-QOS-MIB", "sleQueueControlRequest"),
        ("SLE-QOS-MIB", "sleQueueControlStatus"),
        ("SLE-QOS-MIB", "sleQueueControlTimer"),
        ("SLE-QOS-MIB", "sleQueueControlTimeStamp"),
        ("SLE-QOS-MIB", "sleQueueControlReqResult"),
        ("SLE-QOS-MIB", "sleQueueControlInterfaceIndex"),
        ("SLE-QOS-MIB", "sleQueueControlId"),
        ("SLE-QOS-MIB", "sleQueueControlREDEnable"),
        ("SLE-QOS-MIB", "sleQueueControlMappedCoS"),
        ("SLE-QOS-MIB", "sleQueueControlWREDMinThreshold"),
        ("SLE-QOS-MIB", "sleQueueControlWREDMaxThreshold"),
        ("SLE-QOS-MIB", "sleQueueControlWREDProbMax"),
        ("SLE-QOS-MIB", "sleQueueControlMinBandwidth"),
        ("SLE-QOS-MIB", "sleQueueControlMaxBandwidth"),
        ("SLE-QOS-MIB", "sleQueueControlWeight"),
        ("SLE-QOS-MIB", "sleQueueControlMaxLatency"),
        ("SLE-QOS-MIB", "sleUserFlowControlInnerVlan"),
        ("SLE-QOS-MIB", "sleUserFlowControlInner8021p"),
        ("SLE-QOS-MIB", "sleQosUserFlowNum"),
        ("SLE-QOS-MIB", "sleQosTrafficProfileNum"),
        ("SLE-QOS-MIB", "sleQosCounterNum"),
        ("SLE-QOS-MIB", "sleQosQueueNum"),
        ("SLE-QOS-MIB", "sleQosColorMarkingProfileNum"),
        ("SLE-QOS-MIB", "sleQosRuleMode"),
        ("SLE-QOS-MIB", "sleQoSBaseControlRequest"),
        ("SLE-QOS-MIB", "sleQoSBaseControlStatus"),
        ("SLE-QOS-MIB", "sleQoSBaseControlTimer"),
        ("SLE-QOS-MIB", "sleQoSBaseControlTimeStamp"),
        ("SLE-QOS-MIB", "sleQoSBaseControlReqResult"),
        ("SLE-QOS-MIB", "sleQoSBaseControlRuleMode"),
        ("SLE-QOS-MIB", "sleTrafficProfileIndex"),
        ("SLE-QOS-MIB", "sleTrafficProfileMinBandwidth"),
        ("SLE-QOS-MIB", "sleTrafficProfileMaxBandwidth"),
        ("SLE-QOS-MIB", "sleTrafficProfileMaxBurstSize"),
        ("SLE-QOS-MIB", "sleTrafficProfileUseCount"),
        ("SLE-QOS-MIB", "sleUserFlowName"),
        ("SLE-QOS-MIB", "sleUserFlowIngressPorts"),
        ("SLE-QOS-MIB", "sleUserFlowEgressPorts"),
        ("SLE-QOS-MIB", "sleUserFlowEthernetType"),
        ("SLE-QOS-MIB", "sleUserFlowSrcMacAddr"),
        ("SLE-QOS-MIB", "sleUserFlowDstMacAddr"),
        ("SLE-QOS-MIB", "sleUserFlowVlan"),
        ("SLE-QOS-MIB", "sleUserFlow8021p"),
        ("SLE-QOS-MIB", "sleUserFlowSrcIpAddr"),
        ("SLE-QOS-MIB", "sleUserFlowSrcPrefixLength"),
        ("SLE-QOS-MIB", "sleUserFlowDstIpAddr"),
        ("SLE-QOS-MIB", "sleUserFlowDstPrefixLength"),
        ("SLE-QOS-MIB", "sleUserFlowIpPktPriorityType"),
        ("SLE-QOS-MIB", "sleUserFlowIpPktPriority"),
        ("SLE-QOS-MIB", "sleUserFlowProtocolType"),
        ("SLE-QOS-MIB", "sleUserFlowTcpFlag"),
        ("SLE-QOS-MIB", "sleUserFlowSrcL4Port"),
        ("SLE-QOS-MIB", "sleUserFlowDstL4Port"),
        ("SLE-QOS-MIB", "sleUserFlowPktLen"),
        ("SLE-QOS-MIB", "sleUserFlowValidFlags"),
        ("SLE-QOS-MIB", "sleUserFlowMatchFlags"),
        ("SLE-QOS-MIB", "sleUserFlowPriority"),
        ("SLE-QOS-MIB", "sleUserFlowMatchCounterId"),
        ("SLE-QOS-MIB", "sleUserFlowMatchTrafficProfileId"),
        ("SLE-QOS-MIB", "sleUserFlowMatchQueue"),
        ("SLE-QOS-MIB", "sleUserFlowMatchIpPktPriorityType"),
        ("SLE-QOS-MIB", "sleUserFlowMatchIpPktPriority"),
        ("SLE-QOS-MIB", "sleUserFlowMatchRedirPort"),
        ("SLE-QOS-MIB", "sleUserFlowMatchVid"),
        ("SLE-QOS-MIB", "sleUserFlowMatchDstMac"),
        ("SLE-QOS-MIB", "sleUserFlowMatchPortMap"),
        ("SLE-QOS-MIB", "sleUserFlowMatchEgressType"),
        ("SLE-QOS-MIB", "sleUserFlowMatchAction"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchCounterId"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchTrafficProfileId"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchQueue"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchIpPktPriorityType"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchIpPktPriority"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchRedirPort"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchVid"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchAction"),
        ("SLE-QOS-MIB", "sleUserFlowMatchColorMarkingId"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchColorMarkingId"),
        ("SLE-QOS-MIB", "sleUserFlowInnerVlan"),
        ("SLE-QOS-MIB", "sleUserFlowInner8021p"),
        ("SLE-QOS-MIB", "sleUserFlowMatchRoutePrimary"),
        ("SLE-QOS-MIB", "sleUserFlowMatchRouteSecondary"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchRoutePrimary"),
        ("SLE-QOS-MIB", "sleUserFlowControlMatchRouteSecondary"),
        ("SLE-QOS-MIB", "slePortSchedulInterfaceIndex"),
        ("SLE-QOS-MIB", "slePortScheduleMode"),
        ("SLE-QOS-MIB", "sleQueueId"),
        ("SLE-QOS-MIB", "sleQueueREDEnable"),
        ("SLE-QOS-MIB", "sleQueueMappedCoS"),
        ("SLE-QOS-MIB", "sleQueueWREDMinThreshold"),
        ("SLE-QOS-MIB", "sleQueueWREDMaxThreshold"),
        ("SLE-QOS-MIB", "sleQueueWREDProbMax"),
        ("SLE-QOS-MIB", "sleQueueMinBandwidth"),
        ("SLE-QOS-MIB", "sleQueueMaxBandwidth"),
        ("SLE-QOS-MIB", "sleQueueWeight"),
        ("SLE-QOS-MIB", "sleQueueMaxLatency"),
        ("SLE-QOS-MIB", "sleQueueMaxPackets"),
        ("SLE-QOS-MIB", "sleQueueQuantum"),
        ("SLE-QOS-MIB", "sleQueueControlQuantum"),
        ("SLE-QOS-MIB", "sleCounterIndex"),
        ("SLE-QOS-MIB", "sleCounterPackets"),
        ("SLE-QOS-MIB", "sleColorMarkingIndex"),
        ("SLE-QOS-MIB", "sleColorMarkingType"),
        ("SLE-QOS-MIB", "sleColorMarkingMode"),
        ("SLE-QOS-MIB", "sleColorMarkingAwareMode"),
        ("SLE-QOS-MIB", "sleColorMarkingCIR"),
        ("SLE-QOS-MIB", "sleColorMarkingCBS"),
        ("SLE-QOS-MIB", "sleColorMarkingPIR"),
        ("SLE-QOS-MIB", "sleColorMarkingPBS"),
        ("SLE-QOS-MIB", "sleColorMarkingEBS"),
        ("SLE-QOS-MIB", "sleColorMarkingRedAction"),
        ("SLE-QOS-MIB", "sleColorMarkingYellowAction"),
        ("SLE-QOS-MIB", "sleColorMarkingGreenAction"),
        ("SLE-QOS-MIB", "sleColorMarkingRedDscp"),
        ("SLE-QOS-MIB", "sleColorMarkingYellowDscp"),
        ("SLE-QOS-MIB", "sleColorMarkingGreenDscp"),
        ("SLE-QOS-MIB", "sleColorMarkingUseCount"),
        ("SLE-QOS-MIB", "sleQueueControlMaxPackets"),
        ("SLE-QOS-MIB", "slePortScheduleControlRequest"),
        ("SLE-QOS-MIB", "sleScheduleControlStatus"),
        ("SLE-QOS-MIB", "slePortScheduleControlTimer"),
        ("SLE-QOS-MIB", "slePortScheduleControlTimeStamp"),
        ("SLE-QOS-MIB", "slePortScheduleControlReqResult"),
        ("SLE-QOS-MIB", "slePortScheduleControlInterfaceIndex"),
        ("SLE-QOS-MIB", "slePortScheduleControlMode"),
        ("SLE-QOS-MIB", "sleCounterControlRequest"),
        ("SLE-QOS-MIB", "sleCounterControlStatus"),
        ("SLE-QOS-MIB", "sleCounterControlTimer"),
        ("SLE-QOS-MIB", "sleCounterControlTimeStamp"),
        ("SLE-QOS-MIB", "sleCounterControlReqResult"),
        ("SLE-QOS-MIB", "sleCounterControlIndex"),
        ("SLE-QOS-MIB", "sleColorMarkingControlReqest"),
        ("SLE-QOS-MIB", "sleColorMarkingControlStatus"),
        ("SLE-QOS-MIB", "sleColorMarkingControlTimer"),
        ("SLE-QOS-MIB", "sleColorMarkingControlTimeStamp"),
        ("SLE-QOS-MIB", "sleColorMarkingControlReqResult"),
        ("SLE-QOS-MIB", "sleColorMarkingControlIndex"),
        ("SLE-QOS-MIB", "sleColorMarkingControlType"),
        ("SLE-QOS-MIB", "sleColorMarkingControlMode"),
        ("SLE-QOS-MIB", "sleColorMarkingControlAwareMode"),
        ("SLE-QOS-MIB", "sleColorMarkingControlCIR"),
        ("SLE-QOS-MIB", "sleColorMarkingControlCBS"),
        ("SLE-QOS-MIB", "sleColorMarkingControlPIR"),
        ("SLE-QOS-MIB", "sleColorMarkingControlPBS"),
        ("SLE-QOS-MIB", "sleColorMarkingControlEBS"),
        ("SLE-QOS-MIB", "sleColorMarkingControlRedAction"),
        ("SLE-QOS-MIB", "sleColorMarkingControlYellowAction"),
        ("SLE-QOS-MIB", "sleColorMarkingControlGreenAction"),
        ("SLE-QOS-MIB", "sleColorMarkingControlRedDscp"),
        ("SLE-QOS-MIB", "sleColorMarkingControlYellowDscp"),
        ("SLE-QOS-MIB", "sleColorMarkingControlGreenDscp"))
)
if mibBuilder.loadTexts:
    sleQoSControlGroup.setStatus("current")


# Notification objects

sleQoSBaseRuleModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 1, 3, 1)
)
sleQoSBaseRuleModeChanged.setObjects(
      *(("SLE-QOS-MIB", "sleQoSBaseControlRequest"),
        ("SLE-QOS-MIB", "sleQoSBaseControlTimeStamp"),
        ("SLE-QOS-MIB", "sleQoSBaseControlReqResult"),
        ("SLE-QOS-MIB", "sleQosRuleMode"))
)
if mibBuilder.loadTexts:
    sleQoSBaseRuleModeChanged.setStatus(
        "current"
    )

sleTrafficProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 2, 3, 1)
)
sleTrafficProfileChanged.setObjects(
      *(("SLE-QOS-MIB", "sleTrafficProfileMinBandwidth"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlTimeStamp"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlReqResult"),
        ("SLE-QOS-MIB", "sleTrafficProfileControlRequest"),
        ("SLE-QOS-MIB", "sleTrafficProfileMaxBurstSize"),
        ("SLE-QOS-MIB", "sleTrafficProfileMaxBandwidth"))
)
if mibBuilder.loadTexts:
    sleTrafficProfileChanged.setStatus(
        "current"
    )

sleUserFlowCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 3, 1)
)
sleUserFlowCreated.setObjects(
      *(("SLE-QOS-MIB", "sleUserFlowControlReqest"),
        ("SLE-QOS-MIB", "sleUserFlowControlTimeStamp"),
        ("SLE-QOS-MIB", "sleUserFlowControlReqResult"),
        ("SLE-QOS-MIB", "sleUserFlowControlName"))
)
if mibBuilder.loadTexts:
    sleUserFlowCreated.setStatus(
        "current"
    )

sleUserFlowDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 3, 2)
)
sleUserFlowDestroyed.setObjects(
      *(("SLE-QOS-MIB", "sleUserFlowControlReqest"),
        ("SLE-QOS-MIB", "sleUserFlowControlTimeStamp"),
        ("SLE-QOS-MIB", "sleUserFlowControlReqResult"),
        ("SLE-QOS-MIB", "sleUserFlowControlName"))
)
if mibBuilder.loadTexts:
    sleUserFlowDestroyed.setStatus(
        "current"
    )

sleUserFlowClassifierProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 3, 3)
)
sleUserFlowClassifierProfileChanged.setObjects(
      *(("SLE-QOS-MIB", "sleUserFlowControlReqest"),
        ("SLE-QOS-MIB", "sleUserFlowControlTimeStamp"),
        ("SLE-QOS-MIB", "sleUserFlowControlReqResult"),
        ("SLE-QOS-MIB", "sleUserFlowControlName"))
)
if mibBuilder.loadTexts:
    sleUserFlowClassifierProfileChanged.setStatus(
        "current"
    )

sleUserFlowMatchActionProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 3, 4)
)
sleUserFlowMatchActionProfileChanged.setObjects(
      *(("SLE-QOS-MIB", "sleUserFlowControlReqest"),
        ("SLE-QOS-MIB", "sleUserFlowControlTimeStamp"),
        ("SLE-QOS-MIB", "sleUserFlowControlReqResult"),
        ("SLE-QOS-MIB", "sleUserFlowControlName"))
)
if mibBuilder.loadTexts:
    sleUserFlowMatchActionProfileChanged.setStatus(
        "current"
    )

sleUserFlowNomatchActionProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 3, 3, 5)
)
sleUserFlowNomatchActionProfileChanged.setObjects(
      *(("SLE-QOS-MIB", "sleUserFlowControlReqest"),
        ("SLE-QOS-MIB", "sleUserFlowControlTimeStamp"),
        ("SLE-QOS-MIB", "sleUserFlowControlReqResult"),
        ("SLE-QOS-MIB", "sleUserFlowControlName"))
)
if mibBuilder.loadTexts:
    sleUserFlowNomatchActionProfileChanged.setStatus(
        "current"
    )

slePortScheduleModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 4, 3, 1)
)
slePortScheduleModeChanged.setObjects(
      *(("SLE-QOS-MIB", "slePortScheduleMode"),
        ("SLE-QOS-MIB", "slePortScheduleControlRequest"),
        ("SLE-QOS-MIB", "slePortScheduleControlTimeStamp"),
        ("SLE-QOS-MIB", "slePortScheduleControlReqResult"))
)
if mibBuilder.loadTexts:
    slePortScheduleModeChanged.setStatus(
        "current"
    )

sleQueueProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 3, 1)
)
sleQueueProfileChanged.setObjects(
      *(("SLE-QOS-MIB", "sleQueueWREDMinThreshold"),
        ("SLE-QOS-MIB", "sleQueueWREDMaxThreshold"),
        ("SLE-QOS-MIB", "sleQueueWREDProbMax"),
        ("SLE-QOS-MIB", "sleQueueMinBandwidth"),
        ("SLE-QOS-MIB", "sleQueueMaxBandwidth"),
        ("SLE-QOS-MIB", "sleQueueControlTimeStamp"),
        ("SLE-QOS-MIB", "sleQueueControlReqResult"),
        ("SLE-QOS-MIB", "sleQueueControlRequest"),
        ("SLE-QOS-MIB", "sleQueueWeight"),
        ("SLE-QOS-MIB", "sleQueueREDEnable"),
        ("SLE-QOS-MIB", "sleQueueMappedCoS"))
)
if mibBuilder.loadTexts:
    sleQueueProfileChanged.setStatus(
        "current"
    )

sleQueueQuantumChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 5, 3, 2)
)
sleQueueQuantumChanged.setObjects(
      *(("SLE-QOS-MIB", "sleQueueControlRequest"),
        ("SLE-QOS-MIB", "sleQueueControlTimeStamp"),
        ("SLE-QOS-MIB", "sleQueueControlReqResult"),
        ("SLE-QOS-MIB", "sleQueueControlQuantum"))
)
if mibBuilder.loadTexts:
    sleQueueQuantumChanged.setStatus(
        "current"
    )

sleCounterCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 6, 3, 1)
)
sleCounterCleared.setObjects(
      *(("SLE-QOS-MIB", "sleCounterControlRequest"),
        ("SLE-QOS-MIB", "sleCounterControlTimeStamp"),
        ("SLE-QOS-MIB", "sleCounterControlReqResult"),
        ("SLE-QOS-MIB", "sleCounterControlIndex"))
)
if mibBuilder.loadTexts:
    sleCounterCleared.setStatus(
        "current"
    )

sleColorMarkingProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 7, 3, 1)
)
sleColorMarkingProfileChanged.setObjects(
      *(("SLE-QOS-MIB", "sleColorMarkingControlReqest"),
        ("SLE-QOS-MIB", "sleColorMarkingControlReqResult"),
        ("SLE-QOS-MIB", "sleColorMarkingControlTimeStamp"),
        ("SLE-QOS-MIB", "sleColorMarkingType"),
        ("SLE-QOS-MIB", "sleColorMarkingMode"),
        ("SLE-QOS-MIB", "sleColorMarkingAwareMode"),
        ("SLE-QOS-MIB", "sleColorMarkingCIR"),
        ("SLE-QOS-MIB", "sleColorMarkingCBS"),
        ("SLE-QOS-MIB", "sleColorMarkingPIR"),
        ("SLE-QOS-MIB", "sleColorMarkingPBS"),
        ("SLE-QOS-MIB", "sleColorMarkingEBS"),
        ("SLE-QOS-MIB", "sleColorMarkingRedAction"),
        ("SLE-QOS-MIB", "sleColorMarkingYellowAction"),
        ("SLE-QOS-MIB", "sleColorMarkingGreenAction"),
        ("SLE-QOS-MIB", "sleColorMarkingRedDscp"),
        ("SLE-QOS-MIB", "sleColorMarkingYellowDscp"),
        ("SLE-QOS-MIB", "sleColorMarkingGreenDscp"))
)
if mibBuilder.loadTexts:
    sleColorMarkingProfileChanged.setStatus(
        "current"
    )


# Notifications groups

sleQoSNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 10, 11)
)
sleQoSNotificationGroup.setObjects(
      *(("SLE-QOS-MIB", "sleTrafficProfileChanged"),
        ("SLE-QOS-MIB", "sleUserFlowCreated"),
        ("SLE-QOS-MIB", "sleUserFlowDestroyed"),
        ("SLE-QOS-MIB", "sleUserFlowClassifierProfileChanged"),
        ("SLE-QOS-MIB", "sleUserFlowMatchActionProfileChanged"),
        ("SLE-QOS-MIB", "sleUserFlowNomatchActionProfileChanged"),
        ("SLE-QOS-MIB", "slePortScheduleModeChanged"),
        ("SLE-QOS-MIB", "sleQueueProfileChanged"),
        ("SLE-QOS-MIB", "sleCounterCleared"),
        ("SLE-QOS-MIB", "sleColorMarkingProfileChanged"),
        ("SLE-QOS-MIB", "sleQoSBaseRuleModeChanged"),
        ("SLE-QOS-MIB", "sleQueueQuantumChanged"))
)
if mibBuilder.loadTexts:
    sleQoSNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-QOS-MIB",
    **{"SleTrafficProfileControlRequestType": SleTrafficProfileControlRequestType,
       "SleUserFlowMatchType": SleUserFlowMatchType,
       "SleUserFlowActionType": SleUserFlowActionType,
       "SleBooleanType": SleBooleanType,
       "SlePortScheduleControlRequestType": SlePortScheduleControlRequestType,
       "SleQueueControlRequestType": SleQueueControlRequestType,
       "SleUserFlowControlRequestType": SleUserFlowControlRequestType,
       "sleQoS": sleQoS,
       "sleQoSBase": sleQoSBase,
       "sleQoSBaseInfo": sleQoSBaseInfo,
       "sleQosUserFlowNum": sleQosUserFlowNum,
       "sleQosTrafficProfileNum": sleQosTrafficProfileNum,
       "sleQosCounterNum": sleQosCounterNum,
       "sleQosQueueNum": sleQosQueueNum,
       "sleQosColorMarkingProfileNum": sleQosColorMarkingProfileNum,
       "sleQosRuleMode": sleQosRuleMode,
       "sleQoSBaseControl": sleQoSBaseControl,
       "sleQoSBaseControlRequest": sleQoSBaseControlRequest,
       "sleQoSBaseControlStatus": sleQoSBaseControlStatus,
       "sleQoSBaseControlTimer": sleQoSBaseControlTimer,
       "sleQoSBaseControlTimeStamp": sleQoSBaseControlTimeStamp,
       "sleQoSBaseControlReqResult": sleQoSBaseControlReqResult,
       "sleQoSBaseControlRuleMode": sleQoSBaseControlRuleMode,
       "sleQoSBaseNotification": sleQoSBaseNotification,
       "sleQoSBaseRuleModeChanged": sleQoSBaseRuleModeChanged,
       "sleTrafficProfile": sleTrafficProfile,
       "sleTrafficProfileTable": sleTrafficProfileTable,
       "sleTrafficProfileEntry": sleTrafficProfileEntry,
       "sleTrafficProfileIndex": sleTrafficProfileIndex,
       "sleTrafficProfileMinBandwidth": sleTrafficProfileMinBandwidth,
       "sleTrafficProfileMaxBandwidth": sleTrafficProfileMaxBandwidth,
       "sleTrafficProfileMaxBurstSize": sleTrafficProfileMaxBurstSize,
       "sleTrafficProfileUseCount": sleTrafficProfileUseCount,
       "sleTrafficProfileControl": sleTrafficProfileControl,
       "sleTrafficProfileControlRequest": sleTrafficProfileControlRequest,
       "sleTrafficProfileControlStatus": sleTrafficProfileControlStatus,
       "sleTrafficProfileControlTimer": sleTrafficProfileControlTimer,
       "sleTrafficProfileControlTimeStamp": sleTrafficProfileControlTimeStamp,
       "sleTrafficProfileControlReqResult": sleTrafficProfileControlReqResult,
       "sleTrafficProfileControlIndex": sleTrafficProfileControlIndex,
       "sleTrafficProfileControlMinBandwidth": sleTrafficProfileControlMinBandwidth,
       "sleTrafficProfileControlMaxBandwidth": sleTrafficProfileControlMaxBandwidth,
       "sleTrafficProfileControlMaxBurstSize": sleTrafficProfileControlMaxBurstSize,
       "sleTrafficProfileNotification": sleTrafficProfileNotification,
       "sleTrafficProfileChanged": sleTrafficProfileChanged,
       "sleUserFlow": sleUserFlow,
       "sleUserFlowTable": sleUserFlowTable,
       "sleUserFlowEntry": sleUserFlowEntry,
       "sleUserFlowName": sleUserFlowName,
       "sleUserFlowIngressPorts": sleUserFlowIngressPorts,
       "sleUserFlowEgressPorts": sleUserFlowEgressPorts,
       "sleUserFlowEthernetType": sleUserFlowEthernetType,
       "sleUserFlowSrcMacAddr": sleUserFlowSrcMacAddr,
       "sleUserFlowDstMacAddr": sleUserFlowDstMacAddr,
       "sleUserFlowVlan": sleUserFlowVlan,
       "sleUserFlow8021p": sleUserFlow8021p,
       "sleUserFlowSrcIpAddr": sleUserFlowSrcIpAddr,
       "sleUserFlowSrcPrefixLength": sleUserFlowSrcPrefixLength,
       "sleUserFlowDstIpAddr": sleUserFlowDstIpAddr,
       "sleUserFlowDstPrefixLength": sleUserFlowDstPrefixLength,
       "sleUserFlowIpPktPriorityType": sleUserFlowIpPktPriorityType,
       "sleUserFlowIpPktPriority": sleUserFlowIpPktPriority,
       "sleUserFlowProtocolType": sleUserFlowProtocolType,
       "sleUserFlowTcpFlag": sleUserFlowTcpFlag,
       "sleUserFlowSrcL4Port": sleUserFlowSrcL4Port,
       "sleUserFlowDstL4Port": sleUserFlowDstL4Port,
       "sleUserFlowPktLen": sleUserFlowPktLen,
       "sleUserFlowValidFlags": sleUserFlowValidFlags,
       "sleUserFlowMatchFlags": sleUserFlowMatchFlags,
       "sleUserFlowPriority": sleUserFlowPriority,
       "sleUserFlowMatchCounterId": sleUserFlowMatchCounterId,
       "sleUserFlowMatchTrafficProfileId": sleUserFlowMatchTrafficProfileId,
       "sleUserFlowMatchQueue": sleUserFlowMatchQueue,
       "sleUserFlowMatchIpPktPriorityType": sleUserFlowMatchIpPktPriorityType,
       "sleUserFlowMatchIpPktPriority": sleUserFlowMatchIpPktPriority,
       "sleUserFlowMatchRedirPort": sleUserFlowMatchRedirPort,
       "sleUserFlowMatchVid": sleUserFlowMatchVid,
       "sleUserFlowMatchDstMac": sleUserFlowMatchDstMac,
       "sleUserFlowMatchPortMap": sleUserFlowMatchPortMap,
       "sleUserFlowMatchEgressType": sleUserFlowMatchEgressType,
       "sleUserFlowMatchAction": sleUserFlowMatchAction,
       "sleUserFlowNomatchCounterId": sleUserFlowNomatchCounterId,
       "sleUserFlowNomatchTrafficProfileId": sleUserFlowNomatchTrafficProfileId,
       "sleUserFlowNomatchQueue": sleUserFlowNomatchQueue,
       "sleUserFlowNomatchIpPktPriorityType": sleUserFlowNomatchIpPktPriorityType,
       "sleUserFlowNomatchIpPktPriority": sleUserFlowNomatchIpPktPriority,
       "sleUserFlowNomatchRedirPort": sleUserFlowNomatchRedirPort,
       "sleUserFlowNomatchVid": sleUserFlowNomatchVid,
       "sleUserFlowNomatchAction": sleUserFlowNomatchAction,
       "sleUserFlowMatchColorMarkingId": sleUserFlowMatchColorMarkingId,
       "sleUserFlowNomatchColorMarkingId": sleUserFlowNomatchColorMarkingId,
       "sleUserFlowInnerVlan": sleUserFlowInnerVlan,
       "sleUserFlowInner8021p": sleUserFlowInner8021p,
       "sleUserFlowMatchRoutePrimary": sleUserFlowMatchRoutePrimary,
       "sleUserFlowMatchRouteSecondary": sleUserFlowMatchRouteSecondary,
       "sleUserFlowControl": sleUserFlowControl,
       "sleUserFlowControlReqest": sleUserFlowControlReqest,
       "sleUserFlowControlStatus": sleUserFlowControlStatus,
       "sleUserFlowControlTimer": sleUserFlowControlTimer,
       "sleUserFlowControlTimeStamp": sleUserFlowControlTimeStamp,
       "sleUserFlowControlReqResult": sleUserFlowControlReqResult,
       "sleUserFlowControlName": sleUserFlowControlName,
       "sleUserFlowControlIngressPorts": sleUserFlowControlIngressPorts,
       "sleUserFlowControlEgressPorts": sleUserFlowControlEgressPorts,
       "sleUserFlowControlEthernetType": sleUserFlowControlEthernetType,
       "sleUserFlowControlSrcMacAddr": sleUserFlowControlSrcMacAddr,
       "sleUserFlowControlDstMacAddr": sleUserFlowControlDstMacAddr,
       "sleUserFlowControlVlan": sleUserFlowControlVlan,
       "sleUserFlowControl8021p": sleUserFlowControl8021p,
       "sleUserFlowControlSrcIpAddr": sleUserFlowControlSrcIpAddr,
       "sleUserFlowControlSrcPrefixLength": sleUserFlowControlSrcPrefixLength,
       "sleUserFlowControlDstIpAddr": sleUserFlowControlDstIpAddr,
       "sleUserFlowControlDstPrefixLength": sleUserFlowControlDstPrefixLength,
       "sleUserFlowControlIpPktPriorityType": sleUserFlowControlIpPktPriorityType,
       "sleUserFlowControlIpPktPriority": sleUserFlowControlIpPktPriority,
       "sleUserFlowControlProtocolType": sleUserFlowControlProtocolType,
       "sleUserFlowControlTcpFlag": sleUserFlowControlTcpFlag,
       "sleUserFlowControlSrcL4Port": sleUserFlowControlSrcL4Port,
       "sleUserFlowControlDstL4Port": sleUserFlowControlDstL4Port,
       "sleUserFlowControlPktLen": sleUserFlowControlPktLen,
       "sleUserFlowControlValidFlag": sleUserFlowControlValidFlag,
       "sleUserFlowControlMatchFlag": sleUserFlowControlMatchFlag,
       "sleUserFlowControlPriority": sleUserFlowControlPriority,
       "sleUserFlowControlMatchCounterId": sleUserFlowControlMatchCounterId,
       "sleUserFlowControlMatchTrafficProfileId": sleUserFlowControlMatchTrafficProfileId,
       "sleUserFlowControlMatchQueue": sleUserFlowControlMatchQueue,
       "sleUserFlowControlMatchIpPktPriorityType": sleUserFlowControlMatchIpPktPriorityType,
       "sleUserFlowControlMatchIpPktPriority": sleUserFlowControlMatchIpPktPriority,
       "sleUserFlowControlMatchRedirPort": sleUserFlowControlMatchRedirPort,
       "sleUserFlowControlMatchVid": sleUserFlowControlMatchVid,
       "sleUserFlowControlMatchDstMac": sleUserFlowControlMatchDstMac,
       "sleUserFlowControlMatchPortMap": sleUserFlowControlMatchPortMap,
       "sleUserFlowControlMatchEgressType": sleUserFlowControlMatchEgressType,
       "sleUserFlowControlMatchAction": sleUserFlowControlMatchAction,
       "sleUserFlowControlNomatchCounterId": sleUserFlowControlNomatchCounterId,
       "sleUserFlowControlNomatchTrafficProfileId": sleUserFlowControlNomatchTrafficProfileId,
       "sleUserFlowControlNomatchQueue": sleUserFlowControlNomatchQueue,
       "sleUserFlowControlNomatchIpPktPriorityType": sleUserFlowControlNomatchIpPktPriorityType,
       "sleUserFlowControlNomatchIpPktPriority": sleUserFlowControlNomatchIpPktPriority,
       "sleUserFlowControlNomatchRedirPort": sleUserFlowControlNomatchRedirPort,
       "sleUserFlowControlNomatchVid": sleUserFlowControlNomatchVid,
       "sleUserFlowControlNomatchAction": sleUserFlowControlNomatchAction,
       "sleUserFlowControlMatchColorMarkingId": sleUserFlowControlMatchColorMarkingId,
       "sleUserFlowControlNomatchColorMarkingId": sleUserFlowControlNomatchColorMarkingId,
       "sleUserFlowControlInnerVlan": sleUserFlowControlInnerVlan,
       "sleUserFlowControlInner8021p": sleUserFlowControlInner8021p,
       "sleUserFlowControlMatchRoutePrimary": sleUserFlowControlMatchRoutePrimary,
       "sleUserFlowControlMatchRouteSecondary": sleUserFlowControlMatchRouteSecondary,
       "sleUserFlowNotification": sleUserFlowNotification,
       "sleUserFlowCreated": sleUserFlowCreated,
       "sleUserFlowDestroyed": sleUserFlowDestroyed,
       "sleUserFlowClassifierProfileChanged": sleUserFlowClassifierProfileChanged,
       "sleUserFlowMatchActionProfileChanged": sleUserFlowMatchActionProfileChanged,
       "sleUserFlowNomatchActionProfileChanged": sleUserFlowNomatchActionProfileChanged,
       "slePortSchedule": slePortSchedule,
       "slePortSchedultTable": slePortSchedultTable,
       "slePortSchedultEntry": slePortSchedultEntry,
       "slePortSchedulInterfaceIndex": slePortSchedulInterfaceIndex,
       "slePortScheduleMode": slePortScheduleMode,
       "slePortScheduleControl": slePortScheduleControl,
       "slePortScheduleControlRequest": slePortScheduleControlRequest,
       "sleScheduleControlStatus": sleScheduleControlStatus,
       "slePortScheduleControlTimer": slePortScheduleControlTimer,
       "slePortScheduleControlTimeStamp": slePortScheduleControlTimeStamp,
       "slePortScheduleControlReqResult": slePortScheduleControlReqResult,
       "slePortScheduleControlInterfaceIndex": slePortScheduleControlInterfaceIndex,
       "slePortScheduleControlMode": slePortScheduleControlMode,
       "slePortScheduleNotification": slePortScheduleNotification,
       "slePortScheduleModeChanged": slePortScheduleModeChanged,
       "sleQueue": sleQueue,
       "sleQueueTable": sleQueueTable,
       "sleQueueEntry": sleQueueEntry,
       "sleQueueId": sleQueueId,
       "sleQueueREDEnable": sleQueueREDEnable,
       "sleQueueMappedCoS": sleQueueMappedCoS,
       "sleQueueWREDMinThreshold": sleQueueWREDMinThreshold,
       "sleQueueWREDMaxThreshold": sleQueueWREDMaxThreshold,
       "sleQueueWREDProbMax": sleQueueWREDProbMax,
       "sleQueueMinBandwidth": sleQueueMinBandwidth,
       "sleQueueMaxBandwidth": sleQueueMaxBandwidth,
       "sleQueueWeight": sleQueueWeight,
       "sleQueueMaxLatency": sleQueueMaxLatency,
       "sleQueueMaxPackets": sleQueueMaxPackets,
       "sleQueueQuantum": sleQueueQuantum,
       "sleQueueUsedPkts": sleQueueUsedPkts,
       "sleQueueUsedBytes": sleQueueUsedBytes,
       "sleQueueControl": sleQueueControl,
       "sleQueueControlRequest": sleQueueControlRequest,
       "sleQueueControlStatus": sleQueueControlStatus,
       "sleQueueControlTimer": sleQueueControlTimer,
       "sleQueueControlTimeStamp": sleQueueControlTimeStamp,
       "sleQueueControlReqResult": sleQueueControlReqResult,
       "sleQueueControlInterfaceIndex": sleQueueControlInterfaceIndex,
       "sleQueueControlId": sleQueueControlId,
       "sleQueueControlREDEnable": sleQueueControlREDEnable,
       "sleQueueControlMappedCoS": sleQueueControlMappedCoS,
       "sleQueueControlWREDMinThreshold": sleQueueControlWREDMinThreshold,
       "sleQueueControlWREDMaxThreshold": sleQueueControlWREDMaxThreshold,
       "sleQueueControlWREDProbMax": sleQueueControlWREDProbMax,
       "sleQueueControlMinBandwidth": sleQueueControlMinBandwidth,
       "sleQueueControlMaxBandwidth": sleQueueControlMaxBandwidth,
       "sleQueueControlWeight": sleQueueControlWeight,
       "sleQueueControlMaxLatency": sleQueueControlMaxLatency,
       "sleQueueControlMaxPackets": sleQueueControlMaxPackets,
       "sleQueueControlQuantum": sleQueueControlQuantum,
       "sleQueueNotification": sleQueueNotification,
       "sleQueueProfileChanged": sleQueueProfileChanged,
       "sleQueueQuantumChanged": sleQueueQuantumChanged,
       "sleCounter": sleCounter,
       "sleCounterTable": sleCounterTable,
       "sleCounterEntry": sleCounterEntry,
       "sleCounterIndex": sleCounterIndex,
       "sleCounterPackets": sleCounterPackets,
       "sleCounterControl": sleCounterControl,
       "sleCounterControlRequest": sleCounterControlRequest,
       "sleCounterControlStatus": sleCounterControlStatus,
       "sleCounterControlTimer": sleCounterControlTimer,
       "sleCounterControlTimeStamp": sleCounterControlTimeStamp,
       "sleCounterControlReqResult": sleCounterControlReqResult,
       "sleCounterControlIndex": sleCounterControlIndex,
       "sleCounterNotification": sleCounterNotification,
       "sleCounterCleared": sleCounterCleared,
       "sleColorMarking": sleColorMarking,
       "sleColorMarkingTable": sleColorMarkingTable,
       "sleColorMarkingEntry": sleColorMarkingEntry,
       "sleColorMarkingIndex": sleColorMarkingIndex,
       "sleColorMarkingType": sleColorMarkingType,
       "sleColorMarkingMode": sleColorMarkingMode,
       "sleColorMarkingAwareMode": sleColorMarkingAwareMode,
       "sleColorMarkingCIR": sleColorMarkingCIR,
       "sleColorMarkingCBS": sleColorMarkingCBS,
       "sleColorMarkingPIR": sleColorMarkingPIR,
       "sleColorMarkingPBS": sleColorMarkingPBS,
       "sleColorMarkingEBS": sleColorMarkingEBS,
       "sleColorMarkingRedAction": sleColorMarkingRedAction,
       "sleColorMarkingYellowAction": sleColorMarkingYellowAction,
       "sleColorMarkingGreenAction": sleColorMarkingGreenAction,
       "sleColorMarkingRedDscp": sleColorMarkingRedDscp,
       "sleColorMarkingYellowDscp": sleColorMarkingYellowDscp,
       "sleColorMarkingGreenDscp": sleColorMarkingGreenDscp,
       "sleColorMarkingUseCount": sleColorMarkingUseCount,
       "sleColorMarkingControl": sleColorMarkingControl,
       "sleColorMarkingControlReqest": sleColorMarkingControlReqest,
       "sleColorMarkingControlStatus": sleColorMarkingControlStatus,
       "sleColorMarkingControlTimer": sleColorMarkingControlTimer,
       "sleColorMarkingControlTimeStamp": sleColorMarkingControlTimeStamp,
       "sleColorMarkingControlReqResult": sleColorMarkingControlReqResult,
       "sleColorMarkingControlIndex": sleColorMarkingControlIndex,
       "sleColorMarkingControlType": sleColorMarkingControlType,
       "sleColorMarkingControlMode": sleColorMarkingControlMode,
       "sleColorMarkingControlAwareMode": sleColorMarkingControlAwareMode,
       "sleColorMarkingControlCIR": sleColorMarkingControlCIR,
       "sleColorMarkingControlCBS": sleColorMarkingControlCBS,
       "sleColorMarkingControlPIR": sleColorMarkingControlPIR,
       "sleColorMarkingControlPBS": sleColorMarkingControlPBS,
       "sleColorMarkingControlEBS": sleColorMarkingControlEBS,
       "sleColorMarkingControlRedAction": sleColorMarkingControlRedAction,
       "sleColorMarkingControlYellowAction": sleColorMarkingControlYellowAction,
       "sleColorMarkingControlGreenAction": sleColorMarkingControlGreenAction,
       "sleColorMarkingControlRedDscp": sleColorMarkingControlRedDscp,
       "sleColorMarkingControlYellowDscp": sleColorMarkingControlYellowDscp,
       "sleColorMarkingControlGreenDscp": sleColorMarkingControlGreenDscp,
       "sleColorMarkingNotification": sleColorMarkingNotification,
       "sleColorMarkingProfileChanged": sleColorMarkingProfileChanged,
       "sleQoSGroup": sleQoSGroup,
       "sleQoSControlGroup": sleQoSControlGroup,
       "sleQoSNotificationGroup": sleQoSNotificationGroup}
)
