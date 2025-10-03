# SNMP MIB module (TIMETRA-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\TIMETRA-LDP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:17:12 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(MplsLdpIdentifier,
 MplsLsrIdentifier) = mibBuilder.importSymbols(
    "MPLS-LDP-MIB",
    "MplsLdpIdentifier",
    "MplsLsrIdentifier")

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
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(TFilterID,
 TFilterLogId) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TFilterID",
    "TFilterLogId")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(SdpId,
 ServType,
 TdmOptionsCasTrunkFraming,
 TdmOptionsSigPkts) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "SdpId",
    "ServType",
    "TdmOptionsCasTrunkFraming",
    "TdmOptionsSigPkts")

(TNamedItem,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TmnxAddressAndPrefixAddress,
 TmnxAddressAndPrefixPrefix,
 TmnxAddressAndPrefixType,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxLdpFECType,
 TmnxOperState,
 TmnxServId,
 TmnxVRtrMplsLspID,
 TmnxVcId,
 TmnxVcType) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TmnxAddressAndPrefixAddress",
    "TmnxAddressAndPrefixPrefix",
    "TmnxAddressAndPrefixType",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxLdpFECType",
    "TmnxOperState",
    "TmnxServId",
    "TmnxVRtrMplsLspID",
    "TmnxVcId",
    "TmnxVcType")

(vRtrID,
 vRtrLdpStatus) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrLdpStatus")


# MODULE-IDENTITY

timetraLdpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 8)
)
if mibBuilder.loadTexts:
    timetraLdpMIBModule.setRevisions(
        ("2017-01-01 00:00",
         "2016-01-01 00:00",
         "2015-01-01 00:00",
         "2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-03-16 00:00",
         "2005-08-31 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2003-01-20 00:00",
         "2001-08-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxLdpKeepAliveFactor(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class TmnxLdpKeepAliveTimeout(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TmnxLdpHelloFactor(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class TmnxLdpHelloTimeout(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TmnxLdpBackoffTime(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2592000),
    )



class TmnxLdpFECPolicy(TextualConvention, Integer32):
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
        *(("system", 1),
          ("interface", 2),
          ("all", 3),
          ("none", 4))
    )



class TmnxLdpLabelDistMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstreamOnDemand", 1),
          ("downstreamUnsolicited", 2))
    )



class TmnxLdpAdjacencyType(TextualConvention, Integer32):
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
        *(("link", 1),
          ("targeted", 2),
          ("both", 3))
    )



class TmnxVpnId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10



class TmnxLabelStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("dummyB0", 0),
          ("dummyB1", 1),
          ("statusSignalingSupported", 2),
          ("inUsePush", 3),
          ("inUseSwap", 4),
          ("inUsePop", 5),
          ("released", 6),
          ("notInUse", 7),
          ("withdrawn", 8),
          ("controlWord", 9),
          ("withdrawPending", 10),
          ("alternateNextHop", 11),
          ("alternatePHop", 12),
          ("unnumIf", 13),
          ("srIsisNextHop", 14),
          ("srOspfNextHop", 15),
          ("entLblCap", 16))
    )


class TmnxLabelSigStatus(TextualConvention, Unsigned32):
    status = "current"


class TmnxLdpFECTunnelType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("static", 1)
    )



class TmnxLdpFECFlags(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("dummyB0", 0),
          ("egress", 1),
          ("ingress", 2),
          ("installedSwap", 3),
          ("installedPush", 4),
          ("installedPop", 5),
          ("local", 6),
          ("nextHop", 7),
          ("importPolicyRejected", 8),
          ("exportPolicyAccepted", 9),
          ("installedStaticFec", 10),
          ("vcSwitching", 11),
          ("importTargPolicyRejected", 12),
          ("exportTargPolicyRejected", 13),
          ("importPeerPolicyRejected", 14),
          ("localMultihomedSecondary", 15),
          ("bgpNextHop", 16),
          ("labelReqSent", 17),
          ("classBasedForwarding", 18),
          ("srIsisNextHop", 19),
          ("srOspfNextHop", 20),
          ("upperFec", 21),
          ("lowerFec", 22),
          ("communityMismatch", 23),
          ("bkpUpperFec", 24))
    )


class TmnxLdpGenOperDownReasonCode(TextualConvention, Integer32):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("operUp", 0),
          ("adminDown", 1),
          ("noListenSocket", 2),
          ("noDiscoverySocket", 3),
          ("noRtm", 4),
          ("noTtm", 5),
          ("iomFailure", 6),
          ("recvFailure", 7),
          ("clearDown", 8),
          ("noResources", 9),
          ("systemIpDown", 10),
          ("helloFailure", 11),
          ("ipv6NotSupported", 12),
          ("noBgp", 13))
    )



class TmnxLdpIntTargOperDownReasonCode(TextualConvention, Integer32):
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
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("operUp", 0),
          ("adminDown", 1),
          ("noListenSocket", 2),
          ("noDiscoverySocket", 3),
          ("noResources", 4),
          ("addrFecDeprogram", 5),
          ("svcFecDeprogram", 6),
          ("clearDown", 7),
          ("instanceDown", 8),
          ("interfaceDown", 9),
          ("targetIpInvalid", 10),
          ("interfaceInvalid", 11),
          ("lsrInterfaceDown", 12),
          ("lsrInterfaceInvalid", 13),
          ("helloFailure", 14),
          ("parentIfDown", 15),
          ("interfaceNoValidIp", 16),
          ("lsrInterfaceNoValidIp", 17))
    )



class TmnxLdpFec129Tlv(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )



class TmnxLdpNewKeepAliveTimeout(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )



class TmnxLdpNewHelloTimeout(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )



class TmnxLdpInLblWdrawalReasonCode(TextualConvention, Integer32):
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
        *(("none", 0),
          ("noSwLabel", 1),
          ("localFault", 2),
          ("stackMismatch", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxLdpConformance_ObjectIdentity = ObjectIdentity
tmnxLdpConformance = _TmnxLdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8)
)
_TmnxLdpCompliances_ObjectIdentity = ObjectIdentity
tmnxLdpCompliances = _TmnxLdpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 1)
)
_TmnxLdpGroups_ObjectIdentity = ObjectIdentity
tmnxLdpGroups = _TmnxLdpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2)
)
_TmnxLdpObjs_ObjectIdentity = ObjectIdentity
tmnxLdpObjs = _TmnxLdpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8)
)
_VRtrLdpGeneralTable_Object = MibTable
vRtrLdpGeneralTable = _VRtrLdpGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpGeneralTable.setStatus("obsolete")
_VRtrLdpGeneralEntry_Object = MibTableRow
vRtrLdpGeneralEntry = _VRtrLdpGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1)
)
vRtrLdpGeneralEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrLdpGeneralEntry.setStatus("obsolete")
_VRtrLdpGenLastChange_Type = TimeStamp
_VRtrLdpGenLastChange_Object = MibTableColumn
vRtrLdpGenLastChange = _VRtrLdpGenLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 1),
    _VRtrLdpGenLastChange_Type()
)
vRtrLdpGenLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenLastChange.setStatus("obsolete")


class _VRtrLdpGenAdminState_Type(TmnxAdminState):
    """Custom type vRtrLdpGenAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrLdpGenAdminState_Type.__name__ = "TmnxAdminState"
_VRtrLdpGenAdminState_Object = MibTableColumn
vRtrLdpGenAdminState = _VRtrLdpGenAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 2),
    _VRtrLdpGenAdminState_Type()
)
vRtrLdpGenAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenAdminState.setStatus("obsolete")
_VRtrLdpGenOperState_Type = TmnxOperState
_VRtrLdpGenOperState_Object = MibTableColumn
vRtrLdpGenOperState = _VRtrLdpGenOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 3),
    _VRtrLdpGenOperState_Type()
)
vRtrLdpGenOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenOperState.setStatus("obsolete")
_VRtrLdpGenLdpLsrId_Type = MplsLsrIdentifier
_VRtrLdpGenLdpLsrId_Object = MibTableColumn
vRtrLdpGenLdpLsrId = _VRtrLdpGenLdpLsrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 4),
    _VRtrLdpGenLdpLsrId_Type()
)
vRtrLdpGenLdpLsrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenLdpLsrId.setStatus("obsolete")
_VRtrLdpGenProtocolVersion_Type = Unsigned32
_VRtrLdpGenProtocolVersion_Object = MibTableColumn
vRtrLdpGenProtocolVersion = _VRtrLdpGenProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 5),
    _VRtrLdpGenProtocolVersion_Type()
)
vRtrLdpGenProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenProtocolVersion.setStatus("obsolete")


class _VRtrLdpGenDeaggregateFec_Type(TruthValue):
    """Custom type vRtrLdpGenDeaggregateFec based on TruthValue"""
    defaultValue = 2


_VRtrLdpGenDeaggregateFec_Type.__name__ = "TruthValue"
_VRtrLdpGenDeaggregateFec_Object = MibTableColumn
vRtrLdpGenDeaggregateFec = _VRtrLdpGenDeaggregateFec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 6),
    _VRtrLdpGenDeaggregateFec_Type()
)
vRtrLdpGenDeaggregateFec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenDeaggregateFec.setStatus("obsolete")


class _VRtrLdpGenKeepAliveFactor_Type(TmnxLdpKeepAliveFactor):
    """Custom type vRtrLdpGenKeepAliveFactor based on TmnxLdpKeepAliveFactor"""
    defaultValue = 3


_VRtrLdpGenKeepAliveFactor_Type.__name__ = "TmnxLdpKeepAliveFactor"
_VRtrLdpGenKeepAliveFactor_Object = MibTableColumn
vRtrLdpGenKeepAliveFactor = _VRtrLdpGenKeepAliveFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 7),
    _VRtrLdpGenKeepAliveFactor_Type()
)
vRtrLdpGenKeepAliveFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenKeepAliveFactor.setStatus("obsolete")


class _VRtrLdpGenKeepAliveTimeout_Type(TmnxLdpNewKeepAliveTimeout):
    """Custom type vRtrLdpGenKeepAliveTimeout based on TmnxLdpNewKeepAliveTimeout"""
    defaultValue = 30


_VRtrLdpGenKeepAliveTimeout_Type.__name__ = "TmnxLdpNewKeepAliveTimeout"
_VRtrLdpGenKeepAliveTimeout_Object = MibTableColumn
vRtrLdpGenKeepAliveTimeout = _VRtrLdpGenKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 8),
    _VRtrLdpGenKeepAliveTimeout_Type()
)
vRtrLdpGenKeepAliveTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenKeepAliveTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpGenKeepAliveTimeout.setUnits("seconds")


class _VRtrLdpGenHelloFactor_Type(TmnxLdpHelloFactor):
    """Custom type vRtrLdpGenHelloFactor based on TmnxLdpHelloFactor"""
    defaultValue = 3


_VRtrLdpGenHelloFactor_Type.__name__ = "TmnxLdpHelloFactor"
_VRtrLdpGenHelloFactor_Object = MibTableColumn
vRtrLdpGenHelloFactor = _VRtrLdpGenHelloFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 9),
    _VRtrLdpGenHelloFactor_Type()
)
vRtrLdpGenHelloFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenHelloFactor.setStatus("obsolete")


class _VRtrLdpGenHelloTimeout_Type(TmnxLdpNewHelloTimeout):
    """Custom type vRtrLdpGenHelloTimeout based on TmnxLdpNewHelloTimeout"""
    defaultValue = 15


_VRtrLdpGenHelloTimeout_Type.__name__ = "TmnxLdpNewHelloTimeout"
_VRtrLdpGenHelloTimeout_Object = MibTableColumn
vRtrLdpGenHelloTimeout = _VRtrLdpGenHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 10),
    _VRtrLdpGenHelloTimeout_Type()
)
vRtrLdpGenHelloTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenHelloTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpGenHelloTimeout.setUnits("seconds")


class _VRtrLdpGenRoutePreference_Type(Unsigned32):
    """Custom type vRtrLdpGenRoutePreference based on Unsigned32"""
    defaultValue = 9

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrLdpGenRoutePreference_Type.__name__ = "Unsigned32"
_VRtrLdpGenRoutePreference_Object = MibTableColumn
vRtrLdpGenRoutePreference = _VRtrLdpGenRoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 11),
    _VRtrLdpGenRoutePreference_Type()
)
vRtrLdpGenRoutePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenRoutePreference.setStatus("obsolete")


class _VRtrLdpGenControlMode_Type(Integer32):
    """Custom type vRtrLdpGenControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ordered", 1),
          ("independent", 2))
    )


_VRtrLdpGenControlMode_Type.__name__ = "Integer32"
_VRtrLdpGenControlMode_Object = MibTableColumn
vRtrLdpGenControlMode = _VRtrLdpGenControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 12),
    _VRtrLdpGenControlMode_Type()
)
vRtrLdpGenControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenControlMode.setStatus("obsolete")
_VRtrLdpGenDistMethod_Type = TmnxLdpLabelDistMethod
_VRtrLdpGenDistMethod_Object = MibTableColumn
vRtrLdpGenDistMethod = _VRtrLdpGenDistMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 13),
    _VRtrLdpGenDistMethod_Type()
)
vRtrLdpGenDistMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenDistMethod.setStatus("obsolete")


class _VRtrLdpGenRetentionMode_Type(Integer32):
    """Custom type vRtrLdpGenRetentionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("conservative", 1),
          ("liberal", 2))
    )


_VRtrLdpGenRetentionMode_Type.__name__ = "Integer32"
_VRtrLdpGenRetentionMode_Object = MibTableColumn
vRtrLdpGenRetentionMode = _VRtrLdpGenRetentionMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 14),
    _VRtrLdpGenRetentionMode_Type()
)
vRtrLdpGenRetentionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenRetentionMode.setStatus("obsolete")


class _VRtrLdpGenTransportAddrType_Type(Integer32):
    """Custom type vRtrLdpGenTransportAddrType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("system", 2))
    )


_VRtrLdpGenTransportAddrType_Type.__name__ = "Integer32"
_VRtrLdpGenTransportAddrType_Object = MibTableColumn
vRtrLdpGenTransportAddrType = _VRtrLdpGenTransportAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 15),
    _VRtrLdpGenTransportAddrType_Type()
)
vRtrLdpGenTransportAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTransportAddrType.setStatus("obsolete")


class _VRtrLdpGenPropagatePolicy_Type(TmnxLdpFECPolicy):
    """Custom type vRtrLdpGenPropagatePolicy based on TmnxLdpFECPolicy"""
    defaultValue = 1


_VRtrLdpGenPropagatePolicy_Type.__name__ = "TmnxLdpFECPolicy"
_VRtrLdpGenPropagatePolicy_Object = MibTableColumn
vRtrLdpGenPropagatePolicy = _VRtrLdpGenPropagatePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 16),
    _VRtrLdpGenPropagatePolicy_Type()
)
vRtrLdpGenPropagatePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenPropagatePolicy.setStatus("obsolete")


class _VRtrLdpGenLoopDetectCapable_Type(Integer32):
    """Custom type vRtrLdpGenLoopDetectCapable based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("other", 2),
          ("hopCount", 3),
          ("pathVector", 4),
          ("hopCountAndPathVector", 5))
    )


_VRtrLdpGenLoopDetectCapable_Type.__name__ = "Integer32"
_VRtrLdpGenLoopDetectCapable_Object = MibTableColumn
vRtrLdpGenLoopDetectCapable = _VRtrLdpGenLoopDetectCapable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 17),
    _VRtrLdpGenLoopDetectCapable_Type()
)
vRtrLdpGenLoopDetectCapable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenLoopDetectCapable.setStatus("obsolete")


class _VRtrLdpGenHopLimit_Type(Unsigned32):
    """Custom type vRtrLdpGenHopLimit based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrLdpGenHopLimit_Type.__name__ = "Unsigned32"
_VRtrLdpGenHopLimit_Object = MibTableColumn
vRtrLdpGenHopLimit = _VRtrLdpGenHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 18),
    _VRtrLdpGenHopLimit_Type()
)
vRtrLdpGenHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenHopLimit.setStatus("obsolete")


class _VRtrLdpGenPathVectorLimit_Type(Unsigned32):
    """Custom type vRtrLdpGenPathVectorLimit based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrLdpGenPathVectorLimit_Type.__name__ = "Unsigned32"
_VRtrLdpGenPathVectorLimit_Object = MibTableColumn
vRtrLdpGenPathVectorLimit = _VRtrLdpGenPathVectorLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 19),
    _VRtrLdpGenPathVectorLimit_Type()
)
vRtrLdpGenPathVectorLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenPathVectorLimit.setStatus("obsolete")


class _VRtrLdpGenBackoffTime_Type(TmnxLdpBackoffTime):
    """Custom type vRtrLdpGenBackoffTime based on TmnxLdpBackoffTime"""
    defaultValue = 15

    subtypeSpec = TmnxLdpBackoffTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2592000),
    )


_VRtrLdpGenBackoffTime_Type.__name__ = "TmnxLdpBackoffTime"
_VRtrLdpGenBackoffTime_Object = MibTableColumn
vRtrLdpGenBackoffTime = _VRtrLdpGenBackoffTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 20),
    _VRtrLdpGenBackoffTime_Type()
)
vRtrLdpGenBackoffTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenBackoffTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpGenBackoffTime.setUnits("seconds")


class _VRtrLdpGenMaxBackoffTime_Type(TmnxLdpBackoffTime):
    """Custom type vRtrLdpGenMaxBackoffTime based on TmnxLdpBackoffTime"""
    defaultValue = 120


_VRtrLdpGenMaxBackoffTime_Type.__name__ = "TmnxLdpBackoffTime"
_VRtrLdpGenMaxBackoffTime_Object = MibTableColumn
vRtrLdpGenMaxBackoffTime = _VRtrLdpGenMaxBackoffTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 21),
    _VRtrLdpGenMaxBackoffTime_Type()
)
vRtrLdpGenMaxBackoffTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenMaxBackoffTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpGenMaxBackoffTime.setUnits("seconds")


class _VRtrLdpGenTargKeepAliveFactor_Type(TmnxLdpKeepAliveFactor):
    """Custom type vRtrLdpGenTargKeepAliveFactor based on TmnxLdpKeepAliveFactor"""
    defaultValue = 4


_VRtrLdpGenTargKeepAliveFactor_Type.__name__ = "TmnxLdpKeepAliveFactor"
_VRtrLdpGenTargKeepAliveFactor_Object = MibTableColumn
vRtrLdpGenTargKeepAliveFactor = _VRtrLdpGenTargKeepAliveFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 22),
    _VRtrLdpGenTargKeepAliveFactor_Type()
)
vRtrLdpGenTargKeepAliveFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTargKeepAliveFactor.setStatus("obsolete")


class _VRtrLdpGenTargKeepAliveTimeout_Type(TmnxLdpNewKeepAliveTimeout):
    """Custom type vRtrLdpGenTargKeepAliveTimeout based on TmnxLdpNewKeepAliveTimeout"""
    defaultValue = 40


_VRtrLdpGenTargKeepAliveTimeout_Type.__name__ = "TmnxLdpNewKeepAliveTimeout"
_VRtrLdpGenTargKeepAliveTimeout_Object = MibTableColumn
vRtrLdpGenTargKeepAliveTimeout = _VRtrLdpGenTargKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 23),
    _VRtrLdpGenTargKeepAliveTimeout_Type()
)
vRtrLdpGenTargKeepAliveTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTargKeepAliveTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpGenTargKeepAliveTimeout.setUnits("seconds")


class _VRtrLdpGenTargHelloFactor_Type(TmnxLdpHelloFactor):
    """Custom type vRtrLdpGenTargHelloFactor based on TmnxLdpHelloFactor"""
    defaultValue = 3


_VRtrLdpGenTargHelloFactor_Type.__name__ = "TmnxLdpHelloFactor"
_VRtrLdpGenTargHelloFactor_Object = MibTableColumn
vRtrLdpGenTargHelloFactor = _VRtrLdpGenTargHelloFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 24),
    _VRtrLdpGenTargHelloFactor_Type()
)
vRtrLdpGenTargHelloFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTargHelloFactor.setStatus("obsolete")


class _VRtrLdpGenTargHelloTimeout_Type(TmnxLdpNewHelloTimeout):
    """Custom type vRtrLdpGenTargHelloTimeout based on TmnxLdpNewHelloTimeout"""
    defaultValue = 45


_VRtrLdpGenTargHelloTimeout_Type.__name__ = "TmnxLdpNewHelloTimeout"
_VRtrLdpGenTargHelloTimeout_Object = MibTableColumn
vRtrLdpGenTargHelloTimeout = _VRtrLdpGenTargHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 25),
    _VRtrLdpGenTargHelloTimeout_Type()
)
vRtrLdpGenTargHelloTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTargHelloTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpGenTargHelloTimeout.setUnits("seconds")


class _VRtrLdpGenTargPassiveMode_Type(TruthValue):
    """Custom type vRtrLdpGenTargPassiveMode based on TruthValue"""
    defaultValue = 2


_VRtrLdpGenTargPassiveMode_Type.__name__ = "TruthValue"
_VRtrLdpGenTargPassiveMode_Object = MibTableColumn
vRtrLdpGenTargPassiveMode = _VRtrLdpGenTargPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 26),
    _VRtrLdpGenTargPassiveMode_Type()
)
vRtrLdpGenTargPassiveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTargPassiveMode.setStatus("obsolete")


class _VRtrLdpGenTargetedSessions_Type(TruthValue):
    """Custom type vRtrLdpGenTargetedSessions based on TruthValue"""
    defaultValue = 1


_VRtrLdpGenTargetedSessions_Type.__name__ = "TruthValue"
_VRtrLdpGenTargetedSessions_Object = MibTableColumn
vRtrLdpGenTargetedSessions = _VRtrLdpGenTargetedSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 27),
    _VRtrLdpGenTargetedSessions_Type()
)
vRtrLdpGenTargetedSessions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTargetedSessions.setStatus("obsolete")
_VRtrLdpGenCreateTime_Type = TimeStamp
_VRtrLdpGenCreateTime_Object = MibTableColumn
vRtrLdpGenCreateTime = _VRtrLdpGenCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 28),
    _VRtrLdpGenCreateTime_Type()
)
vRtrLdpGenCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenCreateTime.setStatus("obsolete")
_VRtrLdpGenUpTime_Type = TimeInterval
_VRtrLdpGenUpTime_Object = MibTableColumn
vRtrLdpGenUpTime = _VRtrLdpGenUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 29),
    _VRtrLdpGenUpTime_Type()
)
vRtrLdpGenUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenUpTime.setStatus("obsolete")


class _VRtrLdpGenImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpGenImportPolicy1_Object = MibTableColumn
vRtrLdpGenImportPolicy1 = _VRtrLdpGenImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 30),
    _VRtrLdpGenImportPolicy1_Type()
)
vRtrLdpGenImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenImportPolicy1.setStatus("obsolete")


class _VRtrLdpGenImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpGenImportPolicy2_Object = MibTableColumn
vRtrLdpGenImportPolicy2 = _VRtrLdpGenImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 31),
    _VRtrLdpGenImportPolicy2_Type()
)
vRtrLdpGenImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenImportPolicy2.setStatus("obsolete")


class _VRtrLdpGenImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpGenImportPolicy3_Object = MibTableColumn
vRtrLdpGenImportPolicy3 = _VRtrLdpGenImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 32),
    _VRtrLdpGenImportPolicy3_Type()
)
vRtrLdpGenImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenImportPolicy3.setStatus("obsolete")


class _VRtrLdpGenImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpGenImportPolicy4_Object = MibTableColumn
vRtrLdpGenImportPolicy4 = _VRtrLdpGenImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 33),
    _VRtrLdpGenImportPolicy4_Type()
)
vRtrLdpGenImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenImportPolicy4.setStatus("obsolete")


class _VRtrLdpGenImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpGenImportPolicy5_Object = MibTableColumn
vRtrLdpGenImportPolicy5 = _VRtrLdpGenImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 34),
    _VRtrLdpGenImportPolicy5_Type()
)
vRtrLdpGenImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenImportPolicy5.setStatus("obsolete")


class _VRtrLdpGenExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpGenExportPolicy1_Object = MibTableColumn
vRtrLdpGenExportPolicy1 = _VRtrLdpGenExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 35),
    _VRtrLdpGenExportPolicy1_Type()
)
vRtrLdpGenExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenExportPolicy1.setStatus("obsolete")


class _VRtrLdpGenExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpGenExportPolicy2_Object = MibTableColumn
vRtrLdpGenExportPolicy2 = _VRtrLdpGenExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 36),
    _VRtrLdpGenExportPolicy2_Type()
)
vRtrLdpGenExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenExportPolicy2.setStatus("obsolete")


class _VRtrLdpGenExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpGenExportPolicy3_Object = MibTableColumn
vRtrLdpGenExportPolicy3 = _VRtrLdpGenExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 37),
    _VRtrLdpGenExportPolicy3_Type()
)
vRtrLdpGenExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenExportPolicy3.setStatus("obsolete")


class _VRtrLdpGenExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpGenExportPolicy4_Object = MibTableColumn
vRtrLdpGenExportPolicy4 = _VRtrLdpGenExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 38),
    _VRtrLdpGenExportPolicy4_Type()
)
vRtrLdpGenExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenExportPolicy4.setStatus("obsolete")


class _VRtrLdpGenExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpGenExportPolicy5_Object = MibTableColumn
vRtrLdpGenExportPolicy5 = _VRtrLdpGenExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 39),
    _VRtrLdpGenExportPolicy5_Type()
)
vRtrLdpGenExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenExportPolicy5.setStatus("obsolete")


class _VRtrLdpGenTunnelDownDampTime_Type(Unsigned32):
    """Custom type vRtrLdpGenTunnelDownDampTime based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_VRtrLdpGenTunnelDownDampTime_Type.__name__ = "Unsigned32"
_VRtrLdpGenTunnelDownDampTime_Object = MibTableColumn
vRtrLdpGenTunnelDownDampTime = _VRtrLdpGenTunnelDownDampTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 40),
    _VRtrLdpGenTunnelDownDampTime_Type()
)
vRtrLdpGenTunnelDownDampTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTunnelDownDampTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpGenTunnelDownDampTime.setUnits("seconds")
_VRtrLdpGenOperDownReason_Type = TmnxLdpGenOperDownReasonCode
_VRtrLdpGenOperDownReason_Object = MibTableColumn
vRtrLdpGenOperDownReason = _VRtrLdpGenOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 41),
    _VRtrLdpGenOperDownReason_Type()
)
vRtrLdpGenOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenOperDownReason.setStatus("obsolete")


class _VRtrLdpGenTrustList_Type(TFilterID):
    """Custom type vRtrLdpGenTrustList based on TFilterID"""
    defaultValue = 0


_VRtrLdpGenTrustList_Type.__name__ = "TFilterID"
_VRtrLdpGenTrustList_Object = MibTableColumn
vRtrLdpGenTrustList = _VRtrLdpGenTrustList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 42),
    _VRtrLdpGenTrustList_Type()
)
vRtrLdpGenTrustList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTrustList.setStatus("obsolete")


class _VRtrLdpGenGracefulRestart_Type(TruthValue):
    """Custom type vRtrLdpGenGracefulRestart based on TruthValue"""
    defaultValue = 2


_VRtrLdpGenGracefulRestart_Type.__name__ = "TruthValue"
_VRtrLdpGenGracefulRestart_Object = MibTableColumn
vRtrLdpGenGracefulRestart = _VRtrLdpGenGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 43),
    _VRtrLdpGenGracefulRestart_Type()
)
vRtrLdpGenGracefulRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenGracefulRestart.setStatus("obsolete")


class _VRtrLdpGenGRNbrLiveTime_Type(Unsigned32):
    """Custom type vRtrLdpGenGRNbrLiveTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_VRtrLdpGenGRNbrLiveTime_Type.__name__ = "Unsigned32"
_VRtrLdpGenGRNbrLiveTime_Object = MibTableColumn
vRtrLdpGenGRNbrLiveTime = _VRtrLdpGenGRNbrLiveTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 44),
    _VRtrLdpGenGRNbrLiveTime_Type()
)
vRtrLdpGenGRNbrLiveTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenGRNbrLiveTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpGenGRNbrLiveTime.setUnits("seconds")


class _VRtrLdpGenGRMaxRecoveryTime_Type(Unsigned32):
    """Custom type vRtrLdpGenGRMaxRecoveryTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 1800),
    )


_VRtrLdpGenGRMaxRecoveryTime_Type.__name__ = "Unsigned32"
_VRtrLdpGenGRMaxRecoveryTime_Object = MibTableColumn
vRtrLdpGenGRMaxRecoveryTime = _VRtrLdpGenGRMaxRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 45),
    _VRtrLdpGenGRMaxRecoveryTime_Type()
)
vRtrLdpGenGRMaxRecoveryTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenGRMaxRecoveryTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpGenGRMaxRecoveryTime.setUnits("seconds")


class _VRtrLdpGenLabelWithdrawalDelay_Type(Unsigned32):
    """Custom type vRtrLdpGenLabelWithdrawalDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 120),
    )


_VRtrLdpGenLabelWithdrawalDelay_Type.__name__ = "Unsigned32"
_VRtrLdpGenLabelWithdrawalDelay_Object = MibTableColumn
vRtrLdpGenLabelWithdrawalDelay = _VRtrLdpGenLabelWithdrawalDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 46),
    _VRtrLdpGenLabelWithdrawalDelay_Type()
)
vRtrLdpGenLabelWithdrawalDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenLabelWithdrawalDelay.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpGenLabelWithdrawalDelay.setUnits("seconds")


class _VRtrLdpGenImplicitNull_Type(TruthValue):
    """Custom type vRtrLdpGenImplicitNull based on TruthValue"""
    defaultValue = 2


_VRtrLdpGenImplicitNull_Type.__name__ = "TruthValue"
_VRtrLdpGenImplicitNull_Object = MibTableColumn
vRtrLdpGenImplicitNull = _VRtrLdpGenImplicitNull_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 47),
    _VRtrLdpGenImplicitNull_Type()
)
vRtrLdpGenImplicitNull.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenImplicitNull.setStatus("obsolete")


class _VRtrLdpGenShortTTLPropLocal_Type(TruthValue):
    """Custom type vRtrLdpGenShortTTLPropLocal based on TruthValue"""
    defaultValue = 1


_VRtrLdpGenShortTTLPropLocal_Type.__name__ = "TruthValue"
_VRtrLdpGenShortTTLPropLocal_Object = MibTableColumn
vRtrLdpGenShortTTLPropLocal = _VRtrLdpGenShortTTLPropLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 48),
    _VRtrLdpGenShortTTLPropLocal_Type()
)
vRtrLdpGenShortTTLPropLocal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenShortTTLPropLocal.setStatus("obsolete")


class _VRtrLdpGenShortTTLPropTransit_Type(TruthValue):
    """Custom type vRtrLdpGenShortTTLPropTransit based on TruthValue"""
    defaultValue = 1


_VRtrLdpGenShortTTLPropTransit_Type.__name__ = "TruthValue"
_VRtrLdpGenShortTTLPropTransit_Object = MibTableColumn
vRtrLdpGenShortTTLPropTransit = _VRtrLdpGenShortTTLPropTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 49),
    _VRtrLdpGenShortTTLPropTransit_Type()
)
vRtrLdpGenShortTTLPropTransit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenShortTTLPropTransit.setStatus("obsolete")


class _VRtrLdpGenMPMBBTime_Type(Unsigned32):
    """Custom type vRtrLdpGenMPMBBTime based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VRtrLdpGenMPMBBTime_Type.__name__ = "Unsigned32"
_VRtrLdpGenMPMBBTime_Object = MibTableColumn
vRtrLdpGenMPMBBTime = _VRtrLdpGenMPMBBTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 50),
    _VRtrLdpGenMPMBBTime_Type()
)
vRtrLdpGenMPMBBTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenMPMBBTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpGenMPMBBTime.setUnits("seconds")


class _VRtrLdpGenTunlTblExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenTunlTblExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenTunlTblExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpGenTunlTblExportPolicy1_Object = MibTableColumn
vRtrLdpGenTunlTblExportPolicy1 = _VRtrLdpGenTunlTblExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 51),
    _VRtrLdpGenTunlTblExportPolicy1_Type()
)
vRtrLdpGenTunlTblExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTunlTblExportPolicy1.setStatus("obsolete")


class _VRtrLdpGenTunlTblExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenTunlTblExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenTunlTblExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpGenTunlTblExportPolicy2_Object = MibTableColumn
vRtrLdpGenTunlTblExportPolicy2 = _VRtrLdpGenTunlTblExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 52),
    _VRtrLdpGenTunlTblExportPolicy2_Type()
)
vRtrLdpGenTunlTblExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTunlTblExportPolicy2.setStatus("obsolete")


class _VRtrLdpGenTunlTblExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenTunlTblExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenTunlTblExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpGenTunlTblExportPolicy3_Object = MibTableColumn
vRtrLdpGenTunlTblExportPolicy3 = _VRtrLdpGenTunlTblExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 53),
    _VRtrLdpGenTunlTblExportPolicy3_Type()
)
vRtrLdpGenTunlTblExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTunlTblExportPolicy3.setStatus("obsolete")


class _VRtrLdpGenTunlTblExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenTunlTblExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenTunlTblExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpGenTunlTblExportPolicy4_Object = MibTableColumn
vRtrLdpGenTunlTblExportPolicy4 = _VRtrLdpGenTunlTblExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 54),
    _VRtrLdpGenTunlTblExportPolicy4_Type()
)
vRtrLdpGenTunlTblExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTunlTblExportPolicy4.setStatus("obsolete")


class _VRtrLdpGenTunlTblExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenTunlTblExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenTunlTblExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpGenTunlTblExportPolicy5_Object = MibTableColumn
vRtrLdpGenTunlTblExportPolicy5 = _VRtrLdpGenTunlTblExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 55),
    _VRtrLdpGenTunlTblExportPolicy5_Type()
)
vRtrLdpGenTunlTblExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTunlTblExportPolicy5.setStatus("obsolete")


class _VRtrLdpGenP2MPCapability_Type(TruthValue):
    """Custom type vRtrLdpGenP2MPCapability based on TruthValue"""
    defaultValue = 2


_VRtrLdpGenP2MPCapability_Type.__name__ = "TruthValue"
_VRtrLdpGenP2MPCapability_Object = MibTableColumn
vRtrLdpGenP2MPCapability = _VRtrLdpGenP2MPCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 56),
    _VRtrLdpGenP2MPCapability_Type()
)
vRtrLdpGenP2MPCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenP2MPCapability.setStatus("obsolete")


class _VRtrLdpGenMPMBBCapability_Type(TruthValue):
    """Custom type vRtrLdpGenMPMBBCapability based on TruthValue"""
    defaultValue = 2


_VRtrLdpGenMPMBBCapability_Type.__name__ = "TruthValue"
_VRtrLdpGenMPMBBCapability_Object = MibTableColumn
vRtrLdpGenMPMBBCapability = _VRtrLdpGenMPMBBCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 57),
    _VRtrLdpGenMPMBBCapability_Type()
)
vRtrLdpGenMPMBBCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenMPMBBCapability.setStatus("obsolete")


class _VRtrLdpGenDynamicCapability_Type(TruthValue):
    """Custom type vRtrLdpGenDynamicCapability based on TruthValue"""
    defaultValue = 2


_VRtrLdpGenDynamicCapability_Type.__name__ = "TruthValue"
_VRtrLdpGenDynamicCapability_Object = MibTableColumn
vRtrLdpGenDynamicCapability = _VRtrLdpGenDynamicCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 58),
    _VRtrLdpGenDynamicCapability_Type()
)
vRtrLdpGenDynamicCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenDynamicCapability.setStatus("obsolete")


class _VRtrLdpGenLdpFrr_Type(TruthValue):
    """Custom type vRtrLdpGenLdpFrr based on TruthValue"""
    defaultValue = 2


_VRtrLdpGenLdpFrr_Type.__name__ = "TruthValue"
_VRtrLdpGenLdpFrr_Object = MibTableColumn
vRtrLdpGenLdpFrr = _VRtrLdpGenLdpFrr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 59),
    _VRtrLdpGenLdpFrr_Type()
)
vRtrLdpGenLdpFrr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenLdpFrr.setStatus("obsolete")


class _VRtrLdpGenTargHelloReduction_Type(TruthValue):
    """Custom type vRtrLdpGenTargHelloReduction based on TruthValue"""
    defaultValue = 2


_VRtrLdpGenTargHelloReduction_Type.__name__ = "TruthValue"
_VRtrLdpGenTargHelloReduction_Object = MibTableColumn
vRtrLdpGenTargHelloReduction = _VRtrLdpGenTargHelloReduction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 60),
    _VRtrLdpGenTargHelloReduction_Type()
)
vRtrLdpGenTargHelloReduction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTargHelloReduction.setStatus("obsolete")


class _VRtrLdpGenTargHelloReductionFctr_Type(Unsigned32):
    """Custom type vRtrLdpGenTargHelloReductionFctr based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_VRtrLdpGenTargHelloReductionFctr_Type.__name__ = "Unsigned32"
_VRtrLdpGenTargHelloReductionFctr_Object = MibTableColumn
vRtrLdpGenTargHelloReductionFctr = _VRtrLdpGenTargHelloReductionFctr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 61),
    _VRtrLdpGenTargHelloReductionFctr_Type()
)
vRtrLdpGenTargHelloReductionFctr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTargHelloReductionFctr.setStatus("obsolete")


class _VRtrLdpGenMcastUpstreamFrr_Type(TruthValue):
    """Custom type vRtrLdpGenMcastUpstreamFrr based on TruthValue"""
    defaultValue = 2


_VRtrLdpGenMcastUpstreamFrr_Type.__name__ = "TruthValue"
_VRtrLdpGenMcastUpstreamFrr_Object = MibTableColumn
vRtrLdpGenMcastUpstreamFrr = _VRtrLdpGenMcastUpstreamFrr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 62),
    _VRtrLdpGenMcastUpstreamFrr_Type()
)
vRtrLdpGenMcastUpstreamFrr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenMcastUpstreamFrr.setStatus("obsolete")
_VRtrLdpGenOverloadCapability_Type = TruthValue
_VRtrLdpGenOverloadCapability_Object = MibTableColumn
vRtrLdpGenOverloadCapability = _VRtrLdpGenOverloadCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 63),
    _VRtrLdpGenOverloadCapability_Type()
)
vRtrLdpGenOverloadCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenOverloadCapability.setStatus("obsolete")
_VRtrLdpStatsTable_Object = MibTable
vRtrLdpStatsTable = _VRtrLdpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    vRtrLdpStatsTable.setStatus("obsolete")
_VRtrLdpStatsEntry_Object = MibTableRow
vRtrLdpStatsEntry = _VRtrLdpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpStatsEntry.setStatus("obsolete")
_VRtrLdpStatsOperDownEvents_Type = Counter32
_VRtrLdpStatsOperDownEvents_Object = MibTableColumn
vRtrLdpStatsOperDownEvents = _VRtrLdpStatsOperDownEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 1),
    _VRtrLdpStatsOperDownEvents_Type()
)
vRtrLdpStatsOperDownEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsOperDownEvents.setStatus("obsolete")
_VRtrLdpStatsActiveSessions_Type = Gauge32
_VRtrLdpStatsActiveSessions_Object = MibTableColumn
vRtrLdpStatsActiveSessions = _VRtrLdpStatsActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 2),
    _VRtrLdpStatsActiveSessions_Type()
)
vRtrLdpStatsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsActiveSessions.setStatus("obsolete")
_VRtrLdpStatsActiveAdjacencies_Type = Gauge32
_VRtrLdpStatsActiveAdjacencies_Object = MibTableColumn
vRtrLdpStatsActiveAdjacencies = _VRtrLdpStatsActiveAdjacencies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 3),
    _VRtrLdpStatsActiveAdjacencies_Type()
)
vRtrLdpStatsActiveAdjacencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsActiveAdjacencies.setStatus("obsolete")
_VRtrLdpStatsActiveInterfaces_Type = Gauge32
_VRtrLdpStatsActiveInterfaces_Object = MibTableColumn
vRtrLdpStatsActiveInterfaces = _VRtrLdpStatsActiveInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 4),
    _VRtrLdpStatsActiveInterfaces_Type()
)
vRtrLdpStatsActiveInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsActiveInterfaces.setStatus("obsolete")
_VRtrLdpStatsInactiveInterfaces_Type = Gauge32
_VRtrLdpStatsInactiveInterfaces_Object = MibTableColumn
vRtrLdpStatsInactiveInterfaces = _VRtrLdpStatsInactiveInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 5),
    _VRtrLdpStatsInactiveInterfaces_Type()
)
vRtrLdpStatsInactiveInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsInactiveInterfaces.setStatus("obsolete")
_VRtrLdpStatsActiveTargSessions_Type = Gauge32
_VRtrLdpStatsActiveTargSessions_Object = MibTableColumn
vRtrLdpStatsActiveTargSessions = _VRtrLdpStatsActiveTargSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 6),
    _VRtrLdpStatsActiveTargSessions_Type()
)
vRtrLdpStatsActiveTargSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsActiveTargSessions.setStatus("obsolete")
_VRtrLdpStatsInactiveTargSessions_Type = Gauge32
_VRtrLdpStatsInactiveTargSessions_Object = MibTableColumn
vRtrLdpStatsInactiveTargSessions = _VRtrLdpStatsInactiveTargSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 7),
    _VRtrLdpStatsInactiveTargSessions_Type()
)
vRtrLdpStatsInactiveTargSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsInactiveTargSessions.setStatus("obsolete")
_VRtrLdpStatsAddrFECRecv_Type = Gauge32
_VRtrLdpStatsAddrFECRecv_Object = MibTableColumn
vRtrLdpStatsAddrFECRecv = _VRtrLdpStatsAddrFECRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 8),
    _VRtrLdpStatsAddrFECRecv_Type()
)
vRtrLdpStatsAddrFECRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsAddrFECRecv.setStatus("obsolete")
_VRtrLdpStatsAddrFECSent_Type = Gauge32
_VRtrLdpStatsAddrFECSent_Object = MibTableColumn
vRtrLdpStatsAddrFECSent = _VRtrLdpStatsAddrFECSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 9),
    _VRtrLdpStatsAddrFECSent_Type()
)
vRtrLdpStatsAddrFECSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsAddrFECSent.setStatus("obsolete")
_VRtrLdpStatsSvcFECRecv_Type = Gauge32
_VRtrLdpStatsSvcFECRecv_Object = MibTableColumn
vRtrLdpStatsSvcFECRecv = _VRtrLdpStatsSvcFECRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 10),
    _VRtrLdpStatsSvcFECRecv_Type()
)
vRtrLdpStatsSvcFECRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsSvcFECRecv.setStatus("obsolete")
_VRtrLdpStatsSvcFECSent_Type = Gauge32
_VRtrLdpStatsSvcFECSent_Object = MibTableColumn
vRtrLdpStatsSvcFECSent = _VRtrLdpStatsSvcFECSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 11),
    _VRtrLdpStatsSvcFECSent_Type()
)
vRtrLdpStatsSvcFECSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsSvcFECSent.setStatus("obsolete")
_VRtrLdpStatsAttemptedSessions_Type = Counter32
_VRtrLdpStatsAttemptedSessions_Object = MibTableColumn
vRtrLdpStatsAttemptedSessions = _VRtrLdpStatsAttemptedSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 12),
    _VRtrLdpStatsAttemptedSessions_Type()
)
vRtrLdpStatsAttemptedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsAttemptedSessions.setStatus("obsolete")
_VRtrLdpStatsSessRejNoHelloErrors_Type = Counter32
_VRtrLdpStatsSessRejNoHelloErrors_Object = MibTableColumn
vRtrLdpStatsSessRejNoHelloErrors = _VRtrLdpStatsSessRejNoHelloErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 13),
    _VRtrLdpStatsSessRejNoHelloErrors_Type()
)
vRtrLdpStatsSessRejNoHelloErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsSessRejNoHelloErrors.setStatus("obsolete")
_VRtrLdpStatsSessRejAdvErrors_Type = Counter32
_VRtrLdpStatsSessRejAdvErrors_Object = MibTableColumn
vRtrLdpStatsSessRejAdvErrors = _VRtrLdpStatsSessRejAdvErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 14),
    _VRtrLdpStatsSessRejAdvErrors_Type()
)
vRtrLdpStatsSessRejAdvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsSessRejAdvErrors.setStatus("obsolete")
_VRtrLdpStatsSessRejMaxPduErrors_Type = Counter32
_VRtrLdpStatsSessRejMaxPduErrors_Object = MibTableColumn
vRtrLdpStatsSessRejMaxPduErrors = _VRtrLdpStatsSessRejMaxPduErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 15),
    _VRtrLdpStatsSessRejMaxPduErrors_Type()
)
vRtrLdpStatsSessRejMaxPduErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsSessRejMaxPduErrors.setStatus("obsolete")
_VRtrLdpStatsSessRejLabelRangeErrors_Type = Counter32
_VRtrLdpStatsSessRejLabelRangeErrors_Object = MibTableColumn
vRtrLdpStatsSessRejLabelRangeErrors = _VRtrLdpStatsSessRejLabelRangeErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 16),
    _VRtrLdpStatsSessRejLabelRangeErrors_Type()
)
vRtrLdpStatsSessRejLabelRangeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsSessRejLabelRangeErrors.setStatus("obsolete")
_VRtrLdpStatsBadLdpIdentifierErrors_Type = Counter32
_VRtrLdpStatsBadLdpIdentifierErrors_Object = MibTableColumn
vRtrLdpStatsBadLdpIdentifierErrors = _VRtrLdpStatsBadLdpIdentifierErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 17),
    _VRtrLdpStatsBadLdpIdentifierErrors_Type()
)
vRtrLdpStatsBadLdpIdentifierErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsBadLdpIdentifierErrors.setStatus("obsolete")
_VRtrLdpStatsBadPduLengthErrors_Type = Counter32
_VRtrLdpStatsBadPduLengthErrors_Object = MibTableColumn
vRtrLdpStatsBadPduLengthErrors = _VRtrLdpStatsBadPduLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 18),
    _VRtrLdpStatsBadPduLengthErrors_Type()
)
vRtrLdpStatsBadPduLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsBadPduLengthErrors.setStatus("obsolete")
_VRtrLdpStatsBadMessageLengthErrors_Type = Counter32
_VRtrLdpStatsBadMessageLengthErrors_Object = MibTableColumn
vRtrLdpStatsBadMessageLengthErrors = _VRtrLdpStatsBadMessageLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 19),
    _VRtrLdpStatsBadMessageLengthErrors_Type()
)
vRtrLdpStatsBadMessageLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsBadMessageLengthErrors.setStatus("obsolete")
_VRtrLdpStatsBadTlvLengthErrors_Type = Counter32
_VRtrLdpStatsBadTlvLengthErrors_Object = MibTableColumn
vRtrLdpStatsBadTlvLengthErrors = _VRtrLdpStatsBadTlvLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 20),
    _VRtrLdpStatsBadTlvLengthErrors_Type()
)
vRtrLdpStatsBadTlvLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsBadTlvLengthErrors.setStatus("obsolete")
_VRtrLdpStatsMalformedTlvValueErrors_Type = Counter32
_VRtrLdpStatsMalformedTlvValueErrors_Object = MibTableColumn
vRtrLdpStatsMalformedTlvValueErrors = _VRtrLdpStatsMalformedTlvValueErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 21),
    _VRtrLdpStatsMalformedTlvValueErrors_Type()
)
vRtrLdpStatsMalformedTlvValueErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsMalformedTlvValueErrors.setStatus("obsolete")
_VRtrLdpStatsKeepAliveExpiredErrors_Type = Counter32
_VRtrLdpStatsKeepAliveExpiredErrors_Object = MibTableColumn
vRtrLdpStatsKeepAliveExpiredErrors = _VRtrLdpStatsKeepAliveExpiredErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 22),
    _VRtrLdpStatsKeepAliveExpiredErrors_Type()
)
vRtrLdpStatsKeepAliveExpiredErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsKeepAliveExpiredErrors.setStatus("obsolete")
_VRtrLdpStatsShutdownNotifRecv_Type = Counter32
_VRtrLdpStatsShutdownNotifRecv_Object = MibTableColumn
vRtrLdpStatsShutdownNotifRecv = _VRtrLdpStatsShutdownNotifRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 23),
    _VRtrLdpStatsShutdownNotifRecv_Type()
)
vRtrLdpStatsShutdownNotifRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsShutdownNotifRecv.setStatus("obsolete")
_VRtrLdpStatsShutdownNotifSent_Type = Counter32
_VRtrLdpStatsShutdownNotifSent_Object = MibTableColumn
vRtrLdpStatsShutdownNotifSent = _VRtrLdpStatsShutdownNotifSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 24),
    _VRtrLdpStatsShutdownNotifSent_Type()
)
vRtrLdpStatsShutdownNotifSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsShutdownNotifSent.setStatus("obsolete")
_VRtrLdpStatsEgrFecPfxCount_Type = Counter32
_VRtrLdpStatsEgrFecPfxCount_Object = MibTableColumn
vRtrLdpStatsEgrFecPfxCount = _VRtrLdpStatsEgrFecPfxCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 25),
    _VRtrLdpStatsEgrFecPfxCount_Type()
)
vRtrLdpStatsEgrFecPfxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsEgrFecPfxCount.setStatus("obsolete")
_VRtrLdpStatsUnknownTlvErrors_Type = Counter32
_VRtrLdpStatsUnknownTlvErrors_Object = MibTableColumn
vRtrLdpStatsUnknownTlvErrors = _VRtrLdpStatsUnknownTlvErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 26),
    _VRtrLdpStatsUnknownTlvErrors_Type()
)
vRtrLdpStatsUnknownTlvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsUnknownTlvErrors.setStatus("obsolete")
_VRtrLdpStatsP2MPFECSent_Type = Gauge32
_VRtrLdpStatsP2MPFECSent_Object = MibTableColumn
vRtrLdpStatsP2MPFECSent = _VRtrLdpStatsP2MPFECSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 27),
    _VRtrLdpStatsP2MPFECSent_Type()
)
vRtrLdpStatsP2MPFECSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsP2MPFECSent.setStatus("obsolete")
_VRtrLdpStatsP2MPFECRecv_Type = Gauge32
_VRtrLdpStatsP2MPFECRecv_Object = MibTableColumn
vRtrLdpStatsP2MPFECRecv = _VRtrLdpStatsP2MPFECRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 28),
    _VRtrLdpStatsP2MPFECRecv_Type()
)
vRtrLdpStatsP2MPFECRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsP2MPFECRecv.setStatus("obsolete")
_VRtrLdpPolicyTable_Object = MibTable
vRtrLdpPolicyTable = _VRtrLdpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    vRtrLdpPolicyTable.setStatus("obsolete")
_VRtrLdpPolicyEntry_Object = MibTableRow
vRtrLdpPolicyEntry = _VRtrLdpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 3, 1)
)
vRtrLdpPolicyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPolicyType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPolicyIndex"),
)
if mibBuilder.loadTexts:
    vRtrLdpPolicyEntry.setStatus("obsolete")


class _VRtrLdpPolicyType_Type(Integer32):
    """Custom type vRtrLdpPolicyType based on Integer32"""
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
        *(("import", 1),
          ("export", 2),
          ("ingress", 3),
          ("egress", 4))
    )


_VRtrLdpPolicyType_Type.__name__ = "Integer32"
_VRtrLdpPolicyType_Object = MibTableColumn
vRtrLdpPolicyType = _VRtrLdpPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 3, 1, 1),
    _VRtrLdpPolicyType_Type()
)
vRtrLdpPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpPolicyType.setStatus("obsolete")


class _VRtrLdpPolicyIndex_Type(Unsigned32):
    """Custom type vRtrLdpPolicyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_VRtrLdpPolicyIndex_Type.__name__ = "Unsigned32"
_VRtrLdpPolicyIndex_Object = MibTableColumn
vRtrLdpPolicyIndex = _VRtrLdpPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 3, 1, 2),
    _VRtrLdpPolicyIndex_Type()
)
vRtrLdpPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpPolicyIndex.setStatus("obsolete")
_VRtrLdpPolicyRowStatus_Type = RowStatus
_VRtrLdpPolicyRowStatus_Object = MibTableColumn
vRtrLdpPolicyRowStatus = _VRtrLdpPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 3, 1, 3),
    _VRtrLdpPolicyRowStatus_Type()
)
vRtrLdpPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPolicyRowStatus.setStatus("obsolete")


class _VRtrLdpPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpPolicyName_Object = MibTableColumn
vRtrLdpPolicyName = _VRtrLdpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 3, 1, 4),
    _VRtrLdpPolicyName_Type()
)
vRtrLdpPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPolicyName.setStatus("obsolete")


class _VRtrLdpIfTableSpinlock_Type(TestAndIncr):
    """Custom type vRtrLdpIfTableSpinlock based on TestAndIncr"""
    defaultValue = 0


_VRtrLdpIfTableSpinlock_Type.__name__ = "TestAndIncr"
_VRtrLdpIfTableSpinlock_Object = MibScalar
vRtrLdpIfTableSpinlock = _VRtrLdpIfTableSpinlock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 4),
    _VRtrLdpIfTableSpinlock_Type()
)
vRtrLdpIfTableSpinlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpIfTableSpinlock.setStatus("obsolete")
_VRtrLdpIfTable_Object = MibTable
vRtrLdpIfTable = _VRtrLdpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5)
)
if mibBuilder.loadTexts:
    vRtrLdpIfTable.setStatus("obsolete")
_VRtrLdpIfEntry_Object = MibTableRow
vRtrLdpIfEntry = _VRtrLdpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1)
)
vRtrLdpIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpIfIndex"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerAddress"),
)
if mibBuilder.loadTexts:
    vRtrLdpIfEntry.setStatus("obsolete")
_VRtrLdpIfIndex_Type = InterfaceIndexOrZero
_VRtrLdpIfIndex_Object = MibTableColumn
vRtrLdpIfIndex = _VRtrLdpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 1),
    _VRtrLdpIfIndex_Type()
)
vRtrLdpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpIfIndex.setStatus("obsolete")
_VRtrLdpPeerAddress_Type = IpAddress
_VRtrLdpPeerAddress_Object = MibTableColumn
vRtrLdpPeerAddress = _VRtrLdpPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 2),
    _VRtrLdpPeerAddress_Type()
)
vRtrLdpPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpPeerAddress.setStatus("obsolete")
_VRtrLdpIfRowStatus_Type = RowStatus
_VRtrLdpIfRowStatus_Object = MibTableColumn
vRtrLdpIfRowStatus = _VRtrLdpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 3),
    _VRtrLdpIfRowStatus_Type()
)
vRtrLdpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfRowStatus.setStatus("obsolete")
_VRtrLdpIfLastChange_Type = TimeStamp
_VRtrLdpIfLastChange_Object = MibTableColumn
vRtrLdpIfLastChange = _VRtrLdpIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 4),
    _VRtrLdpIfLastChange_Type()
)
vRtrLdpIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpIfLastChange.setStatus("obsolete")


class _VRtrLdpIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrLdpIfAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrLdpIfAdminState_Type.__name__ = "TmnxAdminState"
_VRtrLdpIfAdminState_Object = MibTableColumn
vRtrLdpIfAdminState = _VRtrLdpIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 5),
    _VRtrLdpIfAdminState_Type()
)
vRtrLdpIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfAdminState.setStatus("obsolete")
_VRtrLdpIfOperState_Type = TmnxOperState
_VRtrLdpIfOperState_Object = MibTableColumn
vRtrLdpIfOperState = _VRtrLdpIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 6),
    _VRtrLdpIfOperState_Type()
)
vRtrLdpIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpIfOperState.setStatus("obsolete")


class _VRtrLdpIfInheritance_Type(Unsigned32):
    """Custom type vRtrLdpIfInheritance based on Unsigned32"""
    defaultValue = 0


_VRtrLdpIfInheritance_Type.__name__ = "Unsigned32"
_VRtrLdpIfInheritance_Object = MibTableColumn
vRtrLdpIfInheritance = _VRtrLdpIfInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 7),
    _VRtrLdpIfInheritance_Type()
)
vRtrLdpIfInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfInheritance.setStatus("obsolete")


class _VRtrLdpIfKeepAliveFactor_Type(TmnxLdpKeepAliveFactor):
    """Custom type vRtrLdpIfKeepAliveFactor based on TmnxLdpKeepAliveFactor"""
    defaultValue = 3


_VRtrLdpIfKeepAliveFactor_Type.__name__ = "TmnxLdpKeepAliveFactor"
_VRtrLdpIfKeepAliveFactor_Object = MibTableColumn
vRtrLdpIfKeepAliveFactor = _VRtrLdpIfKeepAliveFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 8),
    _VRtrLdpIfKeepAliveFactor_Type()
)
vRtrLdpIfKeepAliveFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfKeepAliveFactor.setStatus("obsolete")


class _VRtrLdpIfKeepAliveTimeout_Type(TmnxLdpNewKeepAliveTimeout):
    """Custom type vRtrLdpIfKeepAliveTimeout based on TmnxLdpNewKeepAliveTimeout"""
    defaultValue = 30


_VRtrLdpIfKeepAliveTimeout_Type.__name__ = "TmnxLdpNewKeepAliveTimeout"
_VRtrLdpIfKeepAliveTimeout_Object = MibTableColumn
vRtrLdpIfKeepAliveTimeout = _VRtrLdpIfKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 9),
    _VRtrLdpIfKeepAliveTimeout_Type()
)
vRtrLdpIfKeepAliveTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfKeepAliveTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpIfKeepAliveTimeout.setUnits("seconds")


class _VRtrLdpIfHelloFactor_Type(TmnxLdpHelloFactor):
    """Custom type vRtrLdpIfHelloFactor based on TmnxLdpHelloFactor"""
    defaultValue = 3


_VRtrLdpIfHelloFactor_Type.__name__ = "TmnxLdpHelloFactor"
_VRtrLdpIfHelloFactor_Object = MibTableColumn
vRtrLdpIfHelloFactor = _VRtrLdpIfHelloFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 10),
    _VRtrLdpIfHelloFactor_Type()
)
vRtrLdpIfHelloFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfHelloFactor.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpIfHelloFactor.setUnits("seconds")


class _VRtrLdpIfHelloTimeout_Type(TmnxLdpNewHelloTimeout):
    """Custom type vRtrLdpIfHelloTimeout based on TmnxLdpNewHelloTimeout"""
    defaultValue = 15


_VRtrLdpIfHelloTimeout_Type.__name__ = "TmnxLdpNewHelloTimeout"
_VRtrLdpIfHelloTimeout_Object = MibTableColumn
vRtrLdpIfHelloTimeout = _VRtrLdpIfHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 11),
    _VRtrLdpIfHelloTimeout_Type()
)
vRtrLdpIfHelloTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfHelloTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpIfHelloTimeout.setUnits("seconds")


class _VRtrLdpIfBackoffTime_Type(TmnxLdpBackoffTime):
    """Custom type vRtrLdpIfBackoffTime based on TmnxLdpBackoffTime"""
    defaultValue = 15

    subtypeSpec = TmnxLdpBackoffTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2592000),
    )


_VRtrLdpIfBackoffTime_Type.__name__ = "TmnxLdpBackoffTime"
_VRtrLdpIfBackoffTime_Object = MibTableColumn
vRtrLdpIfBackoffTime = _VRtrLdpIfBackoffTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 12),
    _VRtrLdpIfBackoffTime_Type()
)
vRtrLdpIfBackoffTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfBackoffTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpIfBackoffTime.setUnits("seconds")


class _VRtrLdpIfMaxBackoffTime_Type(TmnxLdpBackoffTime):
    """Custom type vRtrLdpIfMaxBackoffTime based on TmnxLdpBackoffTime"""
    defaultValue = 120


_VRtrLdpIfMaxBackoffTime_Type.__name__ = "TmnxLdpBackoffTime"
_VRtrLdpIfMaxBackoffTime_Object = MibTableColumn
vRtrLdpIfMaxBackoffTime = _VRtrLdpIfMaxBackoffTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 13),
    _VRtrLdpIfMaxBackoffTime_Type()
)
vRtrLdpIfMaxBackoffTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfMaxBackoffTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpIfMaxBackoffTime.setUnits("seconds")


class _VRtrLdpIfTransportAddrType_Type(Integer32):
    """Custom type vRtrLdpIfTransportAddrType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("system", 2))
    )


_VRtrLdpIfTransportAddrType_Type.__name__ = "Integer32"
_VRtrLdpIfTransportAddrType_Object = MibTableColumn
vRtrLdpIfTransportAddrType = _VRtrLdpIfTransportAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 14),
    _VRtrLdpIfTransportAddrType_Type()
)
vRtrLdpIfTransportAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfTransportAddrType.setStatus("obsolete")


class _VRtrLdpIfPassiveMode_Type(TruthValue):
    """Custom type vRtrLdpIfPassiveMode based on TruthValue"""
    defaultValue = 2


_VRtrLdpIfPassiveMode_Type.__name__ = "TruthValue"
_VRtrLdpIfPassiveMode_Object = MibTableColumn
vRtrLdpIfPassiveMode = _VRtrLdpIfPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 15),
    _VRtrLdpIfPassiveMode_Type()
)
vRtrLdpIfPassiveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfPassiveMode.setStatus("obsolete")
_VRtrLdpIfAutoCreate_Type = TruthValue
_VRtrLdpIfAutoCreate_Object = MibTableColumn
vRtrLdpIfAutoCreate = _VRtrLdpIfAutoCreate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 16),
    _VRtrLdpIfAutoCreate_Type()
)
vRtrLdpIfAutoCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpIfAutoCreate.setStatus("obsolete")
_VRtrLdpIfOperDownReason_Type = TmnxLdpIntTargOperDownReasonCode
_VRtrLdpIfOperDownReason_Object = MibTableColumn
vRtrLdpIfOperDownReason = _VRtrLdpIfOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 17),
    _VRtrLdpIfOperDownReason_Type()
)
vRtrLdpIfOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpIfOperDownReason.setStatus("obsolete")


class _VRtrLdpIfTunneling_Type(TruthValue):
    """Custom type vRtrLdpIfTunneling based on TruthValue"""
    defaultValue = 2


_VRtrLdpIfTunneling_Type.__name__ = "TruthValue"
_VRtrLdpIfTunneling_Object = MibTableColumn
vRtrLdpIfTunneling = _VRtrLdpIfTunneling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 18),
    _VRtrLdpIfTunneling_Type()
)
vRtrLdpIfTunneling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfTunneling.setStatus("obsolete")


class _VRtrLdpIfBfdEnabled_Type(TruthValue):
    """Custom type vRtrLdpIfBfdEnabled based on TruthValue"""
    defaultValue = 2


_VRtrLdpIfBfdEnabled_Type.__name__ = "TruthValue"
_VRtrLdpIfBfdEnabled_Object = MibTableColumn
vRtrLdpIfBfdEnabled = _VRtrLdpIfBfdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 19),
    _VRtrLdpIfBfdEnabled_Type()
)
vRtrLdpIfBfdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfBfdEnabled.setStatus("obsolete")


class _VRtrLdpIfLinkLsrIfType_Type(Integer32):
    """Custom type vRtrLdpIfLinkLsrIfType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("interface", 2))
    )


_VRtrLdpIfLinkLsrIfType_Type.__name__ = "Integer32"
_VRtrLdpIfLinkLsrIfType_Object = MibTableColumn
vRtrLdpIfLinkLsrIfType = _VRtrLdpIfLinkLsrIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 20),
    _VRtrLdpIfLinkLsrIfType_Type()
)
vRtrLdpIfLinkLsrIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfLinkLsrIfType.setStatus("obsolete")


class _VRtrLdpIfTargLsrIfIndex_Type(InterfaceIndexOrZero):
    """Custom type vRtrLdpIfTargLsrIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_VRtrLdpIfTargLsrIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_VRtrLdpIfTargLsrIfIndex_Object = MibTableColumn
vRtrLdpIfTargLsrIfIndex = _VRtrLdpIfTargLsrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 21),
    _VRtrLdpIfTargLsrIfIndex_Type()
)
vRtrLdpIfTargLsrIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfTargLsrIfIndex.setStatus("obsolete")


class _VRtrLdpIfMulticast_Type(TmnxEnabledDisabled):
    """Custom type vRtrLdpIfMulticast based on TmnxEnabledDisabled"""
    defaultValue = 1


_VRtrLdpIfMulticast_Type.__name__ = "TmnxEnabledDisabled"
_VRtrLdpIfMulticast_Object = MibTableColumn
vRtrLdpIfMulticast = _VRtrLdpIfMulticast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 22),
    _VRtrLdpIfMulticast_Type()
)
vRtrLdpIfMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfMulticast.setStatus("obsolete")


class _VRtrLdpIfHelloReduction_Type(TruthValue):
    """Custom type vRtrLdpIfHelloReduction based on TruthValue"""
    defaultValue = 2


_VRtrLdpIfHelloReduction_Type.__name__ = "TruthValue"
_VRtrLdpIfHelloReduction_Object = MibTableColumn
vRtrLdpIfHelloReduction = _VRtrLdpIfHelloReduction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 23),
    _VRtrLdpIfHelloReduction_Type()
)
vRtrLdpIfHelloReduction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfHelloReduction.setStatus("obsolete")


class _VRtrLdpIfHelloReductionFactor_Type(Unsigned32):
    """Custom type vRtrLdpIfHelloReductionFactor based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 20),
    )


_VRtrLdpIfHelloReductionFactor_Type.__name__ = "Unsigned32"
_VRtrLdpIfHelloReductionFactor_Object = MibTableColumn
vRtrLdpIfHelloReductionFactor = _VRtrLdpIfHelloReductionFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 24),
    _VRtrLdpIfHelloReductionFactor_Type()
)
vRtrLdpIfHelloReductionFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfHelloReductionFactor.setStatus("obsolete")


class _VRtrLdpIfOperHelloTimeout_Type(TmnxLdpNewHelloTimeout):
    """Custom type vRtrLdpIfOperHelloTimeout based on TmnxLdpNewHelloTimeout"""
    subtypeSpec = TmnxLdpNewHelloTimeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_VRtrLdpIfOperHelloTimeout_Type.__name__ = "TmnxLdpNewHelloTimeout"
_VRtrLdpIfOperHelloTimeout_Object = MibTableColumn
vRtrLdpIfOperHelloTimeout = _VRtrLdpIfOperHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 25),
    _VRtrLdpIfOperHelloTimeout_Type()
)
vRtrLdpIfOperHelloTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpIfOperHelloTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpIfOperHelloTimeout.setUnits("seconds")


class _VRtrLdpIfLinkLsrIfIndex_Type(InterfaceIndexOrZero):
    """Custom type vRtrLdpIfLinkLsrIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_VRtrLdpIfLinkLsrIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_VRtrLdpIfLinkLsrIfIndex_Object = MibTableColumn
vRtrLdpIfLinkLsrIfIndex = _VRtrLdpIfLinkLsrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 26),
    _VRtrLdpIfLinkLsrIfIndex_Type()
)
vRtrLdpIfLinkLsrIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfLinkLsrIfIndex.setStatus("obsolete")


class _VRtrLdpIfCreator_Type(Integer32):
    """Custom type vRtrLdpIfCreator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("template", 2),
          ("sdp", 3))
    )


_VRtrLdpIfCreator_Type.__name__ = "Integer32"
_VRtrLdpIfCreator_Object = MibTableColumn
vRtrLdpIfCreator = _VRtrLdpIfCreator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 27),
    _VRtrLdpIfCreator_Type()
)
vRtrLdpIfCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpIfCreator.setStatus("obsolete")
_VRtrLdpIfTemplName_Type = TNamedItemOrEmpty
_VRtrLdpIfTemplName_Object = MibTableColumn
vRtrLdpIfTemplName = _VRtrLdpIfTemplName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 28),
    _VRtrLdpIfTemplName_Type()
)
vRtrLdpIfTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpIfTemplName.setStatus("obsolete")
_VRtrLdpIfUpTime_Type = TimeInterval
_VRtrLdpIfUpTime_Object = MibTableColumn
vRtrLdpIfUpTime = _VRtrLdpIfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 29),
    _VRtrLdpIfUpTime_Type()
)
vRtrLdpIfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpIfUpTime.setStatus("obsolete")
_VRtrLdpIfStatsTable_Object = MibTable
vRtrLdpIfStatsTable = _VRtrLdpIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 6)
)
if mibBuilder.loadTexts:
    vRtrLdpIfStatsTable.setStatus("obsolete")
_VRtrLdpIfStatsEntry_Object = MibTableRow
vRtrLdpIfStatsEntry = _VRtrLdpIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 6, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpIfStatsEntry.setStatus("obsolete")
_VRtrLdpIfExistingAdjacencies_Type = Gauge32
_VRtrLdpIfExistingAdjacencies_Object = MibTableColumn
vRtrLdpIfExistingAdjacencies = _VRtrLdpIfExistingAdjacencies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 6, 1, 1),
    _VRtrLdpIfExistingAdjacencies_Type()
)
vRtrLdpIfExistingAdjacencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpIfExistingAdjacencies.setStatus("obsolete")
_VRtrLdpHelloAdjTable_Object = MibTable
vRtrLdpHelloAdjTable = _VRtrLdpHelloAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7)
)
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjTable.setStatus("obsolete")
_VRtrLdpHelloAdjEntry_Object = MibTableRow
vRtrLdpHelloAdjEntry = _VRtrLdpHelloAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1)
)
vRtrLdpHelloAdjEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpIfIndex"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerAddress"),
)
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjEntry.setStatus("obsolete")
_VRtrLdpPeerLdpId_Type = MplsLdpIdentifier
_VRtrLdpPeerLdpId_Object = MibTableColumn
vRtrLdpPeerLdpId = _VRtrLdpPeerLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 1),
    _VRtrLdpPeerLdpId_Type()
)
vRtrLdpPeerLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpPeerLdpId.setStatus("obsolete")
_VRtrLdpHelloAdjLocalLdpId_Type = MplsLdpIdentifier
_VRtrLdpHelloAdjLocalLdpId_Object = MibTableColumn
vRtrLdpHelloAdjLocalLdpId = _VRtrLdpHelloAdjLocalLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 2),
    _VRtrLdpHelloAdjLocalLdpId_Type()
)
vRtrLdpHelloAdjLocalLdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjLocalLdpId.setStatus("obsolete")


class _VRtrLdpHelloAdjEntityIndex_Type(Unsigned32):
    """Custom type vRtrLdpHelloAdjEntityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrLdpHelloAdjEntityIndex_Type.__name__ = "Unsigned32"
_VRtrLdpHelloAdjEntityIndex_Object = MibTableColumn
vRtrLdpHelloAdjEntityIndex = _VRtrLdpHelloAdjEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 3),
    _VRtrLdpHelloAdjEntityIndex_Type()
)
vRtrLdpHelloAdjEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjEntityIndex.setStatus("obsolete")


class _VRtrLdpHelloAdjIndex_Type(Unsigned32):
    """Custom type vRtrLdpHelloAdjIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrLdpHelloAdjIndex_Type.__name__ = "Unsigned32"
_VRtrLdpHelloAdjIndex_Object = MibTableColumn
vRtrLdpHelloAdjIndex = _VRtrLdpHelloAdjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 4),
    _VRtrLdpHelloAdjIndex_Type()
)
vRtrLdpHelloAdjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjIndex.setStatus("obsolete")
_VRtrLdpHelloAdjHoldTimeRemaining_Type = Unsigned32
_VRtrLdpHelloAdjHoldTimeRemaining_Object = MibTableColumn
vRtrLdpHelloAdjHoldTimeRemaining = _VRtrLdpHelloAdjHoldTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 5),
    _VRtrLdpHelloAdjHoldTimeRemaining_Type()
)
vRtrLdpHelloAdjHoldTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjHoldTimeRemaining.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjHoldTimeRemaining.setUnits("seconds")
_VRtrLdpHelloAdjType_Type = TmnxLdpAdjacencyType
_VRtrLdpHelloAdjType_Object = MibTableColumn
vRtrLdpHelloAdjType = _VRtrLdpHelloAdjType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 6),
    _VRtrLdpHelloAdjType_Type()
)
vRtrLdpHelloAdjType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjType.setStatus("obsolete")
_VRtrLdpHelloAdjRemoteConfSeqNum_Type = Unsigned32
_VRtrLdpHelloAdjRemoteConfSeqNum_Object = MibTableColumn
vRtrLdpHelloAdjRemoteConfSeqNum = _VRtrLdpHelloAdjRemoteConfSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 7),
    _VRtrLdpHelloAdjRemoteConfSeqNum_Type()
)
vRtrLdpHelloAdjRemoteConfSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjRemoteConfSeqNum.setStatus("obsolete")
_VRtrLdpHelloAdjRemoteIpAddress_Type = IpAddress
_VRtrLdpHelloAdjRemoteIpAddress_Object = MibTableColumn
vRtrLdpHelloAdjRemoteIpAddress = _VRtrLdpHelloAdjRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 8),
    _VRtrLdpHelloAdjRemoteIpAddress_Type()
)
vRtrLdpHelloAdjRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjRemoteIpAddress.setStatus("obsolete")
_VRtrLdpHelloAdjUpTime_Type = TimeInterval
_VRtrLdpHelloAdjUpTime_Object = MibTableColumn
vRtrLdpHelloAdjUpTime = _VRtrLdpHelloAdjUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 9),
    _VRtrLdpHelloAdjUpTime_Type()
)
vRtrLdpHelloAdjUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjUpTime.setStatus("obsolete")
_VRtrLdpHelloAdjLocalConfSeqNum_Type = Unsigned32
_VRtrLdpHelloAdjLocalConfSeqNum_Object = MibTableColumn
vRtrLdpHelloAdjLocalConfSeqNum = _VRtrLdpHelloAdjLocalConfSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 10),
    _VRtrLdpHelloAdjLocalConfSeqNum_Type()
)
vRtrLdpHelloAdjLocalConfSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjLocalConfSeqNum.setStatus("obsolete")
_VRtrLdpHelloAdjLocalIpAddress_Type = IpAddress
_VRtrLdpHelloAdjLocalIpAddress_Object = MibTableColumn
vRtrLdpHelloAdjLocalIpAddress = _VRtrLdpHelloAdjLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 11),
    _VRtrLdpHelloAdjLocalIpAddress_Type()
)
vRtrLdpHelloAdjLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjLocalIpAddress.setStatus("obsolete")
_VRtrLdpHelloAdjInHelloMsgCount_Type = Counter32
_VRtrLdpHelloAdjInHelloMsgCount_Object = MibTableColumn
vRtrLdpHelloAdjInHelloMsgCount = _VRtrLdpHelloAdjInHelloMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 12),
    _VRtrLdpHelloAdjInHelloMsgCount_Type()
)
vRtrLdpHelloAdjInHelloMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjInHelloMsgCount.setStatus("obsolete")
_VRtrLdpHelloAdjOutHelloMsgCount_Type = Counter32
_VRtrLdpHelloAdjOutHelloMsgCount_Object = MibTableColumn
vRtrLdpHelloAdjOutHelloMsgCount = _VRtrLdpHelloAdjOutHelloMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 13),
    _VRtrLdpHelloAdjOutHelloMsgCount_Type()
)
vRtrLdpHelloAdjOutHelloMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjOutHelloMsgCount.setStatus("obsolete")
_VRtrLdpHelloAdjLocalHelloTimeout_Type = TmnxLdpHelloTimeout
_VRtrLdpHelloAdjLocalHelloTimeout_Object = MibTableColumn
vRtrLdpHelloAdjLocalHelloTimeout = _VRtrLdpHelloAdjLocalHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 14),
    _VRtrLdpHelloAdjLocalHelloTimeout_Type()
)
vRtrLdpHelloAdjLocalHelloTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjLocalHelloTimeout.setStatus("obsolete")
_VRtrLdpHelloAdjRemoteHelloTimeout_Type = TmnxLdpHelloTimeout
_VRtrLdpHelloAdjRemoteHelloTimeout_Object = MibTableColumn
vRtrLdpHelloAdjRemoteHelloTimeout = _VRtrLdpHelloAdjRemoteHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 15),
    _VRtrLdpHelloAdjRemoteHelloTimeout_Type()
)
vRtrLdpHelloAdjRemoteHelloTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjRemoteHelloTimeout.setStatus("obsolete")


class _VRtrLdpHelloAdjBfdStatus_Type(Integer32):
    """Custom type vRtrLdpHelloAdjBfdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noService", 1),
          ("inService", 2),
          ("outOfService", 3))
    )


_VRtrLdpHelloAdjBfdStatus_Type.__name__ = "Integer32"
_VRtrLdpHelloAdjBfdStatus_Object = MibTableColumn
vRtrLdpHelloAdjBfdStatus = _VRtrLdpHelloAdjBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 16),
    _VRtrLdpHelloAdjBfdStatus_Type()
)
vRtrLdpHelloAdjBfdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjBfdStatus.setStatus("obsolete")
_VRtrLdpHelloAdjMapTable_Object = MibTable
vRtrLdpHelloAdjMapTable = _VRtrLdpHelloAdjMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 8)
)
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjMapTable.setStatus("obsolete")
_VRtrLdpHelloAdjMapEntry_Object = MibTableRow
vRtrLdpHelloAdjMapEntry = _VRtrLdpHelloAdjMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 8, 1)
)
vRtrLdpHelloAdjMapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpIfIndex"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerAddress"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpHelloAdjMapLdpId"),
)
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjMapEntry.setStatus("obsolete")
_VRtrLdpHelloAdjMapLdpId_Type = MplsLdpIdentifier
_VRtrLdpHelloAdjMapLdpId_Object = MibTableColumn
vRtrLdpHelloAdjMapLdpId = _VRtrLdpHelloAdjMapLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 8, 1, 1),
    _VRtrLdpHelloAdjMapLdpId_Type()
)
vRtrLdpHelloAdjMapLdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjMapLdpId.setStatus("obsolete")
_VRtrLdpSessionTable_Object = MibTable
vRtrLdpSessionTable = _VRtrLdpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9)
)
if mibBuilder.loadTexts:
    vRtrLdpSessionTable.setStatus("obsolete")
_VRtrLdpSessionEntry_Object = MibTableRow
vRtrLdpSessionEntry = _VRtrLdpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1)
)
vRtrLdpSessionEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    vRtrLdpSessionEntry.setStatus("obsolete")
_VRtrLdpSessLocalLdpId_Type = MplsLdpIdentifier
_VRtrLdpSessLocalLdpId_Object = MibTableColumn
vRtrLdpSessLocalLdpId = _VRtrLdpSessLocalLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 1),
    _VRtrLdpSessLocalLdpId_Type()
)
vRtrLdpSessLocalLdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessLocalLdpId.setStatus("obsolete")


class _VRtrLdpSessEntityIndex_Type(Unsigned32):
    """Custom type vRtrLdpSessEntityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrLdpSessEntityIndex_Type.__name__ = "Unsigned32"
_VRtrLdpSessEntityIndex_Object = MibTableColumn
vRtrLdpSessEntityIndex = _VRtrLdpSessEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 2),
    _VRtrLdpSessEntityIndex_Type()
)
vRtrLdpSessEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessEntityIndex.setStatus("obsolete")
_VRtrLdpSessLabelDistMethod_Type = TmnxLdpLabelDistMethod
_VRtrLdpSessLabelDistMethod_Object = MibTableColumn
vRtrLdpSessLabelDistMethod = _VRtrLdpSessLabelDistMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 3),
    _VRtrLdpSessLabelDistMethod_Type()
)
vRtrLdpSessLabelDistMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessLabelDistMethod.setStatus("obsolete")


class _VRtrLdpSessLoopDetectForPV_Type(Integer32):
    """Custom type vRtrLdpSessLoopDetectForPV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VRtrLdpSessLoopDetectForPV_Type.__name__ = "Integer32"
_VRtrLdpSessLoopDetectForPV_Object = MibTableColumn
vRtrLdpSessLoopDetectForPV = _VRtrLdpSessLoopDetectForPV_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 4),
    _VRtrLdpSessLoopDetectForPV_Type()
)
vRtrLdpSessLoopDetectForPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessLoopDetectForPV.setStatus("obsolete")


class _VRtrLdpSessPathVectorLimit_Type(Unsigned32):
    """Custom type vRtrLdpSessPathVectorLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrLdpSessPathVectorLimit_Type.__name__ = "Unsigned32"
_VRtrLdpSessPathVectorLimit_Object = MibTableColumn
vRtrLdpSessPathVectorLimit = _VRtrLdpSessPathVectorLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 5),
    _VRtrLdpSessPathVectorLimit_Type()
)
vRtrLdpSessPathVectorLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessPathVectorLimit.setStatus("obsolete")


class _VRtrLdpSessState_Type(Integer32):
    """Custom type vRtrLdpSessState based on Integer32"""
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
        *(("nonexistent", 1),
          ("initialized", 2),
          ("openrec", 3),
          ("opensent", 4),
          ("operational", 5))
    )


_VRtrLdpSessState_Type.__name__ = "Integer32"
_VRtrLdpSessState_Object = MibTableColumn
vRtrLdpSessState = _VRtrLdpSessState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 6),
    _VRtrLdpSessState_Type()
)
vRtrLdpSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessState.setStatus("obsolete")
_VRtrLdpSessAdjacencyType_Type = TmnxLdpAdjacencyType
_VRtrLdpSessAdjacencyType_Object = MibTableColumn
vRtrLdpSessAdjacencyType = _VRtrLdpSessAdjacencyType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 7),
    _VRtrLdpSessAdjacencyType_Type()
)
vRtrLdpSessAdjacencyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessAdjacencyType.setStatus("obsolete")
_VRtrLdpSessProtocolVersion_Type = Unsigned32
_VRtrLdpSessProtocolVersion_Object = MibTableColumn
vRtrLdpSessProtocolVersion = _VRtrLdpSessProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 8),
    _VRtrLdpSessProtocolVersion_Type()
)
vRtrLdpSessProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessProtocolVersion.setStatus("obsolete")


class _VRtrLdpSessLocalUdpPort_Type(Unsigned32):
    """Custom type vRtrLdpSessLocalUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrLdpSessLocalUdpPort_Type.__name__ = "Unsigned32"
_VRtrLdpSessLocalUdpPort_Object = MibTableColumn
vRtrLdpSessLocalUdpPort = _VRtrLdpSessLocalUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 9),
    _VRtrLdpSessLocalUdpPort_Type()
)
vRtrLdpSessLocalUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessLocalUdpPort.setStatus("obsolete")


class _VRtrLdpSessPeerUdpPort_Type(Unsigned32):
    """Custom type vRtrLdpSessPeerUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrLdpSessPeerUdpPort_Type.__name__ = "Unsigned32"
_VRtrLdpSessPeerUdpPort_Object = MibTableColumn
vRtrLdpSessPeerUdpPort = _VRtrLdpSessPeerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 10),
    _VRtrLdpSessPeerUdpPort_Type()
)
vRtrLdpSessPeerUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessPeerUdpPort.setStatus("obsolete")


class _VRtrLdpSessLocalTcpPort_Type(Unsigned32):
    """Custom type vRtrLdpSessLocalTcpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrLdpSessLocalTcpPort_Type.__name__ = "Unsigned32"
_VRtrLdpSessLocalTcpPort_Object = MibTableColumn
vRtrLdpSessLocalTcpPort = _VRtrLdpSessLocalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 11),
    _VRtrLdpSessLocalTcpPort_Type()
)
vRtrLdpSessLocalTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessLocalTcpPort.setStatus("obsolete")


class _VRtrLdpSessPeerTcpPort_Type(Unsigned32):
    """Custom type vRtrLdpSessPeerTcpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrLdpSessPeerTcpPort_Type.__name__ = "Unsigned32"
_VRtrLdpSessPeerTcpPort_Object = MibTableColumn
vRtrLdpSessPeerTcpPort = _VRtrLdpSessPeerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 12),
    _VRtrLdpSessPeerTcpPort_Type()
)
vRtrLdpSessPeerTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessPeerTcpPort.setStatus("obsolete")
_VRtrLdpSessLocalAddress_Type = IpAddress
_VRtrLdpSessLocalAddress_Object = MibTableColumn
vRtrLdpSessLocalAddress = _VRtrLdpSessLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 13),
    _VRtrLdpSessLocalAddress_Type()
)
vRtrLdpSessLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessLocalAddress.setStatus("obsolete")
_VRtrLdpSessPeerAddress_Type = IpAddress
_VRtrLdpSessPeerAddress_Object = MibTableColumn
vRtrLdpSessPeerAddress = _VRtrLdpSessPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 14),
    _VRtrLdpSessPeerAddress_Type()
)
vRtrLdpSessPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessPeerAddress.setStatus("obsolete")
_VRtrLdpSessKAHoldTimeRemaining_Type = TimeInterval
_VRtrLdpSessKAHoldTimeRemaining_Object = MibTableColumn
vRtrLdpSessKAHoldTimeRemaining = _VRtrLdpSessKAHoldTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 15),
    _VRtrLdpSessKAHoldTimeRemaining_Type()
)
vRtrLdpSessKAHoldTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessKAHoldTimeRemaining.setStatus("obsolete")


class _VRtrLdpSessMaxPduLength_Type(Unsigned32):
    """Custom type vRtrLdpSessMaxPduLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrLdpSessMaxPduLength_Type.__name__ = "Unsigned32"
_VRtrLdpSessMaxPduLength_Object = MibTableColumn
vRtrLdpSessMaxPduLength = _VRtrLdpSessMaxPduLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 16),
    _VRtrLdpSessMaxPduLength_Type()
)
vRtrLdpSessMaxPduLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessMaxPduLength.setStatus("obsolete")
_VRtrLdpSessUpTime_Type = TimeInterval
_VRtrLdpSessUpTime_Object = MibTableColumn
vRtrLdpSessUpTime = _VRtrLdpSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 17),
    _VRtrLdpSessUpTime_Type()
)
vRtrLdpSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessUpTime.setStatus("obsolete")
_VRtrLdpSessLocalKATimeout_Type = TmnxLdpKeepAliveTimeout
_VRtrLdpSessLocalKATimeout_Object = MibTableColumn
vRtrLdpSessLocalKATimeout = _VRtrLdpSessLocalKATimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 18),
    _VRtrLdpSessLocalKATimeout_Type()
)
vRtrLdpSessLocalKATimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessLocalKATimeout.setStatus("obsolete")
_VRtrLdpSessPeerKATimeout_Type = TmnxLdpKeepAliveTimeout
_VRtrLdpSessPeerKATimeout_Object = MibTableColumn
vRtrLdpSessPeerKATimeout = _VRtrLdpSessPeerKATimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 19),
    _VRtrLdpSessPeerKATimeout_Type()
)
vRtrLdpSessPeerKATimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessPeerKATimeout.setStatus("obsolete")


class _VRtrLdpSessAdvertise_Type(Integer32):
    """Custom type vRtrLdpSessAdvertise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("address", 1),
          ("service", 2),
          ("addressAndService", 3))
    )


_VRtrLdpSessAdvertise_Type.__name__ = "Integer32"
_VRtrLdpSessAdvertise_Object = MibTableColumn
vRtrLdpSessAdvertise = _VRtrLdpSessAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 20),
    _VRtrLdpSessAdvertise_Type()
)
vRtrLdpSessAdvertise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessAdvertise.setStatus("obsolete")
_VRtrLdpSessRestartHelperState_Type = TruthValue
_VRtrLdpSessRestartHelperState_Object = MibTableColumn
vRtrLdpSessRestartHelperState = _VRtrLdpSessRestartHelperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 21),
    _VRtrLdpSessRestartHelperState_Type()
)
vRtrLdpSessRestartHelperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessRestartHelperState.setStatus("obsolete")
_VRtrLdpSessPeerNumRestart_Type = Counter32
_VRtrLdpSessPeerNumRestart_Object = MibTableColumn
vRtrLdpSessPeerNumRestart = _VRtrLdpSessPeerNumRestart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 22),
    _VRtrLdpSessPeerNumRestart_Type()
)
vRtrLdpSessPeerNumRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessPeerNumRestart.setStatus("obsolete")
_VRtrLdpSessLastRestartTime_Type = TimeStamp
_VRtrLdpSessLastRestartTime_Object = MibTableColumn
vRtrLdpSessLastRestartTime = _VRtrLdpSessLastRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 23),
    _VRtrLdpSessLastRestartTime_Type()
)
vRtrLdpSessLastRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessLastRestartTime.setStatus("obsolete")
_VRtrLdpSessFtReconnectTimeNego_Type = Unsigned32
_VRtrLdpSessFtReconnectTimeNego_Object = MibTableColumn
vRtrLdpSessFtReconnectTimeNego = _VRtrLdpSessFtReconnectTimeNego_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 24),
    _VRtrLdpSessFtReconnectTimeNego_Type()
)
vRtrLdpSessFtReconnectTimeNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessFtReconnectTimeNego.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpSessFtReconnectTimeNego.setUnits("seconds")
_VRtrLdpSessFtRecoveryTimeNego_Type = Unsigned32
_VRtrLdpSessFtRecoveryTimeNego_Object = MibTableColumn
vRtrLdpSessFtRecoveryTimeNego = _VRtrLdpSessFtRecoveryTimeNego_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 25),
    _VRtrLdpSessFtRecoveryTimeNego_Type()
)
vRtrLdpSessFtRecoveryTimeNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessFtRecoveryTimeNego.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpSessFtRecoveryTimeNego.setUnits("seconds")
_VRtrLdpSessFtReconTimeRemaining_Type = Unsigned32
_VRtrLdpSessFtReconTimeRemaining_Object = MibTableColumn
vRtrLdpSessFtReconTimeRemaining = _VRtrLdpSessFtReconTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 26),
    _VRtrLdpSessFtReconTimeRemaining_Type()
)
vRtrLdpSessFtReconTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessFtReconTimeRemaining.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpSessFtReconTimeRemaining.setUnits("seconds")
_VRtrLdpSessFtRecovTimeRemaining_Type = Unsigned32
_VRtrLdpSessFtRecovTimeRemaining_Object = MibTableColumn
vRtrLdpSessFtRecovTimeRemaining = _VRtrLdpSessFtRecovTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 27),
    _VRtrLdpSessFtRecovTimeRemaining_Type()
)
vRtrLdpSessFtRecovTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessFtRecovTimeRemaining.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpSessFtRecovTimeRemaining.setUnits("seconds")


class _VRtrLdpSessBfdStatus_Type(Integer32):
    """Custom type vRtrLdpSessBfdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noService", 1),
          ("inService", 2),
          ("outOfService", 3))
    )


_VRtrLdpSessBfdStatus_Type.__name__ = "Integer32"
_VRtrLdpSessBfdStatus_Object = MibTableColumn
vRtrLdpSessBfdStatus = _VRtrLdpSessBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 28),
    _VRtrLdpSessBfdStatus_Type()
)
vRtrLdpSessBfdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessBfdStatus.setStatus("obsolete")
_VRtrLdpSessP2MPCapabilityNego_Type = TruthValue
_VRtrLdpSessP2MPCapabilityNego_Object = MibTableColumn
vRtrLdpSessP2MPCapabilityNego = _VRtrLdpSessP2MPCapabilityNego_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 29),
    _VRtrLdpSessP2MPCapabilityNego_Type()
)
vRtrLdpSessP2MPCapabilityNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessP2MPCapabilityNego.setStatus("obsolete")
_VRtrLdpSessMPMBBCapabilityNego_Type = TruthValue
_VRtrLdpSessMPMBBCapabilityNego_Object = MibTableColumn
vRtrLdpSessMPMBBCapabilityNego = _VRtrLdpSessMPMBBCapabilityNego_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 30),
    _VRtrLdpSessMPMBBCapabilityNego_Type()
)
vRtrLdpSessMPMBBCapabilityNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessMPMBBCapabilityNego.setStatus("obsolete")
_VRtrLdpSessDynamicCapabilityNego_Type = TruthValue
_VRtrLdpSessDynamicCapabilityNego_Object = MibTableColumn
vRtrLdpSessDynamicCapabilityNego = _VRtrLdpSessDynamicCapabilityNego_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 31),
    _VRtrLdpSessDynamicCapabilityNego_Type()
)
vRtrLdpSessDynamicCapabilityNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessDynamicCapabilityNego.setStatus("obsolete")
_VRtrLdpSessOvrloadCapabltyNego_Type = TruthValue
_VRtrLdpSessOvrloadCapabltyNego_Object = MibTableColumn
vRtrLdpSessOvrloadCapabltyNego = _VRtrLdpSessOvrloadCapabltyNego_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 32),
    _VRtrLdpSessOvrloadCapabltyNego_Type()
)
vRtrLdpSessOvrloadCapabltyNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessOvrloadCapabltyNego.setStatus("obsolete")
_VRtrLdpSessAddrFecOverloadSent_Type = TruthValue
_VRtrLdpSessAddrFecOverloadSent_Object = MibTableColumn
vRtrLdpSessAddrFecOverloadSent = _VRtrLdpSessAddrFecOverloadSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 33),
    _VRtrLdpSessAddrFecOverloadSent_Type()
)
vRtrLdpSessAddrFecOverloadSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessAddrFecOverloadSent.setStatus("obsolete")
_VRtrLdpSessAddrFecOverloadRecv_Type = TruthValue
_VRtrLdpSessAddrFecOverloadRecv_Object = MibTableColumn
vRtrLdpSessAddrFecOverloadRecv = _VRtrLdpSessAddrFecOverloadRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 34),
    _VRtrLdpSessAddrFecOverloadRecv_Type()
)
vRtrLdpSessAddrFecOverloadRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessAddrFecOverloadRecv.setStatus("obsolete")
_VRtrLdpSessMcastFecOverloadSent_Type = TruthValue
_VRtrLdpSessMcastFecOverloadSent_Object = MibTableColumn
vRtrLdpSessMcastFecOverloadSent = _VRtrLdpSessMcastFecOverloadSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 35),
    _VRtrLdpSessMcastFecOverloadSent_Type()
)
vRtrLdpSessMcastFecOverloadSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessMcastFecOverloadSent.setStatus("obsolete")
_VRtrLdpSessMcastFecOverloadRecv_Type = TruthValue
_VRtrLdpSessMcastFecOverloadRecv_Object = MibTableColumn
vRtrLdpSessMcastFecOverloadRecv = _VRtrLdpSessMcastFecOverloadRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 36),
    _VRtrLdpSessMcastFecOverloadRecv_Type()
)
vRtrLdpSessMcastFecOverloadRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessMcastFecOverloadRecv.setStatus("obsolete")
_VRtrLdpSessServFecOverloadSent_Type = TruthValue
_VRtrLdpSessServFecOverloadSent_Object = MibTableColumn
vRtrLdpSessServFecOverloadSent = _VRtrLdpSessServFecOverloadSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 37),
    _VRtrLdpSessServFecOverloadSent_Type()
)
vRtrLdpSessServFecOverloadSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessServFecOverloadSent.setStatus("obsolete")
_VRtrLdpSessServFecOverloadRecv_Type = TruthValue
_VRtrLdpSessServFecOverloadRecv_Object = MibTableColumn
vRtrLdpSessServFecOverloadRecv = _VRtrLdpSessServFecOverloadRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 38),
    _VRtrLdpSessServFecOverloadRecv_Type()
)
vRtrLdpSessServFecOverloadRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessServFecOverloadRecv.setStatus("obsolete")
_VRtrLdpSessOperMaxFecThreshold_Type = Unsigned32
_VRtrLdpSessOperMaxFecThreshold_Object = MibTableColumn
vRtrLdpSessOperMaxFecThreshold = _VRtrLdpSessOperMaxFecThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 39),
    _VRtrLdpSessOperMaxFecThreshold_Type()
)
vRtrLdpSessOperMaxFecThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessOperMaxFecThreshold.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpSessOperMaxFecThreshold.setUnits("percent")
_VRtrLdpSessionStatsTable_Object = MibTable
vRtrLdpSessionStatsTable = _VRtrLdpSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10)
)
if mibBuilder.loadTexts:
    vRtrLdpSessionStatsTable.setStatus("obsolete")
_VRtrLdpSessionStatsEntry_Object = MibTableRow
vRtrLdpSessionStatsEntry = _VRtrLdpSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpSessionStatsEntry.setStatus("obsolete")
_VRtrLdpSessStatsTargAdj_Type = Gauge32
_VRtrLdpSessStatsTargAdj_Object = MibTableColumn
vRtrLdpSessStatsTargAdj = _VRtrLdpSessStatsTargAdj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 1),
    _VRtrLdpSessStatsTargAdj_Type()
)
vRtrLdpSessStatsTargAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsTargAdj.setStatus("obsolete")
_VRtrLdpSessStatsLinkAdj_Type = Gauge32
_VRtrLdpSessStatsLinkAdj_Object = MibTableColumn
vRtrLdpSessStatsLinkAdj = _VRtrLdpSessStatsLinkAdj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 2),
    _VRtrLdpSessStatsLinkAdj_Type()
)
vRtrLdpSessStatsLinkAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLinkAdj.setStatus("obsolete")
_VRtrLdpSessStatsFECRecv_Type = Counter32
_VRtrLdpSessStatsFECRecv_Object = MibTableColumn
vRtrLdpSessStatsFECRecv = _VRtrLdpSessStatsFECRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 3),
    _VRtrLdpSessStatsFECRecv_Type()
)
vRtrLdpSessStatsFECRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsFECRecv.setStatus("obsolete")
_VRtrLdpSessStatsFECSent_Type = Counter32
_VRtrLdpSessStatsFECSent_Object = MibTableColumn
vRtrLdpSessStatsFECSent = _VRtrLdpSessStatsFECSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 4),
    _VRtrLdpSessStatsFECSent_Type()
)
vRtrLdpSessStatsFECSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsFECSent.setStatus("obsolete")
_VRtrLdpSessStatsHelloIn_Type = Counter32
_VRtrLdpSessStatsHelloIn_Object = MibTableColumn
vRtrLdpSessStatsHelloIn = _VRtrLdpSessStatsHelloIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 5),
    _VRtrLdpSessStatsHelloIn_Type()
)
vRtrLdpSessStatsHelloIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsHelloIn.setStatus("obsolete")
_VRtrLdpSessStatsHelloOut_Type = Counter32
_VRtrLdpSessStatsHelloOut_Object = MibTableColumn
vRtrLdpSessStatsHelloOut = _VRtrLdpSessStatsHelloOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 6),
    _VRtrLdpSessStatsHelloOut_Type()
)
vRtrLdpSessStatsHelloOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsHelloOut.setStatus("obsolete")
_VRtrLdpSessStatsKeepaliveIn_Type = Counter32
_VRtrLdpSessStatsKeepaliveIn_Object = MibTableColumn
vRtrLdpSessStatsKeepaliveIn = _VRtrLdpSessStatsKeepaliveIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 7),
    _VRtrLdpSessStatsKeepaliveIn_Type()
)
vRtrLdpSessStatsKeepaliveIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsKeepaliveIn.setStatus("obsolete")
_VRtrLdpSessStatsKeepaliveOut_Type = Counter32
_VRtrLdpSessStatsKeepaliveOut_Object = MibTableColumn
vRtrLdpSessStatsKeepaliveOut = _VRtrLdpSessStatsKeepaliveOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 8),
    _VRtrLdpSessStatsKeepaliveOut_Type()
)
vRtrLdpSessStatsKeepaliveOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsKeepaliveOut.setStatus("obsolete")
_VRtrLdpSessStatsInitIn_Type = Counter32
_VRtrLdpSessStatsInitIn_Object = MibTableColumn
vRtrLdpSessStatsInitIn = _VRtrLdpSessStatsInitIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 9),
    _VRtrLdpSessStatsInitIn_Type()
)
vRtrLdpSessStatsInitIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsInitIn.setStatus("obsolete")
_VRtrLdpSessStatsInitOut_Type = Counter32
_VRtrLdpSessStatsInitOut_Object = MibTableColumn
vRtrLdpSessStatsInitOut = _VRtrLdpSessStatsInitOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 10),
    _VRtrLdpSessStatsInitOut_Type()
)
vRtrLdpSessStatsInitOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsInitOut.setStatus("obsolete")
_VRtrLdpSessStatsLabelMappingIn_Type = Counter32
_VRtrLdpSessStatsLabelMappingIn_Object = MibTableColumn
vRtrLdpSessStatsLabelMappingIn = _VRtrLdpSessStatsLabelMappingIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 11),
    _VRtrLdpSessStatsLabelMappingIn_Type()
)
vRtrLdpSessStatsLabelMappingIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelMappingIn.setStatus("obsolete")
_VRtrLdpSessStatsLabelMappingOut_Type = Counter32
_VRtrLdpSessStatsLabelMappingOut_Object = MibTableColumn
vRtrLdpSessStatsLabelMappingOut = _VRtrLdpSessStatsLabelMappingOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 12),
    _VRtrLdpSessStatsLabelMappingOut_Type()
)
vRtrLdpSessStatsLabelMappingOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelMappingOut.setStatus("obsolete")
_VRtrLdpSessStatsLabelRequestIn_Type = Counter32
_VRtrLdpSessStatsLabelRequestIn_Object = MibTableColumn
vRtrLdpSessStatsLabelRequestIn = _VRtrLdpSessStatsLabelRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 13),
    _VRtrLdpSessStatsLabelRequestIn_Type()
)
vRtrLdpSessStatsLabelRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelRequestIn.setStatus("obsolete")
_VRtrLdpSessStatsLabelRequestOut_Type = Counter32
_VRtrLdpSessStatsLabelRequestOut_Object = MibTableColumn
vRtrLdpSessStatsLabelRequestOut = _VRtrLdpSessStatsLabelRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 14),
    _VRtrLdpSessStatsLabelRequestOut_Type()
)
vRtrLdpSessStatsLabelRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelRequestOut.setStatus("obsolete")
_VRtrLdpSessStatsLabelReleaseIn_Type = Counter32
_VRtrLdpSessStatsLabelReleaseIn_Object = MibTableColumn
vRtrLdpSessStatsLabelReleaseIn = _VRtrLdpSessStatsLabelReleaseIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 15),
    _VRtrLdpSessStatsLabelReleaseIn_Type()
)
vRtrLdpSessStatsLabelReleaseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelReleaseIn.setStatus("obsolete")
_VRtrLdpSessStatsLabelReleaseOut_Type = Counter32
_VRtrLdpSessStatsLabelReleaseOut_Object = MibTableColumn
vRtrLdpSessStatsLabelReleaseOut = _VRtrLdpSessStatsLabelReleaseOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 16),
    _VRtrLdpSessStatsLabelReleaseOut_Type()
)
vRtrLdpSessStatsLabelReleaseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelReleaseOut.setStatus("obsolete")
_VRtrLdpSessStatsLabelWithdrawIn_Type = Counter32
_VRtrLdpSessStatsLabelWithdrawIn_Object = MibTableColumn
vRtrLdpSessStatsLabelWithdrawIn = _VRtrLdpSessStatsLabelWithdrawIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 17),
    _VRtrLdpSessStatsLabelWithdrawIn_Type()
)
vRtrLdpSessStatsLabelWithdrawIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelWithdrawIn.setStatus("obsolete")
_VRtrLdpSessStatsLabelWithdrawOut_Type = Counter32
_VRtrLdpSessStatsLabelWithdrawOut_Object = MibTableColumn
vRtrLdpSessStatsLabelWithdrawOut = _VRtrLdpSessStatsLabelWithdrawOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 18),
    _VRtrLdpSessStatsLabelWithdrawOut_Type()
)
vRtrLdpSessStatsLabelWithdrawOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelWithdrawOut.setStatus("obsolete")
_VRtrLdpSessStatsLabelAbortIn_Type = Counter32
_VRtrLdpSessStatsLabelAbortIn_Object = MibTableColumn
vRtrLdpSessStatsLabelAbortIn = _VRtrLdpSessStatsLabelAbortIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 19),
    _VRtrLdpSessStatsLabelAbortIn_Type()
)
vRtrLdpSessStatsLabelAbortIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelAbortIn.setStatus("obsolete")
_VRtrLdpSessStatsLabelAbortOut_Type = Counter32
_VRtrLdpSessStatsLabelAbortOut_Object = MibTableColumn
vRtrLdpSessStatsLabelAbortOut = _VRtrLdpSessStatsLabelAbortOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 20),
    _VRtrLdpSessStatsLabelAbortOut_Type()
)
vRtrLdpSessStatsLabelAbortOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelAbortOut.setStatus("obsolete")
_VRtrLdpSessStatsAddrIn_Type = Counter32
_VRtrLdpSessStatsAddrIn_Object = MibTableColumn
vRtrLdpSessStatsAddrIn = _VRtrLdpSessStatsAddrIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 21),
    _VRtrLdpSessStatsAddrIn_Type()
)
vRtrLdpSessStatsAddrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsAddrIn.setStatus("obsolete")
_VRtrLdpSessStatsAddrOut_Type = Counter32
_VRtrLdpSessStatsAddrOut_Object = MibTableColumn
vRtrLdpSessStatsAddrOut = _VRtrLdpSessStatsAddrOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 22),
    _VRtrLdpSessStatsAddrOut_Type()
)
vRtrLdpSessStatsAddrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsAddrOut.setStatus("obsolete")
_VRtrLdpSessStatsAddrWithdrawIn_Type = Counter32
_VRtrLdpSessStatsAddrWithdrawIn_Object = MibTableColumn
vRtrLdpSessStatsAddrWithdrawIn = _VRtrLdpSessStatsAddrWithdrawIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 23),
    _VRtrLdpSessStatsAddrWithdrawIn_Type()
)
vRtrLdpSessStatsAddrWithdrawIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsAddrWithdrawIn.setStatus("obsolete")
_VRtrLdpSessStatsAddrWithdrawOut_Type = Counter32
_VRtrLdpSessStatsAddrWithdrawOut_Object = MibTableColumn
vRtrLdpSessStatsAddrWithdrawOut = _VRtrLdpSessStatsAddrWithdrawOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 24),
    _VRtrLdpSessStatsAddrWithdrawOut_Type()
)
vRtrLdpSessStatsAddrWithdrawOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsAddrWithdrawOut.setStatus("obsolete")
_VRtrLdpSessStatsNotificationIn_Type = Counter32
_VRtrLdpSessStatsNotificationIn_Object = MibTableColumn
vRtrLdpSessStatsNotificationIn = _VRtrLdpSessStatsNotificationIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 25),
    _VRtrLdpSessStatsNotificationIn_Type()
)
vRtrLdpSessStatsNotificationIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsNotificationIn.setStatus("obsolete")
_VRtrLdpSessStatsNotificationOut_Type = Counter32
_VRtrLdpSessStatsNotificationOut_Object = MibTableColumn
vRtrLdpSessStatsNotificationOut = _VRtrLdpSessStatsNotificationOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 26),
    _VRtrLdpSessStatsNotificationOut_Type()
)
vRtrLdpSessStatsNotificationOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsNotificationOut.setStatus("obsolete")
_VRtrLdpSessStatsAddrRecv_Type = Counter32
_VRtrLdpSessStatsAddrRecv_Object = MibTableColumn
vRtrLdpSessStatsAddrRecv = _VRtrLdpSessStatsAddrRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 27),
    _VRtrLdpSessStatsAddrRecv_Type()
)
vRtrLdpSessStatsAddrRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsAddrRecv.setStatus("obsolete")
_VRtrLdpSessStatsAddrSent_Type = Counter32
_VRtrLdpSessStatsAddrSent_Object = MibTableColumn
vRtrLdpSessStatsAddrSent = _VRtrLdpSessStatsAddrSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 28),
    _VRtrLdpSessStatsAddrSent_Type()
)
vRtrLdpSessStatsAddrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsAddrSent.setStatus("obsolete")
_VRtrLdpServFecTable_Object = MibTable
vRtrLdpServFecTable = _VRtrLdpServFecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11)
)
if mibBuilder.loadTexts:
    vRtrLdpServFecTable.setStatus("obsolete")
_VRtrLdpServFecEntry_Object = MibTableRow
vRtrLdpServFecEntry = _VRtrLdpServFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1)
)
vRtrLdpServFecEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpServFecFecType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpServFecVcType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpServFecVcId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    vRtrLdpServFecEntry.setStatus("obsolete")
_VRtrLdpServFecFecType_Type = TmnxLdpFECType
_VRtrLdpServFecFecType_Object = MibTableColumn
vRtrLdpServFecFecType = _VRtrLdpServFecFecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 1),
    _VRtrLdpServFecFecType_Type()
)
vRtrLdpServFecFecType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpServFecFecType.setStatus("obsolete")
_VRtrLdpServFecVcType_Type = TmnxVcType
_VRtrLdpServFecVcType_Object = MibTableColumn
vRtrLdpServFecVcType = _VRtrLdpServFecVcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 2),
    _VRtrLdpServFecVcType_Type()
)
vRtrLdpServFecVcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpServFecVcType.setStatus("obsolete")
_VRtrLdpServFecVcId_Type = TmnxVcId
_VRtrLdpServFecVcId_Object = MibTableColumn
vRtrLdpServFecVcId = _VRtrLdpServFecVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 3),
    _VRtrLdpServFecVcId_Type()
)
vRtrLdpServFecVcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpServFecVcId.setStatus("obsolete")
_VRtrLdpServFecServType_Type = ServType
_VRtrLdpServFecServType_Object = MibTableColumn
vRtrLdpServFecServType = _VRtrLdpServFecServType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 4),
    _VRtrLdpServFecServType_Type()
)
vRtrLdpServFecServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecServType.setStatus("obsolete")


class _VRtrLdpServFecServId_Type(TmnxServId):
    """Custom type vRtrLdpServFecServId based on TmnxServId"""
    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrLdpServFecServId_Type.__name__ = "TmnxServId"
_VRtrLdpServFecServId_Object = MibTableColumn
vRtrLdpServFecServId = _VRtrLdpServFecServId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 5),
    _VRtrLdpServFecServId_Type()
)
vRtrLdpServFecServId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecServId.setStatus("obsolete")
_VRtrLdpServFecVpnId_Type = TmnxVpnId
_VRtrLdpServFecVpnId_Object = MibTableColumn
vRtrLdpServFecVpnId = _VRtrLdpServFecVpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 6),
    _VRtrLdpServFecVpnId_Type()
)
vRtrLdpServFecVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecVpnId.setStatus("obsolete")
_VRtrLdpServFecFlags_Type = TmnxLdpFECFlags
_VRtrLdpServFecFlags_Object = MibTableColumn
vRtrLdpServFecFlags = _VRtrLdpServFecFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 7),
    _VRtrLdpServFecFlags_Type()
)
vRtrLdpServFecFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecFlags.setStatus("obsolete")
_VRtrLdpServFecNumInLabels_Type = Unsigned32
_VRtrLdpServFecNumInLabels_Object = MibTableColumn
vRtrLdpServFecNumInLabels = _VRtrLdpServFecNumInLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 8),
    _VRtrLdpServFecNumInLabels_Type()
)
vRtrLdpServFecNumInLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecNumInLabels.setStatus("obsolete")
_VRtrLdpServFecNumOutLabels_Type = Unsigned32
_VRtrLdpServFecNumOutLabels_Object = MibTableColumn
vRtrLdpServFecNumOutLabels = _VRtrLdpServFecNumOutLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 9),
    _VRtrLdpServFecNumOutLabels_Type()
)
vRtrLdpServFecNumOutLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecNumOutLabels.setStatus("obsolete")
_VRtrLdpServFecInLabel1_Type = Unsigned32
_VRtrLdpServFecInLabel1_Object = MibTableColumn
vRtrLdpServFecInLabel1 = _VRtrLdpServFecInLabel1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 10),
    _VRtrLdpServFecInLabel1_Type()
)
vRtrLdpServFecInLabel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabel1.setStatus("obsolete")
_VRtrLdpServFecInLabelStatus1_Type = TmnxLabelStatus
_VRtrLdpServFecInLabelStatus1_Object = MibTableColumn
vRtrLdpServFecInLabelStatus1 = _VRtrLdpServFecInLabelStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 11),
    _VRtrLdpServFecInLabelStatus1_Type()
)
vRtrLdpServFecInLabelStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelStatus1.setStatus("obsolete")
_VRtrLdpServFecInLabel2_Type = Unsigned32
_VRtrLdpServFecInLabel2_Object = MibTableColumn
vRtrLdpServFecInLabel2 = _VRtrLdpServFecInLabel2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 12),
    _VRtrLdpServFecInLabel2_Type()
)
vRtrLdpServFecInLabel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabel2.setStatus("obsolete")
_VRtrLdpServFecInLabelStatus2_Type = TmnxLabelStatus
_VRtrLdpServFecInLabelStatus2_Object = MibTableColumn
vRtrLdpServFecInLabelStatus2 = _VRtrLdpServFecInLabelStatus2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 13),
    _VRtrLdpServFecInLabelStatus2_Type()
)
vRtrLdpServFecInLabelStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelStatus2.setStatus("obsolete")
_VRtrLdpServFecInLabel3_Type = Unsigned32
_VRtrLdpServFecInLabel3_Object = MibTableColumn
vRtrLdpServFecInLabel3 = _VRtrLdpServFecInLabel3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 14),
    _VRtrLdpServFecInLabel3_Type()
)
vRtrLdpServFecInLabel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabel3.setStatus("obsolete")
_VRtrLdpServFecInLabelStatus3_Type = TmnxLabelStatus
_VRtrLdpServFecInLabelStatus3_Object = MibTableColumn
vRtrLdpServFecInLabelStatus3 = _VRtrLdpServFecInLabelStatus3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 15),
    _VRtrLdpServFecInLabelStatus3_Type()
)
vRtrLdpServFecInLabelStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelStatus3.setStatus("obsolete")
_VRtrLdpServFecInLabel4_Type = Unsigned32
_VRtrLdpServFecInLabel4_Object = MibTableColumn
vRtrLdpServFecInLabel4 = _VRtrLdpServFecInLabel4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 16),
    _VRtrLdpServFecInLabel4_Type()
)
vRtrLdpServFecInLabel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabel4.setStatus("obsolete")
_VRtrLdpServFecInLabelStatus4_Type = TmnxLabelStatus
_VRtrLdpServFecInLabelStatus4_Object = MibTableColumn
vRtrLdpServFecInLabelStatus4 = _VRtrLdpServFecInLabelStatus4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 17),
    _VRtrLdpServFecInLabelStatus4_Type()
)
vRtrLdpServFecInLabelStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelStatus4.setStatus("obsolete")
_VRtrLdpServFecInLabel5_Type = Unsigned32
_VRtrLdpServFecInLabel5_Object = MibTableColumn
vRtrLdpServFecInLabel5 = _VRtrLdpServFecInLabel5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 18),
    _VRtrLdpServFecInLabel5_Type()
)
vRtrLdpServFecInLabel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabel5.setStatus("obsolete")
_VRtrLdpServFecInLabelStatus5_Type = TmnxLabelStatus
_VRtrLdpServFecInLabelStatus5_Object = MibTableColumn
vRtrLdpServFecInLabelStatus5 = _VRtrLdpServFecInLabelStatus5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 19),
    _VRtrLdpServFecInLabelStatus5_Type()
)
vRtrLdpServFecInLabelStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelStatus5.setStatus("obsolete")
_VRtrLdpServFecOutLabel1_Type = Unsigned32
_VRtrLdpServFecOutLabel1_Object = MibTableColumn
vRtrLdpServFecOutLabel1 = _VRtrLdpServFecOutLabel1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 20),
    _VRtrLdpServFecOutLabel1_Type()
)
vRtrLdpServFecOutLabel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabel1.setStatus("obsolete")
_VRtrLdpServFecOutLabelStatus1_Type = TmnxLabelStatus
_VRtrLdpServFecOutLabelStatus1_Object = MibTableColumn
vRtrLdpServFecOutLabelStatus1 = _VRtrLdpServFecOutLabelStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 21),
    _VRtrLdpServFecOutLabelStatus1_Type()
)
vRtrLdpServFecOutLabelStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelStatus1.setStatus("obsolete")
_VRtrLdpServFecOutLabel2_Type = Unsigned32
_VRtrLdpServFecOutLabel2_Object = MibTableColumn
vRtrLdpServFecOutLabel2 = _VRtrLdpServFecOutLabel2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 22),
    _VRtrLdpServFecOutLabel2_Type()
)
vRtrLdpServFecOutLabel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabel2.setStatus("obsolete")
_VRtrLdpServFecOutLabelStatus2_Type = TmnxLabelStatus
_VRtrLdpServFecOutLabelStatus2_Object = MibTableColumn
vRtrLdpServFecOutLabelStatus2 = _VRtrLdpServFecOutLabelStatus2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 23),
    _VRtrLdpServFecOutLabelStatus2_Type()
)
vRtrLdpServFecOutLabelStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelStatus2.setStatus("obsolete")
_VRtrLdpServFecOutLabel3_Type = Unsigned32
_VRtrLdpServFecOutLabel3_Object = MibTableColumn
vRtrLdpServFecOutLabel3 = _VRtrLdpServFecOutLabel3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 24),
    _VRtrLdpServFecOutLabel3_Type()
)
vRtrLdpServFecOutLabel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabel3.setStatus("obsolete")
_VRtrLdpServFecOutLabelStatus3_Type = TmnxLabelStatus
_VRtrLdpServFecOutLabelStatus3_Object = MibTableColumn
vRtrLdpServFecOutLabelStatus3 = _VRtrLdpServFecOutLabelStatus3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 25),
    _VRtrLdpServFecOutLabelStatus3_Type()
)
vRtrLdpServFecOutLabelStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelStatus3.setStatus("obsolete")
_VRtrLdpServFecOutLabel4_Type = Unsigned32
_VRtrLdpServFecOutLabel4_Object = MibTableColumn
vRtrLdpServFecOutLabel4 = _VRtrLdpServFecOutLabel4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 26),
    _VRtrLdpServFecOutLabel4_Type()
)
vRtrLdpServFecOutLabel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabel4.setStatus("obsolete")
_VRtrLdpServFecOutLabelStatus4_Type = TmnxLabelStatus
_VRtrLdpServFecOutLabelStatus4_Object = MibTableColumn
vRtrLdpServFecOutLabelStatus4 = _VRtrLdpServFecOutLabelStatus4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 27),
    _VRtrLdpServFecOutLabelStatus4_Type()
)
vRtrLdpServFecOutLabelStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelStatus4.setStatus("obsolete")
_VRtrLdpServFecOutLabel5_Type = Unsigned32
_VRtrLdpServFecOutLabel5_Object = MibTableColumn
vRtrLdpServFecOutLabel5 = _VRtrLdpServFecOutLabel5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 28),
    _VRtrLdpServFecOutLabel5_Type()
)
vRtrLdpServFecOutLabel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabel5.setStatus("obsolete")
_VRtrLdpServFecOutLabelStatus5_Type = TmnxLabelStatus
_VRtrLdpServFecOutLabelStatus5_Object = MibTableColumn
vRtrLdpServFecOutLabelStatus5 = _VRtrLdpServFecOutLabelStatus5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 29),
    _VRtrLdpServFecOutLabelStatus5_Type()
)
vRtrLdpServFecOutLabelStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelStatus5.setStatus("obsolete")
_VRtrLdpServFecSdpId_Type = SdpId
_VRtrLdpServFecSdpId_Object = MibTableColumn
vRtrLdpServFecSdpId = _VRtrLdpServFecSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 30),
    _VRtrLdpServFecSdpId_Type()
)
vRtrLdpServFecSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecSdpId.setStatus("obsolete")
_VRtrLdpServFecLocalMTU_Type = Unsigned32
_VRtrLdpServFecLocalMTU_Object = MibTableColumn
vRtrLdpServFecLocalMTU = _VRtrLdpServFecLocalMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 31),
    _VRtrLdpServFecLocalMTU_Type()
)
vRtrLdpServFecLocalMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecLocalMTU.setStatus("obsolete")
_VRtrLdpServFecRemoteMTU_Type = Unsigned32
_VRtrLdpServFecRemoteMTU_Object = MibTableColumn
vRtrLdpServFecRemoteMTU = _VRtrLdpServFecRemoteMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 32),
    _VRtrLdpServFecRemoteMTU_Type()
)
vRtrLdpServFecRemoteMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecRemoteMTU.setStatus("obsolete")
_VRtrLdpServFecLocalVlanTag_Type = Unsigned32
_VRtrLdpServFecLocalVlanTag_Object = MibTableColumn
vRtrLdpServFecLocalVlanTag = _VRtrLdpServFecLocalVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 33),
    _VRtrLdpServFecLocalVlanTag_Type()
)
vRtrLdpServFecLocalVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecLocalVlanTag.setStatus("obsolete")
_VRtrLdpServFecRemoteVlanTag_Type = Unsigned32
_VRtrLdpServFecRemoteVlanTag_Object = MibTableColumn
vRtrLdpServFecRemoteVlanTag = _VRtrLdpServFecRemoteVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 34),
    _VRtrLdpServFecRemoteVlanTag_Type()
)
vRtrLdpServFecRemoteVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecRemoteVlanTag.setStatus("obsolete")
_VRtrLdpServFecLocalMaxCellConcat_Type = Unsigned32
_VRtrLdpServFecLocalMaxCellConcat_Object = MibTableColumn
vRtrLdpServFecLocalMaxCellConcat = _VRtrLdpServFecLocalMaxCellConcat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 35),
    _VRtrLdpServFecLocalMaxCellConcat_Type()
)
vRtrLdpServFecLocalMaxCellConcat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecLocalMaxCellConcat.setStatus("obsolete")
_VRtrLdpServFecRemoteMaxCellConcat_Type = Unsigned32
_VRtrLdpServFecRemoteMaxCellConcat_Object = MibTableColumn
vRtrLdpServFecRemoteMaxCellConcat = _VRtrLdpServFecRemoteMaxCellConcat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 36),
    _VRtrLdpServFecRemoteMaxCellConcat_Type()
)
vRtrLdpServFecRemoteMaxCellConcat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecRemoteMaxCellConcat.setStatus("obsolete")
_VRtrLdpServFecInLabelSigStatus1_Type = TmnxLabelSigStatus
_VRtrLdpServFecInLabelSigStatus1_Object = MibTableColumn
vRtrLdpServFecInLabelSigStatus1 = _VRtrLdpServFecInLabelSigStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 37),
    _VRtrLdpServFecInLabelSigStatus1_Type()
)
vRtrLdpServFecInLabelSigStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelSigStatus1.setStatus("obsolete")
_VRtrLdpServFecInLabelSigStatus2_Type = TmnxLabelSigStatus
_VRtrLdpServFecInLabelSigStatus2_Object = MibTableColumn
vRtrLdpServFecInLabelSigStatus2 = _VRtrLdpServFecInLabelSigStatus2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 38),
    _VRtrLdpServFecInLabelSigStatus2_Type()
)
vRtrLdpServFecInLabelSigStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelSigStatus2.setStatus("obsolete")
_VRtrLdpServFecInLabelSigStatus3_Type = TmnxLabelSigStatus
_VRtrLdpServFecInLabelSigStatus3_Object = MibTableColumn
vRtrLdpServFecInLabelSigStatus3 = _VRtrLdpServFecInLabelSigStatus3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 39),
    _VRtrLdpServFecInLabelSigStatus3_Type()
)
vRtrLdpServFecInLabelSigStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelSigStatus3.setStatus("obsolete")
_VRtrLdpServFecInLabelSigStatus4_Type = TmnxLabelSigStatus
_VRtrLdpServFecInLabelSigStatus4_Object = MibTableColumn
vRtrLdpServFecInLabelSigStatus4 = _VRtrLdpServFecInLabelSigStatus4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 40),
    _VRtrLdpServFecInLabelSigStatus4_Type()
)
vRtrLdpServFecInLabelSigStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelSigStatus4.setStatus("obsolete")
_VRtrLdpServFecInLabelSigStatus5_Type = TmnxLabelSigStatus
_VRtrLdpServFecInLabelSigStatus5_Object = MibTableColumn
vRtrLdpServFecInLabelSigStatus5 = _VRtrLdpServFecInLabelSigStatus5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 41),
    _VRtrLdpServFecInLabelSigStatus5_Type()
)
vRtrLdpServFecInLabelSigStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelSigStatus5.setStatus("obsolete")
_VRtrLdpServFecOutLabelSigStatus1_Type = TmnxLabelSigStatus
_VRtrLdpServFecOutLabelSigStatus1_Object = MibTableColumn
vRtrLdpServFecOutLabelSigStatus1 = _VRtrLdpServFecOutLabelSigStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 42),
    _VRtrLdpServFecOutLabelSigStatus1_Type()
)
vRtrLdpServFecOutLabelSigStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelSigStatus1.setStatus("obsolete")
_VRtrLdpServFecOutLabelSigStatus2_Type = TmnxLabelSigStatus
_VRtrLdpServFecOutLabelSigStatus2_Object = MibTableColumn
vRtrLdpServFecOutLabelSigStatus2 = _VRtrLdpServFecOutLabelSigStatus2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 43),
    _VRtrLdpServFecOutLabelSigStatus2_Type()
)
vRtrLdpServFecOutLabelSigStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelSigStatus2.setStatus("obsolete")
_VRtrLdpServFecOutLabelSigStatus3_Type = TmnxLabelSigStatus
_VRtrLdpServFecOutLabelSigStatus3_Object = MibTableColumn
vRtrLdpServFecOutLabelSigStatus3 = _VRtrLdpServFecOutLabelSigStatus3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 44),
    _VRtrLdpServFecOutLabelSigStatus3_Type()
)
vRtrLdpServFecOutLabelSigStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelSigStatus3.setStatus("obsolete")
_VRtrLdpServFecOutLabelSigStatus4_Type = TmnxLabelSigStatus
_VRtrLdpServFecOutLabelSigStatus4_Object = MibTableColumn
vRtrLdpServFecOutLabelSigStatus4 = _VRtrLdpServFecOutLabelSigStatus4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 45),
    _VRtrLdpServFecOutLabelSigStatus4_Type()
)
vRtrLdpServFecOutLabelSigStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelSigStatus4.setStatus("obsolete")
_VRtrLdpServFecOutLabelSigStatus5_Type = TmnxLabelSigStatus
_VRtrLdpServFecOutLabelSigStatus5_Object = MibTableColumn
vRtrLdpServFecOutLabelSigStatus5 = _VRtrLdpServFecOutLabelSigStatus5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 46),
    _VRtrLdpServFecOutLabelSigStatus5_Type()
)
vRtrLdpServFecOutLabelSigStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelSigStatus5.setStatus("obsolete")
_VRtrLdpServFecMateEndpointVcId_Type = TmnxVcId
_VRtrLdpServFecMateEndpointVcId_Object = MibTableColumn
vRtrLdpServFecMateEndpointVcId = _VRtrLdpServFecMateEndpointVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 47),
    _VRtrLdpServFecMateEndpointVcId_Type()
)
vRtrLdpServFecMateEndpointVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecMateEndpointVcId.setStatus("obsolete")
_VRtrLdpServFecMateEndpointSdpId_Type = SdpId
_VRtrLdpServFecMateEndpointSdpId_Object = MibTableColumn
vRtrLdpServFecMateEndpointSdpId = _VRtrLdpServFecMateEndpointSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 48),
    _VRtrLdpServFecMateEndpointSdpId_Type()
)
vRtrLdpServFecMateEndpointSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecMateEndpointSdpId.setStatus("obsolete")
_VRtrLdpServFecLocalIpv4Capblty_Type = TruthValue
_VRtrLdpServFecLocalIpv4Capblty_Object = MibTableColumn
vRtrLdpServFecLocalIpv4Capblty = _VRtrLdpServFecLocalIpv4Capblty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 49),
    _VRtrLdpServFecLocalIpv4Capblty_Type()
)
vRtrLdpServFecLocalIpv4Capblty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecLocalIpv4Capblty.setStatus("obsolete")
_VRtrLdpServFecRemoteIpv4Capblty_Type = TruthValue
_VRtrLdpServFecRemoteIpv4Capblty_Object = MibTableColumn
vRtrLdpServFecRemoteIpv4Capblty = _VRtrLdpServFecRemoteIpv4Capblty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 50),
    _VRtrLdpServFecRemoteIpv4Capblty_Type()
)
vRtrLdpServFecRemoteIpv4Capblty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecRemoteIpv4Capblty.setStatus("obsolete")
_VRtrLdpServFecLocalIpv6Capblty_Type = TruthValue
_VRtrLdpServFecLocalIpv6Capblty_Object = MibTableColumn
vRtrLdpServFecLocalIpv6Capblty = _VRtrLdpServFecLocalIpv6Capblty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 51),
    _VRtrLdpServFecLocalIpv6Capblty_Type()
)
vRtrLdpServFecLocalIpv6Capblty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecLocalIpv6Capblty.setStatus("obsolete")
_VRtrLdpServFecRemoteIpv6Capblty_Type = TruthValue
_VRtrLdpServFecRemoteIpv6Capblty_Object = MibTableColumn
vRtrLdpServFecRemoteIpv6Capblty = _VRtrLdpServFecRemoteIpv6Capblty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 52),
    _VRtrLdpServFecRemoteIpv6Capblty_Type()
)
vRtrLdpServFecRemoteIpv6Capblty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecRemoteIpv6Capblty.setStatus("obsolete")
_VRtrLdpServFecLocalIpv4CeIpAddr_Type = IpAddress
_VRtrLdpServFecLocalIpv4CeIpAddr_Object = MibTableColumn
vRtrLdpServFecLocalIpv4CeIpAddr = _VRtrLdpServFecLocalIpv4CeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 53),
    _VRtrLdpServFecLocalIpv4CeIpAddr_Type()
)
vRtrLdpServFecLocalIpv4CeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecLocalIpv4CeIpAddr.setStatus("obsolete")
_VRtrLdpServFecRemoteIpv4CeIpAddr_Type = IpAddress
_VRtrLdpServFecRemoteIpv4CeIpAddr_Object = MibTableColumn
vRtrLdpServFecRemoteIpv4CeIpAddr = _VRtrLdpServFecRemoteIpv4CeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 54),
    _VRtrLdpServFecRemoteIpv4CeIpAddr_Type()
)
vRtrLdpServFecRemoteIpv4CeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecRemoteIpv4CeIpAddr.setStatus("obsolete")
_VRtrLdpServFecInLbl1WdwReason_Type = TmnxLdpInLblWdrawalReasonCode
_VRtrLdpServFecInLbl1WdwReason_Object = MibTableColumn
vRtrLdpServFecInLbl1WdwReason = _VRtrLdpServFecInLbl1WdwReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 55),
    _VRtrLdpServFecInLbl1WdwReason_Type()
)
vRtrLdpServFecInLbl1WdwReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLbl1WdwReason.setStatus("obsolete")
_VRtrLdpServFecLocalFLTxCapblty_Type = TruthValue
_VRtrLdpServFecLocalFLTxCapblty_Object = MibTableColumn
vRtrLdpServFecLocalFLTxCapblty = _VRtrLdpServFecLocalFLTxCapblty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 56),
    _VRtrLdpServFecLocalFLTxCapblty_Type()
)
vRtrLdpServFecLocalFLTxCapblty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecLocalFLTxCapblty.setStatus("obsolete")
_VRtrLdpServFecLocalFLRxCapblty_Type = TruthValue
_VRtrLdpServFecLocalFLRxCapblty_Object = MibTableColumn
vRtrLdpServFecLocalFLRxCapblty = _VRtrLdpServFecLocalFLRxCapblty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 57),
    _VRtrLdpServFecLocalFLRxCapblty_Type()
)
vRtrLdpServFecLocalFLRxCapblty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecLocalFLRxCapblty.setStatus("obsolete")
_VRtrLdpServFecRemoteFLTxCapblty_Type = TruthValue
_VRtrLdpServFecRemoteFLTxCapblty_Object = MibTableColumn
vRtrLdpServFecRemoteFLTxCapblty = _VRtrLdpServFecRemoteFLTxCapblty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 58),
    _VRtrLdpServFecRemoteFLTxCapblty_Type()
)
vRtrLdpServFecRemoteFLTxCapblty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecRemoteFLTxCapblty.setStatus("obsolete")
_VRtrLdpServFecRemoteFLRxCapblty_Type = TruthValue
_VRtrLdpServFecRemoteFLRxCapblty_Object = MibTableColumn
vRtrLdpServFecRemoteFLRxCapblty = _VRtrLdpServFecRemoteFLRxCapblty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 59),
    _VRtrLdpServFecRemoteFLRxCapblty_Type()
)
vRtrLdpServFecRemoteFLRxCapblty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecRemoteFLRxCapblty.setStatus("obsolete")
_VRtrLdpServFecMapTable_Object = MibTable
vRtrLdpServFecMapTable = _VRtrLdpServFecMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 12)
)
if mibBuilder.loadTexts:
    vRtrLdpServFecMapTable.setStatus("obsolete")
_VRtrLdpServFecMapEntry_Object = MibTableRow
vRtrLdpServFecMapEntry = _VRtrLdpServFecMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 12, 1)
)
vRtrLdpServFecMapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpServFecMapFecType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpServFecMapVcType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpServFecMapVcId"),
)
if mibBuilder.loadTexts:
    vRtrLdpServFecMapEntry.setStatus("obsolete")
_VRtrLdpServFecMapFecType_Type = TmnxLdpFECType
_VRtrLdpServFecMapFecType_Object = MibTableColumn
vRtrLdpServFecMapFecType = _VRtrLdpServFecMapFecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 12, 1, 1),
    _VRtrLdpServFecMapFecType_Type()
)
vRtrLdpServFecMapFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecMapFecType.setStatus("obsolete")
_VRtrLdpServFecMapVcType_Type = TmnxVcType
_VRtrLdpServFecMapVcType_Object = MibTableColumn
vRtrLdpServFecMapVcType = _VRtrLdpServFecMapVcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 12, 1, 2),
    _VRtrLdpServFecMapVcType_Type()
)
vRtrLdpServFecMapVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecMapVcType.setStatus("obsolete")
_VRtrLdpServFecMapVcId_Type = TmnxVcId
_VRtrLdpServFecMapVcId_Object = MibTableColumn
vRtrLdpServFecMapVcId = _VRtrLdpServFecMapVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 12, 1, 3),
    _VRtrLdpServFecMapVcId_Type()
)
vRtrLdpServFecMapVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecMapVcId.setStatus("obsolete")
_VRtrLdpAddrFecTable_Object = MibTable
vRtrLdpAddrFecTable = _VRtrLdpAddrFecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13)
)
if mibBuilder.loadTexts:
    vRtrLdpAddrFecTable.setStatus("obsolete")
_VRtrLdpAddrFecEntry_Object = MibTableRow
vRtrLdpAddrFecEntry = _VRtrLdpAddrFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1)
)
vRtrLdpAddrFecEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddrFecFecType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddrFecIpPrefix"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddrFecIpMask"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    vRtrLdpAddrFecEntry.setStatus("obsolete")
_VRtrLdpAddrFecFecType_Type = TmnxLdpFECType
_VRtrLdpAddrFecFecType_Object = MibTableColumn
vRtrLdpAddrFecFecType = _VRtrLdpAddrFecFecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 1),
    _VRtrLdpAddrFecFecType_Type()
)
vRtrLdpAddrFecFecType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecFecType.setStatus("obsolete")
_VRtrLdpAddrFecIpPrefix_Type = IpAddress
_VRtrLdpAddrFecIpPrefix_Object = MibTableColumn
vRtrLdpAddrFecIpPrefix = _VRtrLdpAddrFecIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 2),
    _VRtrLdpAddrFecIpPrefix_Type()
)
vRtrLdpAddrFecIpPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecIpPrefix.setStatus("obsolete")
_VRtrLdpAddrFecIpMask_Type = IpAddress
_VRtrLdpAddrFecIpMask_Object = MibTableColumn
vRtrLdpAddrFecIpMask = _VRtrLdpAddrFecIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 3),
    _VRtrLdpAddrFecIpMask_Type()
)
vRtrLdpAddrFecIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecIpMask.setStatus("obsolete")
_VRtrLdpAddrFecFlags_Type = TmnxLdpFECFlags
_VRtrLdpAddrFecFlags_Object = MibTableColumn
vRtrLdpAddrFecFlags = _VRtrLdpAddrFecFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 4),
    _VRtrLdpAddrFecFlags_Type()
)
vRtrLdpAddrFecFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecFlags.setStatus("obsolete")
_VRtrLdpAddrFecNumInLabels_Type = Unsigned32
_VRtrLdpAddrFecNumInLabels_Object = MibTableColumn
vRtrLdpAddrFecNumInLabels = _VRtrLdpAddrFecNumInLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 5),
    _VRtrLdpAddrFecNumInLabels_Type()
)
vRtrLdpAddrFecNumInLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecNumInLabels.setStatus("obsolete")
_VRtrLdpAddrFecNumOutLabels_Type = Unsigned32
_VRtrLdpAddrFecNumOutLabels_Object = MibTableColumn
vRtrLdpAddrFecNumOutLabels = _VRtrLdpAddrFecNumOutLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 6),
    _VRtrLdpAddrFecNumOutLabels_Type()
)
vRtrLdpAddrFecNumOutLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecNumOutLabels.setStatus("obsolete")
_VRtrLdpAddrFecInLabel1_Type = Unsigned32
_VRtrLdpAddrFecInLabel1_Object = MibTableColumn
vRtrLdpAddrFecInLabel1 = _VRtrLdpAddrFecInLabel1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 7),
    _VRtrLdpAddrFecInLabel1_Type()
)
vRtrLdpAddrFecInLabel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabel1.setStatus("obsolete")
_VRtrLdpAddrFecInLabelStatus1_Type = TmnxLabelStatus
_VRtrLdpAddrFecInLabelStatus1_Object = MibTableColumn
vRtrLdpAddrFecInLabelStatus1 = _VRtrLdpAddrFecInLabelStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 8),
    _VRtrLdpAddrFecInLabelStatus1_Type()
)
vRtrLdpAddrFecInLabelStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelStatus1.setStatus("obsolete")
_VRtrLdpAddrFecInLabelIfIndex1_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecInLabelIfIndex1_Object = MibTableColumn
vRtrLdpAddrFecInLabelIfIndex1 = _VRtrLdpAddrFecInLabelIfIndex1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 9),
    _VRtrLdpAddrFecInLabelIfIndex1_Type()
)
vRtrLdpAddrFecInLabelIfIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelIfIndex1.setStatus("obsolete")
_VRtrLdpAddrFecInLabel2_Type = Unsigned32
_VRtrLdpAddrFecInLabel2_Object = MibTableColumn
vRtrLdpAddrFecInLabel2 = _VRtrLdpAddrFecInLabel2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 10),
    _VRtrLdpAddrFecInLabel2_Type()
)
vRtrLdpAddrFecInLabel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabel2.setStatus("obsolete")
_VRtrLdpAddrFecInLabelStatus2_Type = TmnxLabelStatus
_VRtrLdpAddrFecInLabelStatus2_Object = MibTableColumn
vRtrLdpAddrFecInLabelStatus2 = _VRtrLdpAddrFecInLabelStatus2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 11),
    _VRtrLdpAddrFecInLabelStatus2_Type()
)
vRtrLdpAddrFecInLabelStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelStatus2.setStatus("obsolete")
_VRtrLdpAddrFecInLabelIfIndex2_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecInLabelIfIndex2_Object = MibTableColumn
vRtrLdpAddrFecInLabelIfIndex2 = _VRtrLdpAddrFecInLabelIfIndex2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 12),
    _VRtrLdpAddrFecInLabelIfIndex2_Type()
)
vRtrLdpAddrFecInLabelIfIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelIfIndex2.setStatus("obsolete")
_VRtrLdpAddrFecInLabel3_Type = Unsigned32
_VRtrLdpAddrFecInLabel3_Object = MibTableColumn
vRtrLdpAddrFecInLabel3 = _VRtrLdpAddrFecInLabel3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 13),
    _VRtrLdpAddrFecInLabel3_Type()
)
vRtrLdpAddrFecInLabel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabel3.setStatus("obsolete")
_VRtrLdpAddrFecInLabelStatus3_Type = TmnxLabelStatus
_VRtrLdpAddrFecInLabelStatus3_Object = MibTableColumn
vRtrLdpAddrFecInLabelStatus3 = _VRtrLdpAddrFecInLabelStatus3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 14),
    _VRtrLdpAddrFecInLabelStatus3_Type()
)
vRtrLdpAddrFecInLabelStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelStatus3.setStatus("obsolete")
_VRtrLdpAddrFecInLabelIfIndex3_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecInLabelIfIndex3_Object = MibTableColumn
vRtrLdpAddrFecInLabelIfIndex3 = _VRtrLdpAddrFecInLabelIfIndex3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 15),
    _VRtrLdpAddrFecInLabelIfIndex3_Type()
)
vRtrLdpAddrFecInLabelIfIndex3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelIfIndex3.setStatus("obsolete")
_VRtrLdpAddrFecInLabel4_Type = Unsigned32
_VRtrLdpAddrFecInLabel4_Object = MibTableColumn
vRtrLdpAddrFecInLabel4 = _VRtrLdpAddrFecInLabel4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 16),
    _VRtrLdpAddrFecInLabel4_Type()
)
vRtrLdpAddrFecInLabel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabel4.setStatus("obsolete")
_VRtrLdpAddrFecInLabelStatus4_Type = TmnxLabelStatus
_VRtrLdpAddrFecInLabelStatus4_Object = MibTableColumn
vRtrLdpAddrFecInLabelStatus4 = _VRtrLdpAddrFecInLabelStatus4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 17),
    _VRtrLdpAddrFecInLabelStatus4_Type()
)
vRtrLdpAddrFecInLabelStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelStatus4.setStatus("obsolete")
_VRtrLdpAddrFecInLabelIfIndex4_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecInLabelIfIndex4_Object = MibTableColumn
vRtrLdpAddrFecInLabelIfIndex4 = _VRtrLdpAddrFecInLabelIfIndex4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 18),
    _VRtrLdpAddrFecInLabelIfIndex4_Type()
)
vRtrLdpAddrFecInLabelIfIndex4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelIfIndex4.setStatus("obsolete")
_VRtrLdpAddrFecInLabel5_Type = Unsigned32
_VRtrLdpAddrFecInLabel5_Object = MibTableColumn
vRtrLdpAddrFecInLabel5 = _VRtrLdpAddrFecInLabel5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 19),
    _VRtrLdpAddrFecInLabel5_Type()
)
vRtrLdpAddrFecInLabel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabel5.setStatus("obsolete")
_VRtrLdpAddrFecInLabelStatus5_Type = TmnxLabelStatus
_VRtrLdpAddrFecInLabelStatus5_Object = MibTableColumn
vRtrLdpAddrFecInLabelStatus5 = _VRtrLdpAddrFecInLabelStatus5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 20),
    _VRtrLdpAddrFecInLabelStatus5_Type()
)
vRtrLdpAddrFecInLabelStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelStatus5.setStatus("obsolete")
_VRtrLdpAddrFecInLabelIfIndex5_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecInLabelIfIndex5_Object = MibTableColumn
vRtrLdpAddrFecInLabelIfIndex5 = _VRtrLdpAddrFecInLabelIfIndex5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 21),
    _VRtrLdpAddrFecInLabelIfIndex5_Type()
)
vRtrLdpAddrFecInLabelIfIndex5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelIfIndex5.setStatus("obsolete")
_VRtrLdpAddrFecOutLabel1_Type = Unsigned32
_VRtrLdpAddrFecOutLabel1_Object = MibTableColumn
vRtrLdpAddrFecOutLabel1 = _VRtrLdpAddrFecOutLabel1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 22),
    _VRtrLdpAddrFecOutLabel1_Type()
)
vRtrLdpAddrFecOutLabel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabel1.setStatus("obsolete")
_VRtrLdpAddrFecOutLabelStatus1_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLabelStatus1_Object = MibTableColumn
vRtrLdpAddrFecOutLabelStatus1 = _VRtrLdpAddrFecOutLabelStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 23),
    _VRtrLdpAddrFecOutLabelStatus1_Type()
)
vRtrLdpAddrFecOutLabelStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelStatus1.setStatus("obsolete")
_VRtrLdpAddrFecOutLabelIfIndex1_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLabelIfIndex1_Object = MibTableColumn
vRtrLdpAddrFecOutLabelIfIndex1 = _VRtrLdpAddrFecOutLabelIfIndex1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 24),
    _VRtrLdpAddrFecOutLabelIfIndex1_Type()
)
vRtrLdpAddrFecOutLabelIfIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelIfIndex1.setStatus("obsolete")
_VRtrLdpAddrFecOutLabelNextHop1_Type = IpAddress
_VRtrLdpAddrFecOutLabelNextHop1_Object = MibTableColumn
vRtrLdpAddrFecOutLabelNextHop1 = _VRtrLdpAddrFecOutLabelNextHop1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 25),
    _VRtrLdpAddrFecOutLabelNextHop1_Type()
)
vRtrLdpAddrFecOutLabelNextHop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelNextHop1.setStatus("obsolete")
_VRtrLdpAddrFecOutLabel2_Type = Unsigned32
_VRtrLdpAddrFecOutLabel2_Object = MibTableColumn
vRtrLdpAddrFecOutLabel2 = _VRtrLdpAddrFecOutLabel2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 26),
    _VRtrLdpAddrFecOutLabel2_Type()
)
vRtrLdpAddrFecOutLabel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabel2.setStatus("obsolete")
_VRtrLdpAddrFecOutLabelStatus2_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLabelStatus2_Object = MibTableColumn
vRtrLdpAddrFecOutLabelStatus2 = _VRtrLdpAddrFecOutLabelStatus2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 27),
    _VRtrLdpAddrFecOutLabelStatus2_Type()
)
vRtrLdpAddrFecOutLabelStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelStatus2.setStatus("obsolete")
_VRtrLdpAddrFecOutLabelIfIndex2_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLabelIfIndex2_Object = MibTableColumn
vRtrLdpAddrFecOutLabelIfIndex2 = _VRtrLdpAddrFecOutLabelIfIndex2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 28),
    _VRtrLdpAddrFecOutLabelIfIndex2_Type()
)
vRtrLdpAddrFecOutLabelIfIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelIfIndex2.setStatus("obsolete")
_VRtrLdpAddrFecOutLabelNextHop2_Type = IpAddress
_VRtrLdpAddrFecOutLabelNextHop2_Object = MibTableColumn
vRtrLdpAddrFecOutLabelNextHop2 = _VRtrLdpAddrFecOutLabelNextHop2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 29),
    _VRtrLdpAddrFecOutLabelNextHop2_Type()
)
vRtrLdpAddrFecOutLabelNextHop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelNextHop2.setStatus("obsolete")
_VRtrLdpAddrFecOutLabel3_Type = Unsigned32
_VRtrLdpAddrFecOutLabel3_Object = MibTableColumn
vRtrLdpAddrFecOutLabel3 = _VRtrLdpAddrFecOutLabel3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 30),
    _VRtrLdpAddrFecOutLabel3_Type()
)
vRtrLdpAddrFecOutLabel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabel3.setStatus("obsolete")
_VRtrLdpAddrFecOutLabelStatus3_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLabelStatus3_Object = MibTableColumn
vRtrLdpAddrFecOutLabelStatus3 = _VRtrLdpAddrFecOutLabelStatus3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 31),
    _VRtrLdpAddrFecOutLabelStatus3_Type()
)
vRtrLdpAddrFecOutLabelStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelStatus3.setStatus("obsolete")
_VRtrLdpAddrFecOutLabelIfIndex3_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLabelIfIndex3_Object = MibTableColumn
vRtrLdpAddrFecOutLabelIfIndex3 = _VRtrLdpAddrFecOutLabelIfIndex3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 32),
    _VRtrLdpAddrFecOutLabelIfIndex3_Type()
)
vRtrLdpAddrFecOutLabelIfIndex3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelIfIndex3.setStatus("obsolete")
_VRtrLdpAddrFecOutLabelNextHop3_Type = IpAddress
_VRtrLdpAddrFecOutLabelNextHop3_Object = MibTableColumn
vRtrLdpAddrFecOutLabelNextHop3 = _VRtrLdpAddrFecOutLabelNextHop3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 33),
    _VRtrLdpAddrFecOutLabelNextHop3_Type()
)
vRtrLdpAddrFecOutLabelNextHop3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelNextHop3.setStatus("obsolete")
_VRtrLdpAddrFecOutLabel4_Type = Unsigned32
_VRtrLdpAddrFecOutLabel4_Object = MibTableColumn
vRtrLdpAddrFecOutLabel4 = _VRtrLdpAddrFecOutLabel4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 34),
    _VRtrLdpAddrFecOutLabel4_Type()
)
vRtrLdpAddrFecOutLabel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabel4.setStatus("obsolete")
_VRtrLdpAddrFecOutLabelStatus4_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLabelStatus4_Object = MibTableColumn
vRtrLdpAddrFecOutLabelStatus4 = _VRtrLdpAddrFecOutLabelStatus4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 35),
    _VRtrLdpAddrFecOutLabelStatus4_Type()
)
vRtrLdpAddrFecOutLabelStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelStatus4.setStatus("obsolete")
_VRtrLdpAddrFecOutLabelIfIndex4_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLabelIfIndex4_Object = MibTableColumn
vRtrLdpAddrFecOutLabelIfIndex4 = _VRtrLdpAddrFecOutLabelIfIndex4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 36),
    _VRtrLdpAddrFecOutLabelIfIndex4_Type()
)
vRtrLdpAddrFecOutLabelIfIndex4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelIfIndex4.setStatus("obsolete")
_VRtrLdpAddrFecOutLabelNextHop4_Type = IpAddress
_VRtrLdpAddrFecOutLabelNextHop4_Object = MibTableColumn
vRtrLdpAddrFecOutLabelNextHop4 = _VRtrLdpAddrFecOutLabelNextHop4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 37),
    _VRtrLdpAddrFecOutLabelNextHop4_Type()
)
vRtrLdpAddrFecOutLabelNextHop4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelNextHop4.setStatus("obsolete")
_VRtrLdpAddrFecOutLabel5_Type = Unsigned32
_VRtrLdpAddrFecOutLabel5_Object = MibTableColumn
vRtrLdpAddrFecOutLabel5 = _VRtrLdpAddrFecOutLabel5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 38),
    _VRtrLdpAddrFecOutLabel5_Type()
)
vRtrLdpAddrFecOutLabel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabel5.setStatus("obsolete")
_VRtrLdpAddrFecOutLabelStatus5_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLabelStatus5_Object = MibTableColumn
vRtrLdpAddrFecOutLabelStatus5 = _VRtrLdpAddrFecOutLabelStatus5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 39),
    _VRtrLdpAddrFecOutLabelStatus5_Type()
)
vRtrLdpAddrFecOutLabelStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelStatus5.setStatus("obsolete")
_VRtrLdpAddrFecOutLabelIfIndex5_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLabelIfIndex5_Object = MibTableColumn
vRtrLdpAddrFecOutLabelIfIndex5 = _VRtrLdpAddrFecOutLabelIfIndex5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 40),
    _VRtrLdpAddrFecOutLabelIfIndex5_Type()
)
vRtrLdpAddrFecOutLabelIfIndex5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelIfIndex5.setStatus("obsolete")
_VRtrLdpAddrFecOutLabelNextHop5_Type = IpAddress
_VRtrLdpAddrFecOutLabelNextHop5_Object = MibTableColumn
vRtrLdpAddrFecOutLabelNextHop5 = _VRtrLdpAddrFecOutLabelNextHop5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 41),
    _VRtrLdpAddrFecOutLabelNextHop5_Type()
)
vRtrLdpAddrFecOutLabelNextHop5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelNextHop5.setStatus("obsolete")
_VRtrLdpAddrFecLspId_Type = TmnxVRtrMplsLspID
_VRtrLdpAddrFecLspId_Object = MibTableColumn
vRtrLdpAddrFecLspId = _VRtrLdpAddrFecLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 42),
    _VRtrLdpAddrFecLspId_Type()
)
vRtrLdpAddrFecLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecLspId.setStatus("obsolete")
_VRtrLdpAddrFecLspId2_Type = TmnxVRtrMplsLspID
_VRtrLdpAddrFecLspId2_Object = MibTableColumn
vRtrLdpAddrFecLspId2 = _VRtrLdpAddrFecLspId2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 43),
    _VRtrLdpAddrFecLspId2_Type()
)
vRtrLdpAddrFecLspId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecLspId2.setStatus("obsolete")
_VRtrLdpAddrFecLspId3_Type = TmnxVRtrMplsLspID
_VRtrLdpAddrFecLspId3_Object = MibTableColumn
vRtrLdpAddrFecLspId3 = _VRtrLdpAddrFecLspId3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 44),
    _VRtrLdpAddrFecLspId3_Type()
)
vRtrLdpAddrFecLspId3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecLspId3.setStatus("obsolete")
_VRtrLdpAddrFecLspId4_Type = TmnxVRtrMplsLspID
_VRtrLdpAddrFecLspId4_Object = MibTableColumn
vRtrLdpAddrFecLspId4 = _VRtrLdpAddrFecLspId4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 45),
    _VRtrLdpAddrFecLspId4_Type()
)
vRtrLdpAddrFecLspId4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecLspId4.setStatus("obsolete")
_VRtrLdpAddrFecLspId5_Type = TmnxVRtrMplsLspID
_VRtrLdpAddrFecLspId5_Object = MibTableColumn
vRtrLdpAddrFecLspId5 = _VRtrLdpAddrFecLspId5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 46),
    _VRtrLdpAddrFecLspId5_Type()
)
vRtrLdpAddrFecLspId5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecLspId5.setStatus("obsolete")
_VRtrLdpAddrFecMapTable_Object = MibTable
vRtrLdpAddrFecMapTable = _VRtrLdpAddrFecMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 14)
)
if mibBuilder.loadTexts:
    vRtrLdpAddrFecMapTable.setStatus("obsolete")
_VRtrLdpAddrFecMapEntry_Object = MibTableRow
vRtrLdpAddrFecMapEntry = _VRtrLdpAddrFecMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 14, 1)
)
vRtrLdpAddrFecMapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapFecType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapIpPrefix"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapIpMask"),
)
if mibBuilder.loadTexts:
    vRtrLdpAddrFecMapEntry.setStatus("obsolete")
_VRtrLdpAddrFecMapFecType_Type = TmnxLdpFECType
_VRtrLdpAddrFecMapFecType_Object = MibTableColumn
vRtrLdpAddrFecMapFecType = _VRtrLdpAddrFecMapFecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 14, 1, 1),
    _VRtrLdpAddrFecMapFecType_Type()
)
vRtrLdpAddrFecMapFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecMapFecType.setStatus("obsolete")
_VRtrLdpAddrFecMapIpPrefix_Type = IpAddress
_VRtrLdpAddrFecMapIpPrefix_Object = MibTableColumn
vRtrLdpAddrFecMapIpPrefix = _VRtrLdpAddrFecMapIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 14, 1, 2),
    _VRtrLdpAddrFecMapIpPrefix_Type()
)
vRtrLdpAddrFecMapIpPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecMapIpPrefix.setStatus("obsolete")
_VRtrLdpAddrFecMapIpMask_Type = IpAddress
_VRtrLdpAddrFecMapIpMask_Object = MibTableColumn
vRtrLdpAddrFecMapIpMask = _VRtrLdpAddrFecMapIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 14, 1, 3),
    _VRtrLdpAddrFecMapIpMask_Type()
)
vRtrLdpAddrFecMapIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecMapIpMask.setStatus("obsolete")
_VRtrLdpAdjBackoffTable_Object = MibTable
vRtrLdpAdjBackoffTable = _VRtrLdpAdjBackoffTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 15)
)
if mibBuilder.loadTexts:
    vRtrLdpAdjBackoffTable.setStatus("obsolete")
_VRtrLdpAdjBackoffEntry_Object = MibTableRow
vRtrLdpAdjBackoffEntry = _VRtrLdpAdjBackoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 15, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpAdjBackoffEntry.setStatus("obsolete")


class _VRtrLdpAdjInitBackoff_Type(Unsigned32):
    """Custom type vRtrLdpAdjInitBackoff based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2592000),
    )


_VRtrLdpAdjInitBackoff_Type.__name__ = "Unsigned32"
_VRtrLdpAdjInitBackoff_Object = MibTableColumn
vRtrLdpAdjInitBackoff = _VRtrLdpAdjInitBackoff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 15, 1, 1),
    _VRtrLdpAdjInitBackoff_Type()
)
vRtrLdpAdjInitBackoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAdjInitBackoff.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpAdjInitBackoff.setUnits("seconds")


class _VRtrLdpAdjMaxBackoff_Type(Unsigned32):
    """Custom type vRtrLdpAdjMaxBackoff based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2592000),
    )


_VRtrLdpAdjMaxBackoff_Type.__name__ = "Unsigned32"
_VRtrLdpAdjMaxBackoff_Object = MibTableColumn
vRtrLdpAdjMaxBackoff = _VRtrLdpAdjMaxBackoff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 15, 1, 2),
    _VRtrLdpAdjMaxBackoff_Type()
)
vRtrLdpAdjMaxBackoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAdjMaxBackoff.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpAdjMaxBackoff.setUnits("seconds")
_VRtrLdpAdjCurrentBackoff_Type = Unsigned32
_VRtrLdpAdjCurrentBackoff_Object = MibTableColumn
vRtrLdpAdjCurrentBackoff = _VRtrLdpAdjCurrentBackoff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 15, 1, 3),
    _VRtrLdpAdjCurrentBackoff_Type()
)
vRtrLdpAdjCurrentBackoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAdjCurrentBackoff.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpAdjCurrentBackoff.setUnits("seconds")
_VRtrLdpAdjWaitingTime_Type = Unsigned32
_VRtrLdpAdjWaitingTime_Object = MibTableColumn
vRtrLdpAdjWaitingTime = _VRtrLdpAdjWaitingTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 15, 1, 4),
    _VRtrLdpAdjWaitingTime_Type()
)
vRtrLdpAdjWaitingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAdjWaitingTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpAdjWaitingTime.setUnits("seconds")
_VRtrLdpAdjBackoffStatus_Type = TruthValue
_VRtrLdpAdjBackoffStatus_Object = MibTableColumn
vRtrLdpAdjBackoffStatus = _VRtrLdpAdjBackoffStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 15, 1, 5),
    _VRtrLdpAdjBackoffStatus_Type()
)
vRtrLdpAdjBackoffStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAdjBackoffStatus.setStatus("obsolete")
_VRtrLdpPeerParamsTable_Object = MibTable
vRtrLdpPeerParamsTable = _VRtrLdpPeerParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16)
)
if mibBuilder.loadTexts:
    vRtrLdpPeerParamsTable.setStatus("obsolete")
_VRtrLdpPeerParamsEntry_Object = MibTableRow
vRtrLdpPeerParamsEntry = _VRtrLdpPeerParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1)
)
vRtrLdpPeerParamsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerAddress"),
)
if mibBuilder.loadTexts:
    vRtrLdpPeerParamsEntry.setStatus("obsolete")
_VRtrLdpPeerRowStatus_Type = RowStatus
_VRtrLdpPeerRowStatus_Object = MibTableColumn
vRtrLdpPeerRowStatus = _VRtrLdpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 1),
    _VRtrLdpPeerRowStatus_Type()
)
vRtrLdpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerRowStatus.setStatus("obsolete")


class _VRtrLdpPeerAuth_Type(TruthValue):
    """Custom type vRtrLdpPeerAuth based on TruthValue"""
    defaultValue = 2


_VRtrLdpPeerAuth_Type.__name__ = "TruthValue"
_VRtrLdpPeerAuth_Object = MibTableColumn
vRtrLdpPeerAuth = _VRtrLdpPeerAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 2),
    _VRtrLdpPeerAuth_Type()
)
vRtrLdpPeerAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerAuth.setStatus("obsolete")


class _VRtrLdpPeerAuthKey_Type(OctetString):
    """Custom type vRtrLdpPeerAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VRtrLdpPeerAuthKey_Type.__name__ = "OctetString"
_VRtrLdpPeerAuthKey_Object = MibTableColumn
vRtrLdpPeerAuthKey = _VRtrLdpPeerAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 3),
    _VRtrLdpPeerAuthKey_Type()
)
vRtrLdpPeerAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerAuthKey.setStatus("obsolete")


class _VRtrLdpPeerMinTTLValue_Type(Unsigned32):
    """Custom type vRtrLdpPeerMinTTLValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_VRtrLdpPeerMinTTLValue_Type.__name__ = "Unsigned32"
_VRtrLdpPeerMinTTLValue_Object = MibTableColumn
vRtrLdpPeerMinTTLValue = _VRtrLdpPeerMinTTLValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 4),
    _VRtrLdpPeerMinTTLValue_Type()
)
vRtrLdpPeerMinTTLValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerMinTTLValue.setStatus("obsolete")


class _VRtrLdpPeerTTLLogId_Type(TFilterLogId):
    """Custom type vRtrLdpPeerTTLLogId based on TFilterLogId"""
    defaultValue = 0


_VRtrLdpPeerTTLLogId_Type.__name__ = "TFilterLogId"
_VRtrLdpPeerTTLLogId_Object = MibTableColumn
vRtrLdpPeerTTLLogId = _VRtrLdpPeerTTLLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 5),
    _VRtrLdpPeerTTLLogId_Type()
)
vRtrLdpPeerTTLLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTTLLogId.setStatus("obsolete")


class _VRtrLdpPeerAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type vRtrLdpPeerAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPeerAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_VRtrLdpPeerAuthKeyChain_Object = MibTableColumn
vRtrLdpPeerAuthKeyChain = _VRtrLdpPeerAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 6),
    _VRtrLdpPeerAuthKeyChain_Type()
)
vRtrLdpPeerAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerAuthKeyChain.setStatus("obsolete")


class _VRtrLdpPeerDODLabelDistribution_Type(TruthValue):
    """Custom type vRtrLdpPeerDODLabelDistribution based on TruthValue"""
    defaultValue = 2


_VRtrLdpPeerDODLabelDistribution_Type.__name__ = "TruthValue"
_VRtrLdpPeerDODLabelDistribution_Object = MibTableColumn
vRtrLdpPeerDODLabelDistribution = _VRtrLdpPeerDODLabelDistribution_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 7),
    _VRtrLdpPeerDODLabelDistribution_Type()
)
vRtrLdpPeerDODLabelDistribution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerDODLabelDistribution.setStatus("obsolete")


class _VRtrLdpPeerImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpPeerImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPeerImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpPeerImportPolicy1_Object = MibTableColumn
vRtrLdpPeerImportPolicy1 = _VRtrLdpPeerImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 8),
    _VRtrLdpPeerImportPolicy1_Type()
)
vRtrLdpPeerImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerImportPolicy1.setStatus("obsolete")


class _VRtrLdpPeerImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpPeerImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPeerImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpPeerImportPolicy2_Object = MibTableColumn
vRtrLdpPeerImportPolicy2 = _VRtrLdpPeerImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 9),
    _VRtrLdpPeerImportPolicy2_Type()
)
vRtrLdpPeerImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerImportPolicy2.setStatus("obsolete")


class _VRtrLdpPeerImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpPeerImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPeerImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpPeerImportPolicy3_Object = MibTableColumn
vRtrLdpPeerImportPolicy3 = _VRtrLdpPeerImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 10),
    _VRtrLdpPeerImportPolicy3_Type()
)
vRtrLdpPeerImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerImportPolicy3.setStatus("obsolete")


class _VRtrLdpPeerImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpPeerImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPeerImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpPeerImportPolicy4_Object = MibTableColumn
vRtrLdpPeerImportPolicy4 = _VRtrLdpPeerImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 11),
    _VRtrLdpPeerImportPolicy4_Type()
)
vRtrLdpPeerImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerImportPolicy4.setStatus("obsolete")


class _VRtrLdpPeerImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpPeerImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPeerImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpPeerImportPolicy5_Object = MibTableColumn
vRtrLdpPeerImportPolicy5 = _VRtrLdpPeerImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 12),
    _VRtrLdpPeerImportPolicy5_Type()
)
vRtrLdpPeerImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerImportPolicy5.setStatus("obsolete")


class _VRtrLdpPeerExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpPeerExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPeerExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpPeerExportPolicy1_Object = MibTableColumn
vRtrLdpPeerExportPolicy1 = _VRtrLdpPeerExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 13),
    _VRtrLdpPeerExportPolicy1_Type()
)
vRtrLdpPeerExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerExportPolicy1.setStatus("obsolete")


class _VRtrLdpPeerExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpPeerExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPeerExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpPeerExportPolicy2_Object = MibTableColumn
vRtrLdpPeerExportPolicy2 = _VRtrLdpPeerExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 14),
    _VRtrLdpPeerExportPolicy2_Type()
)
vRtrLdpPeerExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerExportPolicy2.setStatus("obsolete")


class _VRtrLdpPeerExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpPeerExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPeerExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpPeerExportPolicy3_Object = MibTableColumn
vRtrLdpPeerExportPolicy3 = _VRtrLdpPeerExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 15),
    _VRtrLdpPeerExportPolicy3_Type()
)
vRtrLdpPeerExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerExportPolicy3.setStatus("obsolete")


class _VRtrLdpPeerExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpPeerExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPeerExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpPeerExportPolicy4_Object = MibTableColumn
vRtrLdpPeerExportPolicy4 = _VRtrLdpPeerExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 16),
    _VRtrLdpPeerExportPolicy4_Type()
)
vRtrLdpPeerExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerExportPolicy4.setStatus("obsolete")


class _VRtrLdpPeerExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpPeerExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPeerExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpPeerExportPolicy5_Object = MibTableColumn
vRtrLdpPeerExportPolicy5 = _VRtrLdpPeerExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 17),
    _VRtrLdpPeerExportPolicy5_Type()
)
vRtrLdpPeerExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerExportPolicy5.setStatus("obsolete")


class _VRtrLdpPeerFec129CiscoInterop_Type(TruthValue):
    """Custom type vRtrLdpPeerFec129CiscoInterop based on TruthValue"""
    defaultValue = 2


_VRtrLdpPeerFec129CiscoInterop_Type.__name__ = "TruthValue"
_VRtrLdpPeerFec129CiscoInterop_Object = MibTableColumn
vRtrLdpPeerFec129CiscoInterop = _VRtrLdpPeerFec129CiscoInterop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 18),
    _VRtrLdpPeerFec129CiscoInterop_Type()
)
vRtrLdpPeerFec129CiscoInterop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerFec129CiscoInterop.setStatus("obsolete")


class _VRtrLdpPeerPMTUDiscovery_Type(TruthValue):
    """Custom type vRtrLdpPeerPMTUDiscovery based on TruthValue"""
    defaultValue = 2


_VRtrLdpPeerPMTUDiscovery_Type.__name__ = "TruthValue"
_VRtrLdpPeerPMTUDiscovery_Object = MibTableColumn
vRtrLdpPeerPMTUDiscovery = _VRtrLdpPeerPMTUDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 19),
    _VRtrLdpPeerPMTUDiscovery_Type()
)
vRtrLdpPeerPMTUDiscovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerPMTUDiscovery.setStatus("obsolete")


class _VRtrLdpPeerAdvAdjAddrOnly_Type(TruthValue):
    """Custom type vRtrLdpPeerAdvAdjAddrOnly based on TruthValue"""
    defaultValue = 2


_VRtrLdpPeerAdvAdjAddrOnly_Type.__name__ = "TruthValue"
_VRtrLdpPeerAdvAdjAddrOnly_Object = MibTableColumn
vRtrLdpPeerAdvAdjAddrOnly = _VRtrLdpPeerAdvAdjAddrOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 20),
    _VRtrLdpPeerAdvAdjAddrOnly_Type()
)
vRtrLdpPeerAdvAdjAddrOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerAdvAdjAddrOnly.setStatus("obsolete")


class _VRtrLdpPeerPeIDMacFlushInterop_Type(TruthValue):
    """Custom type vRtrLdpPeerPeIDMacFlushInterop based on TruthValue"""
    defaultValue = 2


_VRtrLdpPeerPeIDMacFlushInterop_Type.__name__ = "TruthValue"
_VRtrLdpPeerPeIDMacFlushInterop_Object = MibTableColumn
vRtrLdpPeerPeIDMacFlushInterop = _VRtrLdpPeerPeIDMacFlushInterop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 21),
    _VRtrLdpPeerPeIDMacFlushInterop_Type()
)
vRtrLdpPeerPeIDMacFlushInterop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerPeIDMacFlushInterop.setStatus("obsolete")


class _VRtrLdpPeerMaxFec_Type(Unsigned32):
    """Custom type vRtrLdpPeerMaxFec based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrLdpPeerMaxFec_Type.__name__ = "Unsigned32"
_VRtrLdpPeerMaxFec_Object = MibTableColumn
vRtrLdpPeerMaxFec = _VRtrLdpPeerMaxFec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 22),
    _VRtrLdpPeerMaxFec_Type()
)
vRtrLdpPeerMaxFec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerMaxFec.setStatus("obsolete")


class _VRtrLdpPeerMaxFecLogOnly_Type(TruthValue):
    """Custom type vRtrLdpPeerMaxFecLogOnly based on TruthValue"""
    defaultValue = 2


_VRtrLdpPeerMaxFecLogOnly_Type.__name__ = "TruthValue"
_VRtrLdpPeerMaxFecLogOnly_Object = MibTableColumn
vRtrLdpPeerMaxFecLogOnly = _VRtrLdpPeerMaxFecLogOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 23),
    _VRtrLdpPeerMaxFecLogOnly_Type()
)
vRtrLdpPeerMaxFecLogOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerMaxFecLogOnly.setStatus("obsolete")


class _VRtrLdpPeerMaxFecThreshold_Type(Unsigned32):
    """Custom type vRtrLdpPeerMaxFecThreshold based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VRtrLdpPeerMaxFecThreshold_Type.__name__ = "Unsigned32"
_VRtrLdpPeerMaxFecThreshold_Object = MibTableColumn
vRtrLdpPeerMaxFecThreshold = _VRtrLdpPeerMaxFecThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 24),
    _VRtrLdpPeerMaxFecThreshold_Type()
)
vRtrLdpPeerMaxFecThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerMaxFecThreshold.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpPeerMaxFecThreshold.setUnits("percent")
_TmnxLdpNotificationObjects_ObjectIdentity = ObjectIdentity
tmnxLdpNotificationObjects = _TmnxLdpNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 17)
)


class _VRtrLdpInstanceNotifyReasonCode_Type(Integer32):
    """Custom type vRtrLdpInstanceNotifyReasonCode based on Integer32"""
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
        *(("adminUp", 1),
          ("adminDown", 2),
          ("operUp", 3),
          ("operDown", 4))
    )


_VRtrLdpInstanceNotifyReasonCode_Type.__name__ = "Integer32"
_VRtrLdpInstanceNotifyReasonCode_Object = MibScalar
vRtrLdpInstanceNotifyReasonCode = _VRtrLdpInstanceNotifyReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 17, 1),
    _VRtrLdpInstanceNotifyReasonCode_Type()
)
vRtrLdpInstanceNotifyReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrLdpInstanceNotifyReasonCode.setStatus("obsolete")


class _VRtrLdpIfNotifyReasonCode_Type(Integer32):
    """Custom type vRtrLdpIfNotifyReasonCode based on Integer32"""
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
        *(("adminUp", 1),
          ("adminDown", 2),
          ("operUp", 3),
          ("operDown", 4),
          ("sysIpUp", 5),
          ("sysIpDown", 6))
    )


_VRtrLdpIfNotifyReasonCode_Type.__name__ = "Integer32"
_VRtrLdpIfNotifyReasonCode_Object = MibScalar
vRtrLdpIfNotifyReasonCode = _VRtrLdpIfNotifyReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 17, 2),
    _VRtrLdpIfNotifyReasonCode_Type()
)
vRtrLdpIfNotifyReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrLdpIfNotifyReasonCode.setStatus("obsolete")


class _VRtrLdpNotifyLocalServiceID_Type(TmnxServId):
    """Custom type vRtrLdpNotifyLocalServiceID based on TmnxServId"""
    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrLdpNotifyLocalServiceID_Type.__name__ = "TmnxServId"
_VRtrLdpNotifyLocalServiceID_Object = MibScalar
vRtrLdpNotifyLocalServiceID = _VRtrLdpNotifyLocalServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 17, 3),
    _VRtrLdpNotifyLocalServiceID_Type()
)
vRtrLdpNotifyLocalServiceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrLdpNotifyLocalServiceID.setStatus("obsolete")


class _VRtrLdpNotifyRemoteServiceID_Type(TmnxServId):
    """Custom type vRtrLdpNotifyRemoteServiceID based on TmnxServId"""
    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrLdpNotifyRemoteServiceID_Type.__name__ = "TmnxServId"
_VRtrLdpNotifyRemoteServiceID_Object = MibScalar
vRtrLdpNotifyRemoteServiceID = _VRtrLdpNotifyRemoteServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 17, 4),
    _VRtrLdpNotifyRemoteServiceID_Type()
)
vRtrLdpNotifyRemoteServiceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrLdpNotifyRemoteServiceID.setStatus("obsolete")
_VRtrLdpNotifyLocalGroupID_Type = TmnxVcId
_VRtrLdpNotifyLocalGroupID_Object = MibScalar
vRtrLdpNotifyLocalGroupID = _VRtrLdpNotifyLocalGroupID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 17, 5),
    _VRtrLdpNotifyLocalGroupID_Type()
)
vRtrLdpNotifyLocalGroupID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrLdpNotifyLocalGroupID.setStatus("current")
_VRtrLdpNotifyRemoteGroupID_Type = TmnxVcId
_VRtrLdpNotifyRemoteGroupID_Object = MibScalar
vRtrLdpNotifyRemoteGroupID = _VRtrLdpNotifyRemoteGroupID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 17, 6),
    _VRtrLdpNotifyRemoteGroupID_Type()
)
vRtrLdpNotifyRemoteGroupID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrLdpNotifyRemoteGroupID.setStatus("current")
_VRtrLdpSessOverloadState_Type = TruthValue
_VRtrLdpSessOverloadState_Object = MibScalar
vRtrLdpSessOverloadState = _VRtrLdpSessOverloadState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 17, 7),
    _VRtrLdpSessOverloadState_Type()
)
vRtrLdpSessOverloadState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrLdpSessOverloadState.setStatus("obsolete")


class _VRtrLdpSessOverloadDirection_Type(Integer32):
    """Custom type vRtrLdpSessOverloadDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sent", 1),
          ("received", 2))
    )


_VRtrLdpSessOverloadDirection_Type.__name__ = "Integer32"
_VRtrLdpSessOverloadDirection_Object = MibScalar
vRtrLdpSessOverloadDirection = _VRtrLdpSessOverloadDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 17, 8),
    _VRtrLdpSessOverloadDirection_Type()
)
vRtrLdpSessOverloadDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrLdpSessOverloadDirection.setStatus("obsolete")


class _VRtrLdpSessOverloadFecType_Type(Integer32):
    """Custom type vRtrLdpSessOverloadFecType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("prefixes", 1),
          ("multicast", 2),
          ("services", 3))
    )


_VRtrLdpSessOverloadFecType_Type.__name__ = "Integer32"
_VRtrLdpSessOverloadFecType_Object = MibScalar
vRtrLdpSessOverloadFecType = _VRtrLdpSessOverloadFecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 17, 9),
    _VRtrLdpSessOverloadFecType_Type()
)
vRtrLdpSessOverloadFecType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrLdpSessOverloadFecType.setStatus("obsolete")


class _VRtrLdpSessOperThresLevel_Type(Integer32):
    """Custom type vRtrLdpSessOperThresLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1))
    )


_VRtrLdpSessOperThresLevel_Type.__name__ = "Integer32"
_VRtrLdpSessOperThresLevel_Object = MibScalar
vRtrLdpSessOperThresLevel = _VRtrLdpSessOperThresLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 17, 10),
    _VRtrLdpSessOperThresLevel_Type()
)
vRtrLdpSessOperThresLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrLdpSessOperThresLevel.setStatus("obsolete")
_VRtrLdpStaticFecTable_Object = MibTable
vRtrLdpStaticFecTable = _VRtrLdpStaticFecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 18)
)
if mibBuilder.loadTexts:
    vRtrLdpStaticFecTable.setStatus("obsolete")
_VRtrLdpStaticFecEntry_Object = MibTableRow
vRtrLdpStaticFecEntry = _VRtrLdpStaticFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 18, 1)
)
vRtrLdpStaticFecEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpStaticFecIpPrefix"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpStaticFecIpMask"),
)
if mibBuilder.loadTexts:
    vRtrLdpStaticFecEntry.setStatus("obsolete")
_VRtrLdpStaticFecIpPrefix_Type = IpAddress
_VRtrLdpStaticFecIpPrefix_Object = MibTableColumn
vRtrLdpStaticFecIpPrefix = _VRtrLdpStaticFecIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 18, 1, 1),
    _VRtrLdpStaticFecIpPrefix_Type()
)
vRtrLdpStaticFecIpPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecIpPrefix.setStatus("obsolete")
_VRtrLdpStaticFecIpMask_Type = IpAddress
_VRtrLdpStaticFecIpMask_Object = MibTableColumn
vRtrLdpStaticFecIpMask = _VRtrLdpStaticFecIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 18, 1, 2),
    _VRtrLdpStaticFecIpMask_Type()
)
vRtrLdpStaticFecIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecIpMask.setStatus("obsolete")
_VRtrLdpStaticFecRowStatus_Type = RowStatus
_VRtrLdpStaticFecRowStatus_Object = MibTableColumn
vRtrLdpStaticFecRowStatus = _VRtrLdpStaticFecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 18, 1, 3),
    _VRtrLdpStaticFecRowStatus_Type()
)
vRtrLdpStaticFecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecRowStatus.setStatus("obsolete")
_VRtrLdpStaticFecNextNHIndex_Type = Unsigned32
_VRtrLdpStaticFecNextNHIndex_Object = MibTableColumn
vRtrLdpStaticFecNextNHIndex = _VRtrLdpStaticFecNextNHIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 18, 1, 4),
    _VRtrLdpStaticFecNextNHIndex_Type()
)
vRtrLdpStaticFecNextNHIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNextNHIndex.setStatus("obsolete")


class _VRtrLdpStaticFecIngLabel_Type(Unsigned32):
    """Custom type vRtrLdpStaticFecIngLabel based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 262112),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_VRtrLdpStaticFecIngLabel_Type.__name__ = "Unsigned32"
_VRtrLdpStaticFecIngLabel_Object = MibTableColumn
vRtrLdpStaticFecIngLabel = _VRtrLdpStaticFecIngLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 18, 1, 5),
    _VRtrLdpStaticFecIngLabel_Type()
)
vRtrLdpStaticFecIngLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecIngLabel.setStatus("obsolete")
_VRtrLdpStaticFecNumNH_Type = Gauge32
_VRtrLdpStaticFecNumNH_Object = MibTableColumn
vRtrLdpStaticFecNumNH = _VRtrLdpStaticFecNumNH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 18, 1, 6),
    _VRtrLdpStaticFecNumNH_Type()
)
vRtrLdpStaticFecNumNH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNumNH.setStatus("obsolete")
_VRtrLdpStaticFecOperIngLabel_Type = Unsigned32
_VRtrLdpStaticFecOperIngLabel_Object = MibTableColumn
vRtrLdpStaticFecOperIngLabel = _VRtrLdpStaticFecOperIngLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 18, 1, 7),
    _VRtrLdpStaticFecOperIngLabel_Type()
)
vRtrLdpStaticFecOperIngLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecOperIngLabel.setStatus("obsolete")
_VRtrLdpStaticFecNHTable_Object = MibTable
vRtrLdpStaticFecNHTable = _VRtrLdpStaticFecNHTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 19)
)
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNHTable.setStatus("obsolete")
_VRtrLdpStaticFecNHEntry_Object = MibTableRow
vRtrLdpStaticFecNHEntry = _VRtrLdpStaticFecNHEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 19, 1)
)
vRtrLdpStaticFecNHEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpStaticFecIpPrefix"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpStaticFecIpMask"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpStaticFecNHIndex"),
)
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNHEntry.setStatus("obsolete")
_VRtrLdpStaticFecNHIndex_Type = Unsigned32
_VRtrLdpStaticFecNHIndex_Object = MibTableColumn
vRtrLdpStaticFecNHIndex = _VRtrLdpStaticFecNHIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 19, 1, 1),
    _VRtrLdpStaticFecNHIndex_Type()
)
vRtrLdpStaticFecNHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNHIndex.setStatus("obsolete")
_VRtrLdpStaticFecNHRowStatus_Type = RowStatus
_VRtrLdpStaticFecNHRowStatus_Object = MibTableColumn
vRtrLdpStaticFecNHRowStatus = _VRtrLdpStaticFecNHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 19, 1, 2),
    _VRtrLdpStaticFecNHRowStatus_Type()
)
vRtrLdpStaticFecNHRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNHRowStatus.setStatus("obsolete")


class _VRtrLdpStaticFecNHType_Type(Integer32):
    """Custom type vRtrLdpStaticFecNHType based on Integer32"""
    defaultValue = 0

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
        *(("unknown", 0),
          ("ipAddress", 1),
          ("pop", 2),
          ("ifName", 3),
          ("ifNameAndIpAddress", 4))
    )


_VRtrLdpStaticFecNHType_Type.__name__ = "Integer32"
_VRtrLdpStaticFecNHType_Object = MibTableColumn
vRtrLdpStaticFecNHType = _VRtrLdpStaticFecNHType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 19, 1, 3),
    _VRtrLdpStaticFecNHType_Type()
)
vRtrLdpStaticFecNHType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNHType.setStatus("obsolete")


class _VRtrLdpStaticFecNHIpAddr_Type(IpAddress):
    """Custom type vRtrLdpStaticFecNHIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_VRtrLdpStaticFecNHIpAddr_Type.__name__ = "IpAddress"
_VRtrLdpStaticFecNHIpAddr_Object = MibTableColumn
vRtrLdpStaticFecNHIpAddr = _VRtrLdpStaticFecNHIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 19, 1, 4),
    _VRtrLdpStaticFecNHIpAddr_Type()
)
vRtrLdpStaticFecNHIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNHIpAddr.setStatus("obsolete")


class _VRtrLdpStaticFecNHEgrLabel_Type(Unsigned32):
    """Custom type vRtrLdpStaticFecNHEgrLabel based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_VRtrLdpStaticFecNHEgrLabel_Type.__name__ = "Unsigned32"
_VRtrLdpStaticFecNHEgrLabel_Object = MibTableColumn
vRtrLdpStaticFecNHEgrLabel = _VRtrLdpStaticFecNHEgrLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 19, 1, 5),
    _VRtrLdpStaticFecNHEgrLabel_Type()
)
vRtrLdpStaticFecNHEgrLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNHEgrLabel.setStatus("obsolete")


class _VRtrLdpStaticFecNHIfName_Type(DisplayString):
    """Custom type vRtrLdpStaticFecNHIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VRtrLdpStaticFecNHIfName_Type.__name__ = "DisplayString"
_VRtrLdpStaticFecNHIfName_Object = MibTableColumn
vRtrLdpStaticFecNHIfName = _VRtrLdpStaticFecNHIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 19, 1, 6),
    _VRtrLdpStaticFecNHIfName_Type()
)
vRtrLdpStaticFecNHIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNHIfName.setStatus("obsolete")
_VRtrLdpTargTable_Object = MibTable
vRtrLdpTargTable = _VRtrLdpTargTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20)
)
if mibBuilder.loadTexts:
    vRtrLdpTargTable.setStatus("obsolete")
_VRtrLdpTargEntry_Object = MibTableRow
vRtrLdpTargEntry = _VRtrLdpTargEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpTargEntry.setStatus("obsolete")


class _VRtrLdpTargImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpTargImportPolicy1_Object = MibTableColumn
vRtrLdpTargImportPolicy1 = _VRtrLdpTargImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 3),
    _VRtrLdpTargImportPolicy1_Type()
)
vRtrLdpTargImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargImportPolicy1.setStatus("obsolete")


class _VRtrLdpTargImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpTargImportPolicy2_Object = MibTableColumn
vRtrLdpTargImportPolicy2 = _VRtrLdpTargImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 4),
    _VRtrLdpTargImportPolicy2_Type()
)
vRtrLdpTargImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargImportPolicy2.setStatus("obsolete")


class _VRtrLdpTargImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpTargImportPolicy3_Object = MibTableColumn
vRtrLdpTargImportPolicy3 = _VRtrLdpTargImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 5),
    _VRtrLdpTargImportPolicy3_Type()
)
vRtrLdpTargImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargImportPolicy3.setStatus("obsolete")


class _VRtrLdpTargImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpTargImportPolicy4_Object = MibTableColumn
vRtrLdpTargImportPolicy4 = _VRtrLdpTargImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 6),
    _VRtrLdpTargImportPolicy4_Type()
)
vRtrLdpTargImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargImportPolicy4.setStatus("obsolete")


class _VRtrLdpTargImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpTargImportPolicy5_Object = MibTableColumn
vRtrLdpTargImportPolicy5 = _VRtrLdpTargImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 7),
    _VRtrLdpTargImportPolicy5_Type()
)
vRtrLdpTargImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargImportPolicy5.setStatus("obsolete")


class _VRtrLdpTargExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpTargExportPolicy1_Object = MibTableColumn
vRtrLdpTargExportPolicy1 = _VRtrLdpTargExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 8),
    _VRtrLdpTargExportPolicy1_Type()
)
vRtrLdpTargExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargExportPolicy1.setStatus("obsolete")


class _VRtrLdpTargExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpTargExportPolicy2_Object = MibTableColumn
vRtrLdpTargExportPolicy2 = _VRtrLdpTargExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 9),
    _VRtrLdpTargExportPolicy2_Type()
)
vRtrLdpTargExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargExportPolicy2.setStatus("obsolete")


class _VRtrLdpTargExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpTargExportPolicy3_Object = MibTableColumn
vRtrLdpTargExportPolicy3 = _VRtrLdpTargExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 10),
    _VRtrLdpTargExportPolicy3_Type()
)
vRtrLdpTargExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargExportPolicy3.setStatus("obsolete")


class _VRtrLdpTargExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpTargExportPolicy4_Object = MibTableColumn
vRtrLdpTargExportPolicy4 = _VRtrLdpTargExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 11),
    _VRtrLdpTargExportPolicy4_Type()
)
vRtrLdpTargExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargExportPolicy4.setStatus("obsolete")


class _VRtrLdpTargExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpTargExportPolicy5_Object = MibTableColumn
vRtrLdpTargExportPolicy5 = _VRtrLdpTargExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 12),
    _VRtrLdpTargExportPolicy5_Type()
)
vRtrLdpTargExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargExportPolicy5.setStatus("obsolete")


class _VRtrLdpTargTunnelPreference_Type(TruthValue):
    """Custom type vRtrLdpTargTunnelPreference based on TruthValue"""
    defaultValue = 1


_VRtrLdpTargTunnelPreference_Type.__name__ = "TruthValue"
_VRtrLdpTargTunnelPreference_Object = MibTableColumn
vRtrLdpTargTunnelPreference = _VRtrLdpTargTunnelPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 13),
    _VRtrLdpTargTunnelPreference_Type()
)
vRtrLdpTargTunnelPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargTunnelPreference.setStatus("obsolete")
_VRtrLdpIfTunnelingLspTable_Object = MibTable
vRtrLdpIfTunnelingLspTable = _VRtrLdpIfTunnelingLspTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 21)
)
if mibBuilder.loadTexts:
    vRtrLdpIfTunnelingLspTable.setStatus("obsolete")
_VRtrLdpIfTunnelingLspEntry_Object = MibTableRow
vRtrLdpIfTunnelingLspEntry = _VRtrLdpIfTunnelingLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 21, 1)
)
vRtrLdpIfTunnelingLspEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpIfIndex"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerAddress"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpIfLspId"),
)
if mibBuilder.loadTexts:
    vRtrLdpIfTunnelingLspEntry.setStatus("obsolete")
_VRtrLdpIfLspId_Type = TmnxVRtrMplsLspID
_VRtrLdpIfLspId_Object = MibTableColumn
vRtrLdpIfLspId = _VRtrLdpIfLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 21, 1, 1),
    _VRtrLdpIfLspId_Type()
)
vRtrLdpIfLspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpIfLspId.setStatus("obsolete")
_VRtrLdpIfLspRowStatus_Type = RowStatus
_VRtrLdpIfLspRowStatus_Object = MibTableColumn
vRtrLdpIfLspRowStatus = _VRtrLdpIfLspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 21, 1, 2),
    _VRtrLdpIfLspRowStatus_Type()
)
vRtrLdpIfLspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfLspRowStatus.setStatus("obsolete")
_VRtrLdpCepTdmFecTable_Object = MibTable
vRtrLdpCepTdmFecTable = _VRtrLdpCepTdmFecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22)
)
if mibBuilder.loadTexts:
    vRtrLdpCepTdmFecTable.setStatus("obsolete")
_VRtrLdpCepTdmFecEntry_Object = MibTableRow
vRtrLdpCepTdmFecEntry = _VRtrLdpCepTdmFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpCepTdmFecEntry.setStatus("obsolete")
_VRtrLdpCepTdmLocalPayloadSize_Type = Unsigned32
_VRtrLdpCepTdmLocalPayloadSize_Object = MibTableColumn
vRtrLdpCepTdmLocalPayloadSize = _VRtrLdpCepTdmLocalPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 4),
    _VRtrLdpCepTdmLocalPayloadSize_Type()
)
vRtrLdpCepTdmLocalPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalPayloadSize.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalPayloadSize.setUnits("bytes")
_VRtrLdpCepTdmRemotePayloadSize_Type = Unsigned32
_VRtrLdpCepTdmRemotePayloadSize_Object = MibTableColumn
vRtrLdpCepTdmRemotePayloadSize = _VRtrLdpCepTdmRemotePayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 5),
    _VRtrLdpCepTdmRemotePayloadSize_Type()
)
vRtrLdpCepTdmRemotePayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemotePayloadSize.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemotePayloadSize.setUnits("bytes")
_VRtrLdpCepTdmLocalBitrate_Type = Unsigned32
_VRtrLdpCepTdmLocalBitrate_Object = MibTableColumn
vRtrLdpCepTdmLocalBitrate = _VRtrLdpCepTdmLocalBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 6),
    _VRtrLdpCepTdmLocalBitrate_Type()
)
vRtrLdpCepTdmLocalBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalBitrate.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalBitrate.setUnits("sixty-four kilobps")
_VRtrLdpCepTdmRemoteBitrate_Type = Unsigned32
_VRtrLdpCepTdmRemoteBitrate_Object = MibTableColumn
vRtrLdpCepTdmRemoteBitrate = _VRtrLdpCepTdmRemoteBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 7),
    _VRtrLdpCepTdmRemoteBitrate_Type()
)
vRtrLdpCepTdmRemoteBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemoteBitrate.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemoteBitrate.setUnits("sixty-four kilobps")
_VRtrLdpCepTdmLocalRtpHeader_Type = TruthValue
_VRtrLdpCepTdmLocalRtpHeader_Object = MibTableColumn
vRtrLdpCepTdmLocalRtpHeader = _VRtrLdpCepTdmLocalRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 8),
    _VRtrLdpCepTdmLocalRtpHeader_Type()
)
vRtrLdpCepTdmLocalRtpHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalRtpHeader.setStatus("obsolete")
_VRtrLdpCepTdmRemoteRtpHeader_Type = TruthValue
_VRtrLdpCepTdmRemoteRtpHeader_Object = MibTableColumn
vRtrLdpCepTdmRemoteRtpHeader = _VRtrLdpCepTdmRemoteRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 9),
    _VRtrLdpCepTdmRemoteRtpHeader_Type()
)
vRtrLdpCepTdmRemoteRtpHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemoteRtpHeader.setStatus("obsolete")
_VRtrLdpCepTdmLocalDiffTimestamp_Type = TruthValue
_VRtrLdpCepTdmLocalDiffTimestamp_Object = MibTableColumn
vRtrLdpCepTdmLocalDiffTimestamp = _VRtrLdpCepTdmLocalDiffTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 10),
    _VRtrLdpCepTdmLocalDiffTimestamp_Type()
)
vRtrLdpCepTdmLocalDiffTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalDiffTimestamp.setStatus("obsolete")
_VRtrLdpCepTdmRemoteDiffTimestamp_Type = TruthValue
_VRtrLdpCepTdmRemoteDiffTimestamp_Object = MibTableColumn
vRtrLdpCepTdmRemoteDiffTimestamp = _VRtrLdpCepTdmRemoteDiffTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 11),
    _VRtrLdpCepTdmRemoteDiffTimestamp_Type()
)
vRtrLdpCepTdmRemoteDiffTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemoteDiffTimestamp.setStatus("obsolete")
_VRtrLdpCepTdmLocalSigPkts_Type = TdmOptionsSigPkts
_VRtrLdpCepTdmLocalSigPkts_Object = MibTableColumn
vRtrLdpCepTdmLocalSigPkts = _VRtrLdpCepTdmLocalSigPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 12),
    _VRtrLdpCepTdmLocalSigPkts_Type()
)
vRtrLdpCepTdmLocalSigPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalSigPkts.setStatus("obsolete")
_VRtrLdpCepTdmRemoteSigPkts_Type = TdmOptionsSigPkts
_VRtrLdpCepTdmRemoteSigPkts_Object = MibTableColumn
vRtrLdpCepTdmRemoteSigPkts = _VRtrLdpCepTdmRemoteSigPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 13),
    _VRtrLdpCepTdmRemoteSigPkts_Type()
)
vRtrLdpCepTdmRemoteSigPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemoteSigPkts.setStatus("obsolete")
_VRtrLdpCepTdmLocalCasTrunk_Type = TdmOptionsCasTrunkFraming
_VRtrLdpCepTdmLocalCasTrunk_Object = MibTableColumn
vRtrLdpCepTdmLocalCasTrunk = _VRtrLdpCepTdmLocalCasTrunk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 14),
    _VRtrLdpCepTdmLocalCasTrunk_Type()
)
vRtrLdpCepTdmLocalCasTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalCasTrunk.setStatus("obsolete")
_VRtrLdpCepTdmRemoteCasTrunk_Type = TdmOptionsCasTrunkFraming
_VRtrLdpCepTdmRemoteCasTrunk_Object = MibTableColumn
vRtrLdpCepTdmRemoteCasTrunk = _VRtrLdpCepTdmRemoteCasTrunk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 15),
    _VRtrLdpCepTdmRemoteCasTrunk_Type()
)
vRtrLdpCepTdmRemoteCasTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemoteCasTrunk.setStatus("obsolete")
_VRtrLdpCepTdmLocalTimestampFreq_Type = Unsigned32
_VRtrLdpCepTdmLocalTimestampFreq_Object = MibTableColumn
vRtrLdpCepTdmLocalTimestampFreq = _VRtrLdpCepTdmLocalTimestampFreq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 16),
    _VRtrLdpCepTdmLocalTimestampFreq_Type()
)
vRtrLdpCepTdmLocalTimestampFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalTimestampFreq.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalTimestampFreq.setUnits("8 KHz")
_VRtrLdpCepTdmRemoteTimestampFreq_Type = Unsigned32
_VRtrLdpCepTdmRemoteTimestampFreq_Object = MibTableColumn
vRtrLdpCepTdmRemoteTimestampFreq = _VRtrLdpCepTdmRemoteTimestampFreq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 17),
    _VRtrLdpCepTdmRemoteTimestampFreq_Type()
)
vRtrLdpCepTdmRemoteTimestampFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemoteTimestampFreq.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemoteTimestampFreq.setUnits("8 KHz")
_VRtrLdpCepTdmLocalPayloadType_Type = Unsigned32
_VRtrLdpCepTdmLocalPayloadType_Object = MibTableColumn
vRtrLdpCepTdmLocalPayloadType = _VRtrLdpCepTdmLocalPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 18),
    _VRtrLdpCepTdmLocalPayloadType_Type()
)
vRtrLdpCepTdmLocalPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalPayloadType.setStatus("obsolete")
_VRtrLdpCepTdmRemotePayloadType_Type = Unsigned32
_VRtrLdpCepTdmRemotePayloadType_Object = MibTableColumn
vRtrLdpCepTdmRemotePayloadType = _VRtrLdpCepTdmRemotePayloadType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 19),
    _VRtrLdpCepTdmRemotePayloadType_Type()
)
vRtrLdpCepTdmRemotePayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemotePayloadType.setStatus("obsolete")
_VRtrLdpCepTdmLocalSsrcId_Type = Unsigned32
_VRtrLdpCepTdmLocalSsrcId_Object = MibTableColumn
vRtrLdpCepTdmLocalSsrcId = _VRtrLdpCepTdmLocalSsrcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 20),
    _VRtrLdpCepTdmLocalSsrcId_Type()
)
vRtrLdpCepTdmLocalSsrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalSsrcId.setStatus("obsolete")
_VRtrLdpCepTdmRemoteSsrcId_Type = Unsigned32
_VRtrLdpCepTdmRemoteSsrcId_Object = MibTableColumn
vRtrLdpCepTdmRemoteSsrcId = _VRtrLdpCepTdmRemoteSsrcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 21),
    _VRtrLdpCepTdmRemoteSsrcId_Type()
)
vRtrLdpCepTdmRemoteSsrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemoteSsrcId.setStatus("obsolete")
_VLdpServFec129Table_Object = MibTable
vLdpServFec129Table = _VLdpServFec129Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23)
)
if mibBuilder.loadTexts:
    vLdpServFec129Table.setStatus("obsolete")
_VLdpServFec129Entry_Object = MibTableRow
vLdpServFec129Entry = _VLdpServFec129Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1)
)
vLdpServFec129Entry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpServFecVcType"),
    (0, "TIMETRA-LDP-MIB", "vLdpServFec129AgiTlv"),
    (0, "TIMETRA-LDP-MIB", "vLdpServFec129SrcAiiTlv"),
    (0, "TIMETRA-LDP-MIB", "vLdpServFec129TgtAiiTlv"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    vLdpServFec129Entry.setStatus("obsolete")
_VLdpServFec129AgiTlv_Type = TmnxLdpFec129Tlv
_VLdpServFec129AgiTlv_Object = MibTableColumn
vLdpServFec129AgiTlv = _VLdpServFec129AgiTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 1),
    _VLdpServFec129AgiTlv_Type()
)
vLdpServFec129AgiTlv.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpServFec129AgiTlv.setStatus("obsolete")
_VLdpServFec129SrcAiiTlv_Type = TmnxLdpFec129Tlv
_VLdpServFec129SrcAiiTlv_Object = MibTableColumn
vLdpServFec129SrcAiiTlv = _VLdpServFec129SrcAiiTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 2),
    _VLdpServFec129SrcAiiTlv_Type()
)
vLdpServFec129SrcAiiTlv.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpServFec129SrcAiiTlv.setStatus("obsolete")
_VLdpServFec129TgtAiiTlv_Type = TmnxLdpFec129Tlv
_VLdpServFec129TgtAiiTlv_Object = MibTableColumn
vLdpServFec129TgtAiiTlv = _VLdpServFec129TgtAiiTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 3),
    _VLdpServFec129TgtAiiTlv_Type()
)
vLdpServFec129TgtAiiTlv.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpServFec129TgtAiiTlv.setStatus("obsolete")
_VLdpServFec129ServType_Type = ServType
_VLdpServFec129ServType_Object = MibTableColumn
vLdpServFec129ServType = _VLdpServFec129ServType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 4),
    _VLdpServFec129ServType_Type()
)
vLdpServFec129ServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129ServType.setStatus("obsolete")


class _VLdpServFec129ServId_Type(TmnxServId):
    """Custom type vLdpServFec129ServId based on TmnxServId"""
    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VLdpServFec129ServId_Type.__name__ = "TmnxServId"
_VLdpServFec129ServId_Object = MibTableColumn
vLdpServFec129ServId = _VLdpServFec129ServId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 5),
    _VLdpServFec129ServId_Type()
)
vLdpServFec129ServId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129ServId.setStatus("obsolete")
_VLdpServFec129VpnId_Type = TmnxVpnId
_VLdpServFec129VpnId_Object = MibTableColumn
vLdpServFec129VpnId = _VLdpServFec129VpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 6),
    _VLdpServFec129VpnId_Type()
)
vLdpServFec129VpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129VpnId.setStatus("obsolete")
_VLdpServFec129Flags_Type = TmnxLdpFECFlags
_VLdpServFec129Flags_Object = MibTableColumn
vLdpServFec129Flags = _VLdpServFec129Flags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 7),
    _VLdpServFec129Flags_Type()
)
vLdpServFec129Flags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129Flags.setStatus("obsolete")
_VLdpServFec129NumInLabels_Type = Unsigned32
_VLdpServFec129NumInLabels_Object = MibTableColumn
vLdpServFec129NumInLabels = _VLdpServFec129NumInLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 8),
    _VLdpServFec129NumInLabels_Type()
)
vLdpServFec129NumInLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129NumInLabels.setStatus("obsolete")
_VLdpServFec129NumOutLabels_Type = Unsigned32
_VLdpServFec129NumOutLabels_Object = MibTableColumn
vLdpServFec129NumOutLabels = _VLdpServFec129NumOutLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 9),
    _VLdpServFec129NumOutLabels_Type()
)
vLdpServFec129NumOutLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129NumOutLabels.setStatus("obsolete")
_VLdpServFec129InLabel1_Type = Unsigned32
_VLdpServFec129InLabel1_Object = MibTableColumn
vLdpServFec129InLabel1 = _VLdpServFec129InLabel1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 10),
    _VLdpServFec129InLabel1_Type()
)
vLdpServFec129InLabel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129InLabel1.setStatus("obsolete")
_VLdpServFec129InLabelStatus1_Type = TmnxLabelStatus
_VLdpServFec129InLabelStatus1_Object = MibTableColumn
vLdpServFec129InLabelStatus1 = _VLdpServFec129InLabelStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 11),
    _VLdpServFec129InLabelStatus1_Type()
)
vLdpServFec129InLabelStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129InLabelStatus1.setStatus("obsolete")
_VLdpServFec129OutLabel1_Type = Unsigned32
_VLdpServFec129OutLabel1_Object = MibTableColumn
vLdpServFec129OutLabel1 = _VLdpServFec129OutLabel1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 20),
    _VLdpServFec129OutLabel1_Type()
)
vLdpServFec129OutLabel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129OutLabel1.setStatus("obsolete")
_VLdpServFec129OutLabelStatus1_Type = TmnxLabelStatus
_VLdpServFec129OutLabelStatus1_Object = MibTableColumn
vLdpServFec129OutLabelStatus1 = _VLdpServFec129OutLabelStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 21),
    _VLdpServFec129OutLabelStatus1_Type()
)
vLdpServFec129OutLabelStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129OutLabelStatus1.setStatus("obsolete")
_VLdpServFec129SdpId_Type = SdpId
_VLdpServFec129SdpId_Object = MibTableColumn
vLdpServFec129SdpId = _VLdpServFec129SdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 22),
    _VLdpServFec129SdpId_Type()
)
vLdpServFec129SdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129SdpId.setStatus("obsolete")
_VLdpServFec129LocalMTU_Type = Unsigned32
_VLdpServFec129LocalMTU_Object = MibTableColumn
vLdpServFec129LocalMTU = _VLdpServFec129LocalMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 23),
    _VLdpServFec129LocalMTU_Type()
)
vLdpServFec129LocalMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129LocalMTU.setStatus("obsolete")
_VLdpServFec129RemoteMTU_Type = Unsigned32
_VLdpServFec129RemoteMTU_Object = MibTableColumn
vLdpServFec129RemoteMTU = _VLdpServFec129RemoteMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 24),
    _VLdpServFec129RemoteMTU_Type()
)
vLdpServFec129RemoteMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129RemoteMTU.setStatus("obsolete")
_VLdpServFec129LocalVlanTag_Type = Unsigned32
_VLdpServFec129LocalVlanTag_Object = MibTableColumn
vLdpServFec129LocalVlanTag = _VLdpServFec129LocalVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 25),
    _VLdpServFec129LocalVlanTag_Type()
)
vLdpServFec129LocalVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129LocalVlanTag.setStatus("obsolete")
_VLdpServFec129RemoteVlanTag_Type = Unsigned32
_VLdpServFec129RemoteVlanTag_Object = MibTableColumn
vLdpServFec129RemoteVlanTag = _VLdpServFec129RemoteVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 26),
    _VLdpServFec129RemoteVlanTag_Type()
)
vLdpServFec129RemoteVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129RemoteVlanTag.setStatus("obsolete")
_VLdpServFec129LocalMaxCellConcat_Type = Unsigned32
_VLdpServFec129LocalMaxCellConcat_Object = MibTableColumn
vLdpServFec129LocalMaxCellConcat = _VLdpServFec129LocalMaxCellConcat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 27),
    _VLdpServFec129LocalMaxCellConcat_Type()
)
vLdpServFec129LocalMaxCellConcat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129LocalMaxCellConcat.setStatus("obsolete")
_VLdpServFec129RemoteMaxCellConcat_Type = Unsigned32
_VLdpServFec129RemoteMaxCellConcat_Object = MibTableColumn
vLdpServFec129RemoteMaxCellConcat = _VLdpServFec129RemoteMaxCellConcat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 28),
    _VLdpServFec129RemoteMaxCellConcat_Type()
)
vLdpServFec129RemoteMaxCellConcat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129RemoteMaxCellConcat.setStatus("obsolete")
_VLdpServFec129InLabelSigStatus1_Type = TmnxLabelSigStatus
_VLdpServFec129InLabelSigStatus1_Object = MibTableColumn
vLdpServFec129InLabelSigStatus1 = _VLdpServFec129InLabelSigStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 29),
    _VLdpServFec129InLabelSigStatus1_Type()
)
vLdpServFec129InLabelSigStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129InLabelSigStatus1.setStatus("obsolete")
_VLdpServFec129OutLabelSigStatus1_Type = TmnxLabelSigStatus
_VLdpServFec129OutLabelSigStatus1_Object = MibTableColumn
vLdpServFec129OutLabelSigStatus1 = _VLdpServFec129OutLabelSigStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 30),
    _VLdpServFec129OutLabelSigStatus1_Type()
)
vLdpServFec129OutLabelSigStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129OutLabelSigStatus1.setStatus("obsolete")
_VLdpServFec129LocalIpv4Capblty_Type = TruthValue
_VLdpServFec129LocalIpv4Capblty_Object = MibTableColumn
vLdpServFec129LocalIpv4Capblty = _VLdpServFec129LocalIpv4Capblty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 31),
    _VLdpServFec129LocalIpv4Capblty_Type()
)
vLdpServFec129LocalIpv4Capblty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129LocalIpv4Capblty.setStatus("obsolete")
_VLdpServFec129RemoteIpv4Capblty_Type = TruthValue
_VLdpServFec129RemoteIpv4Capblty_Object = MibTableColumn
vLdpServFec129RemoteIpv4Capblty = _VLdpServFec129RemoteIpv4Capblty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 32),
    _VLdpServFec129RemoteIpv4Capblty_Type()
)
vLdpServFec129RemoteIpv4Capblty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129RemoteIpv4Capblty.setStatus("obsolete")
_VLdpServFec129LocalIpv6Capblty_Type = TruthValue
_VLdpServFec129LocalIpv6Capblty_Object = MibTableColumn
vLdpServFec129LocalIpv6Capblty = _VLdpServFec129LocalIpv6Capblty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 33),
    _VLdpServFec129LocalIpv6Capblty_Type()
)
vLdpServFec129LocalIpv6Capblty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129LocalIpv6Capblty.setStatus("obsolete")
_VLdpServFec129RemoteIpv6Capblty_Type = TruthValue
_VLdpServFec129RemoteIpv6Capblty_Object = MibTableColumn
vLdpServFec129RemoteIpv6Capblty = _VLdpServFec129RemoteIpv6Capblty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 34),
    _VLdpServFec129RemoteIpv6Capblty_Type()
)
vLdpServFec129RemoteIpv6Capblty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129RemoteIpv6Capblty.setStatus("obsolete")
_VLdpServFec129LocalIpv4CeIpAddr_Type = IpAddress
_VLdpServFec129LocalIpv4CeIpAddr_Object = MibTableColumn
vLdpServFec129LocalIpv4CeIpAddr = _VLdpServFec129LocalIpv4CeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 35),
    _VLdpServFec129LocalIpv4CeIpAddr_Type()
)
vLdpServFec129LocalIpv4CeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129LocalIpv4CeIpAddr.setStatus("obsolete")
_VLdpServFec129RemoteIpv4CeIpAddr_Type = IpAddress
_VLdpServFec129RemoteIpv4CeIpAddr_Object = MibTableColumn
vLdpServFec129RemoteIpv4CeIpAddr = _VLdpServFec129RemoteIpv4CeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 36),
    _VLdpServFec129RemoteIpv4CeIpAddr_Type()
)
vLdpServFec129RemoteIpv4CeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129RemoteIpv4CeIpAddr.setStatus("obsolete")
_VLdpServFec129InLbl1WdwReason_Type = TmnxLdpInLblWdrawalReasonCode
_VLdpServFec129InLbl1WdwReason_Object = MibTableColumn
vLdpServFec129InLbl1WdwReason = _VLdpServFec129InLbl1WdwReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 37),
    _VLdpServFec129InLbl1WdwReason_Type()
)
vLdpServFec129InLbl1WdwReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129InLbl1WdwReason.setStatus("obsolete")
_VLdpServFec129LocalFLTxCapblty_Type = TruthValue
_VLdpServFec129LocalFLTxCapblty_Object = MibTableColumn
vLdpServFec129LocalFLTxCapblty = _VLdpServFec129LocalFLTxCapblty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 38),
    _VLdpServFec129LocalFLTxCapblty_Type()
)
vLdpServFec129LocalFLTxCapblty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129LocalFLTxCapblty.setStatus("obsolete")
_VLdpServFec129LocalFLRxCapblty_Type = TruthValue
_VLdpServFec129LocalFLRxCapblty_Object = MibTableColumn
vLdpServFec129LocalFLRxCapblty = _VLdpServFec129LocalFLRxCapblty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 39),
    _VLdpServFec129LocalFLRxCapblty_Type()
)
vLdpServFec129LocalFLRxCapblty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129LocalFLRxCapblty.setStatus("obsolete")
_VLdpServFec129RemoteFLTxCapblty_Type = TruthValue
_VLdpServFec129RemoteFLTxCapblty_Object = MibTableColumn
vLdpServFec129RemoteFLTxCapblty = _VLdpServFec129RemoteFLTxCapblty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 40),
    _VLdpServFec129RemoteFLTxCapblty_Type()
)
vLdpServFec129RemoteFLTxCapblty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129RemoteFLTxCapblty.setStatus("obsolete")
_VLdpServFec129RemoteFLRxCapblty_Type = TruthValue
_VLdpServFec129RemoteFLRxCapblty_Object = MibTableColumn
vLdpServFec129RemoteFLRxCapblty = _VLdpServFec129RemoteFLRxCapblty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 41),
    _VLdpServFec129RemoteFLRxCapblty_Type()
)
vLdpServFec129RemoteFLRxCapblty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129RemoteFLRxCapblty.setStatus("obsolete")
_VLdpServFec129MateAgiTlv_Type = TmnxLdpFec129Tlv
_VLdpServFec129MateAgiTlv_Object = MibTableColumn
vLdpServFec129MateAgiTlv = _VLdpServFec129MateAgiTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 42),
    _VLdpServFec129MateAgiTlv_Type()
)
vLdpServFec129MateAgiTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129MateAgiTlv.setStatus("obsolete")
_VLdpServFec129MateSrcAiiTlv_Type = TmnxLdpFec129Tlv
_VLdpServFec129MateSrcAiiTlv_Object = MibTableColumn
vLdpServFec129MateSrcAiiTlv = _VLdpServFec129MateSrcAiiTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 43),
    _VLdpServFec129MateSrcAiiTlv_Type()
)
vLdpServFec129MateSrcAiiTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129MateSrcAiiTlv.setStatus("obsolete")
_VLdpServFec129MateTgtAiiTlv_Type = TmnxLdpFec129Tlv
_VLdpServFec129MateTgtAiiTlv_Object = MibTableColumn
vLdpServFec129MateTgtAiiTlv = _VLdpServFec129MateTgtAiiTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 44),
    _VLdpServFec129MateTgtAiiTlv_Type()
)
vLdpServFec129MateTgtAiiTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129MateTgtAiiTlv.setStatus("obsolete")
_VLdpServFec129MateSdpId_Type = SdpId
_VLdpServFec129MateSdpId_Object = MibTableColumn
vLdpServFec129MateSdpId = _VLdpServFec129MateSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 45),
    _VLdpServFec129MateSdpId_Type()
)
vLdpServFec129MateSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129MateSdpId.setStatus("obsolete")
_VLdpServFec129MapTable_Object = MibTable
vLdpServFec129MapTable = _VLdpServFec129MapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 24)
)
if mibBuilder.loadTexts:
    vLdpServFec129MapTable.setStatus("obsolete")
_VLdpServFec129MapEntry_Object = MibTableRow
vLdpServFec129MapEntry = _VLdpServFec129MapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 24, 1)
)
vLdpServFec129MapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "TIMETRA-LDP-MIB", "vLdpServFec129MapVcType"),
    (0, "TIMETRA-LDP-MIB", "vLdpServFec129MapAgiTlv"),
    (0, "TIMETRA-LDP-MIB", "vLdpServFec129MapSrcAiiTlv"),
    (0, "TIMETRA-LDP-MIB", "vLdpServFec129MapTgtAiiTlv"),
)
if mibBuilder.loadTexts:
    vLdpServFec129MapEntry.setStatus("obsolete")
_VLdpServFec129MapVcType_Type = TmnxVcType
_VLdpServFec129MapVcType_Object = MibTableColumn
vLdpServFec129MapVcType = _VLdpServFec129MapVcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 24, 1, 1),
    _VLdpServFec129MapVcType_Type()
)
vLdpServFec129MapVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129MapVcType.setStatus("obsolete")
_VLdpServFec129MapAgiTlv_Type = TmnxLdpFec129Tlv
_VLdpServFec129MapAgiTlv_Object = MibTableColumn
vLdpServFec129MapAgiTlv = _VLdpServFec129MapAgiTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 24, 1, 2),
    _VLdpServFec129MapAgiTlv_Type()
)
vLdpServFec129MapAgiTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129MapAgiTlv.setStatus("obsolete")
_VLdpServFec129MapSrcAiiTlv_Type = TmnxLdpFec129Tlv
_VLdpServFec129MapSrcAiiTlv_Object = MibTableColumn
vLdpServFec129MapSrcAiiTlv = _VLdpServFec129MapSrcAiiTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 24, 1, 3),
    _VLdpServFec129MapSrcAiiTlv_Type()
)
vLdpServFec129MapSrcAiiTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129MapSrcAiiTlv.setStatus("obsolete")
_VLdpServFec129MapTgtAiiTlv_Type = TmnxLdpFec129Tlv
_VLdpServFec129MapTgtAiiTlv_Object = MibTableColumn
vLdpServFec129MapTgtAiiTlv = _VLdpServFec129MapTgtAiiTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 24, 1, 4),
    _VLdpServFec129MapTgtAiiTlv_Type()
)
vLdpServFec129MapTgtAiiTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129MapTgtAiiTlv.setStatus("obsolete")
_VLdpCepTdmFec129Table_Object = MibTable
vLdpCepTdmFec129Table = _VLdpCepTdmFec129Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25)
)
if mibBuilder.loadTexts:
    vLdpCepTdmFec129Table.setStatus("obsolete")
_VLdpCepTdmFec129Entry_Object = MibTableRow
vLdpCepTdmFec129Entry = _VLdpCepTdmFec129Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1)
)
if mibBuilder.loadTexts:
    vLdpCepTdmFec129Entry.setStatus("obsolete")
_VLdpCepTdmFec129LocalPayloadSize_Type = Unsigned32
_VLdpCepTdmFec129LocalPayloadSize_Object = MibTableColumn
vLdpCepTdmFec129LocalPayloadSize = _VLdpCepTdmFec129LocalPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 4),
    _VLdpCepTdmFec129LocalPayloadSize_Type()
)
vLdpCepTdmFec129LocalPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalPayloadSize.setStatus("obsolete")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalPayloadSize.setUnits("bytes")
_VLdpCepTdmFec129RemotePayloadSize_Type = Unsigned32
_VLdpCepTdmFec129RemotePayloadSize_Object = MibTableColumn
vLdpCepTdmFec129RemotePayloadSize = _VLdpCepTdmFec129RemotePayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 5),
    _VLdpCepTdmFec129RemotePayloadSize_Type()
)
vLdpCepTdmFec129RemotePayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemotePayloadSize.setStatus("obsolete")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemotePayloadSize.setUnits("bytes")
_VLdpCepTdmFec129LocalBitrate_Type = Unsigned32
_VLdpCepTdmFec129LocalBitrate_Object = MibTableColumn
vLdpCepTdmFec129LocalBitrate = _VLdpCepTdmFec129LocalBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 6),
    _VLdpCepTdmFec129LocalBitrate_Type()
)
vLdpCepTdmFec129LocalBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalBitrate.setStatus("obsolete")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalBitrate.setUnits("sixty-four kilobps")
_VLdpCepTdmFec129RemoteBitrate_Type = Unsigned32
_VLdpCepTdmFec129RemoteBitrate_Object = MibTableColumn
vLdpCepTdmFec129RemoteBitrate = _VLdpCepTdmFec129RemoteBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 7),
    _VLdpCepTdmFec129RemoteBitrate_Type()
)
vLdpCepTdmFec129RemoteBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemoteBitrate.setStatus("obsolete")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemoteBitrate.setUnits("sixty-four kilobps")
_VLdpCepTdmFec129LocalRtpHeader_Type = TruthValue
_VLdpCepTdmFec129LocalRtpHeader_Object = MibTableColumn
vLdpCepTdmFec129LocalRtpHeader = _VLdpCepTdmFec129LocalRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 8),
    _VLdpCepTdmFec129LocalRtpHeader_Type()
)
vLdpCepTdmFec129LocalRtpHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalRtpHeader.setStatus("obsolete")
_VLdpCepTdmFec129RemoteRtpHeader_Type = TruthValue
_VLdpCepTdmFec129RemoteRtpHeader_Object = MibTableColumn
vLdpCepTdmFec129RemoteRtpHeader = _VLdpCepTdmFec129RemoteRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 9),
    _VLdpCepTdmFec129RemoteRtpHeader_Type()
)
vLdpCepTdmFec129RemoteRtpHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemoteRtpHeader.setStatus("obsolete")
_VLdpCepTdmFec129LocalDiffTimestamp_Type = TruthValue
_VLdpCepTdmFec129LocalDiffTimestamp_Object = MibTableColumn
vLdpCepTdmFec129LocalDiffTimestamp = _VLdpCepTdmFec129LocalDiffTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 10),
    _VLdpCepTdmFec129LocalDiffTimestamp_Type()
)
vLdpCepTdmFec129LocalDiffTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalDiffTimestamp.setStatus("obsolete")
_VLdpCepTdmFec129RemoteDiffTimestamp_Type = TruthValue
_VLdpCepTdmFec129RemoteDiffTimestamp_Object = MibTableColumn
vLdpCepTdmFec129RemoteDiffTimestamp = _VLdpCepTdmFec129RemoteDiffTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 11),
    _VLdpCepTdmFec129RemoteDiffTimestamp_Type()
)
vLdpCepTdmFec129RemoteDiffTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemoteDiffTimestamp.setStatus("obsolete")
_VLdpCepTdmFec129LocalSigPkts_Type = TdmOptionsSigPkts
_VLdpCepTdmFec129LocalSigPkts_Object = MibTableColumn
vLdpCepTdmFec129LocalSigPkts = _VLdpCepTdmFec129LocalSigPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 12),
    _VLdpCepTdmFec129LocalSigPkts_Type()
)
vLdpCepTdmFec129LocalSigPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalSigPkts.setStatus("obsolete")
_VLdpCepTdmFec129RemoteSigPkts_Type = TdmOptionsSigPkts
_VLdpCepTdmFec129RemoteSigPkts_Object = MibTableColumn
vLdpCepTdmFec129RemoteSigPkts = _VLdpCepTdmFec129RemoteSigPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 13),
    _VLdpCepTdmFec129RemoteSigPkts_Type()
)
vLdpCepTdmFec129RemoteSigPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemoteSigPkts.setStatus("obsolete")
_VLdpCepTdmFec129LocalCasTrunk_Type = TdmOptionsCasTrunkFraming
_VLdpCepTdmFec129LocalCasTrunk_Object = MibTableColumn
vLdpCepTdmFec129LocalCasTrunk = _VLdpCepTdmFec129LocalCasTrunk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 14),
    _VLdpCepTdmFec129LocalCasTrunk_Type()
)
vLdpCepTdmFec129LocalCasTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalCasTrunk.setStatus("obsolete")
_VLdpCepTdmFec129RemoteCasTrunk_Type = TdmOptionsCasTrunkFraming
_VLdpCepTdmFec129RemoteCasTrunk_Object = MibTableColumn
vLdpCepTdmFec129RemoteCasTrunk = _VLdpCepTdmFec129RemoteCasTrunk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 15),
    _VLdpCepTdmFec129RemoteCasTrunk_Type()
)
vLdpCepTdmFec129RemoteCasTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemoteCasTrunk.setStatus("obsolete")
_VLdpCepTdmFec129LocalTimestampFreq_Type = Unsigned32
_VLdpCepTdmFec129LocalTimestampFreq_Object = MibTableColumn
vLdpCepTdmFec129LocalTimestampFreq = _VLdpCepTdmFec129LocalTimestampFreq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 16),
    _VLdpCepTdmFec129LocalTimestampFreq_Type()
)
vLdpCepTdmFec129LocalTimestampFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalTimestampFreq.setStatus("obsolete")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalTimestampFreq.setUnits("8 KHz")
_VLdpCepTdmFec129RemoteTimestampFreq_Type = Unsigned32
_VLdpCepTdmFec129RemoteTimestampFreq_Object = MibTableColumn
vLdpCepTdmFec129RemoteTimestampFreq = _VLdpCepTdmFec129RemoteTimestampFreq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 17),
    _VLdpCepTdmFec129RemoteTimestampFreq_Type()
)
vLdpCepTdmFec129RemoteTimestampFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemoteTimestampFreq.setStatus("obsolete")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemoteTimestampFreq.setUnits("8 KHz")
_VLdpCepTdmFec129LocalPayloadType_Type = Unsigned32
_VLdpCepTdmFec129LocalPayloadType_Object = MibTableColumn
vLdpCepTdmFec129LocalPayloadType = _VLdpCepTdmFec129LocalPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 18),
    _VLdpCepTdmFec129LocalPayloadType_Type()
)
vLdpCepTdmFec129LocalPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalPayloadType.setStatus("obsolete")
_VLdpCepTdmFec129RemotePayloadType_Type = Unsigned32
_VLdpCepTdmFec129RemotePayloadType_Object = MibTableColumn
vLdpCepTdmFec129RemotePayloadType = _VLdpCepTdmFec129RemotePayloadType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 19),
    _VLdpCepTdmFec129RemotePayloadType_Type()
)
vLdpCepTdmFec129RemotePayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemotePayloadType.setStatus("obsolete")
_VLdpCepTdmFec129LocalSsrcId_Type = Unsigned32
_VLdpCepTdmFec129LocalSsrcId_Object = MibTableColumn
vLdpCepTdmFec129LocalSsrcId = _VLdpCepTdmFec129LocalSsrcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 20),
    _VLdpCepTdmFec129LocalSsrcId_Type()
)
vLdpCepTdmFec129LocalSsrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalSsrcId.setStatus("obsolete")
_VLdpCepTdmFec129RemoteSsrcId_Type = Unsigned32
_VLdpCepTdmFec129RemoteSsrcId_Object = MibTableColumn
vLdpCepTdmFec129RemoteSsrcId = _VLdpCepTdmFec129RemoteSsrcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 21),
    _VLdpCepTdmFec129RemoteSsrcId_Type()
)
vLdpCepTdmFec129RemoteSsrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemoteSsrcId.setStatus("obsolete")
_VRtrLdpAggrPreMatchTable_Object = MibTable
vRtrLdpAggrPreMatchTable = _VRtrLdpAggrPreMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 26)
)
if mibBuilder.loadTexts:
    vRtrLdpAggrPreMatchTable.setStatus("obsolete")
_VRtrLdpAggrPreMatchEntry_Object = MibTableRow
vRtrLdpAggrPreMatchEntry = _VRtrLdpAggrPreMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 26, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpAggrPreMatchEntry.setStatus("obsolete")


class _VRtrLdpAggrPreMatchEnabled_Type(TruthValue):
    """Custom type vRtrLdpAggrPreMatchEnabled based on TruthValue"""
    defaultValue = 2


_VRtrLdpAggrPreMatchEnabled_Type.__name__ = "TruthValue"
_VRtrLdpAggrPreMatchEnabled_Object = MibTableColumn
vRtrLdpAggrPreMatchEnabled = _VRtrLdpAggrPreMatchEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 26, 1, 1),
    _VRtrLdpAggrPreMatchEnabled_Type()
)
vRtrLdpAggrPreMatchEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpAggrPreMatchEnabled.setStatus("obsolete")


class _VRtrLdpAggrPreMatchPreExcPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpAggrPreMatchPreExcPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpAggrPreMatchPreExcPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpAggrPreMatchPreExcPolicy1_Object = MibTableColumn
vRtrLdpAggrPreMatchPreExcPolicy1 = _VRtrLdpAggrPreMatchPreExcPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 26, 1, 2),
    _VRtrLdpAggrPreMatchPreExcPolicy1_Type()
)
vRtrLdpAggrPreMatchPreExcPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpAggrPreMatchPreExcPolicy1.setStatus("obsolete")


class _VRtrLdpAggrPreMatchPreExcPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpAggrPreMatchPreExcPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpAggrPreMatchPreExcPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpAggrPreMatchPreExcPolicy2_Object = MibTableColumn
vRtrLdpAggrPreMatchPreExcPolicy2 = _VRtrLdpAggrPreMatchPreExcPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 26, 1, 4),
    _VRtrLdpAggrPreMatchPreExcPolicy2_Type()
)
vRtrLdpAggrPreMatchPreExcPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpAggrPreMatchPreExcPolicy2.setStatus("obsolete")


class _VRtrLdpAggrPreMatchPreExcPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpAggrPreMatchPreExcPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpAggrPreMatchPreExcPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpAggrPreMatchPreExcPolicy3_Object = MibTableColumn
vRtrLdpAggrPreMatchPreExcPolicy3 = _VRtrLdpAggrPreMatchPreExcPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 26, 1, 5),
    _VRtrLdpAggrPreMatchPreExcPolicy3_Type()
)
vRtrLdpAggrPreMatchPreExcPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpAggrPreMatchPreExcPolicy3.setStatus("obsolete")


class _VRtrLdpAggrPreMatchPreExcPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpAggrPreMatchPreExcPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpAggrPreMatchPreExcPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpAggrPreMatchPreExcPolicy4_Object = MibTableColumn
vRtrLdpAggrPreMatchPreExcPolicy4 = _VRtrLdpAggrPreMatchPreExcPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 26, 1, 6),
    _VRtrLdpAggrPreMatchPreExcPolicy4_Type()
)
vRtrLdpAggrPreMatchPreExcPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpAggrPreMatchPreExcPolicy4.setStatus("obsolete")


class _VRtrLdpAggrPreMatchPreExcPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpAggrPreMatchPreExcPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpAggrPreMatchPreExcPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpAggrPreMatchPreExcPolicy5_Object = MibTableColumn
vRtrLdpAggrPreMatchPreExcPolicy5 = _VRtrLdpAggrPreMatchPreExcPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 26, 1, 7),
    _VRtrLdpAggrPreMatchPreExcPolicy5_Type()
)
vRtrLdpAggrPreMatchPreExcPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpAggrPreMatchPreExcPolicy5.setStatus("obsolete")


class _VRtrLdpAggrPreMatchAdminState_Type(TmnxAdminState):
    """Custom type vRtrLdpAggrPreMatchAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrLdpAggrPreMatchAdminState_Type.__name__ = "TmnxAdminState"
_VRtrLdpAggrPreMatchAdminState_Object = MibTableColumn
vRtrLdpAggrPreMatchAdminState = _VRtrLdpAggrPreMatchAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 26, 1, 8),
    _VRtrLdpAggrPreMatchAdminState_Type()
)
vRtrLdpAggrPreMatchAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpAggrPreMatchAdminState.setStatus("obsolete")
_VRtrLdpEgrStatFecPfxTblLastChgd_Type = TimeStamp
_VRtrLdpEgrStatFecPfxTblLastChgd_Object = MibScalar
vRtrLdpEgrStatFecPfxTblLastChgd = _VRtrLdpEgrStatFecPfxTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 27),
    _VRtrLdpEgrStatFecPfxTblLastChgd_Type()
)
vRtrLdpEgrStatFecPfxTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpEgrStatFecPfxTblLastChgd.setStatus("current")
_VRtrLdpEgrStatFecPfxTable_Object = MibTable
vRtrLdpEgrStatFecPfxTable = _VRtrLdpEgrStatFecPfxTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 28)
)
if mibBuilder.loadTexts:
    vRtrLdpEgrStatFecPfxTable.setStatus("current")
_VRtrLdpEgrStatFecPfxEntry_Object = MibTableRow
vRtrLdpEgrStatFecPfxEntry = _VRtrLdpEgrStatFecPfxEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 28, 1)
)
vRtrLdpEgrStatFecPfxEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpEgrStatFecPfxAddrType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpEgrStatFecPfxAddr"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpEgrStatFecPfxMaskLen"),
)
if mibBuilder.loadTexts:
    vRtrLdpEgrStatFecPfxEntry.setStatus("current")
_VRtrLdpEgrStatFecPfxAddrType_Type = TmnxAddressAndPrefixType
_VRtrLdpEgrStatFecPfxAddrType_Object = MibTableColumn
vRtrLdpEgrStatFecPfxAddrType = _VRtrLdpEgrStatFecPfxAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 28, 1, 1),
    _VRtrLdpEgrStatFecPfxAddrType_Type()
)
vRtrLdpEgrStatFecPfxAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpEgrStatFecPfxAddrType.setStatus("current")


class _VRtrLdpEgrStatFecPfxAddr_Type(TmnxAddressAndPrefixAddress):
    """Custom type vRtrLdpEgrStatFecPfxAddr based on TmnxAddressAndPrefixAddress"""
    subtypeSpec = TmnxAddressAndPrefixAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpEgrStatFecPfxAddr_Type.__name__ = "TmnxAddressAndPrefixAddress"
_VRtrLdpEgrStatFecPfxAddr_Object = MibTableColumn
vRtrLdpEgrStatFecPfxAddr = _VRtrLdpEgrStatFecPfxAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 28, 1, 2),
    _VRtrLdpEgrStatFecPfxAddr_Type()
)
vRtrLdpEgrStatFecPfxAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpEgrStatFecPfxAddr.setStatus("current")
_VRtrLdpEgrStatFecPfxMaskLen_Type = TmnxAddressAndPrefixPrefix
_VRtrLdpEgrStatFecPfxMaskLen_Object = MibTableColumn
vRtrLdpEgrStatFecPfxMaskLen = _VRtrLdpEgrStatFecPfxMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 28, 1, 3),
    _VRtrLdpEgrStatFecPfxMaskLen_Type()
)
vRtrLdpEgrStatFecPfxMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpEgrStatFecPfxMaskLen.setStatus("current")
_VRtrLdpEgrStatFecPfxRowStatus_Type = RowStatus
_VRtrLdpEgrStatFecPfxRowStatus_Object = MibTableColumn
vRtrLdpEgrStatFecPfxRowStatus = _VRtrLdpEgrStatFecPfxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 28, 1, 4),
    _VRtrLdpEgrStatFecPfxRowStatus_Type()
)
vRtrLdpEgrStatFecPfxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpEgrStatFecPfxRowStatus.setStatus("current")
_VRtrLdpEgrStatFecPfxLastChgd_Type = TimeStamp
_VRtrLdpEgrStatFecPfxLastChgd_Object = MibTableColumn
vRtrLdpEgrStatFecPfxLastChgd = _VRtrLdpEgrStatFecPfxLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 28, 1, 5),
    _VRtrLdpEgrStatFecPfxLastChgd_Type()
)
vRtrLdpEgrStatFecPfxLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpEgrStatFecPfxLastChgd.setStatus("current")


class _VRtrLdpEgrStatFecPfxCollStats_Type(TruthValue):
    """Custom type vRtrLdpEgrStatFecPfxCollStats based on TruthValue"""
    defaultValue = 2


_VRtrLdpEgrStatFecPfxCollStats_Type.__name__ = "TruthValue"
_VRtrLdpEgrStatFecPfxCollStats_Object = MibTableColumn
vRtrLdpEgrStatFecPfxCollStats = _VRtrLdpEgrStatFecPfxCollStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 28, 1, 6),
    _VRtrLdpEgrStatFecPfxCollStats_Type()
)
vRtrLdpEgrStatFecPfxCollStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpEgrStatFecPfxCollStats.setStatus("current")


class _VRtrLdpEgrStatFecPfxActgPol_Type(Unsigned32):
    """Custom type vRtrLdpEgrStatFecPfxActgPol based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 99),
    )


_VRtrLdpEgrStatFecPfxActgPol_Type.__name__ = "Unsigned32"
_VRtrLdpEgrStatFecPfxActgPol_Object = MibTableColumn
vRtrLdpEgrStatFecPfxActgPol = _VRtrLdpEgrStatFecPfxActgPol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 28, 1, 7),
    _VRtrLdpEgrStatFecPfxActgPol_Type()
)
vRtrLdpEgrStatFecPfxActgPol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpEgrStatFecPfxActgPol.setStatus("current")


class _VRtrLdpEgrStatFecPfxAdminState_Type(TmnxAdminState):
    """Custom type vRtrLdpEgrStatFecPfxAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrLdpEgrStatFecPfxAdminState_Type.__name__ = "TmnxAdminState"
_VRtrLdpEgrStatFecPfxAdminState_Object = MibTableColumn
vRtrLdpEgrStatFecPfxAdminState = _VRtrLdpEgrStatFecPfxAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 28, 1, 8),
    _VRtrLdpEgrStatFecPfxAdminState_Type()
)
vRtrLdpEgrStatFecPfxAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpEgrStatFecPfxAdminState.setStatus("current")
_VRtrLdpEgrStatisticsTable_Object = MibTable
vRtrLdpEgrStatisticsTable = _VRtrLdpEgrStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29)
)
if mibBuilder.loadTexts:
    vRtrLdpEgrStatisticsTable.setStatus("current")
_VRtrLdpEgrStatisticsEntry_Object = MibTableRow
vRtrLdpEgrStatisticsEntry = _VRtrLdpEgrStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpEgrStatisticsEntry.setStatus("current")
_VRtrLdpInProfilePktsFc0_Type = Counter64
_VRtrLdpInProfilePktsFc0_Object = MibTableColumn
vRtrLdpInProfilePktsFc0 = _VRtrLdpInProfilePktsFc0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 1),
    _VRtrLdpInProfilePktsFc0_Type()
)
vRtrLdpInProfilePktsFc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc0.setStatus("current")
_VRtrLdpInProfilePktsFc0Low32_Type = Counter32
_VRtrLdpInProfilePktsFc0Low32_Object = MibTableColumn
vRtrLdpInProfilePktsFc0Low32 = _VRtrLdpInProfilePktsFc0Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 2),
    _VRtrLdpInProfilePktsFc0Low32_Type()
)
vRtrLdpInProfilePktsFc0Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc0Low32.setStatus("current")
_VRtrLdpInProfilePktsFc0High32_Type = Counter32
_VRtrLdpInProfilePktsFc0High32_Object = MibTableColumn
vRtrLdpInProfilePktsFc0High32 = _VRtrLdpInProfilePktsFc0High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 3),
    _VRtrLdpInProfilePktsFc0High32_Type()
)
vRtrLdpInProfilePktsFc0High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc0High32.setStatus("current")
_VRtrLdpInProfilePktsFc1_Type = Counter64
_VRtrLdpInProfilePktsFc1_Object = MibTableColumn
vRtrLdpInProfilePktsFc1 = _VRtrLdpInProfilePktsFc1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 4),
    _VRtrLdpInProfilePktsFc1_Type()
)
vRtrLdpInProfilePktsFc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc1.setStatus("current")
_VRtrLdpInProfilePktsFc1Low32_Type = Counter32
_VRtrLdpInProfilePktsFc1Low32_Object = MibTableColumn
vRtrLdpInProfilePktsFc1Low32 = _VRtrLdpInProfilePktsFc1Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 5),
    _VRtrLdpInProfilePktsFc1Low32_Type()
)
vRtrLdpInProfilePktsFc1Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc1Low32.setStatus("current")
_VRtrLdpInProfilePktsFc1High32_Type = Counter32
_VRtrLdpInProfilePktsFc1High32_Object = MibTableColumn
vRtrLdpInProfilePktsFc1High32 = _VRtrLdpInProfilePktsFc1High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 6),
    _VRtrLdpInProfilePktsFc1High32_Type()
)
vRtrLdpInProfilePktsFc1High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc1High32.setStatus("current")
_VRtrLdpInProfilePktsFc2_Type = Counter64
_VRtrLdpInProfilePktsFc2_Object = MibTableColumn
vRtrLdpInProfilePktsFc2 = _VRtrLdpInProfilePktsFc2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 7),
    _VRtrLdpInProfilePktsFc2_Type()
)
vRtrLdpInProfilePktsFc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc2.setStatus("current")
_VRtrLdpInProfilePktsFc2Low32_Type = Counter32
_VRtrLdpInProfilePktsFc2Low32_Object = MibTableColumn
vRtrLdpInProfilePktsFc2Low32 = _VRtrLdpInProfilePktsFc2Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 8),
    _VRtrLdpInProfilePktsFc2Low32_Type()
)
vRtrLdpInProfilePktsFc2Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc2Low32.setStatus("current")
_VRtrLdpInProfilePktsFc2High32_Type = Counter32
_VRtrLdpInProfilePktsFc2High32_Object = MibTableColumn
vRtrLdpInProfilePktsFc2High32 = _VRtrLdpInProfilePktsFc2High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 9),
    _VRtrLdpInProfilePktsFc2High32_Type()
)
vRtrLdpInProfilePktsFc2High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc2High32.setStatus("current")
_VRtrLdpInProfilePktsFc3_Type = Counter64
_VRtrLdpInProfilePktsFc3_Object = MibTableColumn
vRtrLdpInProfilePktsFc3 = _VRtrLdpInProfilePktsFc3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 10),
    _VRtrLdpInProfilePktsFc3_Type()
)
vRtrLdpInProfilePktsFc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc3.setStatus("current")
_VRtrLdpInProfilePktsFc3Low32_Type = Counter32
_VRtrLdpInProfilePktsFc3Low32_Object = MibTableColumn
vRtrLdpInProfilePktsFc3Low32 = _VRtrLdpInProfilePktsFc3Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 11),
    _VRtrLdpInProfilePktsFc3Low32_Type()
)
vRtrLdpInProfilePktsFc3Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc3Low32.setStatus("current")
_VRtrLdpInProfilePktsFc3High32_Type = Counter32
_VRtrLdpInProfilePktsFc3High32_Object = MibTableColumn
vRtrLdpInProfilePktsFc3High32 = _VRtrLdpInProfilePktsFc3High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 12),
    _VRtrLdpInProfilePktsFc3High32_Type()
)
vRtrLdpInProfilePktsFc3High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc3High32.setStatus("current")
_VRtrLdpInProfilePktsFc4_Type = Counter64
_VRtrLdpInProfilePktsFc4_Object = MibTableColumn
vRtrLdpInProfilePktsFc4 = _VRtrLdpInProfilePktsFc4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 13),
    _VRtrLdpInProfilePktsFc4_Type()
)
vRtrLdpInProfilePktsFc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc4.setStatus("current")
_VRtrLdpInProfilePktsFc4Low32_Type = Counter32
_VRtrLdpInProfilePktsFc4Low32_Object = MibTableColumn
vRtrLdpInProfilePktsFc4Low32 = _VRtrLdpInProfilePktsFc4Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 14),
    _VRtrLdpInProfilePktsFc4Low32_Type()
)
vRtrLdpInProfilePktsFc4Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc4Low32.setStatus("current")
_VRtrLdpInProfilePktsFc4High32_Type = Counter32
_VRtrLdpInProfilePktsFc4High32_Object = MibTableColumn
vRtrLdpInProfilePktsFc4High32 = _VRtrLdpInProfilePktsFc4High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 15),
    _VRtrLdpInProfilePktsFc4High32_Type()
)
vRtrLdpInProfilePktsFc4High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc4High32.setStatus("current")
_VRtrLdpInProfilePktsFc5_Type = Counter64
_VRtrLdpInProfilePktsFc5_Object = MibTableColumn
vRtrLdpInProfilePktsFc5 = _VRtrLdpInProfilePktsFc5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 16),
    _VRtrLdpInProfilePktsFc5_Type()
)
vRtrLdpInProfilePktsFc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc5.setStatus("current")
_VRtrLdpInProfilePktsFc5Low32_Type = Counter32
_VRtrLdpInProfilePktsFc5Low32_Object = MibTableColumn
vRtrLdpInProfilePktsFc5Low32 = _VRtrLdpInProfilePktsFc5Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 17),
    _VRtrLdpInProfilePktsFc5Low32_Type()
)
vRtrLdpInProfilePktsFc5Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc5Low32.setStatus("current")
_VRtrLdpInProfilePktsFc5High32_Type = Counter32
_VRtrLdpInProfilePktsFc5High32_Object = MibTableColumn
vRtrLdpInProfilePktsFc5High32 = _VRtrLdpInProfilePktsFc5High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 18),
    _VRtrLdpInProfilePktsFc5High32_Type()
)
vRtrLdpInProfilePktsFc5High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc5High32.setStatus("current")
_VRtrLdpInProfilePktsFc6_Type = Counter64
_VRtrLdpInProfilePktsFc6_Object = MibTableColumn
vRtrLdpInProfilePktsFc6 = _VRtrLdpInProfilePktsFc6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 19),
    _VRtrLdpInProfilePktsFc6_Type()
)
vRtrLdpInProfilePktsFc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc6.setStatus("current")
_VRtrLdpInProfilePktsFc6Low32_Type = Counter32
_VRtrLdpInProfilePktsFc6Low32_Object = MibTableColumn
vRtrLdpInProfilePktsFc6Low32 = _VRtrLdpInProfilePktsFc6Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 20),
    _VRtrLdpInProfilePktsFc6Low32_Type()
)
vRtrLdpInProfilePktsFc6Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc6Low32.setStatus("current")
_VRtrLdpInProfilePktsFc6High32_Type = Counter32
_VRtrLdpInProfilePktsFc6High32_Object = MibTableColumn
vRtrLdpInProfilePktsFc6High32 = _VRtrLdpInProfilePktsFc6High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 21),
    _VRtrLdpInProfilePktsFc6High32_Type()
)
vRtrLdpInProfilePktsFc6High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc6High32.setStatus("current")
_VRtrLdpInProfilePktsFc7_Type = Counter64
_VRtrLdpInProfilePktsFc7_Object = MibTableColumn
vRtrLdpInProfilePktsFc7 = _VRtrLdpInProfilePktsFc7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 22),
    _VRtrLdpInProfilePktsFc7_Type()
)
vRtrLdpInProfilePktsFc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc7.setStatus("current")
_VRtrLdpInProfilePktsFc7Low32_Type = Counter32
_VRtrLdpInProfilePktsFc7Low32_Object = MibTableColumn
vRtrLdpInProfilePktsFc7Low32 = _VRtrLdpInProfilePktsFc7Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 23),
    _VRtrLdpInProfilePktsFc7Low32_Type()
)
vRtrLdpInProfilePktsFc7Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc7Low32.setStatus("current")
_VRtrLdpInProfilePktsFc7High32_Type = Counter32
_VRtrLdpInProfilePktsFc7High32_Object = MibTableColumn
vRtrLdpInProfilePktsFc7High32 = _VRtrLdpInProfilePktsFc7High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 24),
    _VRtrLdpInProfilePktsFc7High32_Type()
)
vRtrLdpInProfilePktsFc7High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfilePktsFc7High32.setStatus("current")
_VRtrLdpInProfileOctetsFc0_Type = Counter64
_VRtrLdpInProfileOctetsFc0_Object = MibTableColumn
vRtrLdpInProfileOctetsFc0 = _VRtrLdpInProfileOctetsFc0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 25),
    _VRtrLdpInProfileOctetsFc0_Type()
)
vRtrLdpInProfileOctetsFc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc0.setStatus("current")
_VRtrLdpInProfileOctetsFc0Low32_Type = Counter32
_VRtrLdpInProfileOctetsFc0Low32_Object = MibTableColumn
vRtrLdpInProfileOctetsFc0Low32 = _VRtrLdpInProfileOctetsFc0Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 26),
    _VRtrLdpInProfileOctetsFc0Low32_Type()
)
vRtrLdpInProfileOctetsFc0Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc0Low32.setStatus("current")
_VRtrLdpInProfileOctetsFc0High32_Type = Counter32
_VRtrLdpInProfileOctetsFc0High32_Object = MibTableColumn
vRtrLdpInProfileOctetsFc0High32 = _VRtrLdpInProfileOctetsFc0High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 27),
    _VRtrLdpInProfileOctetsFc0High32_Type()
)
vRtrLdpInProfileOctetsFc0High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc0High32.setStatus("current")
_VRtrLdpInProfileOctetsFc1_Type = Counter64
_VRtrLdpInProfileOctetsFc1_Object = MibTableColumn
vRtrLdpInProfileOctetsFc1 = _VRtrLdpInProfileOctetsFc1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 28),
    _VRtrLdpInProfileOctetsFc1_Type()
)
vRtrLdpInProfileOctetsFc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc1.setStatus("current")
_VRtrLdpInProfileOctetsFc1Low32_Type = Counter32
_VRtrLdpInProfileOctetsFc1Low32_Object = MibTableColumn
vRtrLdpInProfileOctetsFc1Low32 = _VRtrLdpInProfileOctetsFc1Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 29),
    _VRtrLdpInProfileOctetsFc1Low32_Type()
)
vRtrLdpInProfileOctetsFc1Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc1Low32.setStatus("current")
_VRtrLdpInProfileOctetsFc1High32_Type = Counter32
_VRtrLdpInProfileOctetsFc1High32_Object = MibTableColumn
vRtrLdpInProfileOctetsFc1High32 = _VRtrLdpInProfileOctetsFc1High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 30),
    _VRtrLdpInProfileOctetsFc1High32_Type()
)
vRtrLdpInProfileOctetsFc1High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc1High32.setStatus("current")
_VRtrLdpInProfileOctetsFc2_Type = Counter64
_VRtrLdpInProfileOctetsFc2_Object = MibTableColumn
vRtrLdpInProfileOctetsFc2 = _VRtrLdpInProfileOctetsFc2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 31),
    _VRtrLdpInProfileOctetsFc2_Type()
)
vRtrLdpInProfileOctetsFc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc2.setStatus("current")
_VRtrLdpInProfileOctetsFc2Low32_Type = Counter32
_VRtrLdpInProfileOctetsFc2Low32_Object = MibTableColumn
vRtrLdpInProfileOctetsFc2Low32 = _VRtrLdpInProfileOctetsFc2Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 32),
    _VRtrLdpInProfileOctetsFc2Low32_Type()
)
vRtrLdpInProfileOctetsFc2Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc2Low32.setStatus("current")
_VRtrLdpInProfileOctetsFc2High32_Type = Counter32
_VRtrLdpInProfileOctetsFc2High32_Object = MibTableColumn
vRtrLdpInProfileOctetsFc2High32 = _VRtrLdpInProfileOctetsFc2High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 33),
    _VRtrLdpInProfileOctetsFc2High32_Type()
)
vRtrLdpInProfileOctetsFc2High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc2High32.setStatus("current")
_VRtrLdpInProfileOctetsFc3_Type = Counter64
_VRtrLdpInProfileOctetsFc3_Object = MibTableColumn
vRtrLdpInProfileOctetsFc3 = _VRtrLdpInProfileOctetsFc3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 34),
    _VRtrLdpInProfileOctetsFc3_Type()
)
vRtrLdpInProfileOctetsFc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc3.setStatus("current")
_VRtrLdpInProfileOctetsFc3Low32_Type = Counter32
_VRtrLdpInProfileOctetsFc3Low32_Object = MibTableColumn
vRtrLdpInProfileOctetsFc3Low32 = _VRtrLdpInProfileOctetsFc3Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 35),
    _VRtrLdpInProfileOctetsFc3Low32_Type()
)
vRtrLdpInProfileOctetsFc3Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc3Low32.setStatus("current")
_VRtrLdpInProfileOctetsFc3High32_Type = Counter32
_VRtrLdpInProfileOctetsFc3High32_Object = MibTableColumn
vRtrLdpInProfileOctetsFc3High32 = _VRtrLdpInProfileOctetsFc3High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 36),
    _VRtrLdpInProfileOctetsFc3High32_Type()
)
vRtrLdpInProfileOctetsFc3High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc3High32.setStatus("current")
_VRtrLdpInProfileOctetsFc4_Type = Counter64
_VRtrLdpInProfileOctetsFc4_Object = MibTableColumn
vRtrLdpInProfileOctetsFc4 = _VRtrLdpInProfileOctetsFc4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 37),
    _VRtrLdpInProfileOctetsFc4_Type()
)
vRtrLdpInProfileOctetsFc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc4.setStatus("current")
_VRtrLdpInProfileOctetsFc4Low32_Type = Counter32
_VRtrLdpInProfileOctetsFc4Low32_Object = MibTableColumn
vRtrLdpInProfileOctetsFc4Low32 = _VRtrLdpInProfileOctetsFc4Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 38),
    _VRtrLdpInProfileOctetsFc4Low32_Type()
)
vRtrLdpInProfileOctetsFc4Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc4Low32.setStatus("current")
_VRtrLdpInProfileOctetsFc4High32_Type = Counter32
_VRtrLdpInProfileOctetsFc4High32_Object = MibTableColumn
vRtrLdpInProfileOctetsFc4High32 = _VRtrLdpInProfileOctetsFc4High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 39),
    _VRtrLdpInProfileOctetsFc4High32_Type()
)
vRtrLdpInProfileOctetsFc4High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc4High32.setStatus("current")
_VRtrLdpInProfileOctetsFc5_Type = Counter64
_VRtrLdpInProfileOctetsFc5_Object = MibTableColumn
vRtrLdpInProfileOctetsFc5 = _VRtrLdpInProfileOctetsFc5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 40),
    _VRtrLdpInProfileOctetsFc5_Type()
)
vRtrLdpInProfileOctetsFc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc5.setStatus("current")
_VRtrLdpInProfileOctetsFc5Low32_Type = Counter32
_VRtrLdpInProfileOctetsFc5Low32_Object = MibTableColumn
vRtrLdpInProfileOctetsFc5Low32 = _VRtrLdpInProfileOctetsFc5Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 41),
    _VRtrLdpInProfileOctetsFc5Low32_Type()
)
vRtrLdpInProfileOctetsFc5Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc5Low32.setStatus("current")
_VRtrLdpInProfileOctetsFc5High32_Type = Counter32
_VRtrLdpInProfileOctetsFc5High32_Object = MibTableColumn
vRtrLdpInProfileOctetsFc5High32 = _VRtrLdpInProfileOctetsFc5High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 42),
    _VRtrLdpInProfileOctetsFc5High32_Type()
)
vRtrLdpInProfileOctetsFc5High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc5High32.setStatus("current")
_VRtrLdpInProfileOctetsFc6_Type = Counter64
_VRtrLdpInProfileOctetsFc6_Object = MibTableColumn
vRtrLdpInProfileOctetsFc6 = _VRtrLdpInProfileOctetsFc6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 43),
    _VRtrLdpInProfileOctetsFc6_Type()
)
vRtrLdpInProfileOctetsFc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc6.setStatus("current")
_VRtrLdpInProfileOctetsFc6Low32_Type = Counter32
_VRtrLdpInProfileOctetsFc6Low32_Object = MibTableColumn
vRtrLdpInProfileOctetsFc6Low32 = _VRtrLdpInProfileOctetsFc6Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 44),
    _VRtrLdpInProfileOctetsFc6Low32_Type()
)
vRtrLdpInProfileOctetsFc6Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc6Low32.setStatus("current")
_VRtrLdpInProfileOctetsFc6High32_Type = Counter32
_VRtrLdpInProfileOctetsFc6High32_Object = MibTableColumn
vRtrLdpInProfileOctetsFc6High32 = _VRtrLdpInProfileOctetsFc6High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 45),
    _VRtrLdpInProfileOctetsFc6High32_Type()
)
vRtrLdpInProfileOctetsFc6High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc6High32.setStatus("current")
_VRtrLdpInProfileOctetsFc7_Type = Counter64
_VRtrLdpInProfileOctetsFc7_Object = MibTableColumn
vRtrLdpInProfileOctetsFc7 = _VRtrLdpInProfileOctetsFc7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 46),
    _VRtrLdpInProfileOctetsFc7_Type()
)
vRtrLdpInProfileOctetsFc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc7.setStatus("current")
_VRtrLdpInProfileOctetsFc7Low32_Type = Counter32
_VRtrLdpInProfileOctetsFc7Low32_Object = MibTableColumn
vRtrLdpInProfileOctetsFc7Low32 = _VRtrLdpInProfileOctetsFc7Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 47),
    _VRtrLdpInProfileOctetsFc7Low32_Type()
)
vRtrLdpInProfileOctetsFc7Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc7Low32.setStatus("current")
_VRtrLdpInProfileOctetsFc7High32_Type = Counter32
_VRtrLdpInProfileOctetsFc7High32_Object = MibTableColumn
vRtrLdpInProfileOctetsFc7High32 = _VRtrLdpInProfileOctetsFc7High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 48),
    _VRtrLdpInProfileOctetsFc7High32_Type()
)
vRtrLdpInProfileOctetsFc7High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpInProfileOctetsFc7High32.setStatus("current")
_VRtrLdpOutOfProfPktsFc0_Type = Counter64
_VRtrLdpOutOfProfPktsFc0_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc0 = _VRtrLdpOutOfProfPktsFc0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 49),
    _VRtrLdpOutOfProfPktsFc0_Type()
)
vRtrLdpOutOfProfPktsFc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc0.setStatus("current")
_VRtrLdpOutOfProfPktsFc0Low32_Type = Counter32
_VRtrLdpOutOfProfPktsFc0Low32_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc0Low32 = _VRtrLdpOutOfProfPktsFc0Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 50),
    _VRtrLdpOutOfProfPktsFc0Low32_Type()
)
vRtrLdpOutOfProfPktsFc0Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc0Low32.setStatus("current")
_VRtrLdpOutOfProfPktsFc0High32_Type = Counter32
_VRtrLdpOutOfProfPktsFc0High32_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc0High32 = _VRtrLdpOutOfProfPktsFc0High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 51),
    _VRtrLdpOutOfProfPktsFc0High32_Type()
)
vRtrLdpOutOfProfPktsFc0High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc0High32.setStatus("current")
_VRtrLdpOutOfProfPktsFc1_Type = Counter64
_VRtrLdpOutOfProfPktsFc1_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc1 = _VRtrLdpOutOfProfPktsFc1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 52),
    _VRtrLdpOutOfProfPktsFc1_Type()
)
vRtrLdpOutOfProfPktsFc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc1.setStatus("current")
_VRtrLdpOutOfProfPktsFc1Low32_Type = Counter32
_VRtrLdpOutOfProfPktsFc1Low32_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc1Low32 = _VRtrLdpOutOfProfPktsFc1Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 53),
    _VRtrLdpOutOfProfPktsFc1Low32_Type()
)
vRtrLdpOutOfProfPktsFc1Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc1Low32.setStatus("current")
_VRtrLdpOutOfProfPktsFc1High32_Type = Counter32
_VRtrLdpOutOfProfPktsFc1High32_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc1High32 = _VRtrLdpOutOfProfPktsFc1High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 54),
    _VRtrLdpOutOfProfPktsFc1High32_Type()
)
vRtrLdpOutOfProfPktsFc1High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc1High32.setStatus("current")
_VRtrLdpOutOfProfPktsFc2_Type = Counter64
_VRtrLdpOutOfProfPktsFc2_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc2 = _VRtrLdpOutOfProfPktsFc2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 55),
    _VRtrLdpOutOfProfPktsFc2_Type()
)
vRtrLdpOutOfProfPktsFc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc2.setStatus("current")
_VRtrLdpOutOfProfPktsFc2Low32_Type = Counter32
_VRtrLdpOutOfProfPktsFc2Low32_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc2Low32 = _VRtrLdpOutOfProfPktsFc2Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 56),
    _VRtrLdpOutOfProfPktsFc2Low32_Type()
)
vRtrLdpOutOfProfPktsFc2Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc2Low32.setStatus("current")
_VRtrLdpOutOfProfPktsFc2High32_Type = Counter32
_VRtrLdpOutOfProfPktsFc2High32_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc2High32 = _VRtrLdpOutOfProfPktsFc2High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 57),
    _VRtrLdpOutOfProfPktsFc2High32_Type()
)
vRtrLdpOutOfProfPktsFc2High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc2High32.setStatus("current")
_VRtrLdpOutOfProfPktsFc3_Type = Counter64
_VRtrLdpOutOfProfPktsFc3_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc3 = _VRtrLdpOutOfProfPktsFc3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 58),
    _VRtrLdpOutOfProfPktsFc3_Type()
)
vRtrLdpOutOfProfPktsFc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc3.setStatus("current")
_VRtrLdpOutOfProfPktsFc3Low32_Type = Counter32
_VRtrLdpOutOfProfPktsFc3Low32_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc3Low32 = _VRtrLdpOutOfProfPktsFc3Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 59),
    _VRtrLdpOutOfProfPktsFc3Low32_Type()
)
vRtrLdpOutOfProfPktsFc3Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc3Low32.setStatus("current")
_VRtrLdpOutOfProfPktsFc3High32_Type = Counter32
_VRtrLdpOutOfProfPktsFc3High32_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc3High32 = _VRtrLdpOutOfProfPktsFc3High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 60),
    _VRtrLdpOutOfProfPktsFc3High32_Type()
)
vRtrLdpOutOfProfPktsFc3High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc3High32.setStatus("current")
_VRtrLdpOutOfProfPktsFc4_Type = Counter64
_VRtrLdpOutOfProfPktsFc4_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc4 = _VRtrLdpOutOfProfPktsFc4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 61),
    _VRtrLdpOutOfProfPktsFc4_Type()
)
vRtrLdpOutOfProfPktsFc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc4.setStatus("current")
_VRtrLdpOutOfProfPktsFc4Low32_Type = Counter32
_VRtrLdpOutOfProfPktsFc4Low32_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc4Low32 = _VRtrLdpOutOfProfPktsFc4Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 62),
    _VRtrLdpOutOfProfPktsFc4Low32_Type()
)
vRtrLdpOutOfProfPktsFc4Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc4Low32.setStatus("current")
_VRtrLdpOutOfProfPktsFc4High32_Type = Counter32
_VRtrLdpOutOfProfPktsFc4High32_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc4High32 = _VRtrLdpOutOfProfPktsFc4High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 63),
    _VRtrLdpOutOfProfPktsFc4High32_Type()
)
vRtrLdpOutOfProfPktsFc4High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc4High32.setStatus("current")
_VRtrLdpOutOfProfPktsFc5_Type = Counter64
_VRtrLdpOutOfProfPktsFc5_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc5 = _VRtrLdpOutOfProfPktsFc5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 64),
    _VRtrLdpOutOfProfPktsFc5_Type()
)
vRtrLdpOutOfProfPktsFc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc5.setStatus("current")
_VRtrLdpOutOfProfPktsFc5Low32_Type = Counter32
_VRtrLdpOutOfProfPktsFc5Low32_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc5Low32 = _VRtrLdpOutOfProfPktsFc5Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 65),
    _VRtrLdpOutOfProfPktsFc5Low32_Type()
)
vRtrLdpOutOfProfPktsFc5Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc5Low32.setStatus("current")
_VRtrLdpOutOfProfPktsFc5High32_Type = Counter32
_VRtrLdpOutOfProfPktsFc5High32_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc5High32 = _VRtrLdpOutOfProfPktsFc5High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 66),
    _VRtrLdpOutOfProfPktsFc5High32_Type()
)
vRtrLdpOutOfProfPktsFc5High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc5High32.setStatus("current")
_VRtrLdpOutOfProfPktsFc6_Type = Counter64
_VRtrLdpOutOfProfPktsFc6_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc6 = _VRtrLdpOutOfProfPktsFc6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 67),
    _VRtrLdpOutOfProfPktsFc6_Type()
)
vRtrLdpOutOfProfPktsFc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc6.setStatus("current")
_VRtrLdpOutOfProfPktsFc6Low32_Type = Counter32
_VRtrLdpOutOfProfPktsFc6Low32_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc6Low32 = _VRtrLdpOutOfProfPktsFc6Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 68),
    _VRtrLdpOutOfProfPktsFc6Low32_Type()
)
vRtrLdpOutOfProfPktsFc6Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc6Low32.setStatus("current")
_VRtrLdpOutOfProfPktsFc6High32_Type = Counter32
_VRtrLdpOutOfProfPktsFc6High32_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc6High32 = _VRtrLdpOutOfProfPktsFc6High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 69),
    _VRtrLdpOutOfProfPktsFc6High32_Type()
)
vRtrLdpOutOfProfPktsFc6High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc6High32.setStatus("current")
_VRtrLdpOutOfProfPktsFc7_Type = Counter64
_VRtrLdpOutOfProfPktsFc7_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc7 = _VRtrLdpOutOfProfPktsFc7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 70),
    _VRtrLdpOutOfProfPktsFc7_Type()
)
vRtrLdpOutOfProfPktsFc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc7.setStatus("current")
_VRtrLdpOutOfProfPktsFc7Low32_Type = Counter32
_VRtrLdpOutOfProfPktsFc7Low32_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc7Low32 = _VRtrLdpOutOfProfPktsFc7Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 71),
    _VRtrLdpOutOfProfPktsFc7Low32_Type()
)
vRtrLdpOutOfProfPktsFc7Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc7Low32.setStatus("current")
_VRtrLdpOutOfProfPktsFc7High32_Type = Counter32
_VRtrLdpOutOfProfPktsFc7High32_Object = MibTableColumn
vRtrLdpOutOfProfPktsFc7High32 = _VRtrLdpOutOfProfPktsFc7High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 72),
    _VRtrLdpOutOfProfPktsFc7High32_Type()
)
vRtrLdpOutOfProfPktsFc7High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfPktsFc7High32.setStatus("current")
_VRtrLdpOutOfProfOctetsFc0_Type = Counter64
_VRtrLdpOutOfProfOctetsFc0_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc0 = _VRtrLdpOutOfProfOctetsFc0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 73),
    _VRtrLdpOutOfProfOctetsFc0_Type()
)
vRtrLdpOutOfProfOctetsFc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc0.setStatus("current")
_VRtrLdpOutOfProfOctetsFc0Low32_Type = Counter32
_VRtrLdpOutOfProfOctetsFc0Low32_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc0Low32 = _VRtrLdpOutOfProfOctetsFc0Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 74),
    _VRtrLdpOutOfProfOctetsFc0Low32_Type()
)
vRtrLdpOutOfProfOctetsFc0Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc0Low32.setStatus("current")
_VRtrLdpOutOfProfOctetsFc0High32_Type = Counter32
_VRtrLdpOutOfProfOctetsFc0High32_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc0High32 = _VRtrLdpOutOfProfOctetsFc0High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 75),
    _VRtrLdpOutOfProfOctetsFc0High32_Type()
)
vRtrLdpOutOfProfOctetsFc0High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc0High32.setStatus("current")
_VRtrLdpOutOfProfOctetsFc1_Type = Counter64
_VRtrLdpOutOfProfOctetsFc1_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc1 = _VRtrLdpOutOfProfOctetsFc1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 76),
    _VRtrLdpOutOfProfOctetsFc1_Type()
)
vRtrLdpOutOfProfOctetsFc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc1.setStatus("current")
_VRtrLdpOutOfProfOctetsFc1Low32_Type = Counter32
_VRtrLdpOutOfProfOctetsFc1Low32_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc1Low32 = _VRtrLdpOutOfProfOctetsFc1Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 77),
    _VRtrLdpOutOfProfOctetsFc1Low32_Type()
)
vRtrLdpOutOfProfOctetsFc1Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc1Low32.setStatus("current")
_VRtrLdpOutOfProfOctetsFc1High32_Type = Counter32
_VRtrLdpOutOfProfOctetsFc1High32_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc1High32 = _VRtrLdpOutOfProfOctetsFc1High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 78),
    _VRtrLdpOutOfProfOctetsFc1High32_Type()
)
vRtrLdpOutOfProfOctetsFc1High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc1High32.setStatus("current")
_VRtrLdpOutOfProfOctetsFc2_Type = Counter64
_VRtrLdpOutOfProfOctetsFc2_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc2 = _VRtrLdpOutOfProfOctetsFc2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 79),
    _VRtrLdpOutOfProfOctetsFc2_Type()
)
vRtrLdpOutOfProfOctetsFc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc2.setStatus("current")
_VRtrLdpOutOfProfOctetsFc2Low32_Type = Counter32
_VRtrLdpOutOfProfOctetsFc2Low32_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc2Low32 = _VRtrLdpOutOfProfOctetsFc2Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 80),
    _VRtrLdpOutOfProfOctetsFc2Low32_Type()
)
vRtrLdpOutOfProfOctetsFc2Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc2Low32.setStatus("current")
_VRtrLdpOutOfProfOctetsFc2High32_Type = Counter32
_VRtrLdpOutOfProfOctetsFc2High32_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc2High32 = _VRtrLdpOutOfProfOctetsFc2High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 81),
    _VRtrLdpOutOfProfOctetsFc2High32_Type()
)
vRtrLdpOutOfProfOctetsFc2High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc2High32.setStatus("current")
_VRtrLdpOutOfProfOctetsFc3_Type = Counter64
_VRtrLdpOutOfProfOctetsFc3_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc3 = _VRtrLdpOutOfProfOctetsFc3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 82),
    _VRtrLdpOutOfProfOctetsFc3_Type()
)
vRtrLdpOutOfProfOctetsFc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc3.setStatus("current")
_VRtrLdpOutOfProfOctetsFc3Low32_Type = Counter32
_VRtrLdpOutOfProfOctetsFc3Low32_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc3Low32 = _VRtrLdpOutOfProfOctetsFc3Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 83),
    _VRtrLdpOutOfProfOctetsFc3Low32_Type()
)
vRtrLdpOutOfProfOctetsFc3Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc3Low32.setStatus("current")
_VRtrLdpOutOfProfOctetsFc3High32_Type = Counter32
_VRtrLdpOutOfProfOctetsFc3High32_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc3High32 = _VRtrLdpOutOfProfOctetsFc3High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 84),
    _VRtrLdpOutOfProfOctetsFc3High32_Type()
)
vRtrLdpOutOfProfOctetsFc3High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc3High32.setStatus("current")
_VRtrLdpOutOfProfOctetsFc4_Type = Counter64
_VRtrLdpOutOfProfOctetsFc4_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc4 = _VRtrLdpOutOfProfOctetsFc4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 85),
    _VRtrLdpOutOfProfOctetsFc4_Type()
)
vRtrLdpOutOfProfOctetsFc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc4.setStatus("current")
_VRtrLdpOutOfProfOctetsFc4Low32_Type = Counter32
_VRtrLdpOutOfProfOctetsFc4Low32_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc4Low32 = _VRtrLdpOutOfProfOctetsFc4Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 86),
    _VRtrLdpOutOfProfOctetsFc4Low32_Type()
)
vRtrLdpOutOfProfOctetsFc4Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc4Low32.setStatus("current")
_VRtrLdpOutOfProfOctetsFc4High32_Type = Counter32
_VRtrLdpOutOfProfOctetsFc4High32_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc4High32 = _VRtrLdpOutOfProfOctetsFc4High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 87),
    _VRtrLdpOutOfProfOctetsFc4High32_Type()
)
vRtrLdpOutOfProfOctetsFc4High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc4High32.setStatus("current")
_VRtrLdpOutOfProfOctetsFc5_Type = Counter64
_VRtrLdpOutOfProfOctetsFc5_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc5 = _VRtrLdpOutOfProfOctetsFc5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 88),
    _VRtrLdpOutOfProfOctetsFc5_Type()
)
vRtrLdpOutOfProfOctetsFc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc5.setStatus("current")
_VRtrLdpOutOfProfOctetsFc5Low32_Type = Counter32
_VRtrLdpOutOfProfOctetsFc5Low32_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc5Low32 = _VRtrLdpOutOfProfOctetsFc5Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 89),
    _VRtrLdpOutOfProfOctetsFc5Low32_Type()
)
vRtrLdpOutOfProfOctetsFc5Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc5Low32.setStatus("current")
_VRtrLdpOutOfProfOctetsFc5High32_Type = Counter32
_VRtrLdpOutOfProfOctetsFc5High32_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc5High32 = _VRtrLdpOutOfProfOctetsFc5High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 90),
    _VRtrLdpOutOfProfOctetsFc5High32_Type()
)
vRtrLdpOutOfProfOctetsFc5High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc5High32.setStatus("current")
_VRtrLdpOutOfProfOctetsFc6_Type = Counter64
_VRtrLdpOutOfProfOctetsFc6_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc6 = _VRtrLdpOutOfProfOctetsFc6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 91),
    _VRtrLdpOutOfProfOctetsFc6_Type()
)
vRtrLdpOutOfProfOctetsFc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc6.setStatus("current")
_VRtrLdpOutOfProfOctetsFc6Low32_Type = Counter32
_VRtrLdpOutOfProfOctetsFc6Low32_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc6Low32 = _VRtrLdpOutOfProfOctetsFc6Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 92),
    _VRtrLdpOutOfProfOctetsFc6Low32_Type()
)
vRtrLdpOutOfProfOctetsFc6Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc6Low32.setStatus("current")
_VRtrLdpOutOfProfOctetsFc6High32_Type = Counter32
_VRtrLdpOutOfProfOctetsFc6High32_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc6High32 = _VRtrLdpOutOfProfOctetsFc6High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 93),
    _VRtrLdpOutOfProfOctetsFc6High32_Type()
)
vRtrLdpOutOfProfOctetsFc6High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc6High32.setStatus("current")
_VRtrLdpOutOfProfOctetsFc7_Type = Counter64
_VRtrLdpOutOfProfOctetsFc7_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc7 = _VRtrLdpOutOfProfOctetsFc7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 94),
    _VRtrLdpOutOfProfOctetsFc7_Type()
)
vRtrLdpOutOfProfOctetsFc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc7.setStatus("current")
_VRtrLdpOutOfProfOctetsFc7Low32_Type = Counter32
_VRtrLdpOutOfProfOctetsFc7Low32_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc7Low32 = _VRtrLdpOutOfProfOctetsFc7Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 95),
    _VRtrLdpOutOfProfOctetsFc7Low32_Type()
)
vRtrLdpOutOfProfOctetsFc7Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc7Low32.setStatus("current")
_VRtrLdpOutOfProfOctetsFc7High32_Type = Counter32
_VRtrLdpOutOfProfOctetsFc7High32_Object = MibTableColumn
vRtrLdpOutOfProfOctetsFc7High32 = _VRtrLdpOutOfProfOctetsFc7High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 96),
    _VRtrLdpOutOfProfOctetsFc7High32_Type()
)
vRtrLdpOutOfProfOctetsFc7High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpOutOfProfOctetsFc7High32.setStatus("current")
_VRtrLdpAggregatePkts_Type = Counter64
_VRtrLdpAggregatePkts_Object = MibTableColumn
vRtrLdpAggregatePkts = _VRtrLdpAggregatePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 97),
    _VRtrLdpAggregatePkts_Type()
)
vRtrLdpAggregatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAggregatePkts.setStatus("current")
_VRtrLdpAggregatePktsLow32_Type = Counter32
_VRtrLdpAggregatePktsLow32_Object = MibTableColumn
vRtrLdpAggregatePktsLow32 = _VRtrLdpAggregatePktsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 98),
    _VRtrLdpAggregatePktsLow32_Type()
)
vRtrLdpAggregatePktsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAggregatePktsLow32.setStatus("current")
_VRtrLdpAggregatePktsHigh32_Type = Counter32
_VRtrLdpAggregatePktsHigh32_Object = MibTableColumn
vRtrLdpAggregatePktsHigh32 = _VRtrLdpAggregatePktsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 99),
    _VRtrLdpAggregatePktsHigh32_Type()
)
vRtrLdpAggregatePktsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAggregatePktsHigh32.setStatus("current")
_VRtrLdpAggregateOctets_Type = Counter64
_VRtrLdpAggregateOctets_Object = MibTableColumn
vRtrLdpAggregateOctets = _VRtrLdpAggregateOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 100),
    _VRtrLdpAggregateOctets_Type()
)
vRtrLdpAggregateOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAggregateOctets.setStatus("current")
_VRtrLdpAggregateOctetsLow32_Type = Counter32
_VRtrLdpAggregateOctetsLow32_Object = MibTableColumn
vRtrLdpAggregateOctetsLow32 = _VRtrLdpAggregateOctetsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 101),
    _VRtrLdpAggregateOctetsLow32_Type()
)
vRtrLdpAggregateOctetsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAggregateOctetsLow32.setStatus("current")
_VRtrLdpAggregateOctetsHigh32_Type = Counter32
_VRtrLdpAggregateOctetsHigh32_Object = MibTableColumn
vRtrLdpAggregateOctetsHigh32 = _VRtrLdpAggregateOctetsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 29, 1, 102),
    _VRtrLdpAggregateOctetsHigh32_Type()
)
vRtrLdpAggregateOctetsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAggregateOctetsHigh32.setStatus("current")
_VRtrLdpAddrFecExtTable_Object = MibTable
vRtrLdpAddrFecExtTable = _VRtrLdpAddrFecExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30)
)
if mibBuilder.loadTexts:
    vRtrLdpAddrFecExtTable.setStatus("obsolete")
_VRtrLdpAddrFecExtEntry_Object = MibTableRow
vRtrLdpAddrFecExtEntry = _VRtrLdpAddrFecExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpAddrFecExtEntry.setStatus("obsolete")
_VRtrLdpAddrFecOutLbl6_Type = Unsigned32
_VRtrLdpAddrFecOutLbl6_Object = MibTableColumn
vRtrLdpAddrFecOutLbl6 = _VRtrLdpAddrFecOutLbl6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 1),
    _VRtrLdpAddrFecOutLbl6_Type()
)
vRtrLdpAddrFecOutLbl6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLbl6.setStatus("obsolete")
_VRtrLdpAddrFecOutLblStatus6_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLblStatus6_Object = MibTableColumn
vRtrLdpAddrFecOutLblStatus6 = _VRtrLdpAddrFecOutLblStatus6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 2),
    _VRtrLdpAddrFecOutLblStatus6_Type()
)
vRtrLdpAddrFecOutLblStatus6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblStatus6.setStatus("obsolete")
_VRtrLdpAddrFecOutLblIfIndex6_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLblIfIndex6_Object = MibTableColumn
vRtrLdpAddrFecOutLblIfIndex6 = _VRtrLdpAddrFecOutLblIfIndex6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 3),
    _VRtrLdpAddrFecOutLblIfIndex6_Type()
)
vRtrLdpAddrFecOutLblIfIndex6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblIfIndex6.setStatus("obsolete")
_VRtrLdpAddrFecOutLblNxtHopType6_Type = InetAddressType
_VRtrLdpAddrFecOutLblNxtHopType6_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopType6 = _VRtrLdpAddrFecOutLblNxtHopType6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 4),
    _VRtrLdpAddrFecOutLblNxtHopType6_Type()
)
vRtrLdpAddrFecOutLblNxtHopType6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopType6.setStatus("obsolete")


class _VRtrLdpAddrFecOutLblNxtHopAddr6_Type(InetAddress):
    """Custom type vRtrLdpAddrFecOutLblNxtHopAddr6 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpAddrFecOutLblNxtHopAddr6_Type.__name__ = "InetAddress"
_VRtrLdpAddrFecOutLblNxtHopAddr6_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopAddr6 = _VRtrLdpAddrFecOutLblNxtHopAddr6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 5),
    _VRtrLdpAddrFecOutLblNxtHopAddr6_Type()
)
vRtrLdpAddrFecOutLblNxtHopAddr6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopAddr6.setStatus("obsolete")
_VRtrLdpAddrFecLspId6_Type = TmnxVRtrMplsLspID
_VRtrLdpAddrFecLspId6_Object = MibTableColumn
vRtrLdpAddrFecLspId6 = _VRtrLdpAddrFecLspId6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 6),
    _VRtrLdpAddrFecLspId6_Type()
)
vRtrLdpAddrFecLspId6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecLspId6.setStatus("obsolete")
_VRtrLdpAddrFecOutLbl7_Type = Unsigned32
_VRtrLdpAddrFecOutLbl7_Object = MibTableColumn
vRtrLdpAddrFecOutLbl7 = _VRtrLdpAddrFecOutLbl7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 7),
    _VRtrLdpAddrFecOutLbl7_Type()
)
vRtrLdpAddrFecOutLbl7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLbl7.setStatus("obsolete")
_VRtrLdpAddrFecOutLblStatus7_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLblStatus7_Object = MibTableColumn
vRtrLdpAddrFecOutLblStatus7 = _VRtrLdpAddrFecOutLblStatus7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 8),
    _VRtrLdpAddrFecOutLblStatus7_Type()
)
vRtrLdpAddrFecOutLblStatus7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblStatus7.setStatus("obsolete")
_VRtrLdpAddrFecOutLblIfIndex7_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLblIfIndex7_Object = MibTableColumn
vRtrLdpAddrFecOutLblIfIndex7 = _VRtrLdpAddrFecOutLblIfIndex7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 9),
    _VRtrLdpAddrFecOutLblIfIndex7_Type()
)
vRtrLdpAddrFecOutLblIfIndex7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblIfIndex7.setStatus("obsolete")
_VRtrLdpAddrFecOutLblNxtHopType7_Type = InetAddressType
_VRtrLdpAddrFecOutLblNxtHopType7_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopType7 = _VRtrLdpAddrFecOutLblNxtHopType7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 10),
    _VRtrLdpAddrFecOutLblNxtHopType7_Type()
)
vRtrLdpAddrFecOutLblNxtHopType7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopType7.setStatus("obsolete")


class _VRtrLdpAddrFecOutLblNxtHopAddr7_Type(InetAddress):
    """Custom type vRtrLdpAddrFecOutLblNxtHopAddr7 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpAddrFecOutLblNxtHopAddr7_Type.__name__ = "InetAddress"
_VRtrLdpAddrFecOutLblNxtHopAddr7_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopAddr7 = _VRtrLdpAddrFecOutLblNxtHopAddr7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 11),
    _VRtrLdpAddrFecOutLblNxtHopAddr7_Type()
)
vRtrLdpAddrFecOutLblNxtHopAddr7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopAddr7.setStatus("obsolete")
_VRtrLdpAddrFecLspId7_Type = TmnxVRtrMplsLspID
_VRtrLdpAddrFecLspId7_Object = MibTableColumn
vRtrLdpAddrFecLspId7 = _VRtrLdpAddrFecLspId7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 12),
    _VRtrLdpAddrFecLspId7_Type()
)
vRtrLdpAddrFecLspId7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecLspId7.setStatus("obsolete")
_VRtrLdpAddrFecOutLbl8_Type = Unsigned32
_VRtrLdpAddrFecOutLbl8_Object = MibTableColumn
vRtrLdpAddrFecOutLbl8 = _VRtrLdpAddrFecOutLbl8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 13),
    _VRtrLdpAddrFecOutLbl8_Type()
)
vRtrLdpAddrFecOutLbl8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLbl8.setStatus("obsolete")
_VRtrLdpAddrFecOutLblStatus8_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLblStatus8_Object = MibTableColumn
vRtrLdpAddrFecOutLblStatus8 = _VRtrLdpAddrFecOutLblStatus8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 14),
    _VRtrLdpAddrFecOutLblStatus8_Type()
)
vRtrLdpAddrFecOutLblStatus8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblStatus8.setStatus("obsolete")
_VRtrLdpAddrFecOutLblIfIndex8_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLblIfIndex8_Object = MibTableColumn
vRtrLdpAddrFecOutLblIfIndex8 = _VRtrLdpAddrFecOutLblIfIndex8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 15),
    _VRtrLdpAddrFecOutLblIfIndex8_Type()
)
vRtrLdpAddrFecOutLblIfIndex8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblIfIndex8.setStatus("obsolete")
_VRtrLdpAddrFecOutLblNxtHopType8_Type = InetAddressType
_VRtrLdpAddrFecOutLblNxtHopType8_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopType8 = _VRtrLdpAddrFecOutLblNxtHopType8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 16),
    _VRtrLdpAddrFecOutLblNxtHopType8_Type()
)
vRtrLdpAddrFecOutLblNxtHopType8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopType8.setStatus("obsolete")


class _VRtrLdpAddrFecOutLblNxtHopAddr8_Type(InetAddress):
    """Custom type vRtrLdpAddrFecOutLblNxtHopAddr8 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpAddrFecOutLblNxtHopAddr8_Type.__name__ = "InetAddress"
_VRtrLdpAddrFecOutLblNxtHopAddr8_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopAddr8 = _VRtrLdpAddrFecOutLblNxtHopAddr8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 17),
    _VRtrLdpAddrFecOutLblNxtHopAddr8_Type()
)
vRtrLdpAddrFecOutLblNxtHopAddr8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopAddr8.setStatus("obsolete")
_VRtrLdpAddrFecLspId8_Type = TmnxVRtrMplsLspID
_VRtrLdpAddrFecLspId8_Object = MibTableColumn
vRtrLdpAddrFecLspId8 = _VRtrLdpAddrFecLspId8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 18),
    _VRtrLdpAddrFecLspId8_Type()
)
vRtrLdpAddrFecLspId8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecLspId8.setStatus("obsolete")
_VRtrLdpAddrFecOutLbl9_Type = Unsigned32
_VRtrLdpAddrFecOutLbl9_Object = MibTableColumn
vRtrLdpAddrFecOutLbl9 = _VRtrLdpAddrFecOutLbl9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 19),
    _VRtrLdpAddrFecOutLbl9_Type()
)
vRtrLdpAddrFecOutLbl9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLbl9.setStatus("obsolete")
_VRtrLdpAddrFecOutLblStatus9_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLblStatus9_Object = MibTableColumn
vRtrLdpAddrFecOutLblStatus9 = _VRtrLdpAddrFecOutLblStatus9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 20),
    _VRtrLdpAddrFecOutLblStatus9_Type()
)
vRtrLdpAddrFecOutLblStatus9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblStatus9.setStatus("obsolete")
_VRtrLdpAddrFecOutLblIfIndex9_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLblIfIndex9_Object = MibTableColumn
vRtrLdpAddrFecOutLblIfIndex9 = _VRtrLdpAddrFecOutLblIfIndex9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 21),
    _VRtrLdpAddrFecOutLblIfIndex9_Type()
)
vRtrLdpAddrFecOutLblIfIndex9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblIfIndex9.setStatus("obsolete")
_VRtrLdpAddrFecOutLblNxtHopType9_Type = InetAddressType
_VRtrLdpAddrFecOutLblNxtHopType9_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopType9 = _VRtrLdpAddrFecOutLblNxtHopType9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 22),
    _VRtrLdpAddrFecOutLblNxtHopType9_Type()
)
vRtrLdpAddrFecOutLblNxtHopType9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopType9.setStatus("obsolete")


class _VRtrLdpAddrFecOutLblNxtHopAddr9_Type(InetAddress):
    """Custom type vRtrLdpAddrFecOutLblNxtHopAddr9 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpAddrFecOutLblNxtHopAddr9_Type.__name__ = "InetAddress"
_VRtrLdpAddrFecOutLblNxtHopAddr9_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopAddr9 = _VRtrLdpAddrFecOutLblNxtHopAddr9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 23),
    _VRtrLdpAddrFecOutLblNxtHopAddr9_Type()
)
vRtrLdpAddrFecOutLblNxtHopAddr9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopAddr9.setStatus("obsolete")
_VRtrLdpAddrFecLspId9_Type = TmnxVRtrMplsLspID
_VRtrLdpAddrFecLspId9_Object = MibTableColumn
vRtrLdpAddrFecLspId9 = _VRtrLdpAddrFecLspId9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 24),
    _VRtrLdpAddrFecLspId9_Type()
)
vRtrLdpAddrFecLspId9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecLspId9.setStatus("obsolete")
_VRtrLdpAddrFecOutLbl10_Type = Unsigned32
_VRtrLdpAddrFecOutLbl10_Object = MibTableColumn
vRtrLdpAddrFecOutLbl10 = _VRtrLdpAddrFecOutLbl10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 25),
    _VRtrLdpAddrFecOutLbl10_Type()
)
vRtrLdpAddrFecOutLbl10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLbl10.setStatus("obsolete")
_VRtrLdpAddrFecOutLblStatus10_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLblStatus10_Object = MibTableColumn
vRtrLdpAddrFecOutLblStatus10 = _VRtrLdpAddrFecOutLblStatus10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 26),
    _VRtrLdpAddrFecOutLblStatus10_Type()
)
vRtrLdpAddrFecOutLblStatus10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblStatus10.setStatus("obsolete")
_VRtrLdpAddrFecOutLblIfIndex10_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLblIfIndex10_Object = MibTableColumn
vRtrLdpAddrFecOutLblIfIndex10 = _VRtrLdpAddrFecOutLblIfIndex10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 27),
    _VRtrLdpAddrFecOutLblIfIndex10_Type()
)
vRtrLdpAddrFecOutLblIfIndex10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblIfIndex10.setStatus("obsolete")
_VRtrLdpAddrFecOutLblNxtHopType10_Type = InetAddressType
_VRtrLdpAddrFecOutLblNxtHopType10_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopType10 = _VRtrLdpAddrFecOutLblNxtHopType10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 28),
    _VRtrLdpAddrFecOutLblNxtHopType10_Type()
)
vRtrLdpAddrFecOutLblNxtHopType10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopType10.setStatus("obsolete")


class _VRtrLdpAddrFecOutLblNxtHopAddr10_Type(InetAddress):
    """Custom type vRtrLdpAddrFecOutLblNxtHopAddr10 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpAddrFecOutLblNxtHopAddr10_Type.__name__ = "InetAddress"
_VRtrLdpAddrFecOutLblNxtHopAddr10_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopAddr10 = _VRtrLdpAddrFecOutLblNxtHopAddr10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 29),
    _VRtrLdpAddrFecOutLblNxtHopAddr10_Type()
)
vRtrLdpAddrFecOutLblNxtHopAddr10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopAddr10.setStatus("obsolete")
_VRtrLdpAddrFecLspId10_Type = TmnxVRtrMplsLspID
_VRtrLdpAddrFecLspId10_Object = MibTableColumn
vRtrLdpAddrFecLspId10 = _VRtrLdpAddrFecLspId10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 30),
    _VRtrLdpAddrFecLspId10_Type()
)
vRtrLdpAddrFecLspId10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecLspId10.setStatus("obsolete")
_VRtrLdpAddrFecOutLbl11_Type = Unsigned32
_VRtrLdpAddrFecOutLbl11_Object = MibTableColumn
vRtrLdpAddrFecOutLbl11 = _VRtrLdpAddrFecOutLbl11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 31),
    _VRtrLdpAddrFecOutLbl11_Type()
)
vRtrLdpAddrFecOutLbl11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLbl11.setStatus("obsolete")
_VRtrLdpAddrFecOutLblStatus11_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLblStatus11_Object = MibTableColumn
vRtrLdpAddrFecOutLblStatus11 = _VRtrLdpAddrFecOutLblStatus11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 32),
    _VRtrLdpAddrFecOutLblStatus11_Type()
)
vRtrLdpAddrFecOutLblStatus11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblStatus11.setStatus("obsolete")
_VRtrLdpAddrFecOutLblIfIndex11_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLblIfIndex11_Object = MibTableColumn
vRtrLdpAddrFecOutLblIfIndex11 = _VRtrLdpAddrFecOutLblIfIndex11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 33),
    _VRtrLdpAddrFecOutLblIfIndex11_Type()
)
vRtrLdpAddrFecOutLblIfIndex11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblIfIndex11.setStatus("obsolete")
_VRtrLdpAddrFecOutLblNxtHopType11_Type = InetAddressType
_VRtrLdpAddrFecOutLblNxtHopType11_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopType11 = _VRtrLdpAddrFecOutLblNxtHopType11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 34),
    _VRtrLdpAddrFecOutLblNxtHopType11_Type()
)
vRtrLdpAddrFecOutLblNxtHopType11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopType11.setStatus("obsolete")


class _VRtrLdpAddrFecOutLblNxtHopAddr11_Type(InetAddress):
    """Custom type vRtrLdpAddrFecOutLblNxtHopAddr11 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpAddrFecOutLblNxtHopAddr11_Type.__name__ = "InetAddress"
_VRtrLdpAddrFecOutLblNxtHopAddr11_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopAddr11 = _VRtrLdpAddrFecOutLblNxtHopAddr11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 35),
    _VRtrLdpAddrFecOutLblNxtHopAddr11_Type()
)
vRtrLdpAddrFecOutLblNxtHopAddr11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopAddr11.setStatus("obsolete")
_VRtrLdpAddrFecLspId11_Type = TmnxVRtrMplsLspID
_VRtrLdpAddrFecLspId11_Object = MibTableColumn
vRtrLdpAddrFecLspId11 = _VRtrLdpAddrFecLspId11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 36),
    _VRtrLdpAddrFecLspId11_Type()
)
vRtrLdpAddrFecLspId11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecLspId11.setStatus("obsolete")
_VRtrLdpAddrFecOutLbl12_Type = Unsigned32
_VRtrLdpAddrFecOutLbl12_Object = MibTableColumn
vRtrLdpAddrFecOutLbl12 = _VRtrLdpAddrFecOutLbl12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 37),
    _VRtrLdpAddrFecOutLbl12_Type()
)
vRtrLdpAddrFecOutLbl12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLbl12.setStatus("obsolete")
_VRtrLdpAddrFecOutLblStatus12_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLblStatus12_Object = MibTableColumn
vRtrLdpAddrFecOutLblStatus12 = _VRtrLdpAddrFecOutLblStatus12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 38),
    _VRtrLdpAddrFecOutLblStatus12_Type()
)
vRtrLdpAddrFecOutLblStatus12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblStatus12.setStatus("obsolete")
_VRtrLdpAddrFecOutLblIfIndex12_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLblIfIndex12_Object = MibTableColumn
vRtrLdpAddrFecOutLblIfIndex12 = _VRtrLdpAddrFecOutLblIfIndex12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 39),
    _VRtrLdpAddrFecOutLblIfIndex12_Type()
)
vRtrLdpAddrFecOutLblIfIndex12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblIfIndex12.setStatus("obsolete")
_VRtrLdpAddrFecOutLblNxtHopType12_Type = InetAddressType
_VRtrLdpAddrFecOutLblNxtHopType12_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopType12 = _VRtrLdpAddrFecOutLblNxtHopType12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 40),
    _VRtrLdpAddrFecOutLblNxtHopType12_Type()
)
vRtrLdpAddrFecOutLblNxtHopType12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopType12.setStatus("obsolete")


class _VRtrLdpAddrFecOutLblNxtHopAddr12_Type(InetAddress):
    """Custom type vRtrLdpAddrFecOutLblNxtHopAddr12 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpAddrFecOutLblNxtHopAddr12_Type.__name__ = "InetAddress"
_VRtrLdpAddrFecOutLblNxtHopAddr12_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopAddr12 = _VRtrLdpAddrFecOutLblNxtHopAddr12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 41),
    _VRtrLdpAddrFecOutLblNxtHopAddr12_Type()
)
vRtrLdpAddrFecOutLblNxtHopAddr12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopAddr12.setStatus("obsolete")
_VRtrLdpAddrFecLspId12_Type = TmnxVRtrMplsLspID
_VRtrLdpAddrFecLspId12_Object = MibTableColumn
vRtrLdpAddrFecLspId12 = _VRtrLdpAddrFecLspId12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 42),
    _VRtrLdpAddrFecLspId12_Type()
)
vRtrLdpAddrFecLspId12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecLspId12.setStatus("obsolete")
_VRtrLdpAddrFecOutLbl13_Type = Unsigned32
_VRtrLdpAddrFecOutLbl13_Object = MibTableColumn
vRtrLdpAddrFecOutLbl13 = _VRtrLdpAddrFecOutLbl13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 43),
    _VRtrLdpAddrFecOutLbl13_Type()
)
vRtrLdpAddrFecOutLbl13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLbl13.setStatus("obsolete")
_VRtrLdpAddrFecOutLblStatus13_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLblStatus13_Object = MibTableColumn
vRtrLdpAddrFecOutLblStatus13 = _VRtrLdpAddrFecOutLblStatus13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 44),
    _VRtrLdpAddrFecOutLblStatus13_Type()
)
vRtrLdpAddrFecOutLblStatus13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblStatus13.setStatus("obsolete")
_VRtrLdpAddrFecOutLblIfIndex13_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLblIfIndex13_Object = MibTableColumn
vRtrLdpAddrFecOutLblIfIndex13 = _VRtrLdpAddrFecOutLblIfIndex13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 45),
    _VRtrLdpAddrFecOutLblIfIndex13_Type()
)
vRtrLdpAddrFecOutLblIfIndex13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblIfIndex13.setStatus("obsolete")
_VRtrLdpAddrFecOutLblNxtHopType13_Type = InetAddressType
_VRtrLdpAddrFecOutLblNxtHopType13_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopType13 = _VRtrLdpAddrFecOutLblNxtHopType13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 46),
    _VRtrLdpAddrFecOutLblNxtHopType13_Type()
)
vRtrLdpAddrFecOutLblNxtHopType13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopType13.setStatus("obsolete")


class _VRtrLdpAddrFecOutLblNxtHopAddr13_Type(InetAddress):
    """Custom type vRtrLdpAddrFecOutLblNxtHopAddr13 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpAddrFecOutLblNxtHopAddr13_Type.__name__ = "InetAddress"
_VRtrLdpAddrFecOutLblNxtHopAddr13_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopAddr13 = _VRtrLdpAddrFecOutLblNxtHopAddr13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 47),
    _VRtrLdpAddrFecOutLblNxtHopAddr13_Type()
)
vRtrLdpAddrFecOutLblNxtHopAddr13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopAddr13.setStatus("obsolete")
_VRtrLdpAddrFecLspId13_Type = TmnxVRtrMplsLspID
_VRtrLdpAddrFecLspId13_Object = MibTableColumn
vRtrLdpAddrFecLspId13 = _VRtrLdpAddrFecLspId13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 48),
    _VRtrLdpAddrFecLspId13_Type()
)
vRtrLdpAddrFecLspId13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecLspId13.setStatus("obsolete")
_VRtrLdpAddrFecOutLbl14_Type = Unsigned32
_VRtrLdpAddrFecOutLbl14_Object = MibTableColumn
vRtrLdpAddrFecOutLbl14 = _VRtrLdpAddrFecOutLbl14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 49),
    _VRtrLdpAddrFecOutLbl14_Type()
)
vRtrLdpAddrFecOutLbl14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLbl14.setStatus("obsolete")
_VRtrLdpAddrFecOutLblStatus14_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLblStatus14_Object = MibTableColumn
vRtrLdpAddrFecOutLblStatus14 = _VRtrLdpAddrFecOutLblStatus14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 50),
    _VRtrLdpAddrFecOutLblStatus14_Type()
)
vRtrLdpAddrFecOutLblStatus14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblStatus14.setStatus("obsolete")
_VRtrLdpAddrFecOutLblIfIndex14_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLblIfIndex14_Object = MibTableColumn
vRtrLdpAddrFecOutLblIfIndex14 = _VRtrLdpAddrFecOutLblIfIndex14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 51),
    _VRtrLdpAddrFecOutLblIfIndex14_Type()
)
vRtrLdpAddrFecOutLblIfIndex14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblIfIndex14.setStatus("obsolete")
_VRtrLdpAddrFecOutLblNxtHopType14_Type = InetAddressType
_VRtrLdpAddrFecOutLblNxtHopType14_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopType14 = _VRtrLdpAddrFecOutLblNxtHopType14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 52),
    _VRtrLdpAddrFecOutLblNxtHopType14_Type()
)
vRtrLdpAddrFecOutLblNxtHopType14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopType14.setStatus("obsolete")


class _VRtrLdpAddrFecOutLblNxtHopAddr14_Type(InetAddress):
    """Custom type vRtrLdpAddrFecOutLblNxtHopAddr14 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpAddrFecOutLblNxtHopAddr14_Type.__name__ = "InetAddress"
_VRtrLdpAddrFecOutLblNxtHopAddr14_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopAddr14 = _VRtrLdpAddrFecOutLblNxtHopAddr14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 53),
    _VRtrLdpAddrFecOutLblNxtHopAddr14_Type()
)
vRtrLdpAddrFecOutLblNxtHopAddr14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopAddr14.setStatus("obsolete")
_VRtrLdpAddrFecLspId14_Type = TmnxVRtrMplsLspID
_VRtrLdpAddrFecLspId14_Object = MibTableColumn
vRtrLdpAddrFecLspId14 = _VRtrLdpAddrFecLspId14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 54),
    _VRtrLdpAddrFecLspId14_Type()
)
vRtrLdpAddrFecLspId14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecLspId14.setStatus("obsolete")
_VRtrLdpAddrFecOutLbl15_Type = Unsigned32
_VRtrLdpAddrFecOutLbl15_Object = MibTableColumn
vRtrLdpAddrFecOutLbl15 = _VRtrLdpAddrFecOutLbl15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 55),
    _VRtrLdpAddrFecOutLbl15_Type()
)
vRtrLdpAddrFecOutLbl15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLbl15.setStatus("obsolete")
_VRtrLdpAddrFecOutLblStatus15_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLblStatus15_Object = MibTableColumn
vRtrLdpAddrFecOutLblStatus15 = _VRtrLdpAddrFecOutLblStatus15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 56),
    _VRtrLdpAddrFecOutLblStatus15_Type()
)
vRtrLdpAddrFecOutLblStatus15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblStatus15.setStatus("obsolete")
_VRtrLdpAddrFecOutLblIfIndex15_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLblIfIndex15_Object = MibTableColumn
vRtrLdpAddrFecOutLblIfIndex15 = _VRtrLdpAddrFecOutLblIfIndex15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 57),
    _VRtrLdpAddrFecOutLblIfIndex15_Type()
)
vRtrLdpAddrFecOutLblIfIndex15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblIfIndex15.setStatus("obsolete")
_VRtrLdpAddrFecOutLblNxtHopType15_Type = InetAddressType
_VRtrLdpAddrFecOutLblNxtHopType15_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopType15 = _VRtrLdpAddrFecOutLblNxtHopType15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 58),
    _VRtrLdpAddrFecOutLblNxtHopType15_Type()
)
vRtrLdpAddrFecOutLblNxtHopType15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopType15.setStatus("obsolete")


class _VRtrLdpAddrFecOutLblNxtHopAddr15_Type(InetAddress):
    """Custom type vRtrLdpAddrFecOutLblNxtHopAddr15 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpAddrFecOutLblNxtHopAddr15_Type.__name__ = "InetAddress"
_VRtrLdpAddrFecOutLblNxtHopAddr15_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopAddr15 = _VRtrLdpAddrFecOutLblNxtHopAddr15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 59),
    _VRtrLdpAddrFecOutLblNxtHopAddr15_Type()
)
vRtrLdpAddrFecOutLblNxtHopAddr15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopAddr15.setStatus("obsolete")
_VRtrLdpAddrFecLspId15_Type = TmnxVRtrMplsLspID
_VRtrLdpAddrFecLspId15_Object = MibTableColumn
vRtrLdpAddrFecLspId15 = _VRtrLdpAddrFecLspId15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 60),
    _VRtrLdpAddrFecLspId15_Type()
)
vRtrLdpAddrFecLspId15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecLspId15.setStatus("obsolete")
_VRtrLdpAddrFecOutLbl16_Type = Unsigned32
_VRtrLdpAddrFecOutLbl16_Object = MibTableColumn
vRtrLdpAddrFecOutLbl16 = _VRtrLdpAddrFecOutLbl16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 61),
    _VRtrLdpAddrFecOutLbl16_Type()
)
vRtrLdpAddrFecOutLbl16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLbl16.setStatus("obsolete")
_VRtrLdpAddrFecOutLblStatus16_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLblStatus16_Object = MibTableColumn
vRtrLdpAddrFecOutLblStatus16 = _VRtrLdpAddrFecOutLblStatus16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 62),
    _VRtrLdpAddrFecOutLblStatus16_Type()
)
vRtrLdpAddrFecOutLblStatus16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblStatus16.setStatus("obsolete")
_VRtrLdpAddrFecOutLblIfIndex16_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLblIfIndex16_Object = MibTableColumn
vRtrLdpAddrFecOutLblIfIndex16 = _VRtrLdpAddrFecOutLblIfIndex16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 63),
    _VRtrLdpAddrFecOutLblIfIndex16_Type()
)
vRtrLdpAddrFecOutLblIfIndex16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblIfIndex16.setStatus("obsolete")
_VRtrLdpAddrFecOutLblNxtHopType16_Type = InetAddressType
_VRtrLdpAddrFecOutLblNxtHopType16_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopType16 = _VRtrLdpAddrFecOutLblNxtHopType16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 64),
    _VRtrLdpAddrFecOutLblNxtHopType16_Type()
)
vRtrLdpAddrFecOutLblNxtHopType16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopType16.setStatus("obsolete")


class _VRtrLdpAddrFecOutLblNxtHopAddr16_Type(InetAddress):
    """Custom type vRtrLdpAddrFecOutLblNxtHopAddr16 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpAddrFecOutLblNxtHopAddr16_Type.__name__ = "InetAddress"
_VRtrLdpAddrFecOutLblNxtHopAddr16_Object = MibTableColumn
vRtrLdpAddrFecOutLblNxtHopAddr16 = _VRtrLdpAddrFecOutLblNxtHopAddr16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 65),
    _VRtrLdpAddrFecOutLblNxtHopAddr16_Type()
)
vRtrLdpAddrFecOutLblNxtHopAddr16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblNxtHopAddr16.setStatus("obsolete")
_VRtrLdpAddrFecLspId16_Type = TmnxVRtrMplsLspID
_VRtrLdpAddrFecLspId16_Object = MibTableColumn
vRtrLdpAddrFecLspId16 = _VRtrLdpAddrFecLspId16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 30, 1, 66),
    _VRtrLdpAddrFecLspId16_Type()
)
vRtrLdpAddrFecLspId16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecLspId16.setStatus("obsolete")
_VRtrLdpP2MPFecTable_Object = MibTable
vRtrLdpP2MPFecTable = _VRtrLdpP2MPFecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 31)
)
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecTable.setStatus("obsolete")
_VRtrLdpP2MPFecEntry_Object = MibTableRow
vRtrLdpP2MPFecEntry = _VRtrLdpP2MPFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 31, 1)
)
vRtrLdpP2MPFecEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpP2MPFecRootAddrType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpP2MPFecRootAddress"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpP2MPFecTunnelType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpP2MPFecTunnelId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecEntry.setStatus("obsolete")
_VRtrLdpP2MPFecTunnelType_Type = TmnxLdpFECTunnelType
_VRtrLdpP2MPFecTunnelType_Object = MibTableColumn
vRtrLdpP2MPFecTunnelType = _VRtrLdpP2MPFecTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 31, 1, 1),
    _VRtrLdpP2MPFecTunnelType_Type()
)
vRtrLdpP2MPFecTunnelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecTunnelType.setStatus("obsolete")
_VRtrLdpP2MPFecTunnelId_Type = Unsigned32
_VRtrLdpP2MPFecTunnelId_Object = MibTableColumn
vRtrLdpP2MPFecTunnelId = _VRtrLdpP2MPFecTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 31, 1, 2),
    _VRtrLdpP2MPFecTunnelId_Type()
)
vRtrLdpP2MPFecTunnelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecTunnelId.setStatus("obsolete")
_VRtrLdpP2MPFecRootAddrType_Type = InetAddressType
_VRtrLdpP2MPFecRootAddrType_Object = MibTableColumn
vRtrLdpP2MPFecRootAddrType = _VRtrLdpP2MPFecRootAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 31, 1, 3),
    _VRtrLdpP2MPFecRootAddrType_Type()
)
vRtrLdpP2MPFecRootAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecRootAddrType.setStatus("obsolete")


class _VRtrLdpP2MPFecRootAddress_Type(InetAddress):
    """Custom type vRtrLdpP2MPFecRootAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrLdpP2MPFecRootAddress_Type.__name__ = "InetAddress"
_VRtrLdpP2MPFecRootAddress_Object = MibTableColumn
vRtrLdpP2MPFecRootAddress = _VRtrLdpP2MPFecRootAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 31, 1, 4),
    _VRtrLdpP2MPFecRootAddress_Type()
)
vRtrLdpP2MPFecRootAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecRootAddress.setStatus("obsolete")
_VRtrLdpP2MPFecFlags_Type = TmnxLdpFECFlags
_VRtrLdpP2MPFecFlags_Object = MibTableColumn
vRtrLdpP2MPFecFlags = _VRtrLdpP2MPFecFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 31, 1, 5),
    _VRtrLdpP2MPFecFlags_Type()
)
vRtrLdpP2MPFecFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecFlags.setStatus("obsolete")
_VRtrLdpP2MPFecNumInLabels_Type = Gauge32
_VRtrLdpP2MPFecNumInLabels_Object = MibTableColumn
vRtrLdpP2MPFecNumInLabels = _VRtrLdpP2MPFecNumInLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 31, 1, 6),
    _VRtrLdpP2MPFecNumInLabels_Type()
)
vRtrLdpP2MPFecNumInLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecNumInLabels.setStatus("obsolete")
_VRtrLdpP2MPFecNumOutLabels_Type = Gauge32
_VRtrLdpP2MPFecNumOutLabels_Object = MibTableColumn
vRtrLdpP2MPFecNumOutLabels = _VRtrLdpP2MPFecNumOutLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 31, 1, 7),
    _VRtrLdpP2MPFecNumOutLabels_Type()
)
vRtrLdpP2MPFecNumOutLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecNumOutLabels.setStatus("obsolete")
_VRtrLdpP2MPFecTunnelIfId_Type = Unsigned32
_VRtrLdpP2MPFecTunnelIfId_Object = MibTableColumn
vRtrLdpP2MPFecTunnelIfId = _VRtrLdpP2MPFecTunnelIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 31, 1, 8),
    _VRtrLdpP2MPFecTunnelIfId_Type()
)
vRtrLdpP2MPFecTunnelIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecTunnelIfId.setStatus("obsolete")
_VRtrLdpP2MPFecMetric_Type = Unsigned32
_VRtrLdpP2MPFecMetric_Object = MibTableColumn
vRtrLdpP2MPFecMetric = _VRtrLdpP2MPFecMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 31, 1, 9),
    _VRtrLdpP2MPFecMetric_Type()
)
vRtrLdpP2MPFecMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecMetric.setStatus("obsolete")
_VRtrLdpP2MPFecMTU_Type = Unsigned32
_VRtrLdpP2MPFecMTU_Object = MibTableColumn
vRtrLdpP2MPFecMTU = _VRtrLdpP2MPFecMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 31, 1, 10),
    _VRtrLdpP2MPFecMTU_Type()
)
vRtrLdpP2MPFecMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecMTU.setStatus("obsolete")
_VRtrLdpP2MPFecInLabelTable_Object = MibTable
vRtrLdpP2MPFecInLabelTable = _VRtrLdpP2MPFecInLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 32)
)
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecInLabelTable.setStatus("obsolete")
_VRtrLdpP2MPFecInLabelEntry_Object = MibTableRow
vRtrLdpP2MPFecInLabelEntry = _VRtrLdpP2MPFecInLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 32, 1)
)
vRtrLdpP2MPFecInLabelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpP2MPFecRootAddrType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpP2MPFecRootAddress"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpP2MPFecTunnelType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpP2MPFecTunnelId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpP2MPFecInLblId"),
)
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecInLabelEntry.setStatus("obsolete")
_VRtrLdpP2MPFecInLblId_Type = Unsigned32
_VRtrLdpP2MPFecInLblId_Object = MibTableColumn
vRtrLdpP2MPFecInLblId = _VRtrLdpP2MPFecInLblId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 32, 1, 1),
    _VRtrLdpP2MPFecInLblId_Type()
)
vRtrLdpP2MPFecInLblId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecInLblId.setStatus("obsolete")
_VRtrLdpP2MPFecInLbl_Type = Unsigned32
_VRtrLdpP2MPFecInLbl_Object = MibTableColumn
vRtrLdpP2MPFecInLbl = _VRtrLdpP2MPFecInLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 32, 1, 2),
    _VRtrLdpP2MPFecInLbl_Type()
)
vRtrLdpP2MPFecInLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecInLbl.setStatus("obsolete")
_VRtrLdpP2MPFecInLblStatus_Type = TmnxLabelStatus
_VRtrLdpP2MPFecInLblStatus_Object = MibTableColumn
vRtrLdpP2MPFecInLblStatus = _VRtrLdpP2MPFecInLblStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 32, 1, 3),
    _VRtrLdpP2MPFecInLblStatus_Type()
)
vRtrLdpP2MPFecInLblStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecInLblStatus.setStatus("obsolete")
_VRtrLdpP2MPFecInLblIfIndex_Type = InterfaceIndexOrZero
_VRtrLdpP2MPFecInLblIfIndex_Object = MibTableColumn
vRtrLdpP2MPFecInLblIfIndex = _VRtrLdpP2MPFecInLblIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 32, 1, 4),
    _VRtrLdpP2MPFecInLblIfIndex_Type()
)
vRtrLdpP2MPFecInLblIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecInLblIfIndex.setStatus("obsolete")
_VRtrLdpP2MPFecOutLabelTable_Object = MibTable
vRtrLdpP2MPFecOutLabelTable = _VRtrLdpP2MPFecOutLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 33)
)
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecOutLabelTable.setStatus("obsolete")
_VRtrLdpP2MPFecOutLabelEntry_Object = MibTableRow
vRtrLdpP2MPFecOutLabelEntry = _VRtrLdpP2MPFecOutLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 33, 1)
)
vRtrLdpP2MPFecOutLabelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpP2MPFecRootAddrType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpP2MPFecRootAddress"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpP2MPFecTunnelType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpP2MPFecTunnelId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpP2MPFecOutLblId"),
)
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecOutLabelEntry.setStatus("obsolete")
_VRtrLdpP2MPFecOutLblId_Type = Unsigned32
_VRtrLdpP2MPFecOutLblId_Object = MibTableColumn
vRtrLdpP2MPFecOutLblId = _VRtrLdpP2MPFecOutLblId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 33, 1, 1),
    _VRtrLdpP2MPFecOutLblId_Type()
)
vRtrLdpP2MPFecOutLblId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecOutLblId.setStatus("obsolete")
_VRtrLdpP2MPFecOutLbl_Type = Unsigned32
_VRtrLdpP2MPFecOutLbl_Object = MibTableColumn
vRtrLdpP2MPFecOutLbl = _VRtrLdpP2MPFecOutLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 33, 1, 2),
    _VRtrLdpP2MPFecOutLbl_Type()
)
vRtrLdpP2MPFecOutLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecOutLbl.setStatus("obsolete")
_VRtrLdpP2MPFecOutLblStatus_Type = TmnxLabelStatus
_VRtrLdpP2MPFecOutLblStatus_Object = MibTableColumn
vRtrLdpP2MPFecOutLblStatus = _VRtrLdpP2MPFecOutLblStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 33, 1, 3),
    _VRtrLdpP2MPFecOutLblStatus_Type()
)
vRtrLdpP2MPFecOutLblStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecOutLblStatus.setStatus("obsolete")
_VRtrLdpP2MPFecOutLblNxtHopType_Type = InetAddressType
_VRtrLdpP2MPFecOutLblNxtHopType_Object = MibTableColumn
vRtrLdpP2MPFecOutLblNxtHopType = _VRtrLdpP2MPFecOutLblNxtHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 33, 1, 4),
    _VRtrLdpP2MPFecOutLblNxtHopType_Type()
)
vRtrLdpP2MPFecOutLblNxtHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecOutLblNxtHopType.setStatus("obsolete")


class _VRtrLdpP2MPFecOutLblNxtHopAddr_Type(InetAddress):
    """Custom type vRtrLdpP2MPFecOutLblNxtHopAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpP2MPFecOutLblNxtHopAddr_Type.__name__ = "InetAddress"
_VRtrLdpP2MPFecOutLblNxtHopAddr_Object = MibTableColumn
vRtrLdpP2MPFecOutLblNxtHopAddr = _VRtrLdpP2MPFecOutLblNxtHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 33, 1, 5),
    _VRtrLdpP2MPFecOutLblNxtHopAddr_Type()
)
vRtrLdpP2MPFecOutLblNxtHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecOutLblNxtHopAddr.setStatus("obsolete")
_VRtrLdpP2MPFecOutLblIfIndex_Type = InterfaceIndexOrZero
_VRtrLdpP2MPFecOutLblIfIndex_Object = MibTableColumn
vRtrLdpP2MPFecOutLblIfIndex = _VRtrLdpP2MPFecOutLblIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 33, 1, 6),
    _VRtrLdpP2MPFecOutLblIfIndex_Type()
)
vRtrLdpP2MPFecOutLblIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecOutLblIfIndex.setStatus("obsolete")
_VRtrLdpP2MPFecOutLblLspId_Type = TmnxVRtrMplsLspID
_VRtrLdpP2MPFecOutLblLspId_Object = MibTableColumn
vRtrLdpP2MPFecOutLblLspId = _VRtrLdpP2MPFecOutLblLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 33, 1, 7),
    _VRtrLdpP2MPFecOutLblLspId_Type()
)
vRtrLdpP2MPFecOutLblLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecOutLblLspId.setStatus("obsolete")
_VRtrLdpP2MPFecMapTable_Object = MibTable
vRtrLdpP2MPFecMapTable = _VRtrLdpP2MPFecMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 34)
)
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecMapTable.setStatus("obsolete")
_VRtrLdpP2MPFecMapEntry_Object = MibTableRow
vRtrLdpP2MPFecMapEntry = _VRtrLdpP2MPFecMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 34, 1)
)
vRtrLdpP2MPFecMapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpP2MPFecRootAddrType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpP2MPFecRootAddress"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpP2MPFecMapFecType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpP2MPFecMapId"),
)
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecMapEntry.setStatus("obsolete")
_VRtrLdpP2MPFecMapFecType_Type = TmnxLdpFECTunnelType
_VRtrLdpP2MPFecMapFecType_Object = MibTableColumn
vRtrLdpP2MPFecMapFecType = _VRtrLdpP2MPFecMapFecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 34, 1, 1),
    _VRtrLdpP2MPFecMapFecType_Type()
)
vRtrLdpP2MPFecMapFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecMapFecType.setStatus("obsolete")
_VRtrLdpP2MPFecMapId_Type = Unsigned32
_VRtrLdpP2MPFecMapId_Object = MibTableColumn
vRtrLdpP2MPFecMapId = _VRtrLdpP2MPFecMapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 34, 1, 2),
    _VRtrLdpP2MPFecMapId_Type()
)
vRtrLdpP2MPFecMapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpP2MPFecMapId.setStatus("obsolete")
_VRtrLdpAddrFecOutLblInfoTable_Object = MibTable
vRtrLdpAddrFecOutLblInfoTable = _VRtrLdpAddrFecOutLblInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 35)
)
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblInfoTable.setStatus("obsolete")
_VRtrLdpAddrFecOutLblInfoEntry_Object = MibTableRow
vRtrLdpAddrFecOutLblInfoEntry = _VRtrLdpAddrFecOutLblInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 35, 1)
)
vRtrLdpAddrFecOutLblInfoEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddrFecFecType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddrFecIpPrefix"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddrFecIpMask"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblId"),
)
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblInfoEntry.setStatus("obsolete")
_VRtrLdpAddrFecOutLblId_Type = Unsigned32
_VRtrLdpAddrFecOutLblId_Object = MibTableColumn
vRtrLdpAddrFecOutLblId = _VRtrLdpAddrFecOutLblId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 35, 1, 1),
    _VRtrLdpAddrFecOutLblId_Type()
)
vRtrLdpAddrFecOutLblId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblId.setStatus("obsolete")
_VRtrLdpAddrFecOutLblMetric_Type = Unsigned32
_VRtrLdpAddrFecOutLblMetric_Object = MibTableColumn
vRtrLdpAddrFecOutLblMetric = _VRtrLdpAddrFecOutLblMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 35, 1, 2),
    _VRtrLdpAddrFecOutLblMetric_Type()
)
vRtrLdpAddrFecOutLblMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblMetric.setStatus("obsolete")
_VRtrLdpAddrFecOutLblMtu_Type = Unsigned32
_VRtrLdpAddrFecOutLblMtu_Object = MibTableColumn
vRtrLdpAddrFecOutLblMtu = _VRtrLdpAddrFecOutLblMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 35, 1, 3),
    _VRtrLdpAddrFecOutLblMtu_Type()
)
vRtrLdpAddrFecOutLblMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLblMtu.setStatus("obsolete")
_VRtrLdpNgP2MPFecTable_Object = MibTable
vRtrLdpNgP2MPFecTable = _VRtrLdpNgP2MPFecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 36)
)
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecTable.setStatus("obsolete")
_VRtrLdpNgP2MPFecEntry_Object = MibTableRow
vRtrLdpNgP2MPFecEntry = _VRtrLdpNgP2MPFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 36, 1)
)
vRtrLdpNgP2MPFecEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecRootAddrType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecRootAddress"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOpaqueType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOpaqueLength"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOpaqueValue"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecEntry.setStatus("obsolete")


class _VRtrLdpNgP2MPFecOpaqueType_Type(Unsigned32):
    """Custom type vRtrLdpNgP2MPFecOpaqueType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrLdpNgP2MPFecOpaqueType_Type.__name__ = "Unsigned32"
_VRtrLdpNgP2MPFecOpaqueType_Object = MibTableColumn
vRtrLdpNgP2MPFecOpaqueType = _VRtrLdpNgP2MPFecOpaqueType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 36, 1, 1),
    _VRtrLdpNgP2MPFecOpaqueType_Type()
)
vRtrLdpNgP2MPFecOpaqueType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecOpaqueType.setStatus("obsolete")


class _VRtrLdpNgP2MPFecOpaqueLength_Type(Unsigned32):
    """Custom type vRtrLdpNgP2MPFecOpaqueLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrLdpNgP2MPFecOpaqueLength_Type.__name__ = "Unsigned32"
_VRtrLdpNgP2MPFecOpaqueLength_Object = MibTableColumn
vRtrLdpNgP2MPFecOpaqueLength = _VRtrLdpNgP2MPFecOpaqueLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 36, 1, 2),
    _VRtrLdpNgP2MPFecOpaqueLength_Type()
)
vRtrLdpNgP2MPFecOpaqueLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecOpaqueLength.setStatus("obsolete")


class _VRtrLdpNgP2MPFecOpaqueValue_Type(OctetString):
    """Custom type vRtrLdpNgP2MPFecOpaqueValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VRtrLdpNgP2MPFecOpaqueValue_Type.__name__ = "OctetString"
_VRtrLdpNgP2MPFecOpaqueValue_Object = MibTableColumn
vRtrLdpNgP2MPFecOpaqueValue = _VRtrLdpNgP2MPFecOpaqueValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 36, 1, 3),
    _VRtrLdpNgP2MPFecOpaqueValue_Type()
)
vRtrLdpNgP2MPFecOpaqueValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecOpaqueValue.setStatus("obsolete")
_VRtrLdpNgP2MPFecRootAddrType_Type = InetAddressType
_VRtrLdpNgP2MPFecRootAddrType_Object = MibTableColumn
vRtrLdpNgP2MPFecRootAddrType = _VRtrLdpNgP2MPFecRootAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 36, 1, 4),
    _VRtrLdpNgP2MPFecRootAddrType_Type()
)
vRtrLdpNgP2MPFecRootAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecRootAddrType.setStatus("obsolete")


class _VRtrLdpNgP2MPFecRootAddress_Type(InetAddress):
    """Custom type vRtrLdpNgP2MPFecRootAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpNgP2MPFecRootAddress_Type.__name__ = "InetAddress"
_VRtrLdpNgP2MPFecRootAddress_Object = MibTableColumn
vRtrLdpNgP2MPFecRootAddress = _VRtrLdpNgP2MPFecRootAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 36, 1, 5),
    _VRtrLdpNgP2MPFecRootAddress_Type()
)
vRtrLdpNgP2MPFecRootAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecRootAddress.setStatus("obsolete")
_VRtrLdpNgP2MPFecFlags_Type = TmnxLdpFECFlags
_VRtrLdpNgP2MPFecFlags_Object = MibTableColumn
vRtrLdpNgP2MPFecFlags = _VRtrLdpNgP2MPFecFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 36, 1, 6),
    _VRtrLdpNgP2MPFecFlags_Type()
)
vRtrLdpNgP2MPFecFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecFlags.setStatus("obsolete")
_VRtrLdpNgP2MPFecNumInLabels_Type = Gauge32
_VRtrLdpNgP2MPFecNumInLabels_Object = MibTableColumn
vRtrLdpNgP2MPFecNumInLabels = _VRtrLdpNgP2MPFecNumInLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 36, 1, 7),
    _VRtrLdpNgP2MPFecNumInLabels_Type()
)
vRtrLdpNgP2MPFecNumInLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecNumInLabels.setStatus("obsolete")
_VRtrLdpNgP2MPFecNumOutLabels_Type = Gauge32
_VRtrLdpNgP2MPFecNumOutLabels_Object = MibTableColumn
vRtrLdpNgP2MPFecNumOutLabels = _VRtrLdpNgP2MPFecNumOutLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 36, 1, 8),
    _VRtrLdpNgP2MPFecNumOutLabels_Type()
)
vRtrLdpNgP2MPFecNumOutLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecNumOutLabels.setStatus("obsolete")
_VRtrLdpNgP2MPFecTunnelIfId_Type = Unsigned32
_VRtrLdpNgP2MPFecTunnelIfId_Object = MibTableColumn
vRtrLdpNgP2MPFecTunnelIfId = _VRtrLdpNgP2MPFecTunnelIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 36, 1, 9),
    _VRtrLdpNgP2MPFecTunnelIfId_Type()
)
vRtrLdpNgP2MPFecTunnelIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecTunnelIfId.setStatus("obsolete")
_VRtrLdpNgP2MPFecMetric_Type = Unsigned32
_VRtrLdpNgP2MPFecMetric_Object = MibTableColumn
vRtrLdpNgP2MPFecMetric = _VRtrLdpNgP2MPFecMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 36, 1, 10),
    _VRtrLdpNgP2MPFecMetric_Type()
)
vRtrLdpNgP2MPFecMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecMetric.setStatus("obsolete")
_VRtrLdpNgP2MPFecMTU_Type = Unsigned32
_VRtrLdpNgP2MPFecMTU_Object = MibTableColumn
vRtrLdpNgP2MPFecMTU = _VRtrLdpNgP2MPFecMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 36, 1, 11),
    _VRtrLdpNgP2MPFecMTU_Type()
)
vRtrLdpNgP2MPFecMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecMTU.setStatus("obsolete")
_VRtrLdpNgP2MPFecInLabelTable_Object = MibTable
vRtrLdpNgP2MPFecInLabelTable = _VRtrLdpNgP2MPFecInLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 37)
)
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecInLabelTable.setStatus("obsolete")
_VRtrLdpNgP2MPFecInLabelEntry_Object = MibTableRow
vRtrLdpNgP2MPFecInLabelEntry = _VRtrLdpNgP2MPFecInLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 37, 1)
)
vRtrLdpNgP2MPFecInLabelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecRootAddrType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecRootAddress"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOpaqueType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOpaqueLength"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOpaqueValue"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecInLblId"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecInLabelEntry.setStatus("obsolete")
_VRtrLdpNgP2MPFecInLblId_Type = Unsigned32
_VRtrLdpNgP2MPFecInLblId_Object = MibTableColumn
vRtrLdpNgP2MPFecInLblId = _VRtrLdpNgP2MPFecInLblId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 37, 1, 1),
    _VRtrLdpNgP2MPFecInLblId_Type()
)
vRtrLdpNgP2MPFecInLblId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecInLblId.setStatus("obsolete")
_VRtrLdpNgP2MPFecInLbl_Type = Unsigned32
_VRtrLdpNgP2MPFecInLbl_Object = MibTableColumn
vRtrLdpNgP2MPFecInLbl = _VRtrLdpNgP2MPFecInLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 37, 1, 2),
    _VRtrLdpNgP2MPFecInLbl_Type()
)
vRtrLdpNgP2MPFecInLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecInLbl.setStatus("obsolete")
_VRtrLdpNgP2MPFecInLblStatus_Type = TmnxLabelStatus
_VRtrLdpNgP2MPFecInLblStatus_Object = MibTableColumn
vRtrLdpNgP2MPFecInLblStatus = _VRtrLdpNgP2MPFecInLblStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 37, 1, 3),
    _VRtrLdpNgP2MPFecInLblStatus_Type()
)
vRtrLdpNgP2MPFecInLblStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecInLblStatus.setStatus("obsolete")
_VRtrLdpNgP2MPFecInLblIfIndex_Type = InterfaceIndexOrZero
_VRtrLdpNgP2MPFecInLblIfIndex_Object = MibTableColumn
vRtrLdpNgP2MPFecInLblIfIndex = _VRtrLdpNgP2MPFecInLblIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 37, 1, 4),
    _VRtrLdpNgP2MPFecInLblIfIndex_Type()
)
vRtrLdpNgP2MPFecInLblIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecInLblIfIndex.setStatus("obsolete")
_VRtrLdpNgP2MPFecOutLabelTable_Object = MibTable
vRtrLdpNgP2MPFecOutLabelTable = _VRtrLdpNgP2MPFecOutLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 38)
)
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecOutLabelTable.setStatus("obsolete")
_VRtrLdpNgP2MPFecOutLabelEntry_Object = MibTableRow
vRtrLdpNgP2MPFecOutLabelEntry = _VRtrLdpNgP2MPFecOutLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 38, 1)
)
vRtrLdpNgP2MPFecOutLabelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecRootAddrType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecRootAddress"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOpaqueType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOpaqueLength"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOpaqueValue"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOutLblId"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecOutLabelEntry.setStatus("obsolete")
_VRtrLdpNgP2MPFecOutLblId_Type = Unsigned32
_VRtrLdpNgP2MPFecOutLblId_Object = MibTableColumn
vRtrLdpNgP2MPFecOutLblId = _VRtrLdpNgP2MPFecOutLblId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 38, 1, 1),
    _VRtrLdpNgP2MPFecOutLblId_Type()
)
vRtrLdpNgP2MPFecOutLblId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecOutLblId.setStatus("obsolete")
_VRtrLdpNgP2MPFecOutLbl_Type = Unsigned32
_VRtrLdpNgP2MPFecOutLbl_Object = MibTableColumn
vRtrLdpNgP2MPFecOutLbl = _VRtrLdpNgP2MPFecOutLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 38, 1, 2),
    _VRtrLdpNgP2MPFecOutLbl_Type()
)
vRtrLdpNgP2MPFecOutLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecOutLbl.setStatus("obsolete")
_VRtrLdpNgP2MPFecOutLblStatus_Type = TmnxLabelStatus
_VRtrLdpNgP2MPFecOutLblStatus_Object = MibTableColumn
vRtrLdpNgP2MPFecOutLblStatus = _VRtrLdpNgP2MPFecOutLblStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 38, 1, 3),
    _VRtrLdpNgP2MPFecOutLblStatus_Type()
)
vRtrLdpNgP2MPFecOutLblStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecOutLblStatus.setStatus("obsolete")
_VRtrLdpNgP2MPFecOutLblNxtHopType_Type = InetAddressType
_VRtrLdpNgP2MPFecOutLblNxtHopType_Object = MibTableColumn
vRtrLdpNgP2MPFecOutLblNxtHopType = _VRtrLdpNgP2MPFecOutLblNxtHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 38, 1, 4),
    _VRtrLdpNgP2MPFecOutLblNxtHopType_Type()
)
vRtrLdpNgP2MPFecOutLblNxtHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecOutLblNxtHopType.setStatus("obsolete")


class _VRtrLdpNgP2MPFecOutLblNxtHopAddr_Type(InetAddress):
    """Custom type vRtrLdpNgP2MPFecOutLblNxtHopAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpNgP2MPFecOutLblNxtHopAddr_Type.__name__ = "InetAddress"
_VRtrLdpNgP2MPFecOutLblNxtHopAddr_Object = MibTableColumn
vRtrLdpNgP2MPFecOutLblNxtHopAddr = _VRtrLdpNgP2MPFecOutLblNxtHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 38, 1, 5),
    _VRtrLdpNgP2MPFecOutLblNxtHopAddr_Type()
)
vRtrLdpNgP2MPFecOutLblNxtHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecOutLblNxtHopAddr.setStatus("obsolete")
_VRtrLdpNgP2MPFecOutLblIfIndex_Type = InterfaceIndexOrZero
_VRtrLdpNgP2MPFecOutLblIfIndex_Object = MibTableColumn
vRtrLdpNgP2MPFecOutLblIfIndex = _VRtrLdpNgP2MPFecOutLblIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 38, 1, 6),
    _VRtrLdpNgP2MPFecOutLblIfIndex_Type()
)
vRtrLdpNgP2MPFecOutLblIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecOutLblIfIndex.setStatus("obsolete")
_VRtrLdpNgP2MPFecOutLblLspId_Type = TmnxVRtrMplsLspID
_VRtrLdpNgP2MPFecOutLblLspId_Object = MibTableColumn
vRtrLdpNgP2MPFecOutLblLspId = _VRtrLdpNgP2MPFecOutLblLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 38, 1, 7),
    _VRtrLdpNgP2MPFecOutLblLspId_Type()
)
vRtrLdpNgP2MPFecOutLblLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecOutLblLspId.setStatus("obsolete")
_VRtrLdpNgP2MPFecMapTable_Object = MibTable
vRtrLdpNgP2MPFecMapTable = _VRtrLdpNgP2MPFecMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 39)
)
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecMapTable.setStatus("obsolete")
_VRtrLdpNgP2MPFecMapEntry_Object = MibTableRow
vRtrLdpNgP2MPFecMapEntry = _VRtrLdpNgP2MPFecMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 39, 1)
)
vRtrLdpNgP2MPFecMapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecRootAddrType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecRootAddress"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOpaqueType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOpaqueLength"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOpaqueValue"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecMapEntry.setStatus("obsolete")
_VRtrLdpNgP2MPFecMapFlags_Type = TmnxLdpFECFlags
_VRtrLdpNgP2MPFecMapFlags_Object = MibTableColumn
vRtrLdpNgP2MPFecMapFlags = _VRtrLdpNgP2MPFecMapFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 39, 1, 1),
    _VRtrLdpNgP2MPFecMapFlags_Type()
)
vRtrLdpNgP2MPFecMapFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecMapFlags.setStatus("obsolete")
_VRtrLdpNgP2MPFecMapNumInLabels_Type = Gauge32
_VRtrLdpNgP2MPFecMapNumInLabels_Object = MibTableColumn
vRtrLdpNgP2MPFecMapNumInLabels = _VRtrLdpNgP2MPFecMapNumInLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 39, 1, 2),
    _VRtrLdpNgP2MPFecMapNumInLabels_Type()
)
vRtrLdpNgP2MPFecMapNumInLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecMapNumInLabels.setStatus("obsolete")
_VRtrLdpNgP2MPFecMapNumOutLabels_Type = Gauge32
_VRtrLdpNgP2MPFecMapNumOutLabels_Object = MibTableColumn
vRtrLdpNgP2MPFecMapNumOutLabels = _VRtrLdpNgP2MPFecMapNumOutLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 39, 1, 3),
    _VRtrLdpNgP2MPFecMapNumOutLabels_Type()
)
vRtrLdpNgP2MPFecMapNumOutLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecMapNumOutLabels.setStatus("obsolete")
_VRtrLdpNgP2MPFecMapTunnelIfId_Type = Unsigned32
_VRtrLdpNgP2MPFecMapTunnelIfId_Object = MibTableColumn
vRtrLdpNgP2MPFecMapTunnelIfId = _VRtrLdpNgP2MPFecMapTunnelIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 39, 1, 4),
    _VRtrLdpNgP2MPFecMapTunnelIfId_Type()
)
vRtrLdpNgP2MPFecMapTunnelIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecMapTunnelIfId.setStatus("obsolete")
_VRtrLdpNgP2MPFecMapMetric_Type = Unsigned32
_VRtrLdpNgP2MPFecMapMetric_Object = MibTableColumn
vRtrLdpNgP2MPFecMapMetric = _VRtrLdpNgP2MPFecMapMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 39, 1, 5),
    _VRtrLdpNgP2MPFecMapMetric_Type()
)
vRtrLdpNgP2MPFecMapMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecMapMetric.setStatus("obsolete")
_VRtrLdpNgP2MPFecMapMTU_Type = Unsigned32
_VRtrLdpNgP2MPFecMapMTU_Object = MibTableColumn
vRtrLdpNgP2MPFecMapMTU = _VRtrLdpNgP2MPFecMapMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 39, 1, 6),
    _VRtrLdpNgP2MPFecMapMTU_Type()
)
vRtrLdpNgP2MPFecMapMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgP2MPFecMapMTU.setStatus("obsolete")
_VRtrLdpAddressFecTable_Object = MibTable
vRtrLdpAddressFecTable = _VRtrLdpAddressFecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 40)
)
if mibBuilder.loadTexts:
    vRtrLdpAddressFecTable.setStatus("obsolete")
_VRtrLdpAddressFecEntry_Object = MibTableRow
vRtrLdpAddressFecEntry = _VRtrLdpAddressFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 40, 1)
)
vRtrLdpAddressFecEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecFecType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefixType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefix"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefixLen"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    vRtrLdpAddressFecEntry.setStatus("obsolete")
_VRtrLdpAddressFecFecType_Type = TmnxLdpFECType
_VRtrLdpAddressFecFecType_Object = MibTableColumn
vRtrLdpAddressFecFecType = _VRtrLdpAddressFecFecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 40, 1, 1),
    _VRtrLdpAddressFecFecType_Type()
)
vRtrLdpAddressFecFecType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecFecType.setStatus("obsolete")
_VRtrLdpAddressFecIpPrefixType_Type = InetAddressType
_VRtrLdpAddressFecIpPrefixType_Object = MibTableColumn
vRtrLdpAddressFecIpPrefixType = _VRtrLdpAddressFecIpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 40, 1, 2),
    _VRtrLdpAddressFecIpPrefixType_Type()
)
vRtrLdpAddressFecIpPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecIpPrefixType.setStatus("obsolete")


class _VRtrLdpAddressFecIpPrefix_Type(InetAddress):
    """Custom type vRtrLdpAddressFecIpPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpAddressFecIpPrefix_Type.__name__ = "InetAddress"
_VRtrLdpAddressFecIpPrefix_Object = MibTableColumn
vRtrLdpAddressFecIpPrefix = _VRtrLdpAddressFecIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 40, 1, 3),
    _VRtrLdpAddressFecIpPrefix_Type()
)
vRtrLdpAddressFecIpPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecIpPrefix.setStatus("obsolete")


class _VRtrLdpAddressFecIpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type vRtrLdpAddressFecIpPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_VRtrLdpAddressFecIpPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_VRtrLdpAddressFecIpPrefixLen_Object = MibTableColumn
vRtrLdpAddressFecIpPrefixLen = _VRtrLdpAddressFecIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 40, 1, 4),
    _VRtrLdpAddressFecIpPrefixLen_Type()
)
vRtrLdpAddressFecIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecIpPrefixLen.setStatus("obsolete")
_VRtrLdpAddressFecFlags_Type = TmnxLdpFECFlags
_VRtrLdpAddressFecFlags_Object = MibTableColumn
vRtrLdpAddressFecFlags = _VRtrLdpAddressFecFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 40, 1, 5),
    _VRtrLdpAddressFecFlags_Type()
)
vRtrLdpAddressFecFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecFlags.setStatus("obsolete")
_VRtrLdpAddressFecNumInLabels_Type = Unsigned32
_VRtrLdpAddressFecNumInLabels_Object = MibTableColumn
vRtrLdpAddressFecNumInLabels = _VRtrLdpAddressFecNumInLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 40, 1, 6),
    _VRtrLdpAddressFecNumInLabels_Type()
)
vRtrLdpAddressFecNumInLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecNumInLabels.setStatus("obsolete")
_VRtrLdpAddressFecNumOutLabels_Type = Unsigned32
_VRtrLdpAddressFecNumOutLabels_Object = MibTableColumn
vRtrLdpAddressFecNumOutLabels = _VRtrLdpAddressFecNumOutLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 40, 1, 7),
    _VRtrLdpAddressFecNumOutLabels_Type()
)
vRtrLdpAddressFecNumOutLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecNumOutLabels.setStatus("obsolete")
_VRtrLdpAddressFecInLabelTable_Object = MibTable
vRtrLdpAddressFecInLabelTable = _VRtrLdpAddressFecInLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 41)
)
if mibBuilder.loadTexts:
    vRtrLdpAddressFecInLabelTable.setStatus("obsolete")
_VRtrLdpAddressFecInLabelEntry_Object = MibTableRow
vRtrLdpAddressFecInLabelEntry = _VRtrLdpAddressFecInLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 41, 1)
)
vRtrLdpAddressFecInLabelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecFecType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefixType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefix"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefixLen"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecInLblId"),
)
if mibBuilder.loadTexts:
    vRtrLdpAddressFecInLabelEntry.setStatus("obsolete")
_VRtrLdpAddressFecInLblId_Type = Unsigned32
_VRtrLdpAddressFecInLblId_Object = MibTableColumn
vRtrLdpAddressFecInLblId = _VRtrLdpAddressFecInLblId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 41, 1, 1),
    _VRtrLdpAddressFecInLblId_Type()
)
vRtrLdpAddressFecInLblId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecInLblId.setStatus("obsolete")
_VRtrLdpAddressFecInLbl_Type = Unsigned32
_VRtrLdpAddressFecInLbl_Object = MibTableColumn
vRtrLdpAddressFecInLbl = _VRtrLdpAddressFecInLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 41, 1, 2),
    _VRtrLdpAddressFecInLbl_Type()
)
vRtrLdpAddressFecInLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecInLbl.setStatus("obsolete")
_VRtrLdpAddressFecInLblStatus_Type = TmnxLabelStatus
_VRtrLdpAddressFecInLblStatus_Object = MibTableColumn
vRtrLdpAddressFecInLblStatus = _VRtrLdpAddressFecInLblStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 41, 1, 3),
    _VRtrLdpAddressFecInLblStatus_Type()
)
vRtrLdpAddressFecInLblStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecInLblStatus.setStatus("obsolete")
_VRtrLdpAddressFecInLblIfIndex_Type = InterfaceIndexOrZero
_VRtrLdpAddressFecInLblIfIndex_Object = MibTableColumn
vRtrLdpAddressFecInLblIfIndex = _VRtrLdpAddressFecInLblIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 41, 1, 4),
    _VRtrLdpAddressFecInLblIfIndex_Type()
)
vRtrLdpAddressFecInLblIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecInLblIfIndex.setStatus("obsolete")
_VRtrLdpAddressFecOutLabelTable_Object = MibTable
vRtrLdpAddressFecOutLabelTable = _VRtrLdpAddressFecOutLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 42)
)
if mibBuilder.loadTexts:
    vRtrLdpAddressFecOutLabelTable.setStatus("obsolete")
_VRtrLdpAddressFecOutLabelEntry_Object = MibTableRow
vRtrLdpAddressFecOutLabelEntry = _VRtrLdpAddressFecOutLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 42, 1)
)
vRtrLdpAddressFecOutLabelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecFecType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefixType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefix"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefixLen"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecOutLblId"),
)
if mibBuilder.loadTexts:
    vRtrLdpAddressFecOutLabelEntry.setStatus("obsolete")
_VRtrLdpAddressFecOutLblId_Type = Unsigned32
_VRtrLdpAddressFecOutLblId_Object = MibTableColumn
vRtrLdpAddressFecOutLblId = _VRtrLdpAddressFecOutLblId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 42, 1, 1),
    _VRtrLdpAddressFecOutLblId_Type()
)
vRtrLdpAddressFecOutLblId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecOutLblId.setStatus("obsolete")
_VRtrLdpAddressFecOutLbl_Type = Unsigned32
_VRtrLdpAddressFecOutLbl_Object = MibTableColumn
vRtrLdpAddressFecOutLbl = _VRtrLdpAddressFecOutLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 42, 1, 2),
    _VRtrLdpAddressFecOutLbl_Type()
)
vRtrLdpAddressFecOutLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecOutLbl.setStatus("obsolete")
_VRtrLdpAddressFecOutLblStatus_Type = TmnxLabelStatus
_VRtrLdpAddressFecOutLblStatus_Object = MibTableColumn
vRtrLdpAddressFecOutLblStatus = _VRtrLdpAddressFecOutLblStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 42, 1, 3),
    _VRtrLdpAddressFecOutLblStatus_Type()
)
vRtrLdpAddressFecOutLblStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecOutLblStatus.setStatus("obsolete")
_VRtrLdpAddressFecOutLblIfIndex_Type = InterfaceIndexOrZero
_VRtrLdpAddressFecOutLblIfIndex_Object = MibTableColumn
vRtrLdpAddressFecOutLblIfIndex = _VRtrLdpAddressFecOutLblIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 42, 1, 4),
    _VRtrLdpAddressFecOutLblIfIndex_Type()
)
vRtrLdpAddressFecOutLblIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecOutLblIfIndex.setStatus("obsolete")
_VRtrLdpAddressFecOutLblNHType_Type = InetAddressType
_VRtrLdpAddressFecOutLblNHType_Object = MibTableColumn
vRtrLdpAddressFecOutLblNHType = _VRtrLdpAddressFecOutLblNHType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 42, 1, 5),
    _VRtrLdpAddressFecOutLblNHType_Type()
)
vRtrLdpAddressFecOutLblNHType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecOutLblNHType.setStatus("obsolete")


class _VRtrLdpAddressFecOutLblNHAddr_Type(InetAddress):
    """Custom type vRtrLdpAddressFecOutLblNHAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpAddressFecOutLblNHAddr_Type.__name__ = "InetAddress"
_VRtrLdpAddressFecOutLblNHAddr_Object = MibTableColumn
vRtrLdpAddressFecOutLblNHAddr = _VRtrLdpAddressFecOutLblNHAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 42, 1, 6),
    _VRtrLdpAddressFecOutLblNHAddr_Type()
)
vRtrLdpAddressFecOutLblNHAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecOutLblNHAddr.setStatus("obsolete")
_VRtrLdpAddressFecOutLblMetric_Type = Unsigned32
_VRtrLdpAddressFecOutLblMetric_Object = MibTableColumn
vRtrLdpAddressFecOutLblMetric = _VRtrLdpAddressFecOutLblMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 42, 1, 7),
    _VRtrLdpAddressFecOutLblMetric_Type()
)
vRtrLdpAddressFecOutLblMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecOutLblMetric.setStatus("obsolete")
_VRtrLdpAddressFecOutLblMtu_Type = Unsigned32
_VRtrLdpAddressFecOutLblMtu_Object = MibTableColumn
vRtrLdpAddressFecOutLblMtu = _VRtrLdpAddressFecOutLblMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 42, 1, 8),
    _VRtrLdpAddressFecOutLblMtu_Type()
)
vRtrLdpAddressFecOutLblMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecOutLblMtu.setStatus("obsolete")
_VRtrLdpAddressFecOutLblLspId_Type = TmnxVRtrMplsLspID
_VRtrLdpAddressFecOutLblLspId_Object = MibTableColumn
vRtrLdpAddressFecOutLblLspId = _VRtrLdpAddressFecOutLblLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 42, 1, 9),
    _VRtrLdpAddressFecOutLblLspId_Type()
)
vRtrLdpAddressFecOutLblLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecOutLblLspId.setStatus("obsolete")
_VRtrLdpAddressFecMapTable_Object = MibTable
vRtrLdpAddressFecMapTable = _VRtrLdpAddressFecMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 43)
)
if mibBuilder.loadTexts:
    vRtrLdpAddressFecMapTable.setStatus("obsolete")
_VRtrLdpAddressFecMapEntry_Object = MibTableRow
vRtrLdpAddressFecMapEntry = _VRtrLdpAddressFecMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 43, 1)
)
vRtrLdpAddressFecMapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecFecType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefixType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefix"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefixLen"),
)
if mibBuilder.loadTexts:
    vRtrLdpAddressFecMapEntry.setStatus("obsolete")
_VRtrLdpAddressFecMapFlags_Type = TmnxLdpFECFlags
_VRtrLdpAddressFecMapFlags_Object = MibTableColumn
vRtrLdpAddressFecMapFlags = _VRtrLdpAddressFecMapFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 43, 1, 1),
    _VRtrLdpAddressFecMapFlags_Type()
)
vRtrLdpAddressFecMapFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecMapFlags.setStatus("obsolete")
_VRtrLdpAddressFecMapNumInLabels_Type = Unsigned32
_VRtrLdpAddressFecMapNumInLabels_Object = MibTableColumn
vRtrLdpAddressFecMapNumInLabels = _VRtrLdpAddressFecMapNumInLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 43, 1, 2),
    _VRtrLdpAddressFecMapNumInLabels_Type()
)
vRtrLdpAddressFecMapNumInLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecMapNumInLabels.setStatus("obsolete")
_VRtrLdpAddressFecMapNumOutLabels_Type = Unsigned32
_VRtrLdpAddressFecMapNumOutLabels_Object = MibTableColumn
vRtrLdpAddressFecMapNumOutLabels = _VRtrLdpAddressFecMapNumOutLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 43, 1, 3),
    _VRtrLdpAddressFecMapNumOutLabels_Type()
)
vRtrLdpAddressFecMapNumOutLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddressFecMapNumOutLabels.setStatus("obsolete")
_VRtrLdpAddrActiveFecTable_Object = MibTable
vRtrLdpAddrActiveFecTable = _VRtrLdpAddrActiveFecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 44)
)
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecTable.setStatus("obsolete")
_VRtrLdpAddrActiveFecEntry_Object = MibTableRow
vRtrLdpAddrActiveFecEntry = _VRtrLdpAddrActiveFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 44, 1)
)
vRtrLdpAddrActiveFecEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecFecType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefixType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefix"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefixLen"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOpType"),
)
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecEntry.setStatus("obsolete")


class _VRtrLdpAddrActiveFecOpType_Type(Integer32):
    """Custom type vRtrLdpAddrActiveFecOpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pop", 1),
          ("push", 2),
          ("swap", 3))
    )


_VRtrLdpAddrActiveFecOpType_Type.__name__ = "Integer32"
_VRtrLdpAddrActiveFecOpType_Object = MibTableColumn
vRtrLdpAddrActiveFecOpType = _VRtrLdpAddrActiveFecOpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 44, 1, 1),
    _VRtrLdpAddrActiveFecOpType_Type()
)
vRtrLdpAddrActiveFecOpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecOpType.setStatus("obsolete")
_VRtrLdpAddrActiveFecFecFlags_Type = TmnxLdpFECFlags
_VRtrLdpAddrActiveFecFecFlags_Object = MibTableColumn
vRtrLdpAddrActiveFecFecFlags = _VRtrLdpAddrActiveFecFecFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 44, 1, 2),
    _VRtrLdpAddrActiveFecFecFlags_Type()
)
vRtrLdpAddrActiveFecFecFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecFecFlags.setStatus("obsolete")
_VRtrLdpAddrActiveFecNumInLbls_Type = Unsigned32
_VRtrLdpAddrActiveFecNumInLbls_Object = MibTableColumn
vRtrLdpAddrActiveFecNumInLbls = _VRtrLdpAddrActiveFecNumInLbls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 44, 1, 3),
    _VRtrLdpAddrActiveFecNumInLbls_Type()
)
vRtrLdpAddrActiveFecNumInLbls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecNumInLbls.setStatus("obsolete")
_VRtrLdpAddrActiveFecNumOutLbls_Type = Unsigned32
_VRtrLdpAddrActiveFecNumOutLbls_Object = MibTableColumn
vRtrLdpAddrActiveFecNumOutLbls = _VRtrLdpAddrActiveFecNumOutLbls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 44, 1, 4),
    _VRtrLdpAddrActiveFecNumOutLbls_Type()
)
vRtrLdpAddrActiveFecNumOutLbls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecNumOutLbls.setStatus("obsolete")
_VRtrLdpAddrActiveFecInLblTable_Object = MibTable
vRtrLdpAddrActiveFecInLblTable = _VRtrLdpAddrActiveFecInLblTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 45)
)
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecInLblTable.setStatus("obsolete")
_VRtrLdpAddrActiveFecInLblEntry_Object = MibTableRow
vRtrLdpAddrActiveFecInLblEntry = _VRtrLdpAddrActiveFecInLblEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 45, 1)
)
vRtrLdpAddrActiveFecInLblEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecFecType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefixType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefix"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefixLen"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOpType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecInLblId"),
)
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecInLblEntry.setStatus("obsolete")
_VRtrLdpAddrActiveFecInLblId_Type = Unsigned32
_VRtrLdpAddrActiveFecInLblId_Object = MibTableColumn
vRtrLdpAddrActiveFecInLblId = _VRtrLdpAddrActiveFecInLblId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 45, 1, 1),
    _VRtrLdpAddrActiveFecInLblId_Type()
)
vRtrLdpAddrActiveFecInLblId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecInLblId.setStatus("obsolete")
_VRtrLdpAddrActiveFecInLbl_Type = Unsigned32
_VRtrLdpAddrActiveFecInLbl_Object = MibTableColumn
vRtrLdpAddrActiveFecInLbl = _VRtrLdpAddrActiveFecInLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 45, 1, 2),
    _VRtrLdpAddrActiveFecInLbl_Type()
)
vRtrLdpAddrActiveFecInLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecInLbl.setStatus("obsolete")
_VRtrLdpAddrActiveFecInLblIfIndex_Type = InterfaceIndexOrZero
_VRtrLdpAddrActiveFecInLblIfIndex_Object = MibTableColumn
vRtrLdpAddrActiveFecInLblIfIndex = _VRtrLdpAddrActiveFecInLblIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 45, 1, 3),
    _VRtrLdpAddrActiveFecInLblIfIndex_Type()
)
vRtrLdpAddrActiveFecInLblIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecInLblIfIndex.setStatus("obsolete")
_VRtrLdpAddrActiveFecOutLblTable_Object = MibTable
vRtrLdpAddrActiveFecOutLblTable = _VRtrLdpAddrActiveFecOutLblTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 46)
)
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecOutLblTable.setStatus("obsolete")
_VRtrLdpAddrActiveFecOutLblEntry_Object = MibTableRow
vRtrLdpAddrActiveFecOutLblEntry = _VRtrLdpAddrActiveFecOutLblEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 46, 1)
)
vRtrLdpAddrActiveFecOutLblEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecFecType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefixType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefix"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddressFecIpPrefixLen"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOpType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOutLblId"),
)
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecOutLblEntry.setStatus("obsolete")
_VRtrLdpAddrActiveFecOutLblId_Type = Unsigned32
_VRtrLdpAddrActiveFecOutLblId_Object = MibTableColumn
vRtrLdpAddrActiveFecOutLblId = _VRtrLdpAddrActiveFecOutLblId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 46, 1, 1),
    _VRtrLdpAddrActiveFecOutLblId_Type()
)
vRtrLdpAddrActiveFecOutLblId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecOutLblId.setStatus("obsolete")
_VRtrLdpAddrActiveFecOutLbl_Type = Unsigned32
_VRtrLdpAddrActiveFecOutLbl_Object = MibTableColumn
vRtrLdpAddrActiveFecOutLbl = _VRtrLdpAddrActiveFecOutLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 46, 1, 2),
    _VRtrLdpAddrActiveFecOutLbl_Type()
)
vRtrLdpAddrActiveFecOutLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecOutLbl.setStatus("obsolete")
_VRtrLdpAddrActiveFecOutLblStatus_Type = TmnxLabelStatus
_VRtrLdpAddrActiveFecOutLblStatus_Object = MibTableColumn
vRtrLdpAddrActiveFecOutLblStatus = _VRtrLdpAddrActiveFecOutLblStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 46, 1, 3),
    _VRtrLdpAddrActiveFecOutLblStatus_Type()
)
vRtrLdpAddrActiveFecOutLblStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecOutLblStatus.setStatus("obsolete")
_VRtrLdpAddrActiveFecOutLblIfIdx_Type = InterfaceIndexOrZero
_VRtrLdpAddrActiveFecOutLblIfIdx_Object = MibTableColumn
vRtrLdpAddrActiveFecOutLblIfIdx = _VRtrLdpAddrActiveFecOutLblIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 46, 1, 4),
    _VRtrLdpAddrActiveFecOutLblIfIdx_Type()
)
vRtrLdpAddrActiveFecOutLblIfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecOutLblIfIdx.setStatus("obsolete")
_VRtrLdpAddrActiveFecOutLblNHType_Type = InetAddressType
_VRtrLdpAddrActiveFecOutLblNHType_Object = MibTableColumn
vRtrLdpAddrActiveFecOutLblNHType = _VRtrLdpAddrActiveFecOutLblNHType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 46, 1, 5),
    _VRtrLdpAddrActiveFecOutLblNHType_Type()
)
vRtrLdpAddrActiveFecOutLblNHType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecOutLblNHType.setStatus("obsolete")


class _VRtrLdpAddrActiveFecOutLblNHAddr_Type(InetAddress):
    """Custom type vRtrLdpAddrActiveFecOutLblNHAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpAddrActiveFecOutLblNHAddr_Type.__name__ = "InetAddress"
_VRtrLdpAddrActiveFecOutLblNHAddr_Object = MibTableColumn
vRtrLdpAddrActiveFecOutLblNHAddr = _VRtrLdpAddrActiveFecOutLblNHAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 46, 1, 6),
    _VRtrLdpAddrActiveFecOutLblNHAddr_Type()
)
vRtrLdpAddrActiveFecOutLblNHAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecOutLblNHAddr.setStatus("obsolete")
_VRtrLdpAddrActiveFecOutLblMetric_Type = Unsigned32
_VRtrLdpAddrActiveFecOutLblMetric_Object = MibTableColumn
vRtrLdpAddrActiveFecOutLblMetric = _VRtrLdpAddrActiveFecOutLblMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 46, 1, 7),
    _VRtrLdpAddrActiveFecOutLblMetric_Type()
)
vRtrLdpAddrActiveFecOutLblMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecOutLblMetric.setStatus("obsolete")
_VRtrLdpAddrActiveFecOutLblMtu_Type = Unsigned32
_VRtrLdpAddrActiveFecOutLblMtu_Object = MibTableColumn
vRtrLdpAddrActiveFecOutLblMtu = _VRtrLdpAddrActiveFecOutLblMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 46, 1, 8),
    _VRtrLdpAddrActiveFecOutLblMtu_Type()
)
vRtrLdpAddrActiveFecOutLblMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecOutLblMtu.setStatus("obsolete")
_VRtrLdpAddrActiveFecOutLblLspId_Type = TmnxVRtrMplsLspID
_VRtrLdpAddrActiveFecOutLblLspId_Object = MibTableColumn
vRtrLdpAddrActiveFecOutLblLspId = _VRtrLdpAddrActiveFecOutLblLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 46, 1, 9),
    _VRtrLdpAddrActiveFecOutLblLspId_Type()
)
vRtrLdpAddrActiveFecOutLblLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrActiveFecOutLblLspId.setStatus("obsolete")
_VRtrLdpSessionAddrTable_Object = MibTable
vRtrLdpSessionAddrTable = _VRtrLdpSessionAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 47)
)
if mibBuilder.loadTexts:
    vRtrLdpSessionAddrTable.setStatus("obsolete")
_VRtrLdpSessionAddrEntry_Object = MibTableRow
vRtrLdpSessionAddrEntry = _VRtrLdpSessionAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 47, 1)
)
vRtrLdpSessionAddrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    vRtrLdpSessionAddrEntry.setStatus("obsolete")
_VRtrLdpSessionAddrLocalLdpId_Type = MplsLdpIdentifier
_VRtrLdpSessionAddrLocalLdpId_Object = MibTableColumn
vRtrLdpSessionAddrLocalLdpId = _VRtrLdpSessionAddrLocalLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 47, 1, 1),
    _VRtrLdpSessionAddrLocalLdpId_Type()
)
vRtrLdpSessionAddrLocalLdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessionAddrLocalLdpId.setStatus("obsolete")
_VRtrLdpSessionAddrNumInAddrs_Type = Unsigned32
_VRtrLdpSessionAddrNumInAddrs_Object = MibTableColumn
vRtrLdpSessionAddrNumInAddrs = _VRtrLdpSessionAddrNumInAddrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 47, 1, 2),
    _VRtrLdpSessionAddrNumInAddrs_Type()
)
vRtrLdpSessionAddrNumInAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessionAddrNumInAddrs.setStatus("obsolete")
_VRtrLdpSessionAddrNumOutAddrs_Type = Unsigned32
_VRtrLdpSessionAddrNumOutAddrs_Object = MibTableColumn
vRtrLdpSessionAddrNumOutAddrs = _VRtrLdpSessionAddrNumOutAddrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 47, 1, 3),
    _VRtrLdpSessionAddrNumOutAddrs_Type()
)
vRtrLdpSessionAddrNumOutAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessionAddrNumOutAddrs.setStatus("obsolete")
_VRtrLdpSessionInAddrTable_Object = MibTable
vRtrLdpSessionInAddrTable = _VRtrLdpSessionInAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 48)
)
if mibBuilder.loadTexts:
    vRtrLdpSessionInAddrTable.setStatus("obsolete")
_VRtrLdpSessionInAddrEntry_Object = MibTableRow
vRtrLdpSessionInAddrEntry = _VRtrLdpSessionInAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 48, 1)
)
vRtrLdpSessionInAddrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpSessionInAddrAddrType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpSessionInAddrAddress"),
)
if mibBuilder.loadTexts:
    vRtrLdpSessionInAddrEntry.setStatus("obsolete")
_VRtrLdpSessionInAddrAddrType_Type = InetAddressType
_VRtrLdpSessionInAddrAddrType_Object = MibTableColumn
vRtrLdpSessionInAddrAddrType = _VRtrLdpSessionInAddrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 48, 1, 1),
    _VRtrLdpSessionInAddrAddrType_Type()
)
vRtrLdpSessionInAddrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpSessionInAddrAddrType.setStatus("obsolete")


class _VRtrLdpSessionInAddrAddress_Type(InetAddress):
    """Custom type vRtrLdpSessionInAddrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpSessionInAddrAddress_Type.__name__ = "InetAddress"
_VRtrLdpSessionInAddrAddress_Object = MibTableColumn
vRtrLdpSessionInAddrAddress = _VRtrLdpSessionInAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 48, 1, 2),
    _VRtrLdpSessionInAddrAddress_Type()
)
vRtrLdpSessionInAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpSessionInAddrAddress.setStatus("obsolete")
_VRtrLdpSessionInAddrLocalLdpId_Type = MplsLdpIdentifier
_VRtrLdpSessionInAddrLocalLdpId_Object = MibTableColumn
vRtrLdpSessionInAddrLocalLdpId = _VRtrLdpSessionInAddrLocalLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 48, 1, 3),
    _VRtrLdpSessionInAddrLocalLdpId_Type()
)
vRtrLdpSessionInAddrLocalLdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessionInAddrLocalLdpId.setStatus("obsolete")
_VRtrLdpSessionOutAddrTable_Object = MibTable
vRtrLdpSessionOutAddrTable = _VRtrLdpSessionOutAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 49)
)
if mibBuilder.loadTexts:
    vRtrLdpSessionOutAddrTable.setStatus("obsolete")
_VRtrLdpSessionOutAddrEntry_Object = MibTableRow
vRtrLdpSessionOutAddrEntry = _VRtrLdpSessionOutAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 49, 1)
)
vRtrLdpSessionOutAddrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpSessionOutAddrAddrType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpSessionOutAddrAddress"),
)
if mibBuilder.loadTexts:
    vRtrLdpSessionOutAddrEntry.setStatus("obsolete")
_VRtrLdpSessionOutAddrAddrType_Type = InetAddressType
_VRtrLdpSessionOutAddrAddrType_Object = MibTableColumn
vRtrLdpSessionOutAddrAddrType = _VRtrLdpSessionOutAddrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 49, 1, 1),
    _VRtrLdpSessionOutAddrAddrType_Type()
)
vRtrLdpSessionOutAddrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpSessionOutAddrAddrType.setStatus("obsolete")


class _VRtrLdpSessionOutAddrAddress_Type(InetAddress):
    """Custom type vRtrLdpSessionOutAddrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpSessionOutAddrAddress_Type.__name__ = "InetAddress"
_VRtrLdpSessionOutAddrAddress_Object = MibTableColumn
vRtrLdpSessionOutAddrAddress = _VRtrLdpSessionOutAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 49, 1, 2),
    _VRtrLdpSessionOutAddrAddress_Type()
)
vRtrLdpSessionOutAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpSessionOutAddrAddress.setStatus("obsolete")
_VRtrLdpSessionOutAddrLocalLdpId_Type = MplsLdpIdentifier
_VRtrLdpSessionOutAddrLocalLdpId_Object = MibTableColumn
vRtrLdpSessionOutAddrLocalLdpId = _VRtrLdpSessionOutAddrLocalLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 49, 1, 3),
    _VRtrLdpSessionOutAddrLocalLdpId_Type()
)
vRtrLdpSessionOutAddrLocalLdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessionOutAddrLocalLdpId.setStatus("obsolete")
_VRtrLdpPeerTemplTableLstChanged_Type = TimeStamp
_VRtrLdpPeerTemplTableLstChanged_Object = MibScalar
vRtrLdpPeerTemplTableLstChanged = _VRtrLdpPeerTemplTableLstChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 50),
    _VRtrLdpPeerTemplTableLstChanged_Type()
)
vRtrLdpPeerTemplTableLstChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplTableLstChanged.setStatus("current")
_VRtrLdpPeerTemplTable_Object = MibTable
vRtrLdpPeerTemplTable = _VRtrLdpPeerTemplTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51)
)
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplTable.setStatus("current")
_VRtrLdpPeerTemplEntry_Object = MibTableRow
vRtrLdpPeerTemplEntry = _VRtrLdpPeerTemplEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1)
)
vRtrLdpPeerTemplEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerTemplName"),
)
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplEntry.setStatus("current")
_VRtrLdpPeerTemplName_Type = TNamedItem
_VRtrLdpPeerTemplName_Object = MibTableColumn
vRtrLdpPeerTemplName = _VRtrLdpPeerTemplName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 1),
    _VRtrLdpPeerTemplName_Type()
)
vRtrLdpPeerTemplName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplName.setStatus("current")
_VRtrLdpPeerTemplLastChanged_Type = TimeStamp
_VRtrLdpPeerTemplLastChanged_Object = MibTableColumn
vRtrLdpPeerTemplLastChanged = _VRtrLdpPeerTemplLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 2),
    _VRtrLdpPeerTemplLastChanged_Type()
)
vRtrLdpPeerTemplLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplLastChanged.setStatus("current")
_VRtrLdpPeerTemplRowStatus_Type = RowStatus
_VRtrLdpPeerTemplRowStatus_Object = MibTableColumn
vRtrLdpPeerTemplRowStatus = _VRtrLdpPeerTemplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 3),
    _VRtrLdpPeerTemplRowStatus_Type()
)
vRtrLdpPeerTemplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplRowStatus.setStatus("current")


class _VRtrLdpPeerTemplAdminState_Type(TmnxAdminState):
    """Custom type vRtrLdpPeerTemplAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrLdpPeerTemplAdminState_Type.__name__ = "TmnxAdminState"
_VRtrLdpPeerTemplAdminState_Object = MibTableColumn
vRtrLdpPeerTemplAdminState = _VRtrLdpPeerTemplAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 4),
    _VRtrLdpPeerTemplAdminState_Type()
)
vRtrLdpPeerTemplAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplAdminState.setStatus("current")


class _VRtrLdpPeerTemplInheritance_Type(Unsigned32):
    """Custom type vRtrLdpPeerTemplInheritance based on Unsigned32"""
    defaultValue = 0


_VRtrLdpPeerTemplInheritance_Type.__name__ = "Unsigned32"
_VRtrLdpPeerTemplInheritance_Object = MibTableColumn
vRtrLdpPeerTemplInheritance = _VRtrLdpPeerTemplInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 5),
    _VRtrLdpPeerTemplInheritance_Type()
)
vRtrLdpPeerTemplInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplInheritance.setStatus("current")


class _VRtrLdpPeerTemplKeepAliveFactor_Type(TmnxLdpKeepAliveFactor):
    """Custom type vRtrLdpPeerTemplKeepAliveFactor based on TmnxLdpKeepAliveFactor"""
    defaultValue = 4


_VRtrLdpPeerTemplKeepAliveFactor_Type.__name__ = "TmnxLdpKeepAliveFactor"
_VRtrLdpPeerTemplKeepAliveFactor_Object = MibTableColumn
vRtrLdpPeerTemplKeepAliveFactor = _VRtrLdpPeerTemplKeepAliveFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 6),
    _VRtrLdpPeerTemplKeepAliveFactor_Type()
)
vRtrLdpPeerTemplKeepAliveFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplKeepAliveFactor.setStatus("current")


class _VRtrLdpPeerTemplKeepAliveTimeout_Type(TmnxLdpNewKeepAliveTimeout):
    """Custom type vRtrLdpPeerTemplKeepAliveTimeout based on TmnxLdpNewKeepAliveTimeout"""
    defaultValue = 40


_VRtrLdpPeerTemplKeepAliveTimeout_Type.__name__ = "TmnxLdpNewKeepAliveTimeout"
_VRtrLdpPeerTemplKeepAliveTimeout_Object = MibTableColumn
vRtrLdpPeerTemplKeepAliveTimeout = _VRtrLdpPeerTemplKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 7),
    _VRtrLdpPeerTemplKeepAliveTimeout_Type()
)
vRtrLdpPeerTemplKeepAliveTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplKeepAliveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplKeepAliveTimeout.setUnits("seconds")


class _VRtrLdpPeerTemplHelloFactor_Type(TmnxLdpHelloFactor):
    """Custom type vRtrLdpPeerTemplHelloFactor based on TmnxLdpHelloFactor"""
    defaultValue = 3


_VRtrLdpPeerTemplHelloFactor_Type.__name__ = "TmnxLdpHelloFactor"
_VRtrLdpPeerTemplHelloFactor_Object = MibTableColumn
vRtrLdpPeerTemplHelloFactor = _VRtrLdpPeerTemplHelloFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 8),
    _VRtrLdpPeerTemplHelloFactor_Type()
)
vRtrLdpPeerTemplHelloFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplHelloFactor.setStatus("current")


class _VRtrLdpPeerTemplHelloTimeout_Type(TmnxLdpNewHelloTimeout):
    """Custom type vRtrLdpPeerTemplHelloTimeout based on TmnxLdpNewHelloTimeout"""
    defaultValue = 45


_VRtrLdpPeerTemplHelloTimeout_Type.__name__ = "TmnxLdpNewHelloTimeout"
_VRtrLdpPeerTemplHelloTimeout_Object = MibTableColumn
vRtrLdpPeerTemplHelloTimeout = _VRtrLdpPeerTemplHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 9),
    _VRtrLdpPeerTemplHelloTimeout_Type()
)
vRtrLdpPeerTemplHelloTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplHelloTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplHelloTimeout.setUnits("seconds")


class _VRtrLdpPeerTemplTunneling_Type(TruthValue):
    """Custom type vRtrLdpPeerTemplTunneling based on TruthValue"""
    defaultValue = 2


_VRtrLdpPeerTemplTunneling_Type.__name__ = "TruthValue"
_VRtrLdpPeerTemplTunneling_Object = MibTableColumn
vRtrLdpPeerTemplTunneling = _VRtrLdpPeerTemplTunneling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 10),
    _VRtrLdpPeerTemplTunneling_Type()
)
vRtrLdpPeerTemplTunneling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplTunneling.setStatus("current")


class _VRtrLdpPeerTemplBfdEnabled_Type(TruthValue):
    """Custom type vRtrLdpPeerTemplBfdEnabled based on TruthValue"""
    defaultValue = 2


_VRtrLdpPeerTemplBfdEnabled_Type.__name__ = "TruthValue"
_VRtrLdpPeerTemplBfdEnabled_Object = MibTableColumn
vRtrLdpPeerTemplBfdEnabled = _VRtrLdpPeerTemplBfdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 11),
    _VRtrLdpPeerTemplBfdEnabled_Type()
)
vRtrLdpPeerTemplBfdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplBfdEnabled.setStatus("current")


class _VRtrLdpPeerTemplLsrIfIndex_Type(InterfaceIndexOrZero):
    """Custom type vRtrLdpPeerTemplLsrIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_VRtrLdpPeerTemplLsrIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_VRtrLdpPeerTemplLsrIfIndex_Object = MibTableColumn
vRtrLdpPeerTemplLsrIfIndex = _VRtrLdpPeerTemplLsrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 12),
    _VRtrLdpPeerTemplLsrIfIndex_Type()
)
vRtrLdpPeerTemplLsrIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplLsrIfIndex.setStatus("current")


class _VRtrLdpPeerTemplHelloReduction_Type(TruthValue):
    """Custom type vRtrLdpPeerTemplHelloReduction based on TruthValue"""
    defaultValue = 2


_VRtrLdpPeerTemplHelloReduction_Type.__name__ = "TruthValue"
_VRtrLdpPeerTemplHelloReduction_Object = MibTableColumn
vRtrLdpPeerTemplHelloReduction = _VRtrLdpPeerTemplHelloReduction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 13),
    _VRtrLdpPeerTemplHelloReduction_Type()
)
vRtrLdpPeerTemplHelloReduction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplHelloReduction.setStatus("current")


class _VRtrLdpPeerTemplHelloReductnFctr_Type(Unsigned32):
    """Custom type vRtrLdpPeerTemplHelloReductnFctr based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_VRtrLdpPeerTemplHelloReductnFctr_Type.__name__ = "Unsigned32"
_VRtrLdpPeerTemplHelloReductnFctr_Object = MibTableColumn
vRtrLdpPeerTemplHelloReductnFctr = _VRtrLdpPeerTemplHelloReductnFctr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 14),
    _VRtrLdpPeerTemplHelloReductnFctr_Type()
)
vRtrLdpPeerTemplHelloReductnFctr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplHelloReductnFctr.setStatus("current")
_VRtrLdpPeerTemplCreateTime_Type = TimeStamp
_VRtrLdpPeerTemplCreateTime_Object = MibTableColumn
vRtrLdpPeerTemplCreateTime = _VRtrLdpPeerTemplCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 15),
    _VRtrLdpPeerTemplCreateTime_Type()
)
vRtrLdpPeerTemplCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplCreateTime.setStatus("current")
_VRtrLdpPeerTemplIndex_Type = Counter64
_VRtrLdpPeerTemplIndex_Object = MibTableColumn
vRtrLdpPeerTemplIndex = _VRtrLdpPeerTemplIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 16),
    _VRtrLdpPeerTemplIndex_Type()
)
vRtrLdpPeerTemplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplIndex.setStatus("current")


class _VRtrLdpPeerTemplLsrIdAdvert_Type(TruthValue):
    """Custom type vRtrLdpPeerTemplLsrIdAdvert based on TruthValue"""
    defaultValue = 2


_VRtrLdpPeerTemplLsrIdAdvert_Type.__name__ = "TruthValue"
_VRtrLdpPeerTemplLsrIdAdvert_Object = MibTableColumn
vRtrLdpPeerTemplLsrIdAdvert = _VRtrLdpPeerTemplLsrIdAdvert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 17),
    _VRtrLdpPeerTemplLsrIdAdvert_Type()
)
vRtrLdpPeerTemplLsrIdAdvert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplLsrIdAdvert.setStatus("current")


class _VRtrLdpPeerTemplLsrIdCommunity_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpPeerTemplLsrIdCommunity based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPeerTemplLsrIdCommunity_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpPeerTemplLsrIdCommunity_Object = MibTableColumn
vRtrLdpPeerTemplLsrIdCommunity = _VRtrLdpPeerTemplLsrIdCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 18),
    _VRtrLdpPeerTemplLsrIdCommunity_Type()
)
vRtrLdpPeerTemplLsrIdCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplLsrIdCommunity.setStatus("current")


class _VRtrLdpPeerTemplMcastTunneling_Type(TruthValue):
    """Custom type vRtrLdpPeerTemplMcastTunneling based on TruthValue"""
    defaultValue = 2


_VRtrLdpPeerTemplMcastTunneling_Type.__name__ = "TruthValue"
_VRtrLdpPeerTemplMcastTunneling_Object = MibTableColumn
vRtrLdpPeerTemplMcastTunneling = _VRtrLdpPeerTemplMcastTunneling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 51, 1, 19),
    _VRtrLdpPeerTemplMcastTunneling_Type()
)
vRtrLdpPeerTemplMcastTunneling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplMcastTunneling.setStatus("current")
_VRtrLdpPeerTmplPlcyMpTblLstChgd_Type = TimeStamp
_VRtrLdpPeerTmplPlcyMpTblLstChgd_Object = MibScalar
vRtrLdpPeerTmplPlcyMpTblLstChgd = _VRtrLdpPeerTmplPlcyMpTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 52),
    _VRtrLdpPeerTmplPlcyMpTblLstChgd_Type()
)
vRtrLdpPeerTmplPlcyMpTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpPeerTmplPlcyMpTblLstChgd.setStatus("current")
_VRtrLdpPeerTemplPlcyMapTable_Object = MibTable
vRtrLdpPeerTemplPlcyMapTable = _VRtrLdpPeerTemplPlcyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 53)
)
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplPlcyMapTable.setStatus("current")
_VRtrLdpPeerTemplPlcyMapEntry_Object = MibTableRow
vRtrLdpPeerTemplPlcyMapEntry = _VRtrLdpPeerTemplPlcyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 53, 1)
)
vRtrLdpPeerTemplPlcyMapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerTemplName"),
)
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplPlcyMapEntry.setStatus("current")
_VRtrLdpPeerTemplPlcyMapLstChange_Type = TimeStamp
_VRtrLdpPeerTemplPlcyMapLstChange_Object = MibTableColumn
vRtrLdpPeerTemplPlcyMapLstChange = _VRtrLdpPeerTemplPlcyMapLstChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 53, 1, 1),
    _VRtrLdpPeerTemplPlcyMapLstChange_Type()
)
vRtrLdpPeerTemplPlcyMapLstChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplPlcyMapLstChange.setStatus("current")
_VRtrLdpPeerTemplPlcyMapRowStatus_Type = RowStatus
_VRtrLdpPeerTemplPlcyMapRowStatus_Object = MibTableColumn
vRtrLdpPeerTemplPlcyMapRowStatus = _VRtrLdpPeerTemplPlcyMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 53, 1, 2),
    _VRtrLdpPeerTemplPlcyMapRowStatus_Type()
)
vRtrLdpPeerTemplPlcyMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplPlcyMapRowStatus.setStatus("current")


class _VRtrLdpPeerTemplPlcyMapPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpPeerTemplPlcyMapPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPeerTemplPlcyMapPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpPeerTemplPlcyMapPolicy1_Object = MibTableColumn
vRtrLdpPeerTemplPlcyMapPolicy1 = _VRtrLdpPeerTemplPlcyMapPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 53, 1, 3),
    _VRtrLdpPeerTemplPlcyMapPolicy1_Type()
)
vRtrLdpPeerTemplPlcyMapPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplPlcyMapPolicy1.setStatus("current")


class _VRtrLdpPeerTemplPlcyMapPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpPeerTemplPlcyMapPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPeerTemplPlcyMapPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpPeerTemplPlcyMapPolicy2_Object = MibTableColumn
vRtrLdpPeerTemplPlcyMapPolicy2 = _VRtrLdpPeerTemplPlcyMapPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 53, 1, 4),
    _VRtrLdpPeerTemplPlcyMapPolicy2_Type()
)
vRtrLdpPeerTemplPlcyMapPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplPlcyMapPolicy2.setStatus("current")


class _VRtrLdpPeerTemplPlcyMapPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpPeerTemplPlcyMapPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPeerTemplPlcyMapPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpPeerTemplPlcyMapPolicy3_Object = MibTableColumn
vRtrLdpPeerTemplPlcyMapPolicy3 = _VRtrLdpPeerTemplPlcyMapPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 53, 1, 5),
    _VRtrLdpPeerTemplPlcyMapPolicy3_Type()
)
vRtrLdpPeerTemplPlcyMapPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplPlcyMapPolicy3.setStatus("current")


class _VRtrLdpPeerTemplPlcyMapPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpPeerTemplPlcyMapPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPeerTemplPlcyMapPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpPeerTemplPlcyMapPolicy4_Object = MibTableColumn
vRtrLdpPeerTemplPlcyMapPolicy4 = _VRtrLdpPeerTemplPlcyMapPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 53, 1, 6),
    _VRtrLdpPeerTemplPlcyMapPolicy4_Type()
)
vRtrLdpPeerTemplPlcyMapPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplPlcyMapPolicy4.setStatus("current")


class _VRtrLdpPeerTemplPlcyMapPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpPeerTemplPlcyMapPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPeerTemplPlcyMapPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpPeerTemplPlcyMapPolicy5_Object = MibTableColumn
vRtrLdpPeerTemplPlcyMapPolicy5 = _VRtrLdpPeerTemplPlcyMapPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 53, 1, 7),
    _VRtrLdpPeerTemplPlcyMapPolicy5_Type()
)
vRtrLdpPeerTemplPlcyMapPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplPlcyMapPolicy5.setStatus("current")
_VRtrLdpPeerTemplPlcyMapIndex_Type = Counter64
_VRtrLdpPeerTemplPlcyMapIndex_Object = MibTableColumn
vRtrLdpPeerTemplPlcyMapIndex = _VRtrLdpPeerTemplPlcyMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 53, 1, 8),
    _VRtrLdpPeerTemplPlcyMapIndex_Type()
)
vRtrLdpPeerTemplPlcyMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplPlcyMapIndex.setStatus("current")
_VRtrLdpPeerTemplPlcyMapCreateTim_Type = TimeStamp
_VRtrLdpPeerTemplPlcyMapCreateTim_Object = MibTableColumn
vRtrLdpPeerTemplPlcyMapCreateTim = _VRtrLdpPeerTemplPlcyMapCreateTim_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 53, 1, 9),
    _VRtrLdpPeerTemplPlcyMapCreateTim_Type()
)
vRtrLdpPeerTemplPlcyMapCreateTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplPlcyMapCreateTim.setStatus("current")
_VRtrLdpPeerTemplPeerTable_Object = MibTable
vRtrLdpPeerTemplPeerTable = _VRtrLdpPeerTemplPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 54)
)
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplPeerTable.setStatus("current")
_VRtrLdpPeerTemplPeerEntry_Object = MibTableRow
vRtrLdpPeerTemplPeerEntry = _VRtrLdpPeerTemplPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 54, 1)
)
vRtrLdpPeerTemplPeerEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerTemplName"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPeerAddrType"),
    (0, "TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPeerAddress"),
)
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplPeerEntry.setStatus("current")
_VRtrLdpPeerTemplPeerAddrType_Type = InetAddressType
_VRtrLdpPeerTemplPeerAddrType_Object = MibTableColumn
vRtrLdpPeerTemplPeerAddrType = _VRtrLdpPeerTemplPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 54, 1, 1),
    _VRtrLdpPeerTemplPeerAddrType_Type()
)
vRtrLdpPeerTemplPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplPeerAddrType.setStatus("current")


class _VRtrLdpPeerTemplPeerAddress_Type(InetAddress):
    """Custom type vRtrLdpPeerTemplPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpPeerTemplPeerAddress_Type.__name__ = "InetAddress"
_VRtrLdpPeerTemplPeerAddress_Object = MibTableColumn
vRtrLdpPeerTemplPeerAddress = _VRtrLdpPeerTemplPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 54, 1, 2),
    _VRtrLdpPeerTemplPeerAddress_Type()
)
vRtrLdpPeerTemplPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplPeerAddress.setStatus("current")
_VRtrLdpPeerTemplPeerCreateTime_Type = TimeStamp
_VRtrLdpPeerTemplPeerCreateTime_Object = MibTableColumn
vRtrLdpPeerTemplPeerCreateTime = _VRtrLdpPeerTemplPeerCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 54, 1, 3),
    _VRtrLdpPeerTemplPeerCreateTime_Type()
)
vRtrLdpPeerTemplPeerCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpPeerTemplPeerCreateTime.setStatus("current")
_TmnxLdpNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxLdpNotifyPrefix = _TmnxLdpNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 8)
)
_TmnxLdpNotifications_ObjectIdentity = ObjectIdentity
tmnxLdpNotifications = _TmnxLdpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 8, 0)
)
vRtrLdpGeneralEntry.registerAugmentions(
    ("TIMETRA-LDP-MIB",
     "vRtrLdpStatsEntry")
)
vRtrLdpStatsEntry.setIndexNames(*vRtrLdpGeneralEntry.getIndexNames())
vRtrLdpIfEntry.registerAugmentions(
    ("TIMETRA-LDP-MIB",
     "vRtrLdpIfStatsEntry")
)
vRtrLdpIfStatsEntry.setIndexNames(*vRtrLdpIfEntry.getIndexNames())
vRtrLdpSessionEntry.registerAugmentions(
    ("TIMETRA-LDP-MIB",
     "vRtrLdpSessionStatsEntry")
)
vRtrLdpSessionStatsEntry.setIndexNames(*vRtrLdpSessionEntry.getIndexNames())
vRtrLdpHelloAdjEntry.registerAugmentions(
    ("TIMETRA-LDP-MIB",
     "vRtrLdpAdjBackoffEntry")
)
vRtrLdpAdjBackoffEntry.setIndexNames(*vRtrLdpHelloAdjEntry.getIndexNames())
vRtrLdpGeneralEntry.registerAugmentions(
    ("TIMETRA-LDP-MIB",
     "vRtrLdpTargEntry")
)
vRtrLdpTargEntry.setIndexNames(*vRtrLdpGeneralEntry.getIndexNames())
vRtrLdpServFecEntry.registerAugmentions(
    ("TIMETRA-LDP-MIB",
     "vRtrLdpCepTdmFecEntry")
)
vRtrLdpCepTdmFecEntry.setIndexNames(*vRtrLdpServFecEntry.getIndexNames())
vLdpServFec129Entry.registerAugmentions(
    ("TIMETRA-LDP-MIB",
     "vLdpCepTdmFec129Entry")
)
vLdpCepTdmFec129Entry.setIndexNames(*vLdpServFec129Entry.getIndexNames())
vRtrLdpGeneralEntry.registerAugmentions(
    ("TIMETRA-LDP-MIB",
     "vRtrLdpAggrPreMatchEntry")
)
vRtrLdpAggrPreMatchEntry.setIndexNames(*vRtrLdpGeneralEntry.getIndexNames())
vRtrLdpEgrStatFecPfxEntry.registerAugmentions(
    ("TIMETRA-LDP-MIB",
     "vRtrLdpEgrStatisticsEntry")
)
vRtrLdpEgrStatisticsEntry.setIndexNames(*vRtrLdpEgrStatFecPfxEntry.getIndexNames())
vRtrLdpAddrFecEntry.registerAugmentions(
    ("TIMETRA-LDP-MIB",
     "vRtrLdpAddrFecExtEntry")
)
vRtrLdpAddrFecExtEntry.setIndexNames(*vRtrLdpAddrFecEntry.getIndexNames())

# Managed Objects groups

tmnxLdpAddrFecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 6)
)
tmnxLdpAddrFecGroup.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpAddrFecFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecNumInLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecNumOutLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapFecType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapIpPrefix"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapIpMask"))
)
if mibBuilder.loadTexts:
    tmnxLdpAddrFecGroup.setStatus("obsolete")

tmnxLdpNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 7)
)
tmnxLdpNotifyObjsGroup.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpInstanceNotifyReasonCode"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfNotifyReasonCode"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNotifyLocalGroupID"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNotifyRemoteGroupID"))
)
if mibBuilder.loadTexts:
    tmnxLdpNotifyObjsGroup.setStatus("obsolete")

tmnxLdpAdjBackoffGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 10)
)
tmnxLdpAdjBackoffGroup.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpAdjInitBackoff"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAdjMaxBackoff"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAdjCurrentBackoff"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAdjWaitingTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAdjBackoffStatus"))
)
if mibBuilder.loadTexts:
    tmnxLdpAdjBackoffGroup.setStatus("obsolete")

tmnxLdpObsoleteObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 11)
)
tmnxLdpObsoleteObjsGroup.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpNotifyLocalServiceID"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNotifyRemoteServiceID"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPolicyRowStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPolicyName"))
)
if mibBuilder.loadTexts:
    tmnxLdpObsoleteObjsGroup.setStatus("current")

tmnxLdpAdjR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 15)
)
tmnxLdpAdjR2r1Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjMapLdpId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjLocalLdpId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjEntityIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjHoldTimeRemaining"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjRemoteConfSeqNum"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjRemoteIpAddress"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjUpTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjLocalConfSeqNum"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjLocalIpAddress"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjInHelloMsgCount"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjOutHelloMsgCount"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjLocalHelloTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjRemoteHelloTimeout"))
)
if mibBuilder.loadTexts:
    tmnxLdpAdjR2r1Group.setStatus("obsolete")

tmnxLdpSessionR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 16)
)
tmnxLdpSessionR2r1Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpSessLocalLdpId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessEntityIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLabelDistMethod"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLoopDetectForPV"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessPathVectorLimit"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessAdjacencyType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessProtocolVersion"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLocalUdpPort"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessPeerUdpPort"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLocalTcpPort"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessPeerTcpPort"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLocalAddress"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessPeerAddress"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessKAHoldTimeRemaining"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessMaxPduLength"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessUpTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLocalKATimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessPeerKATimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsTargAdj"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLinkAdj"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsFECRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsFECSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsHelloIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsHelloOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsKeepaliveIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsKeepaliveOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsInitIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsInitOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelMappingIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelMappingOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelRequestIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelRequestOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelReleaseIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelReleaseOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelWithdrawIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelWithdrawOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelAbortIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelAbortOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrWithdrawIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrWithdrawOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsNotificationIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsNotificationOut"))
)
if mibBuilder.loadTexts:
    tmnxLdpSessionR2r1Group.setStatus("obsolete")

tmnxLdpStaticFecV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 17)
)
tmnxLdpStaticFecV3v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpStaticFecRowStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecNextNHIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecIngLabel"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecNumNH"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecOperIngLabel"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecNHRowStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecNHType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecNHIpAddr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecNHEgrLabel"))
)
if mibBuilder.loadTexts:
    tmnxLdpStaticFecV3v0Group.setStatus("obsolete")

tmnxLdpIfV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 19)
)
tmnxLdpIfV3v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpIfTableSpinlock"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfRowStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfLastChange"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfAdminState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfOperState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfInheritance"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfKeepAliveFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfKeepAliveTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfHelloFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfHelloTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfBackoffTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfMaxBackoffTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfTransportAddrType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfPassiveMode"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfAutoCreate"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfOperDownReason"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfExistingAdjacencies"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerRowStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerAuth"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerAuthKey"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerMinTTLValue"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTTLLogId"))
)
if mibBuilder.loadTexts:
    tmnxLdpIfV3v0Group.setStatus("obsolete")

tmnxLdpGlobalV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 20)
)
tmnxLdpGlobalV3v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpGenLastChange"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenAdminState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenOperState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenLdpLsrId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenProtocolVersion"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenDeaggregateFec"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenKeepAliveFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenKeepAliveTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenHelloFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenHelloTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenRoutePreference"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenControlMode"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenDistMethod"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenRetentionMode"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTransportAddrType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenPropagatePolicy"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenLoopDetectCapable"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenHopLimit"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenPathVectorLimit"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenBackoffTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenMaxBackoffTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargKeepAliveFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargKeepAliveTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargHelloFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargHelloTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargPassiveMode"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargetedSessions"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenCreateTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenUpTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTunnelDownDampTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenOperDownReason"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTrustList"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsOperDownEvents"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsActiveSessions"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsActiveAdjacencies"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsActiveInterfaces"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsInactiveInterfaces"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsActiveTargSessions"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsInactiveTargSessions"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsAddrFECRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsAddrFECSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsSvcFECRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsSvcFECSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsAttemptedSessions"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejNoHelloErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejAdvErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejMaxPduErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejLabelRangeErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsBadLdpIdentifierErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsBadPduLengthErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsBadMessageLengthErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsBadTlvLengthErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsMalformedTlvValueErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsKeepAliveExpiredErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsShutdownNotifRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsShutdownNotifSent"))
)
if mibBuilder.loadTexts:
    tmnxLdpGlobalV3v0Group.setStatus("obsolete")

tmnxLdpServFecV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 21)
)
tmnxLdpServFecV4v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpServFecServType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecServId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecVpnId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecNumInLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecNumOutLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecSdpId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalMTU"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteMTU"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalVlanTag"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteVlanTag"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalMaxCellConcat"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteMaxCellConcat"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecMapFecType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecMapVcType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecMapVcId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus5"))
)
if mibBuilder.loadTexts:
    tmnxLdpServFecV4v0Group.setStatus("obsolete")

tmnxLdpGlobalV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 22)
)
tmnxLdpGlobalV5v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpGenLastChange"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenAdminState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenOperState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenLdpLsrId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenProtocolVersion"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenDeaggregateFec"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenKeepAliveFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenKeepAliveTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenHelloFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenHelloTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenRoutePreference"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenControlMode"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenDistMethod"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenRetentionMode"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTransportAddrType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenPropagatePolicy"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenLoopDetectCapable"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenHopLimit"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenPathVectorLimit"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenBackoffTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenMaxBackoffTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargKeepAliveFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargKeepAliveTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargHelloFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargHelloTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargPassiveMode"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargetedSessions"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenCreateTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenUpTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTunnelDownDampTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenOperDownReason"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenGracefulRestart"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenGRNbrLiveTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenGRMaxRecoveryTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargImportPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargImportPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargImportPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargImportPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargImportPolicy5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargExportPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargExportPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargExportPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargExportPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargExportPolicy5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargTunnelPreference"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsOperDownEvents"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsActiveSessions"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsActiveAdjacencies"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsActiveInterfaces"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsInactiveInterfaces"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsActiveTargSessions"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsInactiveTargSessions"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsAddrFECRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsAddrFECSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsSvcFECRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsSvcFECSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsAttemptedSessions"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejNoHelloErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejAdvErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejMaxPduErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejLabelRangeErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsBadLdpIdentifierErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsBadPduLengthErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsBadMessageLengthErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsBadTlvLengthErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsMalformedTlvValueErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsKeepAliveExpiredErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsShutdownNotifRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsShutdownNotifSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsEgrFecPfxCount"))
)
if mibBuilder.loadTexts:
    tmnxLdpGlobalV5v0Group.setStatus("obsolete")

tmnxLdpIfV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 23)
)
tmnxLdpIfV5v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpIfTableSpinlock"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfRowStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfLastChange"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfAdminState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfOperState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfInheritance"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfKeepAliveFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfKeepAliveTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfHelloFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfHelloTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfBackoffTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfMaxBackoffTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfTransportAddrType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfPassiveMode"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfAutoCreate"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfOperDownReason"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfExistingAdjacencies"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfTunneling"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfLspRowStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerRowStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerAuth"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerAuthKey"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerMinTTLValue"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTTLLogId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerAuthKeyChain"))
)
if mibBuilder.loadTexts:
    tmnxLdpIfV5v0Group.setStatus("obsolete")

tmnxLdpServFecV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 24)
)
tmnxLdpServFecV5v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpServFecServType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecServId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecVpnId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecNumInLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecNumOutLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecSdpId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalMTU"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteMTU"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalVlanTag"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteVlanTag"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalMaxCellConcat"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteMaxCellConcat"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecMapFecType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecMapVcType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecMapVcId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecMateEndpointVcId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecMateEndpointSdpId"))
)
if mibBuilder.loadTexts:
    tmnxLdpServFecV5v0Group.setStatus("obsolete")

tmnxLdpAddrFecV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 25)
)
tmnxLdpAddrFecV5v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpAddrFecFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecNumInLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecNumOutLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapFecType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapIpPrefix"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapIpMask"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop5"))
)
if mibBuilder.loadTexts:
    tmnxLdpAddrFecV5v0Group.setStatus("obsolete")

tmnxLdpSessionV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 26)
)
tmnxLdpSessionV5v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpSessLocalLdpId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessEntityIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLabelDistMethod"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLoopDetectForPV"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessPathVectorLimit"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessAdjacencyType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessProtocolVersion"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLocalUdpPort"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessPeerUdpPort"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLocalTcpPort"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessPeerTcpPort"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLocalAddress"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessPeerAddress"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessKAHoldTimeRemaining"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessMaxPduLength"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessUpTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLocalKATimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessPeerKATimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessAdvertise"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessRestartHelperState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessPeerNumRestart"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLastRestartTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessFtReconnectTimeNego"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessFtRecoveryTimeNego"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessFtReconTimeRemaining"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessFtRecovTimeRemaining"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsTargAdj"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLinkAdj"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsFECRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsFECSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsHelloIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsHelloOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsKeepaliveIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsKeepaliveOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsInitIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsInitOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelMappingIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelMappingOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelRequestIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelRequestOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelReleaseIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelReleaseOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelWithdrawIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelWithdrawOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelAbortIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelAbortOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrWithdrawIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrWithdrawOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsNotificationIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsNotificationOut"))
)
if mibBuilder.loadTexts:
    tmnxLdpSessionV5v0Group.setStatus("obsolete")

tmnxLdpObsoletedV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 27)
)
tmnxLdpObsoletedV5v0Group.setObjects(
    ("TIMETRA-LDP-MIB", "vRtrLdpGenTrustList")
)
if mibBuilder.loadTexts:
    tmnxLdpObsoletedV5v0Group.setStatus("current")

tmnxLdpCepTdmFecV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 28)
)
tmnxLdpCepTdmFecV6v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalPayloadSize"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemotePayloadSize"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalBitrate"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteBitrate"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalRtpHeader"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteRtpHeader"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalDiffTimestamp"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteDiffTimestamp"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalSigPkts"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteSigPkts"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalCasTrunk"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteCasTrunk"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalTimestampFreq"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteTimestampFreq"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalPayloadType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemotePayloadType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalSsrcId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteSsrcId"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalPayloadSize"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemotePayloadSize"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalBitrate"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteBitrate"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalRtpHeader"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteRtpHeader"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalDiffTimestamp"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteDiffTimestamp"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalSigPkts"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteSigPkts"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalCasTrunk"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteCasTrunk"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalTimestampFreq"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteTimestampFreq"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalPayloadType"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemotePayloadType"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalSsrcId"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteSsrcId"))
)
if mibBuilder.loadTexts:
    tmnxLdpCepTdmFecV6v0Group.setStatus("obsolete")

tmnxLdpServFecV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 29)
)
tmnxLdpServFecV6v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpServFecServType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecServId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecVpnId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecNumInLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecNumOutLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecSdpId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalMTU"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteMTU"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalVlanTag"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteVlanTag"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalMaxCellConcat"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteMaxCellConcat"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecMateEndpointVcId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecMateEndpointSdpId"))
)
if mibBuilder.loadTexts:
    tmnxLdpServFecV6v0Group.setStatus("obsolete")

tmnxLdpServFec129V6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 30)
)
tmnxLdpServFec129V6v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vLdpServFec129ServType"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129ServId"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129VpnId"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129Flags"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129NumInLabels"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129NumOutLabels"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129InLabel1"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129InLabelStatus1"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129OutLabel1"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129OutLabelStatus1"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129SdpId"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129LocalMTU"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129RemoteMTU"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129LocalVlanTag"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129RemoteVlanTag"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129LocalMaxCellConcat"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129RemoteMaxCellConcat"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129InLabelSigStatus1"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129OutLabelSigStatus1"))
)
if mibBuilder.loadTexts:
    tmnxLdpServFec129V6v0Group.setStatus("obsolete")

tmnxLdpServFecObsoletedV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 31)
)
tmnxLdpServFecObsoletedV6v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpServFecMapFecType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecMapVcType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecMapVcId"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129MapVcType"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129MapAgiTlv"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129MapSrcAiiTlv"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129MapTgtAiiTlv"))
)
if mibBuilder.loadTexts:
    tmnxLdpServFecObsoletedV6v0Group.setStatus("current")

tmnxLdpAggrPreMatchV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 32)
)
tmnxLdpAggrPreMatchV7v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpAggrPreMatchAdminState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAggrPreMatchEnabled"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAggrPreMatchPreExcPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAggrPreMatchPreExcPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAggrPreMatchPreExcPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAggrPreMatchPreExcPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAggrPreMatchPreExcPolicy5"))
)
if mibBuilder.loadTexts:
    tmnxLdpAggrPreMatchV7v0Group.setStatus("obsolete")

tmnxLdpObsoletedV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 33)
)
tmnxLdpObsoletedV4v0Group.setObjects(
    ("TIMETRA-LDP-MIB", "vRtrLdpIfNotifyReasonCode")
)
if mibBuilder.loadTexts:
    tmnxLdpObsoletedV4v0Group.setStatus("current")

tmnxLdpNotifyObjsV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 34)
)
tmnxLdpNotifyObjsV4v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpInstanceNotifyReasonCode"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNotifyLocalGroupID"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNotifyRemoteGroupID"))
)
if mibBuilder.loadTexts:
    tmnxLdpNotifyObjsV4v0Group.setStatus("obsolete")

tmnxLdpStatsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 35)
)
tmnxLdpStatsV7v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpEgrStatFecPfxTblLastChgd"),
        ("TIMETRA-LDP-MIB", "vRtrLdpEgrStatFecPfxLastChgd"),
        ("TIMETRA-LDP-MIB", "vRtrLdpEgrStatFecPfxRowStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpEgrStatFecPfxActgPol"),
        ("TIMETRA-LDP-MIB", "vRtrLdpEgrStatFecPfxCollStats"),
        ("TIMETRA-LDP-MIB", "vRtrLdpEgrStatFecPfxAdminState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc0"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc0High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc0Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc1High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc1Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc2High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc2Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc3High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc3Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc4High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc4Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc5High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc5Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc6"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc6High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc6Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc7"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc7High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfileOctetsFc7Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc0"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc0High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc0Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc1High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc1Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc2High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc2Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc3High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc3Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc4High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc4Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc5High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc5Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc6"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc6High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc6Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc7"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc7High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInProfilePktsFc7Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc0"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc0High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc0Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc1High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc1Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc2High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc2Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc3High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc3Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc4High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc4Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc5High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc5Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc6"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc6High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc6Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc7"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc7High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfOctetsFc7Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc0"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc0High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc0Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc1High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc1Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc2High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc2Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc3High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc3Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc4High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc4Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc5High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc5Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc6"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc6High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc6Low32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc7"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc7High32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpOutOfProfPktsFc7Low32"))
)
if mibBuilder.loadTexts:
    tmnxLdpStatsV7v0Group.setStatus("current")

tmnxLdpAddrFecV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 36)
)
tmnxLdpAddrFecV7v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId6"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId7"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId8"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId9"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId10"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId11"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId12"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId13"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId14"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId15"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId16"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl6"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl7"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl8"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl9"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl10"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl11"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl12"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl13"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl14"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl15"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl16"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex6"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex7"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex8"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex9"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex10"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex11"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex12"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex13"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex14"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex15"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex16"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr6"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr7"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr8"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr9"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr10"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr11"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr12"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr13"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr14"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr15"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr16"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType6"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType7"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType8"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType9"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType10"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType11"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType12"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType13"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType14"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType15"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType16"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus6"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus7"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus8"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus9"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus10"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus11"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus12"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus13"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus14"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus15"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus16"))
)
if mibBuilder.loadTexts:
    tmnxLdpAddrFecV7v0Group.setStatus("obsolete")

tmnxLdpGenExtGlobalV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 37)
)
tmnxLdpGenExtGlobalV5v0Group.setObjects(
    ("TIMETRA-LDP-MIB", "vRtrLdpGenLabelWithdrawalDelay")
)
if mibBuilder.loadTexts:
    tmnxLdpGenExtGlobalV5v0Group.setStatus("obsolete")

tmnxLdpGlobalV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 38)
)
tmnxLdpGlobalV8v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpIfBfdEnabled"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfLinkLsrIfType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfTargLsrIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenImplicitNull"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenShortTTLPropLocal"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenShortTTLPropTransit"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerDODLabelDistribution"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfMulticast"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenMPMBBTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerImportPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerImportPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerImportPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerImportPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerImportPolicy5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerExportPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerExportPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerExportPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerExportPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerExportPolicy5"))
)
if mibBuilder.loadTexts:
    tmnxLdpGlobalV8v0Group.setStatus("obsolete")

tmnxLdpSessionV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 39)
)
tmnxLdpSessionV8v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpSessBfdStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessP2MPCapabilityNego"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessMPMBBCapabilityNego"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessDynamicCapabilityNego"))
)
if mibBuilder.loadTexts:
    tmnxLdpSessionV8v0Group.setStatus("obsolete")

tmnxLdpP2MPFecV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 40)
)
tmnxLdpP2MPFecV8v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecNumInLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecNumOutLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecInLbl"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecInLblStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecInLblIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecOutLbl"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecOutLblStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecOutLblNxtHopType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecOutLblNxtHopAddr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecOutLblIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecOutLblLspId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecMapFecType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecMapId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecTunnelIfId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecMetric"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecMTU"))
)
if mibBuilder.loadTexts:
    tmnxLdpP2MPFecV8v0Group.setStatus("obsolete")

tmnxLdpStatsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 41)
)
tmnxLdpStatsV8v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpStatsUnknownTlvErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsP2MPFECSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsP2MPFECRecv"))
)
if mibBuilder.loadTexts:
    tmnxLdpStatsV8v0Group.setStatus("obsolete")

tmnxLdpPeerV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 42)
)
tmnxLdpPeerV7v0Group.setObjects(
    ("TIMETRA-LDP-MIB", "vRtrLdpPeerFec129CiscoInterop")
)
if mibBuilder.loadTexts:
    tmnxLdpPeerV7v0Group.setStatus("obsolete")

tmnxLdpServFecV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 43)
)
tmnxLdpServFecV8v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalIpv4Capblty"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteIpv4Capblty"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalIpv6Capblty"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteIpv6Capblty"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalIpv4CeIpAddr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteIpv4CeIpAddr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLbl1WdwReason"))
)
if mibBuilder.loadTexts:
    tmnxLdpServFecV8v0Group.setStatus("obsolete")

tmnxLdpServFec129V8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 44)
)
tmnxLdpServFec129V8v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vLdpServFec129LocalIpv4Capblty"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129RemoteIpv4Capblty"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129LocalIpv6Capblty"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129RemoteIpv6Capblty"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129LocalIpv4CeIpAddr"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129RemoteIpv4CeIpAddr"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129InLbl1WdwReason"))
)
if mibBuilder.loadTexts:
    tmnxLdpServFec129V8v0Group.setStatus("obsolete")

tmnxLdpAddrFecV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 45)
)
tmnxLdpAddrFecV8v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblMetric"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblMtu"))
)
if mibBuilder.loadTexts:
    tmnxLdpAddrFecV8v0Group.setStatus("obsolete")

tmnxLdpGlobalV8v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 46)
)
tmnxLdpGlobalV8v0R4Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpGenTunlTblExportPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTunlTblExportPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTunlTblExportPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTunlTblExportPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTunlTblExportPolicy5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerPMTUDiscovery"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenP2MPCapability"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenMPMBBCapability"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenDynamicCapability"))
)
if mibBuilder.loadTexts:
    tmnxLdpGlobalV8v0R4Group.setStatus("obsolete")

tmnxLdpGlobalV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 47)
)
tmnxLdpGlobalV9v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vLdpServFec129MateAgiTlv"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129MateSdpId"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129MateSrcAiiTlv"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129MateTgtAiiTlv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerPMTUDiscovery"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalFLTxCapblty"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalFLRxCapblty"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteFLTxCapblty"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteFLRxCapblty"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129LocalFLTxCapblty"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129LocalFLRxCapblty"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129RemoteFLTxCapblty"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129RemoteFLRxCapblty"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerAdvAdjAddrOnly"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessionAddrLocalLdpId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessionAddrNumInAddrs"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessionAddrNumOutAddrs"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessionInAddrLocalLdpId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessionOutAddrLocalLdpId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrSent"))
)
if mibBuilder.loadTexts:
    tmnxLdpGlobalV9v0Group.setStatus("obsolete")

tmnxLdpGlobalV9v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 48)
)
tmnxLdpGlobalV9v0R4Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpGenLdpFrr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjBfdStatus"))
)
if mibBuilder.loadTexts:
    tmnxLdpGlobalV9v0R4Group.setStatus("obsolete")

tmnxLdpP2MPFecV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 49)
)
tmnxLdpP2MPFecV10v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecNumInLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecNumOutLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecTunnelIfId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecMetric"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecMTU"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecInLbl"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecInLblStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecInLblIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOutLbl"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOutLblStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOutLblNxtHopType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOutLblNxtHopAddr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOutLblIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOutLblLspId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecMapFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecMapNumInLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecMapNumOutLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecMapTunnelIfId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecMapMetric"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecMapMTU"))
)
if mibBuilder.loadTexts:
    tmnxLdpP2MPFecV10v0Group.setStatus("obsolete")

tmnxLdpAddressFecV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 50)
)
tmnxLdpAddressFecV10v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpAddressFecFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecNumInLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecNumOutLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecInLbl"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecInLblStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecInLblIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecOutLbl"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecOutLblStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecOutLblIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecOutLblNHType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecOutLblNHAddr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecOutLblMetric"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecOutLblMtu"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecOutLblLspId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecMapFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecMapNumInLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecMapNumOutLabels"))
)
if mibBuilder.loadTexts:
    tmnxLdpAddressFecV10v0Group.setStatus("obsolete")

tmnxLdpAddrActiveFecV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 51)
)
tmnxLdpAddrActiveFecV10v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecFecFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecNumInLbls"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecNumOutLbls"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecInLbl"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecInLblIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOutLbl"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOutLblStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOutLblIfIdx"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOutLblNHType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOutLblNHAddr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOutLblMetric"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOutLblMtu"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOutLblLspId"))
)
if mibBuilder.loadTexts:
    tmnxLdpAddrActiveFecV10v0Group.setStatus("obsolete")

tmnxLdpAddrFecObsoletedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 52)
)
tmnxLdpAddrFecObsoletedGroup.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpAddrFecFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecNumInLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecNumOutLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapFecType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapIpPrefix"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapIpMask"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl6"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus6"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex6"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType6"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr6"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId6"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl7"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus7"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex7"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType7"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr7"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId7"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl8"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus8"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex8"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType8"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr8"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId8"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl9"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus9"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex9"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType9"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr9"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId9"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl10"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus10"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex10"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType10"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr10"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId10"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl11"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus11"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex11"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType11"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr11"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId11"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl12"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus12"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex12"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType12"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr12"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId12"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl13"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus13"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex13"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType13"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr13"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId13"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl14"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus14"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex14"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType14"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr14"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId14"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl15"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus15"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex15"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType15"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr15"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId15"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLbl16"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblStatus16"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblIfIndex16"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopType16"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblNxtHopAddr16"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId16"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblMetric"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLblMtu"))
)
if mibBuilder.loadTexts:
    tmnxLdpAddrFecObsoletedGroup.setStatus("current")

tmnxLdpP2MPFecObsoletedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 53)
)
tmnxLdpP2MPFecObsoletedGroup.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecNumInLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecNumOutLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecInLbl"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecInLblStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecInLblIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecOutLbl"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecOutLblStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecOutLblNxtHopType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecOutLblNxtHopAddr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecOutLblIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecOutLblLspId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecMapFecType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecMapId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecTunnelIfId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecMetric"),
        ("TIMETRA-LDP-MIB", "vRtrLdpP2MPFecMTU"))
)
if mibBuilder.loadTexts:
    tmnxLdpP2MPFecObsoletedGroup.setStatus("current")

tmnxLdpHelloReductionV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 54)
)
tmnxLdpHelloReductionV11v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpGenTargHelloReduction"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargHelloReductionFctr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfHelloReduction"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfHelloReductionFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfOperHelloTimeout"))
)
if mibBuilder.loadTexts:
    tmnxLdpHelloReductionV11v0Group.setStatus("obsolete")

tmnxLdpGlobalV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 55)
)
tmnxLdpGlobalV11v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpIfLinkLsrIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecNHIfName"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenMcastUpstreamFrr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerPeIDMacFlushInterop"))
)
if mibBuilder.loadTexts:
    tmnxLdpGlobalV11v0Group.setStatus("obsolete")

tmnxLdpLsrOverloadV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 56)
)
tmnxLdpLsrOverloadV11v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpGenOverloadCapability"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessOvrloadCapabltyNego"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessAddrFecOverloadSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessAddrFecOverloadRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessMcastFecOverloadSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessMcastFecOverloadRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessServFecOverloadSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessServFecOverloadRecv"))
)
if mibBuilder.loadTexts:
    tmnxLdpLsrOverloadV11v0Group.setStatus("obsolete")

tmnxLdpTLDPAutoCreateV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 57)
)
tmnxLdpTLDPAutoCreateV11v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplRowStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplLastChanged"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplAdminState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplInheritance"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplKeepAliveFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplKeepAliveTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplHelloFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplHelloTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplTunneling"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplBfdEnabled"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplLsrIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplHelloReduction"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplHelloReductnFctr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplCreateTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPlcyMapPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPlcyMapPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPlcyMapPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPlcyMapPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPlcyMapPolicy5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPlcyMapIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPlcyMapCreateTim"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPlcyMapLstChange"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPlcyMapRowStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplTableLstChanged"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTmplPlcyMpTblLstChgd"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPeerCreateTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfCreator"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfTemplName"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfUpTime"))
)
if mibBuilder.loadTexts:
    tmnxLdpTLDPAutoCreateV11v0Group.setStatus("obsolete")

tmnxLdpLsrOvrloadNotifyObjs = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 58)
)
tmnxLdpLsrOvrloadNotifyObjs.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpSessOverloadState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessOverloadDirection"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessOverloadFecType"))
)
if mibBuilder.loadTexts:
    tmnxLdpLsrOvrloadNotifyObjs.setStatus("obsolete")

tmnxLdpFecLimitPerPeerV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 60)
)
tmnxLdpFecLimitPerPeerV13v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpPeerMaxFec"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerMaxFecLogOnly"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerMaxFecThreshold"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessOperMaxFecThreshold"))
)
if mibBuilder.loadTexts:
    tmnxLdpFecLimitPerPeerV13v0Group.setStatus("obsolete")

tmnxLdpFecLimitNotifyObjs = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 62)
)
tmnxLdpFecLimitNotifyObjs.setObjects(
    ("TIMETRA-LDP-MIB", "vRtrLdpSessOperThresLevel")
)
if mibBuilder.loadTexts:
    tmnxLdpFecLimitNotifyObjs.setStatus("obsolete")

tmnxLdpObsoletedV13V0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 63)
)
tmnxLdpObsoletedV13V0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpAdjInitBackoff"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAdjMaxBackoff"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAdjCurrentBackoff"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAdjWaitingTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAdjBackoffStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjMapLdpId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjLocalLdpId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjEntityIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjHoldTimeRemaining"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjRemoteConfSeqNum"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjRemoteIpAddress"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjUpTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjLocalConfSeqNum"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjLocalIpAddress"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjInHelloMsgCount"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjOutHelloMsgCount"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjLocalHelloTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjRemoteHelloTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecRowStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecNextNHIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecIngLabel"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecNumNH"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecOperIngLabel"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecNHRowStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecNHType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecNHIpAddr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecNHEgrLabel"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenLastChange"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenAdminState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenOperState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenLdpLsrId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenProtocolVersion"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenDeaggregateFec"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenKeepAliveFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenKeepAliveTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenHelloFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenHelloTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenRoutePreference"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenControlMode"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenDistMethod"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenRetentionMode"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTransportAddrType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenPropagatePolicy"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenLoopDetectCapable"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenHopLimit"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenPathVectorLimit"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenBackoffTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenMaxBackoffTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargKeepAliveFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargKeepAliveTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargHelloFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargHelloTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargPassiveMode"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargetedSessions"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenCreateTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenUpTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTunnelDownDampTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenOperDownReason"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenGracefulRestart"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenGRNbrLiveTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenGRMaxRecoveryTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargImportPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargImportPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargImportPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargImportPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargImportPolicy5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargExportPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargExportPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargExportPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargExportPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargExportPolicy5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpTargTunnelPreference"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsOperDownEvents"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsActiveSessions"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsActiveAdjacencies"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsActiveInterfaces"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsInactiveInterfaces"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsActiveTargSessions"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsInactiveTargSessions"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsAddrFECRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsAddrFECSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsSvcFECRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsSvcFECSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsAttemptedSessions"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejNoHelloErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejAdvErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejMaxPduErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejLabelRangeErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsBadLdpIdentifierErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsBadPduLengthErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsBadMessageLengthErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsBadTlvLengthErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsMalformedTlvValueErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsKeepAliveExpiredErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsShutdownNotifRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsShutdownNotifSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsEgrFecPfxCount"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfTableSpinlock"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfRowStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfLastChange"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfAdminState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfOperState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfInheritance"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfKeepAliveFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfKeepAliveTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfHelloFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfHelloTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfBackoffTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfMaxBackoffTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfTransportAddrType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfPassiveMode"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfAutoCreate"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfOperDownReason"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfExistingAdjacencies"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfTunneling"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfLspRowStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerRowStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerAuth"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerAuthKey"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerMinTTLValue"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTTLLogId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerAuthKeyChain"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLocalLdpId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessEntityIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLabelDistMethod"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLoopDetectForPV"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessPathVectorLimit"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessAdjacencyType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessProtocolVersion"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLocalUdpPort"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessPeerUdpPort"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLocalTcpPort"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessPeerTcpPort"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLocalAddress"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessPeerAddress"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessKAHoldTimeRemaining"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessMaxPduLength"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessUpTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLocalKATimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessPeerKATimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessAdvertise"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessRestartHelperState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessPeerNumRestart"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessLastRestartTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessFtReconnectTimeNego"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessFtRecoveryTimeNego"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessFtReconTimeRemaining"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessFtRecovTimeRemaining"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsTargAdj"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLinkAdj"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsFECRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsFECSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsHelloIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsHelloOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsKeepaliveIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsKeepaliveOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsInitIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsInitOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelMappingIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelMappingOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelRequestIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelRequestOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelReleaseIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelReleaseOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelWithdrawIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelWithdrawOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelAbortIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelAbortOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrWithdrawIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrWithdrawOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsNotificationIn"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsNotificationOut"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalPayloadSize"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemotePayloadSize"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalBitrate"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteBitrate"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalRtpHeader"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteRtpHeader"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalDiffTimestamp"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteDiffTimestamp"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalSigPkts"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteSigPkts"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalCasTrunk"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteCasTrunk"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalTimestampFreq"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteTimestampFreq"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalPayloadType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemotePayloadType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalSsrcId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteSsrcId"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalPayloadSize"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemotePayloadSize"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalBitrate"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteBitrate"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalRtpHeader"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteRtpHeader"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalDiffTimestamp"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteDiffTimestamp"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalSigPkts"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteSigPkts"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalCasTrunk"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteCasTrunk"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalTimestampFreq"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteTimestampFreq"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalPayloadType"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemotePayloadType"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalSsrcId"),
        ("TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteSsrcId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecServType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecServId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecVpnId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecNumInLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecNumOutLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecSdpId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalMTU"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteMTU"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalVlanTag"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteVlanTag"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalMaxCellConcat"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteMaxCellConcat"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecMateEndpointVcId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecMateEndpointSdpId"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129ServType"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129ServId"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129VpnId"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129Flags"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129NumInLabels"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129NumOutLabels"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129InLabel1"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129InLabelStatus1"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129OutLabel1"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129OutLabelStatus1"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129SdpId"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129LocalMTU"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129RemoteMTU"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129LocalVlanTag"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129RemoteVlanTag"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129LocalMaxCellConcat"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129RemoteMaxCellConcat"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129InLabelSigStatus1"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129OutLabelSigStatus1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAggrPreMatchAdminState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAggrPreMatchEnabled"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAggrPreMatchPreExcPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAggrPreMatchPreExcPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAggrPreMatchPreExcPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAggrPreMatchPreExcPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAggrPreMatchPreExcPolicy5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenLabelWithdrawalDelay"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfBfdEnabled"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfLinkLsrIfType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfTargLsrIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenImplicitNull"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenShortTTLPropLocal"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenShortTTLPropTransit"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerDODLabelDistribution"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfMulticast"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenMPMBBTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerImportPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerImportPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerImportPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerImportPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerImportPolicy5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerExportPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerExportPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerExportPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerExportPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerExportPolicy5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessBfdStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessP2MPCapabilityNego"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessMPMBBCapabilityNego"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessDynamicCapabilityNego"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsUnknownTlvErrors"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsP2MPFECSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStatsP2MPFECRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerFec129CiscoInterop"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalIpv4Capblty"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteIpv4Capblty"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalIpv6Capblty"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteIpv6Capblty"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalIpv4CeIpAddr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteIpv4CeIpAddr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecInLbl1WdwReason"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129LocalIpv4Capblty"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129RemoteIpv4Capblty"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129LocalIpv6Capblty"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129RemoteIpv6Capblty"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129LocalIpv4CeIpAddr"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129RemoteIpv4CeIpAddr"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129InLbl1WdwReason"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTunlTblExportPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTunlTblExportPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTunlTblExportPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTunlTblExportPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTunlTblExportPolicy5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerPMTUDiscovery"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenP2MPCapability"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenMPMBBCapability"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenDynamicCapability"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129MateAgiTlv"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129MateSdpId"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129MateSrcAiiTlv"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129MateTgtAiiTlv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerPMTUDiscovery"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalFLTxCapblty"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecLocalFLRxCapblty"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteFLTxCapblty"),
        ("TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteFLRxCapblty"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129LocalFLTxCapblty"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129LocalFLRxCapblty"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129RemoteFLTxCapblty"),
        ("TIMETRA-LDP-MIB", "vLdpServFec129RemoteFLRxCapblty"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerAdvAdjAddrOnly"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessionAddrLocalLdpId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessionAddrNumInAddrs"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessionAddrNumOutAddrs"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessionInAddrLocalLdpId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessionOutAddrLocalLdpId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenLdpFrr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpHelloAdjBfdStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecNumInLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecNumOutLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecTunnelIfId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecMetric"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecMTU"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecInLbl"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecInLblStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecInLblIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOutLbl"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOutLblStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOutLblNxtHopType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOutLblNxtHopAddr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOutLblIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecOutLblLspId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecMapFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecMapNumInLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecMapNumOutLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecMapTunnelIfId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecMapMetric"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNgP2MPFecMapMTU"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecNumInLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecNumOutLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecInLbl"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecInLblStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecInLblIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecOutLbl"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecOutLblStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecOutLblIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecOutLblNHType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecOutLblNHAddr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecOutLblMetric"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecOutLblMtu"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecOutLblLspId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecMapFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecMapNumInLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddressFecMapNumOutLabels"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecFecFlags"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecNumInLbls"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecNumOutLbls"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecInLbl"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecInLblIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOutLbl"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOutLblStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOutLblIfIdx"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOutLblNHType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOutLblNHAddr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOutLblMetric"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOutLblMtu"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAddrActiveFecOutLblLspId"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargHelloReduction"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenTargHelloReductionFctr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfHelloReduction"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfHelloReductionFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfOperHelloTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfLinkLsrIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpStaticFecNHIfName"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenMcastUpstreamFrr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerPeIDMacFlushInterop"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenOverloadCapability"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessOvrloadCapabltyNego"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessAddrFecOverloadSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessAddrFecOverloadRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessMcastFecOverloadSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessMcastFecOverloadRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessServFecOverloadSent"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessServFecOverloadRecv"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfCreator"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfTemplName"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfUpTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerMaxFec"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerMaxFecLogOnly"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerMaxFecThreshold"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessOperMaxFecThreshold"))
)
if mibBuilder.loadTexts:
    tmnxLdpObsoletedV13V0Group.setStatus("current")

tmnxLdpTLDPAutoCreateV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 64)
)
tmnxLdpTLDPAutoCreateV13v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplRowStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplLastChanged"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplAdminState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplInheritance"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplKeepAliveFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplKeepAliveTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplHelloFactor"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplHelloTimeout"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplTunneling"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplBfdEnabled"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplLsrIfIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplHelloReduction"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplHelloReductnFctr"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplCreateTime"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPlcyMapPolicy1"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPlcyMapPolicy2"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPlcyMapPolicy3"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPlcyMapPolicy4"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPlcyMapPolicy5"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPlcyMapIndex"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPlcyMapCreateTim"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPlcyMapLstChange"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPlcyMapRowStatus"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplTableLstChanged"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTmplPlcyMpTblLstChgd"),
        ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplPeerCreateTime"))
)
if mibBuilder.loadTexts:
    tmnxLdpTLDPAutoCreateV13v0Group.setStatus("current")

tmnxLdpNotifyObjsV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 65)
)
tmnxLdpNotifyObjsV13v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpNotifyLocalGroupID"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNotifyRemoteGroupID"))
)
if mibBuilder.loadTexts:
    tmnxLdpNotifyObjsV13v0Group.setStatus("current")

tmnxLdpObsoletedNotifyObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 66)
)
tmnxLdpObsoletedNotifyObjGroup.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpInstanceNotifyReasonCode"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessOverloadState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessOverloadDirection"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessOverloadFecType"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessOperThresLevel"))
)
if mibBuilder.loadTexts:
    tmnxLdpObsoletedNotifyObjGroup.setStatus("current")

tmnxLdpLocalLsrIdAdvertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 69)
)
tmnxLdpLocalLsrIdAdvertGroup.setObjects(
    ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplLsrIdAdvert")
)
if mibBuilder.loadTexts:
    tmnxLdpLocalLsrIdAdvertGroup.setStatus("current")

tmnxLdpLocalLsrIdCommunityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 70)
)
tmnxLdpLocalLsrIdCommunityGroup.setObjects(
    ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplLsrIdCommunity")
)
if mibBuilder.loadTexts:
    tmnxLdpLocalLsrIdCommunityGroup.setStatus("current")

tmnxLdpAggrEgrStatsV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 71)
)
tmnxLdpAggrEgrStatsV16v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpAggregatePkts"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAggregatePktsLow32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAggregatePktsHigh32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAggregateOctets"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAggregateOctetsLow32"),
        ("TIMETRA-LDP-MIB", "vRtrLdpAggregateOctetsHigh32"))
)
if mibBuilder.loadTexts:
    tmnxLdpAggrEgrStatsV16v0Group.setStatus("current")

tmnxLdpPeerMcastTunnelingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 72)
)
tmnxLdpPeerMcastTunnelingGroup.setObjects(
    ("TIMETRA-LDP-MIB", "vRtrLdpPeerTemplMcastTunneling")
)
if mibBuilder.loadTexts:
    tmnxLdpPeerMcastTunnelingGroup.setStatus("current")


# Notification objects

vRtrLdpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 8, 0, 1)
)
vRtrLdpStateChange.setObjects(
    ("TIMETRA-VRTR-MIB", "vRtrLdpStatus")
)
if mibBuilder.loadTexts:
    vRtrLdpStateChange.setStatus(
        "current"
    )

vRtrLdpInstanceStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 8, 0, 2)
)
vRtrLdpInstanceStateChange.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpGenAdminState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenOperState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInstanceNotifyReasonCode"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGenOperDownReason"))
)
if mibBuilder.loadTexts:
    vRtrLdpInstanceStateChange.setStatus(
        "obsolete"
    )

vRtrLdpIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 8, 0, 3)
)
vRtrLdpIfStateChange.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpIfAdminState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfOperState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfOperDownReason"))
)
if mibBuilder.loadTexts:
    vRtrLdpIfStateChange.setStatus(
        "obsolete"
    )

vRtrLdpSvcIdMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 8, 0, 4)
)
vRtrLdpSvcIdMismatch.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpNotifyLocalServiceID"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNotifyRemoteServiceID"))
)
if mibBuilder.loadTexts:
    vRtrLdpSvcIdMismatch.setStatus(
        "obsolete"
    )

vRtrLdpGroupIdMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 8, 0, 5)
)
vRtrLdpGroupIdMismatch.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpNotifyLocalGroupID"),
        ("TIMETRA-LDP-MIB", "vRtrLdpNotifyRemoteGroupID"))
)
if mibBuilder.loadTexts:
    vRtrLdpGroupIdMismatch.setStatus(
        "current"
    )

vRtrLdpSessionStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 8, 0, 6)
)
vRtrLdpSessionStateChange.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpSessState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessOverloadState"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessOverloadDirection"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessOverloadFecType"))
)
if mibBuilder.loadTexts:
    vRtrLdpSessionStateChange.setStatus(
        "obsolete"
    )

vRtrLdpSessMaxFecThresChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 8, 0, 7)
)
vRtrLdpSessMaxFecThresChanged.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpPeerMaxFec"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessOperThresLevel"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessOperMaxFecThreshold"))
)
if mibBuilder.loadTexts:
    vRtrLdpSessMaxFecThresChanged.setStatus(
        "obsolete"
    )

vRtrLdpSessMaxFecLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 8, 0, 8)
)
vRtrLdpSessMaxFecLimitReached.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpPeerMaxFec"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessOperMaxFecThreshold"))
)
if mibBuilder.loadTexts:
    vRtrLdpSessMaxFecLimitReached.setStatus(
        "obsolete"
    )


# Notifications groups

tmnxLdpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 8)
)
tmnxLdpNotificationGroup.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpStateChange"),
        ("TIMETRA-LDP-MIB", "vRtrLdpInstanceStateChange"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfStateChange"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGroupIdMismatch"))
)
if mibBuilder.loadTexts:
    tmnxLdpNotificationGroup.setStatus(
        "obsolete"
    )

tmnxLdpObsoleteNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 12)
)
tmnxLdpObsoleteNotificationGroup.setObjects(
    ("TIMETRA-LDP-MIB", "vRtrLdpSvcIdMismatch")
)
if mibBuilder.loadTexts:
    tmnxLdpObsoleteNotificationGroup.setStatus(
        "current"
    )

tmnxLdpLsrOvrloadNotify = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 59)
)
tmnxLdpLsrOvrloadNotify.setObjects(
    ("TIMETRA-LDP-MIB", "vRtrLdpSessionStateChange")
)
if mibBuilder.loadTexts:
    tmnxLdpLsrOvrloadNotify.setStatus(
        "obsolete"
    )

tmnxLdpFecLimitPerPeerNotify = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 61)
)
tmnxLdpFecLimitPerPeerNotify.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpSessMaxFecThresChanged"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessMaxFecLimitReached"))
)
if mibBuilder.loadTexts:
    tmnxLdpFecLimitPerPeerNotify.setStatus(
        "obsolete"
    )

tmnxLdpObsoletedNtfnV13v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 67)
)
tmnxLdpObsoletedNtfnV13v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpInstanceStateChange"),
        ("TIMETRA-LDP-MIB", "vRtrLdpIfStateChange"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessionStateChange"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessMaxFecThresChanged"),
        ("TIMETRA-LDP-MIB", "vRtrLdpSessMaxFecLimitReached"))
)
if mibBuilder.loadTexts:
    tmnxLdpObsoletedNtfnV13v0Group.setStatus(
        "current"
    )

tmnxLdpNotificationV13v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 68)
)
tmnxLdpNotificationV13v0Group.setObjects(
      *(("TIMETRA-LDP-MIB", "vRtrLdpStateChange"),
        ("TIMETRA-LDP-MIB", "vRtrLdpGroupIdMismatch"))
)
if mibBuilder.loadTexts:
    tmnxLdpNotificationV13v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxLdpV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 1, 4)
)
tmnxLdpV4v0Compliance.setObjects(
      *(("TIMETRA-LDP-MIB", "tmnxLdpGlobalV3v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpIfV3v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAdjR2r1Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpSessionR2r1Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFecV4v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAddrFecGroup"),
        ("TIMETRA-LDP-MIB", "tmnxLdpNotificationGroup"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStaticFecV3v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLdpV4v0Compliance.setStatus(
        "obsolete"
    )

tmnxLdpV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 1, 5)
)
tmnxLdpV5v0Compliance.setObjects(
      *(("TIMETRA-LDP-MIB", "tmnxLdpGlobalV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpIfV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAdjR2r1Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpSessionV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFecV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAddrFecV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpNotificationGroup"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStaticFecV3v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGenExtGlobalV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLdpV5v0Compliance.setStatus(
        "obsolete"
    )

tmnxLdpV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 1, 6)
)
tmnxLdpV6v0Compliance.setObjects(
      *(("TIMETRA-LDP-MIB", "tmnxLdpGlobalV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpIfV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAdjR2r1Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpSessionV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFecV6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFec129V6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAddrFecV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpNotificationGroup"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStaticFecV3v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpCepTdmFecV6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGenExtGlobalV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLdpV6v0Compliance.setStatus(
        "obsolete"
    )

tmnxLdpV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 1, 7)
)
tmnxLdpV7v0Compliance.setObjects(
      *(("TIMETRA-LDP-MIB", "tmnxLdpGlobalV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpIfV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAdjR2r1Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpSessionV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFecV6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFec129V6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAddrFecV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpNotificationGroup"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStaticFecV3v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAggrPreMatchV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStatsV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpCepTdmFecV6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGenExtGlobalV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLdpV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxLdpV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 1, 8)
)
tmnxLdpV8v0Compliance.setObjects(
      *(("TIMETRA-LDP-MIB", "tmnxLdpGlobalV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpIfV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAdjR2r1Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpSessionV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFecV6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFec129V6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAddrFecV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpNotificationGroup"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStaticFecV3v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAggrPreMatchV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStatsV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpCepTdmFecV6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGenExtGlobalV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpSessionV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpP2MPFecV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStatsV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpPeerV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFecV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFec129V8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAddrFecV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV8v0R4Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAddrFecV7v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLdpV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxLdpV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 1, 9)
)
tmnxLdpV9v0Compliance.setObjects(
      *(("TIMETRA-LDP-MIB", "tmnxLdpGlobalV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpIfV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAdjR2r1Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpSessionV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFecV6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFec129V6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAddrFecV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpNotificationGroup"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStaticFecV3v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAggrPreMatchV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStatsV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAdjBackoffGroup"),
        ("TIMETRA-LDP-MIB", "tmnxLdpCepTdmFecV6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGenExtGlobalV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpSessionV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpP2MPFecV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStatsV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpPeerV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFecV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFec129V8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAddrFecV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV8v0R4Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAddrFecV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV9v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV9v0R4Group"))
)
if mibBuilder.loadTexts:
    tmnxLdpV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxLdpV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 1, 10)
)
tmnxLdpV10v0Compliance.setObjects(
      *(("TIMETRA-LDP-MIB", "tmnxLdpGlobalV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpIfV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAdjR2r1Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpSessionV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFecV6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFec129V6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpNotificationGroup"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStaticFecV3v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAggrPreMatchV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStatsV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAdjBackoffGroup"),
        ("TIMETRA-LDP-MIB", "tmnxLdpCepTdmFecV6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGenExtGlobalV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpSessionV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStatsV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpPeerV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFecV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFec129V8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV8v0R4Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV9v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV9v0R4Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpP2MPFecV10v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAddressFecV10v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAddrActiveFecV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLdpV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxLdpV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 1, 11)
)
tmnxLdpV11v0Compliance.setObjects(
      *(("TIMETRA-LDP-MIB", "tmnxLdpGlobalV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpIfV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAdjR2r1Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpSessionV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFecV6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFec129V6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpNotificationGroup"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStaticFecV3v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAggrPreMatchV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStatsV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAdjBackoffGroup"),
        ("TIMETRA-LDP-MIB", "tmnxLdpCepTdmFecV6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGenExtGlobalV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpSessionV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStatsV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpPeerV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFecV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFec129V8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV8v0R4Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV9v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV9v0R4Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpP2MPFecV10v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAddressFecV10v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAddrActiveFecV10v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpHelloReductionV11v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV11v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpLsrOverloadV11v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpTLDPAutoCreateV11v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpLsrOvrloadNotify"),
        ("TIMETRA-LDP-MIB", "tmnxLdpLsrOvrloadNotifyObjs"))
)
if mibBuilder.loadTexts:
    tmnxLdpV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxLdpV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 1, 12)
)
tmnxLdpV12v0Compliance.setObjects(
      *(("TIMETRA-LDP-MIB", "tmnxLdpGlobalV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpIfV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAdjR2r1Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpSessionV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFecV6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFec129V6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpNotificationGroup"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStaticFecV3v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAggrPreMatchV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStatsV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAdjBackoffGroup"),
        ("TIMETRA-LDP-MIB", "tmnxLdpCepTdmFecV6v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGenExtGlobalV5v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpSessionV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpStatsV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpPeerV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFecV8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpServFec129V8v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV8v0R4Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV9v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV9v0R4Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpP2MPFecV10v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAddressFecV10v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpAddrActiveFecV10v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpHelloReductionV11v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpGlobalV11v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpLsrOverloadV11v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpTLDPAutoCreateV11v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpLsrOvrloadNotify"),
        ("TIMETRA-LDP-MIB", "tmnxLdpLsrOvrloadNotifyObjs"),
        ("TIMETRA-LDP-MIB", "tmnxLdpFecLimitPerPeerV13v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpFecLimitPerPeerNotify"),
        ("TIMETRA-LDP-MIB", "tmnxLdpFecLimitNotifyObjs"))
)
if mibBuilder.loadTexts:
    tmnxLdpV12v0Compliance.setStatus(
        "obsolete"
    )

tmnxLdpV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 1, 13)
)
tmnxLdpV13v0Compliance.setObjects(
      *(("TIMETRA-LDP-MIB", "tmnxLdpStatsV7v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpObsoletedV13V0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpTLDPAutoCreateV13v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpNotifyObjsV13v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpObsoletedNotifyObjGroup"),
        ("TIMETRA-LDP-MIB", "tmnxLdpObsoletedNtfnV13v0Group"),
        ("TIMETRA-LDP-MIB", "tmnxLdpNotificationV13v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLdpV13v0Compliance.setStatus(
        "current"
    )

tmnxLdpV15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 1, 14)
)
tmnxLdpV15v0Compliance.setObjects(
      *(("TIMETRA-LDP-MIB", "tmnxLdpLocalLsrIdAdvertGroup"),
        ("TIMETRA-LDP-MIB", "tmnxLdpLocalLsrIdCommunityGroup"))
)
if mibBuilder.loadTexts:
    tmnxLdpV15v0Compliance.setStatus(
        "current"
    )

tmnxLdpV16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 1, 15)
)
tmnxLdpV16v0Compliance.setObjects(
    ("TIMETRA-LDP-MIB", "tmnxLdpAggrEgrStatsV16v0Group")
)
if mibBuilder.loadTexts:
    tmnxLdpV16v0Compliance.setStatus(
        "current"
    )

tmnxLdpV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 1, 16)
)
tmnxLdpV20v0Compliance.setObjects(
    ("TIMETRA-LDP-MIB", "tmnxLdpPeerMcastTunnelingGroup")
)
if mibBuilder.loadTexts:
    tmnxLdpV20v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-LDP-MIB",
    **{"TmnxLdpKeepAliveFactor": TmnxLdpKeepAliveFactor,
       "TmnxLdpKeepAliveTimeout": TmnxLdpKeepAliveTimeout,
       "TmnxLdpHelloFactor": TmnxLdpHelloFactor,
       "TmnxLdpHelloTimeout": TmnxLdpHelloTimeout,
       "TmnxLdpBackoffTime": TmnxLdpBackoffTime,
       "TmnxLdpFECPolicy": TmnxLdpFECPolicy,
       "TmnxLdpLabelDistMethod": TmnxLdpLabelDistMethod,
       "TmnxLdpAdjacencyType": TmnxLdpAdjacencyType,
       "TmnxVpnId": TmnxVpnId,
       "TmnxLabelStatus": TmnxLabelStatus,
       "TmnxLabelSigStatus": TmnxLabelSigStatus,
       "TmnxLdpFECTunnelType": TmnxLdpFECTunnelType,
       "TmnxLdpFECFlags": TmnxLdpFECFlags,
       "TmnxLdpGenOperDownReasonCode": TmnxLdpGenOperDownReasonCode,
       "TmnxLdpIntTargOperDownReasonCode": TmnxLdpIntTargOperDownReasonCode,
       "TmnxLdpFec129Tlv": TmnxLdpFec129Tlv,
       "TmnxLdpNewKeepAliveTimeout": TmnxLdpNewKeepAliveTimeout,
       "TmnxLdpNewHelloTimeout": TmnxLdpNewHelloTimeout,
       "TmnxLdpInLblWdrawalReasonCode": TmnxLdpInLblWdrawalReasonCode,
       "timetraLdpMIBModule": timetraLdpMIBModule,
       "tmnxLdpConformance": tmnxLdpConformance,
       "tmnxLdpCompliances": tmnxLdpCompliances,
       "tmnxLdpV4v0Compliance": tmnxLdpV4v0Compliance,
       "tmnxLdpV5v0Compliance": tmnxLdpV5v0Compliance,
       "tmnxLdpV6v0Compliance": tmnxLdpV6v0Compliance,
       "tmnxLdpV7v0Compliance": tmnxLdpV7v0Compliance,
       "tmnxLdpV8v0Compliance": tmnxLdpV8v0Compliance,
       "tmnxLdpV9v0Compliance": tmnxLdpV9v0Compliance,
       "tmnxLdpV10v0Compliance": tmnxLdpV10v0Compliance,
       "tmnxLdpV11v0Compliance": tmnxLdpV11v0Compliance,
       "tmnxLdpV12v0Compliance": tmnxLdpV12v0Compliance,
       "tmnxLdpV13v0Compliance": tmnxLdpV13v0Compliance,
       "tmnxLdpV15v0Compliance": tmnxLdpV15v0Compliance,
       "tmnxLdpV16v0Compliance": tmnxLdpV16v0Compliance,
       "tmnxLdpV20v0Compliance": tmnxLdpV20v0Compliance,
       "tmnxLdpGroups": tmnxLdpGroups,
       "tmnxLdpAddrFecGroup": tmnxLdpAddrFecGroup,
       "tmnxLdpNotifyObjsGroup": tmnxLdpNotifyObjsGroup,
       "tmnxLdpNotificationGroup": tmnxLdpNotificationGroup,
       "tmnxLdpAdjBackoffGroup": tmnxLdpAdjBackoffGroup,
       "tmnxLdpObsoleteObjsGroup": tmnxLdpObsoleteObjsGroup,
       "tmnxLdpObsoleteNotificationGroup": tmnxLdpObsoleteNotificationGroup,
       "tmnxLdpAdjR2r1Group": tmnxLdpAdjR2r1Group,
       "tmnxLdpSessionR2r1Group": tmnxLdpSessionR2r1Group,
       "tmnxLdpStaticFecV3v0Group": tmnxLdpStaticFecV3v0Group,
       "tmnxLdpIfV3v0Group": tmnxLdpIfV3v0Group,
       "tmnxLdpGlobalV3v0Group": tmnxLdpGlobalV3v0Group,
       "tmnxLdpServFecV4v0Group": tmnxLdpServFecV4v0Group,
       "tmnxLdpGlobalV5v0Group": tmnxLdpGlobalV5v0Group,
       "tmnxLdpIfV5v0Group": tmnxLdpIfV5v0Group,
       "tmnxLdpServFecV5v0Group": tmnxLdpServFecV5v0Group,
       "tmnxLdpAddrFecV5v0Group": tmnxLdpAddrFecV5v0Group,
       "tmnxLdpSessionV5v0Group": tmnxLdpSessionV5v0Group,
       "tmnxLdpObsoletedV5v0Group": tmnxLdpObsoletedV5v0Group,
       "tmnxLdpCepTdmFecV6v0Group": tmnxLdpCepTdmFecV6v0Group,
       "tmnxLdpServFecV6v0Group": tmnxLdpServFecV6v0Group,
       "tmnxLdpServFec129V6v0Group": tmnxLdpServFec129V6v0Group,
       "tmnxLdpServFecObsoletedV6v0Group": tmnxLdpServFecObsoletedV6v0Group,
       "tmnxLdpAggrPreMatchV7v0Group": tmnxLdpAggrPreMatchV7v0Group,
       "tmnxLdpObsoletedV4v0Group": tmnxLdpObsoletedV4v0Group,
       "tmnxLdpNotifyObjsV4v0Group": tmnxLdpNotifyObjsV4v0Group,
       "tmnxLdpStatsV7v0Group": tmnxLdpStatsV7v0Group,
       "tmnxLdpAddrFecV7v0Group": tmnxLdpAddrFecV7v0Group,
       "tmnxLdpGenExtGlobalV5v0Group": tmnxLdpGenExtGlobalV5v0Group,
       "tmnxLdpGlobalV8v0Group": tmnxLdpGlobalV8v0Group,
       "tmnxLdpSessionV8v0Group": tmnxLdpSessionV8v0Group,
       "tmnxLdpP2MPFecV8v0Group": tmnxLdpP2MPFecV8v0Group,
       "tmnxLdpStatsV8v0Group": tmnxLdpStatsV8v0Group,
       "tmnxLdpPeerV7v0Group": tmnxLdpPeerV7v0Group,
       "tmnxLdpServFecV8v0Group": tmnxLdpServFecV8v0Group,
       "tmnxLdpServFec129V8v0Group": tmnxLdpServFec129V8v0Group,
       "tmnxLdpAddrFecV8v0Group": tmnxLdpAddrFecV8v0Group,
       "tmnxLdpGlobalV8v0R4Group": tmnxLdpGlobalV8v0R4Group,
       "tmnxLdpGlobalV9v0Group": tmnxLdpGlobalV9v0Group,
       "tmnxLdpGlobalV9v0R4Group": tmnxLdpGlobalV9v0R4Group,
       "tmnxLdpP2MPFecV10v0Group": tmnxLdpP2MPFecV10v0Group,
       "tmnxLdpAddressFecV10v0Group": tmnxLdpAddressFecV10v0Group,
       "tmnxLdpAddrActiveFecV10v0Group": tmnxLdpAddrActiveFecV10v0Group,
       "tmnxLdpAddrFecObsoletedGroup": tmnxLdpAddrFecObsoletedGroup,
       "tmnxLdpP2MPFecObsoletedGroup": tmnxLdpP2MPFecObsoletedGroup,
       "tmnxLdpHelloReductionV11v0Group": tmnxLdpHelloReductionV11v0Group,
       "tmnxLdpGlobalV11v0Group": tmnxLdpGlobalV11v0Group,
       "tmnxLdpLsrOverloadV11v0Group": tmnxLdpLsrOverloadV11v0Group,
       "tmnxLdpTLDPAutoCreateV11v0Group": tmnxLdpTLDPAutoCreateV11v0Group,
       "tmnxLdpLsrOvrloadNotifyObjs": tmnxLdpLsrOvrloadNotifyObjs,
       "tmnxLdpLsrOvrloadNotify": tmnxLdpLsrOvrloadNotify,
       "tmnxLdpFecLimitPerPeerV13v0Group": tmnxLdpFecLimitPerPeerV13v0Group,
       "tmnxLdpFecLimitPerPeerNotify": tmnxLdpFecLimitPerPeerNotify,
       "tmnxLdpFecLimitNotifyObjs": tmnxLdpFecLimitNotifyObjs,
       "tmnxLdpObsoletedV13V0Group": tmnxLdpObsoletedV13V0Group,
       "tmnxLdpTLDPAutoCreateV13v0Group": tmnxLdpTLDPAutoCreateV13v0Group,
       "tmnxLdpNotifyObjsV13v0Group": tmnxLdpNotifyObjsV13v0Group,
       "tmnxLdpObsoletedNotifyObjGroup": tmnxLdpObsoletedNotifyObjGroup,
       "tmnxLdpObsoletedNtfnV13v0Group": tmnxLdpObsoletedNtfnV13v0Group,
       "tmnxLdpNotificationV13v0Group": tmnxLdpNotificationV13v0Group,
       "tmnxLdpLocalLsrIdAdvertGroup": tmnxLdpLocalLsrIdAdvertGroup,
       "tmnxLdpLocalLsrIdCommunityGroup": tmnxLdpLocalLsrIdCommunityGroup,
       "tmnxLdpAggrEgrStatsV16v0Group": tmnxLdpAggrEgrStatsV16v0Group,
       "tmnxLdpPeerMcastTunnelingGroup": tmnxLdpPeerMcastTunnelingGroup,
       "tmnxLdpObjs": tmnxLdpObjs,
       "vRtrLdpGeneralTable": vRtrLdpGeneralTable,
       "vRtrLdpGeneralEntry": vRtrLdpGeneralEntry,
       "vRtrLdpGenLastChange": vRtrLdpGenLastChange,
       "vRtrLdpGenAdminState": vRtrLdpGenAdminState,
       "vRtrLdpGenOperState": vRtrLdpGenOperState,
       "vRtrLdpGenLdpLsrId": vRtrLdpGenLdpLsrId,
       "vRtrLdpGenProtocolVersion": vRtrLdpGenProtocolVersion,
       "vRtrLdpGenDeaggregateFec": vRtrLdpGenDeaggregateFec,
       "vRtrLdpGenKeepAliveFactor": vRtrLdpGenKeepAliveFactor,
       "vRtrLdpGenKeepAliveTimeout": vRtrLdpGenKeepAliveTimeout,
       "vRtrLdpGenHelloFactor": vRtrLdpGenHelloFactor,
       "vRtrLdpGenHelloTimeout": vRtrLdpGenHelloTimeout,
       "vRtrLdpGenRoutePreference": vRtrLdpGenRoutePreference,
       "vRtrLdpGenControlMode": vRtrLdpGenControlMode,
       "vRtrLdpGenDistMethod": vRtrLdpGenDistMethod,
       "vRtrLdpGenRetentionMode": vRtrLdpGenRetentionMode,
       "vRtrLdpGenTransportAddrType": vRtrLdpGenTransportAddrType,
       "vRtrLdpGenPropagatePolicy": vRtrLdpGenPropagatePolicy,
       "vRtrLdpGenLoopDetectCapable": vRtrLdpGenLoopDetectCapable,
       "vRtrLdpGenHopLimit": vRtrLdpGenHopLimit,
       "vRtrLdpGenPathVectorLimit": vRtrLdpGenPathVectorLimit,
       "vRtrLdpGenBackoffTime": vRtrLdpGenBackoffTime,
       "vRtrLdpGenMaxBackoffTime": vRtrLdpGenMaxBackoffTime,
       "vRtrLdpGenTargKeepAliveFactor": vRtrLdpGenTargKeepAliveFactor,
       "vRtrLdpGenTargKeepAliveTimeout": vRtrLdpGenTargKeepAliveTimeout,
       "vRtrLdpGenTargHelloFactor": vRtrLdpGenTargHelloFactor,
       "vRtrLdpGenTargHelloTimeout": vRtrLdpGenTargHelloTimeout,
       "vRtrLdpGenTargPassiveMode": vRtrLdpGenTargPassiveMode,
       "vRtrLdpGenTargetedSessions": vRtrLdpGenTargetedSessions,
       "vRtrLdpGenCreateTime": vRtrLdpGenCreateTime,
       "vRtrLdpGenUpTime": vRtrLdpGenUpTime,
       "vRtrLdpGenImportPolicy1": vRtrLdpGenImportPolicy1,
       "vRtrLdpGenImportPolicy2": vRtrLdpGenImportPolicy2,
       "vRtrLdpGenImportPolicy3": vRtrLdpGenImportPolicy3,
       "vRtrLdpGenImportPolicy4": vRtrLdpGenImportPolicy4,
       "vRtrLdpGenImportPolicy5": vRtrLdpGenImportPolicy5,
       "vRtrLdpGenExportPolicy1": vRtrLdpGenExportPolicy1,
       "vRtrLdpGenExportPolicy2": vRtrLdpGenExportPolicy2,
       "vRtrLdpGenExportPolicy3": vRtrLdpGenExportPolicy3,
       "vRtrLdpGenExportPolicy4": vRtrLdpGenExportPolicy4,
       "vRtrLdpGenExportPolicy5": vRtrLdpGenExportPolicy5,
       "vRtrLdpGenTunnelDownDampTime": vRtrLdpGenTunnelDownDampTime,
       "vRtrLdpGenOperDownReason": vRtrLdpGenOperDownReason,
       "vRtrLdpGenTrustList": vRtrLdpGenTrustList,
       "vRtrLdpGenGracefulRestart": vRtrLdpGenGracefulRestart,
       "vRtrLdpGenGRNbrLiveTime": vRtrLdpGenGRNbrLiveTime,
       "vRtrLdpGenGRMaxRecoveryTime": vRtrLdpGenGRMaxRecoveryTime,
       "vRtrLdpGenLabelWithdrawalDelay": vRtrLdpGenLabelWithdrawalDelay,
       "vRtrLdpGenImplicitNull": vRtrLdpGenImplicitNull,
       "vRtrLdpGenShortTTLPropLocal": vRtrLdpGenShortTTLPropLocal,
       "vRtrLdpGenShortTTLPropTransit": vRtrLdpGenShortTTLPropTransit,
       "vRtrLdpGenMPMBBTime": vRtrLdpGenMPMBBTime,
       "vRtrLdpGenTunlTblExportPolicy1": vRtrLdpGenTunlTblExportPolicy1,
       "vRtrLdpGenTunlTblExportPolicy2": vRtrLdpGenTunlTblExportPolicy2,
       "vRtrLdpGenTunlTblExportPolicy3": vRtrLdpGenTunlTblExportPolicy3,
       "vRtrLdpGenTunlTblExportPolicy4": vRtrLdpGenTunlTblExportPolicy4,
       "vRtrLdpGenTunlTblExportPolicy5": vRtrLdpGenTunlTblExportPolicy5,
       "vRtrLdpGenP2MPCapability": vRtrLdpGenP2MPCapability,
       "vRtrLdpGenMPMBBCapability": vRtrLdpGenMPMBBCapability,
       "vRtrLdpGenDynamicCapability": vRtrLdpGenDynamicCapability,
       "vRtrLdpGenLdpFrr": vRtrLdpGenLdpFrr,
       "vRtrLdpGenTargHelloReduction": vRtrLdpGenTargHelloReduction,
       "vRtrLdpGenTargHelloReductionFctr": vRtrLdpGenTargHelloReductionFctr,
       "vRtrLdpGenMcastUpstreamFrr": vRtrLdpGenMcastUpstreamFrr,
       "vRtrLdpGenOverloadCapability": vRtrLdpGenOverloadCapability,
       "vRtrLdpStatsTable": vRtrLdpStatsTable,
       "vRtrLdpStatsEntry": vRtrLdpStatsEntry,
       "vRtrLdpStatsOperDownEvents": vRtrLdpStatsOperDownEvents,
       "vRtrLdpStatsActiveSessions": vRtrLdpStatsActiveSessions,
       "vRtrLdpStatsActiveAdjacencies": vRtrLdpStatsActiveAdjacencies,
       "vRtrLdpStatsActiveInterfaces": vRtrLdpStatsActiveInterfaces,
       "vRtrLdpStatsInactiveInterfaces": vRtrLdpStatsInactiveInterfaces,
       "vRtrLdpStatsActiveTargSessions": vRtrLdpStatsActiveTargSessions,
       "vRtrLdpStatsInactiveTargSessions": vRtrLdpStatsInactiveTargSessions,
       "vRtrLdpStatsAddrFECRecv": vRtrLdpStatsAddrFECRecv,
       "vRtrLdpStatsAddrFECSent": vRtrLdpStatsAddrFECSent,
       "vRtrLdpStatsSvcFECRecv": vRtrLdpStatsSvcFECRecv,
       "vRtrLdpStatsSvcFECSent": vRtrLdpStatsSvcFECSent,
       "vRtrLdpStatsAttemptedSessions": vRtrLdpStatsAttemptedSessions,
       "vRtrLdpStatsSessRejNoHelloErrors": vRtrLdpStatsSessRejNoHelloErrors,
       "vRtrLdpStatsSessRejAdvErrors": vRtrLdpStatsSessRejAdvErrors,
       "vRtrLdpStatsSessRejMaxPduErrors": vRtrLdpStatsSessRejMaxPduErrors,
       "vRtrLdpStatsSessRejLabelRangeErrors": vRtrLdpStatsSessRejLabelRangeErrors,
       "vRtrLdpStatsBadLdpIdentifierErrors": vRtrLdpStatsBadLdpIdentifierErrors,
       "vRtrLdpStatsBadPduLengthErrors": vRtrLdpStatsBadPduLengthErrors,
       "vRtrLdpStatsBadMessageLengthErrors": vRtrLdpStatsBadMessageLengthErrors,
       "vRtrLdpStatsBadTlvLengthErrors": vRtrLdpStatsBadTlvLengthErrors,
       "vRtrLdpStatsMalformedTlvValueErrors": vRtrLdpStatsMalformedTlvValueErrors,
       "vRtrLdpStatsKeepAliveExpiredErrors": vRtrLdpStatsKeepAliveExpiredErrors,
       "vRtrLdpStatsShutdownNotifRecv": vRtrLdpStatsShutdownNotifRecv,
       "vRtrLdpStatsShutdownNotifSent": vRtrLdpStatsShutdownNotifSent,
       "vRtrLdpStatsEgrFecPfxCount": vRtrLdpStatsEgrFecPfxCount,
       "vRtrLdpStatsUnknownTlvErrors": vRtrLdpStatsUnknownTlvErrors,
       "vRtrLdpStatsP2MPFECSent": vRtrLdpStatsP2MPFECSent,
       "vRtrLdpStatsP2MPFECRecv": vRtrLdpStatsP2MPFECRecv,
       "vRtrLdpPolicyTable": vRtrLdpPolicyTable,
       "vRtrLdpPolicyEntry": vRtrLdpPolicyEntry,
       "vRtrLdpPolicyType": vRtrLdpPolicyType,
       "vRtrLdpPolicyIndex": vRtrLdpPolicyIndex,
       "vRtrLdpPolicyRowStatus": vRtrLdpPolicyRowStatus,
       "vRtrLdpPolicyName": vRtrLdpPolicyName,
       "vRtrLdpIfTableSpinlock": vRtrLdpIfTableSpinlock,
       "vRtrLdpIfTable": vRtrLdpIfTable,
       "vRtrLdpIfEntry": vRtrLdpIfEntry,
       "vRtrLdpIfIndex": vRtrLdpIfIndex,
       "vRtrLdpPeerAddress": vRtrLdpPeerAddress,
       "vRtrLdpIfRowStatus": vRtrLdpIfRowStatus,
       "vRtrLdpIfLastChange": vRtrLdpIfLastChange,
       "vRtrLdpIfAdminState": vRtrLdpIfAdminState,
       "vRtrLdpIfOperState": vRtrLdpIfOperState,
       "vRtrLdpIfInheritance": vRtrLdpIfInheritance,
       "vRtrLdpIfKeepAliveFactor": vRtrLdpIfKeepAliveFactor,
       "vRtrLdpIfKeepAliveTimeout": vRtrLdpIfKeepAliveTimeout,
       "vRtrLdpIfHelloFactor": vRtrLdpIfHelloFactor,
       "vRtrLdpIfHelloTimeout": vRtrLdpIfHelloTimeout,
       "vRtrLdpIfBackoffTime": vRtrLdpIfBackoffTime,
       "vRtrLdpIfMaxBackoffTime": vRtrLdpIfMaxBackoffTime,
       "vRtrLdpIfTransportAddrType": vRtrLdpIfTransportAddrType,
       "vRtrLdpIfPassiveMode": vRtrLdpIfPassiveMode,
       "vRtrLdpIfAutoCreate": vRtrLdpIfAutoCreate,
       "vRtrLdpIfOperDownReason": vRtrLdpIfOperDownReason,
       "vRtrLdpIfTunneling": vRtrLdpIfTunneling,
       "vRtrLdpIfBfdEnabled": vRtrLdpIfBfdEnabled,
       "vRtrLdpIfLinkLsrIfType": vRtrLdpIfLinkLsrIfType,
       "vRtrLdpIfTargLsrIfIndex": vRtrLdpIfTargLsrIfIndex,
       "vRtrLdpIfMulticast": vRtrLdpIfMulticast,
       "vRtrLdpIfHelloReduction": vRtrLdpIfHelloReduction,
       "vRtrLdpIfHelloReductionFactor": vRtrLdpIfHelloReductionFactor,
       "vRtrLdpIfOperHelloTimeout": vRtrLdpIfOperHelloTimeout,
       "vRtrLdpIfLinkLsrIfIndex": vRtrLdpIfLinkLsrIfIndex,
       "vRtrLdpIfCreator": vRtrLdpIfCreator,
       "vRtrLdpIfTemplName": vRtrLdpIfTemplName,
       "vRtrLdpIfUpTime": vRtrLdpIfUpTime,
       "vRtrLdpIfStatsTable": vRtrLdpIfStatsTable,
       "vRtrLdpIfStatsEntry": vRtrLdpIfStatsEntry,
       "vRtrLdpIfExistingAdjacencies": vRtrLdpIfExistingAdjacencies,
       "vRtrLdpHelloAdjTable": vRtrLdpHelloAdjTable,
       "vRtrLdpHelloAdjEntry": vRtrLdpHelloAdjEntry,
       "vRtrLdpPeerLdpId": vRtrLdpPeerLdpId,
       "vRtrLdpHelloAdjLocalLdpId": vRtrLdpHelloAdjLocalLdpId,
       "vRtrLdpHelloAdjEntityIndex": vRtrLdpHelloAdjEntityIndex,
       "vRtrLdpHelloAdjIndex": vRtrLdpHelloAdjIndex,
       "vRtrLdpHelloAdjHoldTimeRemaining": vRtrLdpHelloAdjHoldTimeRemaining,
       "vRtrLdpHelloAdjType": vRtrLdpHelloAdjType,
       "vRtrLdpHelloAdjRemoteConfSeqNum": vRtrLdpHelloAdjRemoteConfSeqNum,
       "vRtrLdpHelloAdjRemoteIpAddress": vRtrLdpHelloAdjRemoteIpAddress,
       "vRtrLdpHelloAdjUpTime": vRtrLdpHelloAdjUpTime,
       "vRtrLdpHelloAdjLocalConfSeqNum": vRtrLdpHelloAdjLocalConfSeqNum,
       "vRtrLdpHelloAdjLocalIpAddress": vRtrLdpHelloAdjLocalIpAddress,
       "vRtrLdpHelloAdjInHelloMsgCount": vRtrLdpHelloAdjInHelloMsgCount,
       "vRtrLdpHelloAdjOutHelloMsgCount": vRtrLdpHelloAdjOutHelloMsgCount,
       "vRtrLdpHelloAdjLocalHelloTimeout": vRtrLdpHelloAdjLocalHelloTimeout,
       "vRtrLdpHelloAdjRemoteHelloTimeout": vRtrLdpHelloAdjRemoteHelloTimeout,
       "vRtrLdpHelloAdjBfdStatus": vRtrLdpHelloAdjBfdStatus,
       "vRtrLdpHelloAdjMapTable": vRtrLdpHelloAdjMapTable,
       "vRtrLdpHelloAdjMapEntry": vRtrLdpHelloAdjMapEntry,
       "vRtrLdpHelloAdjMapLdpId": vRtrLdpHelloAdjMapLdpId,
       "vRtrLdpSessionTable": vRtrLdpSessionTable,
       "vRtrLdpSessionEntry": vRtrLdpSessionEntry,
       "vRtrLdpSessLocalLdpId": vRtrLdpSessLocalLdpId,
       "vRtrLdpSessEntityIndex": vRtrLdpSessEntityIndex,
       "vRtrLdpSessLabelDistMethod": vRtrLdpSessLabelDistMethod,
       "vRtrLdpSessLoopDetectForPV": vRtrLdpSessLoopDetectForPV,
       "vRtrLdpSessPathVectorLimit": vRtrLdpSessPathVectorLimit,
       "vRtrLdpSessState": vRtrLdpSessState,
       "vRtrLdpSessAdjacencyType": vRtrLdpSessAdjacencyType,
       "vRtrLdpSessProtocolVersion": vRtrLdpSessProtocolVersion,
       "vRtrLdpSessLocalUdpPort": vRtrLdpSessLocalUdpPort,
       "vRtrLdpSessPeerUdpPort": vRtrLdpSessPeerUdpPort,
       "vRtrLdpSessLocalTcpPort": vRtrLdpSessLocalTcpPort,
       "vRtrLdpSessPeerTcpPort": vRtrLdpSessPeerTcpPort,
       "vRtrLdpSessLocalAddress": vRtrLdpSessLocalAddress,
       "vRtrLdpSessPeerAddress": vRtrLdpSessPeerAddress,
       "vRtrLdpSessKAHoldTimeRemaining": vRtrLdpSessKAHoldTimeRemaining,
       "vRtrLdpSessMaxPduLength": vRtrLdpSessMaxPduLength,
       "vRtrLdpSessUpTime": vRtrLdpSessUpTime,
       "vRtrLdpSessLocalKATimeout": vRtrLdpSessLocalKATimeout,
       "vRtrLdpSessPeerKATimeout": vRtrLdpSessPeerKATimeout,
       "vRtrLdpSessAdvertise": vRtrLdpSessAdvertise,
       "vRtrLdpSessRestartHelperState": vRtrLdpSessRestartHelperState,
       "vRtrLdpSessPeerNumRestart": vRtrLdpSessPeerNumRestart,
       "vRtrLdpSessLastRestartTime": vRtrLdpSessLastRestartTime,
       "vRtrLdpSessFtReconnectTimeNego": vRtrLdpSessFtReconnectTimeNego,
       "vRtrLdpSessFtRecoveryTimeNego": vRtrLdpSessFtRecoveryTimeNego,
       "vRtrLdpSessFtReconTimeRemaining": vRtrLdpSessFtReconTimeRemaining,
       "vRtrLdpSessFtRecovTimeRemaining": vRtrLdpSessFtRecovTimeRemaining,
       "vRtrLdpSessBfdStatus": vRtrLdpSessBfdStatus,
       "vRtrLdpSessP2MPCapabilityNego": vRtrLdpSessP2MPCapabilityNego,
       "vRtrLdpSessMPMBBCapabilityNego": vRtrLdpSessMPMBBCapabilityNego,
       "vRtrLdpSessDynamicCapabilityNego": vRtrLdpSessDynamicCapabilityNego,
       "vRtrLdpSessOvrloadCapabltyNego": vRtrLdpSessOvrloadCapabltyNego,
       "vRtrLdpSessAddrFecOverloadSent": vRtrLdpSessAddrFecOverloadSent,
       "vRtrLdpSessAddrFecOverloadRecv": vRtrLdpSessAddrFecOverloadRecv,
       "vRtrLdpSessMcastFecOverloadSent": vRtrLdpSessMcastFecOverloadSent,
       "vRtrLdpSessMcastFecOverloadRecv": vRtrLdpSessMcastFecOverloadRecv,
       "vRtrLdpSessServFecOverloadSent": vRtrLdpSessServFecOverloadSent,
       "vRtrLdpSessServFecOverloadRecv": vRtrLdpSessServFecOverloadRecv,
       "vRtrLdpSessOperMaxFecThreshold": vRtrLdpSessOperMaxFecThreshold,
       "vRtrLdpSessionStatsTable": vRtrLdpSessionStatsTable,
       "vRtrLdpSessionStatsEntry": vRtrLdpSessionStatsEntry,
       "vRtrLdpSessStatsTargAdj": vRtrLdpSessStatsTargAdj,
       "vRtrLdpSessStatsLinkAdj": vRtrLdpSessStatsLinkAdj,
       "vRtrLdpSessStatsFECRecv": vRtrLdpSessStatsFECRecv,
       "vRtrLdpSessStatsFECSent": vRtrLdpSessStatsFECSent,
       "vRtrLdpSessStatsHelloIn": vRtrLdpSessStatsHelloIn,
       "vRtrLdpSessStatsHelloOut": vRtrLdpSessStatsHelloOut,
       "vRtrLdpSessStatsKeepaliveIn": vRtrLdpSessStatsKeepaliveIn,
       "vRtrLdpSessStatsKeepaliveOut": vRtrLdpSessStatsKeepaliveOut,
       "vRtrLdpSessStatsInitIn": vRtrLdpSessStatsInitIn,
       "vRtrLdpSessStatsInitOut": vRtrLdpSessStatsInitOut,
       "vRtrLdpSessStatsLabelMappingIn": vRtrLdpSessStatsLabelMappingIn,
       "vRtrLdpSessStatsLabelMappingOut": vRtrLdpSessStatsLabelMappingOut,
       "vRtrLdpSessStatsLabelRequestIn": vRtrLdpSessStatsLabelRequestIn,
       "vRtrLdpSessStatsLabelRequestOut": vRtrLdpSessStatsLabelRequestOut,
       "vRtrLdpSessStatsLabelReleaseIn": vRtrLdpSessStatsLabelReleaseIn,
       "vRtrLdpSessStatsLabelReleaseOut": vRtrLdpSessStatsLabelReleaseOut,
       "vRtrLdpSessStatsLabelWithdrawIn": vRtrLdpSessStatsLabelWithdrawIn,
       "vRtrLdpSessStatsLabelWithdrawOut": vRtrLdpSessStatsLabelWithdrawOut,
       "vRtrLdpSessStatsLabelAbortIn": vRtrLdpSessStatsLabelAbortIn,
       "vRtrLdpSessStatsLabelAbortOut": vRtrLdpSessStatsLabelAbortOut,
       "vRtrLdpSessStatsAddrIn": vRtrLdpSessStatsAddrIn,
       "vRtrLdpSessStatsAddrOut": vRtrLdpSessStatsAddrOut,
       "vRtrLdpSessStatsAddrWithdrawIn": vRtrLdpSessStatsAddrWithdrawIn,
       "vRtrLdpSessStatsAddrWithdrawOut": vRtrLdpSessStatsAddrWithdrawOut,
       "vRtrLdpSessStatsNotificationIn": vRtrLdpSessStatsNotificationIn,
       "vRtrLdpSessStatsNotificationOut": vRtrLdpSessStatsNotificationOut,
       "vRtrLdpSessStatsAddrRecv": vRtrLdpSessStatsAddrRecv,
       "vRtrLdpSessStatsAddrSent": vRtrLdpSessStatsAddrSent,
       "vRtrLdpServFecTable": vRtrLdpServFecTable,
       "vRtrLdpServFecEntry": vRtrLdpServFecEntry,
       "vRtrLdpServFecFecType": vRtrLdpServFecFecType,
       "vRtrLdpServFecVcType": vRtrLdpServFecVcType,
       "vRtrLdpServFecVcId": vRtrLdpServFecVcId,
       "vRtrLdpServFecServType": vRtrLdpServFecServType,
       "vRtrLdpServFecServId": vRtrLdpServFecServId,
       "vRtrLdpServFecVpnId": vRtrLdpServFecVpnId,
       "vRtrLdpServFecFlags": vRtrLdpServFecFlags,
       "vRtrLdpServFecNumInLabels": vRtrLdpServFecNumInLabels,
       "vRtrLdpServFecNumOutLabels": vRtrLdpServFecNumOutLabels,
       "vRtrLdpServFecInLabel1": vRtrLdpServFecInLabel1,
       "vRtrLdpServFecInLabelStatus1": vRtrLdpServFecInLabelStatus1,
       "vRtrLdpServFecInLabel2": vRtrLdpServFecInLabel2,
       "vRtrLdpServFecInLabelStatus2": vRtrLdpServFecInLabelStatus2,
       "vRtrLdpServFecInLabel3": vRtrLdpServFecInLabel3,
       "vRtrLdpServFecInLabelStatus3": vRtrLdpServFecInLabelStatus3,
       "vRtrLdpServFecInLabel4": vRtrLdpServFecInLabel4,
       "vRtrLdpServFecInLabelStatus4": vRtrLdpServFecInLabelStatus4,
       "vRtrLdpServFecInLabel5": vRtrLdpServFecInLabel5,
       "vRtrLdpServFecInLabelStatus5": vRtrLdpServFecInLabelStatus5,
       "vRtrLdpServFecOutLabel1": vRtrLdpServFecOutLabel1,
       "vRtrLdpServFecOutLabelStatus1": vRtrLdpServFecOutLabelStatus1,
       "vRtrLdpServFecOutLabel2": vRtrLdpServFecOutLabel2,
       "vRtrLdpServFecOutLabelStatus2": vRtrLdpServFecOutLabelStatus2,
       "vRtrLdpServFecOutLabel3": vRtrLdpServFecOutLabel3,
       "vRtrLdpServFecOutLabelStatus3": vRtrLdpServFecOutLabelStatus3,
       "vRtrLdpServFecOutLabel4": vRtrLdpServFecOutLabel4,
       "vRtrLdpServFecOutLabelStatus4": vRtrLdpServFecOutLabelStatus4,
       "vRtrLdpServFecOutLabel5": vRtrLdpServFecOutLabel5,
       "vRtrLdpServFecOutLabelStatus5": vRtrLdpServFecOutLabelStatus5,
       "vRtrLdpServFecSdpId": vRtrLdpServFecSdpId,
       "vRtrLdpServFecLocalMTU": vRtrLdpServFecLocalMTU,
       "vRtrLdpServFecRemoteMTU": vRtrLdpServFecRemoteMTU,
       "vRtrLdpServFecLocalVlanTag": vRtrLdpServFecLocalVlanTag,
       "vRtrLdpServFecRemoteVlanTag": vRtrLdpServFecRemoteVlanTag,
       "vRtrLdpServFecLocalMaxCellConcat": vRtrLdpServFecLocalMaxCellConcat,
       "vRtrLdpServFecRemoteMaxCellConcat": vRtrLdpServFecRemoteMaxCellConcat,
       "vRtrLdpServFecInLabelSigStatus1": vRtrLdpServFecInLabelSigStatus1,
       "vRtrLdpServFecInLabelSigStatus2": vRtrLdpServFecInLabelSigStatus2,
       "vRtrLdpServFecInLabelSigStatus3": vRtrLdpServFecInLabelSigStatus3,
       "vRtrLdpServFecInLabelSigStatus4": vRtrLdpServFecInLabelSigStatus4,
       "vRtrLdpServFecInLabelSigStatus5": vRtrLdpServFecInLabelSigStatus5,
       "vRtrLdpServFecOutLabelSigStatus1": vRtrLdpServFecOutLabelSigStatus1,
       "vRtrLdpServFecOutLabelSigStatus2": vRtrLdpServFecOutLabelSigStatus2,
       "vRtrLdpServFecOutLabelSigStatus3": vRtrLdpServFecOutLabelSigStatus3,
       "vRtrLdpServFecOutLabelSigStatus4": vRtrLdpServFecOutLabelSigStatus4,
       "vRtrLdpServFecOutLabelSigStatus5": vRtrLdpServFecOutLabelSigStatus5,
       "vRtrLdpServFecMateEndpointVcId": vRtrLdpServFecMateEndpointVcId,
       "vRtrLdpServFecMateEndpointSdpId": vRtrLdpServFecMateEndpointSdpId,
       "vRtrLdpServFecLocalIpv4Capblty": vRtrLdpServFecLocalIpv4Capblty,
       "vRtrLdpServFecRemoteIpv4Capblty": vRtrLdpServFecRemoteIpv4Capblty,
       "vRtrLdpServFecLocalIpv6Capblty": vRtrLdpServFecLocalIpv6Capblty,
       "vRtrLdpServFecRemoteIpv6Capblty": vRtrLdpServFecRemoteIpv6Capblty,
       "vRtrLdpServFecLocalIpv4CeIpAddr": vRtrLdpServFecLocalIpv4CeIpAddr,
       "vRtrLdpServFecRemoteIpv4CeIpAddr": vRtrLdpServFecRemoteIpv4CeIpAddr,
       "vRtrLdpServFecInLbl1WdwReason": vRtrLdpServFecInLbl1WdwReason,
       "vRtrLdpServFecLocalFLTxCapblty": vRtrLdpServFecLocalFLTxCapblty,
       "vRtrLdpServFecLocalFLRxCapblty": vRtrLdpServFecLocalFLRxCapblty,
       "vRtrLdpServFecRemoteFLTxCapblty": vRtrLdpServFecRemoteFLTxCapblty,
       "vRtrLdpServFecRemoteFLRxCapblty": vRtrLdpServFecRemoteFLRxCapblty,
       "vRtrLdpServFecMapTable": vRtrLdpServFecMapTable,
       "vRtrLdpServFecMapEntry": vRtrLdpServFecMapEntry,
       "vRtrLdpServFecMapFecType": vRtrLdpServFecMapFecType,
       "vRtrLdpServFecMapVcType": vRtrLdpServFecMapVcType,
       "vRtrLdpServFecMapVcId": vRtrLdpServFecMapVcId,
       "vRtrLdpAddrFecTable": vRtrLdpAddrFecTable,
       "vRtrLdpAddrFecEntry": vRtrLdpAddrFecEntry,
       "vRtrLdpAddrFecFecType": vRtrLdpAddrFecFecType,
       "vRtrLdpAddrFecIpPrefix": vRtrLdpAddrFecIpPrefix,
       "vRtrLdpAddrFecIpMask": vRtrLdpAddrFecIpMask,
       "vRtrLdpAddrFecFlags": vRtrLdpAddrFecFlags,
       "vRtrLdpAddrFecNumInLabels": vRtrLdpAddrFecNumInLabels,
       "vRtrLdpAddrFecNumOutLabels": vRtrLdpAddrFecNumOutLabels,
       "vRtrLdpAddrFecInLabel1": vRtrLdpAddrFecInLabel1,
       "vRtrLdpAddrFecInLabelStatus1": vRtrLdpAddrFecInLabelStatus1,
       "vRtrLdpAddrFecInLabelIfIndex1": vRtrLdpAddrFecInLabelIfIndex1,
       "vRtrLdpAddrFecInLabel2": vRtrLdpAddrFecInLabel2,
       "vRtrLdpAddrFecInLabelStatus2": vRtrLdpAddrFecInLabelStatus2,
       "vRtrLdpAddrFecInLabelIfIndex2": vRtrLdpAddrFecInLabelIfIndex2,
       "vRtrLdpAddrFecInLabel3": vRtrLdpAddrFecInLabel3,
       "vRtrLdpAddrFecInLabelStatus3": vRtrLdpAddrFecInLabelStatus3,
       "vRtrLdpAddrFecInLabelIfIndex3": vRtrLdpAddrFecInLabelIfIndex3,
       "vRtrLdpAddrFecInLabel4": vRtrLdpAddrFecInLabel4,
       "vRtrLdpAddrFecInLabelStatus4": vRtrLdpAddrFecInLabelStatus4,
       "vRtrLdpAddrFecInLabelIfIndex4": vRtrLdpAddrFecInLabelIfIndex4,
       "vRtrLdpAddrFecInLabel5": vRtrLdpAddrFecInLabel5,
       "vRtrLdpAddrFecInLabelStatus5": vRtrLdpAddrFecInLabelStatus5,
       "vRtrLdpAddrFecInLabelIfIndex5": vRtrLdpAddrFecInLabelIfIndex5,
       "vRtrLdpAddrFecOutLabel1": vRtrLdpAddrFecOutLabel1,
       "vRtrLdpAddrFecOutLabelStatus1": vRtrLdpAddrFecOutLabelStatus1,
       "vRtrLdpAddrFecOutLabelIfIndex1": vRtrLdpAddrFecOutLabelIfIndex1,
       "vRtrLdpAddrFecOutLabelNextHop1": vRtrLdpAddrFecOutLabelNextHop1,
       "vRtrLdpAddrFecOutLabel2": vRtrLdpAddrFecOutLabel2,
       "vRtrLdpAddrFecOutLabelStatus2": vRtrLdpAddrFecOutLabelStatus2,
       "vRtrLdpAddrFecOutLabelIfIndex2": vRtrLdpAddrFecOutLabelIfIndex2,
       "vRtrLdpAddrFecOutLabelNextHop2": vRtrLdpAddrFecOutLabelNextHop2,
       "vRtrLdpAddrFecOutLabel3": vRtrLdpAddrFecOutLabel3,
       "vRtrLdpAddrFecOutLabelStatus3": vRtrLdpAddrFecOutLabelStatus3,
       "vRtrLdpAddrFecOutLabelIfIndex3": vRtrLdpAddrFecOutLabelIfIndex3,
       "vRtrLdpAddrFecOutLabelNextHop3": vRtrLdpAddrFecOutLabelNextHop3,
       "vRtrLdpAddrFecOutLabel4": vRtrLdpAddrFecOutLabel4,
       "vRtrLdpAddrFecOutLabelStatus4": vRtrLdpAddrFecOutLabelStatus4,
       "vRtrLdpAddrFecOutLabelIfIndex4": vRtrLdpAddrFecOutLabelIfIndex4,
       "vRtrLdpAddrFecOutLabelNextHop4": vRtrLdpAddrFecOutLabelNextHop4,
       "vRtrLdpAddrFecOutLabel5": vRtrLdpAddrFecOutLabel5,
       "vRtrLdpAddrFecOutLabelStatus5": vRtrLdpAddrFecOutLabelStatus5,
       "vRtrLdpAddrFecOutLabelIfIndex5": vRtrLdpAddrFecOutLabelIfIndex5,
       "vRtrLdpAddrFecOutLabelNextHop5": vRtrLdpAddrFecOutLabelNextHop5,
       "vRtrLdpAddrFecLspId": vRtrLdpAddrFecLspId,
       "vRtrLdpAddrFecLspId2": vRtrLdpAddrFecLspId2,
       "vRtrLdpAddrFecLspId3": vRtrLdpAddrFecLspId3,
       "vRtrLdpAddrFecLspId4": vRtrLdpAddrFecLspId4,
       "vRtrLdpAddrFecLspId5": vRtrLdpAddrFecLspId5,
       "vRtrLdpAddrFecMapTable": vRtrLdpAddrFecMapTable,
       "vRtrLdpAddrFecMapEntry": vRtrLdpAddrFecMapEntry,
       "vRtrLdpAddrFecMapFecType": vRtrLdpAddrFecMapFecType,
       "vRtrLdpAddrFecMapIpPrefix": vRtrLdpAddrFecMapIpPrefix,
       "vRtrLdpAddrFecMapIpMask": vRtrLdpAddrFecMapIpMask,
       "vRtrLdpAdjBackoffTable": vRtrLdpAdjBackoffTable,
       "vRtrLdpAdjBackoffEntry": vRtrLdpAdjBackoffEntry,
       "vRtrLdpAdjInitBackoff": vRtrLdpAdjInitBackoff,
       "vRtrLdpAdjMaxBackoff": vRtrLdpAdjMaxBackoff,
       "vRtrLdpAdjCurrentBackoff": vRtrLdpAdjCurrentBackoff,
       "vRtrLdpAdjWaitingTime": vRtrLdpAdjWaitingTime,
       "vRtrLdpAdjBackoffStatus": vRtrLdpAdjBackoffStatus,
       "vRtrLdpPeerParamsTable": vRtrLdpPeerParamsTable,
       "vRtrLdpPeerParamsEntry": vRtrLdpPeerParamsEntry,
       "vRtrLdpPeerRowStatus": vRtrLdpPeerRowStatus,
       "vRtrLdpPeerAuth": vRtrLdpPeerAuth,
       "vRtrLdpPeerAuthKey": vRtrLdpPeerAuthKey,
       "vRtrLdpPeerMinTTLValue": vRtrLdpPeerMinTTLValue,
       "vRtrLdpPeerTTLLogId": vRtrLdpPeerTTLLogId,
       "vRtrLdpPeerAuthKeyChain": vRtrLdpPeerAuthKeyChain,
       "vRtrLdpPeerDODLabelDistribution": vRtrLdpPeerDODLabelDistribution,
       "vRtrLdpPeerImportPolicy1": vRtrLdpPeerImportPolicy1,
       "vRtrLdpPeerImportPolicy2": vRtrLdpPeerImportPolicy2,
       "vRtrLdpPeerImportPolicy3": vRtrLdpPeerImportPolicy3,
       "vRtrLdpPeerImportPolicy4": vRtrLdpPeerImportPolicy4,
       "vRtrLdpPeerImportPolicy5": vRtrLdpPeerImportPolicy5,
       "vRtrLdpPeerExportPolicy1": vRtrLdpPeerExportPolicy1,
       "vRtrLdpPeerExportPolicy2": vRtrLdpPeerExportPolicy2,
       "vRtrLdpPeerExportPolicy3": vRtrLdpPeerExportPolicy3,
       "vRtrLdpPeerExportPolicy4": vRtrLdpPeerExportPolicy4,
       "vRtrLdpPeerExportPolicy5": vRtrLdpPeerExportPolicy5,
       "vRtrLdpPeerFec129CiscoInterop": vRtrLdpPeerFec129CiscoInterop,
       "vRtrLdpPeerPMTUDiscovery": vRtrLdpPeerPMTUDiscovery,
       "vRtrLdpPeerAdvAdjAddrOnly": vRtrLdpPeerAdvAdjAddrOnly,
       "vRtrLdpPeerPeIDMacFlushInterop": vRtrLdpPeerPeIDMacFlushInterop,
       "vRtrLdpPeerMaxFec": vRtrLdpPeerMaxFec,
       "vRtrLdpPeerMaxFecLogOnly": vRtrLdpPeerMaxFecLogOnly,
       "vRtrLdpPeerMaxFecThreshold": vRtrLdpPeerMaxFecThreshold,
       "tmnxLdpNotificationObjects": tmnxLdpNotificationObjects,
       "vRtrLdpInstanceNotifyReasonCode": vRtrLdpInstanceNotifyReasonCode,
       "vRtrLdpIfNotifyReasonCode": vRtrLdpIfNotifyReasonCode,
       "vRtrLdpNotifyLocalServiceID": vRtrLdpNotifyLocalServiceID,
       "vRtrLdpNotifyRemoteServiceID": vRtrLdpNotifyRemoteServiceID,
       "vRtrLdpNotifyLocalGroupID": vRtrLdpNotifyLocalGroupID,
       "vRtrLdpNotifyRemoteGroupID": vRtrLdpNotifyRemoteGroupID,
       "vRtrLdpSessOverloadState": vRtrLdpSessOverloadState,
       "vRtrLdpSessOverloadDirection": vRtrLdpSessOverloadDirection,
       "vRtrLdpSessOverloadFecType": vRtrLdpSessOverloadFecType,
       "vRtrLdpSessOperThresLevel": vRtrLdpSessOperThresLevel,
       "vRtrLdpStaticFecTable": vRtrLdpStaticFecTable,
       "vRtrLdpStaticFecEntry": vRtrLdpStaticFecEntry,
       "vRtrLdpStaticFecIpPrefix": vRtrLdpStaticFecIpPrefix,
       "vRtrLdpStaticFecIpMask": vRtrLdpStaticFecIpMask,
       "vRtrLdpStaticFecRowStatus": vRtrLdpStaticFecRowStatus,
       "vRtrLdpStaticFecNextNHIndex": vRtrLdpStaticFecNextNHIndex,
       "vRtrLdpStaticFecIngLabel": vRtrLdpStaticFecIngLabel,
       "vRtrLdpStaticFecNumNH": vRtrLdpStaticFecNumNH,
       "vRtrLdpStaticFecOperIngLabel": vRtrLdpStaticFecOperIngLabel,
       "vRtrLdpStaticFecNHTable": vRtrLdpStaticFecNHTable,
       "vRtrLdpStaticFecNHEntry": vRtrLdpStaticFecNHEntry,
       "vRtrLdpStaticFecNHIndex": vRtrLdpStaticFecNHIndex,
       "vRtrLdpStaticFecNHRowStatus": vRtrLdpStaticFecNHRowStatus,
       "vRtrLdpStaticFecNHType": vRtrLdpStaticFecNHType,
       "vRtrLdpStaticFecNHIpAddr": vRtrLdpStaticFecNHIpAddr,
       "vRtrLdpStaticFecNHEgrLabel": vRtrLdpStaticFecNHEgrLabel,
       "vRtrLdpStaticFecNHIfName": vRtrLdpStaticFecNHIfName,
       "vRtrLdpTargTable": vRtrLdpTargTable,
       "vRtrLdpTargEntry": vRtrLdpTargEntry,
       "vRtrLdpTargImportPolicy1": vRtrLdpTargImportPolicy1,
       "vRtrLdpTargImportPolicy2": vRtrLdpTargImportPolicy2,
       "vRtrLdpTargImportPolicy3": vRtrLdpTargImportPolicy3,
       "vRtrLdpTargImportPolicy4": vRtrLdpTargImportPolicy4,
       "vRtrLdpTargImportPolicy5": vRtrLdpTargImportPolicy5,
       "vRtrLdpTargExportPolicy1": vRtrLdpTargExportPolicy1,
       "vRtrLdpTargExportPolicy2": vRtrLdpTargExportPolicy2,
       "vRtrLdpTargExportPolicy3": vRtrLdpTargExportPolicy3,
       "vRtrLdpTargExportPolicy4": vRtrLdpTargExportPolicy4,
       "vRtrLdpTargExportPolicy5": vRtrLdpTargExportPolicy5,
       "vRtrLdpTargTunnelPreference": vRtrLdpTargTunnelPreference,
       "vRtrLdpIfTunnelingLspTable": vRtrLdpIfTunnelingLspTable,
       "vRtrLdpIfTunnelingLspEntry": vRtrLdpIfTunnelingLspEntry,
       "vRtrLdpIfLspId": vRtrLdpIfLspId,
       "vRtrLdpIfLspRowStatus": vRtrLdpIfLspRowStatus,
       "vRtrLdpCepTdmFecTable": vRtrLdpCepTdmFecTable,
       "vRtrLdpCepTdmFecEntry": vRtrLdpCepTdmFecEntry,
       "vRtrLdpCepTdmLocalPayloadSize": vRtrLdpCepTdmLocalPayloadSize,
       "vRtrLdpCepTdmRemotePayloadSize": vRtrLdpCepTdmRemotePayloadSize,
       "vRtrLdpCepTdmLocalBitrate": vRtrLdpCepTdmLocalBitrate,
       "vRtrLdpCepTdmRemoteBitrate": vRtrLdpCepTdmRemoteBitrate,
       "vRtrLdpCepTdmLocalRtpHeader": vRtrLdpCepTdmLocalRtpHeader,
       "vRtrLdpCepTdmRemoteRtpHeader": vRtrLdpCepTdmRemoteRtpHeader,
       "vRtrLdpCepTdmLocalDiffTimestamp": vRtrLdpCepTdmLocalDiffTimestamp,
       "vRtrLdpCepTdmRemoteDiffTimestamp": vRtrLdpCepTdmRemoteDiffTimestamp,
       "vRtrLdpCepTdmLocalSigPkts": vRtrLdpCepTdmLocalSigPkts,
       "vRtrLdpCepTdmRemoteSigPkts": vRtrLdpCepTdmRemoteSigPkts,
       "vRtrLdpCepTdmLocalCasTrunk": vRtrLdpCepTdmLocalCasTrunk,
       "vRtrLdpCepTdmRemoteCasTrunk": vRtrLdpCepTdmRemoteCasTrunk,
       "vRtrLdpCepTdmLocalTimestampFreq": vRtrLdpCepTdmLocalTimestampFreq,
       "vRtrLdpCepTdmRemoteTimestampFreq": vRtrLdpCepTdmRemoteTimestampFreq,
       "vRtrLdpCepTdmLocalPayloadType": vRtrLdpCepTdmLocalPayloadType,
       "vRtrLdpCepTdmRemotePayloadType": vRtrLdpCepTdmRemotePayloadType,
       "vRtrLdpCepTdmLocalSsrcId": vRtrLdpCepTdmLocalSsrcId,
       "vRtrLdpCepTdmRemoteSsrcId": vRtrLdpCepTdmRemoteSsrcId,
       "vLdpServFec129Table": vLdpServFec129Table,
       "vLdpServFec129Entry": vLdpServFec129Entry,
       "vLdpServFec129AgiTlv": vLdpServFec129AgiTlv,
       "vLdpServFec129SrcAiiTlv": vLdpServFec129SrcAiiTlv,
       "vLdpServFec129TgtAiiTlv": vLdpServFec129TgtAiiTlv,
       "vLdpServFec129ServType": vLdpServFec129ServType,
       "vLdpServFec129ServId": vLdpServFec129ServId,
       "vLdpServFec129VpnId": vLdpServFec129VpnId,
       "vLdpServFec129Flags": vLdpServFec129Flags,
       "vLdpServFec129NumInLabels": vLdpServFec129NumInLabels,
       "vLdpServFec129NumOutLabels": vLdpServFec129NumOutLabels,
       "vLdpServFec129InLabel1": vLdpServFec129InLabel1,
       "vLdpServFec129InLabelStatus1": vLdpServFec129InLabelStatus1,
       "vLdpServFec129OutLabel1": vLdpServFec129OutLabel1,
       "vLdpServFec129OutLabelStatus1": vLdpServFec129OutLabelStatus1,
       "vLdpServFec129SdpId": vLdpServFec129SdpId,
       "vLdpServFec129LocalMTU": vLdpServFec129LocalMTU,
       "vLdpServFec129RemoteMTU": vLdpServFec129RemoteMTU,
       "vLdpServFec129LocalVlanTag": vLdpServFec129LocalVlanTag,
       "vLdpServFec129RemoteVlanTag": vLdpServFec129RemoteVlanTag,
       "vLdpServFec129LocalMaxCellConcat": vLdpServFec129LocalMaxCellConcat,
       "vLdpServFec129RemoteMaxCellConcat": vLdpServFec129RemoteMaxCellConcat,
       "vLdpServFec129InLabelSigStatus1": vLdpServFec129InLabelSigStatus1,
       "vLdpServFec129OutLabelSigStatus1": vLdpServFec129OutLabelSigStatus1,
       "vLdpServFec129LocalIpv4Capblty": vLdpServFec129LocalIpv4Capblty,
       "vLdpServFec129RemoteIpv4Capblty": vLdpServFec129RemoteIpv4Capblty,
       "vLdpServFec129LocalIpv6Capblty": vLdpServFec129LocalIpv6Capblty,
       "vLdpServFec129RemoteIpv6Capblty": vLdpServFec129RemoteIpv6Capblty,
       "vLdpServFec129LocalIpv4CeIpAddr": vLdpServFec129LocalIpv4CeIpAddr,
       "vLdpServFec129RemoteIpv4CeIpAddr": vLdpServFec129RemoteIpv4CeIpAddr,
       "vLdpServFec129InLbl1WdwReason": vLdpServFec129InLbl1WdwReason,
       "vLdpServFec129LocalFLTxCapblty": vLdpServFec129LocalFLTxCapblty,
       "vLdpServFec129LocalFLRxCapblty": vLdpServFec129LocalFLRxCapblty,
       "vLdpServFec129RemoteFLTxCapblty": vLdpServFec129RemoteFLTxCapblty,
       "vLdpServFec129RemoteFLRxCapblty": vLdpServFec129RemoteFLRxCapblty,
       "vLdpServFec129MateAgiTlv": vLdpServFec129MateAgiTlv,
       "vLdpServFec129MateSrcAiiTlv": vLdpServFec129MateSrcAiiTlv,
       "vLdpServFec129MateTgtAiiTlv": vLdpServFec129MateTgtAiiTlv,
       "vLdpServFec129MateSdpId": vLdpServFec129MateSdpId,
       "vLdpServFec129MapTable": vLdpServFec129MapTable,
       "vLdpServFec129MapEntry": vLdpServFec129MapEntry,
       "vLdpServFec129MapVcType": vLdpServFec129MapVcType,
       "vLdpServFec129MapAgiTlv": vLdpServFec129MapAgiTlv,
       "vLdpServFec129MapSrcAiiTlv": vLdpServFec129MapSrcAiiTlv,
       "vLdpServFec129MapTgtAiiTlv": vLdpServFec129MapTgtAiiTlv,
       "vLdpCepTdmFec129Table": vLdpCepTdmFec129Table,
       "vLdpCepTdmFec129Entry": vLdpCepTdmFec129Entry,
       "vLdpCepTdmFec129LocalPayloadSize": vLdpCepTdmFec129LocalPayloadSize,
       "vLdpCepTdmFec129RemotePayloadSize": vLdpCepTdmFec129RemotePayloadSize,
       "vLdpCepTdmFec129LocalBitrate": vLdpCepTdmFec129LocalBitrate,
       "vLdpCepTdmFec129RemoteBitrate": vLdpCepTdmFec129RemoteBitrate,
       "vLdpCepTdmFec129LocalRtpHeader": vLdpCepTdmFec129LocalRtpHeader,
       "vLdpCepTdmFec129RemoteRtpHeader": vLdpCepTdmFec129RemoteRtpHeader,
       "vLdpCepTdmFec129LocalDiffTimestamp": vLdpCepTdmFec129LocalDiffTimestamp,
       "vLdpCepTdmFec129RemoteDiffTimestamp": vLdpCepTdmFec129RemoteDiffTimestamp,
       "vLdpCepTdmFec129LocalSigPkts": vLdpCepTdmFec129LocalSigPkts,
       "vLdpCepTdmFec129RemoteSigPkts": vLdpCepTdmFec129RemoteSigPkts,
       "vLdpCepTdmFec129LocalCasTrunk": vLdpCepTdmFec129LocalCasTrunk,
       "vLdpCepTdmFec129RemoteCasTrunk": vLdpCepTdmFec129RemoteCasTrunk,
       "vLdpCepTdmFec129LocalTimestampFreq": vLdpCepTdmFec129LocalTimestampFreq,
       "vLdpCepTdmFec129RemoteTimestampFreq": vLdpCepTdmFec129RemoteTimestampFreq,
       "vLdpCepTdmFec129LocalPayloadType": vLdpCepTdmFec129LocalPayloadType,
       "vLdpCepTdmFec129RemotePayloadType": vLdpCepTdmFec129RemotePayloadType,
       "vLdpCepTdmFec129LocalSsrcId": vLdpCepTdmFec129LocalSsrcId,
       "vLdpCepTdmFec129RemoteSsrcId": vLdpCepTdmFec129RemoteSsrcId,
       "vRtrLdpAggrPreMatchTable": vRtrLdpAggrPreMatchTable,
       "vRtrLdpAggrPreMatchEntry": vRtrLdpAggrPreMatchEntry,
       "vRtrLdpAggrPreMatchEnabled": vRtrLdpAggrPreMatchEnabled,
       "vRtrLdpAggrPreMatchPreExcPolicy1": vRtrLdpAggrPreMatchPreExcPolicy1,
       "vRtrLdpAggrPreMatchPreExcPolicy2": vRtrLdpAggrPreMatchPreExcPolicy2,
       "vRtrLdpAggrPreMatchPreExcPolicy3": vRtrLdpAggrPreMatchPreExcPolicy3,
       "vRtrLdpAggrPreMatchPreExcPolicy4": vRtrLdpAggrPreMatchPreExcPolicy4,
       "vRtrLdpAggrPreMatchPreExcPolicy5": vRtrLdpAggrPreMatchPreExcPolicy5,
       "vRtrLdpAggrPreMatchAdminState": vRtrLdpAggrPreMatchAdminState,
       "vRtrLdpEgrStatFecPfxTblLastChgd": vRtrLdpEgrStatFecPfxTblLastChgd,
       "vRtrLdpEgrStatFecPfxTable": vRtrLdpEgrStatFecPfxTable,
       "vRtrLdpEgrStatFecPfxEntry": vRtrLdpEgrStatFecPfxEntry,
       "vRtrLdpEgrStatFecPfxAddrType": vRtrLdpEgrStatFecPfxAddrType,
       "vRtrLdpEgrStatFecPfxAddr": vRtrLdpEgrStatFecPfxAddr,
       "vRtrLdpEgrStatFecPfxMaskLen": vRtrLdpEgrStatFecPfxMaskLen,
       "vRtrLdpEgrStatFecPfxRowStatus": vRtrLdpEgrStatFecPfxRowStatus,
       "vRtrLdpEgrStatFecPfxLastChgd": vRtrLdpEgrStatFecPfxLastChgd,
       "vRtrLdpEgrStatFecPfxCollStats": vRtrLdpEgrStatFecPfxCollStats,
       "vRtrLdpEgrStatFecPfxActgPol": vRtrLdpEgrStatFecPfxActgPol,
       "vRtrLdpEgrStatFecPfxAdminState": vRtrLdpEgrStatFecPfxAdminState,
       "vRtrLdpEgrStatisticsTable": vRtrLdpEgrStatisticsTable,
       "vRtrLdpEgrStatisticsEntry": vRtrLdpEgrStatisticsEntry,
       "vRtrLdpInProfilePktsFc0": vRtrLdpInProfilePktsFc0,
       "vRtrLdpInProfilePktsFc0Low32": vRtrLdpInProfilePktsFc0Low32,
       "vRtrLdpInProfilePktsFc0High32": vRtrLdpInProfilePktsFc0High32,
       "vRtrLdpInProfilePktsFc1": vRtrLdpInProfilePktsFc1,
       "vRtrLdpInProfilePktsFc1Low32": vRtrLdpInProfilePktsFc1Low32,
       "vRtrLdpInProfilePktsFc1High32": vRtrLdpInProfilePktsFc1High32,
       "vRtrLdpInProfilePktsFc2": vRtrLdpInProfilePktsFc2,
       "vRtrLdpInProfilePktsFc2Low32": vRtrLdpInProfilePktsFc2Low32,
       "vRtrLdpInProfilePktsFc2High32": vRtrLdpInProfilePktsFc2High32,
       "vRtrLdpInProfilePktsFc3": vRtrLdpInProfilePktsFc3,
       "vRtrLdpInProfilePktsFc3Low32": vRtrLdpInProfilePktsFc3Low32,
       "vRtrLdpInProfilePktsFc3High32": vRtrLdpInProfilePktsFc3High32,
       "vRtrLdpInProfilePktsFc4": vRtrLdpInProfilePktsFc4,
       "vRtrLdpInProfilePktsFc4Low32": vRtrLdpInProfilePktsFc4Low32,
       "vRtrLdpInProfilePktsFc4High32": vRtrLdpInProfilePktsFc4High32,
       "vRtrLdpInProfilePktsFc5": vRtrLdpInProfilePktsFc5,
       "vRtrLdpInProfilePktsFc5Low32": vRtrLdpInProfilePktsFc5Low32,
       "vRtrLdpInProfilePktsFc5High32": vRtrLdpInProfilePktsFc5High32,
       "vRtrLdpInProfilePktsFc6": vRtrLdpInProfilePktsFc6,
       "vRtrLdpInProfilePktsFc6Low32": vRtrLdpInProfilePktsFc6Low32,
       "vRtrLdpInProfilePktsFc6High32": vRtrLdpInProfilePktsFc6High32,
       "vRtrLdpInProfilePktsFc7": vRtrLdpInProfilePktsFc7,
       "vRtrLdpInProfilePktsFc7Low32": vRtrLdpInProfilePktsFc7Low32,
       "vRtrLdpInProfilePktsFc7High32": vRtrLdpInProfilePktsFc7High32,
       "vRtrLdpInProfileOctetsFc0": vRtrLdpInProfileOctetsFc0,
       "vRtrLdpInProfileOctetsFc0Low32": vRtrLdpInProfileOctetsFc0Low32,
       "vRtrLdpInProfileOctetsFc0High32": vRtrLdpInProfileOctetsFc0High32,
       "vRtrLdpInProfileOctetsFc1": vRtrLdpInProfileOctetsFc1,
       "vRtrLdpInProfileOctetsFc1Low32": vRtrLdpInProfileOctetsFc1Low32,
       "vRtrLdpInProfileOctetsFc1High32": vRtrLdpInProfileOctetsFc1High32,
       "vRtrLdpInProfileOctetsFc2": vRtrLdpInProfileOctetsFc2,
       "vRtrLdpInProfileOctetsFc2Low32": vRtrLdpInProfileOctetsFc2Low32,
       "vRtrLdpInProfileOctetsFc2High32": vRtrLdpInProfileOctetsFc2High32,
       "vRtrLdpInProfileOctetsFc3": vRtrLdpInProfileOctetsFc3,
       "vRtrLdpInProfileOctetsFc3Low32": vRtrLdpInProfileOctetsFc3Low32,
       "vRtrLdpInProfileOctetsFc3High32": vRtrLdpInProfileOctetsFc3High32,
       "vRtrLdpInProfileOctetsFc4": vRtrLdpInProfileOctetsFc4,
       "vRtrLdpInProfileOctetsFc4Low32": vRtrLdpInProfileOctetsFc4Low32,
       "vRtrLdpInProfileOctetsFc4High32": vRtrLdpInProfileOctetsFc4High32,
       "vRtrLdpInProfileOctetsFc5": vRtrLdpInProfileOctetsFc5,
       "vRtrLdpInProfileOctetsFc5Low32": vRtrLdpInProfileOctetsFc5Low32,
       "vRtrLdpInProfileOctetsFc5High32": vRtrLdpInProfileOctetsFc5High32,
       "vRtrLdpInProfileOctetsFc6": vRtrLdpInProfileOctetsFc6,
       "vRtrLdpInProfileOctetsFc6Low32": vRtrLdpInProfileOctetsFc6Low32,
       "vRtrLdpInProfileOctetsFc6High32": vRtrLdpInProfileOctetsFc6High32,
       "vRtrLdpInProfileOctetsFc7": vRtrLdpInProfileOctetsFc7,
       "vRtrLdpInProfileOctetsFc7Low32": vRtrLdpInProfileOctetsFc7Low32,
       "vRtrLdpInProfileOctetsFc7High32": vRtrLdpInProfileOctetsFc7High32,
       "vRtrLdpOutOfProfPktsFc0": vRtrLdpOutOfProfPktsFc0,
       "vRtrLdpOutOfProfPktsFc0Low32": vRtrLdpOutOfProfPktsFc0Low32,
       "vRtrLdpOutOfProfPktsFc0High32": vRtrLdpOutOfProfPktsFc0High32,
       "vRtrLdpOutOfProfPktsFc1": vRtrLdpOutOfProfPktsFc1,
       "vRtrLdpOutOfProfPktsFc1Low32": vRtrLdpOutOfProfPktsFc1Low32,
       "vRtrLdpOutOfProfPktsFc1High32": vRtrLdpOutOfProfPktsFc1High32,
       "vRtrLdpOutOfProfPktsFc2": vRtrLdpOutOfProfPktsFc2,
       "vRtrLdpOutOfProfPktsFc2Low32": vRtrLdpOutOfProfPktsFc2Low32,
       "vRtrLdpOutOfProfPktsFc2High32": vRtrLdpOutOfProfPktsFc2High32,
       "vRtrLdpOutOfProfPktsFc3": vRtrLdpOutOfProfPktsFc3,
       "vRtrLdpOutOfProfPktsFc3Low32": vRtrLdpOutOfProfPktsFc3Low32,
       "vRtrLdpOutOfProfPktsFc3High32": vRtrLdpOutOfProfPktsFc3High32,
       "vRtrLdpOutOfProfPktsFc4": vRtrLdpOutOfProfPktsFc4,
       "vRtrLdpOutOfProfPktsFc4Low32": vRtrLdpOutOfProfPktsFc4Low32,
       "vRtrLdpOutOfProfPktsFc4High32": vRtrLdpOutOfProfPktsFc4High32,
       "vRtrLdpOutOfProfPktsFc5": vRtrLdpOutOfProfPktsFc5,
       "vRtrLdpOutOfProfPktsFc5Low32": vRtrLdpOutOfProfPktsFc5Low32,
       "vRtrLdpOutOfProfPktsFc5High32": vRtrLdpOutOfProfPktsFc5High32,
       "vRtrLdpOutOfProfPktsFc6": vRtrLdpOutOfProfPktsFc6,
       "vRtrLdpOutOfProfPktsFc6Low32": vRtrLdpOutOfProfPktsFc6Low32,
       "vRtrLdpOutOfProfPktsFc6High32": vRtrLdpOutOfProfPktsFc6High32,
       "vRtrLdpOutOfProfPktsFc7": vRtrLdpOutOfProfPktsFc7,
       "vRtrLdpOutOfProfPktsFc7Low32": vRtrLdpOutOfProfPktsFc7Low32,
       "vRtrLdpOutOfProfPktsFc7High32": vRtrLdpOutOfProfPktsFc7High32,
       "vRtrLdpOutOfProfOctetsFc0": vRtrLdpOutOfProfOctetsFc0,
       "vRtrLdpOutOfProfOctetsFc0Low32": vRtrLdpOutOfProfOctetsFc0Low32,
       "vRtrLdpOutOfProfOctetsFc0High32": vRtrLdpOutOfProfOctetsFc0High32,
       "vRtrLdpOutOfProfOctetsFc1": vRtrLdpOutOfProfOctetsFc1,
       "vRtrLdpOutOfProfOctetsFc1Low32": vRtrLdpOutOfProfOctetsFc1Low32,
       "vRtrLdpOutOfProfOctetsFc1High32": vRtrLdpOutOfProfOctetsFc1High32,
       "vRtrLdpOutOfProfOctetsFc2": vRtrLdpOutOfProfOctetsFc2,
       "vRtrLdpOutOfProfOctetsFc2Low32": vRtrLdpOutOfProfOctetsFc2Low32,
       "vRtrLdpOutOfProfOctetsFc2High32": vRtrLdpOutOfProfOctetsFc2High32,
       "vRtrLdpOutOfProfOctetsFc3": vRtrLdpOutOfProfOctetsFc3,
       "vRtrLdpOutOfProfOctetsFc3Low32": vRtrLdpOutOfProfOctetsFc3Low32,
       "vRtrLdpOutOfProfOctetsFc3High32": vRtrLdpOutOfProfOctetsFc3High32,
       "vRtrLdpOutOfProfOctetsFc4": vRtrLdpOutOfProfOctetsFc4,
       "vRtrLdpOutOfProfOctetsFc4Low32": vRtrLdpOutOfProfOctetsFc4Low32,
       "vRtrLdpOutOfProfOctetsFc4High32": vRtrLdpOutOfProfOctetsFc4High32,
       "vRtrLdpOutOfProfOctetsFc5": vRtrLdpOutOfProfOctetsFc5,
       "vRtrLdpOutOfProfOctetsFc5Low32": vRtrLdpOutOfProfOctetsFc5Low32,
       "vRtrLdpOutOfProfOctetsFc5High32": vRtrLdpOutOfProfOctetsFc5High32,
       "vRtrLdpOutOfProfOctetsFc6": vRtrLdpOutOfProfOctetsFc6,
       "vRtrLdpOutOfProfOctetsFc6Low32": vRtrLdpOutOfProfOctetsFc6Low32,
       "vRtrLdpOutOfProfOctetsFc6High32": vRtrLdpOutOfProfOctetsFc6High32,
       "vRtrLdpOutOfProfOctetsFc7": vRtrLdpOutOfProfOctetsFc7,
       "vRtrLdpOutOfProfOctetsFc7Low32": vRtrLdpOutOfProfOctetsFc7Low32,
       "vRtrLdpOutOfProfOctetsFc7High32": vRtrLdpOutOfProfOctetsFc7High32,
       "vRtrLdpAggregatePkts": vRtrLdpAggregatePkts,
       "vRtrLdpAggregatePktsLow32": vRtrLdpAggregatePktsLow32,
       "vRtrLdpAggregatePktsHigh32": vRtrLdpAggregatePktsHigh32,
       "vRtrLdpAggregateOctets": vRtrLdpAggregateOctets,
       "vRtrLdpAggregateOctetsLow32": vRtrLdpAggregateOctetsLow32,
       "vRtrLdpAggregateOctetsHigh32": vRtrLdpAggregateOctetsHigh32,
       "vRtrLdpAddrFecExtTable": vRtrLdpAddrFecExtTable,
       "vRtrLdpAddrFecExtEntry": vRtrLdpAddrFecExtEntry,
       "vRtrLdpAddrFecOutLbl6": vRtrLdpAddrFecOutLbl6,
       "vRtrLdpAddrFecOutLblStatus6": vRtrLdpAddrFecOutLblStatus6,
       "vRtrLdpAddrFecOutLblIfIndex6": vRtrLdpAddrFecOutLblIfIndex6,
       "vRtrLdpAddrFecOutLblNxtHopType6": vRtrLdpAddrFecOutLblNxtHopType6,
       "vRtrLdpAddrFecOutLblNxtHopAddr6": vRtrLdpAddrFecOutLblNxtHopAddr6,
       "vRtrLdpAddrFecLspId6": vRtrLdpAddrFecLspId6,
       "vRtrLdpAddrFecOutLbl7": vRtrLdpAddrFecOutLbl7,
       "vRtrLdpAddrFecOutLblStatus7": vRtrLdpAddrFecOutLblStatus7,
       "vRtrLdpAddrFecOutLblIfIndex7": vRtrLdpAddrFecOutLblIfIndex7,
       "vRtrLdpAddrFecOutLblNxtHopType7": vRtrLdpAddrFecOutLblNxtHopType7,
       "vRtrLdpAddrFecOutLblNxtHopAddr7": vRtrLdpAddrFecOutLblNxtHopAddr7,
       "vRtrLdpAddrFecLspId7": vRtrLdpAddrFecLspId7,
       "vRtrLdpAddrFecOutLbl8": vRtrLdpAddrFecOutLbl8,
       "vRtrLdpAddrFecOutLblStatus8": vRtrLdpAddrFecOutLblStatus8,
       "vRtrLdpAddrFecOutLblIfIndex8": vRtrLdpAddrFecOutLblIfIndex8,
       "vRtrLdpAddrFecOutLblNxtHopType8": vRtrLdpAddrFecOutLblNxtHopType8,
       "vRtrLdpAddrFecOutLblNxtHopAddr8": vRtrLdpAddrFecOutLblNxtHopAddr8,
       "vRtrLdpAddrFecLspId8": vRtrLdpAddrFecLspId8,
       "vRtrLdpAddrFecOutLbl9": vRtrLdpAddrFecOutLbl9,
       "vRtrLdpAddrFecOutLblStatus9": vRtrLdpAddrFecOutLblStatus9,
       "vRtrLdpAddrFecOutLblIfIndex9": vRtrLdpAddrFecOutLblIfIndex9,
       "vRtrLdpAddrFecOutLblNxtHopType9": vRtrLdpAddrFecOutLblNxtHopType9,
       "vRtrLdpAddrFecOutLblNxtHopAddr9": vRtrLdpAddrFecOutLblNxtHopAddr9,
       "vRtrLdpAddrFecLspId9": vRtrLdpAddrFecLspId9,
       "vRtrLdpAddrFecOutLbl10": vRtrLdpAddrFecOutLbl10,
       "vRtrLdpAddrFecOutLblStatus10": vRtrLdpAddrFecOutLblStatus10,
       "vRtrLdpAddrFecOutLblIfIndex10": vRtrLdpAddrFecOutLblIfIndex10,
       "vRtrLdpAddrFecOutLblNxtHopType10": vRtrLdpAddrFecOutLblNxtHopType10,
       "vRtrLdpAddrFecOutLblNxtHopAddr10": vRtrLdpAddrFecOutLblNxtHopAddr10,
       "vRtrLdpAddrFecLspId10": vRtrLdpAddrFecLspId10,
       "vRtrLdpAddrFecOutLbl11": vRtrLdpAddrFecOutLbl11,
       "vRtrLdpAddrFecOutLblStatus11": vRtrLdpAddrFecOutLblStatus11,
       "vRtrLdpAddrFecOutLblIfIndex11": vRtrLdpAddrFecOutLblIfIndex11,
       "vRtrLdpAddrFecOutLblNxtHopType11": vRtrLdpAddrFecOutLblNxtHopType11,
       "vRtrLdpAddrFecOutLblNxtHopAddr11": vRtrLdpAddrFecOutLblNxtHopAddr11,
       "vRtrLdpAddrFecLspId11": vRtrLdpAddrFecLspId11,
       "vRtrLdpAddrFecOutLbl12": vRtrLdpAddrFecOutLbl12,
       "vRtrLdpAddrFecOutLblStatus12": vRtrLdpAddrFecOutLblStatus12,
       "vRtrLdpAddrFecOutLblIfIndex12": vRtrLdpAddrFecOutLblIfIndex12,
       "vRtrLdpAddrFecOutLblNxtHopType12": vRtrLdpAddrFecOutLblNxtHopType12,
       "vRtrLdpAddrFecOutLblNxtHopAddr12": vRtrLdpAddrFecOutLblNxtHopAddr12,
       "vRtrLdpAddrFecLspId12": vRtrLdpAddrFecLspId12,
       "vRtrLdpAddrFecOutLbl13": vRtrLdpAddrFecOutLbl13,
       "vRtrLdpAddrFecOutLblStatus13": vRtrLdpAddrFecOutLblStatus13,
       "vRtrLdpAddrFecOutLblIfIndex13": vRtrLdpAddrFecOutLblIfIndex13,
       "vRtrLdpAddrFecOutLblNxtHopType13": vRtrLdpAddrFecOutLblNxtHopType13,
       "vRtrLdpAddrFecOutLblNxtHopAddr13": vRtrLdpAddrFecOutLblNxtHopAddr13,
       "vRtrLdpAddrFecLspId13": vRtrLdpAddrFecLspId13,
       "vRtrLdpAddrFecOutLbl14": vRtrLdpAddrFecOutLbl14,
       "vRtrLdpAddrFecOutLblStatus14": vRtrLdpAddrFecOutLblStatus14,
       "vRtrLdpAddrFecOutLblIfIndex14": vRtrLdpAddrFecOutLblIfIndex14,
       "vRtrLdpAddrFecOutLblNxtHopType14": vRtrLdpAddrFecOutLblNxtHopType14,
       "vRtrLdpAddrFecOutLblNxtHopAddr14": vRtrLdpAddrFecOutLblNxtHopAddr14,
       "vRtrLdpAddrFecLspId14": vRtrLdpAddrFecLspId14,
       "vRtrLdpAddrFecOutLbl15": vRtrLdpAddrFecOutLbl15,
       "vRtrLdpAddrFecOutLblStatus15": vRtrLdpAddrFecOutLblStatus15,
       "vRtrLdpAddrFecOutLblIfIndex15": vRtrLdpAddrFecOutLblIfIndex15,
       "vRtrLdpAddrFecOutLblNxtHopType15": vRtrLdpAddrFecOutLblNxtHopType15,
       "vRtrLdpAddrFecOutLblNxtHopAddr15": vRtrLdpAddrFecOutLblNxtHopAddr15,
       "vRtrLdpAddrFecLspId15": vRtrLdpAddrFecLspId15,
       "vRtrLdpAddrFecOutLbl16": vRtrLdpAddrFecOutLbl16,
       "vRtrLdpAddrFecOutLblStatus16": vRtrLdpAddrFecOutLblStatus16,
       "vRtrLdpAddrFecOutLblIfIndex16": vRtrLdpAddrFecOutLblIfIndex16,
       "vRtrLdpAddrFecOutLblNxtHopType16": vRtrLdpAddrFecOutLblNxtHopType16,
       "vRtrLdpAddrFecOutLblNxtHopAddr16": vRtrLdpAddrFecOutLblNxtHopAddr16,
       "vRtrLdpAddrFecLspId16": vRtrLdpAddrFecLspId16,
       "vRtrLdpP2MPFecTable": vRtrLdpP2MPFecTable,
       "vRtrLdpP2MPFecEntry": vRtrLdpP2MPFecEntry,
       "vRtrLdpP2MPFecTunnelType": vRtrLdpP2MPFecTunnelType,
       "vRtrLdpP2MPFecTunnelId": vRtrLdpP2MPFecTunnelId,
       "vRtrLdpP2MPFecRootAddrType": vRtrLdpP2MPFecRootAddrType,
       "vRtrLdpP2MPFecRootAddress": vRtrLdpP2MPFecRootAddress,
       "vRtrLdpP2MPFecFlags": vRtrLdpP2MPFecFlags,
       "vRtrLdpP2MPFecNumInLabels": vRtrLdpP2MPFecNumInLabels,
       "vRtrLdpP2MPFecNumOutLabels": vRtrLdpP2MPFecNumOutLabels,
       "vRtrLdpP2MPFecTunnelIfId": vRtrLdpP2MPFecTunnelIfId,
       "vRtrLdpP2MPFecMetric": vRtrLdpP2MPFecMetric,
       "vRtrLdpP2MPFecMTU": vRtrLdpP2MPFecMTU,
       "vRtrLdpP2MPFecInLabelTable": vRtrLdpP2MPFecInLabelTable,
       "vRtrLdpP2MPFecInLabelEntry": vRtrLdpP2MPFecInLabelEntry,
       "vRtrLdpP2MPFecInLblId": vRtrLdpP2MPFecInLblId,
       "vRtrLdpP2MPFecInLbl": vRtrLdpP2MPFecInLbl,
       "vRtrLdpP2MPFecInLblStatus": vRtrLdpP2MPFecInLblStatus,
       "vRtrLdpP2MPFecInLblIfIndex": vRtrLdpP2MPFecInLblIfIndex,
       "vRtrLdpP2MPFecOutLabelTable": vRtrLdpP2MPFecOutLabelTable,
       "vRtrLdpP2MPFecOutLabelEntry": vRtrLdpP2MPFecOutLabelEntry,
       "vRtrLdpP2MPFecOutLblId": vRtrLdpP2MPFecOutLblId,
       "vRtrLdpP2MPFecOutLbl": vRtrLdpP2MPFecOutLbl,
       "vRtrLdpP2MPFecOutLblStatus": vRtrLdpP2MPFecOutLblStatus,
       "vRtrLdpP2MPFecOutLblNxtHopType": vRtrLdpP2MPFecOutLblNxtHopType,
       "vRtrLdpP2MPFecOutLblNxtHopAddr": vRtrLdpP2MPFecOutLblNxtHopAddr,
       "vRtrLdpP2MPFecOutLblIfIndex": vRtrLdpP2MPFecOutLblIfIndex,
       "vRtrLdpP2MPFecOutLblLspId": vRtrLdpP2MPFecOutLblLspId,
       "vRtrLdpP2MPFecMapTable": vRtrLdpP2MPFecMapTable,
       "vRtrLdpP2MPFecMapEntry": vRtrLdpP2MPFecMapEntry,
       "vRtrLdpP2MPFecMapFecType": vRtrLdpP2MPFecMapFecType,
       "vRtrLdpP2MPFecMapId": vRtrLdpP2MPFecMapId,
       "vRtrLdpAddrFecOutLblInfoTable": vRtrLdpAddrFecOutLblInfoTable,
       "vRtrLdpAddrFecOutLblInfoEntry": vRtrLdpAddrFecOutLblInfoEntry,
       "vRtrLdpAddrFecOutLblId": vRtrLdpAddrFecOutLblId,
       "vRtrLdpAddrFecOutLblMetric": vRtrLdpAddrFecOutLblMetric,
       "vRtrLdpAddrFecOutLblMtu": vRtrLdpAddrFecOutLblMtu,
       "vRtrLdpNgP2MPFecTable": vRtrLdpNgP2MPFecTable,
       "vRtrLdpNgP2MPFecEntry": vRtrLdpNgP2MPFecEntry,
       "vRtrLdpNgP2MPFecOpaqueType": vRtrLdpNgP2MPFecOpaqueType,
       "vRtrLdpNgP2MPFecOpaqueLength": vRtrLdpNgP2MPFecOpaqueLength,
       "vRtrLdpNgP2MPFecOpaqueValue": vRtrLdpNgP2MPFecOpaqueValue,
       "vRtrLdpNgP2MPFecRootAddrType": vRtrLdpNgP2MPFecRootAddrType,
       "vRtrLdpNgP2MPFecRootAddress": vRtrLdpNgP2MPFecRootAddress,
       "vRtrLdpNgP2MPFecFlags": vRtrLdpNgP2MPFecFlags,
       "vRtrLdpNgP2MPFecNumInLabels": vRtrLdpNgP2MPFecNumInLabels,
       "vRtrLdpNgP2MPFecNumOutLabels": vRtrLdpNgP2MPFecNumOutLabels,
       "vRtrLdpNgP2MPFecTunnelIfId": vRtrLdpNgP2MPFecTunnelIfId,
       "vRtrLdpNgP2MPFecMetric": vRtrLdpNgP2MPFecMetric,
       "vRtrLdpNgP2MPFecMTU": vRtrLdpNgP2MPFecMTU,
       "vRtrLdpNgP2MPFecInLabelTable": vRtrLdpNgP2MPFecInLabelTable,
       "vRtrLdpNgP2MPFecInLabelEntry": vRtrLdpNgP2MPFecInLabelEntry,
       "vRtrLdpNgP2MPFecInLblId": vRtrLdpNgP2MPFecInLblId,
       "vRtrLdpNgP2MPFecInLbl": vRtrLdpNgP2MPFecInLbl,
       "vRtrLdpNgP2MPFecInLblStatus": vRtrLdpNgP2MPFecInLblStatus,
       "vRtrLdpNgP2MPFecInLblIfIndex": vRtrLdpNgP2MPFecInLblIfIndex,
       "vRtrLdpNgP2MPFecOutLabelTable": vRtrLdpNgP2MPFecOutLabelTable,
       "vRtrLdpNgP2MPFecOutLabelEntry": vRtrLdpNgP2MPFecOutLabelEntry,
       "vRtrLdpNgP2MPFecOutLblId": vRtrLdpNgP2MPFecOutLblId,
       "vRtrLdpNgP2MPFecOutLbl": vRtrLdpNgP2MPFecOutLbl,
       "vRtrLdpNgP2MPFecOutLblStatus": vRtrLdpNgP2MPFecOutLblStatus,
       "vRtrLdpNgP2MPFecOutLblNxtHopType": vRtrLdpNgP2MPFecOutLblNxtHopType,
       "vRtrLdpNgP2MPFecOutLblNxtHopAddr": vRtrLdpNgP2MPFecOutLblNxtHopAddr,
       "vRtrLdpNgP2MPFecOutLblIfIndex": vRtrLdpNgP2MPFecOutLblIfIndex,
       "vRtrLdpNgP2MPFecOutLblLspId": vRtrLdpNgP2MPFecOutLblLspId,
       "vRtrLdpNgP2MPFecMapTable": vRtrLdpNgP2MPFecMapTable,
       "vRtrLdpNgP2MPFecMapEntry": vRtrLdpNgP2MPFecMapEntry,
       "vRtrLdpNgP2MPFecMapFlags": vRtrLdpNgP2MPFecMapFlags,
       "vRtrLdpNgP2MPFecMapNumInLabels": vRtrLdpNgP2MPFecMapNumInLabels,
       "vRtrLdpNgP2MPFecMapNumOutLabels": vRtrLdpNgP2MPFecMapNumOutLabels,
       "vRtrLdpNgP2MPFecMapTunnelIfId": vRtrLdpNgP2MPFecMapTunnelIfId,
       "vRtrLdpNgP2MPFecMapMetric": vRtrLdpNgP2MPFecMapMetric,
       "vRtrLdpNgP2MPFecMapMTU": vRtrLdpNgP2MPFecMapMTU,
       "vRtrLdpAddressFecTable": vRtrLdpAddressFecTable,
       "vRtrLdpAddressFecEntry": vRtrLdpAddressFecEntry,
       "vRtrLdpAddressFecFecType": vRtrLdpAddressFecFecType,
       "vRtrLdpAddressFecIpPrefixType": vRtrLdpAddressFecIpPrefixType,
       "vRtrLdpAddressFecIpPrefix": vRtrLdpAddressFecIpPrefix,
       "vRtrLdpAddressFecIpPrefixLen": vRtrLdpAddressFecIpPrefixLen,
       "vRtrLdpAddressFecFlags": vRtrLdpAddressFecFlags,
       "vRtrLdpAddressFecNumInLabels": vRtrLdpAddressFecNumInLabels,
       "vRtrLdpAddressFecNumOutLabels": vRtrLdpAddressFecNumOutLabels,
       "vRtrLdpAddressFecInLabelTable": vRtrLdpAddressFecInLabelTable,
       "vRtrLdpAddressFecInLabelEntry": vRtrLdpAddressFecInLabelEntry,
       "vRtrLdpAddressFecInLblId": vRtrLdpAddressFecInLblId,
       "vRtrLdpAddressFecInLbl": vRtrLdpAddressFecInLbl,
       "vRtrLdpAddressFecInLblStatus": vRtrLdpAddressFecInLblStatus,
       "vRtrLdpAddressFecInLblIfIndex": vRtrLdpAddressFecInLblIfIndex,
       "vRtrLdpAddressFecOutLabelTable": vRtrLdpAddressFecOutLabelTable,
       "vRtrLdpAddressFecOutLabelEntry": vRtrLdpAddressFecOutLabelEntry,
       "vRtrLdpAddressFecOutLblId": vRtrLdpAddressFecOutLblId,
       "vRtrLdpAddressFecOutLbl": vRtrLdpAddressFecOutLbl,
       "vRtrLdpAddressFecOutLblStatus": vRtrLdpAddressFecOutLblStatus,
       "vRtrLdpAddressFecOutLblIfIndex": vRtrLdpAddressFecOutLblIfIndex,
       "vRtrLdpAddressFecOutLblNHType": vRtrLdpAddressFecOutLblNHType,
       "vRtrLdpAddressFecOutLblNHAddr": vRtrLdpAddressFecOutLblNHAddr,
       "vRtrLdpAddressFecOutLblMetric": vRtrLdpAddressFecOutLblMetric,
       "vRtrLdpAddressFecOutLblMtu": vRtrLdpAddressFecOutLblMtu,
       "vRtrLdpAddressFecOutLblLspId": vRtrLdpAddressFecOutLblLspId,
       "vRtrLdpAddressFecMapTable": vRtrLdpAddressFecMapTable,
       "vRtrLdpAddressFecMapEntry": vRtrLdpAddressFecMapEntry,
       "vRtrLdpAddressFecMapFlags": vRtrLdpAddressFecMapFlags,
       "vRtrLdpAddressFecMapNumInLabels": vRtrLdpAddressFecMapNumInLabels,
       "vRtrLdpAddressFecMapNumOutLabels": vRtrLdpAddressFecMapNumOutLabels,
       "vRtrLdpAddrActiveFecTable": vRtrLdpAddrActiveFecTable,
       "vRtrLdpAddrActiveFecEntry": vRtrLdpAddrActiveFecEntry,
       "vRtrLdpAddrActiveFecOpType": vRtrLdpAddrActiveFecOpType,
       "vRtrLdpAddrActiveFecFecFlags": vRtrLdpAddrActiveFecFecFlags,
       "vRtrLdpAddrActiveFecNumInLbls": vRtrLdpAddrActiveFecNumInLbls,
       "vRtrLdpAddrActiveFecNumOutLbls": vRtrLdpAddrActiveFecNumOutLbls,
       "vRtrLdpAddrActiveFecInLblTable": vRtrLdpAddrActiveFecInLblTable,
       "vRtrLdpAddrActiveFecInLblEntry": vRtrLdpAddrActiveFecInLblEntry,
       "vRtrLdpAddrActiveFecInLblId": vRtrLdpAddrActiveFecInLblId,
       "vRtrLdpAddrActiveFecInLbl": vRtrLdpAddrActiveFecInLbl,
       "vRtrLdpAddrActiveFecInLblIfIndex": vRtrLdpAddrActiveFecInLblIfIndex,
       "vRtrLdpAddrActiveFecOutLblTable": vRtrLdpAddrActiveFecOutLblTable,
       "vRtrLdpAddrActiveFecOutLblEntry": vRtrLdpAddrActiveFecOutLblEntry,
       "vRtrLdpAddrActiveFecOutLblId": vRtrLdpAddrActiveFecOutLblId,
       "vRtrLdpAddrActiveFecOutLbl": vRtrLdpAddrActiveFecOutLbl,
       "vRtrLdpAddrActiveFecOutLblStatus": vRtrLdpAddrActiveFecOutLblStatus,
       "vRtrLdpAddrActiveFecOutLblIfIdx": vRtrLdpAddrActiveFecOutLblIfIdx,
       "vRtrLdpAddrActiveFecOutLblNHType": vRtrLdpAddrActiveFecOutLblNHType,
       "vRtrLdpAddrActiveFecOutLblNHAddr": vRtrLdpAddrActiveFecOutLblNHAddr,
       "vRtrLdpAddrActiveFecOutLblMetric": vRtrLdpAddrActiveFecOutLblMetric,
       "vRtrLdpAddrActiveFecOutLblMtu": vRtrLdpAddrActiveFecOutLblMtu,
       "vRtrLdpAddrActiveFecOutLblLspId": vRtrLdpAddrActiveFecOutLblLspId,
       "vRtrLdpSessionAddrTable": vRtrLdpSessionAddrTable,
       "vRtrLdpSessionAddrEntry": vRtrLdpSessionAddrEntry,
       "vRtrLdpSessionAddrLocalLdpId": vRtrLdpSessionAddrLocalLdpId,
       "vRtrLdpSessionAddrNumInAddrs": vRtrLdpSessionAddrNumInAddrs,
       "vRtrLdpSessionAddrNumOutAddrs": vRtrLdpSessionAddrNumOutAddrs,
       "vRtrLdpSessionInAddrTable": vRtrLdpSessionInAddrTable,
       "vRtrLdpSessionInAddrEntry": vRtrLdpSessionInAddrEntry,
       "vRtrLdpSessionInAddrAddrType": vRtrLdpSessionInAddrAddrType,
       "vRtrLdpSessionInAddrAddress": vRtrLdpSessionInAddrAddress,
       "vRtrLdpSessionInAddrLocalLdpId": vRtrLdpSessionInAddrLocalLdpId,
       "vRtrLdpSessionOutAddrTable": vRtrLdpSessionOutAddrTable,
       "vRtrLdpSessionOutAddrEntry": vRtrLdpSessionOutAddrEntry,
       "vRtrLdpSessionOutAddrAddrType": vRtrLdpSessionOutAddrAddrType,
       "vRtrLdpSessionOutAddrAddress": vRtrLdpSessionOutAddrAddress,
       "vRtrLdpSessionOutAddrLocalLdpId": vRtrLdpSessionOutAddrLocalLdpId,
       "vRtrLdpPeerTemplTableLstChanged": vRtrLdpPeerTemplTableLstChanged,
       "vRtrLdpPeerTemplTable": vRtrLdpPeerTemplTable,
       "vRtrLdpPeerTemplEntry": vRtrLdpPeerTemplEntry,
       "vRtrLdpPeerTemplName": vRtrLdpPeerTemplName,
       "vRtrLdpPeerTemplLastChanged": vRtrLdpPeerTemplLastChanged,
       "vRtrLdpPeerTemplRowStatus": vRtrLdpPeerTemplRowStatus,
       "vRtrLdpPeerTemplAdminState": vRtrLdpPeerTemplAdminState,
       "vRtrLdpPeerTemplInheritance": vRtrLdpPeerTemplInheritance,
       "vRtrLdpPeerTemplKeepAliveFactor": vRtrLdpPeerTemplKeepAliveFactor,
       "vRtrLdpPeerTemplKeepAliveTimeout": vRtrLdpPeerTemplKeepAliveTimeout,
       "vRtrLdpPeerTemplHelloFactor": vRtrLdpPeerTemplHelloFactor,
       "vRtrLdpPeerTemplHelloTimeout": vRtrLdpPeerTemplHelloTimeout,
       "vRtrLdpPeerTemplTunneling": vRtrLdpPeerTemplTunneling,
       "vRtrLdpPeerTemplBfdEnabled": vRtrLdpPeerTemplBfdEnabled,
       "vRtrLdpPeerTemplLsrIfIndex": vRtrLdpPeerTemplLsrIfIndex,
       "vRtrLdpPeerTemplHelloReduction": vRtrLdpPeerTemplHelloReduction,
       "vRtrLdpPeerTemplHelloReductnFctr": vRtrLdpPeerTemplHelloReductnFctr,
       "vRtrLdpPeerTemplCreateTime": vRtrLdpPeerTemplCreateTime,
       "vRtrLdpPeerTemplIndex": vRtrLdpPeerTemplIndex,
       "vRtrLdpPeerTemplLsrIdAdvert": vRtrLdpPeerTemplLsrIdAdvert,
       "vRtrLdpPeerTemplLsrIdCommunity": vRtrLdpPeerTemplLsrIdCommunity,
       "vRtrLdpPeerTemplMcastTunneling": vRtrLdpPeerTemplMcastTunneling,
       "vRtrLdpPeerTmplPlcyMpTblLstChgd": vRtrLdpPeerTmplPlcyMpTblLstChgd,
       "vRtrLdpPeerTemplPlcyMapTable": vRtrLdpPeerTemplPlcyMapTable,
       "vRtrLdpPeerTemplPlcyMapEntry": vRtrLdpPeerTemplPlcyMapEntry,
       "vRtrLdpPeerTemplPlcyMapLstChange": vRtrLdpPeerTemplPlcyMapLstChange,
       "vRtrLdpPeerTemplPlcyMapRowStatus": vRtrLdpPeerTemplPlcyMapRowStatus,
       "vRtrLdpPeerTemplPlcyMapPolicy1": vRtrLdpPeerTemplPlcyMapPolicy1,
       "vRtrLdpPeerTemplPlcyMapPolicy2": vRtrLdpPeerTemplPlcyMapPolicy2,
       "vRtrLdpPeerTemplPlcyMapPolicy3": vRtrLdpPeerTemplPlcyMapPolicy3,
       "vRtrLdpPeerTemplPlcyMapPolicy4": vRtrLdpPeerTemplPlcyMapPolicy4,
       "vRtrLdpPeerTemplPlcyMapPolicy5": vRtrLdpPeerTemplPlcyMapPolicy5,
       "vRtrLdpPeerTemplPlcyMapIndex": vRtrLdpPeerTemplPlcyMapIndex,
       "vRtrLdpPeerTemplPlcyMapCreateTim": vRtrLdpPeerTemplPlcyMapCreateTim,
       "vRtrLdpPeerTemplPeerTable": vRtrLdpPeerTemplPeerTable,
       "vRtrLdpPeerTemplPeerEntry": vRtrLdpPeerTemplPeerEntry,
       "vRtrLdpPeerTemplPeerAddrType": vRtrLdpPeerTemplPeerAddrType,
       "vRtrLdpPeerTemplPeerAddress": vRtrLdpPeerTemplPeerAddress,
       "vRtrLdpPeerTemplPeerCreateTime": vRtrLdpPeerTemplPeerCreateTime,
       "tmnxLdpNotifyPrefix": tmnxLdpNotifyPrefix,
       "tmnxLdpNotifications": tmnxLdpNotifications,
       "vRtrLdpStateChange": vRtrLdpStateChange,
       "vRtrLdpInstanceStateChange": vRtrLdpInstanceStateChange,
       "vRtrLdpIfStateChange": vRtrLdpIfStateChange,
       "vRtrLdpSvcIdMismatch": vRtrLdpSvcIdMismatch,
       "vRtrLdpGroupIdMismatch": vRtrLdpGroupIdMismatch,
       "vRtrLdpSessionStateChange": vRtrLdpSessionStateChange,
       "vRtrLdpSessMaxFecThresChanged": vRtrLdpSessMaxFecThresChanged,
       "vRtrLdpSessMaxFecLimitReached": vRtrLdpSessMaxFecLimitReached}
)
