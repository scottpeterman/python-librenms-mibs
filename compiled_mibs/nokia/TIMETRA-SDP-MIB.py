# SNMP MIB module (TIMETRA-SDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\TIMETRA-SDP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:14:12 2025
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tmnxCardSlotNum,
 tmnxChassisIndex,
 tmnxMDASlotNum) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxCardSlotNum",
    "tmnxChassisIndex",
    "tmnxMDASlotNum")

(TConfigOrVsdFilterID,
 TFilterID) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TConfigOrVsdFilterID",
    "TFilterID")

(timetraSRMIBModules,) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules")

(BridgeId,
 ConfigStatus,
 L2ptProtocols,
 LspIdList,
 MvplsPruneState,
 PWTemplateId,
 SdpBindBandwidth,
 SdpBindVcType,
 SdpId,
 ServObjDesc,
 ServObjName,
 StpExceptionCondition,
 StpPortRole,
 StpProtocol,
 TStpPortState,
 TdmOptionsCasTrunkFraming,
 TdmOptionsSigPkts,
 TlsBpduTranslation,
 TlsLimitMacMove,
 TlsLimitMacMoveLevel,
 TmnxSiteId,
 VpnId,
 custId,
 protectedMacForNotify,
 svcDhcpClientLease,
 svcDhcpCoAError,
 svcDhcpLseStateNewChAddr,
 svcDhcpLseStateNewCiAddr,
 svcDhcpLseStateOldChAddr,
 svcDhcpLseStateOldCiAddr,
 svcDhcpLseStatePopulateError,
 svcDhcpPacketProblem,
 svcDhcpProxyError,
 svcDhcpSubAuthError,
 svcId,
 svcTlsBackboneVplsSvcId,
 svcTlsMacMoveMaxRate,
 svcTlsStpDesignatedRoot,
 svcVpnId,
 tlsDhcpPacketProblem,
 tlsFdbType,
 tmnxCustomerBridgeId,
 tmnxCustomerRootBridgeId,
 tmnxOldSdpBindTlsStpPortState,
 tmnxOtherBridgeId,
 tmnxServConformance,
 tmnxServNotifications,
 tmnxServObjs,
 tmnxSvcObjs,
 tstpTraps) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "BridgeId",
    "ConfigStatus",
    "L2ptProtocols",
    "LspIdList",
    "MvplsPruneState",
    "PWTemplateId",
    "SdpBindBandwidth",
    "SdpBindVcType",
    "SdpId",
    "ServObjDesc",
    "ServObjName",
    "StpExceptionCondition",
    "StpPortRole",
    "StpProtocol",
    "TStpPortState",
    "TdmOptionsCasTrunkFraming",
    "TdmOptionsSigPkts",
    "TlsBpduTranslation",
    "TlsLimitMacMove",
    "TlsLimitMacMoveLevel",
    "TmnxSiteId",
    "VpnId",
    "custId",
    "protectedMacForNotify",
    "svcDhcpClientLease",
    "svcDhcpCoAError",
    "svcDhcpLseStateNewChAddr",
    "svcDhcpLseStateNewCiAddr",
    "svcDhcpLseStateOldChAddr",
    "svcDhcpLseStateOldCiAddr",
    "svcDhcpLseStatePopulateError",
    "svcDhcpPacketProblem",
    "svcDhcpProxyError",
    "svcDhcpSubAuthError",
    "svcId",
    "svcTlsBackboneVplsSvcId",
    "svcTlsMacMoveMaxRate",
    "svcTlsStpDesignatedRoot",
    "svcVpnId",
    "tlsDhcpPacketProblem",
    "tlsFdbType",
    "tmnxCustomerBridgeId",
    "tmnxCustomerRootBridgeId",
    "tmnxOldSdpBindTlsStpPortState",
    "tmnxOtherBridgeId",
    "tmnxServConformance",
    "tmnxServNotifications",
    "tmnxServObjs",
    "tmnxSvcObjs",
    "tstpTraps")

(AluNgeKeygroupIdOrZero,
 SdpBindId,
 ServiceAdminStatus,
 TCpmProtPolicyID,
 TFCSet,
 TItemDescription,
 TLNamedItemOrEmpty,
 TNamedItem,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TQosQGrpInstanceIDorZero,
 TSdpEgressPolicyID,
 TSdpIngressPolicyID,
 TmnxActionType,
 TmnxAdminState,
 TmnxAdminStateTruthValue,
 TmnxBfdEncap,
 TmnxBfdSessOperState,
 TmnxBsxAarpIdOrZero,
 TmnxBsxAarpServiceRefType,
 TmnxBsxTransPrefPolicyIdOrZero,
 TmnxBsxTransitIpPolicyIdOrZero,
 TmnxCreateOrigin,
 TmnxCustId,
 TmnxEnabledDisabled,
 TmnxEnabledDisabledAdminState,
 TmnxEvpnMHEthSegStatus,
 TmnxISID,
 TmnxIgmpVersion,
 TmnxIsidMFibStatus,
 TmnxMplsTpGlobalID,
 TmnxMplsTpNodeID,
 TmnxOperState,
 TmnxPortID,
 TmnxPwGlobalId,
 TmnxServId,
 TmnxSpokeSdpIdOrZero,
 TmnxVPNRouteDistinguisher,
 TmnxVRtrMplsLspID,
 TmnxVRtrMplsLspIDNoZero,
 TmnxVcId,
 TmnxVcIdOrNone) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "AluNgeKeygroupIdOrZero",
    "SdpBindId",
    "ServiceAdminStatus",
    "TCpmProtPolicyID",
    "TFCSet",
    "TItemDescription",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TQosQGrpInstanceIDorZero",
    "TSdpEgressPolicyID",
    "TSdpIngressPolicyID",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxAdminStateTruthValue",
    "TmnxBfdEncap",
    "TmnxBfdSessOperState",
    "TmnxBsxAarpIdOrZero",
    "TmnxBsxAarpServiceRefType",
    "TmnxBsxTransPrefPolicyIdOrZero",
    "TmnxBsxTransitIpPolicyIdOrZero",
    "TmnxCreateOrigin",
    "TmnxCustId",
    "TmnxEnabledDisabled",
    "TmnxEnabledDisabledAdminState",
    "TmnxEvpnMHEthSegStatus",
    "TmnxISID",
    "TmnxIgmpVersion",
    "TmnxIsidMFibStatus",
    "TmnxMplsTpGlobalID",
    "TmnxMplsTpNodeID",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxPwGlobalId",
    "TmnxServId",
    "TmnxSpokeSdpIdOrZero",
    "TmnxVPNRouteDistinguisher",
    "TmnxVRtrMplsLspID",
    "TmnxVRtrMplsLspIDNoZero",
    "TmnxVcId",
    "TmnxVcIdOrNone")


# MODULE-IDENTITY

timetraServicesSdpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 56)
)
if mibBuilder.loadTexts:
    timetraServicesSdpMIBModule.setRevisions(
        ("2016-05-14 00:00",
         "2016-02-01 00:00",
         "2015-01-01 00:00",
         "2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2007-10-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxSdpConformance_ObjectIdentity = ObjectIdentity
tmnxSdpConformance = _TmnxSdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4)
)
_TmnxSdpCompliances_ObjectIdentity = ObjectIdentity
tmnxSdpCompliances = _TmnxSdpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1)
)
_TmnxSdpGroups_ObjectIdentity = ObjectIdentity
tmnxSdpGroups = _TmnxSdpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2)
)
_SvcTlsBgpADPWTempBindTblLC_Type = TimeStamp
_SvcTlsBgpADPWTempBindTblLC_Object = MibScalar
svcTlsBgpADPWTempBindTblLC = _SvcTlsBgpADPWTempBindTblLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 32),
    _SvcTlsBgpADPWTempBindTblLC_Type()
)
svcTlsBgpADPWTempBindTblLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindTblLC.setStatus("current")
_SvcTlsBgpADPWTempBindTable_Object = MibTable
svcTlsBgpADPWTempBindTable = _SvcTlsBgpADPWTempBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 33)
)
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindTable.setStatus("current")
_SvcTlsBgpADPWTempBindEntry_Object = MibTableRow
svcTlsBgpADPWTempBindEntry = _SvcTlsBgpADPWTempBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 33, 1)
)
svcTlsBgpADPWTempBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "pwTemplateId"),
)
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindEntry.setStatus("current")
_SvcTlsBgpADPWTempBindRowStatus_Type = RowStatus
_SvcTlsBgpADPWTempBindRowStatus_Object = MibTableColumn
svcTlsBgpADPWTempBindRowStatus = _SvcTlsBgpADPWTempBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 33, 1, 1),
    _SvcTlsBgpADPWTempBindRowStatus_Type()
)
svcTlsBgpADPWTempBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindRowStatus.setStatus("current")
_SvcTlsBgpADPWTempBindLastChngd_Type = TimeStamp
_SvcTlsBgpADPWTempBindLastChngd_Object = MibTableColumn
svcTlsBgpADPWTempBindLastChngd = _SvcTlsBgpADPWTempBindLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 33, 1, 2),
    _SvcTlsBgpADPWTempBindLastChngd_Type()
)
svcTlsBgpADPWTempBindLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindLastChngd.setStatus("current")


class _SvcTlsBgpADPWTempBindSHG_Type(TNamedItemOrEmpty):
    """Custom type svcTlsBgpADPWTempBindSHG based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_SvcTlsBgpADPWTempBindSHG_Type.__name__ = "TNamedItemOrEmpty"
_SvcTlsBgpADPWTempBindSHG_Object = MibTableColumn
svcTlsBgpADPWTempBindSHG = _SvcTlsBgpADPWTempBindSHG_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 33, 1, 3),
    _SvcTlsBgpADPWTempBindSHG_Type()
)
svcTlsBgpADPWTempBindSHG.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindSHG.setStatus("current")


class _SvcTlsBgpADPWTempBindOperGrp_Type(TNamedItemOrEmpty):
    """Custom type svcTlsBgpADPWTempBindOperGrp based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_SvcTlsBgpADPWTempBindOperGrp_Type.__name__ = "TNamedItemOrEmpty"
_SvcTlsBgpADPWTempBindOperGrp_Object = MibTableColumn
svcTlsBgpADPWTempBindOperGrp = _SvcTlsBgpADPWTempBindOperGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 33, 1, 4),
    _SvcTlsBgpADPWTempBindOperGrp_Type()
)
svcTlsBgpADPWTempBindOperGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindOperGrp.setStatus("current")


class _SvcTlsBgpADPWTempBindCreatOrigin_Type(TmnxCreateOrigin):
    """Custom type svcTlsBgpADPWTempBindCreatOrigin based on TmnxCreateOrigin"""
    defaultValue = 1


_SvcTlsBgpADPWTempBindCreatOrigin_Type.__name__ = "TmnxCreateOrigin"
_SvcTlsBgpADPWTempBindCreatOrigin_Object = MibTableColumn
svcTlsBgpADPWTempBindCreatOrigin = _SvcTlsBgpADPWTempBindCreatOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 33, 1, 5),
    _SvcTlsBgpADPWTempBindCreatOrigin_Type()
)
svcTlsBgpADPWTempBindCreatOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindCreatOrigin.setStatus("current")


class _SvcTlsBgpADPWTempBindBfdTemplate_Type(TNamedItemOrEmpty):
    """Custom type svcTlsBgpADPWTempBindBfdTemplate based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_SvcTlsBgpADPWTempBindBfdTemplate_Type.__name__ = "TNamedItemOrEmpty"
_SvcTlsBgpADPWTempBindBfdTemplate_Object = MibTableColumn
svcTlsBgpADPWTempBindBfdTemplate = _SvcTlsBgpADPWTempBindBfdTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 33, 1, 6),
    _SvcTlsBgpADPWTempBindBfdTemplate_Type()
)
svcTlsBgpADPWTempBindBfdTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindBfdTemplate.setStatus("current")


class _SvcTlsBgpADPWTempBindBfdEnable_Type(TruthValue):
    """Custom type svcTlsBgpADPWTempBindBfdEnable based on TruthValue"""
    defaultValue = 2


_SvcTlsBgpADPWTempBindBfdEnable_Type.__name__ = "TruthValue"
_SvcTlsBgpADPWTempBindBfdEnable_Object = MibTableColumn
svcTlsBgpADPWTempBindBfdEnable = _SvcTlsBgpADPWTempBindBfdEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 33, 1, 7),
    _SvcTlsBgpADPWTempBindBfdEnable_Type()
)
svcTlsBgpADPWTempBindBfdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindBfdEnable.setStatus("current")


class _SvcTlsBgpADPWTempBindBfdEncap_Type(TmnxBfdEncap):
    """Custom type svcTlsBgpADPWTempBindBfdEncap based on TmnxBfdEncap"""
    defaultValue = 1


_SvcTlsBgpADPWTempBindBfdEncap_Type.__name__ = "TmnxBfdEncap"
_SvcTlsBgpADPWTempBindBfdEncap_Object = MibTableColumn
svcTlsBgpADPWTempBindBfdEncap = _SvcTlsBgpADPWTempBindBfdEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 33, 1, 8),
    _SvcTlsBgpADPWTempBindBfdEncap_Type()
)
svcTlsBgpADPWTempBindBfdEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindBfdEncap.setStatus("current")


class _SvcTlsBgpADPWTempBindMonOperGrp_Type(TNamedItemOrEmpty):
    """Custom type svcTlsBgpADPWTempBindMonOperGrp based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_SvcTlsBgpADPWTempBindMonOperGrp_Type.__name__ = "TNamedItemOrEmpty"
_SvcTlsBgpADPWTempBindMonOperGrp_Object = MibTableColumn
svcTlsBgpADPWTempBindMonOperGrp = _SvcTlsBgpADPWTempBindMonOperGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 33, 1, 9),
    _SvcTlsBgpADPWTempBindMonOperGrp_Type()
)
svcTlsBgpADPWTempBindMonOperGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindMonOperGrp.setStatus("current")
_SvcTlsBgpADPWTempBindRTTblLC_Type = TimeStamp
_SvcTlsBgpADPWTempBindRTTblLC_Object = MibScalar
svcTlsBgpADPWTempBindRTTblLC = _SvcTlsBgpADPWTempBindRTTblLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 34),
    _SvcTlsBgpADPWTempBindRTTblLC_Type()
)
svcTlsBgpADPWTempBindRTTblLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindRTTblLC.setStatus("current")
_SvcTlsBgpADPWTempBindRTTable_Object = MibTable
svcTlsBgpADPWTempBindRTTable = _SvcTlsBgpADPWTempBindRTTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 35)
)
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindRTTable.setStatus("current")
_SvcTlsBgpADPWTempBindRTEntry_Object = MibTableRow
svcTlsBgpADPWTempBindRTEntry = _SvcTlsBgpADPWTempBindRTEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 35, 1)
)
svcTlsBgpADPWTempBindRTEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "pwTemplateId"),
    (1, "TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindRT"),
)
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindRTEntry.setStatus("current")
_SvcTlsBgpADPWTempBindRT_Type = TNamedItem
_SvcTlsBgpADPWTempBindRT_Object = MibTableColumn
svcTlsBgpADPWTempBindRT = _SvcTlsBgpADPWTempBindRT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 35, 1, 1),
    _SvcTlsBgpADPWTempBindRT_Type()
)
svcTlsBgpADPWTempBindRT.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindRT.setStatus("current")
_SvcTlsBgpADPWTempBindRTRowStat_Type = RowStatus
_SvcTlsBgpADPWTempBindRTRowStat_Object = MibTableColumn
svcTlsBgpADPWTempBindRTRowStat = _SvcTlsBgpADPWTempBindRTRowStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 35, 1, 2),
    _SvcTlsBgpADPWTempBindRTRowStat_Type()
)
svcTlsBgpADPWTempBindRTRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindRTRowStat.setStatus("current")
_SvcL2RteTableLastChanged_Type = TimeStamp
_SvcL2RteTableLastChanged_Object = MibScalar
svcL2RteTableLastChanged = _SvcL2RteTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 38),
    _SvcL2RteTableLastChanged_Type()
)
svcL2RteTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2RteTableLastChanged.setStatus("current")
_SvcL2RteTable_Object = MibTable
svcL2RteTable = _SvcL2RteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39)
)
if mibBuilder.loadTexts:
    svcL2RteTable.setStatus("current")
_SvcL2RteEntry_Object = MibTableRow
svcL2RteEntry = _SvcL2RteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39, 1)
)
svcL2RteEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "svcL2RteVsiPrefix"),
    (0, "TIMETRA-SDP-MIB", "svcL2RteRouteDistinguisher"),
    (0, "TIMETRA-SDP-MIB", "svcL2RteNextHopType"),
    (0, "TIMETRA-SDP-MIB", "svcL2RteNextHop"),
)
if mibBuilder.loadTexts:
    svcL2RteEntry.setStatus("current")
_SvcL2RteVsiPrefix_Type = Unsigned32
_SvcL2RteVsiPrefix_Object = MibTableColumn
svcL2RteVsiPrefix = _SvcL2RteVsiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39, 1, 1),
    _SvcL2RteVsiPrefix_Type()
)
svcL2RteVsiPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2RteVsiPrefix.setStatus("current")
_SvcL2RteRouteDistinguisher_Type = TmnxVPNRouteDistinguisher
_SvcL2RteRouteDistinguisher_Object = MibTableColumn
svcL2RteRouteDistinguisher = _SvcL2RteRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39, 1, 2),
    _SvcL2RteRouteDistinguisher_Type()
)
svcL2RteRouteDistinguisher.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2RteRouteDistinguisher.setStatus("current")
_SvcL2RteNextHopType_Type = InetAddressType
_SvcL2RteNextHopType_Object = MibTableColumn
svcL2RteNextHopType = _SvcL2RteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39, 1, 3),
    _SvcL2RteNextHopType_Type()
)
svcL2RteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2RteNextHopType.setStatus("current")
_SvcL2RteNextHop_Type = InetAddress
_SvcL2RteNextHop_Object = MibTableColumn
svcL2RteNextHop = _SvcL2RteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39, 1, 4),
    _SvcL2RteNextHop_Type()
)
svcL2RteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2RteNextHop.setStatus("current")
_SvcL2RteSdpBindId_Type = SdpBindId
_SvcL2RteSdpBindId_Object = MibTableColumn
svcL2RteSdpBindId = _SvcL2RteSdpBindId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39, 1, 5),
    _SvcL2RteSdpBindId_Type()
)
svcL2RteSdpBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2RteSdpBindId.setStatus("current")
_SvcL2RtePwTemplateId_Type = PWTemplateId
_SvcL2RtePwTemplateId_Object = MibTableColumn
svcL2RtePwTemplateId = _SvcL2RtePwTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39, 1, 6),
    _SvcL2RtePwTemplateId_Type()
)
svcL2RtePwTemplateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2RtePwTemplateId.setStatus("current")


class _SvcL2RteError_Type(DisplayString):
    """Custom type svcL2RteError based on DisplayString"""
    defaultValue = OctetString("")


_SvcL2RteError_Type.__name__ = "DisplayString"
_SvcL2RteError_Object = MibTableColumn
svcL2RteError = _SvcL2RteError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39, 1, 7),
    _SvcL2RteError_Type()
)
svcL2RteError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2RteError.setStatus("current")


class _SvcL2RteLastErrorTime_Type(TimeStamp):
    """Custom type svcL2RteLastErrorTime based on TimeStamp"""
    defaultValue = 0


_SvcL2RteLastErrorTime_Type.__name__ = "TimeStamp"
_SvcL2RteLastErrorTime_Object = MibTableColumn
svcL2RteLastErrorTime = _SvcL2RteLastErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39, 1, 8),
    _SvcL2RteLastErrorTime_Type()
)
svcL2RteLastErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2RteLastErrorTime.setStatus("current")


class _SvcL2RteStatus_Type(Integer32):
    """Custom type svcL2RteStatus based on Integer32"""
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


_SvcL2RteStatus_Type.__name__ = "Integer32"
_SvcL2RteStatus_Object = MibTableColumn
svcL2RteStatus = _SvcL2RteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39, 1, 9),
    _SvcL2RteStatus_Type()
)
svcL2RteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2RteStatus.setStatus("current")
_SvcL2BgpVplsRteTable_Object = MibTable
svcL2BgpVplsRteTable = _SvcL2BgpVplsRteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 84)
)
if mibBuilder.loadTexts:
    svcL2BgpVplsRteTable.setStatus("current")
_SvcL2BgpVplsRteEntry_Object = MibTableRow
svcL2BgpVplsRteEntry = _SvcL2BgpVplsRteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 84, 1)
)
svcL2BgpVplsRteEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "svcL2BgpVplsRteVeId"),
    (0, "TIMETRA-SDP-MIB", "svcL2BgpVplsRteRD"),
    (0, "TIMETRA-SDP-MIB", "svcL2BgpVplsRteNextHopType"),
    (0, "TIMETRA-SDP-MIB", "svcL2BgpVplsRteNextHop"),
)
if mibBuilder.loadTexts:
    svcL2BgpVplsRteEntry.setStatus("current")
_SvcL2BgpVplsRteVeId_Type = TmnxSiteId
_SvcL2BgpVplsRteVeId_Object = MibTableColumn
svcL2BgpVplsRteVeId = _SvcL2BgpVplsRteVeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 84, 1, 1),
    _SvcL2BgpVplsRteVeId_Type()
)
svcL2BgpVplsRteVeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2BgpVplsRteVeId.setStatus("current")
_SvcL2BgpVplsRteRD_Type = TmnxVPNRouteDistinguisher
_SvcL2BgpVplsRteRD_Object = MibTableColumn
svcL2BgpVplsRteRD = _SvcL2BgpVplsRteRD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 84, 1, 2),
    _SvcL2BgpVplsRteRD_Type()
)
svcL2BgpVplsRteRD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2BgpVplsRteRD.setStatus("current")
_SvcL2BgpVplsRteNextHopType_Type = InetAddressType
_SvcL2BgpVplsRteNextHopType_Object = MibTableColumn
svcL2BgpVplsRteNextHopType = _SvcL2BgpVplsRteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 84, 1, 3),
    _SvcL2BgpVplsRteNextHopType_Type()
)
svcL2BgpVplsRteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2BgpVplsRteNextHopType.setStatus("current")
_SvcL2BgpVplsRteNextHop_Type = InetAddress
_SvcL2BgpVplsRteNextHop_Object = MibTableColumn
svcL2BgpVplsRteNextHop = _SvcL2BgpVplsRteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 84, 1, 4),
    _SvcL2BgpVplsRteNextHop_Type()
)
svcL2BgpVplsRteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2BgpVplsRteNextHop.setStatus("current")
_SvcL2BgpVplsRteSdpBindId_Type = SdpBindId
_SvcL2BgpVplsRteSdpBindId_Object = MibTableColumn
svcL2BgpVplsRteSdpBindId = _SvcL2BgpVplsRteSdpBindId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 84, 1, 5),
    _SvcL2BgpVplsRteSdpBindId_Type()
)
svcL2BgpVplsRteSdpBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVplsRteSdpBindId.setStatus("current")
_SvcL2BgpVplsRtePwTemplateId_Type = PWTemplateId
_SvcL2BgpVplsRtePwTemplateId_Object = MibTableColumn
svcL2BgpVplsRtePwTemplateId = _SvcL2BgpVplsRtePwTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 84, 1, 6),
    _SvcL2BgpVplsRtePwTemplateId_Type()
)
svcL2BgpVplsRtePwTemplateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVplsRtePwTemplateId.setStatus("current")


class _SvcL2BgpVplsRteError_Type(DisplayString):
    """Custom type svcL2BgpVplsRteError based on DisplayString"""
    defaultValue = OctetString("")


_SvcL2BgpVplsRteError_Type.__name__ = "DisplayString"
_SvcL2BgpVplsRteError_Object = MibTableColumn
svcL2BgpVplsRteError = _SvcL2BgpVplsRteError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 84, 1, 7),
    _SvcL2BgpVplsRteError_Type()
)
svcL2BgpVplsRteError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVplsRteError.setStatus("current")


class _SvcL2BgpVplsRteLastErrorTime_Type(TimeStamp):
    """Custom type svcL2BgpVplsRteLastErrorTime based on TimeStamp"""
    defaultValue = 0


_SvcL2BgpVplsRteLastErrorTime_Type.__name__ = "TimeStamp"
_SvcL2BgpVplsRteLastErrorTime_Object = MibTableColumn
svcL2BgpVplsRteLastErrorTime = _SvcL2BgpVplsRteLastErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 84, 1, 8),
    _SvcL2BgpVplsRteLastErrorTime_Type()
)
svcL2BgpVplsRteLastErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVplsRteLastErrorTime.setStatus("current")
_SvcL2BgpVplsRteControlWord_Type = Unsigned32
_SvcL2BgpVplsRteControlWord_Object = MibTableColumn
svcL2BgpVplsRteControlWord = _SvcL2BgpVplsRteControlWord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 84, 1, 9),
    _SvcL2BgpVplsRteControlWord_Type()
)
svcL2BgpVplsRteControlWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVplsRteControlWord.setStatus("current")
_SvcL2BgpVplsRtePathMtu_Type = Integer32
_SvcL2BgpVplsRtePathMtu_Object = MibTableColumn
svcL2BgpVplsRtePathMtu = _SvcL2BgpVplsRtePathMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 84, 1, 10),
    _SvcL2BgpVplsRtePathMtu_Type()
)
svcL2BgpVplsRtePathMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVplsRtePathMtu.setStatus("current")


class _SvcL2BgpVplsRteState_Type(Integer32):
    """Custom type svcL2BgpVplsRteState based on Integer32"""
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


_SvcL2BgpVplsRteState_Type.__name__ = "Integer32"
_SvcL2BgpVplsRteState_Object = MibTableColumn
svcL2BgpVplsRteState = _SvcL2BgpVplsRteState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 84, 1, 11),
    _SvcL2BgpVplsRteState_Type()
)
svcL2BgpVplsRteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVplsRteState.setStatus("current")
_SvcL2BgpVplsRteSeqDelivery_Type = Unsigned32
_SvcL2BgpVplsRteSeqDelivery_Object = MibTableColumn
svcL2BgpVplsRteSeqDelivery = _SvcL2BgpVplsRteSeqDelivery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 84, 1, 12),
    _SvcL2BgpVplsRteSeqDelivery_Type()
)
svcL2BgpVplsRteSeqDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVplsRteSeqDelivery.setStatus("current")
_SvcL2BgpVplsRteDF_Type = TruthValue
_SvcL2BgpVplsRteDF_Object = MibTableColumn
svcL2BgpVplsRteDF = _SvcL2BgpVplsRteDF_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 84, 1, 13),
    _SvcL2BgpVplsRteDF_Type()
)
svcL2BgpVplsRteDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVplsRteDF.setStatus("current")


class _SvcL2BgpVplsRteStatus_Type(Integer32):
    """Custom type svcL2BgpVplsRteStatus based on Integer32"""
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


_SvcL2BgpVplsRteStatus_Type.__name__ = "Integer32"
_SvcL2BgpVplsRteStatus_Object = MibTableColumn
svcL2BgpVplsRteStatus = _SvcL2BgpVplsRteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 84, 1, 14),
    _SvcL2BgpVplsRteStatus_Type()
)
svcL2BgpVplsRteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVplsRteStatus.setStatus("current")
_SvcVllBgpADPWTempBindTblLC_Type = TimeStamp
_SvcVllBgpADPWTempBindTblLC_Object = MibScalar
svcVllBgpADPWTempBindTblLC = _SvcVllBgpADPWTempBindTblLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 143),
    _SvcVllBgpADPWTempBindTblLC_Type()
)
svcVllBgpADPWTempBindTblLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcVllBgpADPWTempBindTblLC.setStatus("current")
_SvcVllBgpADPWTempBindTable_Object = MibTable
svcVllBgpADPWTempBindTable = _SvcVllBgpADPWTempBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 144)
)
if mibBuilder.loadTexts:
    svcVllBgpADPWTempBindTable.setStatus("current")
_SvcVllBgpADPWTempBindEntry_Object = MibTableRow
svcVllBgpADPWTempBindEntry = _SvcVllBgpADPWTempBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 144, 1)
)
svcVllBgpADPWTempBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "pwTemplateId"),
)
if mibBuilder.loadTexts:
    svcVllBgpADPWTempBindEntry.setStatus("current")
_SvcVllBgpADPWTempBindRowStatus_Type = RowStatus
_SvcVllBgpADPWTempBindRowStatus_Object = MibTableColumn
svcVllBgpADPWTempBindRowStatus = _SvcVllBgpADPWTempBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 144, 1, 1),
    _SvcVllBgpADPWTempBindRowStatus_Type()
)
svcVllBgpADPWTempBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVllBgpADPWTempBindRowStatus.setStatus("current")
_SvcVllBgpADPWTempBindLastChngd_Type = TimeStamp
_SvcVllBgpADPWTempBindLastChngd_Object = MibTableColumn
svcVllBgpADPWTempBindLastChngd = _SvcVllBgpADPWTempBindLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 144, 1, 2),
    _SvcVllBgpADPWTempBindLastChngd_Type()
)
svcVllBgpADPWTempBindLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcVllBgpADPWTempBindLastChngd.setStatus("current")


class _SvcVllBgpADPWTempBindEndPt_Type(TNamedItemOrEmpty):
    """Custom type svcVllBgpADPWTempBindEndPt based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_SvcVllBgpADPWTempBindEndPt_Type.__name__ = "TNamedItemOrEmpty"
_SvcVllBgpADPWTempBindEndPt_Object = MibTableColumn
svcVllBgpADPWTempBindEndPt = _SvcVllBgpADPWTempBindEndPt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 144, 1, 3),
    _SvcVllBgpADPWTempBindEndPt_Type()
)
svcVllBgpADPWTempBindEndPt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVllBgpADPWTempBindEndPt.setStatus("current")


class _SvcVllBgpADPWTempBindBfdTemplate_Type(TNamedItemOrEmpty):
    """Custom type svcVllBgpADPWTempBindBfdTemplate based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_SvcVllBgpADPWTempBindBfdTemplate_Type.__name__ = "TNamedItemOrEmpty"
_SvcVllBgpADPWTempBindBfdTemplate_Object = MibTableColumn
svcVllBgpADPWTempBindBfdTemplate = _SvcVllBgpADPWTempBindBfdTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 144, 1, 4),
    _SvcVllBgpADPWTempBindBfdTemplate_Type()
)
svcVllBgpADPWTempBindBfdTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVllBgpADPWTempBindBfdTemplate.setStatus("current")


class _SvcVllBgpADPWTempBindBfdEnable_Type(TruthValue):
    """Custom type svcVllBgpADPWTempBindBfdEnable based on TruthValue"""
    defaultValue = 2


_SvcVllBgpADPWTempBindBfdEnable_Type.__name__ = "TruthValue"
_SvcVllBgpADPWTempBindBfdEnable_Object = MibTableColumn
svcVllBgpADPWTempBindBfdEnable = _SvcVllBgpADPWTempBindBfdEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 144, 1, 5),
    _SvcVllBgpADPWTempBindBfdEnable_Type()
)
svcVllBgpADPWTempBindBfdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVllBgpADPWTempBindBfdEnable.setStatus("current")


class _SvcVllBgpADPWTempBindBfdEncap_Type(TmnxBfdEncap):
    """Custom type svcVllBgpADPWTempBindBfdEncap based on TmnxBfdEncap"""
    defaultValue = 1


_SvcVllBgpADPWTempBindBfdEncap_Type.__name__ = "TmnxBfdEncap"
_SvcVllBgpADPWTempBindBfdEncap_Object = MibTableColumn
svcVllBgpADPWTempBindBfdEncap = _SvcVllBgpADPWTempBindBfdEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 144, 1, 6),
    _SvcVllBgpADPWTempBindBfdEncap_Type()
)
svcVllBgpADPWTempBindBfdEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVllBgpADPWTempBindBfdEncap.setStatus("current")
_SvcVllBgpADPWTempBindRTTblLC_Type = TimeStamp
_SvcVllBgpADPWTempBindRTTblLC_Object = MibScalar
svcVllBgpADPWTempBindRTTblLC = _SvcVllBgpADPWTempBindRTTblLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 145),
    _SvcVllBgpADPWTempBindRTTblLC_Type()
)
svcVllBgpADPWTempBindRTTblLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcVllBgpADPWTempBindRTTblLC.setStatus("current")
_SvcVllBgpADPWTempBindRTTable_Object = MibTable
svcVllBgpADPWTempBindRTTable = _SvcVllBgpADPWTempBindRTTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 146)
)
if mibBuilder.loadTexts:
    svcVllBgpADPWTempBindRTTable.setStatus("current")
_SvcVllBgpADPWTempBindRTEntry_Object = MibTableRow
svcVllBgpADPWTempBindRTEntry = _SvcVllBgpADPWTempBindRTEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 146, 1)
)
svcVllBgpADPWTempBindRTEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "pwTemplateId"),
    (1, "TIMETRA-SDP-MIB", "svcVllBgpADPWTempBindRT"),
)
if mibBuilder.loadTexts:
    svcVllBgpADPWTempBindRTEntry.setStatus("current")
_SvcVllBgpADPWTempBindRT_Type = TNamedItem
_SvcVllBgpADPWTempBindRT_Object = MibTableColumn
svcVllBgpADPWTempBindRT = _SvcVllBgpADPWTempBindRT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 146, 1, 1),
    _SvcVllBgpADPWTempBindRT_Type()
)
svcVllBgpADPWTempBindRT.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcVllBgpADPWTempBindRT.setStatus("current")
_SvcVllBgpADPWTempBindRTRowStat_Type = RowStatus
_SvcVllBgpADPWTempBindRTRowStat_Object = MibTableColumn
svcVllBgpADPWTempBindRTRowStat = _SvcVllBgpADPWTempBindRTRowStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 146, 1, 2),
    _SvcVllBgpADPWTempBindRTRowStat_Type()
)
svcVllBgpADPWTempBindRTRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVllBgpADPWTempBindRTRowStat.setStatus("current")
_SvcL2BgpVpwsRteTable_Object = MibTable
svcL2BgpVpwsRteTable = _SvcL2BgpVpwsRteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 147)
)
if mibBuilder.loadTexts:
    svcL2BgpVpwsRteTable.setStatus("current")
_SvcL2BgpVpwsRteEntry_Object = MibTableRow
svcL2BgpVpwsRteEntry = _SvcL2BgpVpwsRteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 147, 1)
)
svcL2BgpVpwsRteEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "svcL2BgpVpwsRteVeId"),
    (0, "TIMETRA-SDP-MIB", "svcL2BgpVpwsRteRD"),
    (0, "TIMETRA-SDP-MIB", "svcL2BgpVpwsRteNextHopType"),
    (0, "TIMETRA-SDP-MIB", "svcL2BgpVpwsRteNextHop"),
)
if mibBuilder.loadTexts:
    svcL2BgpVpwsRteEntry.setStatus("current")
_SvcL2BgpVpwsRteVeId_Type = TmnxSiteId
_SvcL2BgpVpwsRteVeId_Object = MibTableColumn
svcL2BgpVpwsRteVeId = _SvcL2BgpVpwsRteVeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 147, 1, 1),
    _SvcL2BgpVpwsRteVeId_Type()
)
svcL2BgpVpwsRteVeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2BgpVpwsRteVeId.setStatus("current")
_SvcL2BgpVpwsRteRD_Type = TmnxVPNRouteDistinguisher
_SvcL2BgpVpwsRteRD_Object = MibTableColumn
svcL2BgpVpwsRteRD = _SvcL2BgpVpwsRteRD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 147, 1, 2),
    _SvcL2BgpVpwsRteRD_Type()
)
svcL2BgpVpwsRteRD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2BgpVpwsRteRD.setStatus("current")
_SvcL2BgpVpwsRteNextHopType_Type = InetAddressType
_SvcL2BgpVpwsRteNextHopType_Object = MibTableColumn
svcL2BgpVpwsRteNextHopType = _SvcL2BgpVpwsRteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 147, 1, 3),
    _SvcL2BgpVpwsRteNextHopType_Type()
)
svcL2BgpVpwsRteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2BgpVpwsRteNextHopType.setStatus("current")
_SvcL2BgpVpwsRteNextHop_Type = InetAddress
_SvcL2BgpVpwsRteNextHop_Object = MibTableColumn
svcL2BgpVpwsRteNextHop = _SvcL2BgpVpwsRteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 147, 1, 4),
    _SvcL2BgpVpwsRteNextHop_Type()
)
svcL2BgpVpwsRteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2BgpVpwsRteNextHop.setStatus("current")
_SvcL2BgpVpwsRteSdpBindId_Type = SdpBindId
_SvcL2BgpVpwsRteSdpBindId_Object = MibTableColumn
svcL2BgpVpwsRteSdpBindId = _SvcL2BgpVpwsRteSdpBindId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 147, 1, 5),
    _SvcL2BgpVpwsRteSdpBindId_Type()
)
svcL2BgpVpwsRteSdpBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVpwsRteSdpBindId.setStatus("current")
_SvcL2BgpVpwsRtePwTemplateId_Type = PWTemplateId
_SvcL2BgpVpwsRtePwTemplateId_Object = MibTableColumn
svcL2BgpVpwsRtePwTemplateId = _SvcL2BgpVpwsRtePwTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 147, 1, 6),
    _SvcL2BgpVpwsRtePwTemplateId_Type()
)
svcL2BgpVpwsRtePwTemplateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVpwsRtePwTemplateId.setStatus("current")


class _SvcL2BgpVpwsRteError_Type(DisplayString):
    """Custom type svcL2BgpVpwsRteError based on DisplayString"""
    defaultValue = OctetString("")


_SvcL2BgpVpwsRteError_Type.__name__ = "DisplayString"
_SvcL2BgpVpwsRteError_Object = MibTableColumn
svcL2BgpVpwsRteError = _SvcL2BgpVpwsRteError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 147, 1, 7),
    _SvcL2BgpVpwsRteError_Type()
)
svcL2BgpVpwsRteError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVpwsRteError.setStatus("current")


class _SvcL2BgpVpwsRteLastErrorTime_Type(TimeStamp):
    """Custom type svcL2BgpVpwsRteLastErrorTime based on TimeStamp"""
    defaultValue = 0


_SvcL2BgpVpwsRteLastErrorTime_Type.__name__ = "TimeStamp"
_SvcL2BgpVpwsRteLastErrorTime_Object = MibTableColumn
svcL2BgpVpwsRteLastErrorTime = _SvcL2BgpVpwsRteLastErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 147, 1, 8),
    _SvcL2BgpVpwsRteLastErrorTime_Type()
)
svcL2BgpVpwsRteLastErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVpwsRteLastErrorTime.setStatus("current")
_SvcL2BgpVpwsRteControlWord_Type = Unsigned32
_SvcL2BgpVpwsRteControlWord_Object = MibTableColumn
svcL2BgpVpwsRteControlWord = _SvcL2BgpVpwsRteControlWord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 147, 1, 9),
    _SvcL2BgpVpwsRteControlWord_Type()
)
svcL2BgpVpwsRteControlWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVpwsRteControlWord.setStatus("current")
_SvcL2BgpVpwsRtePathMtu_Type = Integer32
_SvcL2BgpVpwsRtePathMtu_Object = MibTableColumn
svcL2BgpVpwsRtePathMtu = _SvcL2BgpVpwsRtePathMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 147, 1, 10),
    _SvcL2BgpVpwsRtePathMtu_Type()
)
svcL2BgpVpwsRtePathMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVpwsRtePathMtu.setStatus("current")


class _SvcL2BgpVpwsRteState_Type(Integer32):
    """Custom type svcL2BgpVpwsRteState based on Integer32"""
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


_SvcL2BgpVpwsRteState_Type.__name__ = "Integer32"
_SvcL2BgpVpwsRteState_Object = MibTableColumn
svcL2BgpVpwsRteState = _SvcL2BgpVpwsRteState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 147, 1, 11),
    _SvcL2BgpVpwsRteState_Type()
)
svcL2BgpVpwsRteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVpwsRteState.setStatus("current")
_SvcL2BgpVpwsRteSeqDelivery_Type = Unsigned32
_SvcL2BgpVpwsRteSeqDelivery_Object = MibTableColumn
svcL2BgpVpwsRteSeqDelivery = _SvcL2BgpVpwsRteSeqDelivery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 147, 1, 12),
    _SvcL2BgpVpwsRteSeqDelivery_Type()
)
svcL2BgpVpwsRteSeqDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVpwsRteSeqDelivery.setStatus("current")


class _SvcL2BgpVpwsRteStatus_Type(Integer32):
    """Custom type svcL2BgpVpwsRteStatus based on Integer32"""
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


_SvcL2BgpVpwsRteStatus_Type.__name__ = "Integer32"
_SvcL2BgpVpwsRteStatus_Object = MibTableColumn
svcL2BgpVpwsRteStatus = _SvcL2BgpVpwsRteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 147, 1, 13),
    _SvcL2BgpVpwsRteStatus_Type()
)
svcL2BgpVpwsRteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVpwsRteStatus.setStatus("current")
_SvcL2BgpVpwsRteCsv_Type = Unsigned32
_SvcL2BgpVpwsRteCsv_Object = MibTableColumn
svcL2BgpVpwsRteCsv = _SvcL2BgpVpwsRteCsv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 147, 1, 14),
    _SvcL2BgpVpwsRteCsv_Type()
)
svcL2BgpVpwsRteCsv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVpwsRteCsv.setStatus("current")


class _SvcL2BgpVpwsRteTxStatus_Type(Integer32):
    """Custom type svcL2BgpVpwsRteTxStatus based on Integer32"""
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


_SvcL2BgpVpwsRteTxStatus_Type.__name__ = "Integer32"
_SvcL2BgpVpwsRteTxStatus_Object = MibTableColumn
svcL2BgpVpwsRteTxStatus = _SvcL2BgpVpwsRteTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 147, 1, 15),
    _SvcL2BgpVpwsRteTxStatus_Type()
)
svcL2BgpVpwsRteTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVpwsRteTxStatus.setStatus("current")
_SvcL2BgpVpwsRtePreference_Type = Unsigned32
_SvcL2BgpVpwsRtePreference_Object = MibTableColumn
svcL2BgpVpwsRtePreference = _SvcL2BgpVpwsRtePreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 147, 1, 16),
    _SvcL2BgpVpwsRtePreference_Type()
)
svcL2BgpVpwsRtePreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2BgpVpwsRtePreference.setStatus("current")
_TmnxSdpObjs_ObjectIdentity = ObjectIdentity
tmnxSdpObjs = _TmnxSdpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4)
)
_SdpNumEntries_Type = Integer32
_SdpNumEntries_Object = MibScalar
sdpNumEntries = _SdpNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 1),
    _SdpNumEntries_Type()
)
sdpNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpNumEntries.setStatus("current")
_SdpNextFreeId_Type = SdpId
_SdpNextFreeId_Object = MibScalar
sdpNextFreeId = _SdpNextFreeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 2),
    _SdpNextFreeId_Type()
)
sdpNextFreeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpNextFreeId.setStatus("current")
_SdpInfoTable_Object = MibTable
sdpInfoTable = _SdpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3)
)
if mibBuilder.loadTexts:
    sdpInfoTable.setStatus("current")
_SdpInfoEntry_Object = MibTableRow
sdpInfoEntry = _SdpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1)
)
sdpInfoEntry.setIndexNames(
    (0, "TIMETRA-SDP-MIB", "sdpId"),
)
if mibBuilder.loadTexts:
    sdpInfoEntry.setStatus("current")
_SdpId_Type = SdpId
_SdpId_Object = MibTableColumn
sdpId = _SdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 1),
    _SdpId_Type()
)
sdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpId.setStatus("current")
_SdpRowStatus_Type = RowStatus
_SdpRowStatus_Object = MibTableColumn
sdpRowStatus = _SdpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 2),
    _SdpRowStatus_Type()
)
sdpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpRowStatus.setStatus("current")


class _SdpDelivery_Type(Integer32):
    """Custom type sdpDelivery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("mpls", 2),
          ("l2tpv3", 4),
          ("greethbridged", 5))
    )


_SdpDelivery_Type.__name__ = "Integer32"
_SdpDelivery_Object = MibTableColumn
sdpDelivery = _SdpDelivery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 3),
    _SdpDelivery_Type()
)
sdpDelivery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpDelivery.setStatus("current")
_SdpFarEndIpAddress_Type = IpAddress
_SdpFarEndIpAddress_Object = MibTableColumn
sdpFarEndIpAddress = _SdpFarEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 4),
    _SdpFarEndIpAddress_Type()
)
sdpFarEndIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpFarEndIpAddress.setStatus("obsolete")
_SdpLspList_Type = LspIdList
_SdpLspList_Object = MibTableColumn
sdpLspList = _SdpLspList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 5),
    _SdpLspList_Type()
)
sdpLspList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpLspList.setStatus("obsolete")


class _SdpDescription_Type(ServObjDesc):
    """Custom type sdpDescription based on ServObjDesc"""
    defaultValue = OctetString("")


_SdpDescription_Type.__name__ = "ServObjDesc"
_SdpDescription_Object = MibTableColumn
sdpDescription = _SdpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 6),
    _SdpDescription_Type()
)
sdpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpDescription.setStatus("current")


class _SdpLabelSignaling_Type(Integer32):
    """Custom type sdpLabelSignaling based on Integer32"""
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
          ("tldp", 2),
          ("bgp", 3))
    )


_SdpLabelSignaling_Type.__name__ = "Integer32"
_SdpLabelSignaling_Object = MibTableColumn
sdpLabelSignaling = _SdpLabelSignaling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 7),
    _SdpLabelSignaling_Type()
)
sdpLabelSignaling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpLabelSignaling.setStatus("current")


class _SdpAdminStatus_Type(ServiceAdminStatus):
    """Custom type sdpAdminStatus based on ServiceAdminStatus"""
    defaultValue = 2


_SdpAdminStatus_Type.__name__ = "ServiceAdminStatus"
_SdpAdminStatus_Object = MibTableColumn
sdpAdminStatus = _SdpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 8),
    _SdpAdminStatus_Type()
)
sdpAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpAdminStatus.setStatus("current")


class _SdpOperStatus_Type(Integer32):
    """Custom type sdpOperStatus based on Integer32"""
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
        *(("up", 1),
          ("notAlive", 2),
          ("notReady", 3),
          ("invalidEgressInterface", 4),
          ("transportTunnelDown", 5),
          ("down", 6))
    )


_SdpOperStatus_Type.__name__ = "Integer32"
_SdpOperStatus_Object = MibTableColumn
sdpOperStatus = _SdpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 9),
    _SdpOperStatus_Type()
)
sdpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpOperStatus.setStatus("current")


class _SdpAdminPathMtu_Type(Integer32):
    """Custom type sdpAdminPathMtu based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 9782),
    )


_SdpAdminPathMtu_Type.__name__ = "Integer32"
_SdpAdminPathMtu_Object = MibTableColumn
sdpAdminPathMtu = _SdpAdminPathMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 10),
    _SdpAdminPathMtu_Type()
)
sdpAdminPathMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpAdminPathMtu.setStatus("current")
_SdpOperPathMtu_Type = Integer32
_SdpOperPathMtu_Object = MibTableColumn
sdpOperPathMtu = _SdpOperPathMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 11),
    _SdpOperPathMtu_Type()
)
sdpOperPathMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpOperPathMtu.setStatus("current")


class _SdpKeepAliveAdminStatus_Type(TmnxEnabledDisabledAdminState):
    """Custom type sdpKeepAliveAdminStatus based on TmnxEnabledDisabledAdminState"""
    defaultValue = 2


_SdpKeepAliveAdminStatus_Type.__name__ = "TmnxEnabledDisabledAdminState"
_SdpKeepAliveAdminStatus_Object = MibTableColumn
sdpKeepAliveAdminStatus = _SdpKeepAliveAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 12),
    _SdpKeepAliveAdminStatus_Type()
)
sdpKeepAliveAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpKeepAliveAdminStatus.setStatus("current")


class _SdpKeepAliveOperStatus_Type(Integer32):
    """Custom type sdpKeepAliveOperStatus based on Integer32"""
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
        *(("alive", 1),
          ("noResponse", 2),
          ("senderIdInvalid", 3),
          ("responderIdError", 4),
          ("disabled", 5))
    )


_SdpKeepAliveOperStatus_Type.__name__ = "Integer32"
_SdpKeepAliveOperStatus_Object = MibTableColumn
sdpKeepAliveOperStatus = _SdpKeepAliveOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 13),
    _SdpKeepAliveOperStatus_Type()
)
sdpKeepAliveOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpKeepAliveOperStatus.setStatus("current")


class _SdpKeepAliveHelloTime_Type(Integer32):
    """Custom type sdpKeepAliveHelloTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_SdpKeepAliveHelloTime_Type.__name__ = "Integer32"
_SdpKeepAliveHelloTime_Object = MibTableColumn
sdpKeepAliveHelloTime = _SdpKeepAliveHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 14),
    _SdpKeepAliveHelloTime_Type()
)
sdpKeepAliveHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpKeepAliveHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpKeepAliveHelloTime.setUnits("seconds")


class _SdpKeepAliveMaxDropCount_Type(Integer32):
    """Custom type sdpKeepAliveMaxDropCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SdpKeepAliveMaxDropCount_Type.__name__ = "Integer32"
_SdpKeepAliveMaxDropCount_Object = MibTableColumn
sdpKeepAliveMaxDropCount = _SdpKeepAliveMaxDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 15),
    _SdpKeepAliveMaxDropCount_Type()
)
sdpKeepAliveMaxDropCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpKeepAliveMaxDropCount.setStatus("current")


class _SdpKeepAliveHoldDownTime_Type(Integer32):
    """Custom type sdpKeepAliveHoldDownTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_SdpKeepAliveHoldDownTime_Type.__name__ = "Integer32"
_SdpKeepAliveHoldDownTime_Object = MibTableColumn
sdpKeepAliveHoldDownTime = _SdpKeepAliveHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 16),
    _SdpKeepAliveHoldDownTime_Type()
)
sdpKeepAliveHoldDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpKeepAliveHoldDownTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpKeepAliveHoldDownTime.setUnits("seconds")
_SdpLastMgmtChange_Type = TimeStamp
_SdpLastMgmtChange_Object = MibTableColumn
sdpLastMgmtChange = _SdpLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 17),
    _SdpLastMgmtChange_Type()
)
sdpLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpLastMgmtChange.setStatus("current")


class _SdpKeepAliveHelloMessageLength_Type(Integer32):
    """Custom type sdpKeepAliveHelloMessageLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(40, 9198),
    )


_SdpKeepAliveHelloMessageLength_Type.__name__ = "Integer32"
_SdpKeepAliveHelloMessageLength_Object = MibTableColumn
sdpKeepAliveHelloMessageLength = _SdpKeepAliveHelloMessageLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 18),
    _SdpKeepAliveHelloMessageLength_Type()
)
sdpKeepAliveHelloMessageLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpKeepAliveHelloMessageLength.setStatus("current")
_SdpKeepAliveNumHelloRequestMessages_Type = Unsigned32
_SdpKeepAliveNumHelloRequestMessages_Object = MibTableColumn
sdpKeepAliveNumHelloRequestMessages = _SdpKeepAliveNumHelloRequestMessages_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 19),
    _SdpKeepAliveNumHelloRequestMessages_Type()
)
sdpKeepAliveNumHelloRequestMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpKeepAliveNumHelloRequestMessages.setStatus("current")
_SdpKeepAliveNumHelloResponseMessages_Type = Unsigned32
_SdpKeepAliveNumHelloResponseMessages_Object = MibTableColumn
sdpKeepAliveNumHelloResponseMessages = _SdpKeepAliveNumHelloResponseMessages_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 20),
    _SdpKeepAliveNumHelloResponseMessages_Type()
)
sdpKeepAliveNumHelloResponseMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpKeepAliveNumHelloResponseMessages.setStatus("current")
_SdpKeepAliveNumLateHelloResponseMessages_Type = Unsigned32
_SdpKeepAliveNumLateHelloResponseMessages_Object = MibTableColumn
sdpKeepAliveNumLateHelloResponseMessages = _SdpKeepAliveNumLateHelloResponseMessages_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 21),
    _SdpKeepAliveNumLateHelloResponseMessages_Type()
)
sdpKeepAliveNumLateHelloResponseMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpKeepAliveNumLateHelloResponseMessages.setStatus("current")


class _SdpKeepAliveHelloRequestTimeout_Type(Integer32):
    """Custom type sdpKeepAliveHelloRequestTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SdpKeepAliveHelloRequestTimeout_Type.__name__ = "Integer32"
_SdpKeepAliveHelloRequestTimeout_Object = MibTableColumn
sdpKeepAliveHelloRequestTimeout = _SdpKeepAliveHelloRequestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 22),
    _SdpKeepAliveHelloRequestTimeout_Type()
)
sdpKeepAliveHelloRequestTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpKeepAliveHelloRequestTimeout.setStatus("current")
if mibBuilder.loadTexts:
    sdpKeepAliveHelloRequestTimeout.setUnits("seconds")


class _SdpLdpEnabled_Type(TruthValue):
    """Custom type sdpLdpEnabled based on TruthValue"""
    defaultValue = 2


_SdpLdpEnabled_Type.__name__ = "TruthValue"
_SdpLdpEnabled_Object = MibTableColumn
sdpLdpEnabled = _SdpLdpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 23),
    _SdpLdpEnabled_Type()
)
sdpLdpEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpLdpEnabled.setStatus("current")


class _SdpVlanVcEtype_Type(Unsigned32):
    """Custom type sdpVlanVcEtype based on Unsigned32"""
    defaultValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_SdpVlanVcEtype_Type.__name__ = "Unsigned32"
_SdpVlanVcEtype_Object = MibTableColumn
sdpVlanVcEtype = _SdpVlanVcEtype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 24),
    _SdpVlanVcEtype_Type()
)
sdpVlanVcEtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpVlanVcEtype.setStatus("current")


class _SdpAdvertisedVllMtuOverride_Type(TruthValue):
    """Custom type sdpAdvertisedVllMtuOverride based on TruthValue"""
    defaultValue = 2


_SdpAdvertisedVllMtuOverride_Type.__name__ = "TruthValue"
_SdpAdvertisedVllMtuOverride_Object = MibTableColumn
sdpAdvertisedVllMtuOverride = _SdpAdvertisedVllMtuOverride_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 25),
    _SdpAdvertisedVllMtuOverride_Type()
)
sdpAdvertisedVllMtuOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpAdvertisedVllMtuOverride.setStatus("current")


class _SdpOperFlags_Type(Bits):
    """Custom type sdpOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("sdpAdminDown", 0),
          ("signalingSessionDown", 1),
          ("transportTunnelDown", 2),
          ("keepaliveFailure", 3),
          ("invalidEgressInterface", 4),
          ("noSystemIpAddress", 5),
          ("transportTunnelUnstable", 6),
          ("notOnBindingPort", 7))
    )

_SdpOperFlags_Type.__name__ = "Bits"
_SdpOperFlags_Object = MibTableColumn
sdpOperFlags = _SdpOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 26),
    _SdpOperFlags_Type()
)
sdpOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpOperFlags.setStatus("current")
_SdpLastStatusChange_Type = TimeStamp
_SdpLastStatusChange_Object = MibTableColumn
sdpLastStatusChange = _SdpLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 27),
    _SdpLastStatusChange_Type()
)
sdpLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpLastStatusChange.setStatus("current")
_SdpMvplsMgmtService_Type = TmnxServId
_SdpMvplsMgmtService_Object = MibTableColumn
sdpMvplsMgmtService = _SdpMvplsMgmtService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 28),
    _SdpMvplsMgmtService_Type()
)
sdpMvplsMgmtService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpMvplsMgmtService.setStatus("current")
_SdpMvplsMgmtSdpBndId_Type = SdpBindId
_SdpMvplsMgmtSdpBndId_Object = MibTableColumn
sdpMvplsMgmtSdpBndId = _SdpMvplsMgmtSdpBndId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 29),
    _SdpMvplsMgmtSdpBndId_Type()
)
sdpMvplsMgmtSdpBndId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpMvplsMgmtSdpBndId.setStatus("current")


class _SdpCollectAcctStats_Type(TruthValue):
    """Custom type sdpCollectAcctStats based on TruthValue"""
    defaultValue = 2


_SdpCollectAcctStats_Type.__name__ = "TruthValue"
_SdpCollectAcctStats_Object = MibTableColumn
sdpCollectAcctStats = _SdpCollectAcctStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 30),
    _SdpCollectAcctStats_Type()
)
sdpCollectAcctStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpCollectAcctStats.setStatus("current")


class _SdpAccountingPolicyId_Type(Unsigned32):
    """Custom type sdpAccountingPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SdpAccountingPolicyId_Type.__name__ = "Unsigned32"
_SdpAccountingPolicyId_Object = MibTableColumn
sdpAccountingPolicyId = _SdpAccountingPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 31),
    _SdpAccountingPolicyId_Type()
)
sdpAccountingPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpAccountingPolicyId.setStatus("current")


class _SdpClassFwdingEnabled_Type(TmnxAdminStateTruthValue):
    """Custom type sdpClassFwdingEnabled based on TmnxAdminStateTruthValue"""
    defaultValue = 2


_SdpClassFwdingEnabled_Type.__name__ = "TmnxAdminStateTruthValue"
_SdpClassFwdingEnabled_Object = MibTableColumn
sdpClassFwdingEnabled = _SdpClassFwdingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 32),
    _SdpClassFwdingEnabled_Type()
)
sdpClassFwdingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpClassFwdingEnabled.setStatus("current")


class _SdpClassFwdingDefaultLsp_Type(TmnxVRtrMplsLspID):
    """Custom type sdpClassFwdingDefaultLsp based on TmnxVRtrMplsLspID"""
    defaultValue = 0


_SdpClassFwdingDefaultLsp_Type.__name__ = "TmnxVRtrMplsLspID"
_SdpClassFwdingDefaultLsp_Object = MibTableColumn
sdpClassFwdingDefaultLsp = _SdpClassFwdingDefaultLsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 33),
    _SdpClassFwdingDefaultLsp_Type()
)
sdpClassFwdingDefaultLsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpClassFwdingDefaultLsp.setStatus("current")


class _SdpClassFwdingMcLsp_Type(TmnxVRtrMplsLspID):
    """Custom type sdpClassFwdingMcLsp based on TmnxVRtrMplsLspID"""
    defaultValue = 0


_SdpClassFwdingMcLsp_Type.__name__ = "TmnxVRtrMplsLspID"
_SdpClassFwdingMcLsp_Object = MibTableColumn
sdpClassFwdingMcLsp = _SdpClassFwdingMcLsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 34),
    _SdpClassFwdingMcLsp_Type()
)
sdpClassFwdingMcLsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpClassFwdingMcLsp.setStatus("current")


class _SdpMetric_Type(Unsigned32):
    """Custom type sdpMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SdpMetric_Type.__name__ = "Unsigned32"
_SdpMetric_Object = MibTableColumn
sdpMetric = _SdpMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 35),
    _SdpMetric_Type()
)
sdpMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpMetric.setStatus("current")
_SdpAutoSdp_Type = TruthValue
_SdpAutoSdp_Object = MibTableColumn
sdpAutoSdp = _SdpAutoSdp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 36),
    _SdpAutoSdp_Type()
)
sdpAutoSdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAutoSdp.setStatus("current")
_SdpSnmpAllowed_Type = TruthValue
_SdpSnmpAllowed_Object = MibTableColumn
sdpSnmpAllowed = _SdpSnmpAllowed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 37),
    _SdpSnmpAllowed_Type()
)
sdpSnmpAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpSnmpAllowed.setStatus("obsolete")


class _SdpPBBEtype_Type(Unsigned32):
    """Custom type sdpPBBEtype based on Unsigned32"""
    defaultValue = 35047

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_SdpPBBEtype_Type.__name__ = "Unsigned32"
_SdpPBBEtype_Object = MibTableColumn
sdpPBBEtype = _SdpPBBEtype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 38),
    _SdpPBBEtype_Type()
)
sdpPBBEtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPBBEtype.setStatus("current")


class _SdpBandwidthBookingFactor_Type(Unsigned32):
    """Custom type sdpBandwidthBookingFactor based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SdpBandwidthBookingFactor_Type.__name__ = "Unsigned32"
_SdpBandwidthBookingFactor_Object = MibTableColumn
sdpBandwidthBookingFactor = _SdpBandwidthBookingFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 39),
    _SdpBandwidthBookingFactor_Type()
)
sdpBandwidthBookingFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBandwidthBookingFactor.setStatus("current")
_SdpOperBandwidth_Type = Unsigned32
_SdpOperBandwidth_Object = MibTableColumn
sdpOperBandwidth = _SdpOperBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 40),
    _SdpOperBandwidth_Type()
)
sdpOperBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpOperBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    sdpOperBandwidth.setUnits("kilobps")
_SdpAvailableBandwidth_Type = Unsigned32
_SdpAvailableBandwidth_Object = MibTableColumn
sdpAvailableBandwidth = _SdpAvailableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 41),
    _SdpAvailableBandwidth_Type()
)
sdpAvailableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAvailableBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    sdpAvailableBandwidth.setUnits("kilobps")
_SdpMaxBookableBandwidth_Type = Unsigned32
_SdpMaxBookableBandwidth_Object = MibTableColumn
sdpMaxBookableBandwidth = _SdpMaxBookableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 42),
    _SdpMaxBookableBandwidth_Type()
)
sdpMaxBookableBandwidth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sdpMaxBookableBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    sdpMaxBookableBandwidth.setUnits("kilobps")
_SdpBookedBandwidth_Type = Unsigned32
_SdpBookedBandwidth_Object = MibTableColumn
sdpBookedBandwidth = _SdpBookedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 43),
    _SdpBookedBandwidth_Type()
)
sdpBookedBandwidth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sdpBookedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    sdpBookedBandwidth.setUnits("kilobps")
_SdpCreationOrigin_Type = TmnxCreateOrigin
_SdpCreationOrigin_Object = MibTableColumn
sdpCreationOrigin = _SdpCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 44),
    _SdpCreationOrigin_Type()
)
sdpCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpCreationOrigin.setStatus("current")


class _SdpEnforceDiffServLspFc_Type(TruthValue):
    """Custom type sdpEnforceDiffServLspFc based on TruthValue"""
    defaultValue = 2


_SdpEnforceDiffServLspFc_Type.__name__ = "TruthValue"
_SdpEnforceDiffServLspFc_Object = MibTableColumn
sdpEnforceDiffServLspFc = _SdpEnforceDiffServLspFc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 45),
    _SdpEnforceDiffServLspFc_Type()
)
sdpEnforceDiffServLspFc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpEnforceDiffServLspFc.setStatus("current")


class _SdpMixedLspModeEnabled_Type(TruthValue):
    """Custom type sdpMixedLspModeEnabled based on TruthValue"""
    defaultValue = 2


_SdpMixedLspModeEnabled_Type.__name__ = "TruthValue"
_SdpMixedLspModeEnabled_Object = MibTableColumn
sdpMixedLspModeEnabled = _SdpMixedLspModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 46),
    _SdpMixedLspModeEnabled_Type()
)
sdpMixedLspModeEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpMixedLspModeEnabled.setStatus("current")


class _SdpLspRevertTime_Type(Integer32):
    """Custom type sdpLspRevertTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 600),
    )


_SdpLspRevertTime_Type.__name__ = "Integer32"
_SdpLspRevertTime_Object = MibTableColumn
sdpLspRevertTime = _SdpLspRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 47),
    _SdpLspRevertTime_Type()
)
sdpLspRevertTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpLspRevertTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpLspRevertTime.setUnits("seconds")


class _SdpLspRevertTimeCountDown_Type(Integer32):
    """Custom type sdpLspRevertTimeCountDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 600),
    )


_SdpLspRevertTimeCountDown_Type.__name__ = "Integer32"
_SdpLspRevertTimeCountDown_Object = MibTableColumn
sdpLspRevertTimeCountDown = _SdpLspRevertTimeCountDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 48),
    _SdpLspRevertTimeCountDown_Type()
)
sdpLspRevertTimeCountDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpLspRevertTimeCountDown.setStatus("current")
if mibBuilder.loadTexts:
    sdpLspRevertTimeCountDown.setUnits("seconds")
_SdpLdpLspId_Type = Unsigned32
_SdpLdpLspId_Object = MibTableColumn
sdpLdpLspId = _SdpLdpLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 49),
    _SdpLdpLspId_Type()
)
sdpLdpLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpLdpLspId.setStatus("current")
_SdpLdpActive_Type = TruthValue
_SdpLdpActive_Object = MibTableColumn
sdpLdpActive = _SdpLdpActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 50),
    _SdpLdpActive_Type()
)
sdpLdpActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpLdpActive.setStatus("obsolete")


class _SdpNetDomainName_Type(TNamedItemOrEmpty):
    """Custom type sdpNetDomainName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("default")


_SdpNetDomainName_Type.__name__ = "TNamedItemOrEmpty"
_SdpNetDomainName_Object = MibTableColumn
sdpNetDomainName = _SdpNetDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 51),
    _SdpNetDomainName_Type()
)
sdpNetDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpNetDomainName.setStatus("current")


class _SdpEgressIfsNetDomainConsistent_Type(Integer32):
    """Custom type sdpEgressIfsNetDomainConsistent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("consistent", 2),
          ("inconsistent", 3))
    )


_SdpEgressIfsNetDomainConsistent_Type.__name__ = "Integer32"
_SdpEgressIfsNetDomainConsistent_Object = MibTableColumn
sdpEgressIfsNetDomainConsistent = _SdpEgressIfsNetDomainConsistent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 52),
    _SdpEgressIfsNetDomainConsistent_Type()
)
sdpEgressIfsNetDomainConsistent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpEgressIfsNetDomainConsistent.setStatus("current")


class _SdpBgpTunnelEnabled_Type(TruthValue):
    """Custom type sdpBgpTunnelEnabled based on TruthValue"""
    defaultValue = 2


_SdpBgpTunnelEnabled_Type.__name__ = "TruthValue"
_SdpBgpTunnelEnabled_Object = MibTableColumn
sdpBgpTunnelEnabled = _SdpBgpTunnelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 53),
    _SdpBgpTunnelEnabled_Type()
)
sdpBgpTunnelEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBgpTunnelEnabled.setStatus("current")
_SdpBgpTunnelLspId_Type = Unsigned32
_SdpBgpTunnelLspId_Object = MibTableColumn
sdpBgpTunnelLspId = _SdpBgpTunnelLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 54),
    _SdpBgpTunnelLspId_Type()
)
sdpBgpTunnelLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBgpTunnelLspId.setStatus("current")
_SdpTunnelFarEndIpAddress_Type = IpAddress
_SdpTunnelFarEndIpAddress_Object = MibTableColumn
sdpTunnelFarEndIpAddress = _SdpTunnelFarEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 55),
    _SdpTunnelFarEndIpAddress_Type()
)
sdpTunnelFarEndIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpTunnelFarEndIpAddress.setStatus("obsolete")


class _SdpActiveLspType_Type(Integer32):
    """Custom type sdpActiveLspType based on Integer32"""
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
        *(("not-applicable", 0),
          ("rsvp", 1),
          ("ldp", 2),
          ("bgp", 3),
          ("none", 4),
          ("mplsTp", 5),
          ("srIsis", 6),
          ("srOspf", 7),
          ("srTeLsp", 8),
          ("fpe", 9))
    )


_SdpActiveLspType_Type.__name__ = "Integer32"
_SdpActiveLspType_Object = MibTableColumn
sdpActiveLspType = _SdpActiveLspType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 56),
    _SdpActiveLspType_Type()
)
sdpActiveLspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpActiveLspType.setStatus("current")


class _SdpBindingPort_Type(TmnxPortID):
    """Custom type sdpBindingPort based on TmnxPortID"""
    defaultValue = 503316480


_SdpBindingPort_Type.__name__ = "TmnxPortID"
_SdpBindingPort_Object = MibTableColumn
sdpBindingPort = _SdpBindingPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 57),
    _SdpBindingPort_Type()
)
sdpBindingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindingPort.setStatus("current")


class _SdpFarEndNodeId_Type(TmnxMplsTpNodeID):
    """Custom type sdpFarEndNodeId based on TmnxMplsTpNodeID"""
    defaultValue = 0


_SdpFarEndNodeId_Type.__name__ = "TmnxMplsTpNodeID"
_SdpFarEndNodeId_Object = MibTableColumn
sdpFarEndNodeId = _SdpFarEndNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 58),
    _SdpFarEndNodeId_Type()
)
sdpFarEndNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpFarEndNodeId.setStatus("current")


class _SdpFarEndGlobalId_Type(TmnxMplsTpGlobalID):
    """Custom type sdpFarEndGlobalId based on TmnxMplsTpGlobalID"""
    defaultValue = 0


_SdpFarEndGlobalId_Type.__name__ = "TmnxMplsTpGlobalID"
_SdpFarEndGlobalId_Object = MibTableColumn
sdpFarEndGlobalId = _SdpFarEndGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 59),
    _SdpFarEndGlobalId_Type()
)
sdpFarEndGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpFarEndGlobalId.setStatus("current")


class _SdpFarEndInetAddressType_Type(InetAddressType):
    """Custom type sdpFarEndInetAddressType based on InetAddressType"""
    defaultValue = 0


_SdpFarEndInetAddressType_Type.__name__ = "InetAddressType"
_SdpFarEndInetAddressType_Object = MibTableColumn
sdpFarEndInetAddressType = _SdpFarEndInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 60),
    _SdpFarEndInetAddressType_Type()
)
sdpFarEndInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpFarEndInetAddressType.setStatus("current")


class _SdpFarEndInetAddress_Type(InetAddress):
    """Custom type sdpFarEndInetAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SdpFarEndInetAddress_Type.__name__ = "InetAddress"
_SdpFarEndInetAddress_Object = MibTableColumn
sdpFarEndInetAddress = _SdpFarEndInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 61),
    _SdpFarEndInetAddress_Type()
)
sdpFarEndInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpFarEndInetAddress.setStatus("current")


class _SdpLocalEndInetAddressType_Type(InetAddressType):
    """Custom type sdpLocalEndInetAddressType based on InetAddressType"""
    defaultValue = 0


_SdpLocalEndInetAddressType_Type.__name__ = "InetAddressType"
_SdpLocalEndInetAddressType_Object = MibTableColumn
sdpLocalEndInetAddressType = _SdpLocalEndInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 62),
    _SdpLocalEndInetAddressType_Type()
)
sdpLocalEndInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpLocalEndInetAddressType.setStatus("current")


class _SdpLocalEndInetAddress_Type(InetAddress):
    """Custom type sdpLocalEndInetAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SdpLocalEndInetAddress_Type.__name__ = "InetAddress"
_SdpLocalEndInetAddress_Object = MibTableColumn
sdpLocalEndInetAddress = _SdpLocalEndInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 63),
    _SdpLocalEndInetAddress_Type()
)
sdpLocalEndInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpLocalEndInetAddress.setStatus("current")


class _SdpSourceBMacLSB_Type(Unsigned32):
    """Custom type sdpSourceBMacLSB based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_SdpSourceBMacLSB_Type.__name__ = "Unsigned32"
_SdpSourceBMacLSB_Object = MibTableColumn
sdpSourceBMacLSB = _SdpSourceBMacLSB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 64),
    _SdpSourceBMacLSB_Type()
)
sdpSourceBMacLSB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpSourceBMacLSB.setStatus("current")


class _SdpControlPWVCId_Type(TmnxVcIdOrNone):
    """Custom type sdpControlPWVCId based on TmnxVcIdOrNone"""
    defaultValue = 0


_SdpControlPWVCId_Type.__name__ = "TmnxVcIdOrNone"
_SdpControlPWVCId_Object = MibTableColumn
sdpControlPWVCId = _SdpControlPWVCId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 65),
    _SdpControlPWVCId_Type()
)
sdpControlPWVCId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpControlPWVCId.setStatus("current")
_SdpControlPWIsActive_Type = TruthValue
_SdpControlPWIsActive_Object = MibTableColumn
sdpControlPWIsActive = _SdpControlPWIsActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 66),
    _SdpControlPWIsActive_Type()
)
sdpControlPWIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpControlPWIsActive.setStatus("current")


class _SdpTunnelFarEndInetAddressType_Type(InetAddressType):
    """Custom type sdpTunnelFarEndInetAddressType based on InetAddressType"""
    defaultValue = 0


_SdpTunnelFarEndInetAddressType_Type.__name__ = "InetAddressType"
_SdpTunnelFarEndInetAddressType_Object = MibTableColumn
sdpTunnelFarEndInetAddressType = _SdpTunnelFarEndInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 67),
    _SdpTunnelFarEndInetAddressType_Type()
)
sdpTunnelFarEndInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpTunnelFarEndInetAddressType.setStatus("current")


class _SdpTunnelFarEndInetAddress_Type(InetAddress):
    """Custom type sdpTunnelFarEndInetAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SdpTunnelFarEndInetAddress_Type.__name__ = "InetAddress"
_SdpTunnelFarEndInetAddress_Object = MibTableColumn
sdpTunnelFarEndInetAddress = _SdpTunnelFarEndInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 68),
    _SdpTunnelFarEndInetAddress_Type()
)
sdpTunnelFarEndInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpTunnelFarEndInetAddress.setStatus("current")


class _SdpGreAllowFragmentation_Type(TruthValue):
    """Custom type sdpGreAllowFragmentation based on TruthValue"""
    defaultValue = 2


_SdpGreAllowFragmentation_Type.__name__ = "TruthValue"
_SdpGreAllowFragmentation_Object = MibTableColumn
sdpGreAllowFragmentation = _SdpGreAllowFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 69),
    _SdpGreAllowFragmentation_Type()
)
sdpGreAllowFragmentation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpGreAllowFragmentation.setStatus("current")
_SdpFpeLspId_Type = Unsigned32
_SdpFpeLspId_Object = MibTableColumn
sdpFpeLspId = _SdpFpeLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 70),
    _SdpFpeLspId_Type()
)
sdpFpeLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpFpeLspId.setStatus("current")


class _SdpWeightedEcmpEnabled_Type(TruthValue):
    """Custom type sdpWeightedEcmpEnabled based on TruthValue"""
    defaultValue = 2


_SdpWeightedEcmpEnabled_Type.__name__ = "TruthValue"
_SdpWeightedEcmpEnabled_Object = MibTableColumn
sdpWeightedEcmpEnabled = _SdpWeightedEcmpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 71),
    _SdpWeightedEcmpEnabled_Type()
)
sdpWeightedEcmpEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpWeightedEcmpEnabled.setStatus("current")
_SdpOperTunnelFarEndInetAddrType_Type = InetAddressType
_SdpOperTunnelFarEndInetAddrType_Object = MibTableColumn
sdpOperTunnelFarEndInetAddrType = _SdpOperTunnelFarEndInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 72),
    _SdpOperTunnelFarEndInetAddrType_Type()
)
sdpOperTunnelFarEndInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpOperTunnelFarEndInetAddrType.setStatus("current")


class _SdpOperTunnelFarEndInetAddr_Type(InetAddress):
    """Custom type sdpOperTunnelFarEndInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SdpOperTunnelFarEndInetAddr_Type.__name__ = "InetAddress"
_SdpOperTunnelFarEndInetAddr_Object = MibTableColumn
sdpOperTunnelFarEndInetAddr = _SdpOperTunnelFarEndInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 73),
    _SdpOperTunnelFarEndInetAddr_Type()
)
sdpOperTunnelFarEndInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpOperTunnelFarEndInetAddr.setStatus("current")
_SdpBindTable_Object = MibTable
sdpBindTable = _SdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4)
)
if mibBuilder.loadTexts:
    sdpBindTable.setStatus("current")
_SdpBindEntry_Object = MibTableRow
sdpBindEntry = _SdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1)
)
sdpBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindEntry.setStatus("current")
_SdpBindId_Type = SdpBindId
_SdpBindId_Object = MibTableColumn
sdpBindId = _SdpBindId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 1),
    _SdpBindId_Type()
)
sdpBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindId.setStatus("current")
_SdpBindRowStatus_Type = RowStatus
_SdpBindRowStatus_Object = MibTableColumn
sdpBindRowStatus = _SdpBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 2),
    _SdpBindRowStatus_Type()
)
sdpBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindRowStatus.setStatus("current")


class _SdpBindAdminIngressLabel_Type(Unsigned32):
    """Custom type sdpBindAdminIngressLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1048575),
    )


_SdpBindAdminIngressLabel_Type.__name__ = "Unsigned32"
_SdpBindAdminIngressLabel_Object = MibTableColumn
sdpBindAdminIngressLabel = _SdpBindAdminIngressLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 3),
    _SdpBindAdminIngressLabel_Type()
)
sdpBindAdminIngressLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAdminIngressLabel.setStatus("current")


class _SdpBindAdminEgressLabel_Type(Unsigned32):
    """Custom type sdpBindAdminEgressLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1048575),
    )


_SdpBindAdminEgressLabel_Type.__name__ = "Unsigned32"
_SdpBindAdminEgressLabel_Object = MibTableColumn
sdpBindAdminEgressLabel = _SdpBindAdminEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 4),
    _SdpBindAdminEgressLabel_Type()
)
sdpBindAdminEgressLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAdminEgressLabel.setStatus("current")


class _SdpBindOperIngressLabel_Type(Unsigned32):
    """Custom type sdpBindOperIngressLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1048575),
    )


_SdpBindOperIngressLabel_Type.__name__ = "Unsigned32"
_SdpBindOperIngressLabel_Object = MibTableColumn
sdpBindOperIngressLabel = _SdpBindOperIngressLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 5),
    _SdpBindOperIngressLabel_Type()
)
sdpBindOperIngressLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperIngressLabel.setStatus("current")


class _SdpBindOperEgressLabel_Type(Unsigned32):
    """Custom type sdpBindOperEgressLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1048575),
    )


_SdpBindOperEgressLabel_Type.__name__ = "Unsigned32"
_SdpBindOperEgressLabel_Object = MibTableColumn
sdpBindOperEgressLabel = _SdpBindOperEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 6),
    _SdpBindOperEgressLabel_Type()
)
sdpBindOperEgressLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperEgressLabel.setStatus("current")


class _SdpBindAdminStatus_Type(ServiceAdminStatus):
    """Custom type sdpBindAdminStatus based on ServiceAdminStatus"""
    defaultValue = 1


_SdpBindAdminStatus_Type.__name__ = "ServiceAdminStatus"
_SdpBindAdminStatus_Object = MibTableColumn
sdpBindAdminStatus = _SdpBindAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 7),
    _SdpBindAdminStatus_Type()
)
sdpBindAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAdminStatus.setStatus("current")


class _SdpBindOperStatus_Type(Integer32):
    """Custom type sdpBindOperStatus based on Integer32"""
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
        *(("up", 1),
          ("noEgressLabel", 2),
          ("noIngressLabel", 3),
          ("noLabels", 4),
          ("down", 5),
          ("svcMtuMismatch", 6),
          ("sdpPathMtuTooSmall", 7),
          ("sdpNotReady", 8),
          ("sdpDown", 9),
          ("sapDown", 10))
    )


_SdpBindOperStatus_Type.__name__ = "Integer32"
_SdpBindOperStatus_Object = MibTableColumn
sdpBindOperStatus = _SdpBindOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 8),
    _SdpBindOperStatus_Type()
)
sdpBindOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperStatus.setStatus("current")
_SdpBindLastMgmtChange_Type = TimeStamp
_SdpBindLastMgmtChange_Object = MibTableColumn
sdpBindLastMgmtChange = _SdpBindLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 9),
    _SdpBindLastMgmtChange_Type()
)
sdpBindLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindLastMgmtChange.setStatus("current")


class _SdpBindType_Type(Integer32):
    """Custom type sdpBindType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("spoke", 1),
          ("mesh", 2))
    )


_SdpBindType_Type.__name__ = "Integer32"
_SdpBindType_Object = MibTableColumn
sdpBindType = _SdpBindType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 10),
    _SdpBindType_Type()
)
sdpBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindType.setStatus("current")


class _SdpBindIngressMacFilterId_Type(TConfigOrVsdFilterID):
    """Custom type sdpBindIngressMacFilterId based on TConfigOrVsdFilterID"""
    defaultValue = 0


_SdpBindIngressMacFilterId_Type.__name__ = "TConfigOrVsdFilterID"
_SdpBindIngressMacFilterId_Object = MibTableColumn
sdpBindIngressMacFilterId = _SdpBindIngressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 11),
    _SdpBindIngressMacFilterId_Type()
)
sdpBindIngressMacFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressMacFilterId.setStatus("current")


class _SdpBindIngressIpFilterId_Type(TConfigOrVsdFilterID):
    """Custom type sdpBindIngressIpFilterId based on TConfigOrVsdFilterID"""
    defaultValue = 0


_SdpBindIngressIpFilterId_Type.__name__ = "TConfigOrVsdFilterID"
_SdpBindIngressIpFilterId_Object = MibTableColumn
sdpBindIngressIpFilterId = _SdpBindIngressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 12),
    _SdpBindIngressIpFilterId_Type()
)
sdpBindIngressIpFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressIpFilterId.setStatus("current")


class _SdpBindEgressMacFilterId_Type(TFilterID):
    """Custom type sdpBindEgressMacFilterId based on TFilterID"""
    defaultValue = 0


_SdpBindEgressMacFilterId_Type.__name__ = "TFilterID"
_SdpBindEgressMacFilterId_Object = MibTableColumn
sdpBindEgressMacFilterId = _SdpBindEgressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 13),
    _SdpBindEgressMacFilterId_Type()
)
sdpBindEgressMacFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEgressMacFilterId.setStatus("current")


class _SdpBindEgressIpFilterId_Type(TFilterID):
    """Custom type sdpBindEgressIpFilterId based on TFilterID"""
    defaultValue = 0


_SdpBindEgressIpFilterId_Type.__name__ = "TFilterID"
_SdpBindEgressIpFilterId_Object = MibTableColumn
sdpBindEgressIpFilterId = _SdpBindEgressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 14),
    _SdpBindEgressIpFilterId_Type()
)
sdpBindEgressIpFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEgressIpFilterId.setStatus("current")
_SdpBindVpnId_Type = VpnId
_SdpBindVpnId_Object = MibTableColumn
sdpBindVpnId = _SdpBindVpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 15),
    _SdpBindVpnId_Type()
)
sdpBindVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindVpnId.setStatus("current")
_SdpBindCustId_Type = TmnxCustId
_SdpBindCustId_Object = MibTableColumn
sdpBindCustId = _SdpBindCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 16),
    _SdpBindCustId_Type()
)
sdpBindCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCustId.setStatus("current")
_SdpBindVcType_Type = SdpBindVcType
_SdpBindVcType_Object = MibTableColumn
sdpBindVcType = _SdpBindVcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 17),
    _SdpBindVcType_Type()
)
sdpBindVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindVcType.setStatus("current")


class _SdpBindVlanVcTag_Type(Unsigned32):
    """Custom type sdpBindVlanVcTag based on Unsigned32"""
    defaultValue = 4095

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SdpBindVlanVcTag_Type.__name__ = "Unsigned32"
_SdpBindVlanVcTag_Object = MibTableColumn
sdpBindVlanVcTag = _SdpBindVlanVcTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 18),
    _SdpBindVlanVcTag_Type()
)
sdpBindVlanVcTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindVlanVcTag.setStatus("current")


class _SdpBindSplitHorizonGrp_Type(ServObjName):
    """Custom type sdpBindSplitHorizonGrp based on ServObjName"""
    defaultValue = OctetString("")


_SdpBindSplitHorizonGrp_Type.__name__ = "ServObjName"
_SdpBindSplitHorizonGrp_Object = MibTableColumn
sdpBindSplitHorizonGrp = _SdpBindSplitHorizonGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 19),
    _SdpBindSplitHorizonGrp_Type()
)
sdpBindSplitHorizonGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindSplitHorizonGrp.setStatus("current")


class _SdpBindOperFlags_Type(Bits):
    """Custom type sdpBindOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("sdpBindAdminDown", 0),
          ("svcAdminDown", 1),
          ("stitchingSvcTxDown", 2),
          ("sdpOperDown", 3),
          ("sdpPathMtuTooSmall", 4),
          ("noIngressVcLabel", 5),
          ("noEgressVcLabel", 6),
          ("svcMtuMismatch", 7),
          ("vcTypeMismatch", 8),
          ("relearnLimitExceeded", 9),
          ("iesIfAdminDown", 10),
          ("releasedIngressVcLabel", 11),
          ("labelsExhausted", 12),
          ("svcParamMismatch", 13),
          ("insufficientBandwidth", 14),
          ("pwPeerFaultStatusBits", 15),
          ("meshSdpDown", 16),
          ("notManagedByMcRing", 17),
          ("outOfResource", 18),
          ("mhStandby", 19),
          ("oamDownMepFault", 20),
          ("oamUpMepFault", 21),
          ("standbySigSlaveTxDown", 22),
          ("operGrpDown", 23),
          ("withdrawnIngressVcLabel", 24),
          ("vplsPmsiDown", 25),
          ("recProtSrcMac", 26),
          ("peerFaultStatusTxDown", 27),
          ("evpnRouteConflict", 28),
          ("adminLocked", 29),
          ("evpnP2mpConflict", 30),
          ("labelStackLimitExceeded", 31),
          ("vccvBfdDown", 32),
          ("stitchingSvcPwFault", 33))
    )

_SdpBindOperFlags_Type.__name__ = "Bits"
_SdpBindOperFlags_Object = MibTableColumn
sdpBindOperFlags = _SdpBindOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 20),
    _SdpBindOperFlags_Type()
)
sdpBindOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperFlags.setStatus("current")
_SdpBindLastStatusChange_Type = TimeStamp
_SdpBindLastStatusChange_Object = MibTableColumn
sdpBindLastStatusChange = _SdpBindLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 21),
    _SdpBindLastStatusChange_Type()
)
sdpBindLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindLastStatusChange.setStatus("current")
_SdpBindIesIfIndex_Type = InterfaceIndexOrZero
_SdpBindIesIfIndex_Object = MibTableColumn
sdpBindIesIfIndex = _SdpBindIesIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 22),
    _SdpBindIesIfIndex_Type()
)
sdpBindIesIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIesIfIndex.setStatus("current")
_SdpBindMacPinning_Type = TmnxEnabledDisabled
_SdpBindMacPinning_Object = MibTableColumn
sdpBindMacPinning = _SdpBindMacPinning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 23),
    _SdpBindMacPinning_Type()
)
sdpBindMacPinning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindMacPinning.setStatus("current")


class _SdpBindIngressIpv6FilterId_Type(TConfigOrVsdFilterID):
    """Custom type sdpBindIngressIpv6FilterId based on TConfigOrVsdFilterID"""
    defaultValue = 0


_SdpBindIngressIpv6FilterId_Type.__name__ = "TConfigOrVsdFilterID"
_SdpBindIngressIpv6FilterId_Object = MibTableColumn
sdpBindIngressIpv6FilterId = _SdpBindIngressIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 24),
    _SdpBindIngressIpv6FilterId_Type()
)
sdpBindIngressIpv6FilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressIpv6FilterId.setStatus("current")


class _SdpBindEgressIpv6FilterId_Type(TFilterID):
    """Custom type sdpBindEgressIpv6FilterId based on TFilterID"""
    defaultValue = 0


_SdpBindEgressIpv6FilterId_Type.__name__ = "TFilterID"
_SdpBindEgressIpv6FilterId_Object = MibTableColumn
sdpBindEgressIpv6FilterId = _SdpBindEgressIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 25),
    _SdpBindEgressIpv6FilterId_Type()
)
sdpBindEgressIpv6FilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEgressIpv6FilterId.setStatus("current")


class _SdpBindCollectAcctStats_Type(TruthValue):
    """Custom type sdpBindCollectAcctStats based on TruthValue"""
    defaultValue = 2


_SdpBindCollectAcctStats_Type.__name__ = "TruthValue"
_SdpBindCollectAcctStats_Object = MibTableColumn
sdpBindCollectAcctStats = _SdpBindCollectAcctStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 26),
    _SdpBindCollectAcctStats_Type()
)
sdpBindCollectAcctStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindCollectAcctStats.setStatus("current")


class _SdpBindAccountingPolicyId_Type(Unsigned32):
    """Custom type sdpBindAccountingPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SdpBindAccountingPolicyId_Type.__name__ = "Unsigned32"
_SdpBindAccountingPolicyId_Object = MibTableColumn
sdpBindAccountingPolicyId = _SdpBindAccountingPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 27),
    _SdpBindAccountingPolicyId_Type()
)
sdpBindAccountingPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAccountingPolicyId.setStatus("current")


class _SdpBindPwPeerStatusBits_Type(Bits):
    """Custom type sdpBindPwPeerStatusBits based on Bits"""
    namedValues = NamedValues(
        *(("pwNotForwarding", 0),
          ("lacIngressFault", 1),
          ("lacEgresssFault", 2),
          ("psnIngressFault", 3),
          ("psnEgressFault", 4),
          ("pwFwdingStandby", 5))
    )

_SdpBindPwPeerStatusBits_Type.__name__ = "Bits"
_SdpBindPwPeerStatusBits_Object = MibTableColumn
sdpBindPwPeerStatusBits = _SdpBindPwPeerStatusBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 28),
    _SdpBindPwPeerStatusBits_Type()
)
sdpBindPwPeerStatusBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPwPeerStatusBits.setStatus("current")


class _SdpBindPeerVccvCvBits_Type(Bits):
    """Custom type sdpBindPeerVccvCvBits based on Bits"""
    namedValues = NamedValues(
        *(("icmpPing", 0),
          ("lspPing", 1),
          ("bfdFaultDetection", 2),
          ("bfdFaultDetectionAndSignalling", 3))
    )

_SdpBindPeerVccvCvBits_Type.__name__ = "Bits"
_SdpBindPeerVccvCvBits_Object = MibTableColumn
sdpBindPeerVccvCvBits = _SdpBindPeerVccvCvBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 29),
    _SdpBindPeerVccvCvBits_Type()
)
sdpBindPeerVccvCvBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPeerVccvCvBits.setStatus("current")


class _SdpBindPeerVccvCcBits_Type(Bits):
    """Custom type sdpBindPeerVccvCcBits based on Bits"""
    namedValues = NamedValues(
        *(("pwe3ControlWord", 0),
          ("mplsRouterAlertLabel", 1),
          ("mplsPwDemultiplexorLabel", 2))
    )

_SdpBindPeerVccvCcBits_Type.__name__ = "Bits"
_SdpBindPeerVccvCcBits_Object = MibTableColumn
sdpBindPeerVccvCcBits = _SdpBindPeerVccvCcBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 30),
    _SdpBindPeerVccvCcBits_Type()
)
sdpBindPeerVccvCcBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPeerVccvCcBits.setStatus("current")
_SdpBindControlWordBit_Type = TruthValue
_SdpBindControlWordBit_Object = MibTableColumn
sdpBindControlWordBit = _SdpBindControlWordBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 31),
    _SdpBindControlWordBit_Type()
)
sdpBindControlWordBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindControlWordBit.setStatus("current")
_SdpBindOperControlWord_Type = TruthValue
_SdpBindOperControlWord_Object = MibTableColumn
sdpBindOperControlWord = _SdpBindOperControlWord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 32),
    _SdpBindOperControlWord_Type()
)
sdpBindOperControlWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperControlWord.setStatus("current")


class _SdpBindEndPoint_Type(ServObjName):
    """Custom type sdpBindEndPoint based on ServObjName"""
    defaultValue = OctetString("")


_SdpBindEndPoint_Type.__name__ = "ServObjName"
_SdpBindEndPoint_Object = MibTableColumn
sdpBindEndPoint = _SdpBindEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 33),
    _SdpBindEndPoint_Type()
)
sdpBindEndPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEndPoint.setStatus("current")


class _SdpBindEndPointPrecedence_Type(Unsigned32):
    """Custom type sdpBindEndPointPrecedence based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SdpBindEndPointPrecedence_Type.__name__ = "Unsigned32"
_SdpBindEndPointPrecedence_Object = MibTableColumn
sdpBindEndPointPrecedence = _SdpBindEndPointPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 34),
    _SdpBindEndPointPrecedence_Type()
)
sdpBindEndPointPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEndPointPrecedence.setStatus("current")


class _SdpBindIsICB_Type(TruthValue):
    """Custom type sdpBindIsICB based on TruthValue"""
    defaultValue = 2


_SdpBindIsICB_Type.__name__ = "TruthValue"
_SdpBindIsICB_Object = MibTableColumn
sdpBindIsICB = _SdpBindIsICB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 35),
    _SdpBindIsICB_Type()
)
sdpBindIsICB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIsICB.setStatus("current")
_SdpBindPwFaultInetAddressType_Type = InetAddressType
_SdpBindPwFaultInetAddressType_Object = MibTableColumn
sdpBindPwFaultInetAddressType = _SdpBindPwFaultInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 36),
    _SdpBindPwFaultInetAddressType_Type()
)
sdpBindPwFaultInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPwFaultInetAddressType.setStatus("current")


class _SdpBindPwFaultInetAddress_Type(InetAddress):
    """Custom type sdpBindPwFaultInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SdpBindPwFaultInetAddress_Type.__name__ = "InetAddress"
_SdpBindPwFaultInetAddress_Object = MibTableColumn
sdpBindPwFaultInetAddress = _SdpBindPwFaultInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 37),
    _SdpBindPwFaultInetAddress_Type()
)
sdpBindPwFaultInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPwFaultInetAddress.setStatus("current")
_SdpBindClassFwdingOperState_Type = TmnxOperState
_SdpBindClassFwdingOperState_Object = MibTableColumn
sdpBindClassFwdingOperState = _SdpBindClassFwdingOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 38),
    _SdpBindClassFwdingOperState_Type()
)
sdpBindClassFwdingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindClassFwdingOperState.setStatus("current")


class _SdpBindForceVlanVcForwarding_Type(TruthValue):
    """Custom type sdpBindForceVlanVcForwarding based on TruthValue"""
    defaultValue = 2


_SdpBindForceVlanVcForwarding_Type.__name__ = "TruthValue"
_SdpBindForceVlanVcForwarding_Object = MibTableColumn
sdpBindForceVlanVcForwarding = _SdpBindForceVlanVcForwarding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 39),
    _SdpBindForceVlanVcForwarding_Type()
)
sdpBindForceVlanVcForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindForceVlanVcForwarding.setStatus("current")


class _SdpBindAdminBandwidth_Type(SdpBindBandwidth):
    """Custom type sdpBindAdminBandwidth based on SdpBindBandwidth"""
    defaultValue = 0


_SdpBindAdminBandwidth_Type.__name__ = "SdpBindBandwidth"
_SdpBindAdminBandwidth_Object = MibTableColumn
sdpBindAdminBandwidth = _SdpBindAdminBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 40),
    _SdpBindAdminBandwidth_Type()
)
sdpBindAdminBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAdminBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindAdminBandwidth.setUnits("kilobps")
_SdpBindOperBandwidth_Type = SdpBindBandwidth
_SdpBindOperBandwidth_Object = MibTableColumn
sdpBindOperBandwidth = _SdpBindOperBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 41),
    _SdpBindOperBandwidth_Type()
)
sdpBindOperBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindOperBandwidth.setUnits("kilobps")
_SdpBindCreationOrigin_Type = TmnxCreateOrigin
_SdpBindCreationOrigin_Object = MibTableColumn
sdpBindCreationOrigin = _SdpBindCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 42),
    _SdpBindCreationOrigin_Type()
)
sdpBindCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCreationOrigin.setStatus("current")


class _SdpBindDescription_Type(TItemDescription):
    """Custom type sdpBindDescription based on TItemDescription"""
    defaultValue = OctetString("")


_SdpBindDescription_Type.__name__ = "TItemDescription"
_SdpBindDescription_Object = MibTableColumn
sdpBindDescription = _SdpBindDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 43),
    _SdpBindDescription_Type()
)
sdpBindDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindDescription.setStatus("current")
_SdpBindSiteName_Type = TNamedItemOrEmpty
_SdpBindSiteName_Object = MibTableColumn
sdpBindSiteName = _SdpBindSiteName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 44),
    _SdpBindSiteName_Type()
)
sdpBindSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindSiteName.setStatus("current")


class _SdpBindHashLabel_Type(TruthValue):
    """Custom type sdpBindHashLabel based on TruthValue"""
    defaultValue = 2


_SdpBindHashLabel_Type.__name__ = "TruthValue"
_SdpBindHashLabel_Object = MibTableColumn
sdpBindHashLabel = _SdpBindHashLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 45),
    _SdpBindHashLabel_Type()
)
sdpBindHashLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindHashLabel.setStatus("current")


class _SdpBindIsaAaApplicationProfile_Type(ServObjName):
    """Custom type sdpBindIsaAaApplicationProfile based on ServObjName"""
    defaultValue = OctetString("")


_SdpBindIsaAaApplicationProfile_Type.__name__ = "ServObjName"
_SdpBindIsaAaApplicationProfile_Object = MibTableColumn
sdpBindIsaAaApplicationProfile = _SdpBindIsaAaApplicationProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 46),
    _SdpBindIsaAaApplicationProfile_Type()
)
sdpBindIsaAaApplicationProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIsaAaApplicationProfile.setStatus("current")


class _SdpBindStandbySigSlave_Type(TruthValue):
    """Custom type sdpBindStandbySigSlave based on TruthValue"""
    defaultValue = 2


_SdpBindStandbySigSlave_Type.__name__ = "TruthValue"
_SdpBindStandbySigSlave_Object = MibTableColumn
sdpBindStandbySigSlave = _SdpBindStandbySigSlave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 47),
    _SdpBindStandbySigSlave_Type()
)
sdpBindStandbySigSlave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindStandbySigSlave.setStatus("current")


class _SdpBindHashLabelSignalCapability_Type(TruthValue):
    """Custom type sdpBindHashLabelSignalCapability based on TruthValue"""
    defaultValue = 2


_SdpBindHashLabelSignalCapability_Type.__name__ = "TruthValue"
_SdpBindHashLabelSignalCapability_Object = MibTableColumn
sdpBindHashLabelSignalCapability = _SdpBindHashLabelSignalCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 48),
    _SdpBindHashLabelSignalCapability_Type()
)
sdpBindHashLabelSignalCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindHashLabelSignalCapability.setStatus("current")


class _SdpBindIngressFlowspec_Type(TruthValue):
    """Custom type sdpBindIngressFlowspec based on TruthValue"""
    defaultValue = 2


_SdpBindIngressFlowspec_Type.__name__ = "TruthValue"
_SdpBindIngressFlowspec_Object = MibTableColumn
sdpBindIngressFlowspec = _SdpBindIngressFlowspec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 49),
    _SdpBindIngressFlowspec_Type()
)
sdpBindIngressFlowspec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressFlowspec.setStatus("obsolete")


class _SdpBindCpmProtPolicyId_Type(TCpmProtPolicyID):
    """Custom type sdpBindCpmProtPolicyId based on TCpmProtPolicyID"""
    defaultValue = 255


_SdpBindCpmProtPolicyId_Type.__name__ = "TCpmProtPolicyID"
_SdpBindCpmProtPolicyId_Object = MibTableColumn
sdpBindCpmProtPolicyId = _SdpBindCpmProtPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 50),
    _SdpBindCpmProtPolicyId_Type()
)
sdpBindCpmProtPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindCpmProtPolicyId.setStatus("current")


class _SdpBindCpmProtMonitorMac_Type(TruthValue):
    """Custom type sdpBindCpmProtMonitorMac based on TruthValue"""
    defaultValue = 2


_SdpBindCpmProtMonitorMac_Type.__name__ = "TruthValue"
_SdpBindCpmProtMonitorMac_Object = MibTableColumn
sdpBindCpmProtMonitorMac = _SdpBindCpmProtMonitorMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 51),
    _SdpBindCpmProtMonitorMac_Type()
)
sdpBindCpmProtMonitorMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindCpmProtMonitorMac.setStatus("current")


class _SdpBindCpmProtEthCfmMonitorFlags_Type(Bits):
    """Custom type sdpBindCpmProtEthCfmMonitorFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("ethCfmMonitor", 0),
          ("ethCfmMonitorAggregate", 1),
          ("ethCfmMonitorCommittedAccessRate", 2))
    )

_SdpBindCpmProtEthCfmMonitorFlags_Type.__name__ = "Bits"
_SdpBindCpmProtEthCfmMonitorFlags_Object = MibTableColumn
sdpBindCpmProtEthCfmMonitorFlags = _SdpBindCpmProtEthCfmMonitorFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 52),
    _SdpBindCpmProtEthCfmMonitorFlags_Type()
)
sdpBindCpmProtEthCfmMonitorFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindCpmProtEthCfmMonitorFlags.setStatus("current")


class _SdpBindTransitIpPolicyId_Type(TmnxBsxTransitIpPolicyIdOrZero):
    """Custom type sdpBindTransitIpPolicyId based on TmnxBsxTransitIpPolicyIdOrZero"""
    defaultValue = 0


_SdpBindTransitIpPolicyId_Type.__name__ = "TmnxBsxTransitIpPolicyIdOrZero"
_SdpBindTransitIpPolicyId_Object = MibTableColumn
sdpBindTransitIpPolicyId = _SdpBindTransitIpPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 53),
    _SdpBindTransitIpPolicyId_Type()
)
sdpBindTransitIpPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindTransitIpPolicyId.setStatus("current")
_SdpBindPwStatusSignaling_Type = TruthValue
_SdpBindPwStatusSignaling_Object = MibTableColumn
sdpBindPwStatusSignaling = _SdpBindPwStatusSignaling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 54),
    _SdpBindPwStatusSignaling_Type()
)
sdpBindPwStatusSignaling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindPwStatusSignaling.setStatus("current")


class _SdpBindOperGrp_Type(TNamedItemOrEmpty):
    """Custom type sdpBindOperGrp based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_SdpBindOperGrp_Type.__name__ = "TNamedItemOrEmpty"
_SdpBindOperGrp_Object = MibTableColumn
sdpBindOperGrp = _SdpBindOperGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 55),
    _SdpBindOperGrp_Type()
)
sdpBindOperGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindOperGrp.setStatus("current")


class _SdpBindMonitorOperGrp_Type(TNamedItemOrEmpty):
    """Custom type sdpBindMonitorOperGrp based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_SdpBindMonitorOperGrp_Type.__name__ = "TNamedItemOrEmpty"
_SdpBindMonitorOperGrp_Object = MibTableColumn
sdpBindMonitorOperGrp = _SdpBindMonitorOperGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 56),
    _SdpBindMonitorOperGrp_Type()
)
sdpBindMonitorOperGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindMonitorOperGrp.setStatus("current")
_SdpBindOperHashLabel_Type = TruthValue
_SdpBindOperHashLabel_Object = MibTableColumn
sdpBindOperHashLabel = _SdpBindOperHashLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 57),
    _SdpBindOperHashLabel_Type()
)
sdpBindOperHashLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperHashLabel.setStatus("current")


class _SdpBindTransitPrefixPolicyId_Type(TmnxBsxTransPrefPolicyIdOrZero):
    """Custom type sdpBindTransitPrefixPolicyId based on TmnxBsxTransPrefPolicyIdOrZero"""
    defaultValue = 0


_SdpBindTransitPrefixPolicyId_Type.__name__ = "TmnxBsxTransPrefPolicyIdOrZero"
_SdpBindTransitPrefixPolicyId_Object = MibTableColumn
sdpBindTransitPrefixPolicyId = _SdpBindTransitPrefixPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 58),
    _SdpBindTransitPrefixPolicyId_Type()
)
sdpBindTransitPrefixPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindTransitPrefixPolicyId.setStatus("current")


class _SdpBindAarpId_Type(TmnxBsxAarpIdOrZero):
    """Custom type sdpBindAarpId based on TmnxBsxAarpIdOrZero"""
    defaultValue = 0


_SdpBindAarpId_Type.__name__ = "TmnxBsxAarpIdOrZero"
_SdpBindAarpId_Object = MibTableColumn
sdpBindAarpId = _SdpBindAarpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 59),
    _SdpBindAarpId_Type()
)
sdpBindAarpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAarpId.setStatus("current")


class _SdpBindIngressQoSNetworkPlcyId_Type(TSdpIngressPolicyID):
    """Custom type sdpBindIngressQoSNetworkPlcyId based on TSdpIngressPolicyID"""
    defaultValue = 0


_SdpBindIngressQoSNetworkPlcyId_Type.__name__ = "TSdpIngressPolicyID"
_SdpBindIngressQoSNetworkPlcyId_Object = MibTableColumn
sdpBindIngressQoSNetworkPlcyId = _SdpBindIngressQoSNetworkPlcyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 60),
    _SdpBindIngressQoSNetworkPlcyId_Type()
)
sdpBindIngressQoSNetworkPlcyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressQoSNetworkPlcyId.setStatus("current")


class _SdpBindEgressQoSNetworkPlcyId_Type(TSdpEgressPolicyID):
    """Custom type sdpBindEgressQoSNetworkPlcyId based on TSdpEgressPolicyID"""
    defaultValue = 0


_SdpBindEgressQoSNetworkPlcyId_Type.__name__ = "TSdpEgressPolicyID"
_SdpBindEgressQoSNetworkPlcyId_Object = MibTableColumn
sdpBindEgressQoSNetworkPlcyId = _SdpBindEgressQoSNetworkPlcyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 61),
    _SdpBindEgressQoSNetworkPlcyId_Type()
)
sdpBindEgressQoSNetworkPlcyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEgressQoSNetworkPlcyId.setStatus("current")


class _SdpBindIngressQoSFpRedirectQGrp_Type(TNamedItemOrEmpty):
    """Custom type sdpBindIngressQoSFpRedirectQGrp based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_SdpBindIngressQoSFpRedirectQGrp_Type.__name__ = "TNamedItemOrEmpty"
_SdpBindIngressQoSFpRedirectQGrp_Object = MibTableColumn
sdpBindIngressQoSFpRedirectQGrp = _SdpBindIngressQoSFpRedirectQGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 62),
    _SdpBindIngressQoSFpRedirectQGrp_Type()
)
sdpBindIngressQoSFpRedirectQGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressQoSFpRedirectQGrp.setStatus("current")


class _SdpBindEgressQoSPortRedirectQGrp_Type(TNamedItemOrEmpty):
    """Custom type sdpBindEgressQoSPortRedirectQGrp based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_SdpBindEgressQoSPortRedirectQGrp_Type.__name__ = "TNamedItemOrEmpty"
_SdpBindEgressQoSPortRedirectQGrp_Object = MibTableColumn
sdpBindEgressQoSPortRedirectQGrp = _SdpBindEgressQoSPortRedirectQGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 63),
    _SdpBindEgressQoSPortRedirectQGrp_Type()
)
sdpBindEgressQoSPortRedirectQGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEgressQoSPortRedirectQGrp.setStatus("current")


class _SdpBindIngressQoSInstanceId_Type(TQosQGrpInstanceIDorZero):
    """Custom type sdpBindIngressQoSInstanceId based on TQosQGrpInstanceIDorZero"""
    defaultValue = 0


_SdpBindIngressQoSInstanceId_Type.__name__ = "TQosQGrpInstanceIDorZero"
_SdpBindIngressQoSInstanceId_Object = MibTableColumn
sdpBindIngressQoSInstanceId = _SdpBindIngressQoSInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 64),
    _SdpBindIngressQoSInstanceId_Type()
)
sdpBindIngressQoSInstanceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressQoSInstanceId.setStatus("current")


class _SdpBindEgressQoSInstanceId_Type(TQosQGrpInstanceIDorZero):
    """Custom type sdpBindEgressQoSInstanceId based on TQosQGrpInstanceIDorZero"""
    defaultValue = 0


_SdpBindEgressQoSInstanceId_Type.__name__ = "TQosQGrpInstanceIDorZero"
_SdpBindEgressQoSInstanceId_Object = MibTableColumn
sdpBindEgressQoSInstanceId = _SdpBindEgressQoSInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 65),
    _SdpBindEgressQoSInstanceId_Type()
)
sdpBindEgressQoSInstanceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEgressQoSInstanceId.setStatus("current")


class _SdpBindAarpServRefType_Type(TmnxBsxAarpServiceRefType):
    """Custom type sdpBindAarpServRefType based on TmnxBsxAarpServiceRefType"""
    defaultValue = 0


_SdpBindAarpServRefType_Type.__name__ = "TmnxBsxAarpServiceRefType"
_SdpBindAarpServRefType_Object = MibTableColumn
sdpBindAarpServRefType = _SdpBindAarpServRefType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 66),
    _SdpBindAarpServRefType_Type()
)
sdpBindAarpServRefType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAarpServRefType.setStatus("current")


class _SdpBindPwLocalStatusBits_Type(Bits):
    """Custom type sdpBindPwLocalStatusBits based on Bits"""
    namedValues = NamedValues(
        *(("pwNotForwarding", 0),
          ("lacIngressFault", 1),
          ("lacEgresssFault", 2),
          ("psnIngressFault", 3),
          ("psnEgressFault", 4),
          ("pwFwdingStandby", 5))
    )

_SdpBindPwLocalStatusBits_Type.__name__ = "Bits"
_SdpBindPwLocalStatusBits_Object = MibTableColumn
sdpBindPwLocalStatusBits = _SdpBindPwLocalStatusBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 67),
    _SdpBindPwLocalStatusBits_Type()
)
sdpBindPwLocalStatusBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPwLocalStatusBits.setStatus("current")


class _SdpBindBlockOnPeerFault_Type(TruthValue):
    """Custom type sdpBindBlockOnPeerFault based on TruthValue"""
    defaultValue = 2


_SdpBindBlockOnPeerFault_Type.__name__ = "TruthValue"
_SdpBindBlockOnPeerFault_Object = MibTableColumn
sdpBindBlockOnPeerFault = _SdpBindBlockOnPeerFault_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 68),
    _SdpBindBlockOnPeerFault_Type()
)
sdpBindBlockOnPeerFault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindBlockOnPeerFault.setStatus("current")


class _SdpBindIngressIPv6Flowspec_Type(TruthValue):
    """Custom type sdpBindIngressIPv6Flowspec based on TruthValue"""
    defaultValue = 2


_SdpBindIngressIPv6Flowspec_Type.__name__ = "TruthValue"
_SdpBindIngressIPv6Flowspec_Object = MibTableColumn
sdpBindIngressIPv6Flowspec = _SdpBindIngressIPv6Flowspec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 69),
    _SdpBindIngressIPv6Flowspec_Type()
)
sdpBindIngressIPv6Flowspec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressIPv6Flowspec.setStatus("obsolete")


class _SdpBindMirrorRemoteSource_Type(TruthValue):
    """Custom type sdpBindMirrorRemoteSource based on TruthValue"""
    defaultValue = 2


_SdpBindMirrorRemoteSource_Type.__name__ = "TruthValue"
_SdpBindMirrorRemoteSource_Object = MibTableColumn
sdpBindMirrorRemoteSource = _SdpBindMirrorRemoteSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 70),
    _SdpBindMirrorRemoteSource_Type()
)
sdpBindMirrorRemoteSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindMirrorRemoteSource.setStatus("current")


class _SdpBindEtreeRootLeafTag_Type(TruthValue):
    """Custom type sdpBindEtreeRootLeafTag based on TruthValue"""
    defaultValue = 2


_SdpBindEtreeRootLeafTag_Type.__name__ = "TruthValue"
_SdpBindEtreeRootLeafTag_Object = MibTableColumn
sdpBindEtreeRootLeafTag = _SdpBindEtreeRootLeafTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 72),
    _SdpBindEtreeRootLeafTag_Type()
)
sdpBindEtreeRootLeafTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEtreeRootLeafTag.setStatus("current")


class _SdpBindCpmProtMonitorIP_Type(TruthValue):
    """Custom type sdpBindCpmProtMonitorIP based on TruthValue"""
    defaultValue = 2


_SdpBindCpmProtMonitorIP_Type.__name__ = "TruthValue"
_SdpBindCpmProtMonitorIP_Object = MibTableColumn
sdpBindCpmProtMonitorIP = _SdpBindCpmProtMonitorIP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 73),
    _SdpBindCpmProtMonitorIP_Type()
)
sdpBindCpmProtMonitorIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindCpmProtMonitorIP.setStatus("current")


class _SdpBindUseSdpBMac_Type(TruthValue):
    """Custom type sdpBindUseSdpBMac based on TruthValue"""
    defaultValue = 2


_SdpBindUseSdpBMac_Type.__name__ = "TruthValue"
_SdpBindUseSdpBMac_Object = MibTableColumn
sdpBindUseSdpBMac = _SdpBindUseSdpBMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 74),
    _SdpBindUseSdpBMac_Type()
)
sdpBindUseSdpBMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindUseSdpBMac.setStatus("current")


class _SdpBindEtreeLeafAc_Type(TruthValue):
    """Custom type sdpBindEtreeLeafAc based on TruthValue"""
    defaultValue = 2


_SdpBindEtreeLeafAc_Type.__name__ = "TruthValue"
_SdpBindEtreeLeafAc_Object = MibTableColumn
sdpBindEtreeLeafAc = _SdpBindEtreeLeafAc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 75),
    _SdpBindEtreeLeafAc_Type()
)
sdpBindEtreeLeafAc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEtreeLeafAc.setStatus("current")


class _SdpBindBfdTemplateName_Type(TNamedItemOrEmpty):
    """Custom type sdpBindBfdTemplateName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SdpBindBfdTemplateName_Type.__name__ = "TNamedItemOrEmpty"
_SdpBindBfdTemplateName_Object = MibTableColumn
sdpBindBfdTemplateName = _SdpBindBfdTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 76),
    _SdpBindBfdTemplateName_Type()
)
sdpBindBfdTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindBfdTemplateName.setStatus("current")


class _SdpBindBfdEnable_Type(TruthValue):
    """Custom type sdpBindBfdEnable based on TruthValue"""
    defaultValue = 2


_SdpBindBfdEnable_Type.__name__ = "TruthValue"
_SdpBindBfdEnable_Object = MibTableColumn
sdpBindBfdEnable = _SdpBindBfdEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 77),
    _SdpBindBfdEnable_Type()
)
sdpBindBfdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindBfdEnable.setStatus("current")


class _SdpBindBfdEncap_Type(TmnxBfdEncap):
    """Custom type sdpBindBfdEncap based on TmnxBfdEncap"""
    defaultValue = 1


_SdpBindBfdEncap_Type.__name__ = "TmnxBfdEncap"
_SdpBindBfdEncap_Object = MibTableColumn
sdpBindBfdEncap = _SdpBindBfdEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 78),
    _SdpBindBfdEncap_Type()
)
sdpBindBfdEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindBfdEncap.setStatus("current")


class _SdpBindForceQinqVcForwarding_Type(TruthValue):
    """Custom type sdpBindForceQinqVcForwarding based on TruthValue"""
    defaultValue = 2


_SdpBindForceQinqVcForwarding_Type.__name__ = "TruthValue"
_SdpBindForceQinqVcForwarding_Object = MibTableColumn
sdpBindForceQinqVcForwarding = _SdpBindForceQinqVcForwarding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 79),
    _SdpBindForceQinqVcForwarding_Type()
)
sdpBindForceQinqVcForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindForceQinqVcForwarding.setStatus("obsolete")


class _SdpBindIngressVlanTranslation_Type(Integer32):
    """Custom type sdpBindIngressVlanTranslation based on Integer32"""
    defaultValue = 1

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
          ("vlanId", 2),
          ("copyOuter", 3))
    )


_SdpBindIngressVlanTranslation_Type.__name__ = "Integer32"
_SdpBindIngressVlanTranslation_Object = MibTableColumn
sdpBindIngressVlanTranslation = _SdpBindIngressVlanTranslation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 80),
    _SdpBindIngressVlanTranslation_Type()
)
sdpBindIngressVlanTranslation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressVlanTranslation.setStatus("obsolete")


class _SdpBindIngressVlanTranslationId_Type(Integer32):
    """Custom type sdpBindIngressVlanTranslationId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 4094),
    )


_SdpBindIngressVlanTranslationId_Type.__name__ = "Integer32"
_SdpBindIngressVlanTranslationId_Object = MibTableColumn
sdpBindIngressVlanTranslationId = _SdpBindIngressVlanTranslationId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 81),
    _SdpBindIngressVlanTranslationId_Type()
)
sdpBindIngressVlanTranslationId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressVlanTranslationId.setStatus("obsolete")
_SdpBindMinReqdSdpOperMtu_Type = Integer32
_SdpBindMinReqdSdpOperMtu_Object = MibTableColumn
sdpBindMinReqdSdpOperMtu = _SdpBindMinReqdSdpOperMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 82),
    _SdpBindMinReqdSdpOperMtu_Type()
)
sdpBindMinReqdSdpOperMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindMinReqdSdpOperMtu.setStatus("current")


class _SdpBindForceQinqVcFwding_Type(Integer32):
    """Custom type sdpBindForceQinqVcFwding based on Integer32"""
    defaultValue = 0

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
          ("ctagctag", 1),
          ("stagctag", 2))
    )


_SdpBindForceQinqVcFwding_Type.__name__ = "Integer32"
_SdpBindForceQinqVcFwding_Object = MibTableColumn
sdpBindForceQinqVcFwding = _SdpBindForceQinqVcFwding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 83),
    _SdpBindForceQinqVcFwding_Type()
)
sdpBindForceQinqVcFwding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindForceQinqVcFwding.setStatus("current")


class _SdpBindMulticastSource_Type(TruthValue):
    """Custom type sdpBindMulticastSource based on TruthValue"""
    defaultValue = 2


_SdpBindMulticastSource_Type.__name__ = "TruthValue"
_SdpBindMulticastSource_Object = MibTableColumn
sdpBindMulticastSource = _SdpBindMulticastSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 84),
    _SdpBindMulticastSource_Type()
)
sdpBindMulticastSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindMulticastSource.setStatus("current")
_SdpBindBaseStatsTable_Object = MibTable
sdpBindBaseStatsTable = _SdpBindBaseStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 5)
)
if mibBuilder.loadTexts:
    sdpBindBaseStatsTable.setStatus("current")
_SdpBindBaseStatsEntry_Object = MibTableRow
sdpBindBaseStatsEntry = _SdpBindBaseStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 5, 1)
)
sdpBindBaseStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindBaseStatsEntry.setStatus("current")
_SdpBindBaseStatsIngressForwardedPackets_Type = Counter64
_SdpBindBaseStatsIngressForwardedPackets_Object = MibTableColumn
sdpBindBaseStatsIngressForwardedPackets = _SdpBindBaseStatsIngressForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 5, 1, 1),
    _SdpBindBaseStatsIngressForwardedPackets_Type()
)
sdpBindBaseStatsIngressForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsIngressForwardedPackets.setStatus("current")
_SdpBindBaseStatsIngressDroppedPackets_Type = Counter64
_SdpBindBaseStatsIngressDroppedPackets_Object = MibTableColumn
sdpBindBaseStatsIngressDroppedPackets = _SdpBindBaseStatsIngressDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 5, 1, 2),
    _SdpBindBaseStatsIngressDroppedPackets_Type()
)
sdpBindBaseStatsIngressDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsIngressDroppedPackets.setStatus("current")
_SdpBindBaseStatsEgressForwardedPackets_Type = Counter64
_SdpBindBaseStatsEgressForwardedPackets_Object = MibTableColumn
sdpBindBaseStatsEgressForwardedPackets = _SdpBindBaseStatsEgressForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 5, 1, 3),
    _SdpBindBaseStatsEgressForwardedPackets_Type()
)
sdpBindBaseStatsEgressForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsEgressForwardedPackets.setStatus("current")
_SdpBindBaseStatsEgressForwardedOctets_Type = Counter64
_SdpBindBaseStatsEgressForwardedOctets_Object = MibTableColumn
sdpBindBaseStatsEgressForwardedOctets = _SdpBindBaseStatsEgressForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 5, 1, 4),
    _SdpBindBaseStatsEgressForwardedOctets_Type()
)
sdpBindBaseStatsEgressForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsEgressForwardedOctets.setStatus("current")
_SdpBindBaseStatsCustId_Type = TmnxCustId
_SdpBindBaseStatsCustId_Object = MibTableColumn
sdpBindBaseStatsCustId = _SdpBindBaseStatsCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 5, 1, 5),
    _SdpBindBaseStatsCustId_Type()
)
sdpBindBaseStatsCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsCustId.setStatus("current")
_SdpBindBaseStatsIngFwdOctets_Type = Counter64
_SdpBindBaseStatsIngFwdOctets_Object = MibTableColumn
sdpBindBaseStatsIngFwdOctets = _SdpBindBaseStatsIngFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 5, 1, 6),
    _SdpBindBaseStatsIngFwdOctets_Type()
)
sdpBindBaseStatsIngFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsIngFwdOctets.setStatus("current")
_SdpBindBaseStatsIngDropOctets_Type = Counter64
_SdpBindBaseStatsIngDropOctets_Object = MibTableColumn
sdpBindBaseStatsIngDropOctets = _SdpBindBaseStatsIngDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 5, 1, 7),
    _SdpBindBaseStatsIngDropOctets_Type()
)
sdpBindBaseStatsIngDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsIngDropOctets.setStatus("current")
_SdpBindTlsTable_Object = MibTable
sdpBindTlsTable = _SdpBindTlsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6)
)
if mibBuilder.loadTexts:
    sdpBindTlsTable.setStatus("current")
_SdpBindTlsEntry_Object = MibTableRow
sdpBindTlsEntry = _SdpBindTlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1)
)
sdpBindTlsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindTlsEntry.setStatus("current")


class _SdpBindTlsStpAdminStatus_Type(TmnxEnabledDisabledAdminState):
    """Custom type sdpBindTlsStpAdminStatus based on TmnxEnabledDisabledAdminState"""
    defaultValue = 1


_SdpBindTlsStpAdminStatus_Type.__name__ = "TmnxEnabledDisabledAdminState"
_SdpBindTlsStpAdminStatus_Object = MibTableColumn
sdpBindTlsStpAdminStatus = _SdpBindTlsStpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 1),
    _SdpBindTlsStpAdminStatus_Type()
)
sdpBindTlsStpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsStpAdminStatus.setStatus("current")


class _SdpBindTlsStpPriority_Type(Integer32):
    """Custom type sdpBindTlsStpPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SdpBindTlsStpPriority_Type.__name__ = "Integer32"
_SdpBindTlsStpPriority_Object = MibTableColumn
sdpBindTlsStpPriority = _SdpBindTlsStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 2),
    _SdpBindTlsStpPriority_Type()
)
sdpBindTlsStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsStpPriority.setStatus("current")


class _SdpBindTlsStpPortNum_Type(Integer32):
    """Custom type sdpBindTlsStpPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_SdpBindTlsStpPortNum_Type.__name__ = "Integer32"
_SdpBindTlsStpPortNum_Object = MibTableColumn
sdpBindTlsStpPortNum = _SdpBindTlsStpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 3),
    _SdpBindTlsStpPortNum_Type()
)
sdpBindTlsStpPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsStpPortNum.setStatus("current")


class _SdpBindTlsStpPathCost_Type(Integer32):
    """Custom type sdpBindTlsStpPathCost based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_SdpBindTlsStpPathCost_Type.__name__ = "Integer32"
_SdpBindTlsStpPathCost_Object = MibTableColumn
sdpBindTlsStpPathCost = _SdpBindTlsStpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 4),
    _SdpBindTlsStpPathCost_Type()
)
sdpBindTlsStpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsStpPathCost.setStatus("current")


class _SdpBindTlsStpRapidStart_Type(TmnxEnabledDisabled):
    """Custom type sdpBindTlsStpRapidStart based on TmnxEnabledDisabled"""
    defaultValue = 2


_SdpBindTlsStpRapidStart_Type.__name__ = "TmnxEnabledDisabled"
_SdpBindTlsStpRapidStart_Object = MibTableColumn
sdpBindTlsStpRapidStart = _SdpBindTlsStpRapidStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 5),
    _SdpBindTlsStpRapidStart_Type()
)
sdpBindTlsStpRapidStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsStpRapidStart.setStatus("current")


class _SdpBindTlsStpBpduEncap_Type(Integer32):
    """Custom type sdpBindTlsStpBpduEncap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("dot1d", 2),
          ("pvst", 3))
    )


_SdpBindTlsStpBpduEncap_Type.__name__ = "Integer32"
_SdpBindTlsStpBpduEncap_Object = MibTableColumn
sdpBindTlsStpBpduEncap = _SdpBindTlsStpBpduEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 6),
    _SdpBindTlsStpBpduEncap_Type()
)
sdpBindTlsStpBpduEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsStpBpduEncap.setStatus("current")
_SdpBindTlsStpPortState_Type = TStpPortState
_SdpBindTlsStpPortState_Object = MibTableColumn
sdpBindTlsStpPortState = _SdpBindTlsStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 7),
    _SdpBindTlsStpPortState_Type()
)
sdpBindTlsStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpPortState.setStatus("current")
_SdpBindTlsStpDesignatedBridge_Type = BridgeId
_SdpBindTlsStpDesignatedBridge_Object = MibTableColumn
sdpBindTlsStpDesignatedBridge = _SdpBindTlsStpDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 8),
    _SdpBindTlsStpDesignatedBridge_Type()
)
sdpBindTlsStpDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpDesignatedBridge.setStatus("current")
_SdpBindTlsStpDesignatedPort_Type = Integer32
_SdpBindTlsStpDesignatedPort_Object = MibTableColumn
sdpBindTlsStpDesignatedPort = _SdpBindTlsStpDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 9),
    _SdpBindTlsStpDesignatedPort_Type()
)
sdpBindTlsStpDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpDesignatedPort.setStatus("current")
_SdpBindTlsStpForwardTransitions_Type = Gauge32
_SdpBindTlsStpForwardTransitions_Object = MibTableColumn
sdpBindTlsStpForwardTransitions = _SdpBindTlsStpForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 10),
    _SdpBindTlsStpForwardTransitions_Type()
)
sdpBindTlsStpForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpForwardTransitions.setStatus("current")
_SdpBindTlsStpInConfigBpdus_Type = Gauge32
_SdpBindTlsStpInConfigBpdus_Object = MibTableColumn
sdpBindTlsStpInConfigBpdus = _SdpBindTlsStpInConfigBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 11),
    _SdpBindTlsStpInConfigBpdus_Type()
)
sdpBindTlsStpInConfigBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpInConfigBpdus.setStatus("current")
_SdpBindTlsStpInTcnBpdus_Type = Gauge32
_SdpBindTlsStpInTcnBpdus_Object = MibTableColumn
sdpBindTlsStpInTcnBpdus = _SdpBindTlsStpInTcnBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 12),
    _SdpBindTlsStpInTcnBpdus_Type()
)
sdpBindTlsStpInTcnBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpInTcnBpdus.setStatus("current")
_SdpBindTlsStpInBadBpdus_Type = Gauge32
_SdpBindTlsStpInBadBpdus_Object = MibTableColumn
sdpBindTlsStpInBadBpdus = _SdpBindTlsStpInBadBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 13),
    _SdpBindTlsStpInBadBpdus_Type()
)
sdpBindTlsStpInBadBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpInBadBpdus.setStatus("current")
_SdpBindTlsStpOutConfigBpdus_Type = Gauge32
_SdpBindTlsStpOutConfigBpdus_Object = MibTableColumn
sdpBindTlsStpOutConfigBpdus = _SdpBindTlsStpOutConfigBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 14),
    _SdpBindTlsStpOutConfigBpdus_Type()
)
sdpBindTlsStpOutConfigBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpOutConfigBpdus.setStatus("current")
_SdpBindTlsStpOutTcnBpdus_Type = Gauge32
_SdpBindTlsStpOutTcnBpdus_Object = MibTableColumn
sdpBindTlsStpOutTcnBpdus = _SdpBindTlsStpOutTcnBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 15),
    _SdpBindTlsStpOutTcnBpdus_Type()
)
sdpBindTlsStpOutTcnBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpOutTcnBpdus.setStatus("current")


class _SdpBindTlsStpOperBpduEncap_Type(Integer32):
    """Custom type sdpBindTlsStpOperBpduEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1d", 2),
          ("pvst", 3))
    )


_SdpBindTlsStpOperBpduEncap_Type.__name__ = "Integer32"
_SdpBindTlsStpOperBpduEncap_Object = MibTableColumn
sdpBindTlsStpOperBpduEncap = _SdpBindTlsStpOperBpduEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 16),
    _SdpBindTlsStpOperBpduEncap_Type()
)
sdpBindTlsStpOperBpduEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpOperBpduEncap.setStatus("current")
_SdpBindTlsStpVpnId_Type = VpnId
_SdpBindTlsStpVpnId_Object = MibTableColumn
sdpBindTlsStpVpnId = _SdpBindTlsStpVpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 17),
    _SdpBindTlsStpVpnId_Type()
)
sdpBindTlsStpVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpVpnId.setStatus("current")
_SdpBindTlsStpCustId_Type = TmnxCustId
_SdpBindTlsStpCustId_Object = MibTableColumn
sdpBindTlsStpCustId = _SdpBindTlsStpCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 18),
    _SdpBindTlsStpCustId_Type()
)
sdpBindTlsStpCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpCustId.setStatus("current")


class _SdpBindTlsMacAddressLimit_Type(Integer32):
    """Custom type sdpBindTlsMacAddressLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511999),
    )


_SdpBindTlsMacAddressLimit_Type.__name__ = "Integer32"
_SdpBindTlsMacAddressLimit_Object = MibTableColumn
sdpBindTlsMacAddressLimit = _SdpBindTlsMacAddressLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 19),
    _SdpBindTlsMacAddressLimit_Type()
)
sdpBindTlsMacAddressLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMacAddressLimit.setStatus("current")
_SdpBindTlsNumMacAddresses_Type = Integer32
_SdpBindTlsNumMacAddresses_Object = MibTableColumn
sdpBindTlsNumMacAddresses = _SdpBindTlsNumMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 20),
    _SdpBindTlsNumMacAddresses_Type()
)
sdpBindTlsNumMacAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsNumMacAddresses.setStatus("current")
_SdpBindTlsNumStaticMacAddresses_Type = Integer32
_SdpBindTlsNumStaticMacAddresses_Object = MibTableColumn
sdpBindTlsNumStaticMacAddresses = _SdpBindTlsNumStaticMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 21),
    _SdpBindTlsNumStaticMacAddresses_Type()
)
sdpBindTlsNumStaticMacAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsNumStaticMacAddresses.setStatus("current")


class _SdpBindTlsMacLearning_Type(TmnxEnabledDisabled):
    """Custom type sdpBindTlsMacLearning based on TmnxEnabledDisabled"""
    defaultValue = 1


_SdpBindTlsMacLearning_Type.__name__ = "TmnxEnabledDisabled"
_SdpBindTlsMacLearning_Object = MibTableColumn
sdpBindTlsMacLearning = _SdpBindTlsMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 22),
    _SdpBindTlsMacLearning_Type()
)
sdpBindTlsMacLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMacLearning.setStatus("current")


class _SdpBindTlsMacAgeing_Type(TmnxEnabledDisabled):
    """Custom type sdpBindTlsMacAgeing based on TmnxEnabledDisabled"""
    defaultValue = 1


_SdpBindTlsMacAgeing_Type.__name__ = "TmnxEnabledDisabled"
_SdpBindTlsMacAgeing_Object = MibTableColumn
sdpBindTlsMacAgeing = _SdpBindTlsMacAgeing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 23),
    _SdpBindTlsMacAgeing_Type()
)
sdpBindTlsMacAgeing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMacAgeing.setStatus("current")
_SdpBindTlsStpOperEdge_Type = TruthValue
_SdpBindTlsStpOperEdge_Object = MibTableColumn
sdpBindTlsStpOperEdge = _SdpBindTlsStpOperEdge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 24),
    _SdpBindTlsStpOperEdge_Type()
)
sdpBindTlsStpOperEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpOperEdge.setStatus("current")


class _SdpBindTlsStpAdminPointToPoint_Type(Integer32):
    """Custom type sdpBindTlsStpAdminPointToPoint based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("forceTrue", 0),
          ("forceFalse", 1))
    )


_SdpBindTlsStpAdminPointToPoint_Type.__name__ = "Integer32"
_SdpBindTlsStpAdminPointToPoint_Object = MibTableColumn
sdpBindTlsStpAdminPointToPoint = _SdpBindTlsStpAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 25),
    _SdpBindTlsStpAdminPointToPoint_Type()
)
sdpBindTlsStpAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsStpAdminPointToPoint.setStatus("current")
_SdpBindTlsStpPortRole_Type = StpPortRole
_SdpBindTlsStpPortRole_Object = MibTableColumn
sdpBindTlsStpPortRole = _SdpBindTlsStpPortRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 26),
    _SdpBindTlsStpPortRole_Type()
)
sdpBindTlsStpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpPortRole.setStatus("current")


class _SdpBindTlsStpAutoEdge_Type(TmnxEnabledDisabled):
    """Custom type sdpBindTlsStpAutoEdge based on TmnxEnabledDisabled"""
    defaultValue = 1


_SdpBindTlsStpAutoEdge_Type.__name__ = "TmnxEnabledDisabled"
_SdpBindTlsStpAutoEdge_Object = MibTableColumn
sdpBindTlsStpAutoEdge = _SdpBindTlsStpAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 27),
    _SdpBindTlsStpAutoEdge_Type()
)
sdpBindTlsStpAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsStpAutoEdge.setStatus("current")
_SdpBindTlsStpOperProtocol_Type = StpProtocol
_SdpBindTlsStpOperProtocol_Object = MibTableColumn
sdpBindTlsStpOperProtocol = _SdpBindTlsStpOperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 28),
    _SdpBindTlsStpOperProtocol_Type()
)
sdpBindTlsStpOperProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpOperProtocol.setStatus("current")
_SdpBindTlsStpInRstBpdus_Type = Gauge32
_SdpBindTlsStpInRstBpdus_Object = MibTableColumn
sdpBindTlsStpInRstBpdus = _SdpBindTlsStpInRstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 29),
    _SdpBindTlsStpInRstBpdus_Type()
)
sdpBindTlsStpInRstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpInRstBpdus.setStatus("current")
_SdpBindTlsStpOutRstBpdus_Type = Gauge32
_SdpBindTlsStpOutRstBpdus_Object = MibTableColumn
sdpBindTlsStpOutRstBpdus = _SdpBindTlsStpOutRstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 30),
    _SdpBindTlsStpOutRstBpdus_Type()
)
sdpBindTlsStpOutRstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpOutRstBpdus.setStatus("current")


class _SdpBindTlsLimitMacMove_Type(TlsLimitMacMove):
    """Custom type sdpBindTlsLimitMacMove based on TlsLimitMacMove"""
    defaultValue = 1


_SdpBindTlsLimitMacMove_Type.__name__ = "TlsLimitMacMove"
_SdpBindTlsLimitMacMove_Object = MibTableColumn
sdpBindTlsLimitMacMove = _SdpBindTlsLimitMacMove_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 31),
    _SdpBindTlsLimitMacMove_Type()
)
sdpBindTlsLimitMacMove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsLimitMacMove.setStatus("current")


class _SdpBindTlsDiscardUnknownSource_Type(TmnxEnabledDisabled):
    """Custom type sdpBindTlsDiscardUnknownSource based on TmnxEnabledDisabled"""
    defaultValue = 2


_SdpBindTlsDiscardUnknownSource_Type.__name__ = "TmnxEnabledDisabled"
_SdpBindTlsDiscardUnknownSource_Object = MibTableColumn
sdpBindTlsDiscardUnknownSource = _SdpBindTlsDiscardUnknownSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 32),
    _SdpBindTlsDiscardUnknownSource_Type()
)
sdpBindTlsDiscardUnknownSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsDiscardUnknownSource.setStatus("current")
_SdpBindTlsMvplsPruneState_Type = MvplsPruneState
_SdpBindTlsMvplsPruneState_Object = MibTableColumn
sdpBindTlsMvplsPruneState = _SdpBindTlsMvplsPruneState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 33),
    _SdpBindTlsMvplsPruneState_Type()
)
sdpBindTlsMvplsPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMvplsPruneState.setStatus("current")
_SdpBindTlsMvplsMgmtService_Type = TmnxServId
_SdpBindTlsMvplsMgmtService_Object = MibTableColumn
sdpBindTlsMvplsMgmtService = _SdpBindTlsMvplsMgmtService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 34),
    _SdpBindTlsMvplsMgmtService_Type()
)
sdpBindTlsMvplsMgmtService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMvplsMgmtService.setStatus("current")
_SdpBindTlsMvplsMgmtSdpBndId_Type = SdpBindId
_SdpBindTlsMvplsMgmtSdpBndId_Object = MibTableColumn
sdpBindTlsMvplsMgmtSdpBndId = _SdpBindTlsMvplsMgmtSdpBndId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 35),
    _SdpBindTlsMvplsMgmtSdpBndId_Type()
)
sdpBindTlsMvplsMgmtSdpBndId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMvplsMgmtSdpBndId.setStatus("current")
_SdpBindTlsStpException_Type = StpExceptionCondition
_SdpBindTlsStpException_Object = MibTableColumn
sdpBindTlsStpException = _SdpBindTlsStpException_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 36),
    _SdpBindTlsStpException_Type()
)
sdpBindTlsStpException.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpException.setStatus("current")


class _SdpBindTlsL2ptTermination_Type(TmnxEnabledDisabled):
    """Custom type sdpBindTlsL2ptTermination based on TmnxEnabledDisabled"""
    defaultValue = 2


_SdpBindTlsL2ptTermination_Type.__name__ = "TmnxEnabledDisabled"
_SdpBindTlsL2ptTermination_Object = MibTableColumn
sdpBindTlsL2ptTermination = _SdpBindTlsL2ptTermination_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 37),
    _SdpBindTlsL2ptTermination_Type()
)
sdpBindTlsL2ptTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptTermination.setStatus("current")


class _SdpBindTlsBpduTranslation_Type(TlsBpduTranslation):
    """Custom type sdpBindTlsBpduTranslation based on TlsBpduTranslation"""
    defaultValue = 2


_SdpBindTlsBpduTranslation_Type.__name__ = "TlsBpduTranslation"
_SdpBindTlsBpduTranslation_Object = MibTableColumn
sdpBindTlsBpduTranslation = _SdpBindTlsBpduTranslation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 38),
    _SdpBindTlsBpduTranslation_Type()
)
sdpBindTlsBpduTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsBpduTranslation.setStatus("current")


class _SdpBindTlsStpRootGuard_Type(TruthValue):
    """Custom type sdpBindTlsStpRootGuard based on TruthValue"""
    defaultValue = 2


_SdpBindTlsStpRootGuard_Type.__name__ = "TruthValue"
_SdpBindTlsStpRootGuard_Object = MibTableColumn
sdpBindTlsStpRootGuard = _SdpBindTlsStpRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 39),
    _SdpBindTlsStpRootGuard_Type()
)
sdpBindTlsStpRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsStpRootGuard.setStatus("current")
_SdpBindTlsStpInMstBpdus_Type = Gauge32
_SdpBindTlsStpInMstBpdus_Object = MibTableColumn
sdpBindTlsStpInMstBpdus = _SdpBindTlsStpInMstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 40),
    _SdpBindTlsStpInMstBpdus_Type()
)
sdpBindTlsStpInMstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpInMstBpdus.setStatus("current")
_SdpBindTlsStpOutMstBpdus_Type = Gauge32
_SdpBindTlsStpOutMstBpdus_Object = MibTableColumn
sdpBindTlsStpOutMstBpdus = _SdpBindTlsStpOutMstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 41),
    _SdpBindTlsStpOutMstBpdus_Type()
)
sdpBindTlsStpOutMstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpOutMstBpdus.setStatus("current")
_SdpBindTlsStpRxdDesigBridge_Type = BridgeId
_SdpBindTlsStpRxdDesigBridge_Object = MibTableColumn
sdpBindTlsStpRxdDesigBridge = _SdpBindTlsStpRxdDesigBridge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 42),
    _SdpBindTlsStpRxdDesigBridge_Type()
)
sdpBindTlsStpRxdDesigBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpRxdDesigBridge.setStatus("current")
_SdpBindTlsMacMoveNextUpTime_Type = Unsigned32
_SdpBindTlsMacMoveNextUpTime_Object = MibTableColumn
sdpBindTlsMacMoveNextUpTime = _SdpBindTlsMacMoveNextUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 43),
    _SdpBindTlsMacMoveNextUpTime_Type()
)
sdpBindTlsMacMoveNextUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMacMoveNextUpTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindTlsMacMoveNextUpTime.setUnits("seconds")
_SdpBindTlsMacMoveRateExcdLeft_Type = Unsigned32
_SdpBindTlsMacMoveRateExcdLeft_Object = MibTableColumn
sdpBindTlsMacMoveRateExcdLeft = _SdpBindTlsMacMoveRateExcdLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 44),
    _SdpBindTlsMacMoveRateExcdLeft_Type()
)
sdpBindTlsMacMoveRateExcdLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMacMoveRateExcdLeft.setStatus("current")


class _SdpBindTlsLimitMacMoveLevel_Type(TlsLimitMacMoveLevel):
    """Custom type sdpBindTlsLimitMacMoveLevel based on TlsLimitMacMoveLevel"""
    defaultValue = 3


_SdpBindTlsLimitMacMoveLevel_Type.__name__ = "TlsLimitMacMoveLevel"
_SdpBindTlsLimitMacMoveLevel_Object = MibTableColumn
sdpBindTlsLimitMacMoveLevel = _SdpBindTlsLimitMacMoveLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 45),
    _SdpBindTlsLimitMacMoveLevel_Type()
)
sdpBindTlsLimitMacMoveLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsLimitMacMoveLevel.setStatus("current")


class _SdpBindTlsBpduTransOper_Type(Integer32):
    """Custom type sdpBindTlsBpduTransOper based on Integer32"""
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
        *(("undefined", 1),
          ("disabled", 2),
          ("pvst", 3),
          ("stp", 4),
          ("pvst-rw", 5))
    )


_SdpBindTlsBpduTransOper_Type.__name__ = "Integer32"
_SdpBindTlsBpduTransOper_Object = MibTableColumn
sdpBindTlsBpduTransOper = _SdpBindTlsBpduTransOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 46),
    _SdpBindTlsBpduTransOper_Type()
)
sdpBindTlsBpduTransOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsBpduTransOper.setStatus("current")


class _SdpBindTlsL2ptProtocols_Type(L2ptProtocols):
    """Custom type sdpBindTlsL2ptProtocols based on L2ptProtocols"""
    defaultBinValue = "1"


_SdpBindTlsL2ptProtocols_Type.__name__ = "L2ptProtocols"
_SdpBindTlsL2ptProtocols_Object = MibTableColumn
sdpBindTlsL2ptProtocols = _SdpBindTlsL2ptProtocols_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 47),
    _SdpBindTlsL2ptProtocols_Type()
)
sdpBindTlsL2ptProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptProtocols.setStatus("current")


class _SdpBindTlsIgnoreStandbySig_Type(TruthValue):
    """Custom type sdpBindTlsIgnoreStandbySig based on TruthValue"""
    defaultValue = 2


_SdpBindTlsIgnoreStandbySig_Type.__name__ = "TruthValue"
_SdpBindTlsIgnoreStandbySig_Object = MibTableColumn
sdpBindTlsIgnoreStandbySig = _SdpBindTlsIgnoreStandbySig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 48),
    _SdpBindTlsIgnoreStandbySig_Type()
)
sdpBindTlsIgnoreStandbySig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsIgnoreStandbySig.setStatus("current")


class _SdpBindTlsBlockOnMeshFail_Type(TruthValue):
    """Custom type sdpBindTlsBlockOnMeshFail based on TruthValue"""
    defaultValue = 2


_SdpBindTlsBlockOnMeshFail_Type.__name__ = "TruthValue"
_SdpBindTlsBlockOnMeshFail_Object = MibTableColumn
sdpBindTlsBlockOnMeshFail = _SdpBindTlsBlockOnMeshFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 49),
    _SdpBindTlsBlockOnMeshFail_Type()
)
sdpBindTlsBlockOnMeshFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsBlockOnMeshFail.setStatus("current")
_SdpBindTlsInTcBitBpdus_Type = Counter32
_SdpBindTlsInTcBitBpdus_Object = MibTableColumn
sdpBindTlsInTcBitBpdus = _SdpBindTlsInTcBitBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 50),
    _SdpBindTlsInTcBitBpdus_Type()
)
sdpBindTlsInTcBitBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsInTcBitBpdus.setStatus("current")
_SdpBindTlsOutTcBitBpdus_Type = Counter32
_SdpBindTlsOutTcBitBpdus_Object = MibTableColumn
sdpBindTlsOutTcBitBpdus = _SdpBindTlsOutTcBitBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 51),
    _SdpBindTlsOutTcBitBpdus_Type()
)
sdpBindTlsOutTcBitBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsOutTcBitBpdus.setStatus("current")


class _SdpBindTlsRestProtSrcMac_Type(TruthValue):
    """Custom type sdpBindTlsRestProtSrcMac based on TruthValue"""
    defaultValue = 2


_SdpBindTlsRestProtSrcMac_Type.__name__ = "TruthValue"
_SdpBindTlsRestProtSrcMac_Object = MibTableColumn
sdpBindTlsRestProtSrcMac = _SdpBindTlsRestProtSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 52),
    _SdpBindTlsRestProtSrcMac_Type()
)
sdpBindTlsRestProtSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsRestProtSrcMac.setStatus("current")


class _SdpBindTlsRestProtSrcMacAction_Type(Integer32):
    """Custom type sdpBindTlsRestProtSrcMacAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("alarmOnly", 2),
          ("discardFrame", 3))
    )


_SdpBindTlsRestProtSrcMacAction_Type.__name__ = "Integer32"
_SdpBindTlsRestProtSrcMacAction_Object = MibTableColumn
sdpBindTlsRestProtSrcMacAction = _SdpBindTlsRestProtSrcMacAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 53),
    _SdpBindTlsRestProtSrcMacAction_Type()
)
sdpBindTlsRestProtSrcMacAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsRestProtSrcMacAction.setStatus("current")


class _SdpBindTlsAutoLearnMacProtect_Type(TruthValue):
    """Custom type sdpBindTlsAutoLearnMacProtect based on TruthValue"""
    defaultValue = 2


_SdpBindTlsAutoLearnMacProtect_Type.__name__ = "TruthValue"
_SdpBindTlsAutoLearnMacProtect_Object = MibTableColumn
sdpBindTlsAutoLearnMacProtect = _SdpBindTlsAutoLearnMacProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 54),
    _SdpBindTlsAutoLearnMacProtect_Type()
)
sdpBindTlsAutoLearnMacProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsAutoLearnMacProtect.setStatus("current")


class _SdpBindDisableSendBvplsEvpnFlush_Type(TruthValue):
    """Custom type sdpBindDisableSendBvplsEvpnFlush based on TruthValue"""
    defaultValue = 2


_SdpBindDisableSendBvplsEvpnFlush_Type.__name__ = "TruthValue"
_SdpBindDisableSendBvplsEvpnFlush_Object = MibTableColumn
sdpBindDisableSendBvplsEvpnFlush = _SdpBindDisableSendBvplsEvpnFlush_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 55),
    _SdpBindDisableSendBvplsEvpnFlush_Type()
)
sdpBindDisableSendBvplsEvpnFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindDisableSendBvplsEvpnFlush.setStatus("current")
_SdpBindTlsRestProtSrcMacOper_Type = TruthValue
_SdpBindTlsRestProtSrcMacOper_Object = MibTableColumn
sdpBindTlsRestProtSrcMacOper = _SdpBindTlsRestProtSrcMacOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 56),
    _SdpBindTlsRestProtSrcMacOper_Type()
)
sdpBindTlsRestProtSrcMacOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsRestProtSrcMacOper.setStatus("current")


class _SdpBindTlsRestProtSrcMacOperAct_Type(Integer32):
    """Custom type sdpBindTlsRestProtSrcMacOperAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("alarmOnly", 2),
          ("discardFrame", 3))
    )


_SdpBindTlsRestProtSrcMacOperAct_Type.__name__ = "Integer32"
_SdpBindTlsRestProtSrcMacOperAct_Object = MibTableColumn
sdpBindTlsRestProtSrcMacOperAct = _SdpBindTlsRestProtSrcMacOperAct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 57),
    _SdpBindTlsRestProtSrcMacOperAct_Type()
)
sdpBindTlsRestProtSrcMacOperAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsRestProtSrcMacOperAct.setStatus("current")


class _SdpBindTlsAutoLrnMacPrtExcList_Type(TNamedItemOrEmpty):
    """Custom type sdpBindTlsAutoLrnMacPrtExcList based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_SdpBindTlsAutoLrnMacPrtExcList_Type.__name__ = "TNamedItemOrEmpty"
_SdpBindTlsAutoLrnMacPrtExcList_Object = MibTableColumn
sdpBindTlsAutoLrnMacPrtExcList = _SdpBindTlsAutoLrnMacPrtExcList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 58),
    _SdpBindTlsAutoLrnMacPrtExcList_Type()
)
sdpBindTlsAutoLrnMacPrtExcList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsAutoLrnMacPrtExcList.setStatus("current")
_SdpBindTlsLastMgmtChange_Type = TimeStamp
_SdpBindTlsLastMgmtChange_Object = MibTableColumn
sdpBindTlsLastMgmtChange = _SdpBindTlsLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 59),
    _SdpBindTlsLastMgmtChange_Type()
)
sdpBindTlsLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsLastMgmtChange.setStatus("current")
_SdpBindMeshTlsTable_Object = MibTable
sdpBindMeshTlsTable = _SdpBindMeshTlsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 7)
)
if mibBuilder.loadTexts:
    sdpBindMeshTlsTable.setStatus("current")
_SdpBindMeshTlsEntry_Object = MibTableRow
sdpBindMeshTlsEntry = _SdpBindMeshTlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 7, 1)
)
sdpBindMeshTlsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindMeshTlsEntry.setStatus("current")
_SdpBindMeshTlsPortState_Type = TStpPortState
_SdpBindMeshTlsPortState_Object = MibTableColumn
sdpBindMeshTlsPortState = _SdpBindMeshTlsPortState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 7, 1, 1),
    _SdpBindMeshTlsPortState_Type()
)
sdpBindMeshTlsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindMeshTlsPortState.setStatus("current")


class _SdpBindMeshTlsHoldDownTimer_Type(Integer32):
    """Custom type sdpBindMeshTlsHoldDownTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-active", 1),
          ("active", 2))
    )


_SdpBindMeshTlsHoldDownTimer_Type.__name__ = "Integer32"
_SdpBindMeshTlsHoldDownTimer_Object = MibTableColumn
sdpBindMeshTlsHoldDownTimer = _SdpBindMeshTlsHoldDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 7, 1, 2),
    _SdpBindMeshTlsHoldDownTimer_Type()
)
sdpBindMeshTlsHoldDownTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindMeshTlsHoldDownTimer.setStatus("current")


class _SdpBindMeshTlsTransitionState_Type(Integer32):
    """Custom type sdpBindMeshTlsTransitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 1),
          ("waiting-for-agreement", 2),
          ("agreement-received", 3))
    )


_SdpBindMeshTlsTransitionState_Type.__name__ = "Integer32"
_SdpBindMeshTlsTransitionState_Object = MibTableColumn
sdpBindMeshTlsTransitionState = _SdpBindMeshTlsTransitionState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 7, 1, 3),
    _SdpBindMeshTlsTransitionState_Type()
)
sdpBindMeshTlsTransitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindMeshTlsTransitionState.setStatus("current")
_SdpBindMeshTlsNotInMstRegion_Type = TruthValue
_SdpBindMeshTlsNotInMstRegion_Object = MibTableColumn
sdpBindMeshTlsNotInMstRegion = _SdpBindMeshTlsNotInMstRegion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 7, 1, 4),
    _SdpBindMeshTlsNotInMstRegion_Type()
)
sdpBindMeshTlsNotInMstRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindMeshTlsNotInMstRegion.setStatus("current")


class _SdpBindMeshTlsRestProtSrcMac_Type(TruthValue):
    """Custom type sdpBindMeshTlsRestProtSrcMac based on TruthValue"""
    defaultValue = 2


_SdpBindMeshTlsRestProtSrcMac_Type.__name__ = "TruthValue"
_SdpBindMeshTlsRestProtSrcMac_Object = MibTableColumn
sdpBindMeshTlsRestProtSrcMac = _SdpBindMeshTlsRestProtSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 7, 1, 5),
    _SdpBindMeshTlsRestProtSrcMac_Type()
)
sdpBindMeshTlsRestProtSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindMeshTlsRestProtSrcMac.setStatus("current")


class _SdpBindMeshTlsRestProtSrcMacAct_Type(Integer32):
    """Custom type sdpBindMeshTlsRestProtSrcMacAct based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("alarmOnly", 2),
          ("discardFrame", 3))
    )


_SdpBindMeshTlsRestProtSrcMacAct_Type.__name__ = "Integer32"
_SdpBindMeshTlsRestProtSrcMacAct_Object = MibTableColumn
sdpBindMeshTlsRestProtSrcMacAct = _SdpBindMeshTlsRestProtSrcMacAct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 7, 1, 6),
    _SdpBindMeshTlsRestProtSrcMacAct_Type()
)
sdpBindMeshTlsRestProtSrcMacAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindMeshTlsRestProtSrcMacAct.setStatus("current")


class _SdpBindMeshTlsAutoLearnMacProt_Type(TruthValue):
    """Custom type sdpBindMeshTlsAutoLearnMacProt based on TruthValue"""
    defaultValue = 2


_SdpBindMeshTlsAutoLearnMacProt_Type.__name__ = "TruthValue"
_SdpBindMeshTlsAutoLearnMacProt_Object = MibTableColumn
sdpBindMeshTlsAutoLearnMacProt = _SdpBindMeshTlsAutoLearnMacProt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 7, 1, 7),
    _SdpBindMeshTlsAutoLearnMacProt_Type()
)
sdpBindMeshTlsAutoLearnMacProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindMeshTlsAutoLearnMacProt.setStatus("current")
_SdpBindMeshTlsRPSMacOper_Type = TruthValue
_SdpBindMeshTlsRPSMacOper_Object = MibTableColumn
sdpBindMeshTlsRPSMacOper = _SdpBindMeshTlsRPSMacOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 7, 1, 8),
    _SdpBindMeshTlsRPSMacOper_Type()
)
sdpBindMeshTlsRPSMacOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindMeshTlsRPSMacOper.setStatus("current")


class _SdpBindMeshTlsRPSMacOperAct_Type(Integer32):
    """Custom type sdpBindMeshTlsRPSMacOperAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("alarmOnly", 2),
          ("discardFrame", 3))
    )


_SdpBindMeshTlsRPSMacOperAct_Type.__name__ = "Integer32"
_SdpBindMeshTlsRPSMacOperAct_Object = MibTableColumn
sdpBindMeshTlsRPSMacOperAct = _SdpBindMeshTlsRPSMacOperAct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 7, 1, 9),
    _SdpBindMeshTlsRPSMacOperAct_Type()
)
sdpBindMeshTlsRPSMacOperAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindMeshTlsRPSMacOperAct.setStatus("current")


class _SdpBindMeshTlsAutLrnMacPrtExcLs_Type(TNamedItemOrEmpty):
    """Custom type sdpBindMeshTlsAutLrnMacPrtExcLs based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_SdpBindMeshTlsAutLrnMacPrtExcLs_Type.__name__ = "TNamedItemOrEmpty"
_SdpBindMeshTlsAutLrnMacPrtExcLs_Object = MibTableColumn
sdpBindMeshTlsAutLrnMacPrtExcLs = _SdpBindMeshTlsAutLrnMacPrtExcLs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 7, 1, 10),
    _SdpBindMeshTlsAutLrnMacPrtExcLs_Type()
)
sdpBindMeshTlsAutLrnMacPrtExcLs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindMeshTlsAutLrnMacPrtExcLs.setStatus("current")
_SdpBindApipeTable_Object = MibTable
sdpBindApipeTable = _SdpBindApipeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 8)
)
if mibBuilder.loadTexts:
    sdpBindApipeTable.setStatus("current")
_SdpBindApipeEntry_Object = MibTableRow
sdpBindApipeEntry = _SdpBindApipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 8, 1)
)
sdpBindApipeEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindApipeEntry.setStatus("current")


class _SdpBindApipeAdminConcatCellCount_Type(Integer32):
    """Custom type sdpBindApipeAdminConcatCellCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SdpBindApipeAdminConcatCellCount_Type.__name__ = "Integer32"
_SdpBindApipeAdminConcatCellCount_Object = MibTableColumn
sdpBindApipeAdminConcatCellCount = _SdpBindApipeAdminConcatCellCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 8, 1, 1),
    _SdpBindApipeAdminConcatCellCount_Type()
)
sdpBindApipeAdminConcatCellCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindApipeAdminConcatCellCount.setStatus("current")


class _SdpBindApipeSigConcatCellCount_Type(Integer32):
    """Custom type sdpBindApipeSigConcatCellCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SdpBindApipeSigConcatCellCount_Type.__name__ = "Integer32"
_SdpBindApipeSigConcatCellCount_Object = MibTableColumn
sdpBindApipeSigConcatCellCount = _SdpBindApipeSigConcatCellCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 8, 1, 2),
    _SdpBindApipeSigConcatCellCount_Type()
)
sdpBindApipeSigConcatCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindApipeSigConcatCellCount.setStatus("current")


class _SdpBindApipeOperConcatCellCount_Type(Integer32):
    """Custom type sdpBindApipeOperConcatCellCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SdpBindApipeOperConcatCellCount_Type.__name__ = "Integer32"
_SdpBindApipeOperConcatCellCount_Object = MibTableColumn
sdpBindApipeOperConcatCellCount = _SdpBindApipeOperConcatCellCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 8, 1, 3),
    _SdpBindApipeOperConcatCellCount_Type()
)
sdpBindApipeOperConcatCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindApipeOperConcatCellCount.setStatus("current")


class _SdpBindApipeConcatMaxDelay_Type(Integer32):
    """Custom type sdpBindApipeConcatMaxDelay based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_SdpBindApipeConcatMaxDelay_Type.__name__ = "Integer32"
_SdpBindApipeConcatMaxDelay_Object = MibTableColumn
sdpBindApipeConcatMaxDelay = _SdpBindApipeConcatMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 8, 1, 4),
    _SdpBindApipeConcatMaxDelay_Type()
)
sdpBindApipeConcatMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindApipeConcatMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindApipeConcatMaxDelay.setUnits("hundreds of microseconds")


class _SdpBindApipeConcatCellClp_Type(TruthValue):
    """Custom type sdpBindApipeConcatCellClp based on TruthValue"""
    defaultValue = 2


_SdpBindApipeConcatCellClp_Type.__name__ = "TruthValue"
_SdpBindApipeConcatCellClp_Object = MibTableColumn
sdpBindApipeConcatCellClp = _SdpBindApipeConcatCellClp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 8, 1, 5),
    _SdpBindApipeConcatCellClp_Type()
)
sdpBindApipeConcatCellClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindApipeConcatCellClp.setStatus("current")


class _SdpBindApipeConcatCellAal5Fr_Type(TruthValue):
    """Custom type sdpBindApipeConcatCellAal5Fr based on TruthValue"""
    defaultValue = 2


_SdpBindApipeConcatCellAal5Fr_Type.__name__ = "TruthValue"
_SdpBindApipeConcatCellAal5Fr_Object = MibTableColumn
sdpBindApipeConcatCellAal5Fr = _SdpBindApipeConcatCellAal5Fr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 8, 1, 6),
    _SdpBindApipeConcatCellAal5Fr_Type()
)
sdpBindApipeConcatCellAal5Fr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindApipeConcatCellAal5Fr.setStatus("current")
_SdpBindDhcpInfoTable_Object = MibTable
sdpBindDhcpInfoTable = _SdpBindDhcpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 9)
)
if mibBuilder.loadTexts:
    sdpBindDhcpInfoTable.setStatus("current")
_SdpBindDhcpInfoEntry_Object = MibTableRow
sdpBindDhcpInfoEntry = _SdpBindDhcpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 9, 1)
)
sdpBindDhcpInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindDhcpInfoEntry.setStatus("current")


class _SdpBindDhcpDescription_Type(ServObjDesc):
    """Custom type sdpBindDhcpDescription based on ServObjDesc"""
    defaultHexValue = ""


_SdpBindDhcpDescription_Type.__name__ = "ServObjDesc"
_SdpBindDhcpDescription_Object = MibTableColumn
sdpBindDhcpDescription = _SdpBindDhcpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 9, 1, 1),
    _SdpBindDhcpDescription_Type()
)
sdpBindDhcpDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindDhcpDescription.setStatus("current")


class _SdpBindDhcpSnoop_Type(TmnxEnabledDisabled):
    """Custom type sdpBindDhcpSnoop based on TmnxEnabledDisabled"""
    defaultValue = 2


_SdpBindDhcpSnoop_Type.__name__ = "TmnxEnabledDisabled"
_SdpBindDhcpSnoop_Object = MibTableColumn
sdpBindDhcpSnoop = _SdpBindDhcpSnoop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 9, 1, 2),
    _SdpBindDhcpSnoop_Type()
)
sdpBindDhcpSnoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindDhcpSnoop.setStatus("current")
_SdpBindDhcpStatsTable_Object = MibTable
sdpBindDhcpStatsTable = _SdpBindDhcpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10)
)
if mibBuilder.loadTexts:
    sdpBindDhcpStatsTable.setStatus("current")
_SdpBindDhcpStatsEntry_Object = MibTableRow
sdpBindDhcpStatsEntry = _SdpBindDhcpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1)
)
sdpBindDhcpStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindDhcpStatsEntry.setStatus("current")
_SdpBindDhcpStatsClntSnoopdPckts_Type = Counter32
_SdpBindDhcpStatsClntSnoopdPckts_Object = MibTableColumn
sdpBindDhcpStatsClntSnoopdPckts = _SdpBindDhcpStatsClntSnoopdPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 1),
    _SdpBindDhcpStatsClntSnoopdPckts_Type()
)
sdpBindDhcpStatsClntSnoopdPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsClntSnoopdPckts.setStatus("current")
_SdpBindDhcpStatsSrvrSnoopdPckts_Type = Counter32
_SdpBindDhcpStatsSrvrSnoopdPckts_Object = MibTableColumn
sdpBindDhcpStatsSrvrSnoopdPckts = _SdpBindDhcpStatsSrvrSnoopdPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 2),
    _SdpBindDhcpStatsSrvrSnoopdPckts_Type()
)
sdpBindDhcpStatsSrvrSnoopdPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsSrvrSnoopdPckts.setStatus("current")
_SdpBindDhcpStatsClntForwdPckts_Type = Counter32
_SdpBindDhcpStatsClntForwdPckts_Object = MibTableColumn
sdpBindDhcpStatsClntForwdPckts = _SdpBindDhcpStatsClntForwdPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 3),
    _SdpBindDhcpStatsClntForwdPckts_Type()
)
sdpBindDhcpStatsClntForwdPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsClntForwdPckts.setStatus("current")
_SdpBindDhcpStatsSrvrForwdPckts_Type = Counter32
_SdpBindDhcpStatsSrvrForwdPckts_Object = MibTableColumn
sdpBindDhcpStatsSrvrForwdPckts = _SdpBindDhcpStatsSrvrForwdPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 4),
    _SdpBindDhcpStatsSrvrForwdPckts_Type()
)
sdpBindDhcpStatsSrvrForwdPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsSrvrForwdPckts.setStatus("current")
_SdpBindDhcpStatsClntDropdPckts_Type = Counter32
_SdpBindDhcpStatsClntDropdPckts_Object = MibTableColumn
sdpBindDhcpStatsClntDropdPckts = _SdpBindDhcpStatsClntDropdPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 5),
    _SdpBindDhcpStatsClntDropdPckts_Type()
)
sdpBindDhcpStatsClntDropdPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsClntDropdPckts.setStatus("current")
_SdpBindDhcpStatsSrvrDropdPckts_Type = Counter32
_SdpBindDhcpStatsSrvrDropdPckts_Object = MibTableColumn
sdpBindDhcpStatsSrvrDropdPckts = _SdpBindDhcpStatsSrvrDropdPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 6),
    _SdpBindDhcpStatsSrvrDropdPckts_Type()
)
sdpBindDhcpStatsSrvrDropdPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsSrvrDropdPckts.setStatus("current")
_SdpBindDhcpStatsClntProxRadPckts_Type = Counter32
_SdpBindDhcpStatsClntProxRadPckts_Object = MibTableColumn
sdpBindDhcpStatsClntProxRadPckts = _SdpBindDhcpStatsClntProxRadPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 7),
    _SdpBindDhcpStatsClntProxRadPckts_Type()
)
sdpBindDhcpStatsClntProxRadPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsClntProxRadPckts.setStatus("current")
_SdpBindDhcpStatsClntProxLSPckts_Type = Counter32
_SdpBindDhcpStatsClntProxLSPckts_Object = MibTableColumn
sdpBindDhcpStatsClntProxLSPckts = _SdpBindDhcpStatsClntProxLSPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 8),
    _SdpBindDhcpStatsClntProxLSPckts_Type()
)
sdpBindDhcpStatsClntProxLSPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsClntProxLSPckts.setStatus("current")
_SdpBindDhcpStatsGenReleasePckts_Type = Counter32
_SdpBindDhcpStatsGenReleasePckts_Object = MibTableColumn
sdpBindDhcpStatsGenReleasePckts = _SdpBindDhcpStatsGenReleasePckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 9),
    _SdpBindDhcpStatsGenReleasePckts_Type()
)
sdpBindDhcpStatsGenReleasePckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsGenReleasePckts.setStatus("current")
_SdpBindDhcpStatsGenForceRenPckts_Type = Counter32
_SdpBindDhcpStatsGenForceRenPckts_Object = MibTableColumn
sdpBindDhcpStatsGenForceRenPckts = _SdpBindDhcpStatsGenForceRenPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 10),
    _SdpBindDhcpStatsGenForceRenPckts_Type()
)
sdpBindDhcpStatsGenForceRenPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsGenForceRenPckts.setStatus("current")
_SdpBindDhcpStatsClntProxUDBPckts_Type = Counter32
_SdpBindDhcpStatsClntProxUDBPckts_Object = MibTableColumn
sdpBindDhcpStatsClntProxUDBPckts = _SdpBindDhcpStatsClntProxUDBPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 11),
    _SdpBindDhcpStatsClntProxUDBPckts_Type()
)
sdpBindDhcpStatsClntProxUDBPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsClntProxUDBPckts.setStatus("current")
_SdpBindDhcpStatsClntProxNqPckts_Type = Counter32
_SdpBindDhcpStatsClntProxNqPckts_Object = MibTableColumn
sdpBindDhcpStatsClntProxNqPckts = _SdpBindDhcpStatsClntProxNqPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 12),
    _SdpBindDhcpStatsClntProxNqPckts_Type()
)
sdpBindDhcpStatsClntProxNqPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsClntProxNqPckts.setStatus("current")
_SdpBindIpipeTable_Object = MibTable
sdpBindIpipeTable = _SdpBindIpipeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 11)
)
if mibBuilder.loadTexts:
    sdpBindIpipeTable.setStatus("current")
_SdpBindIpipeEntry_Object = MibTableRow
sdpBindIpipeEntry = _SdpBindIpipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 11, 1)
)
sdpBindIpipeEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindIpipeEntry.setStatus("current")
_SdpBindIpipeCeInetAddressType_Type = InetAddressType
_SdpBindIpipeCeInetAddressType_Object = MibTableColumn
sdpBindIpipeCeInetAddressType = _SdpBindIpipeCeInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 11, 1, 1),
    _SdpBindIpipeCeInetAddressType_Type()
)
sdpBindIpipeCeInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindIpipeCeInetAddressType.setStatus("current")


class _SdpBindIpipeCeInetAddress_Type(InetAddress):
    """Custom type sdpBindIpipeCeInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_SdpBindIpipeCeInetAddress_Type.__name__ = "InetAddress"
_SdpBindIpipeCeInetAddress_Object = MibTableColumn
sdpBindIpipeCeInetAddress = _SdpBindIpipeCeInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 11, 1, 2),
    _SdpBindIpipeCeInetAddress_Type()
)
sdpBindIpipeCeInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindIpipeCeInetAddress.setStatus("current")
_SdpBindIpipePeerCeInetAddrType_Type = InetAddressType
_SdpBindIpipePeerCeInetAddrType_Object = MibTableColumn
sdpBindIpipePeerCeInetAddrType = _SdpBindIpipePeerCeInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 11, 1, 3),
    _SdpBindIpipePeerCeInetAddrType_Type()
)
sdpBindIpipePeerCeInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindIpipePeerCeInetAddrType.setStatus("current")


class _SdpBindIpipePeerCeInetAddr_Type(InetAddress):
    """Custom type sdpBindIpipePeerCeInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_SdpBindIpipePeerCeInetAddr_Type.__name__ = "InetAddress"
_SdpBindIpipePeerCeInetAddr_Object = MibTableColumn
sdpBindIpipePeerCeInetAddr = _SdpBindIpipePeerCeInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 11, 1, 4),
    _SdpBindIpipePeerCeInetAddr_Type()
)
sdpBindIpipePeerCeInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindIpipePeerCeInetAddr.setStatus("current")
_SdpBindIpipePeerIpv6Capability_Type = TruthValue
_SdpBindIpipePeerIpv6Capability_Object = MibTableColumn
sdpBindIpipePeerIpv6Capability = _SdpBindIpipePeerIpv6Capability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 11, 1, 5),
    _SdpBindIpipePeerIpv6Capability_Type()
)
sdpBindIpipePeerIpv6Capability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindIpipePeerIpv6Capability.setStatus("current")


class _SdpBindIpipePeerLLCeInetAddr_Type(InetAddress):
    """Custom type sdpBindIpipePeerLLCeInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_SdpBindIpipePeerLLCeInetAddr_Type.__name__ = "InetAddress"
_SdpBindIpipePeerLLCeInetAddr_Object = MibTableColumn
sdpBindIpipePeerLLCeInetAddr = _SdpBindIpipePeerLLCeInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 11, 1, 6),
    _SdpBindIpipePeerLLCeInetAddr_Type()
)
sdpBindIpipePeerLLCeInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindIpipePeerLLCeInetAddr.setStatus("current")


class _SdpBindIpipePeerGlobalCeInetAddr_Type(InetAddress):
    """Custom type sdpBindIpipePeerGlobalCeInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_SdpBindIpipePeerGlobalCeInetAddr_Type.__name__ = "InetAddress"
_SdpBindIpipePeerGlobalCeInetAddr_Object = MibTableColumn
sdpBindIpipePeerGlobalCeInetAddr = _SdpBindIpipePeerGlobalCeInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 11, 1, 7),
    _SdpBindIpipePeerGlobalCeInetAddr_Type()
)
sdpBindIpipePeerGlobalCeInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindIpipePeerGlobalCeInetAddr.setStatus("current")
_SdpFCMappingTable_Object = MibTable
sdpFCMappingTable = _SdpFCMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 12)
)
if mibBuilder.loadTexts:
    sdpFCMappingTable.setStatus("current")
_SdpFCMappingEntry_Object = MibTableRow
sdpFCMappingEntry = _SdpFCMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 12, 1)
)
sdpFCMappingEntry.setIndexNames(
    (0, "TIMETRA-SDP-MIB", "sdpId"),
    (0, "TIMETRA-SDP-MIB", "sdpFCMappingFCName"),
)
if mibBuilder.loadTexts:
    sdpFCMappingEntry.setStatus("current")
_SdpFCMappingFCName_Type = TNamedItem
_SdpFCMappingFCName_Object = MibTableColumn
sdpFCMappingFCName = _SdpFCMappingFCName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 12, 1, 1),
    _SdpFCMappingFCName_Type()
)
sdpFCMappingFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpFCMappingFCName.setStatus("current")
_SdpFCMappingRowStatus_Type = RowStatus
_SdpFCMappingRowStatus_Object = MibTableColumn
sdpFCMappingRowStatus = _SdpFCMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 12, 1, 2),
    _SdpFCMappingRowStatus_Type()
)
sdpFCMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpFCMappingRowStatus.setStatus("current")
_SdpFCMappingLspId_Type = TmnxVRtrMplsLspID
_SdpFCMappingLspId_Object = MibTableColumn
sdpFCMappingLspId = _SdpFCMappingLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 12, 1, 3),
    _SdpFCMappingLspId_Type()
)
sdpFCMappingLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpFCMappingLspId.setStatus("current")
_SdpBindTlsMfibAllowedMdaTable_Object = MibTable
sdpBindTlsMfibAllowedMdaTable = _SdpBindTlsMfibAllowedMdaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 13)
)
if mibBuilder.loadTexts:
    sdpBindTlsMfibAllowedMdaTable.setStatus("current")
_SdpBindTlsMfibAllowedMdaEntry_Object = MibTableRow
sdpBindTlsMfibAllowedMdaEntry = _SdpBindTlsMfibAllowedMdaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 13, 1)
)
sdpBindTlsMfibAllowedMdaEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    sdpBindTlsMfibAllowedMdaEntry.setStatus("current")
_SdpBindTlsMfibMdaRowStatus_Type = RowStatus
_SdpBindTlsMfibMdaRowStatus_Object = MibTableColumn
sdpBindTlsMfibMdaRowStatus = _SdpBindTlsMfibMdaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 13, 1, 1),
    _SdpBindTlsMfibMdaRowStatus_Type()
)
sdpBindTlsMfibMdaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindTlsMfibMdaRowStatus.setStatus("current")
_SdpBindCpipeTable_Object = MibTable
sdpBindCpipeTable = _SdpBindCpipeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15)
)
if mibBuilder.loadTexts:
    sdpBindCpipeTable.setStatus("current")
_SdpBindCpipeEntry_Object = MibTableRow
sdpBindCpipeEntry = _SdpBindCpipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1)
)
sdpBindCpipeEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindCpipeEntry.setStatus("current")
_SdpBindCpipeLocalPayloadSize_Type = Unsigned32
_SdpBindCpipeLocalPayloadSize_Object = MibTableColumn
sdpBindCpipeLocalPayloadSize = _SdpBindCpipeLocalPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 1),
    _SdpBindCpipeLocalPayloadSize_Type()
)
sdpBindCpipeLocalPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalPayloadSize.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalPayloadSize.setUnits("bytes")
_SdpBindCpipePeerPayloadSize_Type = Unsigned32
_SdpBindCpipePeerPayloadSize_Object = MibTableColumn
sdpBindCpipePeerPayloadSize = _SdpBindCpipePeerPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 2),
    _SdpBindCpipePeerPayloadSize_Type()
)
sdpBindCpipePeerPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipePeerPayloadSize.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindCpipePeerPayloadSize.setUnits("bytes")
_SdpBindCpipeLocalBitrate_Type = Unsigned32
_SdpBindCpipeLocalBitrate_Object = MibTableColumn
sdpBindCpipeLocalBitrate = _SdpBindCpipeLocalBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 3),
    _SdpBindCpipeLocalBitrate_Type()
)
sdpBindCpipeLocalBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalBitrate.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalBitrate.setUnits("sixty-four kilobps")
_SdpBindCpipePeerBitrate_Type = Unsigned32
_SdpBindCpipePeerBitrate_Object = MibTableColumn
sdpBindCpipePeerBitrate = _SdpBindCpipePeerBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 4),
    _SdpBindCpipePeerBitrate_Type()
)
sdpBindCpipePeerBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipePeerBitrate.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindCpipePeerBitrate.setUnits("sixty-four kilobps")
_SdpBindCpipeLocalSigPkts_Type = TdmOptionsSigPkts
_SdpBindCpipeLocalSigPkts_Object = MibTableColumn
sdpBindCpipeLocalSigPkts = _SdpBindCpipeLocalSigPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 5),
    _SdpBindCpipeLocalSigPkts_Type()
)
sdpBindCpipeLocalSigPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalSigPkts.setStatus("current")
_SdpBindCpipePeerSigPkts_Type = TdmOptionsSigPkts
_SdpBindCpipePeerSigPkts_Object = MibTableColumn
sdpBindCpipePeerSigPkts = _SdpBindCpipePeerSigPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 6),
    _SdpBindCpipePeerSigPkts_Type()
)
sdpBindCpipePeerSigPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipePeerSigPkts.setStatus("current")
_SdpBindCpipeLocalCasTrunkFraming_Type = TdmOptionsCasTrunkFraming
_SdpBindCpipeLocalCasTrunkFraming_Object = MibTableColumn
sdpBindCpipeLocalCasTrunkFraming = _SdpBindCpipeLocalCasTrunkFraming_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 7),
    _SdpBindCpipeLocalCasTrunkFraming_Type()
)
sdpBindCpipeLocalCasTrunkFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalCasTrunkFraming.setStatus("current")
_SdpBindCpipePeerCasTrunkFraming_Type = TdmOptionsCasTrunkFraming
_SdpBindCpipePeerCasTrunkFraming_Object = MibTableColumn
sdpBindCpipePeerCasTrunkFraming = _SdpBindCpipePeerCasTrunkFraming_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 8),
    _SdpBindCpipePeerCasTrunkFraming_Type()
)
sdpBindCpipePeerCasTrunkFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipePeerCasTrunkFraming.setStatus("current")
_SdpBindCpipeLocalUseRtpHeader_Type = TruthValue
_SdpBindCpipeLocalUseRtpHeader_Object = MibTableColumn
sdpBindCpipeLocalUseRtpHeader = _SdpBindCpipeLocalUseRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 9),
    _SdpBindCpipeLocalUseRtpHeader_Type()
)
sdpBindCpipeLocalUseRtpHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalUseRtpHeader.setStatus("current")
_SdpBindCpipePeerUseRtpHeader_Type = TruthValue
_SdpBindCpipePeerUseRtpHeader_Object = MibTableColumn
sdpBindCpipePeerUseRtpHeader = _SdpBindCpipePeerUseRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 10),
    _SdpBindCpipePeerUseRtpHeader_Type()
)
sdpBindCpipePeerUseRtpHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipePeerUseRtpHeader.setStatus("current")
_SdpBindCpipeLocalDifferential_Type = TruthValue
_SdpBindCpipeLocalDifferential_Object = MibTableColumn
sdpBindCpipeLocalDifferential = _SdpBindCpipeLocalDifferential_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 11),
    _SdpBindCpipeLocalDifferential_Type()
)
sdpBindCpipeLocalDifferential.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalDifferential.setStatus("current")
_SdpBindCpipePeerDifferential_Type = TruthValue
_SdpBindCpipePeerDifferential_Object = MibTableColumn
sdpBindCpipePeerDifferential = _SdpBindCpipePeerDifferential_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 12),
    _SdpBindCpipePeerDifferential_Type()
)
sdpBindCpipePeerDifferential.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipePeerDifferential.setStatus("current")
_SdpBindCpipeLocalTimestampFreq_Type = Unsigned32
_SdpBindCpipeLocalTimestampFreq_Object = MibTableColumn
sdpBindCpipeLocalTimestampFreq = _SdpBindCpipeLocalTimestampFreq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 13),
    _SdpBindCpipeLocalTimestampFreq_Type()
)
sdpBindCpipeLocalTimestampFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalTimestampFreq.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalTimestampFreq.setUnits("8 KHz")
_SdpBindCpipePeerTimestampFreq_Type = Unsigned32
_SdpBindCpipePeerTimestampFreq_Object = MibTableColumn
sdpBindCpipePeerTimestampFreq = _SdpBindCpipePeerTimestampFreq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 14),
    _SdpBindCpipePeerTimestampFreq_Type()
)
sdpBindCpipePeerTimestampFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipePeerTimestampFreq.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindCpipePeerTimestampFreq.setUnits("8 KHz")
_SdpBindTlsL2ptStatsTable_Object = MibTable
sdpBindTlsL2ptStatsTable = _SdpBindTlsL2ptStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16)
)
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsTable.setStatus("current")
_SdpBindTlsL2ptStatsEntry_Object = MibTableRow
sdpBindTlsL2ptStatsEntry = _SdpBindTlsL2ptStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1)
)
sdpBindTlsL2ptStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsEntry.setStatus("current")
_SdpBindTlsL2ptStatsLastClearedTime_Type = TimeStamp
_SdpBindTlsL2ptStatsLastClearedTime_Object = MibTableColumn
sdpBindTlsL2ptStatsLastClearedTime = _SdpBindTlsL2ptStatsLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 1),
    _SdpBindTlsL2ptStatsLastClearedTime_Type()
)
sdpBindTlsL2ptStatsLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsLastClearedTime.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 2),
    _SdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 3),
    _SdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 4),
    _SdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 5),
    _SdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 6),
    _SdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 7),
    _SdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 8),
    _SdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 9),
    _SdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 10),
    _SdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 11),
    _SdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 12),
    _SdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 13),
    _SdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsStpConfigBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsStpConfigBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsStpConfigBpdusRx = _SdpBindTlsL2ptStatsStpConfigBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 14),
    _SdpBindTlsL2ptStatsStpConfigBpdusRx_Type()
)
sdpBindTlsL2ptStatsStpConfigBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsStpConfigBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsStpConfigBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsStpConfigBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsStpConfigBpdusTx = _SdpBindTlsL2ptStatsStpConfigBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 15),
    _SdpBindTlsL2ptStatsStpConfigBpdusTx_Type()
)
sdpBindTlsL2ptStatsStpConfigBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsStpConfigBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsStpRstBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsStpRstBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsStpRstBpdusRx = _SdpBindTlsL2ptStatsStpRstBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 16),
    _SdpBindTlsL2ptStatsStpRstBpdusRx_Type()
)
sdpBindTlsL2ptStatsStpRstBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsStpRstBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsStpRstBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsStpRstBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsStpRstBpdusTx = _SdpBindTlsL2ptStatsStpRstBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 17),
    _SdpBindTlsL2ptStatsStpRstBpdusTx_Type()
)
sdpBindTlsL2ptStatsStpRstBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsStpRstBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsStpTcnBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsStpTcnBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsStpTcnBpdusRx = _SdpBindTlsL2ptStatsStpTcnBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 18),
    _SdpBindTlsL2ptStatsStpTcnBpdusRx_Type()
)
sdpBindTlsL2ptStatsStpTcnBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsStpTcnBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsStpTcnBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsStpTcnBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsStpTcnBpdusTx = _SdpBindTlsL2ptStatsStpTcnBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 19),
    _SdpBindTlsL2ptStatsStpTcnBpdusTx_Type()
)
sdpBindTlsL2ptStatsStpTcnBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsStpTcnBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsPvstConfigBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsPvstConfigBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsPvstConfigBpdusRx = _SdpBindTlsL2ptStatsPvstConfigBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 20),
    _SdpBindTlsL2ptStatsPvstConfigBpdusRx_Type()
)
sdpBindTlsL2ptStatsPvstConfigBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsPvstConfigBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsPvstConfigBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsPvstConfigBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsPvstConfigBpdusTx = _SdpBindTlsL2ptStatsPvstConfigBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 21),
    _SdpBindTlsL2ptStatsPvstConfigBpdusTx_Type()
)
sdpBindTlsL2ptStatsPvstConfigBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsPvstConfigBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsPvstRstBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsPvstRstBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsPvstRstBpdusRx = _SdpBindTlsL2ptStatsPvstRstBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 22),
    _SdpBindTlsL2ptStatsPvstRstBpdusRx_Type()
)
sdpBindTlsL2ptStatsPvstRstBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsPvstRstBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsPvstRstBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsPvstRstBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsPvstRstBpdusTx = _SdpBindTlsL2ptStatsPvstRstBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 23),
    _SdpBindTlsL2ptStatsPvstRstBpdusTx_Type()
)
sdpBindTlsL2ptStatsPvstRstBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsPvstRstBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsPvstTcnBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsPvstTcnBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsPvstTcnBpdusRx = _SdpBindTlsL2ptStatsPvstTcnBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 24),
    _SdpBindTlsL2ptStatsPvstTcnBpdusRx_Type()
)
sdpBindTlsL2ptStatsPvstTcnBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsPvstTcnBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsPvstTcnBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsPvstTcnBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsPvstTcnBpdusTx = _SdpBindTlsL2ptStatsPvstTcnBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 25),
    _SdpBindTlsL2ptStatsPvstTcnBpdusTx_Type()
)
sdpBindTlsL2ptStatsPvstTcnBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsPvstTcnBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsOtherBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsOtherBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsOtherBpdusRx = _SdpBindTlsL2ptStatsOtherBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 26),
    _SdpBindTlsL2ptStatsOtherBpdusRx_Type()
)
sdpBindTlsL2ptStatsOtherBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsOtherBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsOtherBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsOtherBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsOtherBpdusTx = _SdpBindTlsL2ptStatsOtherBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 27),
    _SdpBindTlsL2ptStatsOtherBpdusTx_Type()
)
sdpBindTlsL2ptStatsOtherBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsOtherBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsOtherL2ptBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsOtherL2ptBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsOtherL2ptBpdusRx = _SdpBindTlsL2ptStatsOtherL2ptBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 28),
    _SdpBindTlsL2ptStatsOtherL2ptBpdusRx_Type()
)
sdpBindTlsL2ptStatsOtherL2ptBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsOtherL2ptBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsOtherL2ptBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsOtherL2ptBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsOtherL2ptBpdusTx = _SdpBindTlsL2ptStatsOtherL2ptBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 29),
    _SdpBindTlsL2ptStatsOtherL2ptBpdusTx_Type()
)
sdpBindTlsL2ptStatsOtherL2ptBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsOtherL2ptBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsOtherInvalidBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsOtherInvalidBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsOtherInvalidBpdusRx = _SdpBindTlsL2ptStatsOtherInvalidBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 30),
    _SdpBindTlsL2ptStatsOtherInvalidBpdusRx_Type()
)
sdpBindTlsL2ptStatsOtherInvalidBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsOtherInvalidBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsOtherInvalidBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsOtherInvalidBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsOtherInvalidBpdusTx = _SdpBindTlsL2ptStatsOtherInvalidBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 31),
    _SdpBindTlsL2ptStatsOtherInvalidBpdusTx_Type()
)
sdpBindTlsL2ptStatsOtherInvalidBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsOtherInvalidBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 32),
    _SdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 33),
    _SdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 34),
    _SdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 35),
    _SdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 36),
    _SdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 37),
    _SdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 38),
    _SdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 39),
    _SdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 40),
    _SdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 41),
    _SdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsCdpBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsCdpBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsCdpBpdusRx = _SdpBindTlsL2ptStatsCdpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 42),
    _SdpBindTlsL2ptStatsCdpBpdusRx_Type()
)
sdpBindTlsL2ptStatsCdpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsCdpBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsCdpBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsCdpBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsCdpBpdusTx = _SdpBindTlsL2ptStatsCdpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 43),
    _SdpBindTlsL2ptStatsCdpBpdusTx_Type()
)
sdpBindTlsL2ptStatsCdpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsCdpBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsVtpBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsVtpBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsVtpBpdusRx = _SdpBindTlsL2ptStatsVtpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 44),
    _SdpBindTlsL2ptStatsVtpBpdusRx_Type()
)
sdpBindTlsL2ptStatsVtpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsVtpBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsVtpBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsVtpBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsVtpBpdusTx = _SdpBindTlsL2ptStatsVtpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 45),
    _SdpBindTlsL2ptStatsVtpBpdusTx_Type()
)
sdpBindTlsL2ptStatsVtpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsVtpBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsDtpBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsDtpBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsDtpBpdusRx = _SdpBindTlsL2ptStatsDtpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 46),
    _SdpBindTlsL2ptStatsDtpBpdusRx_Type()
)
sdpBindTlsL2ptStatsDtpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsDtpBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsDtpBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsDtpBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsDtpBpdusTx = _SdpBindTlsL2ptStatsDtpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 47),
    _SdpBindTlsL2ptStatsDtpBpdusTx_Type()
)
sdpBindTlsL2ptStatsDtpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsDtpBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsPagpBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsPagpBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsPagpBpdusRx = _SdpBindTlsL2ptStatsPagpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 48),
    _SdpBindTlsL2ptStatsPagpBpdusRx_Type()
)
sdpBindTlsL2ptStatsPagpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsPagpBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsPagpBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsPagpBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsPagpBpdusTx = _SdpBindTlsL2ptStatsPagpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 49),
    _SdpBindTlsL2ptStatsPagpBpdusTx_Type()
)
sdpBindTlsL2ptStatsPagpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsPagpBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsUdldBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsUdldBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsUdldBpdusRx = _SdpBindTlsL2ptStatsUdldBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 50),
    _SdpBindTlsL2ptStatsUdldBpdusRx_Type()
)
sdpBindTlsL2ptStatsUdldBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsUdldBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsUdldBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsUdldBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsUdldBpdusTx = _SdpBindTlsL2ptStatsUdldBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 51),
    _SdpBindTlsL2ptStatsUdldBpdusTx_Type()
)
sdpBindTlsL2ptStatsUdldBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsUdldBpdusTx.setStatus("current")
_PwTemplateTableLastChanged_Type = TimeStamp
_PwTemplateTableLastChanged_Object = MibScalar
pwTemplateTableLastChanged = _PwTemplateTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 17),
    _PwTemplateTableLastChanged_Type()
)
pwTemplateTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTemplateTableLastChanged.setStatus("current")
_PwTemplateTable_Object = MibTable
pwTemplateTable = _PwTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18)
)
if mibBuilder.loadTexts:
    pwTemplateTable.setStatus("current")
_PwTemplateEntry_Object = MibTableRow
pwTemplateEntry = _PwTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1)
)
pwTemplateEntry.setIndexNames(
    (0, "TIMETRA-SDP-MIB", "pwTemplateId"),
)
if mibBuilder.loadTexts:
    pwTemplateEntry.setStatus("current")
_PwTemplateId_Type = PWTemplateId
_PwTemplateId_Object = MibTableColumn
pwTemplateId = _PwTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 1),
    _PwTemplateId_Type()
)
pwTemplateId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwTemplateId.setStatus("current")
_PwTemplateRowStatus_Type = RowStatus
_PwTemplateRowStatus_Object = MibTableColumn
pwTemplateRowStatus = _PwTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 2),
    _PwTemplateRowStatus_Type()
)
pwTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateRowStatus.setStatus("current")
_PwTemplateLastChanged_Type = TimeStamp
_PwTemplateLastChanged_Object = MibTableColumn
pwTemplateLastChanged = _PwTemplateLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 3),
    _PwTemplateLastChanged_Type()
)
pwTemplateLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTemplateLastChanged.setStatus("current")


class _PwTemplateUseProvisionedSdp_Type(TruthValue):
    """Custom type pwTemplateUseProvisionedSdp based on TruthValue"""
    defaultValue = 2


_PwTemplateUseProvisionedSdp_Type.__name__ = "TruthValue"
_PwTemplateUseProvisionedSdp_Object = MibTableColumn
pwTemplateUseProvisionedSdp = _PwTemplateUseProvisionedSdp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 4),
    _PwTemplateUseProvisionedSdp_Type()
)
pwTemplateUseProvisionedSdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateUseProvisionedSdp.setStatus("current")


class _PwTemplateVcType_Type(SdpBindVcType):
    """Custom type pwTemplateVcType based on SdpBindVcType"""
    defaultValue = 2


_PwTemplateVcType_Type.__name__ = "SdpBindVcType"
_PwTemplateVcType_Object = MibTableColumn
pwTemplateVcType = _PwTemplateVcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 5),
    _PwTemplateVcType_Type()
)
pwTemplateVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateVcType.setStatus("current")


class _PwTemplateAccountingPolicyId_Type(Unsigned32):
    """Custom type pwTemplateAccountingPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_PwTemplateAccountingPolicyId_Type.__name__ = "Unsigned32"
_PwTemplateAccountingPolicyId_Object = MibTableColumn
pwTemplateAccountingPolicyId = _PwTemplateAccountingPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 6),
    _PwTemplateAccountingPolicyId_Type()
)
pwTemplateAccountingPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateAccountingPolicyId.setStatus("current")


class _PwTemplateCollectAcctStats_Type(TruthValue):
    """Custom type pwTemplateCollectAcctStats based on TruthValue"""
    defaultValue = 2


_PwTemplateCollectAcctStats_Type.__name__ = "TruthValue"
_PwTemplateCollectAcctStats_Object = MibTableColumn
pwTemplateCollectAcctStats = _PwTemplateCollectAcctStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 7),
    _PwTemplateCollectAcctStats_Type()
)
pwTemplateCollectAcctStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateCollectAcctStats.setStatus("current")


class _PwTemplateMacLearning_Type(TmnxEnabledDisabled):
    """Custom type pwTemplateMacLearning based on TmnxEnabledDisabled"""
    defaultValue = 1


_PwTemplateMacLearning_Type.__name__ = "TmnxEnabledDisabled"
_PwTemplateMacLearning_Object = MibTableColumn
pwTemplateMacLearning = _PwTemplateMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 8),
    _PwTemplateMacLearning_Type()
)
pwTemplateMacLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateMacLearning.setStatus("current")


class _PwTemplateMacAgeing_Type(TmnxEnabledDisabled):
    """Custom type pwTemplateMacAgeing based on TmnxEnabledDisabled"""
    defaultValue = 1


_PwTemplateMacAgeing_Type.__name__ = "TmnxEnabledDisabled"
_PwTemplateMacAgeing_Object = MibTableColumn
pwTemplateMacAgeing = _PwTemplateMacAgeing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 9),
    _PwTemplateMacAgeing_Type()
)
pwTemplateMacAgeing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateMacAgeing.setStatus("current")


class _PwTemplateDiscardUnknownSource_Type(TmnxEnabledDisabled):
    """Custom type pwTemplateDiscardUnknownSource based on TmnxEnabledDisabled"""
    defaultValue = 2


_PwTemplateDiscardUnknownSource_Type.__name__ = "TmnxEnabledDisabled"
_PwTemplateDiscardUnknownSource_Object = MibTableColumn
pwTemplateDiscardUnknownSource = _PwTemplateDiscardUnknownSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 10),
    _PwTemplateDiscardUnknownSource_Type()
)
pwTemplateDiscardUnknownSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateDiscardUnknownSource.setStatus("current")


class _PwTemplateLimitMacMove_Type(TlsLimitMacMove):
    """Custom type pwTemplateLimitMacMove based on TlsLimitMacMove"""
    defaultValue = 1


_PwTemplateLimitMacMove_Type.__name__ = "TlsLimitMacMove"
_PwTemplateLimitMacMove_Object = MibTableColumn
pwTemplateLimitMacMove = _PwTemplateLimitMacMove_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 11),
    _PwTemplateLimitMacMove_Type()
)
pwTemplateLimitMacMove.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateLimitMacMove.setStatus("current")


class _PwTemplateMacPinning_Type(TmnxEnabledDisabled):
    """Custom type pwTemplateMacPinning based on TmnxEnabledDisabled"""
    defaultValue = 2


_PwTemplateMacPinning_Type.__name__ = "TmnxEnabledDisabled"
_PwTemplateMacPinning_Object = MibTableColumn
pwTemplateMacPinning = _PwTemplateMacPinning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 12),
    _PwTemplateMacPinning_Type()
)
pwTemplateMacPinning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateMacPinning.setStatus("current")


class _PwTemplateVlanVcTag_Type(Unsigned32):
    """Custom type pwTemplateVlanVcTag based on Unsigned32"""
    defaultValue = 4095

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_PwTemplateVlanVcTag_Type.__name__ = "Unsigned32"
_PwTemplateVlanVcTag_Object = MibTableColumn
pwTemplateVlanVcTag = _PwTemplateVlanVcTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 13),
    _PwTemplateVlanVcTag_Type()
)
pwTemplateVlanVcTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateVlanVcTag.setStatus("current")


class _PwTemplateMacAddressLimit_Type(Unsigned32):
    """Custom type pwTemplateMacAddressLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511999),
    )


_PwTemplateMacAddressLimit_Type.__name__ = "Unsigned32"
_PwTemplateMacAddressLimit_Object = MibTableColumn
pwTemplateMacAddressLimit = _PwTemplateMacAddressLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 14),
    _PwTemplateMacAddressLimit_Type()
)
pwTemplateMacAddressLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateMacAddressLimit.setStatus("current")


class _PwTemplateShgName_Type(TNamedItemOrEmpty):
    """Custom type pwTemplateShgName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_PwTemplateShgName_Type.__name__ = "TNamedItemOrEmpty"
_PwTemplateShgName_Object = MibTableColumn
pwTemplateShgName = _PwTemplateShgName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 15),
    _PwTemplateShgName_Type()
)
pwTemplateShgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateShgName.setStatus("current")


class _PwTemplateShgDescription_Type(TItemDescription):
    """Custom type pwTemplateShgDescription based on TItemDescription"""
    defaultValue = OctetString("")


_PwTemplateShgDescription_Type.__name__ = "TItemDescription"
_PwTemplateShgDescription_Object = MibTableColumn
pwTemplateShgDescription = _PwTemplateShgDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 16),
    _PwTemplateShgDescription_Type()
)
pwTemplateShgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateShgDescription.setStatus("current")


class _PwTemplateShgRestProtSrcMac_Type(TruthValue):
    """Custom type pwTemplateShgRestProtSrcMac based on TruthValue"""
    defaultValue = 2


_PwTemplateShgRestProtSrcMac_Type.__name__ = "TruthValue"
_PwTemplateShgRestProtSrcMac_Object = MibTableColumn
pwTemplateShgRestProtSrcMac = _PwTemplateShgRestProtSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 17),
    _PwTemplateShgRestProtSrcMac_Type()
)
pwTemplateShgRestProtSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateShgRestProtSrcMac.setStatus("current")


class _PwTemplateShgRestUnprotDstMac_Type(TruthValue):
    """Custom type pwTemplateShgRestUnprotDstMac based on TruthValue"""
    defaultValue = 2


_PwTemplateShgRestUnprotDstMac_Type.__name__ = "TruthValue"
_PwTemplateShgRestUnprotDstMac_Object = MibTableColumn
pwTemplateShgRestUnprotDstMac = _PwTemplateShgRestUnprotDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 18),
    _PwTemplateShgRestUnprotDstMac_Type()
)
pwTemplateShgRestUnprotDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateShgRestUnprotDstMac.setStatus("current")


class _PwTemplateEgressMacFilterId_Type(TFilterID):
    """Custom type pwTemplateEgressMacFilterId based on TFilterID"""
    defaultValue = 0


_PwTemplateEgressMacFilterId_Type.__name__ = "TFilterID"
_PwTemplateEgressMacFilterId_Object = MibTableColumn
pwTemplateEgressMacFilterId = _PwTemplateEgressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 19),
    _PwTemplateEgressMacFilterId_Type()
)
pwTemplateEgressMacFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateEgressMacFilterId.setStatus("current")


class _PwTemplateEgressIpFilterId_Type(TFilterID):
    """Custom type pwTemplateEgressIpFilterId based on TFilterID"""
    defaultValue = 0


_PwTemplateEgressIpFilterId_Type.__name__ = "TFilterID"
_PwTemplateEgressIpFilterId_Object = MibTableColumn
pwTemplateEgressIpFilterId = _PwTemplateEgressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 20),
    _PwTemplateEgressIpFilterId_Type()
)
pwTemplateEgressIpFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateEgressIpFilterId.setStatus("current")


class _PwTemplateEgressIpv6FilterId_Type(TFilterID):
    """Custom type pwTemplateEgressIpv6FilterId based on TFilterID"""
    defaultValue = 0


_PwTemplateEgressIpv6FilterId_Type.__name__ = "TFilterID"
_PwTemplateEgressIpv6FilterId_Object = MibTableColumn
pwTemplateEgressIpv6FilterId = _PwTemplateEgressIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 21),
    _PwTemplateEgressIpv6FilterId_Type()
)
pwTemplateEgressIpv6FilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateEgressIpv6FilterId.setStatus("current")


class _PwTemplateIngressMacFilterId_Type(TFilterID):
    """Custom type pwTemplateIngressMacFilterId based on TFilterID"""
    defaultValue = 0


_PwTemplateIngressMacFilterId_Type.__name__ = "TFilterID"
_PwTemplateIngressMacFilterId_Object = MibTableColumn
pwTemplateIngressMacFilterId = _PwTemplateIngressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 22),
    _PwTemplateIngressMacFilterId_Type()
)
pwTemplateIngressMacFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIngressMacFilterId.setStatus("current")


class _PwTemplateIngressIpFilterId_Type(TFilterID):
    """Custom type pwTemplateIngressIpFilterId based on TFilterID"""
    defaultValue = 0


_PwTemplateIngressIpFilterId_Type.__name__ = "TFilterID"
_PwTemplateIngressIpFilterId_Object = MibTableColumn
pwTemplateIngressIpFilterId = _PwTemplateIngressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 23),
    _PwTemplateIngressIpFilterId_Type()
)
pwTemplateIngressIpFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIngressIpFilterId.setStatus("current")


class _PwTemplateIngressIpv6FilterId_Type(TFilterID):
    """Custom type pwTemplateIngressIpv6FilterId based on TFilterID"""
    defaultValue = 0


_PwTemplateIngressIpv6FilterId_Type.__name__ = "TFilterID"
_PwTemplateIngressIpv6FilterId_Object = MibTableColumn
pwTemplateIngressIpv6FilterId = _PwTemplateIngressIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 24),
    _PwTemplateIngressIpv6FilterId_Type()
)
pwTemplateIngressIpv6FilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIngressIpv6FilterId.setStatus("current")


class _PwTemplateIgmpFastLeave_Type(TmnxEnabledDisabled):
    """Custom type pwTemplateIgmpFastLeave based on TmnxEnabledDisabled"""
    defaultValue = 2


_PwTemplateIgmpFastLeave_Type.__name__ = "TmnxEnabledDisabled"
_PwTemplateIgmpFastLeave_Object = MibTableColumn
pwTemplateIgmpFastLeave = _PwTemplateIgmpFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 25),
    _PwTemplateIgmpFastLeave_Type()
)
pwTemplateIgmpFastLeave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpFastLeave.setStatus("current")


class _PwTemplateIgmpImportPlcy_Type(TNamedItemOrEmpty):
    """Custom type pwTemplateIgmpImportPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_PwTemplateIgmpImportPlcy_Type.__name__ = "TNamedItemOrEmpty"
_PwTemplateIgmpImportPlcy_Object = MibTableColumn
pwTemplateIgmpImportPlcy = _PwTemplateIgmpImportPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 26),
    _PwTemplateIgmpImportPlcy_Type()
)
pwTemplateIgmpImportPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpImportPlcy.setStatus("current")


class _PwTemplateIgmpLastMembIntvl_Type(Unsigned32):
    """Custom type pwTemplateIgmpLastMembIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_PwTemplateIgmpLastMembIntvl_Type.__name__ = "Unsigned32"
_PwTemplateIgmpLastMembIntvl_Object = MibTableColumn
pwTemplateIgmpLastMembIntvl = _PwTemplateIgmpLastMembIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 27),
    _PwTemplateIgmpLastMembIntvl_Type()
)
pwTemplateIgmpLastMembIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpLastMembIntvl.setStatus("current")
if mibBuilder.loadTexts:
    pwTemplateIgmpLastMembIntvl.setUnits("deciseconds")


class _PwTemplateIgmpMaxNbrGrps_Type(Unsigned32):
    """Custom type pwTemplateIgmpMaxNbrGrps based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PwTemplateIgmpMaxNbrGrps_Type.__name__ = "Unsigned32"
_PwTemplateIgmpMaxNbrGrps_Object = MibTableColumn
pwTemplateIgmpMaxNbrGrps = _PwTemplateIgmpMaxNbrGrps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 28),
    _PwTemplateIgmpMaxNbrGrps_Type()
)
pwTemplateIgmpMaxNbrGrps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpMaxNbrGrps.setStatus("current")


class _PwTemplateIgmpGenQueryIntvl_Type(Unsigned32):
    """Custom type pwTemplateIgmpGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_PwTemplateIgmpGenQueryIntvl_Type.__name__ = "Unsigned32"
_PwTemplateIgmpGenQueryIntvl_Object = MibTableColumn
pwTemplateIgmpGenQueryIntvl = _PwTemplateIgmpGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 29),
    _PwTemplateIgmpGenQueryIntvl_Type()
)
pwTemplateIgmpGenQueryIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    pwTemplateIgmpGenQueryIntvl.setUnits("seconds")


class _PwTemplateIgmpQueryRespIntvl_Type(Unsigned32):
    """Custom type pwTemplateIgmpQueryRespIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_PwTemplateIgmpQueryRespIntvl_Type.__name__ = "Unsigned32"
_PwTemplateIgmpQueryRespIntvl_Object = MibTableColumn
pwTemplateIgmpQueryRespIntvl = _PwTemplateIgmpQueryRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 30),
    _PwTemplateIgmpQueryRespIntvl_Type()
)
pwTemplateIgmpQueryRespIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpQueryRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    pwTemplateIgmpQueryRespIntvl.setUnits("seconds")


class _PwTemplateIgmpRobustCount_Type(Unsigned32):
    """Custom type pwTemplateIgmpRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_PwTemplateIgmpRobustCount_Type.__name__ = "Unsigned32"
_PwTemplateIgmpRobustCount_Object = MibTableColumn
pwTemplateIgmpRobustCount = _PwTemplateIgmpRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 31),
    _PwTemplateIgmpRobustCount_Type()
)
pwTemplateIgmpRobustCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpRobustCount.setStatus("current")


class _PwTemplateIgmpSendQueries_Type(TmnxEnabledDisabled):
    """Custom type pwTemplateIgmpSendQueries based on TmnxEnabledDisabled"""
    defaultValue = 2


_PwTemplateIgmpSendQueries_Type.__name__ = "TmnxEnabledDisabled"
_PwTemplateIgmpSendQueries_Object = MibTableColumn
pwTemplateIgmpSendQueries = _PwTemplateIgmpSendQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 32),
    _PwTemplateIgmpSendQueries_Type()
)
pwTemplateIgmpSendQueries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpSendQueries.setStatus("current")


class _PwTemplateIgmpMcacPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type pwTemplateIgmpMcacPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_PwTemplateIgmpMcacPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_PwTemplateIgmpMcacPolicyName_Object = MibTableColumn
pwTemplateIgmpMcacPolicyName = _PwTemplateIgmpMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 33),
    _PwTemplateIgmpMcacPolicyName_Type()
)
pwTemplateIgmpMcacPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpMcacPolicyName.setStatus("obsolete")


class _PwTemplateIgmpMcacUnconstBW_Type(Integer32):
    """Custom type pwTemplateIgmpMcacUnconstBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_PwTemplateIgmpMcacUnconstBW_Type.__name__ = "Integer32"
_PwTemplateIgmpMcacUnconstBW_Object = MibTableColumn
pwTemplateIgmpMcacUnconstBW = _PwTemplateIgmpMcacUnconstBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 34),
    _PwTemplateIgmpMcacUnconstBW_Type()
)
pwTemplateIgmpMcacUnconstBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpMcacUnconstBW.setStatus("obsolete")
if mibBuilder.loadTexts:
    pwTemplateIgmpMcacUnconstBW.setUnits("kilobps")


class _PwTemplateIgmpMcacPrRsvMndBW_Type(Integer32):
    """Custom type pwTemplateIgmpMcacPrRsvMndBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_PwTemplateIgmpMcacPrRsvMndBW_Type.__name__ = "Integer32"
_PwTemplateIgmpMcacPrRsvMndBW_Object = MibTableColumn
pwTemplateIgmpMcacPrRsvMndBW = _PwTemplateIgmpMcacPrRsvMndBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 35),
    _PwTemplateIgmpMcacPrRsvMndBW_Type()
)
pwTemplateIgmpMcacPrRsvMndBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpMcacPrRsvMndBW.setStatus("obsolete")
if mibBuilder.loadTexts:
    pwTemplateIgmpMcacPrRsvMndBW.setUnits("kilobps")


class _PwTemplateIgmpVersion_Type(TmnxIgmpVersion):
    """Custom type pwTemplateIgmpVersion based on TmnxIgmpVersion"""
    defaultValue = 3


_PwTemplateIgmpVersion_Type.__name__ = "TmnxIgmpVersion"
_PwTemplateIgmpVersion_Object = MibTableColumn
pwTemplateIgmpVersion = _PwTemplateIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 36),
    _PwTemplateIgmpVersion_Type()
)
pwTemplateIgmpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpVersion.setStatus("current")


class _PwTemplateForceVlanVcForwarding_Type(TruthValue):
    """Custom type pwTemplateForceVlanVcForwarding based on TruthValue"""
    defaultValue = 2


_PwTemplateForceVlanVcForwarding_Type.__name__ = "TruthValue"
_PwTemplateForceVlanVcForwarding_Object = MibTableColumn
pwTemplateForceVlanVcForwarding = _PwTemplateForceVlanVcForwarding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 37),
    _PwTemplateForceVlanVcForwarding_Type()
)
pwTemplateForceVlanVcForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateForceVlanVcForwarding.setStatus("current")


class _PwTemplateHashLabel_Type(TruthValue):
    """Custom type pwTemplateHashLabel based on TruthValue"""
    defaultValue = 2


_PwTemplateHashLabel_Type.__name__ = "TruthValue"
_PwTemplateHashLabel_Object = MibTableColumn
pwTemplateHashLabel = _PwTemplateHashLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 38),
    _PwTemplateHashLabel_Type()
)
pwTemplateHashLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateHashLabel.setStatus("current")


class _PwTemplateControlWord_Type(TruthValue):
    """Custom type pwTemplateControlWord based on TruthValue"""
    defaultValue = 2


_PwTemplateControlWord_Type.__name__ = "TruthValue"
_PwTemplateControlWord_Object = MibTableColumn
pwTemplateControlWord = _PwTemplateControlWord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 39),
    _PwTemplateControlWord_Type()
)
pwTemplateControlWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateControlWord.setStatus("current")


class _PwTemplateHashLabelSignalCap_Type(TruthValue):
    """Custom type pwTemplateHashLabelSignalCap based on TruthValue"""
    defaultValue = 2


_PwTemplateHashLabelSignalCap_Type.__name__ = "TruthValue"
_PwTemplateHashLabelSignalCap_Object = MibTableColumn
pwTemplateHashLabelSignalCap = _PwTemplateHashLabelSignalCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 40),
    _PwTemplateHashLabelSignalCap_Type()
)
pwTemplateHashLabelSignalCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateHashLabelSignalCap.setStatus("current")


class _PwTemplateRestProtSrcMac_Type(TruthValue):
    """Custom type pwTemplateRestProtSrcMac based on TruthValue"""
    defaultValue = 2


_PwTemplateRestProtSrcMac_Type.__name__ = "TruthValue"
_PwTemplateRestProtSrcMac_Object = MibTableColumn
pwTemplateRestProtSrcMac = _PwTemplateRestProtSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 52),
    _PwTemplateRestProtSrcMac_Type()
)
pwTemplateRestProtSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateRestProtSrcMac.setStatus("current")


class _PwTemplateRestProtSrcMacAction_Type(Integer32):
    """Custom type pwTemplateRestProtSrcMacAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("alarmOnly", 2),
          ("discardFrame", 3))
    )


_PwTemplateRestProtSrcMacAction_Type.__name__ = "Integer32"
_PwTemplateRestProtSrcMacAction_Object = MibTableColumn
pwTemplateRestProtSrcMacAction = _PwTemplateRestProtSrcMacAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 53),
    _PwTemplateRestProtSrcMacAction_Type()
)
pwTemplateRestProtSrcMacAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateRestProtSrcMacAction.setStatus("current")


class _PwTemplateAutoLearnMacProtect_Type(TruthValue):
    """Custom type pwTemplateAutoLearnMacProtect based on TruthValue"""
    defaultValue = 2


_PwTemplateAutoLearnMacProtect_Type.__name__ = "TruthValue"
_PwTemplateAutoLearnMacProtect_Object = MibTableColumn
pwTemplateAutoLearnMacProtect = _PwTemplateAutoLearnMacProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 54),
    _PwTemplateAutoLearnMacProtect_Type()
)
pwTemplateAutoLearnMacProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateAutoLearnMacProtect.setStatus("current")


class _PwTemplateShgRestProtSrcMacAct_Type(Integer32):
    """Custom type pwTemplateShgRestProtSrcMacAct based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("alarmOnly", 2),
          ("discardFrame", 3))
    )


_PwTemplateShgRestProtSrcMacAct_Type.__name__ = "Integer32"
_PwTemplateShgRestProtSrcMacAct_Object = MibTableColumn
pwTemplateShgRestProtSrcMacAct = _PwTemplateShgRestProtSrcMacAct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 55),
    _PwTemplateShgRestProtSrcMacAct_Type()
)
pwTemplateShgRestProtSrcMacAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateShgRestProtSrcMacAct.setStatus("current")


class _PwTemplateShgAutoLearnMacProtect_Type(TruthValue):
    """Custom type pwTemplateShgAutoLearnMacProtect based on TruthValue"""
    defaultValue = 2


_PwTemplateShgAutoLearnMacProtect_Type.__name__ = "TruthValue"
_PwTemplateShgAutoLearnMacProtect_Object = MibTableColumn
pwTemplateShgAutoLearnMacProtect = _PwTemplateShgAutoLearnMacProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 56),
    _PwTemplateShgAutoLearnMacProtect_Type()
)
pwTemplateShgAutoLearnMacProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateShgAutoLearnMacProtect.setStatus("current")


class _PwTemplateIngQoSNetworkPlcyId_Type(TSdpIngressPolicyID):
    """Custom type pwTemplateIngQoSNetworkPlcyId based on TSdpIngressPolicyID"""
    defaultValue = 0

    subtypeSpec = TSdpIngressPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PwTemplateIngQoSNetworkPlcyId_Type.__name__ = "TSdpIngressPolicyID"
_PwTemplateIngQoSNetworkPlcyId_Object = MibTableColumn
pwTemplateIngQoSNetworkPlcyId = _PwTemplateIngQoSNetworkPlcyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 57),
    _PwTemplateIngQoSNetworkPlcyId_Type()
)
pwTemplateIngQoSNetworkPlcyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIngQoSNetworkPlcyId.setStatus("current")


class _PwTemplateEgrQoSNetworkPlcyId_Type(TSdpEgressPolicyID):
    """Custom type pwTemplateEgrQoSNetworkPlcyId based on TSdpEgressPolicyID"""
    defaultValue = 0

    subtypeSpec = TSdpEgressPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PwTemplateEgrQoSNetworkPlcyId_Type.__name__ = "TSdpEgressPolicyID"
_PwTemplateEgrQoSNetworkPlcyId_Object = MibTableColumn
pwTemplateEgrQoSNetworkPlcyId = _PwTemplateEgrQoSNetworkPlcyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 58),
    _PwTemplateEgrQoSNetworkPlcyId_Type()
)
pwTemplateEgrQoSNetworkPlcyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateEgrQoSNetworkPlcyId.setStatus("current")


class _PwTemplateIngQoSFpRedirectQGrp_Type(TNamedItemOrEmpty):
    """Custom type pwTemplateIngQoSFpRedirectQGrp based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_PwTemplateIngQoSFpRedirectQGrp_Type.__name__ = "TNamedItemOrEmpty"
_PwTemplateIngQoSFpRedirectQGrp_Object = MibTableColumn
pwTemplateIngQoSFpRedirectQGrp = _PwTemplateIngQoSFpRedirectQGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 59),
    _PwTemplateIngQoSFpRedirectQGrp_Type()
)
pwTemplateIngQoSFpRedirectQGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIngQoSFpRedirectQGrp.setStatus("current")


class _PwTemplateEgrQoSPortRedirectQGrp_Type(TNamedItemOrEmpty):
    """Custom type pwTemplateEgrQoSPortRedirectQGrp based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_PwTemplateEgrQoSPortRedirectQGrp_Type.__name__ = "TNamedItemOrEmpty"
_PwTemplateEgrQoSPortRedirectQGrp_Object = MibTableColumn
pwTemplateEgrQoSPortRedirectQGrp = _PwTemplateEgrQoSPortRedirectQGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 60),
    _PwTemplateEgrQoSPortRedirectQGrp_Type()
)
pwTemplateEgrQoSPortRedirectQGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateEgrQoSPortRedirectQGrp.setStatus("current")


class _PwTemplateIngQoSInstanceId_Type(TQosQGrpInstanceIDorZero):
    """Custom type pwTemplateIngQoSInstanceId based on TQosQGrpInstanceIDorZero"""
    defaultValue = 0


_PwTemplateIngQoSInstanceId_Type.__name__ = "TQosQGrpInstanceIDorZero"
_PwTemplateIngQoSInstanceId_Object = MibTableColumn
pwTemplateIngQoSInstanceId = _PwTemplateIngQoSInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 61),
    _PwTemplateIngQoSInstanceId_Type()
)
pwTemplateIngQoSInstanceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIngQoSInstanceId.setStatus("current")


class _PwTemplateEgrQoSInstanceId_Type(TQosQGrpInstanceIDorZero):
    """Custom type pwTemplateEgrQoSInstanceId based on TQosQGrpInstanceIDorZero"""
    defaultValue = 0


_PwTemplateEgrQoSInstanceId_Type.__name__ = "TQosQGrpInstanceIDorZero"
_PwTemplateEgrQoSInstanceId_Object = MibTableColumn
pwTemplateEgrQoSInstanceId = _PwTemplateEgrQoSInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 62),
    _PwTemplateEgrQoSInstanceId_Type()
)
pwTemplateEgrQoSInstanceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateEgrQoSInstanceId.setStatus("current")


class _PwTemplateBlockOnPeerFault_Type(TruthValue):
    """Custom type pwTemplateBlockOnPeerFault based on TruthValue"""
    defaultValue = 2


_PwTemplateBlockOnPeerFault_Type.__name__ = "TruthValue"
_PwTemplateBlockOnPeerFault_Object = MibTableColumn
pwTemplateBlockOnPeerFault = _PwTemplateBlockOnPeerFault_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 63),
    _PwTemplateBlockOnPeerFault_Type()
)
pwTemplateBlockOnPeerFault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateBlockOnPeerFault.setStatus("current")


class _PwTemplateForceQinqVcForwarding_Type(TruthValue):
    """Custom type pwTemplateForceQinqVcForwarding based on TruthValue"""
    defaultValue = 2


_PwTemplateForceQinqVcForwarding_Type.__name__ = "TruthValue"
_PwTemplateForceQinqVcForwarding_Object = MibTableColumn
pwTemplateForceQinqVcForwarding = _PwTemplateForceQinqVcForwarding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 64),
    _PwTemplateForceQinqVcForwarding_Type()
)
pwTemplateForceQinqVcForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateForceQinqVcForwarding.setStatus("obsolete")


class _PwTemplatePreferProvSdp_Type(TruthValue):
    """Custom type pwTemplatePreferProvSdp based on TruthValue"""
    defaultValue = 2


_PwTemplatePreferProvSdp_Type.__name__ = "TruthValue"
_PwTemplatePreferProvSdp_Object = MibTableColumn
pwTemplatePreferProvSdp = _PwTemplatePreferProvSdp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 65),
    _PwTemplatePreferProvSdp_Type()
)
pwTemplatePreferProvSdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplatePreferProvSdp.setStatus("current")


class _PwTemplateEntropyLabel_Type(TruthValue):
    """Custom type pwTemplateEntropyLabel based on TruthValue"""
    defaultValue = 2


_PwTemplateEntropyLabel_Type.__name__ = "TruthValue"
_PwTemplateEntropyLabel_Object = MibTableColumn
pwTemplateEntropyLabel = _PwTemplateEntropyLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 66),
    _PwTemplateEntropyLabel_Type()
)
pwTemplateEntropyLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateEntropyLabel.setStatus("current")


class _PwTemplateName_Type(TLNamedItemOrEmpty):
    """Custom type pwTemplateName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_PwTemplateName_Type.__name__ = "TLNamedItemOrEmpty"
_PwTemplateName_Object = MibTableColumn
pwTemplateName = _PwTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 67),
    _PwTemplateName_Type()
)
pwTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateName.setStatus("current")


class _PwTemplateGreDelivery_Type(TruthValue):
    """Custom type pwTemplateGreDelivery based on TruthValue"""
    defaultValue = 2


_PwTemplateGreDelivery_Type.__name__ = "TruthValue"
_PwTemplateGreDelivery_Object = MibTableColumn
pwTemplateGreDelivery = _PwTemplateGreDelivery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 68),
    _PwTemplateGreDelivery_Type()
)
pwTemplateGreDelivery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateGreDelivery.setStatus("current")


class _PwTemplateIngQoSNetworkPlcyName_Type(TLNamedItemOrEmpty):
    """Custom type pwTemplateIngQoSNetworkPlcyName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_PwTemplateIngQoSNetworkPlcyName_Type.__name__ = "TLNamedItemOrEmpty"
_PwTemplateIngQoSNetworkPlcyName_Object = MibTableColumn
pwTemplateIngQoSNetworkPlcyName = _PwTemplateIngQoSNetworkPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 69),
    _PwTemplateIngQoSNetworkPlcyName_Type()
)
pwTemplateIngQoSNetworkPlcyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIngQoSNetworkPlcyName.setStatus("current")


class _PwTemplateEgrQoSNetworkPlcyName_Type(TLNamedItemOrEmpty):
    """Custom type pwTemplateEgrQoSNetworkPlcyName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_PwTemplateEgrQoSNetworkPlcyName_Type.__name__ = "TLNamedItemOrEmpty"
_PwTemplateEgrQoSNetworkPlcyName_Object = MibTableColumn
pwTemplateEgrQoSNetworkPlcyName = _PwTemplateEgrQoSNetworkPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 70),
    _PwTemplateEgrQoSNetworkPlcyName_Type()
)
pwTemplateEgrQoSNetworkPlcyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateEgrQoSNetworkPlcyName.setStatus("current")


class _PwTemplateIngressIpFilterName_Type(TLNamedItemOrEmpty):
    """Custom type pwTemplateIngressIpFilterName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_PwTemplateIngressIpFilterName_Type.__name__ = "TLNamedItemOrEmpty"
_PwTemplateIngressIpFilterName_Object = MibTableColumn
pwTemplateIngressIpFilterName = _PwTemplateIngressIpFilterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 71),
    _PwTemplateIngressIpFilterName_Type()
)
pwTemplateIngressIpFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIngressIpFilterName.setStatus("current")


class _PwTemplateIngressIpv6FilterName_Type(TLNamedItemOrEmpty):
    """Custom type pwTemplateIngressIpv6FilterName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_PwTemplateIngressIpv6FilterName_Type.__name__ = "TLNamedItemOrEmpty"
_PwTemplateIngressIpv6FilterName_Object = MibTableColumn
pwTemplateIngressIpv6FilterName = _PwTemplateIngressIpv6FilterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 72),
    _PwTemplateIngressIpv6FilterName_Type()
)
pwTemplateIngressIpv6FilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIngressIpv6FilterName.setStatus("current")


class _PwTemplateIngressMacFilterName_Type(TLNamedItemOrEmpty):
    """Custom type pwTemplateIngressMacFilterName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_PwTemplateIngressMacFilterName_Type.__name__ = "TLNamedItemOrEmpty"
_PwTemplateIngressMacFilterName_Object = MibTableColumn
pwTemplateIngressMacFilterName = _PwTemplateIngressMacFilterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 73),
    _PwTemplateIngressMacFilterName_Type()
)
pwTemplateIngressMacFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIngressMacFilterName.setStatus("current")


class _PwTemplateEgressIpFilterName_Type(TLNamedItemOrEmpty):
    """Custom type pwTemplateEgressIpFilterName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_PwTemplateEgressIpFilterName_Type.__name__ = "TLNamedItemOrEmpty"
_PwTemplateEgressIpFilterName_Object = MibTableColumn
pwTemplateEgressIpFilterName = _PwTemplateEgressIpFilterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 74),
    _PwTemplateEgressIpFilterName_Type()
)
pwTemplateEgressIpFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateEgressIpFilterName.setStatus("current")


class _PwTemplateEgressIpv6FilterName_Type(TLNamedItemOrEmpty):
    """Custom type pwTemplateEgressIpv6FilterName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_PwTemplateEgressIpv6FilterName_Type.__name__ = "TLNamedItemOrEmpty"
_PwTemplateEgressIpv6FilterName_Object = MibTableColumn
pwTemplateEgressIpv6FilterName = _PwTemplateEgressIpv6FilterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 75),
    _PwTemplateEgressIpv6FilterName_Type()
)
pwTemplateEgressIpv6FilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateEgressIpv6FilterName.setStatus("current")


class _PwTemplateEgressMacFilterName_Type(TLNamedItemOrEmpty):
    """Custom type pwTemplateEgressMacFilterName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_PwTemplateEgressMacFilterName_Type.__name__ = "TLNamedItemOrEmpty"
_PwTemplateEgressMacFilterName_Object = MibTableColumn
pwTemplateEgressMacFilterName = _PwTemplateEgressMacFilterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 76),
    _PwTemplateEgressMacFilterName_Type()
)
pwTemplateEgressMacFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateEgressMacFilterName.setStatus("current")


class _PwTemplateForceQinqVcFwding_Type(Integer32):
    """Custom type pwTemplateForceQinqVcFwding based on Integer32"""
    defaultValue = 0

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
          ("ctagctag", 1),
          ("stagctag", 2))
    )


_PwTemplateForceQinqVcFwding_Type.__name__ = "Integer32"
_PwTemplateForceQinqVcFwding_Object = MibTableColumn
pwTemplateForceQinqVcFwding = _PwTemplateForceQinqVcFwding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 77),
    _PwTemplateForceQinqVcFwding_Type()
)
pwTemplateForceQinqVcFwding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateForceQinqVcFwding.setStatus("current")
_PwTemplateIgmpSnpgGrpSrcTblLC_Type = TimeStamp
_PwTemplateIgmpSnpgGrpSrcTblLC_Object = MibScalar
pwTemplateIgmpSnpgGrpSrcTblLC = _PwTemplateIgmpSnpgGrpSrcTblLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 19),
    _PwTemplateIgmpSnpgGrpSrcTblLC_Type()
)
pwTemplateIgmpSnpgGrpSrcTblLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgGrpSrcTblLC.setStatus("current")
_PwTemplateIgmpSnpgGrpSrcTable_Object = MibTable
pwTemplateIgmpSnpgGrpSrcTable = _PwTemplateIgmpSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 20)
)
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgGrpSrcTable.setStatus("current")
_PwTemplateIgmpSnpgGrpSrcEntry_Object = MibTableRow
pwTemplateIgmpSnpgGrpSrcEntry = _PwTemplateIgmpSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 20, 1)
)
pwTemplateIgmpSnpgGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SDP-MIB", "pwTemplateId"),
    (0, "TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgGrpAddrType"),
    (0, "TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgGrpAddr"),
    (0, "TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgSrcAddrType"),
    (0, "TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgSrcAddr"),
)
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgGrpSrcEntry.setStatus("current")
_PwTemplateIgmpSnpgGrpAddrType_Type = InetAddressType
_PwTemplateIgmpSnpgGrpAddrType_Object = MibTableColumn
pwTemplateIgmpSnpgGrpAddrType = _PwTemplateIgmpSnpgGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 20, 1, 1),
    _PwTemplateIgmpSnpgGrpAddrType_Type()
)
pwTemplateIgmpSnpgGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgGrpAddrType.setStatus("current")


class _PwTemplateIgmpSnpgGrpAddr_Type(InetAddress):
    """Custom type pwTemplateIgmpSnpgGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_PwTemplateIgmpSnpgGrpAddr_Type.__name__ = "InetAddress"
_PwTemplateIgmpSnpgGrpAddr_Object = MibTableColumn
pwTemplateIgmpSnpgGrpAddr = _PwTemplateIgmpSnpgGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 20, 1, 2),
    _PwTemplateIgmpSnpgGrpAddr_Type()
)
pwTemplateIgmpSnpgGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgGrpAddr.setStatus("current")
_PwTemplateIgmpSnpgSrcAddrType_Type = InetAddressType
_PwTemplateIgmpSnpgSrcAddrType_Object = MibTableColumn
pwTemplateIgmpSnpgSrcAddrType = _PwTemplateIgmpSnpgSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 20, 1, 3),
    _PwTemplateIgmpSnpgSrcAddrType_Type()
)
pwTemplateIgmpSnpgSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgSrcAddrType.setStatus("current")


class _PwTemplateIgmpSnpgSrcAddr_Type(InetAddress):
    """Custom type pwTemplateIgmpSnpgSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_PwTemplateIgmpSnpgSrcAddr_Type.__name__ = "InetAddress"
_PwTemplateIgmpSnpgSrcAddr_Object = MibTableColumn
pwTemplateIgmpSnpgSrcAddr = _PwTemplateIgmpSnpgSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 20, 1, 4),
    _PwTemplateIgmpSnpgSrcAddr_Type()
)
pwTemplateIgmpSnpgSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgSrcAddr.setStatus("current")
_PwTemplateIgmpSnpgRowStatus_Type = RowStatus
_PwTemplateIgmpSnpgRowStatus_Object = MibTableColumn
pwTemplateIgmpSnpgRowStatus = _PwTemplateIgmpSnpgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 20, 1, 5),
    _PwTemplateIgmpSnpgRowStatus_Type()
)
pwTemplateIgmpSnpgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgRowStatus.setStatus("current")
_PwTemplateIgmpSnpgLastChngd_Type = TimeStamp
_PwTemplateIgmpSnpgLastChngd_Object = MibTableColumn
pwTemplateIgmpSnpgLastChngd = _PwTemplateIgmpSnpgLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 20, 1, 6),
    _PwTemplateIgmpSnpgLastChngd_Type()
)
pwTemplateIgmpSnpgLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgLastChngd.setStatus("current")
_PwTemplateMfibAllowedMdaTblLC_Type = TimeStamp
_PwTemplateMfibAllowedMdaTblLC_Object = MibScalar
pwTemplateMfibAllowedMdaTblLC = _PwTemplateMfibAllowedMdaTblLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 21),
    _PwTemplateMfibAllowedMdaTblLC_Type()
)
pwTemplateMfibAllowedMdaTblLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTemplateMfibAllowedMdaTblLC.setStatus("current")
_PwTemplateMfibAllowedMdaTable_Object = MibTable
pwTemplateMfibAllowedMdaTable = _PwTemplateMfibAllowedMdaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 22)
)
if mibBuilder.loadTexts:
    pwTemplateMfibAllowedMdaTable.setStatus("current")
_PwTemplateMfibAllowedMdaEntry_Object = MibTableRow
pwTemplateMfibAllowedMdaEntry = _PwTemplateMfibAllowedMdaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 22, 1)
)
pwTemplateMfibAllowedMdaEntry.setIndexNames(
    (0, "TIMETRA-SDP-MIB", "pwTemplateId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    pwTemplateMfibAllowedMdaEntry.setStatus("current")
_PwTemplateMfibMdaRowStatus_Type = RowStatus
_PwTemplateMfibMdaRowStatus_Object = MibTableColumn
pwTemplateMfibMdaRowStatus = _PwTemplateMfibMdaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 22, 1, 1),
    _PwTemplateMfibMdaRowStatus_Type()
)
pwTemplateMfibMdaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateMfibMdaRowStatus.setStatus("current")
_SdpBindTlsMrpTableLastChanged_Type = TimeStamp
_SdpBindTlsMrpTableLastChanged_Object = MibScalar
sdpBindTlsMrpTableLastChanged = _SdpBindTlsMrpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 23),
    _SdpBindTlsMrpTableLastChanged_Type()
)
sdpBindTlsMrpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpTableLastChanged.setStatus("current")
_SdpBindTlsMrpTable_Object = MibTable
sdpBindTlsMrpTable = _SdpBindTlsMrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24)
)
if mibBuilder.loadTexts:
    sdpBindTlsMrpTable.setStatus("current")
_SdpBindTlsMrpEntry_Object = MibTableRow
sdpBindTlsMrpEntry = _SdpBindTlsMrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1)
)
sdpBindTlsMrpEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindTlsMrpEntry.setStatus("current")
_SdpBindTlsMrpLastChngd_Type = TimeStamp
_SdpBindTlsMrpLastChngd_Object = MibTableColumn
sdpBindTlsMrpLastChngd = _SdpBindTlsMrpLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 1),
    _SdpBindTlsMrpLastChngd_Type()
)
sdpBindTlsMrpLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpLastChngd.setStatus("current")


class _SdpBindTlsMrpJoinTime_Type(Unsigned32):
    """Custom type sdpBindTlsMrpJoinTime based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SdpBindTlsMrpJoinTime_Type.__name__ = "Unsigned32"
_SdpBindTlsMrpJoinTime_Object = MibTableColumn
sdpBindTlsMrpJoinTime = _SdpBindTlsMrpJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 2),
    _SdpBindTlsMrpJoinTime_Type()
)
sdpBindTlsMrpJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMrpJoinTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindTlsMrpJoinTime.setUnits("deciseconds")


class _SdpBindTlsMrpLeaveTime_Type(Unsigned32):
    """Custom type sdpBindTlsMrpLeaveTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 60),
    )


_SdpBindTlsMrpLeaveTime_Type.__name__ = "Unsigned32"
_SdpBindTlsMrpLeaveTime_Object = MibTableColumn
sdpBindTlsMrpLeaveTime = _SdpBindTlsMrpLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 3),
    _SdpBindTlsMrpLeaveTime_Type()
)
sdpBindTlsMrpLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMrpLeaveTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindTlsMrpLeaveTime.setUnits("deciseconds")


class _SdpBindTlsMrpLeaveAllTime_Type(Unsigned32):
    """Custom type sdpBindTlsMrpLeaveAllTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_SdpBindTlsMrpLeaveAllTime_Type.__name__ = "Unsigned32"
_SdpBindTlsMrpLeaveAllTime_Object = MibTableColumn
sdpBindTlsMrpLeaveAllTime = _SdpBindTlsMrpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 4),
    _SdpBindTlsMrpLeaveAllTime_Type()
)
sdpBindTlsMrpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMrpLeaveAllTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindTlsMrpLeaveAllTime.setUnits("deciseconds")


class _SdpBindTlsMrpPeriodicTime_Type(Unsigned32):
    """Custom type sdpBindTlsMrpPeriodicTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_SdpBindTlsMrpPeriodicTime_Type.__name__ = "Unsigned32"
_SdpBindTlsMrpPeriodicTime_Object = MibTableColumn
sdpBindTlsMrpPeriodicTime = _SdpBindTlsMrpPeriodicTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 5),
    _SdpBindTlsMrpPeriodicTime_Type()
)
sdpBindTlsMrpPeriodicTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMrpPeriodicTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindTlsMrpPeriodicTime.setUnits("deciseconds")


class _SdpBindTlsMrpPeriodicEnabled_Type(TruthValue):
    """Custom type sdpBindTlsMrpPeriodicEnabled based on TruthValue"""
    defaultValue = 2


_SdpBindTlsMrpPeriodicEnabled_Type.__name__ = "TruthValue"
_SdpBindTlsMrpPeriodicEnabled_Object = MibTableColumn
sdpBindTlsMrpPeriodicEnabled = _SdpBindTlsMrpPeriodicEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 6),
    _SdpBindTlsMrpPeriodicEnabled_Type()
)
sdpBindTlsMrpPeriodicEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMrpPeriodicEnabled.setStatus("current")
_SdpBindTlsMrpRxPdus_Type = Counter32
_SdpBindTlsMrpRxPdus_Object = MibTableColumn
sdpBindTlsMrpRxPdus = _SdpBindTlsMrpRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 7),
    _SdpBindTlsMrpRxPdus_Type()
)
sdpBindTlsMrpRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpRxPdus.setStatus("current")
_SdpBindTlsMrpDroppedPdus_Type = Counter32
_SdpBindTlsMrpDroppedPdus_Object = MibTableColumn
sdpBindTlsMrpDroppedPdus = _SdpBindTlsMrpDroppedPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 8),
    _SdpBindTlsMrpDroppedPdus_Type()
)
sdpBindTlsMrpDroppedPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpDroppedPdus.setStatus("current")
_SdpBindTlsMrpTxPdus_Type = Counter32
_SdpBindTlsMrpTxPdus_Object = MibTableColumn
sdpBindTlsMrpTxPdus = _SdpBindTlsMrpTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 9),
    _SdpBindTlsMrpTxPdus_Type()
)
sdpBindTlsMrpTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpTxPdus.setStatus("current")
_SdpBindTlsMrpRxNewEvent_Type = Counter32
_SdpBindTlsMrpRxNewEvent_Object = MibTableColumn
sdpBindTlsMrpRxNewEvent = _SdpBindTlsMrpRxNewEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 10),
    _SdpBindTlsMrpRxNewEvent_Type()
)
sdpBindTlsMrpRxNewEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpRxNewEvent.setStatus("current")
_SdpBindTlsMrpRxJoinInEvent_Type = Counter32
_SdpBindTlsMrpRxJoinInEvent_Object = MibTableColumn
sdpBindTlsMrpRxJoinInEvent = _SdpBindTlsMrpRxJoinInEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 11),
    _SdpBindTlsMrpRxJoinInEvent_Type()
)
sdpBindTlsMrpRxJoinInEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpRxJoinInEvent.setStatus("current")
_SdpBindTlsMrpRxInEvent_Type = Counter32
_SdpBindTlsMrpRxInEvent_Object = MibTableColumn
sdpBindTlsMrpRxInEvent = _SdpBindTlsMrpRxInEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 12),
    _SdpBindTlsMrpRxInEvent_Type()
)
sdpBindTlsMrpRxInEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpRxInEvent.setStatus("current")
_SdpBindTlsMrpRxJoinEmptyEvent_Type = Counter32
_SdpBindTlsMrpRxJoinEmptyEvent_Object = MibTableColumn
sdpBindTlsMrpRxJoinEmptyEvent = _SdpBindTlsMrpRxJoinEmptyEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 13),
    _SdpBindTlsMrpRxJoinEmptyEvent_Type()
)
sdpBindTlsMrpRxJoinEmptyEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpRxJoinEmptyEvent.setStatus("current")
_SdpBindTlsMrpRxEmptyEvent_Type = Counter32
_SdpBindTlsMrpRxEmptyEvent_Object = MibTableColumn
sdpBindTlsMrpRxEmptyEvent = _SdpBindTlsMrpRxEmptyEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 14),
    _SdpBindTlsMrpRxEmptyEvent_Type()
)
sdpBindTlsMrpRxEmptyEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpRxEmptyEvent.setStatus("current")
_SdpBindTlsMrpRxLeaveEvent_Type = Counter32
_SdpBindTlsMrpRxLeaveEvent_Object = MibTableColumn
sdpBindTlsMrpRxLeaveEvent = _SdpBindTlsMrpRxLeaveEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 15),
    _SdpBindTlsMrpRxLeaveEvent_Type()
)
sdpBindTlsMrpRxLeaveEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpRxLeaveEvent.setStatus("current")
_SdpBindTlsMrpTxNewEvent_Type = Counter32
_SdpBindTlsMrpTxNewEvent_Object = MibTableColumn
sdpBindTlsMrpTxNewEvent = _SdpBindTlsMrpTxNewEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 16),
    _SdpBindTlsMrpTxNewEvent_Type()
)
sdpBindTlsMrpTxNewEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpTxNewEvent.setStatus("current")
_SdpBindTlsMrpTxJoinInEvent_Type = Counter32
_SdpBindTlsMrpTxJoinInEvent_Object = MibTableColumn
sdpBindTlsMrpTxJoinInEvent = _SdpBindTlsMrpTxJoinInEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 17),
    _SdpBindTlsMrpTxJoinInEvent_Type()
)
sdpBindTlsMrpTxJoinInEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpTxJoinInEvent.setStatus("current")
_SdpBindTlsMrpTxInEvent_Type = Counter32
_SdpBindTlsMrpTxInEvent_Object = MibTableColumn
sdpBindTlsMrpTxInEvent = _SdpBindTlsMrpTxInEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 18),
    _SdpBindTlsMrpTxInEvent_Type()
)
sdpBindTlsMrpTxInEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpTxInEvent.setStatus("current")
_SdpBindTlsMrpTxJoinEmptyEvent_Type = Counter32
_SdpBindTlsMrpTxJoinEmptyEvent_Object = MibTableColumn
sdpBindTlsMrpTxJoinEmptyEvent = _SdpBindTlsMrpTxJoinEmptyEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 19),
    _SdpBindTlsMrpTxJoinEmptyEvent_Type()
)
sdpBindTlsMrpTxJoinEmptyEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpTxJoinEmptyEvent.setStatus("current")
_SdpBindTlsMrpTxEmptyEvent_Type = Counter32
_SdpBindTlsMrpTxEmptyEvent_Object = MibTableColumn
sdpBindTlsMrpTxEmptyEvent = _SdpBindTlsMrpTxEmptyEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 20),
    _SdpBindTlsMrpTxEmptyEvent_Type()
)
sdpBindTlsMrpTxEmptyEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpTxEmptyEvent.setStatus("current")
_SdpBindTlsMrpTxLeaveEvent_Type = Counter32
_SdpBindTlsMrpTxLeaveEvent_Object = MibTableColumn
sdpBindTlsMrpTxLeaveEvent = _SdpBindTlsMrpTxLeaveEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 21),
    _SdpBindTlsMrpTxLeaveEvent_Type()
)
sdpBindTlsMrpTxLeaveEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpTxLeaveEvent.setStatus("current")


class _SdpBindTlsMrpPolicy_Type(TNamedItemOrEmpty):
    """Custom type sdpBindTlsMrpPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_SdpBindTlsMrpPolicy_Type.__name__ = "TNamedItemOrEmpty"
_SdpBindTlsMrpPolicy_Object = MibTableColumn
sdpBindTlsMrpPolicy = _SdpBindTlsMrpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 22),
    _SdpBindTlsMrpPolicy_Type()
)
sdpBindTlsMrpPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMrpPolicy.setStatus("current")
_SdpBindTlsMmrpTable_Object = MibTable
sdpBindTlsMmrpTable = _SdpBindTlsMmrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 25)
)
if mibBuilder.loadTexts:
    sdpBindTlsMmrpTable.setStatus("current")
_SdpBindTlsMmrpEntry_Object = MibTableRow
sdpBindTlsMmrpEntry = _SdpBindTlsMmrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 25, 1)
)
sdpBindTlsMmrpEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindTlsMmrpMacAddr"),
)
if mibBuilder.loadTexts:
    sdpBindTlsMmrpEntry.setStatus("current")
_SdpBindTlsMmrpMacAddr_Type = MacAddress
_SdpBindTlsMmrpMacAddr_Object = MibTableColumn
sdpBindTlsMmrpMacAddr = _SdpBindTlsMmrpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 25, 1, 1),
    _SdpBindTlsMmrpMacAddr_Type()
)
sdpBindTlsMmrpMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBindTlsMmrpMacAddr.setStatus("current")
_SdpBindTlsMmrpDeclared_Type = TruthValue
_SdpBindTlsMmrpDeclared_Object = MibTableColumn
sdpBindTlsMmrpDeclared = _SdpBindTlsMmrpDeclared_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 25, 1, 2),
    _SdpBindTlsMmrpDeclared_Type()
)
sdpBindTlsMmrpDeclared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMmrpDeclared.setStatus("current")
_SdpBindTlsMmrpRegistered_Type = TruthValue
_SdpBindTlsMmrpRegistered_Object = MibTableColumn
sdpBindTlsMmrpRegistered = _SdpBindTlsMmrpRegistered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 25, 1, 3),
    _SdpBindTlsMmrpRegistered_Type()
)
sdpBindTlsMmrpRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMmrpRegistered.setStatus("current")
_SdpBindTlsMmrpEndStation_Type = TruthValue
_SdpBindTlsMmrpEndStation_Object = MibTableColumn
sdpBindTlsMmrpEndStation = _SdpBindTlsMmrpEndStation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 25, 1, 4),
    _SdpBindTlsMmrpEndStation_Type()
)
sdpBindTlsMmrpEndStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMmrpEndStation.setStatus("current")
_SdpAutoBindBgpInfoTableLC_Type = TimeStamp
_SdpAutoBindBgpInfoTableLC_Object = MibScalar
sdpAutoBindBgpInfoTableLC = _SdpAutoBindBgpInfoTableLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 26),
    _SdpAutoBindBgpInfoTableLC_Type()
)
sdpAutoBindBgpInfoTableLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAutoBindBgpInfoTableLC.setStatus("current")
_SdpAutoBindBgpInfoTable_Object = MibTable
sdpAutoBindBgpInfoTable = _SdpAutoBindBgpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 27)
)
if mibBuilder.loadTexts:
    sdpAutoBindBgpInfoTable.setStatus("current")
_SdpAutoBindBgpInfoEntry_Object = MibTableRow
sdpAutoBindBgpInfoEntry = _SdpAutoBindBgpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 27, 1)
)
sdpAutoBindBgpInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpAutoBindBgpInfoEntry.setStatus("current")
_SdpAutoBindBgpInfoTemplateId_Type = PWTemplateId
_SdpAutoBindBgpInfoTemplateId_Object = MibTableColumn
sdpAutoBindBgpInfoTemplateId = _SdpAutoBindBgpInfoTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 27, 1, 1),
    _SdpAutoBindBgpInfoTemplateId_Type()
)
sdpAutoBindBgpInfoTemplateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAutoBindBgpInfoTemplateId.setStatus("current")
_SdpAutoBindBgpInfoAGI_Type = TmnxVPNRouteDistinguisher
_SdpAutoBindBgpInfoAGI_Object = MibTableColumn
sdpAutoBindBgpInfoAGI = _SdpAutoBindBgpInfoAGI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 27, 1, 2),
    _SdpAutoBindBgpInfoAGI_Type()
)
sdpAutoBindBgpInfoAGI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAutoBindBgpInfoAGI.setStatus("current")
_SdpAutoBindBgpInfoSAII_Type = Unsigned32
_SdpAutoBindBgpInfoSAII_Object = MibTableColumn
sdpAutoBindBgpInfoSAII = _SdpAutoBindBgpInfoSAII_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 27, 1, 3),
    _SdpAutoBindBgpInfoSAII_Type()
)
sdpAutoBindBgpInfoSAII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAutoBindBgpInfoSAII.setStatus("current")
_SdpAutoBindBgpInfoTAII_Type = Unsigned32
_SdpAutoBindBgpInfoTAII_Object = MibTableColumn
sdpAutoBindBgpInfoTAII = _SdpAutoBindBgpInfoTAII_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 27, 1, 4),
    _SdpAutoBindBgpInfoTAII_Type()
)
sdpAutoBindBgpInfoTAII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAutoBindBgpInfoTAII.setStatus("current")
_SvcApplyEvalPwTemplate_ObjectIdentity = ObjectIdentity
svcApplyEvalPwTemplate = _SvcApplyEvalPwTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 28)
)


class _SvcApplyEvalPwTemplateSvcId_Type(TmnxServId):
    """Custom type svcApplyEvalPwTemplateSvcId based on TmnxServId"""
    defaultValue = 0


_SvcApplyEvalPwTemplateSvcId_Type.__name__ = "TmnxServId"
_SvcApplyEvalPwTemplateSvcId_Object = MibScalar
svcApplyEvalPwTemplateSvcId = _SvcApplyEvalPwTemplateSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 28, 1),
    _SvcApplyEvalPwTemplateSvcId_Type()
)
svcApplyEvalPwTemplateSvcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcApplyEvalPwTemplateSvcId.setStatus("current")


class _SvcApplyEvalPwTemplateId_Type(PWTemplateId):
    """Custom type svcApplyEvalPwTemplateId based on PWTemplateId"""
    defaultValue = 0


_SvcApplyEvalPwTemplateId_Type.__name__ = "PWTemplateId"
_SvcApplyEvalPwTemplateId_Object = MibScalar
svcApplyEvalPwTemplateId = _SvcApplyEvalPwTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 28, 2),
    _SvcApplyEvalPwTemplateId_Type()
)
svcApplyEvalPwTemplateId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcApplyEvalPwTemplateId.setStatus("current")


class _SvcApplyEvalPwTemplateAction_Type(TmnxActionType):
    """Custom type svcApplyEvalPwTemplateAction based on TmnxActionType"""
    defaultValue = 2


_SvcApplyEvalPwTemplateAction_Type.__name__ = "TmnxActionType"
_SvcApplyEvalPwTemplateAction_Object = MibScalar
svcApplyEvalPwTemplateAction = _SvcApplyEvalPwTemplateAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 28, 3),
    _SvcApplyEvalPwTemplateAction_Type()
)
svcApplyEvalPwTemplateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcApplyEvalPwTemplateAction.setStatus("current")


class _SvcApplyEvalPwTemplateSuccess_Type(TruthValue):
    """Custom type svcApplyEvalPwTemplateSuccess based on TruthValue"""
    defaultValue = 2


_SvcApplyEvalPwTemplateSuccess_Type.__name__ = "TruthValue"
_SvcApplyEvalPwTemplateSuccess_Object = MibScalar
svcApplyEvalPwTemplateSuccess = _SvcApplyEvalPwTemplateSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 28, 4),
    _SvcApplyEvalPwTemplateSuccess_Type()
)
svcApplyEvalPwTemplateSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcApplyEvalPwTemplateSuccess.setStatus("current")


class _SvcApplyEvalPwTemplateErrorMsg_Type(DisplayString):
    """Custom type svcApplyEvalPwTemplateErrorMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvcApplyEvalPwTemplateErrorMsg_Type.__name__ = "DisplayString"
_SvcApplyEvalPwTemplateErrorMsg_Object = MibScalar
svcApplyEvalPwTemplateErrorMsg = _SvcApplyEvalPwTemplateErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 28, 5),
    _SvcApplyEvalPwTemplateErrorMsg_Type()
)
svcApplyEvalPwTemplateErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcApplyEvalPwTemplateErrorMsg.setStatus("current")
_SvcApplyEvalPwTemplateTime_Type = TimeStamp
_SvcApplyEvalPwTemplateTime_Object = MibScalar
svcApplyEvalPwTemplateTime = _SvcApplyEvalPwTemplateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 28, 6),
    _SvcApplyEvalPwTemplateTime_Type()
)
svcApplyEvalPwTemplateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcApplyEvalPwTemplateTime.setStatus("current")
_SdpBindPbbTable_Object = MibTable
sdpBindPbbTable = _SdpBindPbbTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 29)
)
if mibBuilder.loadTexts:
    sdpBindPbbTable.setStatus("current")
_SdpBindPbbEntry_Object = MibTableRow
sdpBindPbbEntry = _SdpBindPbbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 29, 1)
)
sdpBindPbbEntry.setIndexNames(
    (0, "TIMETRA-SDP-MIB", "sdpBindPbbSvcIdIVpls"),
    (0, "TIMETRA-SDP-MIB", "sdpBindPbbSvcIdBVpls"),
    (0, "TIMETRA-SDP-MIB", "sdpBindPbbId"),
)
if mibBuilder.loadTexts:
    sdpBindPbbEntry.setStatus("current")
_SdpBindPbbSvcIdIVpls_Type = TmnxServId
_SdpBindPbbSvcIdIVpls_Object = MibTableColumn
sdpBindPbbSvcIdIVpls = _SdpBindPbbSvcIdIVpls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 29, 1, 1),
    _SdpBindPbbSvcIdIVpls_Type()
)
sdpBindPbbSvcIdIVpls.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBindPbbSvcIdIVpls.setStatus("current")
_SdpBindPbbSvcIdBVpls_Type = TmnxServId
_SdpBindPbbSvcIdBVpls_Object = MibTableColumn
sdpBindPbbSvcIdBVpls = _SdpBindPbbSvcIdBVpls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 29, 1, 2),
    _SdpBindPbbSvcIdBVpls_Type()
)
sdpBindPbbSvcIdBVpls.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBindPbbSvcIdBVpls.setStatus("current")
_SdpBindPbbId_Type = SdpBindId
_SdpBindPbbId_Object = MibTableColumn
sdpBindPbbId = _SdpBindPbbId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 29, 1, 3),
    _SdpBindPbbId_Type()
)
sdpBindPbbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBindPbbId.setStatus("current")
_SdpBindPbbRowStatus_Type = RowStatus
_SdpBindPbbRowStatus_Object = MibTableColumn
sdpBindPbbRowStatus = _SdpBindPbbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 29, 1, 4),
    _SdpBindPbbRowStatus_Type()
)
sdpBindPbbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindPbbRowStatus.setStatus("current")
_SdpBindPbbLastMgmtChange_Type = TimeStamp
_SdpBindPbbLastMgmtChange_Object = MibTableColumn
sdpBindPbbLastMgmtChange = _SdpBindPbbLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 29, 1, 5),
    _SdpBindPbbLastMgmtChange_Type()
)
sdpBindPbbLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPbbLastMgmtChange.setStatus("current")


class _SdpBindPbbIgmpSnpgMRouter_Type(TruthValue):
    """Custom type sdpBindPbbIgmpSnpgMRouter based on TruthValue"""
    defaultValue = 2


_SdpBindPbbIgmpSnpgMRouter_Type.__name__ = "TruthValue"
_SdpBindPbbIgmpSnpgMRouter_Object = MibTableColumn
sdpBindPbbIgmpSnpgMRouter = _SdpBindPbbIgmpSnpgMRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 29, 1, 6),
    _SdpBindPbbIgmpSnpgMRouter_Type()
)
sdpBindPbbIgmpSnpgMRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindPbbIgmpSnpgMRouter.setStatus("current")


class _SdpBindPbbMldSnpgMRouter_Type(TruthValue):
    """Custom type sdpBindPbbMldSnpgMRouter based on TruthValue"""
    defaultValue = 2


_SdpBindPbbMldSnpgMRouter_Type.__name__ = "TruthValue"
_SdpBindPbbMldSnpgMRouter_Object = MibTableColumn
sdpBindPbbMldSnpgMRouter = _SdpBindPbbMldSnpgMRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 29, 1, 7),
    _SdpBindPbbMldSnpgMRouter_Type()
)
sdpBindPbbMldSnpgMRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindPbbMldSnpgMRouter.setStatus("current")
_SdpBindFPropBMacAddrTblLastChgd_Type = TimeStamp
_SdpBindFPropBMacAddrTblLastChgd_Object = MibScalar
sdpBindFPropBMacAddrTblLastChgd = _SdpBindFPropBMacAddrTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 30),
    _SdpBindFPropBMacAddrTblLastChgd_Type()
)
sdpBindFPropBMacAddrTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindFPropBMacAddrTblLastChgd.setStatus("current")
_SdpBindFPropBMacAddrTable_Object = MibTable
sdpBindFPropBMacAddrTable = _SdpBindFPropBMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 31)
)
if mibBuilder.loadTexts:
    sdpBindFPropBMacAddrTable.setStatus("current")
_SdpBindFPropBMacAddrEntry_Object = MibTableRow
sdpBindFPropBMacAddrEntry = _SdpBindFPropBMacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 31, 1)
)
sdpBindFPropBMacAddrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindFPropBMacAddrOrMacNameTag"),
    (0, "TIMETRA-SDP-MIB", "sdpBindFPropBMacAddrOrMacName"),
)
if mibBuilder.loadTexts:
    sdpBindFPropBMacAddrEntry.setStatus("current")


class _SdpBindFPropBMacAddrOrMacNameTag_Type(Integer32):
    """Custom type sdpBindFPropBMacAddrOrMacNameTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("macName", 1),
          ("macAddr", 2))
    )


_SdpBindFPropBMacAddrOrMacNameTag_Type.__name__ = "Integer32"
_SdpBindFPropBMacAddrOrMacNameTag_Object = MibTableColumn
sdpBindFPropBMacAddrOrMacNameTag = _SdpBindFPropBMacAddrOrMacNameTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 31, 1, 1),
    _SdpBindFPropBMacAddrOrMacNameTag_Type()
)
sdpBindFPropBMacAddrOrMacNameTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBindFPropBMacAddrOrMacNameTag.setStatus("current")
_SdpBindFPropBMacAddrOrMacName_Type = TNamedItem
_SdpBindFPropBMacAddrOrMacName_Object = MibTableColumn
sdpBindFPropBMacAddrOrMacName = _SdpBindFPropBMacAddrOrMacName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 31, 1, 2),
    _SdpBindFPropBMacAddrOrMacName_Type()
)
sdpBindFPropBMacAddrOrMacName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBindFPropBMacAddrOrMacName.setStatus("current")
_SdpBindFPropBMacAddrRowStatus_Type = RowStatus
_SdpBindFPropBMacAddrRowStatus_Object = MibTableColumn
sdpBindFPropBMacAddrRowStatus = _SdpBindFPropBMacAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 31, 1, 3),
    _SdpBindFPropBMacAddrRowStatus_Type()
)
sdpBindFPropBMacAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindFPropBMacAddrRowStatus.setStatus("current")
_SdpAutoBindBgpVplsTableLC_Type = TimeStamp
_SdpAutoBindBgpVplsTableLC_Object = MibScalar
sdpAutoBindBgpVplsTableLC = _SdpAutoBindBgpVplsTableLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 32),
    _SdpAutoBindBgpVplsTableLC_Type()
)
sdpAutoBindBgpVplsTableLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAutoBindBgpVplsTableLC.setStatus("current")
_SdpAutoBindBgpVplsTable_Object = MibTable
sdpAutoBindBgpVplsTable = _SdpAutoBindBgpVplsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 33)
)
if mibBuilder.loadTexts:
    sdpAutoBindBgpVplsTable.setStatus("current")
_SdpAutoBindBgpVplsEntry_Object = MibTableRow
sdpAutoBindBgpVplsEntry = _SdpAutoBindBgpVplsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 33, 1)
)
sdpAutoBindBgpVplsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpAutoBindBgpVplsEntry.setStatus("current")
_SdpAutoBindBgpVplsTemplateId_Type = PWTemplateId
_SdpAutoBindBgpVplsTemplateId_Object = MibTableColumn
sdpAutoBindBgpVplsTemplateId = _SdpAutoBindBgpVplsTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 33, 1, 1),
    _SdpAutoBindBgpVplsTemplateId_Type()
)
sdpAutoBindBgpVplsTemplateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAutoBindBgpVplsTemplateId.setStatus("current")
_SdpAtBndBgp129Type2TableLC_Type = TimeStamp
_SdpAtBndBgp129Type2TableLC_Object = MibScalar
sdpAtBndBgp129Type2TableLC = _SdpAtBndBgp129Type2TableLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 34),
    _SdpAtBndBgp129Type2TableLC_Type()
)
sdpAtBndBgp129Type2TableLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAtBndBgp129Type2TableLC.setStatus("current")
_SdpAtBndBgp129Type2Table_Object = MibTable
sdpAtBndBgp129Type2Table = _SdpAtBndBgp129Type2Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 35)
)
if mibBuilder.loadTexts:
    sdpAtBndBgp129Type2Table.setStatus("current")
_SdpAtBndBgp129Type2Entry_Object = MibTableRow
sdpAtBndBgp129Type2Entry = _SdpAtBndBgp129Type2Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 35, 1)
)
sdpAtBndBgp129Type2Entry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpAtBndBgp129Type2Entry.setStatus("current")
_SdpAtBndBgp129Type2TemplateId_Type = PWTemplateId
_SdpAtBndBgp129Type2TemplateId_Object = MibTableColumn
sdpAtBndBgp129Type2TemplateId = _SdpAtBndBgp129Type2TemplateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 35, 1, 1),
    _SdpAtBndBgp129Type2TemplateId_Type()
)
sdpAtBndBgp129Type2TemplateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAtBndBgp129Type2TemplateId.setStatus("current")
_SdpAtBndBgp129Type2SaiiGlobalId_Type = TmnxPwGlobalId
_SdpAtBndBgp129Type2SaiiGlobalId_Object = MibTableColumn
sdpAtBndBgp129Type2SaiiGlobalId = _SdpAtBndBgp129Type2SaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 35, 1, 2),
    _SdpAtBndBgp129Type2SaiiGlobalId_Type()
)
sdpAtBndBgp129Type2SaiiGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAtBndBgp129Type2SaiiGlobalId.setStatus("current")
_SdpAtBndBgp129Type2SaiiPrefix_Type = Unsigned32
_SdpAtBndBgp129Type2SaiiPrefix_Object = MibTableColumn
sdpAtBndBgp129Type2SaiiPrefix = _SdpAtBndBgp129Type2SaiiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 35, 1, 3),
    _SdpAtBndBgp129Type2SaiiPrefix_Type()
)
sdpAtBndBgp129Type2SaiiPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAtBndBgp129Type2SaiiPrefix.setStatus("current")
_SdpAtBndBgp129Type2SaiiAcId_Type = Unsigned32
_SdpAtBndBgp129Type2SaiiAcId_Object = MibTableColumn
sdpAtBndBgp129Type2SaiiAcId = _SdpAtBndBgp129Type2SaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 35, 1, 4),
    _SdpAtBndBgp129Type2SaiiAcId_Type()
)
sdpAtBndBgp129Type2SaiiAcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAtBndBgp129Type2SaiiAcId.setStatus("current")
_SdpAtBndBgp129Type2TaiiGlobalId_Type = TmnxPwGlobalId
_SdpAtBndBgp129Type2TaiiGlobalId_Object = MibTableColumn
sdpAtBndBgp129Type2TaiiGlobalId = _SdpAtBndBgp129Type2TaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 35, 1, 5),
    _SdpAtBndBgp129Type2TaiiGlobalId_Type()
)
sdpAtBndBgp129Type2TaiiGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAtBndBgp129Type2TaiiGlobalId.setStatus("current")
_SdpAtBndBgp129Type2TaiiPrefix_Type = Unsigned32
_SdpAtBndBgp129Type2TaiiPrefix_Object = MibTableColumn
sdpAtBndBgp129Type2TaiiPrefix = _SdpAtBndBgp129Type2TaiiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 35, 1, 6),
    _SdpAtBndBgp129Type2TaiiPrefix_Type()
)
sdpAtBndBgp129Type2TaiiPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAtBndBgp129Type2TaiiPrefix.setStatus("current")
_SdpAtBndBgp129Type2TaiiAcId_Type = Unsigned32
_SdpAtBndBgp129Type2TaiiAcId_Object = MibTableColumn
sdpAtBndBgp129Type2TaiiAcId = _SdpAtBndBgp129Type2TaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 35, 1, 7),
    _SdpAtBndBgp129Type2TaiiAcId_Type()
)
sdpAtBndBgp129Type2TaiiAcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAtBndBgp129Type2TaiiAcId.setStatus("current")
_SdpBindEthCfmTableLastChanged_Type = TimeStamp
_SdpBindEthCfmTableLastChanged_Object = MibScalar
sdpBindEthCfmTableLastChanged = _SdpBindEthCfmTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 36),
    _SdpBindEthCfmTableLastChanged_Type()
)
sdpBindEthCfmTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindEthCfmTableLastChanged.setStatus("current")
_SdpBindEthCfmTable_Object = MibTable
sdpBindEthCfmTable = _SdpBindEthCfmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 37)
)
if mibBuilder.loadTexts:
    sdpBindEthCfmTable.setStatus("current")
_SdpBindEthCfmEntry_Object = MibTableRow
sdpBindEthCfmEntry = _SdpBindEthCfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 37, 1)
)
sdpBindEthCfmEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindEthCfmEntry.setStatus("current")
_SdpBindEthCfmRowLastChanged_Type = TimeStamp
_SdpBindEthCfmRowLastChanged_Object = MibTableColumn
sdpBindEthCfmRowLastChanged = _SdpBindEthCfmRowLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 37, 1, 1),
    _SdpBindEthCfmRowLastChanged_Type()
)
sdpBindEthCfmRowLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindEthCfmRowLastChanged.setStatus("current")


class _SdpBindEthCfmVMepFilter_Type(TruthValue):
    """Custom type sdpBindEthCfmVMepFilter based on TruthValue"""
    defaultValue = 2


_SdpBindEthCfmVMepFilter_Type.__name__ = "TruthValue"
_SdpBindEthCfmVMepFilter_Object = MibTableColumn
sdpBindEthCfmVMepFilter = _SdpBindEthCfmVMepFilter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 37, 1, 2),
    _SdpBindEthCfmVMepFilter_Type()
)
sdpBindEthCfmVMepFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEthCfmVMepFilter.setStatus("current")


class _SdpBindEthCfmSquelchIngress_Type(Bits):
    """Custom type sdpBindEthCfmSquelchIngress based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("level0", 0),
          ("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7))
    )

_SdpBindEthCfmSquelchIngress_Type.__name__ = "Bits"
_SdpBindEthCfmSquelchIngress_Object = MibTableColumn
sdpBindEthCfmSquelchIngress = _SdpBindEthCfmSquelchIngress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 37, 1, 3),
    _SdpBindEthCfmSquelchIngress_Type()
)
sdpBindEthCfmSquelchIngress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEthCfmSquelchIngress.setStatus("current")


class _SdpBindEthCfmCollectLmmStats_Type(TruthValue):
    """Custom type sdpBindEthCfmCollectLmmStats based on TruthValue"""
    defaultValue = 2


_SdpBindEthCfmCollectLmmStats_Type.__name__ = "TruthValue"
_SdpBindEthCfmCollectLmmStats_Object = MibTableColumn
sdpBindEthCfmCollectLmmStats = _SdpBindEthCfmCollectLmmStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 37, 1, 4),
    _SdpBindEthCfmCollectLmmStats_Type()
)
sdpBindEthCfmCollectLmmStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEthCfmCollectLmmStats.setStatus("current")


class _SdpBindEthCfmCollLmmFcSts_Type(TFCSet):
    """Custom type sdpBindEthCfmCollLmmFcSts based on TFCSet"""
    defaultBinValue = "0"


_SdpBindEthCfmCollLmmFcSts_Type.__name__ = "TFCSet"
_SdpBindEthCfmCollLmmFcSts_Object = MibTableColumn
sdpBindEthCfmCollLmmFcSts = _SdpBindEthCfmCollLmmFcSts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 37, 1, 5),
    _SdpBindEthCfmCollLmmFcSts_Type()
)
sdpBindEthCfmCollLmmFcSts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEthCfmCollLmmFcSts.setStatus("current")


class _SdpBindEthCfmCollLmmFcStsInP_Type(TFCSet):
    """Custom type sdpBindEthCfmCollLmmFcStsInP based on TFCSet"""
    defaultBinValue = "0"


_SdpBindEthCfmCollLmmFcStsInP_Type.__name__ = "TFCSet"
_SdpBindEthCfmCollLmmFcStsInP_Object = MibTableColumn
sdpBindEthCfmCollLmmFcStsInP = _SdpBindEthCfmCollLmmFcStsInP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 37, 1, 6),
    _SdpBindEthCfmCollLmmFcStsInP_Type()
)
sdpBindEthCfmCollLmmFcStsInP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEthCfmCollLmmFcStsInP.setStatus("current")


class _SdpBindEthCfmSquelchIngressCtag_Type(Bits):
    """Custom type sdpBindEthCfmSquelchIngressCtag based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("level0", 0),
          ("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7))
    )

_SdpBindEthCfmSquelchIngressCtag_Type.__name__ = "Bits"
_SdpBindEthCfmSquelchIngressCtag_Object = MibTableColumn
sdpBindEthCfmSquelchIngressCtag = _SdpBindEthCfmSquelchIngressCtag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 37, 1, 7),
    _SdpBindEthCfmSquelchIngressCtag_Type()
)
sdpBindEthCfmSquelchIngressCtag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEthCfmSquelchIngressCtag.setStatus("current")
_SdpBindTlsSpbTblLastChanged_Type = TimeStamp
_SdpBindTlsSpbTblLastChanged_Object = MibScalar
sdpBindTlsSpbTblLastChanged = _SdpBindTlsSpbTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 38),
    _SdpBindTlsSpbTblLastChanged_Type()
)
sdpBindTlsSpbTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsSpbTblLastChanged.setStatus("current")
_SdpBindTlsSpbTable_Object = MibTable
sdpBindTlsSpbTable = _SdpBindTlsSpbTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 39)
)
if mibBuilder.loadTexts:
    sdpBindTlsSpbTable.setStatus("current")
_SdpBindTlsSpbEntry_Object = MibTableRow
sdpBindTlsSpbEntry = _SdpBindTlsSpbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 39, 1)
)
sdpBindTlsSpbEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindTlsSpbEntry.setStatus("current")
_SdpBindTlsSpbRowStatus_Type = RowStatus
_SdpBindTlsSpbRowStatus_Object = MibTableColumn
sdpBindTlsSpbRowStatus = _SdpBindTlsSpbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 39, 1, 1),
    _SdpBindTlsSpbRowStatus_Type()
)
sdpBindTlsSpbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindTlsSpbRowStatus.setStatus("current")
_SdpBindTlsSpbLastChgd_Type = TimeStamp
_SdpBindTlsSpbLastChgd_Object = MibTableColumn
sdpBindTlsSpbLastChgd = _SdpBindTlsSpbLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 39, 1, 2),
    _SdpBindTlsSpbLastChgd_Type()
)
sdpBindTlsSpbLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsSpbLastChgd.setStatus("current")
_SdpBindTlsSpbIfIndex_Type = InterfaceIndexOrZero
_SdpBindTlsSpbIfIndex_Object = MibTableColumn
sdpBindTlsSpbIfIndex = _SdpBindTlsSpbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 39, 1, 3),
    _SdpBindTlsSpbIfIndex_Type()
)
sdpBindTlsSpbIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsSpbIfIndex.setStatus("current")


class _SdpBindTlsSpbAdminState_Type(TmnxAdminState):
    """Custom type sdpBindTlsSpbAdminState based on TmnxAdminState"""
    defaultValue = 3


_SdpBindTlsSpbAdminState_Type.__name__ = "TmnxAdminState"
_SdpBindTlsSpbAdminState_Object = MibTableColumn
sdpBindTlsSpbAdminState = _SdpBindTlsSpbAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 39, 1, 4),
    _SdpBindTlsSpbAdminState_Type()
)
sdpBindTlsSpbAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindTlsSpbAdminState.setStatus("current")
_SdpPwPortTblLastChanged_Type = TimeStamp
_SdpPwPortTblLastChanged_Object = MibScalar
sdpPwPortTblLastChanged = _SdpPwPortTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 40),
    _SdpPwPortTblLastChanged_Type()
)
sdpPwPortTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpPwPortTblLastChanged.setStatus("current")
_SdpPwPortTable_Object = MibTable
sdpPwPortTable = _SdpPwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41)
)
if mibBuilder.loadTexts:
    sdpPwPortTable.setStatus("current")
_SdpPwPortEntry_Object = MibTableRow
sdpPwPortEntry = _SdpPwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1)
)
sdpPwPortEntry.setIndexNames(
    (0, "TIMETRA-SDP-MIB", "sdpId"),
    (0, "TIMETRA-SDP-MIB", "sdpPwPortId"),
)
if mibBuilder.loadTexts:
    sdpPwPortEntry.setStatus("current")


class _SdpPwPortId_Type(Unsigned32):
    """Custom type sdpPwPortId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_SdpPwPortId_Type.__name__ = "Unsigned32"
_SdpPwPortId_Object = MibTableColumn
sdpPwPortId = _SdpPwPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 1),
    _SdpPwPortId_Type()
)
sdpPwPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpPwPortId.setStatus("current")
_SdpPwPortRowStatus_Type = RowStatus
_SdpPwPortRowStatus_Object = MibTableColumn
sdpPwPortRowStatus = _SdpPwPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 2),
    _SdpPwPortRowStatus_Type()
)
sdpPwPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortRowStatus.setStatus("current")
_SdpPwPortLastChgd_Type = TimeStamp
_SdpPwPortLastChgd_Object = MibTableColumn
sdpPwPortLastChgd = _SdpPwPortLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 3),
    _SdpPwPortLastChgd_Type()
)
sdpPwPortLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpPwPortLastChgd.setStatus("current")


class _SdpPwPortAdminStatus_Type(ServiceAdminStatus):
    """Custom type sdpPwPortAdminStatus based on ServiceAdminStatus"""
    defaultValue = 2


_SdpPwPortAdminStatus_Type.__name__ = "ServiceAdminStatus"
_SdpPwPortAdminStatus_Object = MibTableColumn
sdpPwPortAdminStatus = _SdpPwPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 4),
    _SdpPwPortAdminStatus_Type()
)
sdpPwPortAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortAdminStatus.setStatus("current")
_SdpPwPortVcId_Type = TmnxVcId
_SdpPwPortVcId_Object = MibTableColumn
sdpPwPortVcId = _SdpPwPortVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 5),
    _SdpPwPortVcId_Type()
)
sdpPwPortVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortVcId.setStatus("current")


class _SdpPwPortEncapType_Type(Integer32):
    """Custom type sdpPwPortEncapType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("dot1q", 2),
          ("qinq", 10))
    )


_SdpPwPortEncapType_Type.__name__ = "Integer32"
_SdpPwPortEncapType_Object = MibTableColumn
sdpPwPortEncapType = _SdpPwPortEncapType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 6),
    _SdpPwPortEncapType_Type()
)
sdpPwPortEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortEncapType.setStatus("obsolete")


class _SdpPwPortOperStatus_Type(Integer32):
    """Custom type sdpPwPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 5))
    )


_SdpPwPortOperStatus_Type.__name__ = "Integer32"
_SdpPwPortOperStatus_Object = MibTableColumn
sdpPwPortOperStatus = _SdpPwPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 7),
    _SdpPwPortOperStatus_Type()
)
sdpPwPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpPwPortOperStatus.setStatus("current")


class _SdpPwPortOperFlags_Type(Bits):
    """Custom type sdpPwPortOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("sdpBindAdminDown", 0),
          ("svcAdminDown", 1),
          ("stitchingSvcTxDown", 2),
          ("sdpOperDown", 3),
          ("sdpPathMtuTooSmall", 4),
          ("noIngressVcLabel", 5),
          ("noEgressVcLabel", 6),
          ("svcMtuMismatch", 7),
          ("vcTypeMismatch", 8),
          ("relearnLimitExceeded", 9),
          ("iesIfAdminDown", 10),
          ("releasedIngressVcLabel", 11),
          ("labelsExhausted", 12),
          ("svcParamMismatch", 13),
          ("insufficientBandwidth", 14),
          ("pwPeerFaultStatusBits", 15),
          ("meshSdpDown", 16),
          ("notManagedByMcRing", 17),
          ("outOfResource", 18),
          ("mhStandby", 19),
          ("oamDownMepFault", 20),
          ("oamUpMepFault", 21),
          ("standbySigSlaveTxDown", 22),
          ("operGrpDown", 23),
          ("withdrawnIngressVcLabel", 24),
          ("labelStackLimitExceeded", 25),
          ("stitchingSvcPwFault", 26))
    )

_SdpPwPortOperFlags_Type.__name__ = "Bits"
_SdpPwPortOperFlags_Object = MibTableColumn
sdpPwPortOperFlags = _SdpPwPortOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 8),
    _SdpPwPortOperFlags_Type()
)
sdpPwPortOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpPwPortOperFlags.setStatus("current")


class _SdpPwPortVcType_Type(SdpBindVcType):
    """Custom type sdpPwPortVcType based on SdpBindVcType"""
    defaultValue = 2


_SdpPwPortVcType_Type.__name__ = "SdpBindVcType"
_SdpPwPortVcType_Object = MibTableColumn
sdpPwPortVcType = _SdpPwPortVcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 9),
    _SdpPwPortVcType_Type()
)
sdpPwPortVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortVcType.setStatus("current")


class _SdpPwPortVlanVcTag_Type(Unsigned32):
    """Custom type sdpPwPortVlanVcTag based on Unsigned32"""
    defaultValue = 4095

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SdpPwPortVlanVcTag_Type.__name__ = "Unsigned32"
_SdpPwPortVlanVcTag_Object = MibTableColumn
sdpPwPortVlanVcTag = _SdpPwPortVlanVcTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 10),
    _SdpPwPortVlanVcTag_Type()
)
sdpPwPortVlanVcTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortVlanVcTag.setStatus("current")


class _SdpPwPortEgrShapVPort_Type(TNamedItemOrEmpty):
    """Custom type sdpPwPortEgrShapVPort based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SdpPwPortEgrShapVPort_Type.__name__ = "TNamedItemOrEmpty"
_SdpPwPortEgrShapVPort_Object = MibTableColumn
sdpPwPortEgrShapVPort = _SdpPwPortEgrShapVPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 11),
    _SdpPwPortEgrShapVPort_Type()
)
sdpPwPortEgrShapVPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortEgrShapVPort.setStatus("current")


class _SdpPwPortEgrShapDefIntDestId_Type(TNamedItemOrEmpty):
    """Custom type sdpPwPortEgrShapDefIntDestId based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SdpPwPortEgrShapDefIntDestId_Type.__name__ = "TNamedItemOrEmpty"
_SdpPwPortEgrShapDefIntDestId_Object = MibTableColumn
sdpPwPortEgrShapDefIntDestId = _SdpPwPortEgrShapDefIntDestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 12),
    _SdpPwPortEgrShapDefIntDestId_Type()
)
sdpPwPortEgrShapDefIntDestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortEgrShapDefIntDestId.setStatus("current")


class _SdpPwPortEgrShapSapSecShaper_Type(TNamedItemOrEmpty):
    """Custom type sdpPwPortEgrShapSapSecShaper based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SdpPwPortEgrShapSapSecShaper_Type.__name__ = "TNamedItemOrEmpty"
_SdpPwPortEgrShapSapSecShaper_Object = MibTableColumn
sdpPwPortEgrShapSapSecShaper = _SdpPwPortEgrShapSapSecShaper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 13),
    _SdpPwPortEgrShapSapSecShaper_Type()
)
sdpPwPortEgrShapSapSecShaper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortEgrShapSapSecShaper.setStatus("current")


class _SdpPwPortMonOperGrp_Type(TNamedItemOrEmpty):
    """Custom type sdpPwPortMonOperGrp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SdpPwPortMonOperGrp_Type.__name__ = "TNamedItemOrEmpty"
_SdpPwPortMonOperGrp_Object = MibTableColumn
sdpPwPortMonOperGrp = _SdpPwPortMonOperGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 14),
    _SdpPwPortMonOperGrp_Type()
)
sdpPwPortMonOperGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortMonOperGrp.setStatus("current")


class _SdpPwPortIngVcLabel_Type(Unsigned32):
    """Custom type sdpPwPortIngVcLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1048575),
    )


_SdpPwPortIngVcLabel_Type.__name__ = "Unsigned32"
_SdpPwPortIngVcLabel_Object = MibTableColumn
sdpPwPortIngVcLabel = _SdpPwPortIngVcLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 15),
    _SdpPwPortIngVcLabel_Type()
)
sdpPwPortIngVcLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortIngVcLabel.setStatus("current")


class _SdpPwPortEgrVcLabel_Type(Unsigned32):
    """Custom type sdpPwPortEgrVcLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1048575),
    )


_SdpPwPortEgrVcLabel_Type.__name__ = "Unsigned32"
_SdpPwPortEgrVcLabel_Object = MibTableColumn
sdpPwPortEgrVcLabel = _SdpPwPortEgrVcLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 16),
    _SdpPwPortEgrVcLabel_Type()
)
sdpPwPortEgrVcLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortEgrVcLabel.setStatus("current")


class _SdpPwPortControlWord_Type(TruthValue):
    """Custom type sdpPwPortControlWord based on TruthValue"""
    defaultValue = 2


_SdpPwPortControlWord_Type.__name__ = "TruthValue"
_SdpPwPortControlWord_Object = MibTableColumn
sdpPwPortControlWord = _SdpPwPortControlWord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 17),
    _SdpPwPortControlWord_Type()
)
sdpPwPortControlWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortControlWord.setStatus("current")


class _SdpPwPortEntropyLabel_Type(TruthValue):
    """Custom type sdpPwPortEntropyLabel based on TruthValue"""
    defaultValue = 2


_SdpPwPortEntropyLabel_Type.__name__ = "TruthValue"
_SdpPwPortEntropyLabel_Object = MibTableColumn
sdpPwPortEntropyLabel = _SdpPwPortEntropyLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 18),
    _SdpPwPortEntropyLabel_Type()
)
sdpPwPortEntropyLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortEntropyLabel.setStatus("current")


class _SdpPwPortAdvSvcMtu_Type(Integer32):
    """Custom type sdpPwPortAdvSvcMtu based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 9782),
    )


_SdpPwPortAdvSvcMtu_Type.__name__ = "Integer32"
_SdpPwPortAdvSvcMtu_Object = MibTableColumn
sdpPwPortAdvSvcMtu = _SdpPwPortAdvSvcMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 41, 1, 19),
    _SdpPwPortAdvSvcMtu_Type()
)
sdpPwPortAdvSvcMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortAdvSvcMtu.setStatus("current")
_SdpGrpTblLastChanged_Type = TimeStamp
_SdpGrpTblLastChanged_Object = MibScalar
sdpGrpTblLastChanged = _SdpGrpTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 42),
    _SdpGrpTblLastChanged_Type()
)
sdpGrpTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpGrpTblLastChanged.setStatus("current")
_SdpGrpTable_Object = MibTable
sdpGrpTable = _SdpGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 43)
)
if mibBuilder.loadTexts:
    sdpGrpTable.setStatus("current")
_SdpGrpEntry_Object = MibTableRow
sdpGrpEntry = _SdpGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 43, 1)
)
sdpGrpEntry.setIndexNames(
    (0, "TIMETRA-SDP-MIB", "sdpGrpName"),
)
if mibBuilder.loadTexts:
    sdpGrpEntry.setStatus("current")
_SdpGrpName_Type = TNamedItem
_SdpGrpName_Object = MibTableColumn
sdpGrpName = _SdpGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 43, 1, 1),
    _SdpGrpName_Type()
)
sdpGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpGrpName.setStatus("current")
_SdpGrpRowStatus_Type = RowStatus
_SdpGrpRowStatus_Object = MibTableColumn
sdpGrpRowStatus = _SdpGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 43, 1, 2),
    _SdpGrpRowStatus_Type()
)
sdpGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpGrpRowStatus.setStatus("current")
_SdpGrpLastChange_Type = TimeStamp
_SdpGrpLastChange_Object = MibTableColumn
sdpGrpLastChange = _SdpGrpLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 43, 1, 3),
    _SdpGrpLastChange_Type()
)
sdpGrpLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpGrpLastChange.setStatus("current")


class _SdpGrpValue_Type(Unsigned32):
    """Custom type sdpGrpValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SdpGrpValue_Type.__name__ = "Unsigned32"
_SdpGrpValue_Object = MibTableColumn
sdpGrpValue = _SdpGrpValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 43, 1, 4),
    _SdpGrpValue_Type()
)
sdpGrpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpGrpValue.setStatus("current")
_SdpSdpGrpTblLastChanged_Type = TimeStamp
_SdpSdpGrpTblLastChanged_Object = MibScalar
sdpSdpGrpTblLastChanged = _SdpSdpGrpTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 44),
    _SdpSdpGrpTblLastChanged_Type()
)
sdpSdpGrpTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpSdpGrpTblLastChanged.setStatus("current")
_SdpSdpGrpTable_Object = MibTable
sdpSdpGrpTable = _SdpSdpGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 45)
)
if mibBuilder.loadTexts:
    sdpSdpGrpTable.setStatus("current")
_SdpSdpGrpEntry_Object = MibTableRow
sdpSdpGrpEntry = _SdpSdpGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 45, 1)
)
sdpSdpGrpEntry.setIndexNames(
    (0, "TIMETRA-SDP-MIB", "sdpId"),
    (0, "TIMETRA-SDP-MIB", "sdpGrpName"),
)
if mibBuilder.loadTexts:
    sdpSdpGrpEntry.setStatus("current")
_SdpSdpGrpRowStatus_Type = RowStatus
_SdpSdpGrpRowStatus_Object = MibTableColumn
sdpSdpGrpRowStatus = _SdpSdpGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 45, 1, 1),
    _SdpSdpGrpRowStatus_Type()
)
sdpSdpGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpSdpGrpRowStatus.setStatus("current")
_SdpSdpGrpLastChange_Type = TimeStamp
_SdpSdpGrpLastChange_Object = MibTableColumn
sdpSdpGrpLastChange = _SdpSdpGrpLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 45, 1, 2),
    _SdpSdpGrpLastChange_Type()
)
sdpSdpGrpLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpSdpGrpLastChange.setStatus("current")
_PwTempIncSdpGrpTableLastChanged_Type = TimeStamp
_PwTempIncSdpGrpTableLastChanged_Object = MibScalar
pwTempIncSdpGrpTableLastChanged = _PwTempIncSdpGrpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 46),
    _PwTempIncSdpGrpTableLastChanged_Type()
)
pwTempIncSdpGrpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTempIncSdpGrpTableLastChanged.setStatus("current")
_PwTempIncSdpGrpTable_Object = MibTable
pwTempIncSdpGrpTable = _PwTempIncSdpGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 47)
)
if mibBuilder.loadTexts:
    pwTempIncSdpGrpTable.setStatus("current")
_PwTempIncSdpGrpEntry_Object = MibTableRow
pwTempIncSdpGrpEntry = _PwTempIncSdpGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 47, 1)
)
pwTempIncSdpGrpEntry.setIndexNames(
    (0, "TIMETRA-SDP-MIB", "pwTemplateId"),
    (0, "TIMETRA-SDP-MIB", "sdpGrpName"),
)
if mibBuilder.loadTexts:
    pwTempIncSdpGrpEntry.setStatus("current")
_PwTempIncSdpGrpRowStatus_Type = RowStatus
_PwTempIncSdpGrpRowStatus_Object = MibTableColumn
pwTempIncSdpGrpRowStatus = _PwTempIncSdpGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 47, 1, 1),
    _PwTempIncSdpGrpRowStatus_Type()
)
pwTempIncSdpGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTempIncSdpGrpRowStatus.setStatus("current")
_PwTempIncSdpGrpLastChanged_Type = TimeStamp
_PwTempIncSdpGrpLastChanged_Object = MibTableColumn
pwTempIncSdpGrpLastChanged = _PwTempIncSdpGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 47, 1, 2),
    _PwTempIncSdpGrpLastChanged_Type()
)
pwTempIncSdpGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTempIncSdpGrpLastChanged.setStatus("current")
_PwTempExcSdpGrpTableLastChanged_Type = TimeStamp
_PwTempExcSdpGrpTableLastChanged_Object = MibScalar
pwTempExcSdpGrpTableLastChanged = _PwTempExcSdpGrpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 48),
    _PwTempExcSdpGrpTableLastChanged_Type()
)
pwTempExcSdpGrpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTempExcSdpGrpTableLastChanged.setStatus("current")
_PwTempExcSdpGrpTable_Object = MibTable
pwTempExcSdpGrpTable = _PwTempExcSdpGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 49)
)
if mibBuilder.loadTexts:
    pwTempExcSdpGrpTable.setStatus("current")
_PwTempExcSdpGrpEntry_Object = MibTableRow
pwTempExcSdpGrpEntry = _PwTempExcSdpGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 49, 1)
)
pwTempExcSdpGrpEntry.setIndexNames(
    (0, "TIMETRA-SDP-MIB", "pwTemplateId"),
    (0, "TIMETRA-SDP-MIB", "sdpGrpName"),
)
if mibBuilder.loadTexts:
    pwTempExcSdpGrpEntry.setStatus("current")
_PwTempExcSdpGrpRowStatus_Type = RowStatus
_PwTempExcSdpGrpRowStatus_Object = MibTableColumn
pwTempExcSdpGrpRowStatus = _PwTempExcSdpGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 49, 1, 1),
    _PwTempExcSdpGrpRowStatus_Type()
)
pwTempExcSdpGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTempExcSdpGrpRowStatus.setStatus("current")
_PwTempExcSdpGrpLastChanged_Type = TimeStamp
_PwTempExcSdpGrpLastChanged_Object = MibTableColumn
pwTempExcSdpGrpLastChanged = _PwTempExcSdpGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 49, 1, 2),
    _PwTempExcSdpGrpLastChanged_Type()
)
pwTempExcSdpGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTempExcSdpGrpLastChanged.setStatus("current")
_SdpBindPwPathTableLastChanged_Type = TimeStamp
_SdpBindPwPathTableLastChanged_Object = MibScalar
sdpBindPwPathTableLastChanged = _SdpBindPwPathTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 50),
    _SdpBindPwPathTableLastChanged_Type()
)
sdpBindPwPathTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPwPathTableLastChanged.setStatus("current")
_SdpBindPwPathTable_Object = MibTable
sdpBindPwPathTable = _SdpBindPwPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 51)
)
if mibBuilder.loadTexts:
    sdpBindPwPathTable.setStatus("current")
_SdpBindPwPathEntry_Object = MibTableRow
sdpBindPwPathEntry = _SdpBindPwPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 51, 1)
)
sdpBindPwPathEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindPwPathEntry.setStatus("current")
_SdpBindPwPathRowStatus_Type = RowStatus
_SdpBindPwPathRowStatus_Object = MibTableColumn
sdpBindPwPathRowStatus = _SdpBindPwPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 51, 1, 1),
    _SdpBindPwPathRowStatus_Type()
)
sdpBindPwPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindPwPathRowStatus.setStatus("current")
_SdpBindPwPathLastChanged_Type = TimeStamp
_SdpBindPwPathLastChanged_Object = MibTableColumn
sdpBindPwPathLastChanged = _SdpBindPwPathLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 51, 1, 2),
    _SdpBindPwPathLastChanged_Type()
)
sdpBindPwPathLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPwPathLastChanged.setStatus("current")


class _SdpBindPwPathAgi_Type(TmnxVPNRouteDistinguisher):
    """Custom type sdpBindPwPathAgi based on TmnxVPNRouteDistinguisher"""
    defaultHexValue = "0000000000000000"


_SdpBindPwPathAgi_Type.__name__ = "TmnxVPNRouteDistinguisher"
_SdpBindPwPathAgi_Object = MibTableColumn
sdpBindPwPathAgi = _SdpBindPwPathAgi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 51, 1, 3),
    _SdpBindPwPathAgi_Type()
)
sdpBindPwPathAgi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindPwPathAgi.setStatus("current")


class _SdpBindPwPathSaiiGlobalId_Type(TmnxMplsTpGlobalID):
    """Custom type sdpBindPwPathSaiiGlobalId based on TmnxMplsTpGlobalID"""
    defaultValue = 0


_SdpBindPwPathSaiiGlobalId_Type.__name__ = "TmnxMplsTpGlobalID"
_SdpBindPwPathSaiiGlobalId_Object = MibTableColumn
sdpBindPwPathSaiiGlobalId = _SdpBindPwPathSaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 51, 1, 4),
    _SdpBindPwPathSaiiGlobalId_Type()
)
sdpBindPwPathSaiiGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindPwPathSaiiGlobalId.setStatus("current")


class _SdpBindPwPathSaiiNodeId_Type(TmnxMplsTpNodeID):
    """Custom type sdpBindPwPathSaiiNodeId based on TmnxMplsTpNodeID"""
    defaultValue = 0


_SdpBindPwPathSaiiNodeId_Type.__name__ = "TmnxMplsTpNodeID"
_SdpBindPwPathSaiiNodeId_Object = MibTableColumn
sdpBindPwPathSaiiNodeId = _SdpBindPwPathSaiiNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 51, 1, 5),
    _SdpBindPwPathSaiiNodeId_Type()
)
sdpBindPwPathSaiiNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindPwPathSaiiNodeId.setStatus("current")


class _SdpBindPwPathSaiiAcId_Type(Unsigned32):
    """Custom type sdpBindPwPathSaiiAcId based on Unsigned32"""
    defaultValue = 0


_SdpBindPwPathSaiiAcId_Type.__name__ = "Unsigned32"
_SdpBindPwPathSaiiAcId_Object = MibTableColumn
sdpBindPwPathSaiiAcId = _SdpBindPwPathSaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 51, 1, 6),
    _SdpBindPwPathSaiiAcId_Type()
)
sdpBindPwPathSaiiAcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindPwPathSaiiAcId.setStatus("current")


class _SdpBindPwPathTaiiGlobalId_Type(TmnxMplsTpGlobalID):
    """Custom type sdpBindPwPathTaiiGlobalId based on TmnxMplsTpGlobalID"""
    defaultValue = 0


_SdpBindPwPathTaiiGlobalId_Type.__name__ = "TmnxMplsTpGlobalID"
_SdpBindPwPathTaiiGlobalId_Object = MibTableColumn
sdpBindPwPathTaiiGlobalId = _SdpBindPwPathTaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 51, 1, 7),
    _SdpBindPwPathTaiiGlobalId_Type()
)
sdpBindPwPathTaiiGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindPwPathTaiiGlobalId.setStatus("current")


class _SdpBindPwPathTaiiNodeId_Type(TmnxMplsTpNodeID):
    """Custom type sdpBindPwPathTaiiNodeId based on TmnxMplsTpNodeID"""
    defaultValue = 0


_SdpBindPwPathTaiiNodeId_Type.__name__ = "TmnxMplsTpNodeID"
_SdpBindPwPathTaiiNodeId_Object = MibTableColumn
sdpBindPwPathTaiiNodeId = _SdpBindPwPathTaiiNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 51, 1, 8),
    _SdpBindPwPathTaiiNodeId_Type()
)
sdpBindPwPathTaiiNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindPwPathTaiiNodeId.setStatus("current")


class _SdpBindPwPathTaiiAcId_Type(Unsigned32):
    """Custom type sdpBindPwPathTaiiAcId based on Unsigned32"""
    defaultValue = 0


_SdpBindPwPathTaiiAcId_Type.__name__ = "Unsigned32"
_SdpBindPwPathTaiiAcId_Object = MibTableColumn
sdpBindPwPathTaiiAcId = _SdpBindPwPathTaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 51, 1, 9),
    _SdpBindPwPathTaiiAcId_Type()
)
sdpBindPwPathTaiiAcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindPwPathTaiiAcId.setStatus("current")
_SdpBindCtrlChanPwTableLastChgd_Type = TimeStamp
_SdpBindCtrlChanPwTableLastChgd_Object = MibScalar
sdpBindCtrlChanPwTableLastChgd = _SdpBindCtrlChanPwTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 52),
    _SdpBindCtrlChanPwTableLastChgd_Type()
)
sdpBindCtrlChanPwTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwTableLastChgd.setStatus("current")
_SdpBindCtrlChanPwTable_Object = MibTable
sdpBindCtrlChanPwTable = _SdpBindCtrlChanPwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 53)
)
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwTable.setStatus("current")
_SdpBindCtrlChanPwEntry_Object = MibTableRow
sdpBindCtrlChanPwEntry = _SdpBindCtrlChanPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 53, 1)
)
sdpBindCtrlChanPwEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwEntry.setStatus("current")
_SdpBindCtrlChanPwLastChanged_Type = TimeStamp
_SdpBindCtrlChanPwLastChanged_Object = MibTableColumn
sdpBindCtrlChanPwLastChanged = _SdpBindCtrlChanPwLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 53, 1, 1),
    _SdpBindCtrlChanPwLastChanged_Type()
)
sdpBindCtrlChanPwLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwLastChanged.setStatus("current")


class _SdpBindCtrlChanPwStatus_Type(TmnxEnabledDisabled):
    """Custom type sdpBindCtrlChanPwStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_SdpBindCtrlChanPwStatus_Type.__name__ = "TmnxEnabledDisabled"
_SdpBindCtrlChanPwStatus_Object = MibTableColumn
sdpBindCtrlChanPwStatus = _SdpBindCtrlChanPwStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 53, 1, 2),
    _SdpBindCtrlChanPwStatus_Type()
)
sdpBindCtrlChanPwStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwStatus.setStatus("current")


class _SdpBindCtrlChanPwRefreshTimer_Type(Unsigned32):
    """Custom type sdpBindCtrlChanPwRefreshTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 65535),
    )


_SdpBindCtrlChanPwRefreshTimer_Type.__name__ = "Unsigned32"
_SdpBindCtrlChanPwRefreshTimer_Object = MibTableColumn
sdpBindCtrlChanPwRefreshTimer = _SdpBindCtrlChanPwRefreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 53, 1, 3),
    _SdpBindCtrlChanPwRefreshTimer_Type()
)
sdpBindCtrlChanPwRefreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwRefreshTimer.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwRefreshTimer.setUnits("seconds")
_SdpBindCtrlChanPwPeerExpired_Type = TruthValue
_SdpBindCtrlChanPwPeerExpired_Object = MibTableColumn
sdpBindCtrlChanPwPeerExpired = _SdpBindCtrlChanPwPeerExpired_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 53, 1, 4),
    _SdpBindCtrlChanPwPeerExpired_Type()
)
sdpBindCtrlChanPwPeerExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwPeerExpired.setStatus("current")


class _SdpBindCtrlChanPwRequestTimer_Type(Unsigned32):
    """Custom type sdpBindCtrlChanPwRequestTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 65535),
    )


_SdpBindCtrlChanPwRequestTimer_Type.__name__ = "Unsigned32"
_SdpBindCtrlChanPwRequestTimer_Object = MibTableColumn
sdpBindCtrlChanPwRequestTimer = _SdpBindCtrlChanPwRequestTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 53, 1, 5),
    _SdpBindCtrlChanPwRequestTimer_Type()
)
sdpBindCtrlChanPwRequestTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwRequestTimer.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwRequestTimer.setUnits("seconds")


class _SdpBindCtrlChanPwRetryTimer_Type(Unsigned32):
    """Custom type sdpBindCtrlChanPwRetryTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 60),
    )


_SdpBindCtrlChanPwRetryTimer_Type.__name__ = "Unsigned32"
_SdpBindCtrlChanPwRetryTimer_Object = MibTableColumn
sdpBindCtrlChanPwRetryTimer = _SdpBindCtrlChanPwRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 53, 1, 6),
    _SdpBindCtrlChanPwRetryTimer_Type()
)
sdpBindCtrlChanPwRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwRetryTimer.setUnits("seconds")


class _SdpBindCtrlChanPwTimeoutMult_Type(Unsigned32):
    """Custom type sdpBindCtrlChanPwTimeoutMult based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 15),
    )


_SdpBindCtrlChanPwTimeoutMult_Type.__name__ = "Unsigned32"
_SdpBindCtrlChanPwTimeoutMult_Object = MibTableColumn
sdpBindCtrlChanPwTimeoutMult = _SdpBindCtrlChanPwTimeoutMult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 53, 1, 7),
    _SdpBindCtrlChanPwTimeoutMult_Type()
)
sdpBindCtrlChanPwTimeoutMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwTimeoutMult.setStatus("current")


class _SdpBindCtrlChanPwAck_Type(TruthValue):
    """Custom type sdpBindCtrlChanPwAck based on TruthValue"""
    defaultValue = 2


_SdpBindCtrlChanPwAck_Type.__name__ = "TruthValue"
_SdpBindCtrlChanPwAck_Object = MibTableColumn
sdpBindCtrlChanPwAck = _SdpBindCtrlChanPwAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 53, 1, 8),
    _SdpBindCtrlChanPwAck_Type()
)
sdpBindCtrlChanPwAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwAck.setStatus("current")
_SdpAutoBindBgpVpwsTable_Object = MibTable
sdpAutoBindBgpVpwsTable = _SdpAutoBindBgpVpwsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 54)
)
if mibBuilder.loadTexts:
    sdpAutoBindBgpVpwsTable.setStatus("current")
_SdpAutoBindBgpVpwsEntry_Object = MibTableRow
sdpAutoBindBgpVpwsEntry = _SdpAutoBindBgpVpwsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 54, 1)
)
sdpAutoBindBgpVpwsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpAutoBindBgpVpwsEntry.setStatus("current")
_SdpAutoBindBgpVpwsTemplateId_Type = PWTemplateId
_SdpAutoBindBgpVpwsTemplateId_Object = MibTableColumn
sdpAutoBindBgpVpwsTemplateId = _SdpAutoBindBgpVpwsTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 54, 1, 1),
    _SdpAutoBindBgpVpwsTemplateId_Type()
)
sdpAutoBindBgpVpwsTemplateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAutoBindBgpVpwsTemplateId.setStatus("current")
_SdpBindL2tpv3Table_Object = MibTable
sdpBindL2tpv3Table = _SdpBindL2tpv3Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 55)
)
if mibBuilder.loadTexts:
    sdpBindL2tpv3Table.setStatus("current")
_SdpBindL2tpv3Entry_Object = MibTableRow
sdpBindL2tpv3Entry = _SdpBindL2tpv3Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 55, 1)
)
sdpBindL2tpv3Entry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindL2tpv3Entry.setStatus("current")


class _SdpBindL2tpv3IngressCookie_Type(OctetString):
    """Custom type sdpBindL2tpv3IngressCookie based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SdpBindL2tpv3IngressCookie_Type.__name__ = "OctetString"
_SdpBindL2tpv3IngressCookie_Object = MibTableColumn
sdpBindL2tpv3IngressCookie = _SdpBindL2tpv3IngressCookie_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 55, 1, 1),
    _SdpBindL2tpv3IngressCookie_Type()
)
sdpBindL2tpv3IngressCookie.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindL2tpv3IngressCookie.setStatus("current")


class _SdpBindL2tpv3EgressCookie_Type(OctetString):
    """Custom type sdpBindL2tpv3EgressCookie based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SdpBindL2tpv3EgressCookie_Type.__name__ = "OctetString"
_SdpBindL2tpv3EgressCookie_Object = MibTableColumn
sdpBindL2tpv3EgressCookie = _SdpBindL2tpv3EgressCookie_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 55, 1, 2),
    _SdpBindL2tpv3EgressCookie_Type()
)
sdpBindL2tpv3EgressCookie.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindL2tpv3EgressCookie.setStatus("current")
_SdpBindL2tpv3SessMismatch_Type = TruthValue
_SdpBindL2tpv3SessMismatch_Object = MibTableColumn
sdpBindL2tpv3SessMismatch = _SdpBindL2tpv3SessMismatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 55, 1, 3),
    _SdpBindL2tpv3SessMismatch_Type()
)
sdpBindL2tpv3SessMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindL2tpv3SessMismatch.setStatus("current")
_SdpBindL2tpv3SessMismatchLstClrd_Type = TimeStamp
_SdpBindL2tpv3SessMismatchLstClrd_Object = MibTableColumn
sdpBindL2tpv3SessMismatchLstClrd = _SdpBindL2tpv3SessMismatchLstClrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 55, 1, 4),
    _SdpBindL2tpv3SessMismatchLstClrd_Type()
)
sdpBindL2tpv3SessMismatchLstClrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindL2tpv3SessMismatchLstClrd.setStatus("current")


class _SdpBindL2tpv3IngressCookie2_Type(OctetString):
    """Custom type sdpBindL2tpv3IngressCookie2 based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SdpBindL2tpv3IngressCookie2_Type.__name__ = "OctetString"
_SdpBindL2tpv3IngressCookie2_Object = MibTableColumn
sdpBindL2tpv3IngressCookie2 = _SdpBindL2tpv3IngressCookie2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 55, 1, 5),
    _SdpBindL2tpv3IngressCookie2_Type()
)
sdpBindL2tpv3IngressCookie2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindL2tpv3IngressCookie2.setStatus("current")
_SdpBindTlsStaticIsidRngTable_Object = MibTable
sdpBindTlsStaticIsidRngTable = _SdpBindTlsStaticIsidRngTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 56)
)
if mibBuilder.loadTexts:
    sdpBindTlsStaticIsidRngTable.setStatus("current")
_SdpBindTlsStaticIsidRngEntry_Object = MibTableRow
sdpBindTlsStaticIsidRngEntry = _SdpBindTlsStaticIsidRngEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 56, 1)
)
sdpBindTlsStaticIsidRngEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindTlsStaticIsidRngId"),
)
if mibBuilder.loadTexts:
    sdpBindTlsStaticIsidRngEntry.setStatus("current")


class _SdpBindTlsStaticIsidRngId_Type(Unsigned32):
    """Custom type sdpBindTlsStaticIsidRngId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_SdpBindTlsStaticIsidRngId_Type.__name__ = "Unsigned32"
_SdpBindTlsStaticIsidRngId_Object = MibTableColumn
sdpBindTlsStaticIsidRngId = _SdpBindTlsStaticIsidRngId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 56, 1, 1),
    _SdpBindTlsStaticIsidRngId_Type()
)
sdpBindTlsStaticIsidRngId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBindTlsStaticIsidRngId.setStatus("current")
_SdpBindTlsStaticIsidRngRowStatus_Type = RowStatus
_SdpBindTlsStaticIsidRngRowStatus_Object = MibTableColumn
sdpBindTlsStaticIsidRngRowStatus = _SdpBindTlsStaticIsidRngRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 56, 1, 2),
    _SdpBindTlsStaticIsidRngRowStatus_Type()
)
sdpBindTlsStaticIsidRngRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindTlsStaticIsidRngRowStatus.setStatus("current")
_SdpBindTlsStaticIsidRngLastChgd_Type = TimeStamp
_SdpBindTlsStaticIsidRngLastChgd_Object = MibTableColumn
sdpBindTlsStaticIsidRngLastChgd = _SdpBindTlsStaticIsidRngLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 56, 1, 3),
    _SdpBindTlsStaticIsidRngLastChgd_Type()
)
sdpBindTlsStaticIsidRngLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStaticIsidRngLastChgd.setStatus("current")


class _SdpBindTlsStaticIsidRngLow_Type(TmnxISID):
    """Custom type sdpBindTlsStaticIsidRngLow based on TmnxISID"""
    defaultValue = 0


_SdpBindTlsStaticIsidRngLow_Type.__name__ = "TmnxISID"
_SdpBindTlsStaticIsidRngLow_Object = MibTableColumn
sdpBindTlsStaticIsidRngLow = _SdpBindTlsStaticIsidRngLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 56, 1, 4),
    _SdpBindTlsStaticIsidRngLow_Type()
)
sdpBindTlsStaticIsidRngLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindTlsStaticIsidRngLow.setStatus("current")


class _SdpBindTlsStaticIsidRngHigh_Type(TmnxISID):
    """Custom type sdpBindTlsStaticIsidRngHigh based on TmnxISID"""
    defaultValue = 0


_SdpBindTlsStaticIsidRngHigh_Type.__name__ = "TmnxISID"
_SdpBindTlsStaticIsidRngHigh_Object = MibTableColumn
sdpBindTlsStaticIsidRngHigh = _SdpBindTlsStaticIsidRngHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 56, 1, 5),
    _SdpBindTlsStaticIsidRngHigh_Type()
)
sdpBindTlsStaticIsidRngHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindTlsStaticIsidRngHigh.setStatus("current")
_SdpBindDhcp6InfoTable_Object = MibTable
sdpBindDhcp6InfoTable = _SdpBindDhcp6InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 57)
)
if mibBuilder.loadTexts:
    sdpBindDhcp6InfoTable.setStatus("current")
_SdpBindDhcp6InfoEntry_Object = MibTableRow
sdpBindDhcp6InfoEntry = _SdpBindDhcp6InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 57, 1)
)
if mibBuilder.loadTexts:
    sdpBindDhcp6InfoEntry.setStatus("current")


class _SdpBindDhcp6Description_Type(ServObjDesc):
    """Custom type sdpBindDhcp6Description based on ServObjDesc"""
    defaultHexValue = ""


_SdpBindDhcp6Description_Type.__name__ = "ServObjDesc"
_SdpBindDhcp6Description_Object = MibTableColumn
sdpBindDhcp6Description = _SdpBindDhcp6Description_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 57, 1, 1),
    _SdpBindDhcp6Description_Type()
)
sdpBindDhcp6Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindDhcp6Description.setStatus("current")


class _SdpBindDhcp6Snoop_Type(TmnxEnabledDisabled):
    """Custom type sdpBindDhcp6Snoop based on TmnxEnabledDisabled"""
    defaultValue = 2


_SdpBindDhcp6Snoop_Type.__name__ = "TmnxEnabledDisabled"
_SdpBindDhcp6Snoop_Object = MibTableColumn
sdpBindDhcp6Snoop = _SdpBindDhcp6Snoop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 57, 1, 2),
    _SdpBindDhcp6Snoop_Type()
)
sdpBindDhcp6Snoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindDhcp6Snoop.setStatus("current")
_SdpBindTlsStaticIsidTable_Object = MibTable
sdpBindTlsStaticIsidTable = _SdpBindTlsStaticIsidTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 58)
)
if mibBuilder.loadTexts:
    sdpBindTlsStaticIsidTable.setStatus("current")
_SdpBindTlsStaticIsidEntry_Object = MibTableRow
sdpBindTlsStaticIsidEntry = _SdpBindTlsStaticIsidEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 58, 1)
)
sdpBindTlsStaticIsidEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindTlsStaticIsid"),
)
if mibBuilder.loadTexts:
    sdpBindTlsStaticIsidEntry.setStatus("current")
_SdpBindTlsStaticIsid_Type = TmnxISID
_SdpBindTlsStaticIsid_Object = MibTableColumn
sdpBindTlsStaticIsid = _SdpBindTlsStaticIsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 58, 1, 1),
    _SdpBindTlsStaticIsid_Type()
)
sdpBindTlsStaticIsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBindTlsStaticIsid.setStatus("current")
_SdpBindTlsStaticIsidStatus_Type = TmnxIsidMFibStatus
_SdpBindTlsStaticIsidStatus_Object = MibTableColumn
sdpBindTlsStaticIsidStatus = _SdpBindTlsStaticIsidStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 58, 1, 2),
    _SdpBindTlsStaticIsidStatus_Type()
)
sdpBindTlsStaticIsidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStaticIsidStatus.setStatus("current")
_SdpBindEthLoopbackTable_Object = MibTable
sdpBindEthLoopbackTable = _SdpBindEthLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 59)
)
if mibBuilder.loadTexts:
    sdpBindEthLoopbackTable.setStatus("current")
_SdpBindEthLoopbackEntry_Object = MibTableRow
sdpBindEthLoopbackEntry = _SdpBindEthLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 59, 1)
)
sdpBindEthLoopbackEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindEthLoopbackEntry.setStatus("current")
_SdpBindEthLoopbackRowStatus_Type = RowStatus
_SdpBindEthLoopbackRowStatus_Object = MibTableColumn
sdpBindEthLoopbackRowStatus = _SdpBindEthLoopbackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 59, 1, 1),
    _SdpBindEthLoopbackRowStatus_Type()
)
sdpBindEthLoopbackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEthLoopbackRowStatus.setStatus("current")


class _SdpBindEthLoopbackMode_Type(Integer32):
    """Custom type sdpBindEthLoopbackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )


_SdpBindEthLoopbackMode_Type.__name__ = "Integer32"
_SdpBindEthLoopbackMode_Object = MibTableColumn
sdpBindEthLoopbackMode = _SdpBindEthLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 59, 1, 2),
    _SdpBindEthLoopbackMode_Type()
)
sdpBindEthLoopbackMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEthLoopbackMode.setStatus("current")


class _SdpBindEthLoopbackMacSwap_Type(TmnxEnabledDisabled):
    """Custom type sdpBindEthLoopbackMacSwap based on TmnxEnabledDisabled"""
    defaultValue = 2


_SdpBindEthLoopbackMacSwap_Type.__name__ = "TmnxEnabledDisabled"
_SdpBindEthLoopbackMacSwap_Object = MibTableColumn
sdpBindEthLoopbackMacSwap = _SdpBindEthLoopbackMacSwap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 59, 1, 3),
    _SdpBindEthLoopbackMacSwap_Type()
)
sdpBindEthLoopbackMacSwap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEthLoopbackMacSwap.setStatus("current")


class _SdpBindEthLoopbackMacSwapAddr_Type(MacAddress):
    """Custom type sdpBindEthLoopbackMacSwapAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_SdpBindEthLoopbackMacSwapAddr_Type.__name__ = "MacAddress"
_SdpBindEthLoopbackMacSwapAddr_Object = MibTableColumn
sdpBindEthLoopbackMacSwapAddr = _SdpBindEthLoopbackMacSwapAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 59, 1, 4),
    _SdpBindEthLoopbackMacSwapAddr_Type()
)
sdpBindEthLoopbackMacSwapAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEthLoopbackMacSwapAddr.setStatus("current")


class _SdpBindEthLoopbackMacSwapAddrAll_Type(TruthValue):
    """Custom type sdpBindEthLoopbackMacSwapAddrAll based on TruthValue"""
    defaultValue = 2


_SdpBindEthLoopbackMacSwapAddrAll_Type.__name__ = "TruthValue"
_SdpBindEthLoopbackMacSwapAddrAll_Object = MibTableColumn
sdpBindEthLoopbackMacSwapAddrAll = _SdpBindEthLoopbackMacSwapAddrAll_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 59, 1, 5),
    _SdpBindEthLoopbackMacSwapAddrAll_Type()
)
sdpBindEthLoopbackMacSwapAddrAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEthLoopbackMacSwapAddrAll.setStatus("current")
_SdpBindTlsFdbMacStatsTable_Object = MibTable
sdpBindTlsFdbMacStatsTable = _SdpBindTlsFdbMacStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 60)
)
if mibBuilder.loadTexts:
    sdpBindTlsFdbMacStatsTable.setStatus("current")
_SdpBindTlsFdbMacStatsEntry_Object = MibTableRow
sdpBindTlsFdbMacStatsEntry = _SdpBindTlsFdbMacStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 60, 1)
)
sdpBindTlsFdbMacStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "TIMETRA-SERV-MIB", "tlsFdbType"),
)
if mibBuilder.loadTexts:
    sdpBindTlsFdbMacStatsEntry.setStatus("current")
_SdpBindTlsFdbMacStatsNumEntries_Type = Unsigned32
_SdpBindTlsFdbMacStatsNumEntries_Object = MibTableColumn
sdpBindTlsFdbMacStatsNumEntries = _SdpBindTlsFdbMacStatsNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 60, 1, 1),
    _SdpBindTlsFdbMacStatsNumEntries_Type()
)
sdpBindTlsFdbMacStatsNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsFdbMacStatsNumEntries.setStatus("current")
_SdpBindPwLoopbackTable_Object = MibTable
sdpBindPwLoopbackTable = _SdpBindPwLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 61)
)
if mibBuilder.loadTexts:
    sdpBindPwLoopbackTable.setStatus("current")
_SdpBindPwLoopbackEntry_Object = MibTableRow
sdpBindPwLoopbackEntry = _SdpBindPwLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 61, 1)
)
sdpBindPwLoopbackEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindPwLoopbackEntry.setStatus("current")
_SdpBindPwLoopbackRowStatus_Type = RowStatus
_SdpBindPwLoopbackRowStatus_Object = MibTableColumn
sdpBindPwLoopbackRowStatus = _SdpBindPwLoopbackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 61, 1, 1),
    _SdpBindPwLoopbackRowStatus_Type()
)
sdpBindPwLoopbackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindPwLoopbackRowStatus.setStatus("current")
_SdpBindPwAdminLockTable_Object = MibTable
sdpBindPwAdminLockTable = _SdpBindPwAdminLockTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 62)
)
if mibBuilder.loadTexts:
    sdpBindPwAdminLockTable.setStatus("current")
_SdpBindPwAdminLockEntry_Object = MibTableRow
sdpBindPwAdminLockEntry = _SdpBindPwAdminLockEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 62, 1)
)
sdpBindPwAdminLockEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindPwAdminLockEntry.setStatus("current")
_SdpBindPwAdminLockRowStatus_Type = RowStatus
_SdpBindPwAdminLockRowStatus_Object = MibTableColumn
sdpBindPwAdminLockRowStatus = _SdpBindPwAdminLockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 62, 1, 1),
    _SdpBindPwAdminLockRowStatus_Type()
)
sdpBindPwAdminLockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindPwAdminLockRowStatus.setStatus("current")


class _SdpBindPwAdminLockTestSvc_Type(TmnxServId):
    """Custom type sdpBindPwAdminLockTestSvc based on TmnxServId"""
    defaultValue = 0


_SdpBindPwAdminLockTestSvc_Type.__name__ = "TmnxServId"
_SdpBindPwAdminLockTestSvc_Object = MibTableColumn
sdpBindPwAdminLockTestSvc = _SdpBindPwAdminLockTestSvc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 62, 1, 2),
    _SdpBindPwAdminLockTestSvc_Type()
)
sdpBindPwAdminLockTestSvc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindPwAdminLockTestSvc.setStatus("current")
_PwTemplateAugTableLastChgd_Type = TimeStamp
_PwTemplateAugTableLastChgd_Object = MibScalar
pwTemplateAugTableLastChgd = _PwTemplateAugTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 63),
    _PwTemplateAugTableLastChgd_Type()
)
pwTemplateAugTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTemplateAugTableLastChgd.setStatus("current")
_PwTemplateAugTable_Object = MibTable
pwTemplateAugTable = _PwTemplateAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 64)
)
if mibBuilder.loadTexts:
    pwTemplateAugTable.setStatus("current")
_PwTemplateAugEntry_Object = MibTableRow
pwTemplateAugEntry = _PwTemplateAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 64, 1)
)
if mibBuilder.loadTexts:
    pwTemplateAugEntry.setStatus("current")
_PwTemplateAugLastChgd_Type = TimeStamp
_PwTemplateAugLastChgd_Object = MibTableColumn
pwTemplateAugLastChgd = _PwTemplateAugLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 64, 1, 1),
    _PwTemplateAugLastChgd_Type()
)
pwTemplateAugLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTemplateAugLastChgd.setStatus("current")


class _PwTemplateAugStpAutoEdge_Type(TmnxEnabledDisabled):
    """Custom type pwTemplateAugStpAutoEdge based on TmnxEnabledDisabled"""
    defaultValue = 1


_PwTemplateAugStpAutoEdge_Type.__name__ = "TmnxEnabledDisabled"
_PwTemplateAugStpAutoEdge_Object = MibTableColumn
pwTemplateAugStpAutoEdge = _PwTemplateAugStpAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 64, 1, 2),
    _PwTemplateAugStpAutoEdge_Type()
)
pwTemplateAugStpAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTemplateAugStpAutoEdge.setStatus("current")


class _PwTemplateAugStpRapidStart_Type(TmnxEnabledDisabled):
    """Custom type pwTemplateAugStpRapidStart based on TmnxEnabledDisabled"""
    defaultValue = 2


_PwTemplateAugStpRapidStart_Type.__name__ = "TmnxEnabledDisabled"
_PwTemplateAugStpRapidStart_Object = MibTableColumn
pwTemplateAugStpRapidStart = _PwTemplateAugStpRapidStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 64, 1, 3),
    _PwTemplateAugStpRapidStart_Type()
)
pwTemplateAugStpRapidStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTemplateAugStpRapidStart.setStatus("current")


class _PwTemplateAugStpAdminPtToPt_Type(Integer32):
    """Custom type pwTemplateAugStpAdminPtToPt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("forceTrue", 0),
          ("forceFalse", 1))
    )


_PwTemplateAugStpAdminPtToPt_Type.__name__ = "Integer32"
_PwTemplateAugStpAdminPtToPt_Object = MibTableColumn
pwTemplateAugStpAdminPtToPt = _PwTemplateAugStpAdminPtToPt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 64, 1, 4),
    _PwTemplateAugStpAdminPtToPt_Type()
)
pwTemplateAugStpAdminPtToPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTemplateAugStpAdminPtToPt.setStatus("current")


class _PwTemplateAugStpPathCost_Type(Integer32):
    """Custom type pwTemplateAugStpPathCost based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_PwTemplateAugStpPathCost_Type.__name__ = "Integer32"
_PwTemplateAugStpPathCost_Object = MibTableColumn
pwTemplateAugStpPathCost = _PwTemplateAugStpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 64, 1, 5),
    _PwTemplateAugStpPathCost_Type()
)
pwTemplateAugStpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTemplateAugStpPathCost.setStatus("current")


class _PwTemplateAugStpPriority_Type(Integer32):
    """Custom type pwTemplateAugStpPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PwTemplateAugStpPriority_Type.__name__ = "Integer32"
_PwTemplateAugStpPriority_Object = MibTableColumn
pwTemplateAugStpPriority = _PwTemplateAugStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 64, 1, 6),
    _PwTemplateAugStpPriority_Type()
)
pwTemplateAugStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTemplateAugStpPriority.setStatus("current")


class _PwTemplateAugStpRootGuard_Type(TruthValue):
    """Custom type pwTemplateAugStpRootGuard based on TruthValue"""
    defaultValue = 2


_PwTemplateAugStpRootGuard_Type.__name__ = "TruthValue"
_PwTemplateAugStpRootGuard_Object = MibTableColumn
pwTemplateAugStpRootGuard = _PwTemplateAugStpRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 64, 1, 7),
    _PwTemplateAugStpRootGuard_Type()
)
pwTemplateAugStpRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTemplateAugStpRootGuard.setStatus("current")


class _PwTemplateAugStpAdminStatus_Type(TmnxEnabledDisabledAdminState):
    """Custom type pwTemplateAugStpAdminStatus based on TmnxEnabledDisabledAdminState"""
    defaultValue = 1


_PwTemplateAugStpAdminStatus_Type.__name__ = "TmnxEnabledDisabledAdminState"
_PwTemplateAugStpAdminStatus_Object = MibTableColumn
pwTemplateAugStpAdminStatus = _PwTemplateAugStpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 64, 1, 8),
    _PwTemplateAugStpAdminStatus_Type()
)
pwTemplateAugStpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTemplateAugStpAdminStatus.setStatus("current")


class _PwTemplateAugL2ptTermination_Type(TmnxEnabledDisabled):
    """Custom type pwTemplateAugL2ptTermination based on TmnxEnabledDisabled"""
    defaultValue = 2


_PwTemplateAugL2ptTermination_Type.__name__ = "TmnxEnabledDisabled"
_PwTemplateAugL2ptTermination_Object = MibTableColumn
pwTemplateAugL2ptTermination = _PwTemplateAugL2ptTermination_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 64, 1, 9),
    _PwTemplateAugL2ptTermination_Type()
)
pwTemplateAugL2ptTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTemplateAugL2ptTermination.setStatus("current")


class _PwTemplateAugL2ptProtocols_Type(L2ptProtocols):
    """Custom type pwTemplateAugL2ptProtocols based on L2ptProtocols"""
    defaultBinValue = "0"


_PwTemplateAugL2ptProtocols_Type.__name__ = "L2ptProtocols"
_PwTemplateAugL2ptProtocols_Object = MibTableColumn
pwTemplateAugL2ptProtocols = _PwTemplateAugL2ptProtocols_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 64, 1, 10),
    _PwTemplateAugL2ptProtocols_Type()
)
pwTemplateAugL2ptProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTemplateAugL2ptProtocols.setStatus("current")


class _PwTemplateAugGreAllowFrag_Type(TruthValue):
    """Custom type pwTemplateAugGreAllowFrag based on TruthValue"""
    defaultValue = 2


_PwTemplateAugGreAllowFrag_Type.__name__ = "TruthValue"
_PwTemplateAugGreAllowFrag_Object = MibTableColumn
pwTemplateAugGreAllowFrag = _PwTemplateAugGreAllowFrag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 64, 1, 11),
    _PwTemplateAugGreAllowFrag_Type()
)
pwTemplateAugGreAllowFrag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTemplateAugGreAllowFrag.setStatus("current")


class _PwTemplateAugAluNgeKeyGroupIn_Type(AluNgeKeygroupIdOrZero):
    """Custom type pwTemplateAugAluNgeKeyGroupIn based on AluNgeKeygroupIdOrZero"""
    defaultValue = 0


_PwTemplateAugAluNgeKeyGroupIn_Type.__name__ = "AluNgeKeygroupIdOrZero"
_PwTemplateAugAluNgeKeyGroupIn_Object = MibTableColumn
pwTemplateAugAluNgeKeyGroupIn = _PwTemplateAugAluNgeKeyGroupIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 64, 1, 12),
    _PwTemplateAugAluNgeKeyGroupIn_Type()
)
pwTemplateAugAluNgeKeyGroupIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTemplateAugAluNgeKeyGroupIn.setStatus("current")


class _PwTemplateAugAluNgeKeyGroupOut_Type(AluNgeKeygroupIdOrZero):
    """Custom type pwTemplateAugAluNgeKeyGroupOut based on AluNgeKeygroupIdOrZero"""
    defaultValue = 0


_PwTemplateAugAluNgeKeyGroupOut_Type.__name__ = "AluNgeKeygroupIdOrZero"
_PwTemplateAugAluNgeKeyGroupOut_Object = MibTableColumn
pwTemplateAugAluNgeKeyGroupOut = _PwTemplateAugAluNgeKeyGroupOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 64, 1, 13),
    _PwTemplateAugAluNgeKeyGroupOut_Type()
)
pwTemplateAugAluNgeKeyGroupOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTemplateAugAluNgeKeyGroupOut.setStatus("current")


class _PwTemplateAugAtLnMacPrtExcList_Type(TNamedItemOrEmpty):
    """Custom type pwTemplateAugAtLnMacPrtExcList based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_PwTemplateAugAtLnMacPrtExcList_Type.__name__ = "TNamedItemOrEmpty"
_PwTemplateAugAtLnMacPrtExcList_Object = MibTableColumn
pwTemplateAugAtLnMacPrtExcList = _PwTemplateAugAtLnMacPrtExcList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 64, 1, 14),
    _PwTemplateAugAtLnMacPrtExcList_Type()
)
pwTemplateAugAtLnMacPrtExcList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTemplateAugAtLnMacPrtExcList.setStatus("current")
_SdpSegRouteTableLastChgd_Type = TimeStamp
_SdpSegRouteTableLastChgd_Object = MibScalar
sdpSegRouteTableLastChgd = _SdpSegRouteTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 65),
    _SdpSegRouteTableLastChgd_Type()
)
sdpSegRouteTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpSegRouteTableLastChgd.setStatus("current")
_SdpSegRouteTable_Object = MibTable
sdpSegRouteTable = _SdpSegRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 66)
)
if mibBuilder.loadTexts:
    sdpSegRouteTable.setStatus("current")
_SdpSegRouteEntry_Object = MibTableRow
sdpSegRouteEntry = _SdpSegRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 66, 1)
)
sdpSegRouteEntry.setIndexNames(
    (0, "TIMETRA-SDP-MIB", "sdpId"),
)
if mibBuilder.loadTexts:
    sdpSegRouteEntry.setStatus("current")


class _SdpSegRouteIsIs_Type(TmnxEnabledDisabled):
    """Custom type sdpSegRouteIsIs based on TmnxEnabledDisabled"""
    defaultValue = 2


_SdpSegRouteIsIs_Type.__name__ = "TmnxEnabledDisabled"
_SdpSegRouteIsIs_Object = MibTableColumn
sdpSegRouteIsIs = _SdpSegRouteIsIs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 66, 1, 1),
    _SdpSegRouteIsIs_Type()
)
sdpSegRouteIsIs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpSegRouteIsIs.setStatus("current")
_SdpSegRouteIsIsOperInstId_Type = Integer32
_SdpSegRouteIsIsOperInstId_Object = MibTableColumn
sdpSegRouteIsIsOperInstId = _SdpSegRouteIsIsOperInstId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 66, 1, 3),
    _SdpSegRouteIsIsOperInstId_Type()
)
sdpSegRouteIsIsOperInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpSegRouteIsIsOperInstId.setStatus("current")
_SdpSegRouteIsIsLspId_Type = Unsigned32
_SdpSegRouteIsIsLspId_Object = MibTableColumn
sdpSegRouteIsIsLspId = _SdpSegRouteIsIsLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 66, 1, 4),
    _SdpSegRouteIsIsLspId_Type()
)
sdpSegRouteIsIsLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpSegRouteIsIsLspId.setStatus("current")


class _SdpSegRouteOspf_Type(TmnxEnabledDisabled):
    """Custom type sdpSegRouteOspf based on TmnxEnabledDisabled"""
    defaultValue = 2


_SdpSegRouteOspf_Type.__name__ = "TmnxEnabledDisabled"
_SdpSegRouteOspf_Object = MibTableColumn
sdpSegRouteOspf = _SdpSegRouteOspf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 66, 1, 10),
    _SdpSegRouteOspf_Type()
)
sdpSegRouteOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpSegRouteOspf.setStatus("current")
_SdpSegRouteOspfOperInstId_Type = Integer32
_SdpSegRouteOspfOperInstId_Object = MibTableColumn
sdpSegRouteOspfOperInstId = _SdpSegRouteOspfOperInstId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 66, 1, 12),
    _SdpSegRouteOspfOperInstId_Type()
)
sdpSegRouteOspfOperInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpSegRouteOspfOperInstId.setStatus("current")
_SdpSegRouteOspfLspId_Type = Unsigned32
_SdpSegRouteOspfLspId_Object = MibTableColumn
sdpSegRouteOspfLspId = _SdpSegRouteOspfLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 66, 1, 13),
    _SdpSegRouteOspfLspId_Type()
)
sdpSegRouteOspfLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpSegRouteOspfLspId.setStatus("current")
_SdpSegRouteTeOperInstId_Type = Integer32
_SdpSegRouteTeOperInstId_Object = MibTableColumn
sdpSegRouteTeOperInstId = _SdpSegRouteTeOperInstId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 66, 1, 14),
    _SdpSegRouteTeOperInstId_Type()
)
sdpSegRouteTeOperInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpSegRouteTeOperInstId.setStatus("current")
_SdpEvpnMHEthSegTable_Object = MibTable
sdpEvpnMHEthSegTable = _SdpEvpnMHEthSegTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 67)
)
if mibBuilder.loadTexts:
    sdpEvpnMHEthSegTable.setStatus("current")
_SdpEvpnMHEthSegEntry_Object = MibTableRow
sdpEvpnMHEthSegEntry = _SdpEvpnMHEthSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 67, 1)
)
sdpEvpnMHEthSegEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpEvpnMHEthSegEntry.setStatus("current")
_SdpEvpnMHEthSegName_Type = TNamedItemOrEmpty
_SdpEvpnMHEthSegName_Object = MibTableColumn
sdpEvpnMHEthSegName = _SdpEvpnMHEthSegName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 67, 1, 1),
    _SdpEvpnMHEthSegName_Type()
)
sdpEvpnMHEthSegName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpEvpnMHEthSegName.setStatus("current")
_SdpEvpnMHEthSegStatus_Type = TmnxEvpnMHEthSegStatus
_SdpEvpnMHEthSegStatus_Object = MibTableColumn
sdpEvpnMHEthSegStatus = _SdpEvpnMHEthSegStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 67, 1, 2),
    _SdpEvpnMHEthSegStatus_Type()
)
sdpEvpnMHEthSegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpEvpnMHEthSegStatus.setStatus("current")
_SdpBindExtTableLastChanged_Type = TimeStamp
_SdpBindExtTableLastChanged_Object = MibScalar
sdpBindExtTableLastChanged = _SdpBindExtTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 68),
    _SdpBindExtTableLastChanged_Type()
)
sdpBindExtTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindExtTableLastChanged.setStatus("current")
_SdpBindExtTable_Object = MibTable
sdpBindExtTable = _SdpBindExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 69)
)
if mibBuilder.loadTexts:
    sdpBindExtTable.setStatus("current")
_SdpBindExtEntry_Object = MibTableRow
sdpBindExtEntry = _SdpBindExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 69, 1)
)
if mibBuilder.loadTexts:
    sdpBindExtEntry.setStatus("current")


class _SdpBindExtEntropyLabel_Type(TruthValue):
    """Custom type sdpBindExtEntropyLabel based on TruthValue"""
    defaultValue = 2


_SdpBindExtEntropyLabel_Type.__name__ = "TruthValue"
_SdpBindExtEntropyLabel_Object = MibTableColumn
sdpBindExtEntropyLabel = _SdpBindExtEntropyLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 69, 1, 1),
    _SdpBindExtEntropyLabel_Type()
)
sdpBindExtEntropyLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindExtEntropyLabel.setStatus("current")
_SdpBindExtLastMgmtChange_Type = TimeStamp
_SdpBindExtLastMgmtChange_Object = MibTableColumn
sdpBindExtLastMgmtChange = _SdpBindExtLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 69, 1, 2),
    _SdpBindExtLastMgmtChange_Type()
)
sdpBindExtLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindExtLastMgmtChange.setStatus("current")


class _SdpBindExtBfdFailAction_Type(Integer32):
    """Custom type sdpBindExtBfdFailAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("down", 1))
    )


_SdpBindExtBfdFailAction_Type.__name__ = "Integer32"
_SdpBindExtBfdFailAction_Object = MibTableColumn
sdpBindExtBfdFailAction = _SdpBindExtBfdFailAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 69, 1, 3),
    _SdpBindExtBfdFailAction_Type()
)
sdpBindExtBfdFailAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindExtBfdFailAction.setStatus("current")
_SdpBindExtBfdSessStatOperState_Type = TmnxBfdSessOperState
_SdpBindExtBfdSessStatOperState_Object = MibTableColumn
sdpBindExtBfdSessStatOperState = _SdpBindExtBfdSessStatOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 69, 1, 4),
    _SdpBindExtBfdSessStatOperState_Type()
)
sdpBindExtBfdSessStatOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindExtBfdSessStatOperState.setStatus("current")


class _SdpBindExtBfdWaitForUpTimer_Type(Unsigned32):
    """Custom type sdpBindExtBfdWaitForUpTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SdpBindExtBfdWaitForUpTimer_Type.__name__ = "Unsigned32"
_SdpBindExtBfdWaitForUpTimer_Object = MibTableColumn
sdpBindExtBfdWaitForUpTimer = _SdpBindExtBfdWaitForUpTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 69, 1, 5),
    _SdpBindExtBfdWaitForUpTimer_Type()
)
sdpBindExtBfdWaitForUpTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindExtBfdWaitForUpTimer.setStatus("current")
_SdpBindExtBfdUpTimeRemain_Type = Integer32
_SdpBindExtBfdUpTimeRemain_Object = MibTableColumn
sdpBindExtBfdUpTimeRemain = _SdpBindExtBfdUpTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 69, 1, 6),
    _SdpBindExtBfdUpTimeRemain_Type()
)
sdpBindExtBfdUpTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindExtBfdUpTimeRemain.setStatus("current")
_SdpSegRouteTeLspTableLastChgd_Type = TimeStamp
_SdpSegRouteTeLspTableLastChgd_Object = MibScalar
sdpSegRouteTeLspTableLastChgd = _SdpSegRouteTeLspTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 70),
    _SdpSegRouteTeLspTableLastChgd_Type()
)
sdpSegRouteTeLspTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpSegRouteTeLspTableLastChgd.setStatus("current")
_SdpSegRouteTeLspTable_Object = MibTable
sdpSegRouteTeLspTable = _SdpSegRouteTeLspTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 71)
)
if mibBuilder.loadTexts:
    sdpSegRouteTeLspTable.setStatus("current")
_SdpSegRouteTeLspEntry_Object = MibTableRow
sdpSegRouteTeLspEntry = _SdpSegRouteTeLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 71, 1)
)
sdpSegRouteTeLspEntry.setIndexNames(
    (0, "TIMETRA-SDP-MIB", "sdpId"),
    (0, "TIMETRA-SDP-MIB", "sdpSegRouteTeLspId"),
)
if mibBuilder.loadTexts:
    sdpSegRouteTeLspEntry.setStatus("current")
_SdpSegRouteTeLspId_Type = TmnxVRtrMplsLspID
_SdpSegRouteTeLspId_Object = MibTableColumn
sdpSegRouteTeLspId = _SdpSegRouteTeLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 71, 1, 1),
    _SdpSegRouteTeLspId_Type()
)
sdpSegRouteTeLspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpSegRouteTeLspId.setStatus("current")
_SdpSegRouteTeLspRowStatus_Type = RowStatus
_SdpSegRouteTeLspRowStatus_Object = MibTableColumn
sdpSegRouteTeLspRowStatus = _SdpSegRouteTeLspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 71, 1, 2),
    _SdpSegRouteTeLspRowStatus_Type()
)
sdpSegRouteTeLspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpSegRouteTeLspRowStatus.setStatus("current")
_SdpSegRouteTeLspLastChanged_Type = TimeStamp
_SdpSegRouteTeLspLastChanged_Object = MibTableColumn
sdpSegRouteTeLspLastChanged = _SdpSegRouteTeLspLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 71, 1, 3),
    _SdpSegRouteTeLspLastChanged_Type()
)
sdpSegRouteTeLspLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpSegRouteTeLspLastChanged.setStatus("current")
_SdpMplsLspTableLastChgd_Type = TimeStamp
_SdpMplsLspTableLastChgd_Object = MibScalar
sdpMplsLspTableLastChgd = _SdpMplsLspTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 72),
    _SdpMplsLspTableLastChgd_Type()
)
sdpMplsLspTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpMplsLspTableLastChgd.setStatus("current")
_SdpMplsLspTable_Object = MibTable
sdpMplsLspTable = _SdpMplsLspTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 73)
)
if mibBuilder.loadTexts:
    sdpMplsLspTable.setStatus("current")
_SdpMplsLspEntry_Object = MibTableRow
sdpMplsLspEntry = _SdpMplsLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 73, 1)
)
sdpMplsLspEntry.setIndexNames(
    (0, "TIMETRA-SDP-MIB", "sdpId"),
    (0, "TIMETRA-SDP-MIB", "sdpMplsLspId"),
)
if mibBuilder.loadTexts:
    sdpMplsLspEntry.setStatus("current")
_SdpMplsLspId_Type = TmnxVRtrMplsLspIDNoZero
_SdpMplsLspId_Object = MibTableColumn
sdpMplsLspId = _SdpMplsLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 73, 1, 1),
    _SdpMplsLspId_Type()
)
sdpMplsLspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpMplsLspId.setStatus("current")
_SdpMplsLspRowStatus_Type = RowStatus
_SdpMplsLspRowStatus_Object = MibTableColumn
sdpMplsLspRowStatus = _SdpMplsLspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 73, 1, 2),
    _SdpMplsLspRowStatus_Type()
)
sdpMplsLspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpMplsLspRowStatus.setStatus("current")
_SdpMplsLspLastChanged_Type = TimeStamp
_SdpMplsLspLastChanged_Object = MibTableColumn
sdpMplsLspLastChanged = _SdpMplsLspLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 73, 1, 3),
    _SdpMplsLspLastChanged_Type()
)
sdpMplsLspLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpMplsLspLastChanged.setStatus("current")
_SdpBindExt2TableLastChgd_Type = TimeStamp
_SdpBindExt2TableLastChgd_Object = MibScalar
sdpBindExt2TableLastChgd = _SdpBindExt2TableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 74),
    _SdpBindExt2TableLastChgd_Type()
)
sdpBindExt2TableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindExt2TableLastChgd.setStatus("current")
_SdpBindExt2Table_Object = MibTable
sdpBindExt2Table = _SdpBindExt2Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 75)
)
if mibBuilder.loadTexts:
    sdpBindExt2Table.setStatus("current")
_SdpBindExt2Entry_Object = MibTableRow
sdpBindExt2Entry = _SdpBindExt2Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 75, 1)
)
sdpBindExt2Entry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindExt2Entry.setStatus("current")
_SdpBindExt2LastMgmtChange_Type = TimeStamp
_SdpBindExt2LastMgmtChange_Object = MibTableColumn
sdpBindExt2LastMgmtChange = _SdpBindExt2LastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 75, 1, 1),
    _SdpBindExt2LastMgmtChange_Type()
)
sdpBindExt2LastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindExt2LastMgmtChange.setStatus("current")


class _SdpBindExt2AdvSvcMtu_Type(Integer32):
    """Custom type sdpBindExt2AdvSvcMtu based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 9782),
    )


_SdpBindExt2AdvSvcMtu_Type.__name__ = "Integer32"
_SdpBindExt2AdvSvcMtu_Object = MibTableColumn
sdpBindExt2AdvSvcMtu = _SdpBindExt2AdvSvcMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 75, 1, 2),
    _SdpBindExt2AdvSvcMtu_Type()
)
sdpBindExt2AdvSvcMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindExt2AdvSvcMtu.setStatus("current")
_SdpBindTableLastChanged_Type = TimeStamp
_SdpBindTableLastChanged_Object = MibScalar
sdpBindTableLastChanged = _SdpBindTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 76),
    _SdpBindTableLastChanged_Type()
)
sdpBindTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTableLastChanged.setStatus("current")
_SdpBindTlsTableLastChanged_Type = TimeStamp
_SdpBindTlsTableLastChanged_Object = MibScalar
sdpBindTlsTableLastChanged = _SdpBindTlsTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 77),
    _SdpBindTlsTableLastChanged_Type()
)
sdpBindTlsTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsTableLastChanged.setStatus("current")
_TmnxSdpNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxSdpNotifyObjs = _TmnxSdpNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 100)
)
_SdpNotifySdpId_Type = SdpId
_SdpNotifySdpId_Object = MibScalar
sdpNotifySdpId = _SdpNotifySdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 100, 1),
    _SdpNotifySdpId_Type()
)
sdpNotifySdpId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sdpNotifySdpId.setStatus("current")
_DynamicSdpStatus_Type = ConfigStatus
_DynamicSdpStatus_Object = MibScalar
dynamicSdpStatus = _DynamicSdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 100, 2),
    _DynamicSdpStatus_Type()
)
dynamicSdpStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dynamicSdpStatus.setStatus("current")
_DynamicSdpOrigin_Type = TmnxCreateOrigin
_DynamicSdpOrigin_Object = MibScalar
dynamicSdpOrigin = _DynamicSdpOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 100, 3),
    _DynamicSdpOrigin_Type()
)
dynamicSdpOrigin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dynamicSdpOrigin.setStatus("current")
_DynamicSdpCreationError_Type = DisplayString
_DynamicSdpCreationError_Object = MibScalar
dynamicSdpCreationError = _DynamicSdpCreationError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 100, 4),
    _DynamicSdpCreationError_Type()
)
dynamicSdpCreationError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dynamicSdpCreationError.setStatus("current")
_DynamicSdpBindCreationError_Type = DisplayString
_DynamicSdpBindCreationError_Object = MibScalar
dynamicSdpBindCreationError = _DynamicSdpBindCreationError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 100, 5),
    _DynamicSdpBindCreationError_Type()
)
dynamicSdpBindCreationError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dynamicSdpBindCreationError.setStatus("current")
_SdpBindNotifyMacAddr_Type = MacAddress
_SdpBindNotifyMacAddr_Object = MibScalar
sdpBindNotifyMacAddr = _SdpBindNotifyMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 100, 6),
    _SdpBindNotifyMacAddr_Type()
)
sdpBindNotifyMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sdpBindNotifyMacAddr.setStatus("current")
_SdpEgIfNetDomainInconsCount_Type = Unsigned32
_SdpEgIfNetDomainInconsCount_Object = MibScalar
sdpEgIfNetDomainInconsCount = _SdpEgIfNetDomainInconsCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 100, 7),
    _SdpEgIfNetDomainInconsCount_Type()
)
sdpEgIfNetDomainInconsCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sdpEgIfNetDomainInconsCount.setStatus("current")
_SdpMSPwPeId_Type = TmnxSpokeSdpIdOrZero
_SdpMSPwPeId_Object = MibScalar
sdpMSPwPeId = _SdpMSPwPeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 100, 8),
    _SdpMSPwPeId_Type()
)
sdpMSPwPeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sdpMSPwPeId.setStatus("current")
_SdpBindIpipeCeIpAddrType_Type = InetAddressType
_SdpBindIpipeCeIpAddrType_Object = MibScalar
sdpBindIpipeCeIpAddrType = _SdpBindIpipeCeIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 100, 9),
    _SdpBindIpipeCeIpAddrType_Type()
)
sdpBindIpipeCeIpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sdpBindIpipeCeIpAddrType.setStatus("current")


class _SdpBindIpipeCeIpAddress_Type(InetAddress):
    """Custom type sdpBindIpipeCeIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SdpBindIpipeCeIpAddress_Type.__name__ = "InetAddress"
_SdpBindIpipeCeIpAddress_Object = MibScalar
sdpBindIpipeCeIpAddress = _SdpBindIpipeCeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 100, 10),
    _SdpBindIpipeCeIpAddress_Type()
)
sdpBindIpipeCeIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sdpBindIpipeCeIpAddress.setStatus("current")
_SdpPbbActvPwWithNonActvCtrlPw_Type = TruthValue
_SdpPbbActvPwWithNonActvCtrlPw_Object = MibScalar
sdpPbbActvPwWithNonActvCtrlPw = _SdpPbbActvPwWithNonActvCtrlPw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 100, 11),
    _SdpPbbActvPwWithNonActvCtrlPw_Type()
)
sdpPbbActvPwWithNonActvCtrlPw.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sdpPbbActvPwWithNonActvCtrlPw.setStatus("current")
_SdpTrapsPrefix_ObjectIdentity = ObjectIdentity
sdpTrapsPrefix = _SdpTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4)
)
_SdpTraps_ObjectIdentity = ObjectIdentity
sdpTraps = _SdpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0)
)
sdpBindDhcpInfoEntry.registerAugmentions(
    ("TIMETRA-SDP-MIB",
     "sdpBindDhcp6InfoEntry")
)
sdpBindDhcp6InfoEntry.setIndexNames(*sdpBindDhcpInfoEntry.getIndexNames())
pwTemplateEntry.registerAugmentions(
    ("TIMETRA-SDP-MIB",
     "pwTemplateAugEntry")
)
pwTemplateAugEntry.setIndexNames(*pwTemplateEntry.getIndexNames())
sdpBindEntry.registerAugmentions(
    ("TIMETRA-SDP-MIB",
     "sdpBindExtEntry")
)
sdpBindExtEntry.setIndexNames(*sdpBindEntry.getIndexNames())

# Managed Objects groups

tmnxSdpV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 100)
)
tmnxSdpV6v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpNumEntries"),
        ("TIMETRA-SDP-MIB", "sdpNextFreeId"),
        ("TIMETRA-SDP-MIB", "sdpId"),
        ("TIMETRA-SDP-MIB", "sdpRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpDelivery"),
        ("TIMETRA-SDP-MIB", "sdpFarEndIpAddress"),
        ("TIMETRA-SDP-MIB", "sdpLspList"),
        ("TIMETRA-SDP-MIB", "sdpDescription"),
        ("TIMETRA-SDP-MIB", "sdpLabelSignaling"),
        ("TIMETRA-SDP-MIB", "sdpAdminStatus"),
        ("TIMETRA-SDP-MIB", "sdpOperStatus"),
        ("TIMETRA-SDP-MIB", "sdpOperPathMtu"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveAdminStatus"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveOperStatus"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveHelloTime"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveMaxDropCount"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveHoldDownTime"),
        ("TIMETRA-SDP-MIB", "sdpLastMgmtChange"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveNumHelloRequestMessages"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveNumHelloResponseMessages"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveNumLateHelloResponseMessages"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveHelloRequestTimeout"),
        ("TIMETRA-SDP-MIB", "sdpLdpEnabled"),
        ("TIMETRA-SDP-MIB", "sdpVlanVcEtype"),
        ("TIMETRA-SDP-MIB", "sdpAdvertisedVllMtuOverride"),
        ("TIMETRA-SDP-MIB", "sdpOperFlags"),
        ("TIMETRA-SDP-MIB", "sdpLastStatusChange"),
        ("TIMETRA-SDP-MIB", "sdpMvplsMgmtService"),
        ("TIMETRA-SDP-MIB", "sdpMvplsMgmtSdpBndId"),
        ("TIMETRA-SDP-MIB", "sdpCollectAcctStats"),
        ("TIMETRA-SDP-MIB", "sdpAccountingPolicyId"),
        ("TIMETRA-SDP-MIB", "sdpClassFwdingEnabled"),
        ("TIMETRA-SDP-MIB", "sdpClassFwdingDefaultLsp"),
        ("TIMETRA-SDP-MIB", "sdpClassFwdingMcLsp"),
        ("TIMETRA-SDP-MIB", "sdpMetric"),
        ("TIMETRA-SDP-MIB", "sdpAutoSdp"),
        ("TIMETRA-SDP-MIB", "sdpSnmpAllowed"),
        ("TIMETRA-SDP-MIB", "sdpPBBEtype"),
        ("TIMETRA-SDP-MIB", "sdpBandwidthBookingFactor"),
        ("TIMETRA-SDP-MIB", "sdpOperBandwidth"),
        ("TIMETRA-SDP-MIB", "sdpAvailableBandwidth"),
        ("TIMETRA-SDP-MIB", "sdpAdminPathMtu"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveHelloMessageLength"))
)
if mibBuilder.loadTexts:
    tmnxSdpV6v0Group.setStatus("obsolete")

tmnxSdpBindV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 101)
)
tmnxSdpBindV6v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SDP-MIB", "sdpBindRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindAdminStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindOperStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindLastMgmtChange"),
        ("TIMETRA-SDP-MIB", "sdpBindType"),
        ("TIMETRA-SDP-MIB", "sdpBindIngressMacFilterId"),
        ("TIMETRA-SDP-MIB", "sdpBindIngressIpFilterId"),
        ("TIMETRA-SDP-MIB", "sdpBindEgressMacFilterId"),
        ("TIMETRA-SDP-MIB", "sdpBindEgressIpFilterId"),
        ("TIMETRA-SDP-MIB", "sdpBindVpnId"),
        ("TIMETRA-SDP-MIB", "sdpBindCustId"),
        ("TIMETRA-SDP-MIB", "sdpBindVcType"),
        ("TIMETRA-SDP-MIB", "sdpBindVlanVcTag"),
        ("TIMETRA-SDP-MIB", "sdpBindSplitHorizonGrp"),
        ("TIMETRA-SDP-MIB", "sdpBindOperFlags"),
        ("TIMETRA-SDP-MIB", "sdpBindLastStatusChange"),
        ("TIMETRA-SDP-MIB", "sdpBindIesIfIndex"),
        ("TIMETRA-SDP-MIB", "sdpBindMacPinning"),
        ("TIMETRA-SDP-MIB", "sdpBindIngressIpv6FilterId"),
        ("TIMETRA-SDP-MIB", "sdpBindEgressIpv6FilterId"),
        ("TIMETRA-SDP-MIB", "sdpBindCollectAcctStats"),
        ("TIMETRA-SDP-MIB", "sdpBindAccountingPolicyId"),
        ("TIMETRA-SDP-MIB", "sdpBindPwPeerStatusBits"),
        ("TIMETRA-SDP-MIB", "sdpBindPeerVccvCvBits"),
        ("TIMETRA-SDP-MIB", "sdpBindPeerVccvCcBits"),
        ("TIMETRA-SDP-MIB", "sdpBindControlWordBit"),
        ("TIMETRA-SDP-MIB", "sdpBindOperControlWord"),
        ("TIMETRA-SDP-MIB", "sdpBindEndPoint"),
        ("TIMETRA-SDP-MIB", "sdpBindEndPointPrecedence"),
        ("TIMETRA-SDP-MIB", "sdpBindIsICB"),
        ("TIMETRA-SDP-MIB", "sdpBindPwFaultInetAddressType"),
        ("TIMETRA-SDP-MIB", "sdpBindClassFwdingOperState"),
        ("TIMETRA-SDP-MIB", "sdpBindForceVlanVcForwarding"),
        ("TIMETRA-SDP-MIB", "sdpBindAdminBandwidth"),
        ("TIMETRA-SDP-MIB", "sdpBindOperBandwidth"),
        ("TIMETRA-SDP-MIB", "sdpBindBaseStatsIngressForwardedPackets"),
        ("TIMETRA-SDP-MIB", "sdpBindBaseStatsIngressDroppedPackets"),
        ("TIMETRA-SDP-MIB", "sdpBindBaseStatsEgressForwardedPackets"),
        ("TIMETRA-SDP-MIB", "sdpBindBaseStatsEgressForwardedOctets"),
        ("TIMETRA-SDP-MIB", "sdpBindBaseStatsCustId"),
        ("TIMETRA-SDP-MIB", "sdpBindBaseStatsIngFwdOctets"),
        ("TIMETRA-SDP-MIB", "sdpBindBaseStatsIngDropOctets"),
        ("TIMETRA-SDP-MIB", "sdpBindAdminIngressLabel"),
        ("TIMETRA-SDP-MIB", "sdpBindAdminEgressLabel"),
        ("TIMETRA-SDP-MIB", "sdpBindOperIngressLabel"),
        ("TIMETRA-SDP-MIB", "sdpBindOperEgressLabel"),
        ("TIMETRA-SDP-MIB", "sdpBindPwFaultInetAddress"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindV6v0Group.setStatus("current")

tmnxSdpBindTlsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 102)
)
tmnxSdpBindTlsV6v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindTlsStpAdminStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpPriority"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpPortNum"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpPathCost"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpRapidStart"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpBpduEncap"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpPortState"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpDesignatedBridge"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpDesignatedPort"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpForwardTransitions"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpInConfigBpdus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpInTcnBpdus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpInBadBpdus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpOutConfigBpdus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpOutTcnBpdus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpOperBpduEncap"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpVpnId"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpCustId"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMacAddressLimit"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsNumMacAddresses"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsNumStaticMacAddresses"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMacLearning"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMacAgeing"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpOperEdge"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpAdminPointToPoint"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpPortRole"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpAutoEdge"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpOperProtocol"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpInRstBpdus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpOutRstBpdus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsLimitMacMove"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsDiscardUnknownSource"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMvplsPruneState"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMvplsMgmtService"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMvplsMgmtSdpBndId"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpException"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptTermination"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsBpduTranslation"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpRootGuard"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpInMstBpdus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpOutMstBpdus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpRxdDesigBridge"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMacMoveNextUpTime"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMacMoveRateExcdLeft"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsLimitMacMoveLevel"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsBpduTransOper"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptProtocols"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsIgnoreStandbySig"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsBlockOnMeshFail"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindTlsV6v0Group.setStatus("current")

tmnxSdpBindMeshV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 103)
)
tmnxSdpBindMeshV6v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindMeshTlsPortState"),
        ("TIMETRA-SDP-MIB", "sdpBindMeshTlsNotInMstRegion"),
        ("TIMETRA-SDP-MIB", "sdpBindMeshTlsHoldDownTimer"),
        ("TIMETRA-SDP-MIB", "sdpBindMeshTlsTransitionState"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindMeshV6v0Group.setStatus("current")

tmnxSdpApipeV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 104)
)
tmnxSdpApipeV6v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindApipeAdminConcatCellCount"),
        ("TIMETRA-SDP-MIB", "sdpBindApipeSigConcatCellCount"),
        ("TIMETRA-SDP-MIB", "sdpBindApipeOperConcatCellCount"),
        ("TIMETRA-SDP-MIB", "sdpBindApipeConcatMaxDelay"),
        ("TIMETRA-SDP-MIB", "sdpBindApipeConcatCellClp"),
        ("TIMETRA-SDP-MIB", "sdpBindApipeConcatCellAal5Fr"))
)
if mibBuilder.loadTexts:
    tmnxSdpApipeV6v0Group.setStatus("current")

tmnxSdpBindDhcpV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 105)
)
tmnxSdpBindDhcpV6v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindDhcpDescription"),
        ("TIMETRA-SDP-MIB", "sdpBindDhcpSnoop"),
        ("TIMETRA-SDP-MIB", "sdpBindDhcpStatsClntSnoopdPckts"),
        ("TIMETRA-SDP-MIB", "sdpBindDhcpStatsSrvrSnoopdPckts"),
        ("TIMETRA-SDP-MIB", "sdpBindDhcpStatsClntForwdPckts"),
        ("TIMETRA-SDP-MIB", "sdpBindDhcpStatsSrvrForwdPckts"),
        ("TIMETRA-SDP-MIB", "sdpBindDhcpStatsClntDropdPckts"),
        ("TIMETRA-SDP-MIB", "sdpBindDhcpStatsSrvrDropdPckts"),
        ("TIMETRA-SDP-MIB", "sdpBindDhcpStatsClntProxRadPckts"),
        ("TIMETRA-SDP-MIB", "sdpBindDhcpStatsClntProxLSPckts"),
        ("TIMETRA-SDP-MIB", "sdpBindDhcpStatsGenReleasePckts"),
        ("TIMETRA-SDP-MIB", "sdpBindDhcpStatsGenForceRenPckts"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindDhcpV6v0Group.setStatus("current")

tmnxSdpBindIpipeV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 106)
)
tmnxSdpBindIpipeV6v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindIpipeCeInetAddressType"),
        ("TIMETRA-SDP-MIB", "sdpBindIpipeCeInetAddress"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindIpipeV6v0Group.setStatus("obsolete")

tmnxSdpFCV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 107)
)
tmnxSdpFCV6v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpFCMappingRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpFCMappingLspId"))
)
if mibBuilder.loadTexts:
    tmnxSdpFCV6v0Group.setStatus("current")

tmnxSdpBindCpipeV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 108)
)
tmnxSdpBindCpipeV6v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindCpipeLocalPayloadSize"),
        ("TIMETRA-SDP-MIB", "sdpBindCpipePeerPayloadSize"),
        ("TIMETRA-SDP-MIB", "sdpBindCpipeLocalBitrate"),
        ("TIMETRA-SDP-MIB", "sdpBindCpipePeerBitrate"),
        ("TIMETRA-SDP-MIB", "sdpBindCpipeLocalSigPkts"),
        ("TIMETRA-SDP-MIB", "sdpBindCpipePeerSigPkts"),
        ("TIMETRA-SDP-MIB", "sdpBindCpipeLocalCasTrunkFraming"),
        ("TIMETRA-SDP-MIB", "sdpBindCpipePeerCasTrunkFraming"),
        ("TIMETRA-SDP-MIB", "sdpBindCpipeLocalUseRtpHeader"),
        ("TIMETRA-SDP-MIB", "sdpBindCpipePeerUseRtpHeader"),
        ("TIMETRA-SDP-MIB", "sdpBindCpipeLocalDifferential"),
        ("TIMETRA-SDP-MIB", "sdpBindCpipePeerDifferential"),
        ("TIMETRA-SDP-MIB", "sdpBindCpipeLocalTimestampFreq"),
        ("TIMETRA-SDP-MIB", "sdpBindCpipePeerTimestampFreq"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindCpipeV6v0Group.setStatus("current")

tmnxSdpBindTlsL2ptV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 109)
)
tmnxSdpBindTlsL2ptV6v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindTlsMfibMdaRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsLastClearedTime"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsStpConfigBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsStpConfigBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsStpRstBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsStpRstBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsStpTcnBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsStpTcnBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsPvstConfigBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsPvstConfigBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsPvstRstBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsPvstRstBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsPvstTcnBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsPvstTcnBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsOtherBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsOtherBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsOtherL2ptBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsOtherL2ptBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsOtherInvalidBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsOtherInvalidBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsCdpBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsCdpBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsVtpBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsVtpBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsDtpBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsDtpBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsPagpBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsPagpBpdusTx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsUdldBpdusRx"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsUdldBpdusTx"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindTlsL2ptV6v0Group.setStatus("current")

tmnxSdpAutoBindV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 112)
)
tmnxSdpAutoBindV6v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "pwTemplateTableLastChanged"),
        ("TIMETRA-SDP-MIB", "pwTemplateRowStatus"),
        ("TIMETRA-SDP-MIB", "pwTemplateLastChanged"),
        ("TIMETRA-SDP-MIB", "pwTemplateVcType"),
        ("TIMETRA-SDP-MIB", "pwTemplateAccountingPolicyId"),
        ("TIMETRA-SDP-MIB", "pwTemplateCollectAcctStats"),
        ("TIMETRA-SDP-MIB", "pwTemplateMacLearning"),
        ("TIMETRA-SDP-MIB", "pwTemplateMacAgeing"),
        ("TIMETRA-SDP-MIB", "pwTemplateDiscardUnknownSource"),
        ("TIMETRA-SDP-MIB", "pwTemplateLimitMacMove"),
        ("TIMETRA-SDP-MIB", "pwTemplateMacPinning"),
        ("TIMETRA-SDP-MIB", "pwTemplateMacAddressLimit"),
        ("TIMETRA-SDP-MIB", "pwTemplateShgName"),
        ("TIMETRA-SDP-MIB", "pwTemplateShgDescription"),
        ("TIMETRA-SDP-MIB", "pwTemplateShgRestProtSrcMac"),
        ("TIMETRA-SDP-MIB", "pwTemplateShgRestUnprotDstMac"),
        ("TIMETRA-SDP-MIB", "pwTemplateEgressMacFilterId"),
        ("TIMETRA-SDP-MIB", "pwTemplateEgressIpFilterId"),
        ("TIMETRA-SDP-MIB", "pwTemplateEgressIpv6FilterId"),
        ("TIMETRA-SDP-MIB", "pwTemplateIngressMacFilterId"),
        ("TIMETRA-SDP-MIB", "pwTemplateIngressIpFilterId"),
        ("TIMETRA-SDP-MIB", "pwTemplateIngressIpv6FilterId"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpFastLeave"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpImportPlcy"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpLastMembIntvl"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpMaxNbrGrps"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpGenQueryIntvl"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpQueryRespIntvl"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpRobustCount"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpSendQueries"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpMcacPolicyName"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpMcacPrRsvMndBW"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpMcacUnconstBW"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpVersion"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgGrpSrcTblLC"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgRowStatus"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgLastChngd"),
        ("TIMETRA-SDP-MIB", "pwTemplateMfibAllowedMdaTblLC"),
        ("TIMETRA-SDP-MIB", "pwTemplateMfibMdaRowStatus"),
        ("TIMETRA-SDP-MIB", "pwTemplateUseProvisionedSdp"),
        ("TIMETRA-SDP-MIB", "pwTemplateVlanVcTag"),
        ("TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoTableLC"),
        ("TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoTemplateId"),
        ("TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoAGI"),
        ("TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoSAII"),
        ("TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoTAII"))
)
if mibBuilder.loadTexts:
    tmnxSdpAutoBindV6v0Group.setStatus("obsolete")

tmnxSdpBindTlsMrpV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 113)
)
tmnxSdpBindTlsMrpV6v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindTlsMrpTableLastChanged"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpLastChngd"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpJoinTime"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpLeaveTime"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpLeaveAllTime"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpPeriodicTime"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpPeriodicEnabled"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpRxPdus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpDroppedPdus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpTxPdus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpRxNewEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpRxJoinInEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpRxInEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpRxJoinEmptyEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpRxEmptyEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpRxLeaveEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpTxNewEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpTxJoinInEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpTxInEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpTxJoinEmptyEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpTxEmptyEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpTxLeaveEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMmrpDeclared"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMmrpRegistered"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindTlsMrpV6v0Group.setStatus("obsolete")

tmnxSdpTlsBgpV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 114)
)
tmnxSdpTlsBgpV6v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindTblLC"),
        ("TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindRowStatus"),
        ("TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindLastChngd"),
        ("TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindSHG"),
        ("TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindRTTblLC"),
        ("TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindRTRowStat"))
)
if mibBuilder.loadTexts:
    tmnxSdpTlsBgpV6v0Group.setStatus("current")

tmnxSdpL2V6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 115)
)
tmnxSdpL2V6v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpCreationOrigin"),
        ("TIMETRA-SDP-MIB", "sdpBindCreationOrigin"),
        ("TIMETRA-SDP-MIB", "svcL2RteTableLastChanged"),
        ("TIMETRA-SDP-MIB", "svcL2RteSdpBindId"),
        ("TIMETRA-SDP-MIB", "svcL2RtePwTemplateId"),
        ("TIMETRA-SDP-MIB", "svcL2RteError"),
        ("TIMETRA-SDP-MIB", "svcL2RteLastErrorTime"))
)
if mibBuilder.loadTexts:
    tmnxSdpL2V6v0Group.setStatus("current")

tmnxSdpAutoBindV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 116)
)
tmnxSdpAutoBindV6v1Group.setObjects(
      *(("TIMETRA-SDP-MIB", "pwTemplateTableLastChanged"),
        ("TIMETRA-SDP-MIB", "pwTemplateRowStatus"),
        ("TIMETRA-SDP-MIB", "pwTemplateLastChanged"),
        ("TIMETRA-SDP-MIB", "pwTemplateVcType"),
        ("TIMETRA-SDP-MIB", "pwTemplateAccountingPolicyId"),
        ("TIMETRA-SDP-MIB", "pwTemplateCollectAcctStats"),
        ("TIMETRA-SDP-MIB", "pwTemplateMacLearning"),
        ("TIMETRA-SDP-MIB", "pwTemplateMacAgeing"),
        ("TIMETRA-SDP-MIB", "pwTemplateDiscardUnknownSource"),
        ("TIMETRA-SDP-MIB", "pwTemplateLimitMacMove"),
        ("TIMETRA-SDP-MIB", "pwTemplateMacPinning"),
        ("TIMETRA-SDP-MIB", "pwTemplateMacAddressLimit"),
        ("TIMETRA-SDP-MIB", "pwTemplateShgName"),
        ("TIMETRA-SDP-MIB", "pwTemplateShgDescription"),
        ("TIMETRA-SDP-MIB", "pwTemplateShgRestProtSrcMac"),
        ("TIMETRA-SDP-MIB", "pwTemplateShgRestUnprotDstMac"),
        ("TIMETRA-SDP-MIB", "pwTemplateEgressMacFilterId"),
        ("TIMETRA-SDP-MIB", "pwTemplateEgressIpFilterId"),
        ("TIMETRA-SDP-MIB", "pwTemplateEgressIpv6FilterId"),
        ("TIMETRA-SDP-MIB", "pwTemplateIngressMacFilterId"),
        ("TIMETRA-SDP-MIB", "pwTemplateIngressIpFilterId"),
        ("TIMETRA-SDP-MIB", "pwTemplateIngressIpv6FilterId"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpFastLeave"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpImportPlcy"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpLastMembIntvl"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpMaxNbrGrps"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpGenQueryIntvl"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpQueryRespIntvl"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpRobustCount"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpSendQueries"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpVersion"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgGrpSrcTblLC"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgRowStatus"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgLastChngd"),
        ("TIMETRA-SDP-MIB", "pwTemplateMfibAllowedMdaTblLC"),
        ("TIMETRA-SDP-MIB", "pwTemplateMfibMdaRowStatus"),
        ("TIMETRA-SDP-MIB", "pwTemplateUseProvisionedSdp"),
        ("TIMETRA-SDP-MIB", "pwTemplateVlanVcTag"),
        ("TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoTableLC"),
        ("TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoTemplateId"),
        ("TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoAGI"),
        ("TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoSAII"),
        ("TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoTAII"))
)
if mibBuilder.loadTexts:
    tmnxSdpAutoBindV6v1Group.setStatus("obsolete")

tmnxSdpAutoBindV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 117)
)
tmnxSdpAutoBindV7v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "pwTemplateTableLastChanged"),
        ("TIMETRA-SDP-MIB", "pwTemplateRowStatus"),
        ("TIMETRA-SDP-MIB", "pwTemplateLastChanged"),
        ("TIMETRA-SDP-MIB", "pwTemplateVcType"),
        ("TIMETRA-SDP-MIB", "pwTemplateAccountingPolicyId"),
        ("TIMETRA-SDP-MIB", "pwTemplateCollectAcctStats"),
        ("TIMETRA-SDP-MIB", "pwTemplateMacLearning"),
        ("TIMETRA-SDP-MIB", "pwTemplateMacAgeing"),
        ("TIMETRA-SDP-MIB", "pwTemplateDiscardUnknownSource"),
        ("TIMETRA-SDP-MIB", "pwTemplateLimitMacMove"),
        ("TIMETRA-SDP-MIB", "pwTemplateMacPinning"),
        ("TIMETRA-SDP-MIB", "pwTemplateMacAddressLimit"),
        ("TIMETRA-SDP-MIB", "pwTemplateShgName"),
        ("TIMETRA-SDP-MIB", "pwTemplateShgDescription"),
        ("TIMETRA-SDP-MIB", "pwTemplateShgRestProtSrcMac"),
        ("TIMETRA-SDP-MIB", "pwTemplateShgRestUnprotDstMac"),
        ("TIMETRA-SDP-MIB", "pwTemplateEgressMacFilterId"),
        ("TIMETRA-SDP-MIB", "pwTemplateEgressIpFilterId"),
        ("TIMETRA-SDP-MIB", "pwTemplateEgressIpv6FilterId"),
        ("TIMETRA-SDP-MIB", "pwTemplateIngressMacFilterId"),
        ("TIMETRA-SDP-MIB", "pwTemplateIngressIpFilterId"),
        ("TIMETRA-SDP-MIB", "pwTemplateIngressIpv6FilterId"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpFastLeave"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpImportPlcy"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpLastMembIntvl"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpMaxNbrGrps"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpGenQueryIntvl"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpQueryRespIntvl"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpRobustCount"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpSendQueries"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpVersion"),
        ("TIMETRA-SDP-MIB", "pwTemplateForceVlanVcForwarding"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgGrpSrcTblLC"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgRowStatus"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgLastChngd"),
        ("TIMETRA-SDP-MIB", "pwTemplateMfibAllowedMdaTblLC"),
        ("TIMETRA-SDP-MIB", "pwTemplateMfibMdaRowStatus"),
        ("TIMETRA-SDP-MIB", "pwTemplateUseProvisionedSdp"),
        ("TIMETRA-SDP-MIB", "pwTemplateVlanVcTag"),
        ("TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoTableLC"),
        ("TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoTemplateId"),
        ("TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoAGI"),
        ("TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoSAII"),
        ("TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoTAII"))
)
if mibBuilder.loadTexts:
    tmnxSdpAutoBindV7v0Group.setStatus("current")

tmnxSdpBindIpipeV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 118)
)
tmnxSdpBindIpipeV7v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindIpipeCeInetAddressType"),
        ("TIMETRA-SDP-MIB", "sdpBindIpipeCeInetAddress"),
        ("TIMETRA-SDP-MIB", "sdpBindIpipePeerCeInetAddrType"),
        ("TIMETRA-SDP-MIB", "sdpBindIpipePeerCeInetAddr"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindIpipeV7v0Group.setStatus("obsolete")

tmnxSdpL2V7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 119)
)
tmnxSdpL2V7v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpEnforceDiffServLspFc")
)
if mibBuilder.loadTexts:
    tmnxSdpL2V7v0Group.setStatus("current")

tmnxSdpEvalPwTempV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 120)
)
tmnxSdpEvalPwTempV7v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "svcApplyEvalPwTemplateAction"),
        ("TIMETRA-SDP-MIB", "svcApplyEvalPwTemplateErrorMsg"),
        ("TIMETRA-SDP-MIB", "svcApplyEvalPwTemplateId"),
        ("TIMETRA-SDP-MIB", "svcApplyEvalPwTemplateSuccess"),
        ("TIMETRA-SDP-MIB", "svcApplyEvalPwTemplateSvcId"),
        ("TIMETRA-SDP-MIB", "svcApplyEvalPwTemplateTime"))
)
if mibBuilder.loadTexts:
    tmnxSdpEvalPwTempV7v0Group.setStatus("current")

tmnxSdpLdpBackupV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 121)
)
tmnxSdpLdpBackupV8v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpMixedLspModeEnabled"),
        ("TIMETRA-SDP-MIB", "sdpLspRevertTime"),
        ("TIMETRA-SDP-MIB", "sdpLspRevertTimeCountDown"),
        ("TIMETRA-SDP-MIB", "sdpLdpLspId"),
        ("TIMETRA-SDP-MIB", "sdpLdpActive"))
)
if mibBuilder.loadTexts:
    tmnxSdpLdpBackupV8v0Group.setStatus("obsolete")

tmnxSdpPbbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 122)
)
tmnxSdpPbbGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindPbbRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindPbbLastMgmtChange"),
        ("TIMETRA-SDP-MIB", "sdpBindPbbIgmpSnpgMRouter"))
)
if mibBuilder.loadTexts:
    tmnxSdpPbbGroup.setStatus("current")

tmnxSdpBindGenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 123)
)
tmnxSdpBindGenGroup.setObjects(
    ("TIMETRA-SDP-MIB", "sdpBindDescription")
)
if mibBuilder.loadTexts:
    tmnxSdpBindGenGroup.setStatus("current")

tmnxSdpBindTlsMrpV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 124)
)
tmnxSdpBindTlsMrpV8v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindTlsMrpTableLastChanged"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpLastChngd"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpJoinTime"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpLeaveTime"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpLeaveAllTime"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpPeriodicTime"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpPeriodicEnabled"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpRxPdus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpDroppedPdus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpTxPdus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpRxNewEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpRxJoinInEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpRxInEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpRxJoinEmptyEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpRxEmptyEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpRxLeaveEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpTxNewEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpTxJoinInEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpTxInEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpTxJoinEmptyEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpTxEmptyEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpTxLeaveEvent"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMmrpDeclared"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMmrpRegistered"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMmrpEndStation"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMrpPolicy"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindTlsMrpV8v0Group.setStatus("current")

tmnxSdpV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 125)
)
tmnxSdpV8v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpNetDomainName"),
        ("TIMETRA-SDP-MIB", "sdpEgressIfsNetDomainConsistent"),
        ("TIMETRA-SDP-MIB", "sdpBgpTunnelEnabled"),
        ("TIMETRA-SDP-MIB", "sdpBgpTunnelLspId"),
        ("TIMETRA-SDP-MIB", "sdpTunnelFarEndIpAddress"))
)
if mibBuilder.loadTexts:
    tmnxSdpV8v0Group.setStatus("obsolete")

tmnxSdpBindV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 126)
)
tmnxSdpBindV8v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindSiteName"),
        ("TIMETRA-SDP-MIB", "sdpBindHashLabel"),
        ("TIMETRA-SDP-MIB", "sdpBindHashLabelSignalCapability"),
        ("TIMETRA-SDP-MIB", "sdpBindIsaAaApplicationProfile"),
        ("TIMETRA-SDP-MIB", "sdpBindFPropBMacAddrTblLastChgd"),
        ("TIMETRA-SDP-MIB", "sdpBindFPropBMacAddrRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindPwStatusSignaling"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindV8v0Group.setStatus("current")

tmnxSdpAutoBindV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 127)
)
tmnxSdpAutoBindV8v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "pwTemplateHashLabel"),
        ("TIMETRA-SDP-MIB", "pwTemplateControlWord"),
        ("TIMETRA-SDP-MIB", "pwTemplateHashLabelSignalCap"),
        ("TIMETRA-SDP-MIB", "sdpAutoBindBgpVplsTableLC"),
        ("TIMETRA-SDP-MIB", "sdpAutoBindBgpVplsTemplateId"))
)
if mibBuilder.loadTexts:
    tmnxSdpAutoBindV8v0Group.setStatus("current")

tmnxSdpBindIpipeV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 128)
)
tmnxSdpBindIpipeV8v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindIpipeCeInetAddressType"),
        ("TIMETRA-SDP-MIB", "sdpBindIpipeCeInetAddress"),
        ("TIMETRA-SDP-MIB", "sdpBindIpipePeerCeInetAddrType"),
        ("TIMETRA-SDP-MIB", "sdpBindIpipePeerCeInetAddr"),
        ("TIMETRA-SDP-MIB", "sdpBindIpipePeerIpv6Capability"),
        ("TIMETRA-SDP-MIB", "sdpBindIpipePeerLLCeInetAddr"),
        ("TIMETRA-SDP-MIB", "sdpBindIpipePeerGlobalCeInetAddr"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindIpipeV8v0Group.setStatus("current")

tmnxSdpBindV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 129)
)
tmnxSdpBindV9v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpBindIngressFlowspec")
)
if mibBuilder.loadTexts:
    tmnxSdpBindV9v0Group.setStatus("current")

tmnxSdpBindCpmProtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 130)
)
tmnxSdpBindCpmProtGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindCpmProtPolicyId"),
        ("TIMETRA-SDP-MIB", "sdpBindCpmProtMonitorMac"),
        ("TIMETRA-SDP-MIB", "sdpBindCpmProtEthCfmMonitorFlags"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindCpmProtGroup.setStatus("current")

tmnxSdpBindBsxV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 131)
)
tmnxSdpBindBsxV9v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindTransitIpPolicyId"),
        ("TIMETRA-SDP-MIB", "sdpBindTransitPrefixPolicyId"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindBsxV9v0Group.setStatus("current")

tmnxSdpBindTlsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 132)
)
tmnxSdpBindTlsV8v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindTlsInTcBitBpdus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsOutTcBitBpdus"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindTlsV8v0Group.setStatus("current")

tmnxSdpV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 133)
)
tmnxSdpV9v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpAtBndBgp129Type2SaiiAcId"),
        ("TIMETRA-SDP-MIB", "sdpAtBndBgp129Type2SaiiGlobalId"),
        ("TIMETRA-SDP-MIB", "sdpAtBndBgp129Type2SaiiPrefix"),
        ("TIMETRA-SDP-MIB", "sdpAtBndBgp129Type2TableLC"),
        ("TIMETRA-SDP-MIB", "sdpAtBndBgp129Type2TaiiAcId"),
        ("TIMETRA-SDP-MIB", "sdpAtBndBgp129Type2TaiiGlobalId"),
        ("TIMETRA-SDP-MIB", "sdpAtBndBgp129Type2TaiiPrefix"),
        ("TIMETRA-SDP-MIB", "sdpAtBndBgp129Type2TemplateId"),
        ("TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindOperGrp"),
        ("TIMETRA-SDP-MIB", "sdpBindOperGrp"),
        ("TIMETRA-SDP-MIB", "sdpBindMonitorOperGrp"),
        ("TIMETRA-SDP-MIB", "sdpBindOperHashLabel"))
)
if mibBuilder.loadTexts:
    tmnxSdpV9v0Group.setStatus("current")

tmnxSdpMixedLspModeV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 134)
)
tmnxSdpMixedLspModeV9v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpMixedLspModeEnabled"),
        ("TIMETRA-SDP-MIB", "sdpLspRevertTime"),
        ("TIMETRA-SDP-MIB", "sdpLspRevertTimeCountDown"),
        ("TIMETRA-SDP-MIB", "sdpLdpLspId"),
        ("TIMETRA-SDP-MIB", "sdpActiveLspType"))
)
if mibBuilder.loadTexts:
    tmnxSdpMixedLspModeV9v0Group.setStatus("current")

tmnxSdpSpbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 135)
)
tmnxSdpSpbGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindTlsSpbAdminState"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsSpbIfIndex"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsSpbLastChgd"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsSpbRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsSpbTblLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxSdpSpbGroup.setStatus("current")

tmnxSdpBindBsxV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 136)
)
tmnxSdpBindBsxV10v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindAarpId"),
        ("TIMETRA-SDP-MIB", "sdpBindAarpServRefType"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindBsxV10v0Group.setStatus("current")

tmnxSdpPwPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 137)
)
tmnxSdpPwPortGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpPwPortAdminStatus"),
        ("TIMETRA-SDP-MIB", "sdpPwPortEncapType"),
        ("TIMETRA-SDP-MIB", "sdpPwPortLastChgd"),
        ("TIMETRA-SDP-MIB", "sdpPwPortRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpPwPortTblLastChanged"),
        ("TIMETRA-SDP-MIB", "sdpPwPortVcId"),
        ("TIMETRA-SDP-MIB", "sdpPwPortOperStatus"),
        ("TIMETRA-SDP-MIB", "sdpPwPortOperFlags"),
        ("TIMETRA-SDP-MIB", "sdpPwPortVcType"),
        ("TIMETRA-SDP-MIB", "sdpPwPortVlanVcTag"),
        ("TIMETRA-SDP-MIB", "sdpPwPortEgrShapDefIntDestId"),
        ("TIMETRA-SDP-MIB", "sdpPwPortEgrShapVPort"),
        ("TIMETRA-SDP-MIB", "sdpBindingPort"))
)
if mibBuilder.loadTexts:
    tmnxSdpPwPortGroup.setStatus("obsolete")

tmnxSdpV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 138)
)
tmnxSdpV10v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindPwLocalStatusBits"),
        ("TIMETRA-SDP-MIB", "pwTemplateAutoLearnMacProtect"),
        ("TIMETRA-SDP-MIB", "pwTemplateRestProtSrcMac"),
        ("TIMETRA-SDP-MIB", "pwTemplateRestProtSrcMacAction"),
        ("TIMETRA-SDP-MIB", "pwTemplateShgAutoLearnMacProtect"),
        ("TIMETRA-SDP-MIB", "pwTemplateShgRestProtSrcMacAct"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsAutoLearnMacProtect"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsRestProtSrcMac"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsRestProtSrcMacAction"),
        ("TIMETRA-SDP-MIB", "sdpBindMeshTlsAutoLearnMacProt"),
        ("TIMETRA-SDP-MIB", "sdpBindMeshTlsRestProtSrcMac"),
        ("TIMETRA-SDP-MIB", "sdpBindMeshTlsRestProtSrcMacAct"))
)
if mibBuilder.loadTexts:
    tmnxSdpV10v0Group.setStatus("current")

tmnxSdpBindDhcpV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 139)
)
tmnxSdpBindDhcpV11v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindDhcp6Description"),
        ("TIMETRA-SDP-MIB", "sdpBindDhcp6Snoop"),
        ("TIMETRA-SDP-MIB", "sdpBindDhcpStatsClntProxUDBPckts"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindDhcpV11v0Group.setStatus("current")

tmnxSdpBindDhcpV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 140)
)
tmnxSdpBindDhcpV13v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpBindDhcpStatsClntProxNqPckts")
)
if mibBuilder.loadTexts:
    tmnxSdpBindDhcpV13v0Group.setStatus("current")

tmnxSdpNotifyObjsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 200)
)
tmnxSdpNotifyObjsV6v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpNotifySdpId"),
        ("TIMETRA-SDP-MIB", "sdpMaxBookableBandwidth"),
        ("TIMETRA-SDP-MIB", "sdpBookedBandwidth"),
        ("TIMETRA-SDP-MIB", "dynamicSdpStatus"),
        ("TIMETRA-SDP-MIB", "dynamicSdpOrigin"),
        ("TIMETRA-SDP-MIB", "dynamicSdpCreationError"),
        ("TIMETRA-SDP-MIB", "dynamicSdpBindCreationError"))
)
if mibBuilder.loadTexts:
    tmnxSdpNotifyObjsV6v0Group.setStatus("obsolete")

tmnxSdpNotifyObjsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 201)
)
tmnxSdpNotifyObjsV7v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpNotifySdpId"),
        ("TIMETRA-SDP-MIB", "sdpMaxBookableBandwidth"),
        ("TIMETRA-SDP-MIB", "sdpBookedBandwidth"),
        ("TIMETRA-SDP-MIB", "dynamicSdpStatus"),
        ("TIMETRA-SDP-MIB", "dynamicSdpOrigin"),
        ("TIMETRA-SDP-MIB", "dynamicSdpCreationError"),
        ("TIMETRA-SDP-MIB", "dynamicSdpBindCreationError"),
        ("TIMETRA-SDP-MIB", "sdpBindNotifyMacAddr"))
)
if mibBuilder.loadTexts:
    tmnxSdpNotifyObjsV7v0Group.setStatus("current")

tmnxSdpNotifyObjsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 202)
)
tmnxSdpNotifyObjsV8v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpEgIfNetDomainInconsCount")
)
if mibBuilder.loadTexts:
    tmnxSdpNotifyObjsV8v0Group.setStatus("current")

tmnxSdpBgpVplsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 203)
)
tmnxSdpBgpVplsV8v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "svcL2BgpVplsRteControlWord"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVplsRteError"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVplsRteLastErrorTime"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVplsRtePathMtu"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVplsRtePwTemplateId"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVplsRteSdpBindId"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVplsRteSeqDelivery"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVplsRteState"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVplsRteDF"))
)
if mibBuilder.loadTexts:
    tmnxSdpBgpVplsV8v0Group.setStatus("current")

tmnxSdpL2V8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 204)
)
tmnxSdpL2V8v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "svcL2RteStatus"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVplsRteStatus"))
)
if mibBuilder.loadTexts:
    tmnxSdpL2V8v0Group.setStatus("current")

tmnxSdpPwV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 205)
)
tmnxSdpPwV8v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpBindStandbySigSlave")
)
if mibBuilder.loadTexts:
    tmnxSdpPwV8v0Group.setStatus("current")

tmnxSdpBindEthCfmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 206)
)
tmnxSdpBindEthCfmGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindEthCfmTableLastChanged"),
        ("TIMETRA-SDP-MIB", "sdpBindEthCfmRowLastChanged"),
        ("TIMETRA-SDP-MIB", "sdpBindEthCfmVMepFilter"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindEthCfmGroup.setStatus("current")

tmnxSdpNotifyObjsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 207)
)
tmnxSdpNotifyObjsV9v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpMSPwPeId")
)
if mibBuilder.loadTexts:
    tmnxSdpNotifyObjsV9v0Group.setStatus("current")

tmnxSdpBindIpipeNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 208)
)
tmnxSdpBindIpipeNotifyObjsGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindIpipeCeIpAddrType"),
        ("TIMETRA-SDP-MIB", "sdpBindIpipeCeIpAddress"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindIpipeNotifyObjsGroup.setStatus("current")

tmnxSdpObsoletedObjsV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 300)
)
tmnxSdpObsoletedObjsV6v1Group.setObjects(
      *(("TIMETRA-SDP-MIB", "pwTemplateIgmpMcacPolicyName"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpMcacPrRsvMndBW"),
        ("TIMETRA-SDP-MIB", "pwTemplateIgmpMcacUnconstBW"))
)
if mibBuilder.loadTexts:
    tmnxSdpObsoletedObjsV6v1Group.setStatus("current")

tmnxSdpObsoletedObjsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 301)
)
tmnxSdpObsoletedObjsV9v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpLdpActive")
)
if mibBuilder.loadTexts:
    tmnxSdpObsoletedObjsV9v0Group.setStatus("current")

tmnxSdpBindQGrpObjsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 302)
)
tmnxSdpBindQGrpObjsV10v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindIngressQoSNetworkPlcyId"),
        ("TIMETRA-SDP-MIB", "sdpBindEgressQoSNetworkPlcyId"),
        ("TIMETRA-SDP-MIB", "sdpBindIngressQoSFpRedirectQGrp"),
        ("TIMETRA-SDP-MIB", "sdpBindEgressQoSPortRedirectQGrp"),
        ("TIMETRA-SDP-MIB", "sdpBindIngressQoSInstanceId"),
        ("TIMETRA-SDP-MIB", "sdpBindEgressQoSInstanceId"),
        ("TIMETRA-SDP-MIB", "pwTemplateIngQoSNetworkPlcyId"),
        ("TIMETRA-SDP-MIB", "pwTemplateEgrQoSNetworkPlcyId"),
        ("TIMETRA-SDP-MIB", "pwTemplateIngQoSFpRedirectQGrp"),
        ("TIMETRA-SDP-MIB", "pwTemplateEgrQoSPortRedirectQGrp"),
        ("TIMETRA-SDP-MIB", "pwTemplateIngQoSInstanceId"),
        ("TIMETRA-SDP-MIB", "pwTemplateEgrQoSInstanceId"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindQGrpObjsV10v0Group.setStatus("current")

tmnxSdpGrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 500)
)
tmnxSdpGrpGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "pwTempExcSdpGrpLastChanged"),
        ("TIMETRA-SDP-MIB", "pwTempExcSdpGrpRowStatus"),
        ("TIMETRA-SDP-MIB", "pwTempExcSdpGrpTableLastChanged"),
        ("TIMETRA-SDP-MIB", "pwTempIncSdpGrpLastChanged"),
        ("TIMETRA-SDP-MIB", "pwTempIncSdpGrpRowStatus"),
        ("TIMETRA-SDP-MIB", "pwTempIncSdpGrpTableLastChanged"),
        ("TIMETRA-SDP-MIB", "sdpGrpLastChange"),
        ("TIMETRA-SDP-MIB", "sdpGrpRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpGrpTblLastChanged"),
        ("TIMETRA-SDP-MIB", "sdpGrpValue"),
        ("TIMETRA-SDP-MIB", "sdpSdpGrpLastChange"),
        ("TIMETRA-SDP-MIB", "sdpSdpGrpRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpSdpGrpTblLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxSdpGrpGroup.setStatus("current")

tmnxSdpBindBlockOnPeerFaultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 501)
)
tmnxSdpBindBlockOnPeerFaultGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "pwTemplateBlockOnPeerFault"),
        ("TIMETRA-SDP-MIB", "sdpBindBlockOnPeerFault"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindBlockOnPeerFaultGroup.setStatus("current")

tmnxSdpBindFlowSpecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 502)
)
tmnxSdpBindFlowSpecGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindIngressFlowspec"),
        ("TIMETRA-SDP-MIB", "sdpBindIngressIPv6Flowspec"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindFlowSpecGroup.setStatus("current")

tmnxSdpBindPwPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 503)
)
tmnxSdpBindPwPortGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpFarEndNodeId"),
        ("TIMETRA-SDP-MIB", "sdpFarEndGlobalId"),
        ("TIMETRA-SDP-MIB", "sdpBindPwPathRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindPwPathAgi"),
        ("TIMETRA-SDP-MIB", "sdpBindPwPathLastChanged"),
        ("TIMETRA-SDP-MIB", "sdpBindPwPathSaiiAcId"),
        ("TIMETRA-SDP-MIB", "sdpBindPwPathSaiiGlobalId"),
        ("TIMETRA-SDP-MIB", "sdpBindPwPathSaiiNodeId"),
        ("TIMETRA-SDP-MIB", "sdpBindPwPathTableLastChanged"),
        ("TIMETRA-SDP-MIB", "sdpBindPwPathTaiiAcId"),
        ("TIMETRA-SDP-MIB", "sdpBindPwPathTaiiGlobalId"),
        ("TIMETRA-SDP-MIB", "sdpBindPwPathTaiiNodeId"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindPwPortGroup.setStatus("current")

tmnxSdpVllBgpV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 504)
)
tmnxSdpVllBgpV11v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpAutoBindBgpVpwsTemplateId"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVpwsRteSdpBindId"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVpwsRtePwTemplateId"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVpwsRteError"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVpwsRteLastErrorTime"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVpwsRteControlWord"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVpwsRtePathMtu"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVpwsRteState"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVpwsRteSeqDelivery"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVpwsRteStatus"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVpwsRteCsv"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVpwsRtePreference"),
        ("TIMETRA-SDP-MIB", "svcL2BgpVpwsRteTxStatus"),
        ("TIMETRA-SDP-MIB", "svcVllBgpADPWTempBindRTTblLC"),
        ("TIMETRA-SDP-MIB", "svcVllBgpADPWTempBindRTRowStat"),
        ("TIMETRA-SDP-MIB", "svcVllBgpADPWTempBindTblLC"),
        ("TIMETRA-SDP-MIB", "svcVllBgpADPWTempBindRowStatus"),
        ("TIMETRA-SDP-MIB", "svcVllBgpADPWTempBindLastChngd"),
        ("TIMETRA-SDP-MIB", "svcVllBgpADPWTempBindEndPt"))
)
if mibBuilder.loadTexts:
    tmnxSdpVllBgpV11v0Group.setStatus("current")

tmnxSdpL2tpv3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 505)
)
tmnxSdpL2tpv3Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindMirrorRemoteSource"),
        ("TIMETRA-SDP-MIB", "sdpFarEndInetAddressType"),
        ("TIMETRA-SDP-MIB", "sdpFarEndInetAddress"),
        ("TIMETRA-SDP-MIB", "sdpLocalEndInetAddressType"),
        ("TIMETRA-SDP-MIB", "sdpLocalEndInetAddress"),
        ("TIMETRA-SDP-MIB", "sdpBindL2tpv3SessMismatch"),
        ("TIMETRA-SDP-MIB", "sdpBindL2tpv3SessMismatchLstClrd"),
        ("TIMETRA-SDP-MIB", "sdpBindL2tpv3IngressCookie"),
        ("TIMETRA-SDP-MIB", "sdpBindL2tpv3EgressCookie"))
)
if mibBuilder.loadTexts:
    tmnxSdpL2tpv3Group.setStatus("current")

tmnxSdpBindSpbV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 506)
)
tmnxSdpBindSpbV11v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindTlsStaticIsidStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStaticIsidRngRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStaticIsidRngLastChgd"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStaticIsidRngLow"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStaticIsidRngHigh"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindSpbV11v0Group.setStatus("current")

tmnxSdpBindEthLoopbackV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 507)
)
tmnxSdpBindEthLoopbackV11v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindEthLoopbackRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindEthLoopbackMode"),
        ("TIMETRA-SDP-MIB", "sdpBindEthLoopbackMacSwap"),
        ("TIMETRA-SDP-MIB", "sdpBindEthLoopbackMacSwapAddr"),
        ("TIMETRA-SDP-MIB", "sdpBindEthLoopbackMacSwapAddrAll"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindEthLoopbackV11v0Group.setStatus("current")

tmnxSdpPwSecShaperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 509)
)
tmnxSdpPwSecShaperGroup.setObjects(
    ("TIMETRA-SDP-MIB", "sdpPwPortEgrShapSapSecShaper")
)
if mibBuilder.loadTexts:
    tmnxSdpPwSecShaperGroup.setStatus("current")

tmnxSdpPwPortV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 510)
)
tmnxSdpPwPortV11v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpPwPortAdminStatus"),
        ("TIMETRA-SDP-MIB", "sdpPwPortLastChgd"),
        ("TIMETRA-SDP-MIB", "sdpPwPortRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpPwPortTblLastChanged"),
        ("TIMETRA-SDP-MIB", "sdpPwPortVcId"),
        ("TIMETRA-SDP-MIB", "sdpPwPortOperStatus"),
        ("TIMETRA-SDP-MIB", "sdpPwPortOperFlags"),
        ("TIMETRA-SDP-MIB", "sdpPwPortVcType"),
        ("TIMETRA-SDP-MIB", "sdpPwPortVlanVcTag"),
        ("TIMETRA-SDP-MIB", "sdpPwPortEgrShapDefIntDestId"),
        ("TIMETRA-SDP-MIB", "sdpPwPortEgrShapVPort"),
        ("TIMETRA-SDP-MIB", "sdpBindingPort"))
)
if mibBuilder.loadTexts:
    tmnxSdpPwPortV11v0Group.setStatus("current")

tmnxSdpObsoletedObjsV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 511)
)
tmnxSdpObsoletedObjsV11v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpPwPortEncapType")
)
if mibBuilder.loadTexts:
    tmnxSdpObsoletedObjsV11v0Group.setStatus("current")

tmnxSdpBindCtrlChanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 512)
)
tmnxSdpBindCtrlChanGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindCtrlChanPwStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindCtrlChanPwLastChanged"),
        ("TIMETRA-SDP-MIB", "sdpBindCtrlChanPwRefreshTimer"),
        ("TIMETRA-SDP-MIB", "sdpBindCtrlChanPwPeerExpired"),
        ("TIMETRA-SDP-MIB", "sdpBindCtrlChanPwTableLastChgd"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindCtrlChanGroup.setStatus("current")

sdpBindTlsFdbMacStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 514)
)
sdpBindTlsFdbMacStatsGroup.setObjects(
    ("TIMETRA-SDP-MIB", "sdpBindTlsFdbMacStatsNumEntries")
)
if mibBuilder.loadTexts:
    sdpBindTlsFdbMacStatsGroup.setStatus("current")

sdpBindTlsEtreeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 515)
)
sdpBindTlsEtreeGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindEtreeRootLeafTag"),
        ("TIMETRA-SDP-MIB", "sdpBindEtreeLeafAc"))
)
if mibBuilder.loadTexts:
    sdpBindTlsEtreeGroup.setStatus("current")

tmnxSdpBindCpmProtV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 516)
)
tmnxSdpBindCpmProtV12v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpBindCpmProtMonitorIP")
)
if mibBuilder.loadTexts:
    tmnxSdpBindCpmProtV12v0Group.setStatus("current")

tmnxSdpBindCtrlChanReqGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 517)
)
tmnxSdpBindCtrlChanReqGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindCtrlChanPwRequestTimer"),
        ("TIMETRA-SDP-MIB", "sdpBindCtrlChanPwRetryTimer"),
        ("TIMETRA-SDP-MIB", "sdpBindCtrlChanPwTimeoutMult"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindCtrlChanReqGroup.setStatus("current")

tmnxSdpBindCtrlChanAckGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 518)
)
tmnxSdpBindCtrlChanAckGroup.setObjects(
    ("TIMETRA-SDP-MIB", "sdpBindCtrlChanPwAck")
)
if mibBuilder.loadTexts:
    tmnxSdpBindCtrlChanAckGroup.setStatus("current")

tmnxSdpPBBEpipePWRedV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 519)
)
tmnxSdpPBBEpipePWRedV12v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpSourceBMacLSB"),
        ("TIMETRA-SDP-MIB", "sdpControlPWVCId"),
        ("TIMETRA-SDP-MIB", "sdpBindUseSdpBMac"),
        ("TIMETRA-SDP-MIB", "sdpControlPWIsActive"))
)
if mibBuilder.loadTexts:
    tmnxSdpPBBEpipePWRedV12v0Group.setStatus("current")

tmnxSdpPbbEpipeNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 520)
)
tmnxSdpPbbEpipeNotifyObjsGroup.setObjects(
    ("TIMETRA-SDP-MIB", "sdpPbbActvPwWithNonActvCtrlPw")
)
if mibBuilder.loadTexts:
    tmnxSdpPbbEpipeNotifyObjsGroup.setStatus("current")

tmnxSdpBindEthCfmV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 522)
)
tmnxSdpBindEthCfmV12v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindEthCfmSquelchIngress"),
        ("TIMETRA-SDP-MIB", "sdpBindEthCfmCollectLmmStats"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindEthCfmV12v0Group.setStatus("current")

tmnxSdpV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 523)
)
tmnxSdpV12v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindCreatOrigin"),
        ("TIMETRA-SDP-MIB", "sdpNumEntries"),
        ("TIMETRA-SDP-MIB", "sdpNextFreeId"),
        ("TIMETRA-SDP-MIB", "sdpId"),
        ("TIMETRA-SDP-MIB", "sdpRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpDelivery"),
        ("TIMETRA-SDP-MIB", "sdpFarEndIpAddress"),
        ("TIMETRA-SDP-MIB", "sdpLspList"),
        ("TIMETRA-SDP-MIB", "sdpDescription"),
        ("TIMETRA-SDP-MIB", "sdpLabelSignaling"),
        ("TIMETRA-SDP-MIB", "sdpAdminStatus"),
        ("TIMETRA-SDP-MIB", "sdpOperStatus"),
        ("TIMETRA-SDP-MIB", "sdpOperPathMtu"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveAdminStatus"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveOperStatus"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveHelloTime"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveMaxDropCount"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveHoldDownTime"),
        ("TIMETRA-SDP-MIB", "sdpLastMgmtChange"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveNumHelloRequestMessages"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveNumHelloResponseMessages"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveNumLateHelloResponseMessages"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveHelloRequestTimeout"),
        ("TIMETRA-SDP-MIB", "sdpLdpEnabled"),
        ("TIMETRA-SDP-MIB", "sdpVlanVcEtype"),
        ("TIMETRA-SDP-MIB", "sdpAdvertisedVllMtuOverride"),
        ("TIMETRA-SDP-MIB", "sdpOperFlags"),
        ("TIMETRA-SDP-MIB", "sdpLastStatusChange"),
        ("TIMETRA-SDP-MIB", "sdpMvplsMgmtService"),
        ("TIMETRA-SDP-MIB", "sdpMvplsMgmtSdpBndId"),
        ("TIMETRA-SDP-MIB", "sdpCollectAcctStats"),
        ("TIMETRA-SDP-MIB", "sdpAccountingPolicyId"),
        ("TIMETRA-SDP-MIB", "sdpClassFwdingEnabled"),
        ("TIMETRA-SDP-MIB", "sdpClassFwdingDefaultLsp"),
        ("TIMETRA-SDP-MIB", "sdpClassFwdingMcLsp"),
        ("TIMETRA-SDP-MIB", "sdpMetric"),
        ("TIMETRA-SDP-MIB", "sdpAutoSdp"),
        ("TIMETRA-SDP-MIB", "sdpPBBEtype"),
        ("TIMETRA-SDP-MIB", "sdpBandwidthBookingFactor"),
        ("TIMETRA-SDP-MIB", "sdpOperBandwidth"),
        ("TIMETRA-SDP-MIB", "sdpAvailableBandwidth"),
        ("TIMETRA-SDP-MIB", "sdpAdminPathMtu"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveHelloMessageLength"))
)
if mibBuilder.loadTexts:
    tmnxSdpV12v0Group.setStatus("obsolete")

tmnxSdpObsoletedObjsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 524)
)
tmnxSdpObsoletedObjsV12v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpSnmpAllowed")
)
if mibBuilder.loadTexts:
    tmnxSdpObsoletedObjsV12v0Group.setStatus("current")

tmnxSdpBfdV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 525)
)
tmnxSdpBfdV12v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "svcVllBgpADPWTempBindBfdTemplate"),
        ("TIMETRA-SDP-MIB", "svcVllBgpADPWTempBindBfdEnable"),
        ("TIMETRA-SDP-MIB", "svcVllBgpADPWTempBindBfdEncap"),
        ("TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindBfdTemplate"),
        ("TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindBfdEnable"),
        ("TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindBfdEncap"),
        ("TIMETRA-SDP-MIB", "sdpBindBfdTemplateName"),
        ("TIMETRA-SDP-MIB", "sdpBindBfdEnable"),
        ("TIMETRA-SDP-MIB", "sdpBindBfdEncap"))
)
if mibBuilder.loadTexts:
    tmnxSdpBfdV12v0Group.setStatus("current")

tmnxSdpL2tpv3CookieGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 526)
)
tmnxSdpL2tpv3CookieGroup.setObjects(
    ("TIMETRA-SDP-MIB", "sdpBindL2tpv3IngressCookie2")
)
if mibBuilder.loadTexts:
    tmnxSdpL2tpv3CookieGroup.setStatus("current")

tmnxSdpPwTempBindV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 527)
)
tmnxSdpPwTempBindV12v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindMonOperGrp")
)
if mibBuilder.loadTexts:
    tmnxSdpPwTempBindV12v0Group.setStatus("current")

tmnxSdpPbbV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 528)
)
tmnxSdpPbbV12v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpBindPbbMldSnpgMRouter")
)
if mibBuilder.loadTexts:
    tmnxSdpPbbV12v0Group.setStatus("current")

tmnxSdpPwLoopbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 529)
)
tmnxSdpPwLoopbackGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindPwLoopbackRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindPwAdminLockRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindPwAdminLockTestSvc"))
)
if mibBuilder.loadTexts:
    tmnxSdpPwLoopbackGroup.setStatus("current")

tmnxPwTemplateAugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 530)
)
tmnxPwTemplateAugGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "pwTemplateAugTableLastChgd"),
        ("TIMETRA-SDP-MIB", "pwTemplateAugLastChgd"),
        ("TIMETRA-SDP-MIB", "pwTemplateAugStpAutoEdge"),
        ("TIMETRA-SDP-MIB", "pwTemplateAugStpRapidStart"),
        ("TIMETRA-SDP-MIB", "pwTemplateAugStpAdminPtToPt"),
        ("TIMETRA-SDP-MIB", "pwTemplateAugStpPathCost"),
        ("TIMETRA-SDP-MIB", "pwTemplateAugStpPriority"),
        ("TIMETRA-SDP-MIB", "pwTemplateAugStpRootGuard"),
        ("TIMETRA-SDP-MIB", "pwTemplateAugStpAdminStatus"),
        ("TIMETRA-SDP-MIB", "pwTemplateAugL2ptTermination"),
        ("TIMETRA-SDP-MIB", "pwTemplateAugL2ptProtocols"))
)
if mibBuilder.loadTexts:
    tmnxPwTemplateAugGroup.setStatus("current")

tmnxSdpLdpIpv6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 532)
)
tmnxSdpLdpIpv6Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpTunnelFarEndInetAddressType"),
        ("TIMETRA-SDP-MIB", "sdpTunnelFarEndInetAddress"))
)
if mibBuilder.loadTexts:
    tmnxSdpLdpIpv6Group.setStatus("current")

tmnxSdpBindV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 533)
)
tmnxSdpBindV13v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindIngressVlanTranslation"),
        ("TIMETRA-SDP-MIB", "sdpBindIngressVlanTranslationId"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindV13v0Group.setStatus("obsolete")

tmnxSdpSegRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 534)
)
tmnxSdpSegRouteGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpSegRouteIsIs"),
        ("TIMETRA-SDP-MIB", "sdpSegRouteIsIsOperInstId"),
        ("TIMETRA-SDP-MIB", "sdpSegRouteIsIsLspId"),
        ("TIMETRA-SDP-MIB", "sdpSegRouteOspf"),
        ("TIMETRA-SDP-MIB", "sdpSegRouteOspfOperInstId"),
        ("TIMETRA-SDP-MIB", "sdpSegRouteOspfLspId"),
        ("TIMETRA-SDP-MIB", "sdpSegRouteTableLastChgd"))
)
if mibBuilder.loadTexts:
    tmnxSdpSegRouteGroup.setStatus("current")

tmnxSdpBindV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 535)
)
tmnxSdpBindV11v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindForceQinqVcForwarding"),
        ("TIMETRA-SDP-MIB", "pwTemplateForceQinqVcForwarding"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindV11v0Group.setStatus("obsolete")

tmnxSdpPwPortOperGrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 536)
)
tmnxSdpPwPortOperGrpGroup.setObjects(
    ("TIMETRA-SDP-MIB", "sdpPwPortMonOperGrp")
)
if mibBuilder.loadTexts:
    tmnxSdpPwPortOperGrpGroup.setStatus("current")

tmnxSdpV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 537)
)
tmnxSdpV13v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindCreatOrigin"),
        ("TIMETRA-SDP-MIB", "sdpNumEntries"),
        ("TIMETRA-SDP-MIB", "sdpNextFreeId"),
        ("TIMETRA-SDP-MIB", "sdpId"),
        ("TIMETRA-SDP-MIB", "sdpRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpDelivery"),
        ("TIMETRA-SDP-MIB", "sdpLspList"),
        ("TIMETRA-SDP-MIB", "sdpDescription"),
        ("TIMETRA-SDP-MIB", "sdpLabelSignaling"),
        ("TIMETRA-SDP-MIB", "sdpAdminStatus"),
        ("TIMETRA-SDP-MIB", "sdpOperStatus"),
        ("TIMETRA-SDP-MIB", "sdpOperPathMtu"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveAdminStatus"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveOperStatus"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveHelloTime"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveMaxDropCount"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveHoldDownTime"),
        ("TIMETRA-SDP-MIB", "sdpLastMgmtChange"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveNumHelloRequestMessages"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveNumHelloResponseMessages"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveNumLateHelloResponseMessages"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveHelloRequestTimeout"),
        ("TIMETRA-SDP-MIB", "sdpLdpEnabled"),
        ("TIMETRA-SDP-MIB", "sdpVlanVcEtype"),
        ("TIMETRA-SDP-MIB", "sdpAdvertisedVllMtuOverride"),
        ("TIMETRA-SDP-MIB", "sdpOperFlags"),
        ("TIMETRA-SDP-MIB", "sdpLastStatusChange"),
        ("TIMETRA-SDP-MIB", "sdpMvplsMgmtService"),
        ("TIMETRA-SDP-MIB", "sdpMvplsMgmtSdpBndId"),
        ("TIMETRA-SDP-MIB", "sdpCollectAcctStats"),
        ("TIMETRA-SDP-MIB", "sdpAccountingPolicyId"),
        ("TIMETRA-SDP-MIB", "sdpClassFwdingEnabled"),
        ("TIMETRA-SDP-MIB", "sdpClassFwdingDefaultLsp"),
        ("TIMETRA-SDP-MIB", "sdpClassFwdingMcLsp"),
        ("TIMETRA-SDP-MIB", "sdpMetric"),
        ("TIMETRA-SDP-MIB", "sdpAutoSdp"),
        ("TIMETRA-SDP-MIB", "sdpPBBEtype"),
        ("TIMETRA-SDP-MIB", "sdpBandwidthBookingFactor"),
        ("TIMETRA-SDP-MIB", "sdpOperBandwidth"),
        ("TIMETRA-SDP-MIB", "sdpAvailableBandwidth"),
        ("TIMETRA-SDP-MIB", "sdpAdminPathMtu"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveHelloMessageLength"),
        ("TIMETRA-SDP-MIB", "sdpNetDomainName"),
        ("TIMETRA-SDP-MIB", "sdpEgressIfsNetDomainConsistent"),
        ("TIMETRA-SDP-MIB", "sdpBgpTunnelEnabled"),
        ("TIMETRA-SDP-MIB", "sdpBgpTunnelLspId"))
)
if mibBuilder.loadTexts:
    tmnxSdpV13v0Group.setStatus("obsolete")

tmnxSdpObsoletedObjsV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 538)
)
tmnxSdpObsoletedObjsV13v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpFarEndIpAddress"),
        ("TIMETRA-SDP-MIB", "sdpTunnelFarEndIpAddress"))
)
if mibBuilder.loadTexts:
    tmnxSdpObsoletedObjsV13v0Group.setStatus("current")

sdpBgpEvpnMplsMhGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 539)
)
sdpBgpEvpnMplsMhGroup.setObjects(
    ("TIMETRA-SDP-MIB", "sdpEvpnMHEthSegName")
)
if mibBuilder.loadTexts:
    sdpBgpEvpnMplsMhGroup.setStatus("current")

sdpGreExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 540)
)
sdpGreExtGroup.setObjects(
    ("TIMETRA-SDP-MIB", "sdpGreAllowFragmentation")
)
if mibBuilder.loadTexts:
    sdpGreExtGroup.setStatus("current")

svcPwTmplExt14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 541)
)
svcPwTmplExt14v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "pwTemplatePreferProvSdp")
)
if mibBuilder.loadTexts:
    svcPwTmplExt14v0Group.setStatus("current")

tmnxSdpBindV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 543)
)
tmnxSdpBindV14v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindExtTableLastChanged"),
        ("TIMETRA-SDP-MIB", "sdpBindExtEntropyLabel"),
        ("TIMETRA-SDP-MIB", "sdpBindExtLastMgmtChange"),
        ("TIMETRA-SDP-MIB", "pwTemplateEntropyLabel"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindV14v0Group.setStatus("current")

tmnxSdpSegRouteTeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 544)
)
tmnxSdpSegRouteTeGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpSegRouteTeOperInstId"),
        ("TIMETRA-SDP-MIB", "sdpSegRouteTeLspRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpSegRouteTeLspLastChanged"),
        ("TIMETRA-SDP-MIB", "sdpSegRouteTeLspTableLastChgd"))
)
if mibBuilder.loadTexts:
    tmnxSdpSegRouteTeGroup.setStatus("current")

tmnxSdpFlowSPecObsoletedV14v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 545)
)
tmnxSdpFlowSPecObsoletedV14v0Grp.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindIngressFlowspec"),
        ("TIMETRA-SDP-MIB", "sdpBindIngressIPv6Flowspec"))
)
if mibBuilder.loadTexts:
    tmnxSdpFlowSPecObsoletedV14v0Grp.setStatus("current")

tmnxSdpBindObsoletedV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 546)
)
tmnxSdpBindObsoletedV13v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindIngressVlanTranslation"),
        ("TIMETRA-SDP-MIB", "sdpBindIngressVlanTranslationId"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindObsoletedV13v0Group.setStatus("current")

sdpPwStaticLabelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 547)
)
sdpPwStaticLabelGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpPwPortIngVcLabel"),
        ("TIMETRA-SDP-MIB", "sdpPwPortEgrVcLabel"))
)
if mibBuilder.loadTexts:
    sdpPwStaticLabelGroup.setStatus("current")

sdpBindV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 548)
)
sdpBindV14v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpBindMinReqdSdpOperMtu")
)
if mibBuilder.loadTexts:
    sdpBindV14v0Group.setStatus("current")

sdpBindTlsV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 549)
)
sdpBindTlsV14v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpBindDisableSendBvplsEvpnFlush")
)
if mibBuilder.loadTexts:
    sdpBindTlsV14v0Group.setStatus("current")

sdpFpeV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 550)
)
sdpFpeV14v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpFpeLspId")
)
if mibBuilder.loadTexts:
    sdpFpeV14v0Group.setStatus("current")

sdpBindBgpEvpnAlmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 551)
)
sdpBindBgpEvpnAlmpGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindTlsRestProtSrcMacOper"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsRestProtSrcMacOperAct"),
        ("TIMETRA-SDP-MIB", "sdpBindMeshTlsRPSMacOper"),
        ("TIMETRA-SDP-MIB", "sdpBindMeshTlsRPSMacOperAct"))
)
if mibBuilder.loadTexts:
    sdpBindBgpEvpnAlmpGroup.setStatus("current")

tmnxSdpMplsLspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 552)
)
tmnxSdpMplsLspGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpMplsLspRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpMplsLspLastChanged"),
        ("TIMETRA-SDP-MIB", "sdpMplsLspTableLastChgd"))
)
if mibBuilder.loadTexts:
    tmnxSdpMplsLspGroup.setStatus("current")

tmnxSdpCfmLmmPerQosV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 553)
)
tmnxSdpCfmLmmPerQosV15v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindEthCfmCollLmmFcSts"),
        ("TIMETRA-SDP-MIB", "sdpBindEthCfmCollLmmFcStsInP"))
)
if mibBuilder.loadTexts:
    tmnxSdpCfmLmmPerQosV15v0Group.setStatus("current")

tmnxObsoletedSdpV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 554)
)
tmnxObsoletedSdpV15v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpLspList")
)
if mibBuilder.loadTexts:
    tmnxObsoletedSdpV15v0Group.setStatus("current")

tmnxSdpV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 555)
)
tmnxSdpV15v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindCreatOrigin"),
        ("TIMETRA-SDP-MIB", "sdpNumEntries"),
        ("TIMETRA-SDP-MIB", "sdpNextFreeId"),
        ("TIMETRA-SDP-MIB", "sdpId"),
        ("TIMETRA-SDP-MIB", "sdpRowStatus"),
        ("TIMETRA-SDP-MIB", "sdpDelivery"),
        ("TIMETRA-SDP-MIB", "sdpDescription"),
        ("TIMETRA-SDP-MIB", "sdpLabelSignaling"),
        ("TIMETRA-SDP-MIB", "sdpAdminStatus"),
        ("TIMETRA-SDP-MIB", "sdpOperStatus"),
        ("TIMETRA-SDP-MIB", "sdpOperPathMtu"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveAdminStatus"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveOperStatus"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveHelloTime"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveMaxDropCount"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveHoldDownTime"),
        ("TIMETRA-SDP-MIB", "sdpLastMgmtChange"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveNumHelloRequestMessages"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveNumHelloResponseMessages"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveNumLateHelloResponseMessages"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveHelloRequestTimeout"),
        ("TIMETRA-SDP-MIB", "sdpLdpEnabled"),
        ("TIMETRA-SDP-MIB", "sdpVlanVcEtype"),
        ("TIMETRA-SDP-MIB", "sdpAdvertisedVllMtuOverride"),
        ("TIMETRA-SDP-MIB", "sdpOperFlags"),
        ("TIMETRA-SDP-MIB", "sdpLastStatusChange"),
        ("TIMETRA-SDP-MIB", "sdpMvplsMgmtService"),
        ("TIMETRA-SDP-MIB", "sdpMvplsMgmtSdpBndId"),
        ("TIMETRA-SDP-MIB", "sdpCollectAcctStats"),
        ("TIMETRA-SDP-MIB", "sdpAccountingPolicyId"),
        ("TIMETRA-SDP-MIB", "sdpClassFwdingEnabled"),
        ("TIMETRA-SDP-MIB", "sdpClassFwdingDefaultLsp"),
        ("TIMETRA-SDP-MIB", "sdpClassFwdingMcLsp"),
        ("TIMETRA-SDP-MIB", "sdpMetric"),
        ("TIMETRA-SDP-MIB", "sdpAutoSdp"),
        ("TIMETRA-SDP-MIB", "sdpPBBEtype"),
        ("TIMETRA-SDP-MIB", "sdpBandwidthBookingFactor"),
        ("TIMETRA-SDP-MIB", "sdpOperBandwidth"),
        ("TIMETRA-SDP-MIB", "sdpAvailableBandwidth"),
        ("TIMETRA-SDP-MIB", "sdpAdminPathMtu"),
        ("TIMETRA-SDP-MIB", "sdpKeepAliveHelloMessageLength"),
        ("TIMETRA-SDP-MIB", "sdpNetDomainName"),
        ("TIMETRA-SDP-MIB", "sdpEgressIfsNetDomainConsistent"),
        ("TIMETRA-SDP-MIB", "sdpBgpTunnelEnabled"),
        ("TIMETRA-SDP-MIB", "sdpBgpTunnelLspId"))
)
if mibBuilder.loadTexts:
    tmnxSdpV15v0Group.setStatus("current")

tmnxSdpWeightedLoadBalanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 556)
)
tmnxSdpWeightedLoadBalanceGroup.setObjects(
    ("TIMETRA-SDP-MIB", "sdpWeightedEcmpEnabled")
)
if mibBuilder.loadTexts:
    tmnxSdpWeightedLoadBalanceGroup.setStatus("current")

sdpEvpnMhEthSegV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 557)
)
sdpEvpnMhEthSegV15v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpEvpnMHEthSegStatus")
)
if mibBuilder.loadTexts:
    sdpEvpnMhEthSegV15v0Group.setStatus("current")

tmnxPwTempNameV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 558)
)
tmnxPwTempNameV15v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "pwTemplateName")
)
if mibBuilder.loadTexts:
    tmnxPwTempNameV15v0Group.setStatus("current")

sdpOperTunnelFarEndGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 559)
)
sdpOperTunnelFarEndGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpOperTunnelFarEndInetAddrType"),
        ("TIMETRA-SDP-MIB", "sdpOperTunnelFarEndInetAddr"))
)
if mibBuilder.loadTexts:
    sdpOperTunnelFarEndGroup.setStatus("current")

pwTemplateGreGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 560)
)
pwTemplateGreGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "pwTemplateGreDelivery"),
        ("TIMETRA-SDP-MIB", "pwTemplateAugGreAllowFrag"))
)
if mibBuilder.loadTexts:
    pwTemplateGreGroup.setStatus("current")

pwTemplateQosV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 561)
)
pwTemplateQosV16v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "pwTemplateIngQoSNetworkPlcyName"),
        ("TIMETRA-SDP-MIB", "pwTemplateEgrQoSNetworkPlcyName"))
)
if mibBuilder.loadTexts:
    pwTemplateQosV16v0Group.setStatus("current")

pwTemplateFilterNameV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 562)
)
pwTemplateFilterNameV16v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "pwTemplateIngressIpFilterName"),
        ("TIMETRA-SDP-MIB", "pwTemplateIngressIpv6FilterName"),
        ("TIMETRA-SDP-MIB", "pwTemplateIngressMacFilterName"),
        ("TIMETRA-SDP-MIB", "pwTemplateEgressIpFilterName"),
        ("TIMETRA-SDP-MIB", "pwTemplateEgressIpv6FilterName"),
        ("TIMETRA-SDP-MIB", "pwTemplateEgressMacFilterName"))
)
if mibBuilder.loadTexts:
    pwTemplateFilterNameV16v0Group.setStatus("current")

tmnxSdpBindQinqV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 564)
)
tmnxSdpBindQinqV16v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindForceQinqVcFwding"),
        ("TIMETRA-SDP-MIB", "pwTemplateForceQinqVcFwding"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindQinqV16v0Group.setStatus("current")

tmnxSdpBindV16v0ObsoletedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 565)
)
tmnxSdpBindV16v0ObsoletedGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindForceQinqVcForwarding"),
        ("TIMETRA-SDP-MIB", "pwTemplateForceQinqVcForwarding"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindV16v0ObsoletedGroup.setStatus("current")

sdpPwPortControlWordGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 566)
)
sdpPwPortControlWordGroup.setObjects(
    ("TIMETRA-SDP-MIB", "sdpPwPortControlWord")
)
if mibBuilder.loadTexts:
    sdpPwPortControlWordGroup.setStatus("current")

pwTemplateNgeAutoBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 567)
)
pwTemplateNgeAutoBindGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "pwTemplateAugAluNgeKeyGroupIn"),
        ("TIMETRA-SDP-MIB", "pwTemplateAugAluNgeKeyGroupOut"))
)
if mibBuilder.loadTexts:
    pwTemplateNgeAutoBindGroup.setStatus("current")

sdpBindMcastSrcV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 568)
)
sdpBindMcastSrcV19v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpBindMulticastSource")
)
if mibBuilder.loadTexts:
    sdpBindMcastSrcV19v0Group.setStatus("current")

sdpBindTlsMacListV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 570)
)
sdpBindTlsMacListV20v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindTlsAutoLrnMacPrtExcList"),
        ("TIMETRA-SDP-MIB", "sdpBindMeshTlsAutLrnMacPrtExcLs"),
        ("TIMETRA-SDP-MIB", "pwTemplateAugAtLnMacPrtExcList"))
)
if mibBuilder.loadTexts:
    sdpBindTlsMacListV20v0Group.setStatus("current")

sdpBindCfmSquelchInCtagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 571)
)
sdpBindCfmSquelchInCtagGroup.setObjects(
    ("TIMETRA-SDP-MIB", "sdpBindEthCfmSquelchIngressCtag")
)
if mibBuilder.loadTexts:
    sdpBindCfmSquelchInCtagGroup.setStatus("current")

sdpBindVccvBfdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 572)
)
sdpBindVccvBfdGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindExtBfdFailAction"),
        ("TIMETRA-SDP-MIB", "sdpBindExtBfdSessStatOperState"),
        ("TIMETRA-SDP-MIB", "sdpBindExtBfdWaitForUpTimer"),
        ("TIMETRA-SDP-MIB", "sdpBindExtBfdUpTimeRemain"))
)
if mibBuilder.loadTexts:
    sdpBindVccvBfdGroup.setStatus("current")

sdpBindSvcMtuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 573)
)
sdpBindSvcMtuGroup.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindExt2LastMgmtChange"),
        ("TIMETRA-SDP-MIB", "sdpBindExt2AdvSvcMtu"),
        ("TIMETRA-SDP-MIB", "sdpBindExt2TableLastChgd"))
)
if mibBuilder.loadTexts:
    sdpBindSvcMtuGroup.setStatus("current")

sdpPwPortEntropyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 574)
)
sdpPwPortEntropyGroup.setObjects(
    ("TIMETRA-SDP-MIB", "sdpPwPortEntropyLabel")
)
if mibBuilder.loadTexts:
    sdpPwPortEntropyGroup.setStatus("current")

sdpLastChangeV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 575)
)
sdpLastChangeV21v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindTableLastChanged"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsTableLastChanged"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsLastMgmtChange"))
)
if mibBuilder.loadTexts:
    sdpLastChangeV21v0Group.setStatus("current")

sdpPwPortSvcMtuV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 576)
)
sdpPwPortSvcMtuV21v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpPwPortAdvSvcMtu")
)
if mibBuilder.loadTexts:
    sdpPwPortSvcMtuV21v0Group.setStatus("current")


# Notification objects

sdpCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 1)
)
sdpCreated.setObjects(
    ("TIMETRA-SDP-MIB", "sdpId")
)
if mibBuilder.loadTexts:
    sdpCreated.setStatus(
        "obsolete"
    )

sdpDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 2)
)
sdpDeleted.setObjects(
    ("TIMETRA-SDP-MIB", "sdpId")
)
if mibBuilder.loadTexts:
    sdpDeleted.setStatus(
        "obsolete"
    )

sdpStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 3)
)
sdpStatusChanged.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpId"),
        ("TIMETRA-SDP-MIB", "sdpAdminStatus"),
        ("TIMETRA-SDP-MIB", "sdpOperStatus"))
)
if mibBuilder.loadTexts:
    sdpStatusChanged.setStatus(
        "current"
    )

sdpBindCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 4)
)
sdpBindCreated.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"))
)
if mibBuilder.loadTexts:
    sdpBindCreated.setStatus(
        "obsolete"
    )

sdpBindDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 5)
)
sdpBindDeleted.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"))
)
if mibBuilder.loadTexts:
    sdpBindDeleted.setStatus(
        "obsolete"
    )

sdpBindStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 6)
)
sdpBindStatusChanged.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SDP-MIB", "sdpBindAdminStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindOperStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindOperFlags"))
)
if mibBuilder.loadTexts:
    sdpBindStatusChanged.setStatus(
        "current"
    )

sdpTlsMacAddrLimitAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 7)
)
sdpTlsMacAddrLimitAlarmRaised.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"))
)
if mibBuilder.loadTexts:
    sdpTlsMacAddrLimitAlarmRaised.setStatus(
        "current"
    )

sdpTlsMacAddrLimitAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 8)
)
sdpTlsMacAddrLimitAlarmCleared.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"))
)
if mibBuilder.loadTexts:
    sdpTlsMacAddrLimitAlarmCleared.setStatus(
        "current"
    )

sdpTlsDHCPSuspiciousPcktRcvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 9)
)
sdpTlsDHCPSuspiciousPcktRcvd.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpId"),
        ("TIMETRA-SERV-MIB", "tlsDhcpPacketProblem"))
)
if mibBuilder.loadTexts:
    sdpTlsDHCPSuspiciousPcktRcvd.setStatus(
        "obsolete"
    )

sdpBindDHCPLeaseEntriesExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 10)
)
sdpBindDHCPLeaseEntriesExceeded.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateNewCiAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateNewChAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpClientLease"))
)
if mibBuilder.loadTexts:
    sdpBindDHCPLeaseEntriesExceeded.setStatus(
        "current"
    )

sdpBindDHCPLseStateOverride = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 11)
)
sdpBindDHCPLseStateOverride.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateNewCiAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateNewChAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateOldCiAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateOldChAddr"))
)
if mibBuilder.loadTexts:
    sdpBindDHCPLseStateOverride.setStatus(
        "current"
    )

sdpBindDHCPSuspiciousPcktRcvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 12)
)
sdpBindDHCPSuspiciousPcktRcvd.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SERV-MIB", "svcDhcpPacketProblem"))
)
if mibBuilder.loadTexts:
    sdpBindDHCPSuspiciousPcktRcvd.setStatus(
        "current"
    )

sdpBindDHCPLseStatePopulateErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 13)
)
sdpBindDHCPLseStatePopulateErr.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePopulateError"))
)
if mibBuilder.loadTexts:
    sdpBindDHCPLseStatePopulateErr.setStatus(
        "current"
    )

sdpBindPwPeerStatusBitsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 14)
)
sdpBindPwPeerStatusBitsChanged.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SDP-MIB", "sdpBindPwPeerStatusBits"))
)
if mibBuilder.loadTexts:
    sdpBindPwPeerStatusBitsChanged.setStatus(
        "current"
    )

sdpBindTlsMacMoveExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 15)
)
sdpBindTlsMacMoveExceeded.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SDP-MIB", "sdpBindAdminStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindOperStatus"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMacMoveRateExcdLeft"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMacMoveNextUpTime"),
        ("TIMETRA-SERV-MIB", "svcTlsMacMoveMaxRate"),
        ("TIMETRA-SDP-MIB", "sdpBindNotifyMacAddr"))
)
if mibBuilder.loadTexts:
    sdpBindTlsMacMoveExceeded.setStatus(
        "current"
    )

sdpBindPwPeerFaultAddrChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 16)
)
sdpBindPwPeerFaultAddrChanged.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SDP-MIB", "sdpBindPwFaultInetAddressType"),
        ("TIMETRA-SDP-MIB", "sdpBindPwFaultInetAddress"))
)
if mibBuilder.loadTexts:
    sdpBindPwPeerFaultAddrChanged.setStatus(
        "current"
    )

sdpBindDHCPProxyServerError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 17)
)
sdpBindDHCPProxyServerError.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SERV-MIB", "svcDhcpProxyError"))
)
if mibBuilder.loadTexts:
    sdpBindDHCPProxyServerError.setStatus(
        "current"
    )

sdpBindDHCPCoAError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 18)
)
sdpBindDHCPCoAError.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SERV-MIB", "svcDhcpCoAError"))
)
if mibBuilder.loadTexts:
    sdpBindDHCPCoAError.setStatus(
        "obsolete"
    )

sdpBindDHCPSubAuthError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 19)
)
sdpBindDHCPSubAuthError.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SERV-MIB", "svcDhcpSubAuthError"))
)
if mibBuilder.loadTexts:
    sdpBindDHCPSubAuthError.setStatus(
        "obsolete"
    )

sdpBindSdpStateChangeProcessed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 20)
)
sdpBindSdpStateChangeProcessed.setObjects(
    ("TIMETRA-SDP-MIB", "sdpNotifySdpId")
)
if mibBuilder.loadTexts:
    sdpBindSdpStateChangeProcessed.setStatus(
        "current"
    )

sdpBindDHCPLseStateMobilityErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 21)
)
sdpBindDHCPLseStateMobilityErr.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePopulateError"))
)
if mibBuilder.loadTexts:
    sdpBindDHCPLseStateMobilityErr.setStatus(
        "current"
    )

sdpBandwidthOverbooked = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 22)
)
sdpBandwidthOverbooked.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpId"),
        ("TIMETRA-SDP-MIB", "sdpMaxBookableBandwidth"),
        ("TIMETRA-SDP-MIB", "sdpBookedBandwidth"))
)
if mibBuilder.loadTexts:
    sdpBandwidthOverbooked.setStatus(
        "current"
    )

sdpBindInsufficientBandwidth = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 23)
)
sdpBindInsufficientBandwidth.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SDP-MIB", "sdpAvailableBandwidth"),
        ("TIMETRA-SDP-MIB", "sdpBindAdminBandwidth"))
)
if mibBuilder.loadTexts:
    sdpBindInsufficientBandwidth.setStatus(
        "current"
    )

dynamicSdpConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 24)
)
dynamicSdpConfigChanged.setObjects(
      *(("TIMETRA-SDP-MIB", "dynamicSdpOrigin"),
        ("TIMETRA-SDP-MIB", "sdpId"),
        ("TIMETRA-SDP-MIB", "svcL2RteSdpBindId"),
        ("TIMETRA-SDP-MIB", "dynamicSdpStatus"))
)
if mibBuilder.loadTexts:
    dynamicSdpConfigChanged.setStatus(
        "current"
    )

dynamicSdpBindConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 25)
)
dynamicSdpBindConfigChanged.setObjects(
      *(("TIMETRA-SDP-MIB", "dynamicSdpOrigin"),
        ("TIMETRA-SDP-MIB", "sdpId"),
        ("TIMETRA-SDP-MIB", "svcL2RteSdpBindId"),
        ("TIMETRA-SDP-MIB", "dynamicSdpStatus"),
        ("TIMETRA-SDP-MIB", "sdpMSPwPeId"))
)
if mibBuilder.loadTexts:
    dynamicSdpBindConfigChanged.setStatus(
        "current"
    )

dynamicSdpCreationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 26)
)
dynamicSdpCreationFailed.setObjects(
      *(("TIMETRA-SDP-MIB", "svcL2RteSdpBindId"),
        ("TIMETRA-SDP-MIB", "dynamicSdpOrigin"),
        ("TIMETRA-SDP-MIB", "dynamicSdpCreationError"))
)
if mibBuilder.loadTexts:
    dynamicSdpCreationFailed.setStatus(
        "current"
    )

dynamicSdpBindCreationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 27)
)
dynamicSdpBindCreationFailed.setObjects(
      *(("TIMETRA-SDP-MIB", "svcL2RteSdpBindId"),
        ("TIMETRA-SDP-MIB", "dynamicSdpOrigin"),
        ("TIMETRA-SDP-MIB", "sdpId"),
        ("TIMETRA-SDP-MIB", "pwTemplateLastChanged"),
        ("TIMETRA-SDP-MIB", "dynamicSdpBindCreationError"))
)
if mibBuilder.loadTexts:
    dynamicSdpBindCreationFailed.setStatus(
        "current"
    )

sdpEgrIfsNetDomInconsCntChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 28)
)
sdpEgrIfsNetDomInconsCntChanged.setObjects(
    ("TIMETRA-SDP-MIB", "sdpEgIfNetDomainInconsCount")
)
if mibBuilder.loadTexts:
    sdpEgrIfsNetDomInconsCntChanged.setStatus(
        "current"
    )

sdpBindIpipeCeIpAddressChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 29)
)
sdpBindIpipeCeIpAddressChange.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SDP-MIB", "sdpBindIpipeCeIpAddrType"),
        ("TIMETRA-SDP-MIB", "sdpBindIpipeCeIpAddress"))
)
if mibBuilder.loadTexts:
    sdpBindIpipeCeIpAddressChange.setStatus(
        "current"
    )

sdpBindReceivedProtSrcMac = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 30)
)
sdpBindReceivedProtSrcMac.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SERV-MIB", "protectedMacForNotify"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsRestProtSrcMacAction"))
)
if mibBuilder.loadTexts:
    sdpBindReceivedProtSrcMac.setStatus(
        "current"
    )

sdpBindPwLocalStatusBitsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 31)
)
sdpBindPwLocalStatusBitsChanged.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SDP-MIB", "sdpBindPwLocalStatusBits"))
)
if mibBuilder.loadTexts:
    sdpBindPwLocalStatusBitsChanged.setStatus(
        "current"
    )

sdpBindTlsMacMoveExceedNonBlock = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 32)
)
sdpBindTlsMacMoveExceedNonBlock.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SERV-MIB", "svcTlsMacMoveMaxRate"),
        ("TIMETRA-SDP-MIB", "sdpBindNotifyMacAddr"))
)
if mibBuilder.loadTexts:
    sdpBindTlsMacMoveExceedNonBlock.setStatus(
        "current"
    )

sdpBindEthLoopbackStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 33)
)
sdpBindEthLoopbackStarted.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindEthLoopbackMode"),
        ("TIMETRA-SDP-MIB", "sdpBindEthLoopbackMacSwap"),
        ("TIMETRA-SDP-MIB", "sdpBindEthLoopbackMacSwapAddr"),
        ("TIMETRA-SDP-MIB", "sdpBindEthLoopbackMacSwapAddrAll"))
)
if mibBuilder.loadTexts:
    sdpBindEthLoopbackStarted.setStatus(
        "current"
    )

sdpBindEthLoopbackStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 34)
)
sdpBindEthLoopbackStopped.setObjects(
    ("TIMETRA-SDP-MIB", "sdpBindEthLoopbackMode")
)
if mibBuilder.loadTexts:
    sdpBindEthLoopbackStopped.setStatus(
        "current"
    )

sdpPbbActvPwWithNonActvCtrlPwChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 35)
)
sdpPbbActvPwWithNonActvCtrlPwChg.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpId"),
        ("TIMETRA-SDP-MIB", "sdpPbbActvPwWithNonActvCtrlPw"))
)
if mibBuilder.loadTexts:
    sdpPbbActvPwWithNonActvCtrlPwChg.setStatus(
        "current"
    )

sdpControlPwActiveStateChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 36)
)
sdpControlPwActiveStateChg.setObjects(
    ("TIMETRA-SDP-MIB", "sdpControlPWIsActive")
)
if mibBuilder.loadTexts:
    sdpControlPwActiveStateChg.setStatus(
        "current"
    )

sdpBindReceivedPbbProtSrcMac = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 37)
)
sdpBindReceivedPbbProtSrcMac.setObjects(
      *(("TIMETRA-SERV-MIB", "svcTlsBackboneVplsSvcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SERV-MIB", "protectedMacForNotify"))
)
if mibBuilder.loadTexts:
    sdpBindReceivedPbbProtSrcMac.setStatus(
        "current"
    )

unacknowledgedTCN = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 8)
)
unacknowledgedTCN.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpId"))
)
if mibBuilder.loadTexts:
    unacknowledgedTCN.setStatus(
        "current"
    )

tmnxSvcTopoChgSdpBindMajorState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 14)
)
tmnxSvcTopoChgSdpBindMajorState.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpPortState"),
        ("TIMETRA-SERV-MIB", "tmnxOldSdpBindTlsStpPortState"))
)
if mibBuilder.loadTexts:
    tmnxSvcTopoChgSdpBindMajorState.setStatus(
        "current"
    )

tmnxSvcNewRootSdpBind = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 15)
)
tmnxSvcNewRootSdpBind.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SERV-MIB", "svcTlsStpDesignatedRoot"))
)
if mibBuilder.loadTexts:
    tmnxSvcNewRootSdpBind.setStatus(
        "current"
    )

tmnxSvcTopoChgSdpBindState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 16)
)
tmnxSvcTopoChgSdpBindState.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpPortState"),
        ("TIMETRA-SERV-MIB", "tmnxOldSdpBindTlsStpPortState"))
)
if mibBuilder.loadTexts:
    tmnxSvcTopoChgSdpBindState.setStatus(
        "current"
    )

tmnxSvcSdpBindRcvdTCN = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 17)
)
tmnxSvcSdpBindRcvdTCN.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"))
)
if mibBuilder.loadTexts:
    tmnxSvcSdpBindRcvdTCN.setStatus(
        "current"
    )

tmnxSvcSdpBindRcvdHigherBriPrio = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 18)
)
tmnxSvcSdpBindRcvdHigherBriPrio.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SERV-MIB", "tmnxCustomerBridgeId"),
        ("TIMETRA-SERV-MIB", "tmnxCustomerRootBridgeId"))
)
if mibBuilder.loadTexts:
    tmnxSvcSdpBindRcvdHigherBriPrio.setStatus(
        "current"
    )

tmnxSvcSdpBindEncapPVST = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 19)
)
tmnxSvcSdpBindEncapPVST.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SERV-MIB", "tmnxOtherBridgeId"))
)
if mibBuilder.loadTexts:
    tmnxSvcSdpBindEncapPVST.setStatus(
        "current"
    )

tmnxSvcSdpBindEncapDot1d = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 20)
)
tmnxSvcSdpBindEncapDot1d.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SERV-MIB", "tmnxOtherBridgeId"))
)
if mibBuilder.loadTexts:
    tmnxSvcSdpBindEncapDot1d.setStatus(
        "current"
    )

tmnxSvcSdpActiveProtocolChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 31)
)
tmnxSvcSdpActiveProtocolChange.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpOperProtocol"))
)
if mibBuilder.loadTexts:
    tmnxSvcSdpActiveProtocolChange.setStatus(
        "current"
    )

tmnxStpMeshNotInMstRegion = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 36)
)
tmnxStpMeshNotInMstRegion.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"))
)
if mibBuilder.loadTexts:
    tmnxStpMeshNotInMstRegion.setStatus(
        "current"
    )

tmnxSdpBndStpExcepCondStateChng = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 38)
)
tmnxSdpBndStpExcepCondStateChng.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsStpException"))
)
if mibBuilder.loadTexts:
    tmnxSdpBndStpExcepCondStateChng.setStatus(
        "current"
    )


# Notifications groups

tmnxSdpNotifyV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 400)
)
tmnxSdpNotifyV6v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "unacknowledgedTCN"),
        ("TIMETRA-SDP-MIB", "tmnxSvcTopoChgSdpBindMajorState"),
        ("TIMETRA-SDP-MIB", "tmnxSvcNewRootSdpBind"),
        ("TIMETRA-SDP-MIB", "tmnxSvcTopoChgSdpBindState"),
        ("TIMETRA-SDP-MIB", "tmnxSvcSdpBindRcvdTCN"),
        ("TIMETRA-SDP-MIB", "tmnxSvcSdpBindRcvdHigherBriPrio"),
        ("TIMETRA-SDP-MIB", "tmnxSvcSdpBindEncapPVST"),
        ("TIMETRA-SDP-MIB", "tmnxSvcSdpBindEncapDot1d"),
        ("TIMETRA-SDP-MIB", "tmnxSvcSdpActiveProtocolChange"),
        ("TIMETRA-SDP-MIB", "tmnxStpMeshNotInMstRegion"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBndStpExcepCondStateChng"),
        ("TIMETRA-SDP-MIB", "sdpStatusChanged"),
        ("TIMETRA-SDP-MIB", "sdpBindStatusChanged"),
        ("TIMETRA-SDP-MIB", "sdpTlsMacAddrLimitAlarmRaised"),
        ("TIMETRA-SDP-MIB", "sdpTlsMacAddrLimitAlarmCleared"),
        ("TIMETRA-SDP-MIB", "sdpBindDHCPLeaseEntriesExceeded"),
        ("TIMETRA-SDP-MIB", "sdpBindDHCPLseStateOverride"),
        ("TIMETRA-SDP-MIB", "sdpBindDHCPLseStatePopulateErr"),
        ("TIMETRA-SDP-MIB", "sdpBindDHCPSuspiciousPcktRcvd"),
        ("TIMETRA-SDP-MIB", "sdpBindPwPeerStatusBitsChanged"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMacMoveExceeded"),
        ("TIMETRA-SDP-MIB", "sdpBindPwPeerFaultAddrChanged"),
        ("TIMETRA-SDP-MIB", "sdpBindDHCPProxyServerError"),
        ("TIMETRA-SDP-MIB", "sdpBindSdpStateChangeProcessed"),
        ("TIMETRA-SDP-MIB", "sdpBindDHCPLseStateMobilityErr"),
        ("TIMETRA-SDP-MIB", "sdpBandwidthOverbooked"),
        ("TIMETRA-SDP-MIB", "sdpBindInsufficientBandwidth"),
        ("TIMETRA-SDP-MIB", "dynamicSdpConfigChanged"),
        ("TIMETRA-SDP-MIB", "dynamicSdpBindConfigChanged"),
        ("TIMETRA-SDP-MIB", "dynamicSdpCreationFailed"),
        ("TIMETRA-SDP-MIB", "dynamicSdpBindCreationFailed"))
)
if mibBuilder.loadTexts:
    tmnxSdpNotifyV6v0Group.setStatus(
        "current"
    )

tmnxSdpObsoletedNotifyV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 401)
)
tmnxSdpObsoletedNotifyV6v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpCreated"),
        ("TIMETRA-SDP-MIB", "sdpDeleted"),
        ("TIMETRA-SDP-MIB", "sdpBindCreated"),
        ("TIMETRA-SDP-MIB", "sdpBindDeleted"),
        ("TIMETRA-SDP-MIB", "sdpTlsDHCPSuspiciousPcktRcvd"),
        ("TIMETRA-SDP-MIB", "sdpBindDHCPCoAError"),
        ("TIMETRA-SDP-MIB", "sdpBindDHCPSubAuthError"))
)
if mibBuilder.loadTexts:
    tmnxSdpObsoletedNotifyV6v0Group.setStatus(
        "current"
    )

tmnxSdpNotifyV8v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 402)
)
tmnxSdpNotifyV8v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpEgrIfsNetDomInconsCntChanged")
)
if mibBuilder.loadTexts:
    tmnxSdpNotifyV8v0Group.setStatus(
        "current"
    )

tmnxSdpBindIpipeNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 403)
)
tmnxSdpBindIpipeNotifyGroup.setObjects(
    ("TIMETRA-SDP-MIB", "sdpBindIpipeCeIpAddressChange")
)
if mibBuilder.loadTexts:
    tmnxSdpBindIpipeNotifyGroup.setStatus(
        "current"
    )

tmnxSdpNotifyV10v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 404)
)
tmnxSdpNotifyV10v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindPwLocalStatusBitsChanged"),
        ("TIMETRA-SDP-MIB", "sdpBindReceivedProtSrcMac"))
)
if mibBuilder.loadTexts:
    tmnxSdpNotifyV10v0Group.setStatus(
        "current"
    )

tmnxSdpNotifyV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 405)
)
tmnxSdpNotifyV11v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpBindTlsMacMoveExceedNonBlock")
)
if mibBuilder.loadTexts:
    tmnxSdpNotifyV11v0Group.setStatus(
        "current"
    )

tmnxSdpBindEthLpbkNtfyV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 508)
)
tmnxSdpBindEthLpbkNtfyV11v0Group.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindEthLoopbackStarted"),
        ("TIMETRA-SDP-MIB", "sdpBindEthLoopbackStopped"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindEthLpbkNtfyV11v0Group.setStatus(
        "current"
    )

tmnxSdpPbbEpipeNotifV12v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 521)
)
tmnxSdpPbbEpipeNotifV12v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpPbbActvPwWithNonActvCtrlPwChg")
)
if mibBuilder.loadTexts:
    tmnxSdpPbbEpipeNotifV12v0Group.setStatus(
        "current"
    )

tmnxSdpCtrlPwNotifV12v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 531)
)
tmnxSdpCtrlPwNotifV12v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpControlPwActiveStateChg")
)
if mibBuilder.loadTexts:
    tmnxSdpCtrlPwNotifV12v0Group.setStatus(
        "current"
    )

sdpNotifyV20v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 569)
)
sdpNotifyV20v0Group.setObjects(
    ("TIMETRA-SDP-MIB", "sdpBindReceivedPbbProtSrcMac")
)
if mibBuilder.loadTexts:
    sdpNotifyV20v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxSdp77x0V6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 10)
)
tmnxSdp77x0V6v1Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "tmnxSdpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpApipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV6v1Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpipeV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSdp77x0V6v1Compliance.setStatus(
        "obsolete"
    )

tmnxSdp7450V6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 11)
)
tmnxSdp7450V6v1Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "tmnxSdpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV6v1Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSdp7450V6v1Compliance.setStatus(
        "obsolete"
    )

tmnxSdp77x0V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 12)
)
tmnxSdp77x0V7v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "tmnxSdpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpApipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpEvalPwTempV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindGenGroup"))
)
if mibBuilder.loadTexts:
    tmnxSdp77x0V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxSdp7450V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 13)
)
tmnxSdp7450V7v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "tmnxSdpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpEvalPwTempV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindGenGroup"))
)
if mibBuilder.loadTexts:
    tmnxSdp7450V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxSdp77x0V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 14)
)
tmnxSdp77x0V8v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "tmnxSdpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpApipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpEvalPwTempV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindGenGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpLdpBackupV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBgpVplsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtGroup"))
)
if mibBuilder.loadTexts:
    tmnxSdp77x0V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxSdp7450V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 15)
)
tmnxSdp7450V8v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "tmnxSdpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpEvalPwTempV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindGenGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpLdpBackupV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBgpVplsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtGroup"))
)
if mibBuilder.loadTexts:
    tmnxSdp7450V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxSdp77x0V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 16)
)
tmnxSdp77x0V9v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "tmnxSdpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpApipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpEvalPwTempV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindGenGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBgpVplsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpMixedLspModeV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthCfmGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeNotifyGroup"))
)
if mibBuilder.loadTexts:
    tmnxSdp77x0V9v0Compliance.setStatus(
        "obsolete"
    )

tmnxSdp7450V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 17)
)
tmnxSdp7450V9v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "tmnxSdpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpEvalPwTempV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindGenGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBgpVplsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpMixedLspModeV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthCfmGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeNotifyGroup"))
)
if mibBuilder.loadTexts:
    tmnxSdp7450V9v0Compliance.setStatus(
        "obsolete"
    )

tmnxSdp77x0V10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 18)
)
tmnxSdp77x0V10v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "tmnxSdpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpApipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpEvalPwTempV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindGenGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBgpVplsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpMixedLspModeV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthCfmGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeNotifyGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwPortGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSpbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBlockOnPeerFaultGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSdp77x0V10v0Compliance.setStatus(
        "obsolete"
    )

tmnxSdp7450V10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 19)
)
tmnxSdp7450V10v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "tmnxSdpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpEvalPwTempV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindGenGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBgpVplsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpMixedLspModeV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthCfmGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeNotifyGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwPortGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSpbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBlockOnPeerFaultGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindQGrpObjsV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSdp7450V10v0Compliance.setStatus(
        "obsolete"
    )

tmnxSdp77x0V11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 20)
)
tmnxSdp77x0V11v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "tmnxSdpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpApipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpEvalPwTempV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindGenGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBgpVplsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpMixedLspModeV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthCfmGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeNotifyGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwPortV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSpbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpGrpGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBlockOnPeerFaultGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindPwPortGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpVllBgpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindSpbV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindFlowSpecGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwSecShaperGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLoopbackV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLpbkNtfyV11v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsFdbMacStatsGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanReqGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanAckGroup"))
)
if mibBuilder.loadTexts:
    tmnxSdp77x0V11v0Compliance.setStatus(
        "obsolete"
    )

tmnxSdp7450V11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 21)
)
tmnxSdp7450V11v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "tmnxSdpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpEvalPwTempV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindGenGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBgpVplsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpMixedLspModeV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthCfmGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeNotifyGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwPortV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSpbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindQGrpObjsV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpGrpGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBlockOnPeerFaultGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindPwPortGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpVllBgpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2tpv3Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindSpbV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindFlowSpecGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwSecShaperGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLoopbackV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLpbkNtfyV11v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsFdbMacStatsGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanReqGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanAckGroup"))
)
if mibBuilder.loadTexts:
    tmnxSdp7450V11v0Compliance.setStatus(
        "obsolete"
    )

tmnxSdp77x0V12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 22)
)
tmnxSdp77x0V12v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "tmnxSdpV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpApipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpEvalPwTempV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindGenGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBgpVplsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpMixedLspModeV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthCfmGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeNotifyGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwPortV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSpbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpGrpGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBlockOnPeerFaultGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindPwPortGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpVllBgpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindSpbV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindFlowSpecGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwSecShaperGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLoopbackV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLpbkNtfyV11v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsFdbMacStatsGroup"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsEtreeGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanReqGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanAckGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPBBEpipePWRedV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbEpipeNotifyObjsGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbEpipeNotifV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthCfmV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBfdV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2tpv3CookieGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwTempBindV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwLoopbackGroup"),
        ("TIMETRA-SDP-MIB", "tmnxPwTemplateAugGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpCtrlPwNotifV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSdp77x0V12v0Compliance.setStatus(
        "obsolete"
    )

tmnxSdp7450V12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 23)
)
tmnxSdp7450V12v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "tmnxSdpV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpEvalPwTempV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindGenGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBgpVplsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpMixedLspModeV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthCfmGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeNotifyGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwPortV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSpbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindQGrpObjsV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpGrpGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBlockOnPeerFaultGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindPwPortGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpVllBgpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2tpv3Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindSpbV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindFlowSpecGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwSecShaperGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLoopbackV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLpbkNtfyV11v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsFdbMacStatsGroup"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsEtreeGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanReqGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanAckGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPBBEpipePWRedV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbEpipeNotifyObjsGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbEpipeNotifV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2tpv3CookieGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwTempBindV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwLoopbackGroup"),
        ("TIMETRA-SDP-MIB", "tmnxPwTemplateAugGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpCtrlPwNotifV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSdp7450V12v0Compliance.setStatus(
        "obsolete"
    )

tmnxSdp77x0V13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 24)
)
tmnxSdp77x0V13v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "tmnxSdpV13v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpApipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpEvalPwTempV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindGenGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBgpVplsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpMixedLspModeV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthCfmGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeNotifyGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwPortV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSpbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpGrpGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBlockOnPeerFaultGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindPwPortGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpVllBgpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindSpbV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindFlowSpecGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwSecShaperGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLoopbackV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLpbkNtfyV11v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsFdbMacStatsGroup"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsEtreeGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanReqGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanAckGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPBBEpipePWRedV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbEpipeNotifyObjsGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbEpipeNotifV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthCfmV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBfdV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2tpv3CookieGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwTempBindV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwLoopbackGroup"),
        ("TIMETRA-SDP-MIB", "tmnxPwTemplateAugGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpCtrlPwNotifV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpLdpIpv6Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV13v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSegRouteGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV13v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBgpEvpnMplsMhGroup"))
)
if mibBuilder.loadTexts:
    tmnxSdp77x0V13v0Compliance.setStatus(
        "obsolete"
    )

tmnxSdp7450V13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 25)
)
tmnxSdp7450V13v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "tmnxSdpV13v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpEvalPwTempV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindGenGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBgpVplsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpMixedLspModeV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthCfmGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeNotifyGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwPortV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSpbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindQGrpObjsV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpGrpGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBlockOnPeerFaultGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindPwPortGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpVllBgpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2tpv3Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindSpbV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindFlowSpecGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwSecShaperGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLoopbackV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLpbkNtfyV11v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsFdbMacStatsGroup"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsEtreeGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanReqGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanAckGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPBBEpipePWRedV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbEpipeNotifyObjsGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbEpipeNotifV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2tpv3CookieGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwTempBindV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwLoopbackGroup"),
        ("TIMETRA-SDP-MIB", "tmnxPwTemplateAugGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpCtrlPwNotifV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpLdpIpv6Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV13v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSegRouteGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwPortOperGrpGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV13v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBgpEvpnMplsMhGroup"),
        ("TIMETRA-SDP-MIB", "sdpGreExtGroup"))
)
if mibBuilder.loadTexts:
    tmnxSdp7450V13v0Compliance.setStatus(
        "obsolete"
    )

tmnxSdp7750V14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 26)
)
tmnxSdp7750V14v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "svcPwTmplExt14v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV14v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV13v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpApipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpEvalPwTempV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindGenGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBgpVplsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpMixedLspModeV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthCfmGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeNotifyGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwPortV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSpbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpGrpGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBlockOnPeerFaultGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindPwPortGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpVllBgpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindSpbV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindFlowSpecGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwSecShaperGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLoopbackV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLpbkNtfyV11v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsFdbMacStatsGroup"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsEtreeGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanReqGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanAckGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPBBEpipePWRedV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbEpipeNotifyObjsGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbEpipeNotifV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthCfmV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBfdV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2tpv3CookieGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwTempBindV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwLoopbackGroup"),
        ("TIMETRA-SDP-MIB", "tmnxPwTemplateAugGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpCtrlPwNotifV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpLdpIpv6Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSegRouteGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV13v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBgpEvpnMplsMhGroup"),
        ("TIMETRA-SDP-MIB", "sdpPwStaticLabelGroup"),
        ("TIMETRA-SDP-MIB", "sdpBindV14v0Group"),
        ("TIMETRA-SDP-MIB", "sdpFpeV14v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBindBgpEvpnAlmpGroup"))
)
if mibBuilder.loadTexts:
    tmnxSdp7750V14v0Compliance.setStatus(
        "obsolete"
    )

tmnxSdp7450V14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 27)
)
tmnxSdp7450V14v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "svcPwTmplExt14v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV14v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSegRouteTeGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV13v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpEvalPwTempV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindGenGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBgpVplsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpMixedLspModeV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthCfmGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeNotifyGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwPortV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSpbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindQGrpObjsV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpGrpGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBlockOnPeerFaultGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindPwPortGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpVllBgpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2tpv3Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindSpbV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindFlowSpecGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwSecShaperGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLoopbackV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLpbkNtfyV11v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsFdbMacStatsGroup"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsEtreeGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanReqGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanAckGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPBBEpipePWRedV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbEpipeNotifyObjsGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbEpipeNotifV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2tpv3CookieGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwTempBindV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwLoopbackGroup"),
        ("TIMETRA-SDP-MIB", "tmnxPwTemplateAugGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpCtrlPwNotifV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpLdpIpv6Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSegRouteGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwPortOperGrpGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV13v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBgpEvpnMplsMhGroup"),
        ("TIMETRA-SDP-MIB", "sdpGreExtGroup"),
        ("TIMETRA-SDP-MIB", "sdpPwStaticLabelGroup"),
        ("TIMETRA-SDP-MIB", "sdpBindV14v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsV14v0Group"),
        ("TIMETRA-SDP-MIB", "sdpFpeV14v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBindBgpEvpnAlmpGroup"))
)
if mibBuilder.loadTexts:
    tmnxSdp7450V14v0Compliance.setStatus(
        "obsolete"
    )

tmnxSdp7750V15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 28)
)
tmnxSdp7750V15v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "tmnxSdpMplsLspGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpCfmLmmPerQosV15v0Group"),
        ("TIMETRA-SDP-MIB", "svcPwTmplExt14v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV14v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpApipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpipeV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpEvalPwTempV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindGenGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBgpVplsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpMixedLspModeV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthCfmGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeNotifyGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwPortV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSpbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpGrpGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBlockOnPeerFaultGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindPwPortGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpVllBgpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindSpbV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindFlowSpecGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwSecShaperGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLoopbackV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLpbkNtfyV11v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsFdbMacStatsGroup"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsEtreeGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanReqGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanAckGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPBBEpipePWRedV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbEpipeNotifyObjsGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbEpipeNotifV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthCfmV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBfdV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2tpv3CookieGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwTempBindV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwLoopbackGroup"),
        ("TIMETRA-SDP-MIB", "tmnxPwTemplateAugGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpCtrlPwNotifV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpLdpIpv6Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSegRouteGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV13v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBgpEvpnMplsMhGroup"),
        ("TIMETRA-SDP-MIB", "sdpPwStaticLabelGroup"),
        ("TIMETRA-SDP-MIB", "sdpBindV14v0Group"),
        ("TIMETRA-SDP-MIB", "sdpFpeV14v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBindBgpEvpnAlmpGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV15v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpWeightedLoadBalanceGroup"),
        ("TIMETRA-SDP-MIB", "sdpEvpnMhEthSegV15v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxPwTempNameV15v0Group"),
        ("TIMETRA-SDP-MIB", "sdpOperTunnelFarEndGroup"))
)
if mibBuilder.loadTexts:
    tmnxSdp7750V15v0Compliance.setStatus(
        "current"
    )

tmnxSdp7450V15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 29)
)
tmnxSdp7450V15v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "tmnxSdpMplsLspGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpCfmLmmPerQosV15v0Group"),
        ("TIMETRA-SDP-MIB", "svcPwTmplExt14v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV14v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSegRouteTeGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindMeshV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsL2ptV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindTlsMrpV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpTlsBgpV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpFCV6v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpEvalPwTempV7v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindGenGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBsxV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpAutoBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBgpVplsV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2V8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindV8v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpMixedLspModeV9v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthCfmGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindIpipeNotifyGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwPortV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSpbGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpNotifyV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindQGrpObjsV10v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpGrpGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindBlockOnPeerFaultGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindPwPortGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpVllBgpV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2tpv3Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindSpbV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindFlowSpecGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwSecShaperGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLoopbackV11v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindEthLpbkNtfyV11v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsFdbMacStatsGroup"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsEtreeGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCpmProtV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanReqGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindCtrlChanAckGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPBBEpipePWRedV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbEpipeNotifyObjsGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPbbEpipeNotifV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpL2tpv3CookieGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwTempBindV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwLoopbackGroup"),
        ("TIMETRA-SDP-MIB", "tmnxPwTemplateAugGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpCtrlPwNotifV12v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpLdpIpv6Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpSegRouteGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpPwPortOperGrpGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindDhcpV13v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBgpEvpnMplsMhGroup"),
        ("TIMETRA-SDP-MIB", "sdpGreExtGroup"),
        ("TIMETRA-SDP-MIB", "sdpPwStaticLabelGroup"),
        ("TIMETRA-SDP-MIB", "sdpBindV14v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsV14v0Group"),
        ("TIMETRA-SDP-MIB", "sdpFpeV14v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBindBgpEvpnAlmpGroup"),
        ("TIMETRA-SDP-MIB", "tmnxSdpV15v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxPwTempNameV15v0Group"),
        ("TIMETRA-SDP-MIB", "sdpOperTunnelFarEndGroup"))
)
if mibBuilder.loadTexts:
    tmnxSdp7450V15v0Compliance.setStatus(
        "current"
    )

tmnxSdp7750V16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 30)
)
tmnxSdp7750V16v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "pwTemplateGreGroup"),
        ("TIMETRA-SDP-MIB", "pwTemplateQosV16v0Group"),
        ("TIMETRA-SDP-MIB", "pwTemplateFilterNameV16v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindQinqV16v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSdp7750V16v0Compliance.setStatus(
        "current"
    )

tmnxSdp7450V16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 31)
)
tmnxSdp7450V16v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "pwTemplateGreGroup"),
        ("TIMETRA-SDP-MIB", "pwTemplateQosV16v0Group"),
        ("TIMETRA-SDP-MIB", "pwTemplateFilterNameV16v0Group"),
        ("TIMETRA-SDP-MIB", "tmnxSdpBindQinqV16v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBindSvcMtuGroup"))
)
if mibBuilder.loadTexts:
    tmnxSdp7450V16v0Compliance.setStatus(
        "current"
    )

tmnxSdpV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 32)
)
tmnxSdpV19v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpPwPortControlWordGroup"),
        ("TIMETRA-SDP-MIB", "pwTemplateNgeAutoBindGroup"),
        ("TIMETRA-SDP-MIB", "sdpBindMcastSrcV19v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSdpV19v0Compliance.setStatus(
        "current"
    )

tmnxSdpV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 33)
)
tmnxSdpV20v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpNotifyV20v0Group"),
        ("TIMETRA-SDP-MIB", "sdpBindTlsMacListV20v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSdpV20v0Compliance.setStatus(
        "current"
    )

tmnxSdpV21v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 34)
)
tmnxSdpV21v0Compliance.setObjects(
      *(("TIMETRA-SDP-MIB", "sdpBindCfmSquelchInCtagGroup"),
        ("TIMETRA-SDP-MIB", "sdpBindVccvBfdGroup"),
        ("TIMETRA-SDP-MIB", "sdpPwPortEntropyGroup"),
        ("TIMETRA-SDP-MIB", "sdpLastChangeV21v0Group"),
        ("TIMETRA-SDP-MIB", "sdpPwPortSvcMtuV21v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSdpV21v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SDP-MIB",
    **{"timetraServicesSdpMIBModule": timetraServicesSdpMIBModule,
       "tmnxSdpConformance": tmnxSdpConformance,
       "tmnxSdpCompliances": tmnxSdpCompliances,
       "tmnxSdp77x0V6v1Compliance": tmnxSdp77x0V6v1Compliance,
       "tmnxSdp7450V6v1Compliance": tmnxSdp7450V6v1Compliance,
       "tmnxSdp77x0V7v0Compliance": tmnxSdp77x0V7v0Compliance,
       "tmnxSdp7450V7v0Compliance": tmnxSdp7450V7v0Compliance,
       "tmnxSdp77x0V8v0Compliance": tmnxSdp77x0V8v0Compliance,
       "tmnxSdp7450V8v0Compliance": tmnxSdp7450V8v0Compliance,
       "tmnxSdp77x0V9v0Compliance": tmnxSdp77x0V9v0Compliance,
       "tmnxSdp7450V9v0Compliance": tmnxSdp7450V9v0Compliance,
       "tmnxSdp77x0V10v0Compliance": tmnxSdp77x0V10v0Compliance,
       "tmnxSdp7450V10v0Compliance": tmnxSdp7450V10v0Compliance,
       "tmnxSdp77x0V11v0Compliance": tmnxSdp77x0V11v0Compliance,
       "tmnxSdp7450V11v0Compliance": tmnxSdp7450V11v0Compliance,
       "tmnxSdp77x0V12v0Compliance": tmnxSdp77x0V12v0Compliance,
       "tmnxSdp7450V12v0Compliance": tmnxSdp7450V12v0Compliance,
       "tmnxSdp77x0V13v0Compliance": tmnxSdp77x0V13v0Compliance,
       "tmnxSdp7450V13v0Compliance": tmnxSdp7450V13v0Compliance,
       "tmnxSdp7750V14v0Compliance": tmnxSdp7750V14v0Compliance,
       "tmnxSdp7450V14v0Compliance": tmnxSdp7450V14v0Compliance,
       "tmnxSdp7750V15v0Compliance": tmnxSdp7750V15v0Compliance,
       "tmnxSdp7450V15v0Compliance": tmnxSdp7450V15v0Compliance,
       "tmnxSdp7750V16v0Compliance": tmnxSdp7750V16v0Compliance,
       "tmnxSdp7450V16v0Compliance": tmnxSdp7450V16v0Compliance,
       "tmnxSdpV19v0Compliance": tmnxSdpV19v0Compliance,
       "tmnxSdpV20v0Compliance": tmnxSdpV20v0Compliance,
       "tmnxSdpV21v0Compliance": tmnxSdpV21v0Compliance,
       "tmnxSdpGroups": tmnxSdpGroups,
       "tmnxSdpV6v0Group": tmnxSdpV6v0Group,
       "tmnxSdpBindV6v0Group": tmnxSdpBindV6v0Group,
       "tmnxSdpBindTlsV6v0Group": tmnxSdpBindTlsV6v0Group,
       "tmnxSdpBindMeshV6v0Group": tmnxSdpBindMeshV6v0Group,
       "tmnxSdpApipeV6v0Group": tmnxSdpApipeV6v0Group,
       "tmnxSdpBindDhcpV6v0Group": tmnxSdpBindDhcpV6v0Group,
       "tmnxSdpBindIpipeV6v0Group": tmnxSdpBindIpipeV6v0Group,
       "tmnxSdpFCV6v0Group": tmnxSdpFCV6v0Group,
       "tmnxSdpBindCpipeV6v0Group": tmnxSdpBindCpipeV6v0Group,
       "tmnxSdpBindTlsL2ptV6v0Group": tmnxSdpBindTlsL2ptV6v0Group,
       "tmnxSdpAutoBindV6v0Group": tmnxSdpAutoBindV6v0Group,
       "tmnxSdpBindTlsMrpV6v0Group": tmnxSdpBindTlsMrpV6v0Group,
       "tmnxSdpTlsBgpV6v0Group": tmnxSdpTlsBgpV6v0Group,
       "tmnxSdpL2V6v0Group": tmnxSdpL2V6v0Group,
       "tmnxSdpAutoBindV6v1Group": tmnxSdpAutoBindV6v1Group,
       "tmnxSdpAutoBindV7v0Group": tmnxSdpAutoBindV7v0Group,
       "tmnxSdpBindIpipeV7v0Group": tmnxSdpBindIpipeV7v0Group,
       "tmnxSdpL2V7v0Group": tmnxSdpL2V7v0Group,
       "tmnxSdpEvalPwTempV7v0Group": tmnxSdpEvalPwTempV7v0Group,
       "tmnxSdpLdpBackupV8v0Group": tmnxSdpLdpBackupV8v0Group,
       "tmnxSdpPbbGroup": tmnxSdpPbbGroup,
       "tmnxSdpBindGenGroup": tmnxSdpBindGenGroup,
       "tmnxSdpBindTlsMrpV8v0Group": tmnxSdpBindTlsMrpV8v0Group,
       "tmnxSdpV8v0Group": tmnxSdpV8v0Group,
       "tmnxSdpBindV8v0Group": tmnxSdpBindV8v0Group,
       "tmnxSdpAutoBindV8v0Group": tmnxSdpAutoBindV8v0Group,
       "tmnxSdpBindIpipeV8v0Group": tmnxSdpBindIpipeV8v0Group,
       "tmnxSdpBindV9v0Group": tmnxSdpBindV9v0Group,
       "tmnxSdpBindCpmProtGroup": tmnxSdpBindCpmProtGroup,
       "tmnxSdpBindBsxV9v0Group": tmnxSdpBindBsxV9v0Group,
       "tmnxSdpBindTlsV8v0Group": tmnxSdpBindTlsV8v0Group,
       "tmnxSdpV9v0Group": tmnxSdpV9v0Group,
       "tmnxSdpMixedLspModeV9v0Group": tmnxSdpMixedLspModeV9v0Group,
       "tmnxSdpSpbGroup": tmnxSdpSpbGroup,
       "tmnxSdpBindBsxV10v0Group": tmnxSdpBindBsxV10v0Group,
       "tmnxSdpPwPortGroup": tmnxSdpPwPortGroup,
       "tmnxSdpV10v0Group": tmnxSdpV10v0Group,
       "tmnxSdpBindDhcpV11v0Group": tmnxSdpBindDhcpV11v0Group,
       "tmnxSdpBindDhcpV13v0Group": tmnxSdpBindDhcpV13v0Group,
       "tmnxSdpNotifyObjsV6v0Group": tmnxSdpNotifyObjsV6v0Group,
       "tmnxSdpNotifyObjsV7v0Group": tmnxSdpNotifyObjsV7v0Group,
       "tmnxSdpNotifyObjsV8v0Group": tmnxSdpNotifyObjsV8v0Group,
       "tmnxSdpBgpVplsV8v0Group": tmnxSdpBgpVplsV8v0Group,
       "tmnxSdpL2V8v0Group": tmnxSdpL2V8v0Group,
       "tmnxSdpPwV8v0Group": tmnxSdpPwV8v0Group,
       "tmnxSdpBindEthCfmGroup": tmnxSdpBindEthCfmGroup,
       "tmnxSdpNotifyObjsV9v0Group": tmnxSdpNotifyObjsV9v0Group,
       "tmnxSdpBindIpipeNotifyObjsGroup": tmnxSdpBindIpipeNotifyObjsGroup,
       "tmnxSdpObsoletedObjsV6v1Group": tmnxSdpObsoletedObjsV6v1Group,
       "tmnxSdpObsoletedObjsV9v0Group": tmnxSdpObsoletedObjsV9v0Group,
       "tmnxSdpBindQGrpObjsV10v0Group": tmnxSdpBindQGrpObjsV10v0Group,
       "tmnxSdpNotifyV6v0Group": tmnxSdpNotifyV6v0Group,
       "tmnxSdpObsoletedNotifyV6v0Group": tmnxSdpObsoletedNotifyV6v0Group,
       "tmnxSdpNotifyV8v0Group": tmnxSdpNotifyV8v0Group,
       "tmnxSdpBindIpipeNotifyGroup": tmnxSdpBindIpipeNotifyGroup,
       "tmnxSdpNotifyV10v0Group": tmnxSdpNotifyV10v0Group,
       "tmnxSdpNotifyV11v0Group": tmnxSdpNotifyV11v0Group,
       "tmnxSdpGrpGroup": tmnxSdpGrpGroup,
       "tmnxSdpBindBlockOnPeerFaultGroup": tmnxSdpBindBlockOnPeerFaultGroup,
       "tmnxSdpBindFlowSpecGroup": tmnxSdpBindFlowSpecGroup,
       "tmnxSdpBindPwPortGroup": tmnxSdpBindPwPortGroup,
       "tmnxSdpVllBgpV11v0Group": tmnxSdpVllBgpV11v0Group,
       "tmnxSdpL2tpv3Group": tmnxSdpL2tpv3Group,
       "tmnxSdpBindSpbV11v0Group": tmnxSdpBindSpbV11v0Group,
       "tmnxSdpBindEthLoopbackV11v0Group": tmnxSdpBindEthLoopbackV11v0Group,
       "tmnxSdpBindEthLpbkNtfyV11v0Group": tmnxSdpBindEthLpbkNtfyV11v0Group,
       "tmnxSdpPwSecShaperGroup": tmnxSdpPwSecShaperGroup,
       "tmnxSdpPwPortV11v0Group": tmnxSdpPwPortV11v0Group,
       "tmnxSdpObsoletedObjsV11v0Group": tmnxSdpObsoletedObjsV11v0Group,
       "tmnxSdpBindCtrlChanGroup": tmnxSdpBindCtrlChanGroup,
       "sdpBindTlsFdbMacStatsGroup": sdpBindTlsFdbMacStatsGroup,
       "sdpBindTlsEtreeGroup": sdpBindTlsEtreeGroup,
       "tmnxSdpBindCpmProtV12v0Group": tmnxSdpBindCpmProtV12v0Group,
       "tmnxSdpBindCtrlChanReqGroup": tmnxSdpBindCtrlChanReqGroup,
       "tmnxSdpBindCtrlChanAckGroup": tmnxSdpBindCtrlChanAckGroup,
       "tmnxSdpPBBEpipePWRedV12v0Group": tmnxSdpPBBEpipePWRedV12v0Group,
       "tmnxSdpPbbEpipeNotifyObjsGroup": tmnxSdpPbbEpipeNotifyObjsGroup,
       "tmnxSdpPbbEpipeNotifV12v0Group": tmnxSdpPbbEpipeNotifV12v0Group,
       "tmnxSdpBindEthCfmV12v0Group": tmnxSdpBindEthCfmV12v0Group,
       "tmnxSdpV12v0Group": tmnxSdpV12v0Group,
       "tmnxSdpObsoletedObjsV12v0Group": tmnxSdpObsoletedObjsV12v0Group,
       "tmnxSdpBfdV12v0Group": tmnxSdpBfdV12v0Group,
       "tmnxSdpL2tpv3CookieGroup": tmnxSdpL2tpv3CookieGroup,
       "tmnxSdpPwTempBindV12v0Group": tmnxSdpPwTempBindV12v0Group,
       "tmnxSdpPbbV12v0Group": tmnxSdpPbbV12v0Group,
       "tmnxSdpPwLoopbackGroup": tmnxSdpPwLoopbackGroup,
       "tmnxPwTemplateAugGroup": tmnxPwTemplateAugGroup,
       "tmnxSdpCtrlPwNotifV12v0Group": tmnxSdpCtrlPwNotifV12v0Group,
       "tmnxSdpLdpIpv6Group": tmnxSdpLdpIpv6Group,
       "tmnxSdpBindV13v0Group": tmnxSdpBindV13v0Group,
       "tmnxSdpSegRouteGroup": tmnxSdpSegRouteGroup,
       "tmnxSdpBindV11v0Group": tmnxSdpBindV11v0Group,
       "tmnxSdpPwPortOperGrpGroup": tmnxSdpPwPortOperGrpGroup,
       "tmnxSdpV13v0Group": tmnxSdpV13v0Group,
       "tmnxSdpObsoletedObjsV13v0Group": tmnxSdpObsoletedObjsV13v0Group,
       "sdpBgpEvpnMplsMhGroup": sdpBgpEvpnMplsMhGroup,
       "sdpGreExtGroup": sdpGreExtGroup,
       "svcPwTmplExt14v0Group": svcPwTmplExt14v0Group,
       "tmnxSdpBindV14v0Group": tmnxSdpBindV14v0Group,
       "tmnxSdpSegRouteTeGroup": tmnxSdpSegRouteTeGroup,
       "tmnxSdpFlowSPecObsoletedV14v0Grp": tmnxSdpFlowSPecObsoletedV14v0Grp,
       "tmnxSdpBindObsoletedV13v0Group": tmnxSdpBindObsoletedV13v0Group,
       "sdpPwStaticLabelGroup": sdpPwStaticLabelGroup,
       "sdpBindV14v0Group": sdpBindV14v0Group,
       "sdpBindTlsV14v0Group": sdpBindTlsV14v0Group,
       "sdpFpeV14v0Group": sdpFpeV14v0Group,
       "sdpBindBgpEvpnAlmpGroup": sdpBindBgpEvpnAlmpGroup,
       "tmnxSdpMplsLspGroup": tmnxSdpMplsLspGroup,
       "tmnxSdpCfmLmmPerQosV15v0Group": tmnxSdpCfmLmmPerQosV15v0Group,
       "tmnxObsoletedSdpV15v0Group": tmnxObsoletedSdpV15v0Group,
       "tmnxSdpV15v0Group": tmnxSdpV15v0Group,
       "tmnxSdpWeightedLoadBalanceGroup": tmnxSdpWeightedLoadBalanceGroup,
       "sdpEvpnMhEthSegV15v0Group": sdpEvpnMhEthSegV15v0Group,
       "tmnxPwTempNameV15v0Group": tmnxPwTempNameV15v0Group,
       "sdpOperTunnelFarEndGroup": sdpOperTunnelFarEndGroup,
       "pwTemplateGreGroup": pwTemplateGreGroup,
       "pwTemplateQosV16v0Group": pwTemplateQosV16v0Group,
       "pwTemplateFilterNameV16v0Group": pwTemplateFilterNameV16v0Group,
       "tmnxSdpBindQinqV16v0Group": tmnxSdpBindQinqV16v0Group,
       "tmnxSdpBindV16v0ObsoletedGroup": tmnxSdpBindV16v0ObsoletedGroup,
       "sdpPwPortControlWordGroup": sdpPwPortControlWordGroup,
       "pwTemplateNgeAutoBindGroup": pwTemplateNgeAutoBindGroup,
       "sdpBindMcastSrcV19v0Group": sdpBindMcastSrcV19v0Group,
       "sdpNotifyV20v0Group": sdpNotifyV20v0Group,
       "sdpBindTlsMacListV20v0Group": sdpBindTlsMacListV20v0Group,
       "sdpBindCfmSquelchInCtagGroup": sdpBindCfmSquelchInCtagGroup,
       "sdpBindVccvBfdGroup": sdpBindVccvBfdGroup,
       "sdpBindSvcMtuGroup": sdpBindSvcMtuGroup,
       "sdpPwPortEntropyGroup": sdpPwPortEntropyGroup,
       "sdpLastChangeV21v0Group": sdpLastChangeV21v0Group,
       "sdpPwPortSvcMtuV21v0Group": sdpPwPortSvcMtuV21v0Group,
       "svcTlsBgpADPWTempBindTblLC": svcTlsBgpADPWTempBindTblLC,
       "svcTlsBgpADPWTempBindTable": svcTlsBgpADPWTempBindTable,
       "svcTlsBgpADPWTempBindEntry": svcTlsBgpADPWTempBindEntry,
       "svcTlsBgpADPWTempBindRowStatus": svcTlsBgpADPWTempBindRowStatus,
       "svcTlsBgpADPWTempBindLastChngd": svcTlsBgpADPWTempBindLastChngd,
       "svcTlsBgpADPWTempBindSHG": svcTlsBgpADPWTempBindSHG,
       "svcTlsBgpADPWTempBindOperGrp": svcTlsBgpADPWTempBindOperGrp,
       "svcTlsBgpADPWTempBindCreatOrigin": svcTlsBgpADPWTempBindCreatOrigin,
       "svcTlsBgpADPWTempBindBfdTemplate": svcTlsBgpADPWTempBindBfdTemplate,
       "svcTlsBgpADPWTempBindBfdEnable": svcTlsBgpADPWTempBindBfdEnable,
       "svcTlsBgpADPWTempBindBfdEncap": svcTlsBgpADPWTempBindBfdEncap,
       "svcTlsBgpADPWTempBindMonOperGrp": svcTlsBgpADPWTempBindMonOperGrp,
       "svcTlsBgpADPWTempBindRTTblLC": svcTlsBgpADPWTempBindRTTblLC,
       "svcTlsBgpADPWTempBindRTTable": svcTlsBgpADPWTempBindRTTable,
       "svcTlsBgpADPWTempBindRTEntry": svcTlsBgpADPWTempBindRTEntry,
       "svcTlsBgpADPWTempBindRT": svcTlsBgpADPWTempBindRT,
       "svcTlsBgpADPWTempBindRTRowStat": svcTlsBgpADPWTempBindRTRowStat,
       "svcL2RteTableLastChanged": svcL2RteTableLastChanged,
       "svcL2RteTable": svcL2RteTable,
       "svcL2RteEntry": svcL2RteEntry,
       "svcL2RteVsiPrefix": svcL2RteVsiPrefix,
       "svcL2RteRouteDistinguisher": svcL2RteRouteDistinguisher,
       "svcL2RteNextHopType": svcL2RteNextHopType,
       "svcL2RteNextHop": svcL2RteNextHop,
       "svcL2RteSdpBindId": svcL2RteSdpBindId,
       "svcL2RtePwTemplateId": svcL2RtePwTemplateId,
       "svcL2RteError": svcL2RteError,
       "svcL2RteLastErrorTime": svcL2RteLastErrorTime,
       "svcL2RteStatus": svcL2RteStatus,
       "svcL2BgpVplsRteTable": svcL2BgpVplsRteTable,
       "svcL2BgpVplsRteEntry": svcL2BgpVplsRteEntry,
       "svcL2BgpVplsRteVeId": svcL2BgpVplsRteVeId,
       "svcL2BgpVplsRteRD": svcL2BgpVplsRteRD,
       "svcL2BgpVplsRteNextHopType": svcL2BgpVplsRteNextHopType,
       "svcL2BgpVplsRteNextHop": svcL2BgpVplsRteNextHop,
       "svcL2BgpVplsRteSdpBindId": svcL2BgpVplsRteSdpBindId,
       "svcL2BgpVplsRtePwTemplateId": svcL2BgpVplsRtePwTemplateId,
       "svcL2BgpVplsRteError": svcL2BgpVplsRteError,
       "svcL2BgpVplsRteLastErrorTime": svcL2BgpVplsRteLastErrorTime,
       "svcL2BgpVplsRteControlWord": svcL2BgpVplsRteControlWord,
       "svcL2BgpVplsRtePathMtu": svcL2BgpVplsRtePathMtu,
       "svcL2BgpVplsRteState": svcL2BgpVplsRteState,
       "svcL2BgpVplsRteSeqDelivery": svcL2BgpVplsRteSeqDelivery,
       "svcL2BgpVplsRteDF": svcL2BgpVplsRteDF,
       "svcL2BgpVplsRteStatus": svcL2BgpVplsRteStatus,
       "svcVllBgpADPWTempBindTblLC": svcVllBgpADPWTempBindTblLC,
       "svcVllBgpADPWTempBindTable": svcVllBgpADPWTempBindTable,
       "svcVllBgpADPWTempBindEntry": svcVllBgpADPWTempBindEntry,
       "svcVllBgpADPWTempBindRowStatus": svcVllBgpADPWTempBindRowStatus,
       "svcVllBgpADPWTempBindLastChngd": svcVllBgpADPWTempBindLastChngd,
       "svcVllBgpADPWTempBindEndPt": svcVllBgpADPWTempBindEndPt,
       "svcVllBgpADPWTempBindBfdTemplate": svcVllBgpADPWTempBindBfdTemplate,
       "svcVllBgpADPWTempBindBfdEnable": svcVllBgpADPWTempBindBfdEnable,
       "svcVllBgpADPWTempBindBfdEncap": svcVllBgpADPWTempBindBfdEncap,
       "svcVllBgpADPWTempBindRTTblLC": svcVllBgpADPWTempBindRTTblLC,
       "svcVllBgpADPWTempBindRTTable": svcVllBgpADPWTempBindRTTable,
       "svcVllBgpADPWTempBindRTEntry": svcVllBgpADPWTempBindRTEntry,
       "svcVllBgpADPWTempBindRT": svcVllBgpADPWTempBindRT,
       "svcVllBgpADPWTempBindRTRowStat": svcVllBgpADPWTempBindRTRowStat,
       "svcL2BgpVpwsRteTable": svcL2BgpVpwsRteTable,
       "svcL2BgpVpwsRteEntry": svcL2BgpVpwsRteEntry,
       "svcL2BgpVpwsRteVeId": svcL2BgpVpwsRteVeId,
       "svcL2BgpVpwsRteRD": svcL2BgpVpwsRteRD,
       "svcL2BgpVpwsRteNextHopType": svcL2BgpVpwsRteNextHopType,
       "svcL2BgpVpwsRteNextHop": svcL2BgpVpwsRteNextHop,
       "svcL2BgpVpwsRteSdpBindId": svcL2BgpVpwsRteSdpBindId,
       "svcL2BgpVpwsRtePwTemplateId": svcL2BgpVpwsRtePwTemplateId,
       "svcL2BgpVpwsRteError": svcL2BgpVpwsRteError,
       "svcL2BgpVpwsRteLastErrorTime": svcL2BgpVpwsRteLastErrorTime,
       "svcL2BgpVpwsRteControlWord": svcL2BgpVpwsRteControlWord,
       "svcL2BgpVpwsRtePathMtu": svcL2BgpVpwsRtePathMtu,
       "svcL2BgpVpwsRteState": svcL2BgpVpwsRteState,
       "svcL2BgpVpwsRteSeqDelivery": svcL2BgpVpwsRteSeqDelivery,
       "svcL2BgpVpwsRteStatus": svcL2BgpVpwsRteStatus,
       "svcL2BgpVpwsRteCsv": svcL2BgpVpwsRteCsv,
       "svcL2BgpVpwsRteTxStatus": svcL2BgpVpwsRteTxStatus,
       "svcL2BgpVpwsRtePreference": svcL2BgpVpwsRtePreference,
       "tmnxSdpObjs": tmnxSdpObjs,
       "sdpNumEntries": sdpNumEntries,
       "sdpNextFreeId": sdpNextFreeId,
       "sdpInfoTable": sdpInfoTable,
       "sdpInfoEntry": sdpInfoEntry,
       "sdpId": sdpId,
       "sdpRowStatus": sdpRowStatus,
       "sdpDelivery": sdpDelivery,
       "sdpFarEndIpAddress": sdpFarEndIpAddress,
       "sdpLspList": sdpLspList,
       "sdpDescription": sdpDescription,
       "sdpLabelSignaling": sdpLabelSignaling,
       "sdpAdminStatus": sdpAdminStatus,
       "sdpOperStatus": sdpOperStatus,
       "sdpAdminPathMtu": sdpAdminPathMtu,
       "sdpOperPathMtu": sdpOperPathMtu,
       "sdpKeepAliveAdminStatus": sdpKeepAliveAdminStatus,
       "sdpKeepAliveOperStatus": sdpKeepAliveOperStatus,
       "sdpKeepAliveHelloTime": sdpKeepAliveHelloTime,
       "sdpKeepAliveMaxDropCount": sdpKeepAliveMaxDropCount,
       "sdpKeepAliveHoldDownTime": sdpKeepAliveHoldDownTime,
       "sdpLastMgmtChange": sdpLastMgmtChange,
       "sdpKeepAliveHelloMessageLength": sdpKeepAliveHelloMessageLength,
       "sdpKeepAliveNumHelloRequestMessages": sdpKeepAliveNumHelloRequestMessages,
       "sdpKeepAliveNumHelloResponseMessages": sdpKeepAliveNumHelloResponseMessages,
       "sdpKeepAliveNumLateHelloResponseMessages": sdpKeepAliveNumLateHelloResponseMessages,
       "sdpKeepAliveHelloRequestTimeout": sdpKeepAliveHelloRequestTimeout,
       "sdpLdpEnabled": sdpLdpEnabled,
       "sdpVlanVcEtype": sdpVlanVcEtype,
       "sdpAdvertisedVllMtuOverride": sdpAdvertisedVllMtuOverride,
       "sdpOperFlags": sdpOperFlags,
       "sdpLastStatusChange": sdpLastStatusChange,
       "sdpMvplsMgmtService": sdpMvplsMgmtService,
       "sdpMvplsMgmtSdpBndId": sdpMvplsMgmtSdpBndId,
       "sdpCollectAcctStats": sdpCollectAcctStats,
       "sdpAccountingPolicyId": sdpAccountingPolicyId,
       "sdpClassFwdingEnabled": sdpClassFwdingEnabled,
       "sdpClassFwdingDefaultLsp": sdpClassFwdingDefaultLsp,
       "sdpClassFwdingMcLsp": sdpClassFwdingMcLsp,
       "sdpMetric": sdpMetric,
       "sdpAutoSdp": sdpAutoSdp,
       "sdpSnmpAllowed": sdpSnmpAllowed,
       "sdpPBBEtype": sdpPBBEtype,
       "sdpBandwidthBookingFactor": sdpBandwidthBookingFactor,
       "sdpOperBandwidth": sdpOperBandwidth,
       "sdpAvailableBandwidth": sdpAvailableBandwidth,
       "sdpMaxBookableBandwidth": sdpMaxBookableBandwidth,
       "sdpBookedBandwidth": sdpBookedBandwidth,
       "sdpCreationOrigin": sdpCreationOrigin,
       "sdpEnforceDiffServLspFc": sdpEnforceDiffServLspFc,
       "sdpMixedLspModeEnabled": sdpMixedLspModeEnabled,
       "sdpLspRevertTime": sdpLspRevertTime,
       "sdpLspRevertTimeCountDown": sdpLspRevertTimeCountDown,
       "sdpLdpLspId": sdpLdpLspId,
       "sdpLdpActive": sdpLdpActive,
       "sdpNetDomainName": sdpNetDomainName,
       "sdpEgressIfsNetDomainConsistent": sdpEgressIfsNetDomainConsistent,
       "sdpBgpTunnelEnabled": sdpBgpTunnelEnabled,
       "sdpBgpTunnelLspId": sdpBgpTunnelLspId,
       "sdpTunnelFarEndIpAddress": sdpTunnelFarEndIpAddress,
       "sdpActiveLspType": sdpActiveLspType,
       "sdpBindingPort": sdpBindingPort,
       "sdpFarEndNodeId": sdpFarEndNodeId,
       "sdpFarEndGlobalId": sdpFarEndGlobalId,
       "sdpFarEndInetAddressType": sdpFarEndInetAddressType,
       "sdpFarEndInetAddress": sdpFarEndInetAddress,
       "sdpLocalEndInetAddressType": sdpLocalEndInetAddressType,
       "sdpLocalEndInetAddress": sdpLocalEndInetAddress,
       "sdpSourceBMacLSB": sdpSourceBMacLSB,
       "sdpControlPWVCId": sdpControlPWVCId,
       "sdpControlPWIsActive": sdpControlPWIsActive,
       "sdpTunnelFarEndInetAddressType": sdpTunnelFarEndInetAddressType,
       "sdpTunnelFarEndInetAddress": sdpTunnelFarEndInetAddress,
       "sdpGreAllowFragmentation": sdpGreAllowFragmentation,
       "sdpFpeLspId": sdpFpeLspId,
       "sdpWeightedEcmpEnabled": sdpWeightedEcmpEnabled,
       "sdpOperTunnelFarEndInetAddrType": sdpOperTunnelFarEndInetAddrType,
       "sdpOperTunnelFarEndInetAddr": sdpOperTunnelFarEndInetAddr,
       "sdpBindTable": sdpBindTable,
       "sdpBindEntry": sdpBindEntry,
       "sdpBindId": sdpBindId,
       "sdpBindRowStatus": sdpBindRowStatus,
       "sdpBindAdminIngressLabel": sdpBindAdminIngressLabel,
       "sdpBindAdminEgressLabel": sdpBindAdminEgressLabel,
       "sdpBindOperIngressLabel": sdpBindOperIngressLabel,
       "sdpBindOperEgressLabel": sdpBindOperEgressLabel,
       "sdpBindAdminStatus": sdpBindAdminStatus,
       "sdpBindOperStatus": sdpBindOperStatus,
       "sdpBindLastMgmtChange": sdpBindLastMgmtChange,
       "sdpBindType": sdpBindType,
       "sdpBindIngressMacFilterId": sdpBindIngressMacFilterId,
       "sdpBindIngressIpFilterId": sdpBindIngressIpFilterId,
       "sdpBindEgressMacFilterId": sdpBindEgressMacFilterId,
       "sdpBindEgressIpFilterId": sdpBindEgressIpFilterId,
       "sdpBindVpnId": sdpBindVpnId,
       "sdpBindCustId": sdpBindCustId,
       "sdpBindVcType": sdpBindVcType,
       "sdpBindVlanVcTag": sdpBindVlanVcTag,
       "sdpBindSplitHorizonGrp": sdpBindSplitHorizonGrp,
       "sdpBindOperFlags": sdpBindOperFlags,
       "sdpBindLastStatusChange": sdpBindLastStatusChange,
       "sdpBindIesIfIndex": sdpBindIesIfIndex,
       "sdpBindMacPinning": sdpBindMacPinning,
       "sdpBindIngressIpv6FilterId": sdpBindIngressIpv6FilterId,
       "sdpBindEgressIpv6FilterId": sdpBindEgressIpv6FilterId,
       "sdpBindCollectAcctStats": sdpBindCollectAcctStats,
       "sdpBindAccountingPolicyId": sdpBindAccountingPolicyId,
       "sdpBindPwPeerStatusBits": sdpBindPwPeerStatusBits,
       "sdpBindPeerVccvCvBits": sdpBindPeerVccvCvBits,
       "sdpBindPeerVccvCcBits": sdpBindPeerVccvCcBits,
       "sdpBindControlWordBit": sdpBindControlWordBit,
       "sdpBindOperControlWord": sdpBindOperControlWord,
       "sdpBindEndPoint": sdpBindEndPoint,
       "sdpBindEndPointPrecedence": sdpBindEndPointPrecedence,
       "sdpBindIsICB": sdpBindIsICB,
       "sdpBindPwFaultInetAddressType": sdpBindPwFaultInetAddressType,
       "sdpBindPwFaultInetAddress": sdpBindPwFaultInetAddress,
       "sdpBindClassFwdingOperState": sdpBindClassFwdingOperState,
       "sdpBindForceVlanVcForwarding": sdpBindForceVlanVcForwarding,
       "sdpBindAdminBandwidth": sdpBindAdminBandwidth,
       "sdpBindOperBandwidth": sdpBindOperBandwidth,
       "sdpBindCreationOrigin": sdpBindCreationOrigin,
       "sdpBindDescription": sdpBindDescription,
       "sdpBindSiteName": sdpBindSiteName,
       "sdpBindHashLabel": sdpBindHashLabel,
       "sdpBindIsaAaApplicationProfile": sdpBindIsaAaApplicationProfile,
       "sdpBindStandbySigSlave": sdpBindStandbySigSlave,
       "sdpBindHashLabelSignalCapability": sdpBindHashLabelSignalCapability,
       "sdpBindIngressFlowspec": sdpBindIngressFlowspec,
       "sdpBindCpmProtPolicyId": sdpBindCpmProtPolicyId,
       "sdpBindCpmProtMonitorMac": sdpBindCpmProtMonitorMac,
       "sdpBindCpmProtEthCfmMonitorFlags": sdpBindCpmProtEthCfmMonitorFlags,
       "sdpBindTransitIpPolicyId": sdpBindTransitIpPolicyId,
       "sdpBindPwStatusSignaling": sdpBindPwStatusSignaling,
       "sdpBindOperGrp": sdpBindOperGrp,
       "sdpBindMonitorOperGrp": sdpBindMonitorOperGrp,
       "sdpBindOperHashLabel": sdpBindOperHashLabel,
       "sdpBindTransitPrefixPolicyId": sdpBindTransitPrefixPolicyId,
       "sdpBindAarpId": sdpBindAarpId,
       "sdpBindIngressQoSNetworkPlcyId": sdpBindIngressQoSNetworkPlcyId,
       "sdpBindEgressQoSNetworkPlcyId": sdpBindEgressQoSNetworkPlcyId,
       "sdpBindIngressQoSFpRedirectQGrp": sdpBindIngressQoSFpRedirectQGrp,
       "sdpBindEgressQoSPortRedirectQGrp": sdpBindEgressQoSPortRedirectQGrp,
       "sdpBindIngressQoSInstanceId": sdpBindIngressQoSInstanceId,
       "sdpBindEgressQoSInstanceId": sdpBindEgressQoSInstanceId,
       "sdpBindAarpServRefType": sdpBindAarpServRefType,
       "sdpBindPwLocalStatusBits": sdpBindPwLocalStatusBits,
       "sdpBindBlockOnPeerFault": sdpBindBlockOnPeerFault,
       "sdpBindIngressIPv6Flowspec": sdpBindIngressIPv6Flowspec,
       "sdpBindMirrorRemoteSource": sdpBindMirrorRemoteSource,
       "sdpBindEtreeRootLeafTag": sdpBindEtreeRootLeafTag,
       "sdpBindCpmProtMonitorIP": sdpBindCpmProtMonitorIP,
       "sdpBindUseSdpBMac": sdpBindUseSdpBMac,
       "sdpBindEtreeLeafAc": sdpBindEtreeLeafAc,
       "sdpBindBfdTemplateName": sdpBindBfdTemplateName,
       "sdpBindBfdEnable": sdpBindBfdEnable,
       "sdpBindBfdEncap": sdpBindBfdEncap,
       "sdpBindForceQinqVcForwarding": sdpBindForceQinqVcForwarding,
       "sdpBindIngressVlanTranslation": sdpBindIngressVlanTranslation,
       "sdpBindIngressVlanTranslationId": sdpBindIngressVlanTranslationId,
       "sdpBindMinReqdSdpOperMtu": sdpBindMinReqdSdpOperMtu,
       "sdpBindForceQinqVcFwding": sdpBindForceQinqVcFwding,
       "sdpBindMulticastSource": sdpBindMulticastSource,
       "sdpBindBaseStatsTable": sdpBindBaseStatsTable,
       "sdpBindBaseStatsEntry": sdpBindBaseStatsEntry,
       "sdpBindBaseStatsIngressForwardedPackets": sdpBindBaseStatsIngressForwardedPackets,
       "sdpBindBaseStatsIngressDroppedPackets": sdpBindBaseStatsIngressDroppedPackets,
       "sdpBindBaseStatsEgressForwardedPackets": sdpBindBaseStatsEgressForwardedPackets,
       "sdpBindBaseStatsEgressForwardedOctets": sdpBindBaseStatsEgressForwardedOctets,
       "sdpBindBaseStatsCustId": sdpBindBaseStatsCustId,
       "sdpBindBaseStatsIngFwdOctets": sdpBindBaseStatsIngFwdOctets,
       "sdpBindBaseStatsIngDropOctets": sdpBindBaseStatsIngDropOctets,
       "sdpBindTlsTable": sdpBindTlsTable,
       "sdpBindTlsEntry": sdpBindTlsEntry,
       "sdpBindTlsStpAdminStatus": sdpBindTlsStpAdminStatus,
       "sdpBindTlsStpPriority": sdpBindTlsStpPriority,
       "sdpBindTlsStpPortNum": sdpBindTlsStpPortNum,
       "sdpBindTlsStpPathCost": sdpBindTlsStpPathCost,
       "sdpBindTlsStpRapidStart": sdpBindTlsStpRapidStart,
       "sdpBindTlsStpBpduEncap": sdpBindTlsStpBpduEncap,
       "sdpBindTlsStpPortState": sdpBindTlsStpPortState,
       "sdpBindTlsStpDesignatedBridge": sdpBindTlsStpDesignatedBridge,
       "sdpBindTlsStpDesignatedPort": sdpBindTlsStpDesignatedPort,
       "sdpBindTlsStpForwardTransitions": sdpBindTlsStpForwardTransitions,
       "sdpBindTlsStpInConfigBpdus": sdpBindTlsStpInConfigBpdus,
       "sdpBindTlsStpInTcnBpdus": sdpBindTlsStpInTcnBpdus,
       "sdpBindTlsStpInBadBpdus": sdpBindTlsStpInBadBpdus,
       "sdpBindTlsStpOutConfigBpdus": sdpBindTlsStpOutConfigBpdus,
       "sdpBindTlsStpOutTcnBpdus": sdpBindTlsStpOutTcnBpdus,
       "sdpBindTlsStpOperBpduEncap": sdpBindTlsStpOperBpduEncap,
       "sdpBindTlsStpVpnId": sdpBindTlsStpVpnId,
       "sdpBindTlsStpCustId": sdpBindTlsStpCustId,
       "sdpBindTlsMacAddressLimit": sdpBindTlsMacAddressLimit,
       "sdpBindTlsNumMacAddresses": sdpBindTlsNumMacAddresses,
       "sdpBindTlsNumStaticMacAddresses": sdpBindTlsNumStaticMacAddresses,
       "sdpBindTlsMacLearning": sdpBindTlsMacLearning,
       "sdpBindTlsMacAgeing": sdpBindTlsMacAgeing,
       "sdpBindTlsStpOperEdge": sdpBindTlsStpOperEdge,
       "sdpBindTlsStpAdminPointToPoint": sdpBindTlsStpAdminPointToPoint,
       "sdpBindTlsStpPortRole": sdpBindTlsStpPortRole,
       "sdpBindTlsStpAutoEdge": sdpBindTlsStpAutoEdge,
       "sdpBindTlsStpOperProtocol": sdpBindTlsStpOperProtocol,
       "sdpBindTlsStpInRstBpdus": sdpBindTlsStpInRstBpdus,
       "sdpBindTlsStpOutRstBpdus": sdpBindTlsStpOutRstBpdus,
       "sdpBindTlsLimitMacMove": sdpBindTlsLimitMacMove,
       "sdpBindTlsDiscardUnknownSource": sdpBindTlsDiscardUnknownSource,
       "sdpBindTlsMvplsPruneState": sdpBindTlsMvplsPruneState,
       "sdpBindTlsMvplsMgmtService": sdpBindTlsMvplsMgmtService,
       "sdpBindTlsMvplsMgmtSdpBndId": sdpBindTlsMvplsMgmtSdpBndId,
       "sdpBindTlsStpException": sdpBindTlsStpException,
       "sdpBindTlsL2ptTermination": sdpBindTlsL2ptTermination,
       "sdpBindTlsBpduTranslation": sdpBindTlsBpduTranslation,
       "sdpBindTlsStpRootGuard": sdpBindTlsStpRootGuard,
       "sdpBindTlsStpInMstBpdus": sdpBindTlsStpInMstBpdus,
       "sdpBindTlsStpOutMstBpdus": sdpBindTlsStpOutMstBpdus,
       "sdpBindTlsStpRxdDesigBridge": sdpBindTlsStpRxdDesigBridge,
       "sdpBindTlsMacMoveNextUpTime": sdpBindTlsMacMoveNextUpTime,
       "sdpBindTlsMacMoveRateExcdLeft": sdpBindTlsMacMoveRateExcdLeft,
       "sdpBindTlsLimitMacMoveLevel": sdpBindTlsLimitMacMoveLevel,
       "sdpBindTlsBpduTransOper": sdpBindTlsBpduTransOper,
       "sdpBindTlsL2ptProtocols": sdpBindTlsL2ptProtocols,
       "sdpBindTlsIgnoreStandbySig": sdpBindTlsIgnoreStandbySig,
       "sdpBindTlsBlockOnMeshFail": sdpBindTlsBlockOnMeshFail,
       "sdpBindTlsInTcBitBpdus": sdpBindTlsInTcBitBpdus,
       "sdpBindTlsOutTcBitBpdus": sdpBindTlsOutTcBitBpdus,
       "sdpBindTlsRestProtSrcMac": sdpBindTlsRestProtSrcMac,
       "sdpBindTlsRestProtSrcMacAction": sdpBindTlsRestProtSrcMacAction,
       "sdpBindTlsAutoLearnMacProtect": sdpBindTlsAutoLearnMacProtect,
       "sdpBindDisableSendBvplsEvpnFlush": sdpBindDisableSendBvplsEvpnFlush,
       "sdpBindTlsRestProtSrcMacOper": sdpBindTlsRestProtSrcMacOper,
       "sdpBindTlsRestProtSrcMacOperAct": sdpBindTlsRestProtSrcMacOperAct,
       "sdpBindTlsAutoLrnMacPrtExcList": sdpBindTlsAutoLrnMacPrtExcList,
       "sdpBindTlsLastMgmtChange": sdpBindTlsLastMgmtChange,
       "sdpBindMeshTlsTable": sdpBindMeshTlsTable,
       "sdpBindMeshTlsEntry": sdpBindMeshTlsEntry,
       "sdpBindMeshTlsPortState": sdpBindMeshTlsPortState,
       "sdpBindMeshTlsHoldDownTimer": sdpBindMeshTlsHoldDownTimer,
       "sdpBindMeshTlsTransitionState": sdpBindMeshTlsTransitionState,
       "sdpBindMeshTlsNotInMstRegion": sdpBindMeshTlsNotInMstRegion,
       "sdpBindMeshTlsRestProtSrcMac": sdpBindMeshTlsRestProtSrcMac,
       "sdpBindMeshTlsRestProtSrcMacAct": sdpBindMeshTlsRestProtSrcMacAct,
       "sdpBindMeshTlsAutoLearnMacProt": sdpBindMeshTlsAutoLearnMacProt,
       "sdpBindMeshTlsRPSMacOper": sdpBindMeshTlsRPSMacOper,
       "sdpBindMeshTlsRPSMacOperAct": sdpBindMeshTlsRPSMacOperAct,
       "sdpBindMeshTlsAutLrnMacPrtExcLs": sdpBindMeshTlsAutLrnMacPrtExcLs,
       "sdpBindApipeTable": sdpBindApipeTable,
       "sdpBindApipeEntry": sdpBindApipeEntry,
       "sdpBindApipeAdminConcatCellCount": sdpBindApipeAdminConcatCellCount,
       "sdpBindApipeSigConcatCellCount": sdpBindApipeSigConcatCellCount,
       "sdpBindApipeOperConcatCellCount": sdpBindApipeOperConcatCellCount,
       "sdpBindApipeConcatMaxDelay": sdpBindApipeConcatMaxDelay,
       "sdpBindApipeConcatCellClp": sdpBindApipeConcatCellClp,
       "sdpBindApipeConcatCellAal5Fr": sdpBindApipeConcatCellAal5Fr,
       "sdpBindDhcpInfoTable": sdpBindDhcpInfoTable,
       "sdpBindDhcpInfoEntry": sdpBindDhcpInfoEntry,
       "sdpBindDhcpDescription": sdpBindDhcpDescription,
       "sdpBindDhcpSnoop": sdpBindDhcpSnoop,
       "sdpBindDhcpStatsTable": sdpBindDhcpStatsTable,
       "sdpBindDhcpStatsEntry": sdpBindDhcpStatsEntry,
       "sdpBindDhcpStatsClntSnoopdPckts": sdpBindDhcpStatsClntSnoopdPckts,
       "sdpBindDhcpStatsSrvrSnoopdPckts": sdpBindDhcpStatsSrvrSnoopdPckts,
       "sdpBindDhcpStatsClntForwdPckts": sdpBindDhcpStatsClntForwdPckts,
       "sdpBindDhcpStatsSrvrForwdPckts": sdpBindDhcpStatsSrvrForwdPckts,
       "sdpBindDhcpStatsClntDropdPckts": sdpBindDhcpStatsClntDropdPckts,
       "sdpBindDhcpStatsSrvrDropdPckts": sdpBindDhcpStatsSrvrDropdPckts,
       "sdpBindDhcpStatsClntProxRadPckts": sdpBindDhcpStatsClntProxRadPckts,
       "sdpBindDhcpStatsClntProxLSPckts": sdpBindDhcpStatsClntProxLSPckts,
       "sdpBindDhcpStatsGenReleasePckts": sdpBindDhcpStatsGenReleasePckts,
       "sdpBindDhcpStatsGenForceRenPckts": sdpBindDhcpStatsGenForceRenPckts,
       "sdpBindDhcpStatsClntProxUDBPckts": sdpBindDhcpStatsClntProxUDBPckts,
       "sdpBindDhcpStatsClntProxNqPckts": sdpBindDhcpStatsClntProxNqPckts,
       "sdpBindIpipeTable": sdpBindIpipeTable,
       "sdpBindIpipeEntry": sdpBindIpipeEntry,
       "sdpBindIpipeCeInetAddressType": sdpBindIpipeCeInetAddressType,
       "sdpBindIpipeCeInetAddress": sdpBindIpipeCeInetAddress,
       "sdpBindIpipePeerCeInetAddrType": sdpBindIpipePeerCeInetAddrType,
       "sdpBindIpipePeerCeInetAddr": sdpBindIpipePeerCeInetAddr,
       "sdpBindIpipePeerIpv6Capability": sdpBindIpipePeerIpv6Capability,
       "sdpBindIpipePeerLLCeInetAddr": sdpBindIpipePeerLLCeInetAddr,
       "sdpBindIpipePeerGlobalCeInetAddr": sdpBindIpipePeerGlobalCeInetAddr,
       "sdpFCMappingTable": sdpFCMappingTable,
       "sdpFCMappingEntry": sdpFCMappingEntry,
       "sdpFCMappingFCName": sdpFCMappingFCName,
       "sdpFCMappingRowStatus": sdpFCMappingRowStatus,
       "sdpFCMappingLspId": sdpFCMappingLspId,
       "sdpBindTlsMfibAllowedMdaTable": sdpBindTlsMfibAllowedMdaTable,
       "sdpBindTlsMfibAllowedMdaEntry": sdpBindTlsMfibAllowedMdaEntry,
       "sdpBindTlsMfibMdaRowStatus": sdpBindTlsMfibMdaRowStatus,
       "sdpBindCpipeTable": sdpBindCpipeTable,
       "sdpBindCpipeEntry": sdpBindCpipeEntry,
       "sdpBindCpipeLocalPayloadSize": sdpBindCpipeLocalPayloadSize,
       "sdpBindCpipePeerPayloadSize": sdpBindCpipePeerPayloadSize,
       "sdpBindCpipeLocalBitrate": sdpBindCpipeLocalBitrate,
       "sdpBindCpipePeerBitrate": sdpBindCpipePeerBitrate,
       "sdpBindCpipeLocalSigPkts": sdpBindCpipeLocalSigPkts,
       "sdpBindCpipePeerSigPkts": sdpBindCpipePeerSigPkts,
       "sdpBindCpipeLocalCasTrunkFraming": sdpBindCpipeLocalCasTrunkFraming,
       "sdpBindCpipePeerCasTrunkFraming": sdpBindCpipePeerCasTrunkFraming,
       "sdpBindCpipeLocalUseRtpHeader": sdpBindCpipeLocalUseRtpHeader,
       "sdpBindCpipePeerUseRtpHeader": sdpBindCpipePeerUseRtpHeader,
       "sdpBindCpipeLocalDifferential": sdpBindCpipeLocalDifferential,
       "sdpBindCpipePeerDifferential": sdpBindCpipePeerDifferential,
       "sdpBindCpipeLocalTimestampFreq": sdpBindCpipeLocalTimestampFreq,
       "sdpBindCpipePeerTimestampFreq": sdpBindCpipePeerTimestampFreq,
       "sdpBindTlsL2ptStatsTable": sdpBindTlsL2ptStatsTable,
       "sdpBindTlsL2ptStatsEntry": sdpBindTlsL2ptStatsEntry,
       "sdpBindTlsL2ptStatsLastClearedTime": sdpBindTlsL2ptStatsLastClearedTime,
       "sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx": sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx": sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx": sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx": sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx": sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx": sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx": sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx": sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx": sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx": sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx": sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx": sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx,
       "sdpBindTlsL2ptStatsStpConfigBpdusRx": sdpBindTlsL2ptStatsStpConfigBpdusRx,
       "sdpBindTlsL2ptStatsStpConfigBpdusTx": sdpBindTlsL2ptStatsStpConfigBpdusTx,
       "sdpBindTlsL2ptStatsStpRstBpdusRx": sdpBindTlsL2ptStatsStpRstBpdusRx,
       "sdpBindTlsL2ptStatsStpRstBpdusTx": sdpBindTlsL2ptStatsStpRstBpdusTx,
       "sdpBindTlsL2ptStatsStpTcnBpdusRx": sdpBindTlsL2ptStatsStpTcnBpdusRx,
       "sdpBindTlsL2ptStatsStpTcnBpdusTx": sdpBindTlsL2ptStatsStpTcnBpdusTx,
       "sdpBindTlsL2ptStatsPvstConfigBpdusRx": sdpBindTlsL2ptStatsPvstConfigBpdusRx,
       "sdpBindTlsL2ptStatsPvstConfigBpdusTx": sdpBindTlsL2ptStatsPvstConfigBpdusTx,
       "sdpBindTlsL2ptStatsPvstRstBpdusRx": sdpBindTlsL2ptStatsPvstRstBpdusRx,
       "sdpBindTlsL2ptStatsPvstRstBpdusTx": sdpBindTlsL2ptStatsPvstRstBpdusTx,
       "sdpBindTlsL2ptStatsPvstTcnBpdusRx": sdpBindTlsL2ptStatsPvstTcnBpdusRx,
       "sdpBindTlsL2ptStatsPvstTcnBpdusTx": sdpBindTlsL2ptStatsPvstTcnBpdusTx,
       "sdpBindTlsL2ptStatsOtherBpdusRx": sdpBindTlsL2ptStatsOtherBpdusRx,
       "sdpBindTlsL2ptStatsOtherBpdusTx": sdpBindTlsL2ptStatsOtherBpdusTx,
       "sdpBindTlsL2ptStatsOtherL2ptBpdusRx": sdpBindTlsL2ptStatsOtherL2ptBpdusRx,
       "sdpBindTlsL2ptStatsOtherL2ptBpdusTx": sdpBindTlsL2ptStatsOtherL2ptBpdusTx,
       "sdpBindTlsL2ptStatsOtherInvalidBpdusRx": sdpBindTlsL2ptStatsOtherInvalidBpdusRx,
       "sdpBindTlsL2ptStatsOtherInvalidBpdusTx": sdpBindTlsL2ptStatsOtherInvalidBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx": sdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx": sdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx": sdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx": sdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx": sdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx": sdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx": sdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx": sdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx": sdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx": sdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx,
       "sdpBindTlsL2ptStatsCdpBpdusRx": sdpBindTlsL2ptStatsCdpBpdusRx,
       "sdpBindTlsL2ptStatsCdpBpdusTx": sdpBindTlsL2ptStatsCdpBpdusTx,
       "sdpBindTlsL2ptStatsVtpBpdusRx": sdpBindTlsL2ptStatsVtpBpdusRx,
       "sdpBindTlsL2ptStatsVtpBpdusTx": sdpBindTlsL2ptStatsVtpBpdusTx,
       "sdpBindTlsL2ptStatsDtpBpdusRx": sdpBindTlsL2ptStatsDtpBpdusRx,
       "sdpBindTlsL2ptStatsDtpBpdusTx": sdpBindTlsL2ptStatsDtpBpdusTx,
       "sdpBindTlsL2ptStatsPagpBpdusRx": sdpBindTlsL2ptStatsPagpBpdusRx,
       "sdpBindTlsL2ptStatsPagpBpdusTx": sdpBindTlsL2ptStatsPagpBpdusTx,
       "sdpBindTlsL2ptStatsUdldBpdusRx": sdpBindTlsL2ptStatsUdldBpdusRx,
       "sdpBindTlsL2ptStatsUdldBpdusTx": sdpBindTlsL2ptStatsUdldBpdusTx,
       "pwTemplateTableLastChanged": pwTemplateTableLastChanged,
       "pwTemplateTable": pwTemplateTable,
       "pwTemplateEntry": pwTemplateEntry,
       "pwTemplateId": pwTemplateId,
       "pwTemplateRowStatus": pwTemplateRowStatus,
       "pwTemplateLastChanged": pwTemplateLastChanged,
       "pwTemplateUseProvisionedSdp": pwTemplateUseProvisionedSdp,
       "pwTemplateVcType": pwTemplateVcType,
       "pwTemplateAccountingPolicyId": pwTemplateAccountingPolicyId,
       "pwTemplateCollectAcctStats": pwTemplateCollectAcctStats,
       "pwTemplateMacLearning": pwTemplateMacLearning,
       "pwTemplateMacAgeing": pwTemplateMacAgeing,
       "pwTemplateDiscardUnknownSource": pwTemplateDiscardUnknownSource,
       "pwTemplateLimitMacMove": pwTemplateLimitMacMove,
       "pwTemplateMacPinning": pwTemplateMacPinning,
       "pwTemplateVlanVcTag": pwTemplateVlanVcTag,
       "pwTemplateMacAddressLimit": pwTemplateMacAddressLimit,
       "pwTemplateShgName": pwTemplateShgName,
       "pwTemplateShgDescription": pwTemplateShgDescription,
       "pwTemplateShgRestProtSrcMac": pwTemplateShgRestProtSrcMac,
       "pwTemplateShgRestUnprotDstMac": pwTemplateShgRestUnprotDstMac,
       "pwTemplateEgressMacFilterId": pwTemplateEgressMacFilterId,
       "pwTemplateEgressIpFilterId": pwTemplateEgressIpFilterId,
       "pwTemplateEgressIpv6FilterId": pwTemplateEgressIpv6FilterId,
       "pwTemplateIngressMacFilterId": pwTemplateIngressMacFilterId,
       "pwTemplateIngressIpFilterId": pwTemplateIngressIpFilterId,
       "pwTemplateIngressIpv6FilterId": pwTemplateIngressIpv6FilterId,
       "pwTemplateIgmpFastLeave": pwTemplateIgmpFastLeave,
       "pwTemplateIgmpImportPlcy": pwTemplateIgmpImportPlcy,
       "pwTemplateIgmpLastMembIntvl": pwTemplateIgmpLastMembIntvl,
       "pwTemplateIgmpMaxNbrGrps": pwTemplateIgmpMaxNbrGrps,
       "pwTemplateIgmpGenQueryIntvl": pwTemplateIgmpGenQueryIntvl,
       "pwTemplateIgmpQueryRespIntvl": pwTemplateIgmpQueryRespIntvl,
       "pwTemplateIgmpRobustCount": pwTemplateIgmpRobustCount,
       "pwTemplateIgmpSendQueries": pwTemplateIgmpSendQueries,
       "pwTemplateIgmpMcacPolicyName": pwTemplateIgmpMcacPolicyName,
       "pwTemplateIgmpMcacUnconstBW": pwTemplateIgmpMcacUnconstBW,
       "pwTemplateIgmpMcacPrRsvMndBW": pwTemplateIgmpMcacPrRsvMndBW,
       "pwTemplateIgmpVersion": pwTemplateIgmpVersion,
       "pwTemplateForceVlanVcForwarding": pwTemplateForceVlanVcForwarding,
       "pwTemplateHashLabel": pwTemplateHashLabel,
       "pwTemplateControlWord": pwTemplateControlWord,
       "pwTemplateHashLabelSignalCap": pwTemplateHashLabelSignalCap,
       "pwTemplateRestProtSrcMac": pwTemplateRestProtSrcMac,
       "pwTemplateRestProtSrcMacAction": pwTemplateRestProtSrcMacAction,
       "pwTemplateAutoLearnMacProtect": pwTemplateAutoLearnMacProtect,
       "pwTemplateShgRestProtSrcMacAct": pwTemplateShgRestProtSrcMacAct,
       "pwTemplateShgAutoLearnMacProtect": pwTemplateShgAutoLearnMacProtect,
       "pwTemplateIngQoSNetworkPlcyId": pwTemplateIngQoSNetworkPlcyId,
       "pwTemplateEgrQoSNetworkPlcyId": pwTemplateEgrQoSNetworkPlcyId,
       "pwTemplateIngQoSFpRedirectQGrp": pwTemplateIngQoSFpRedirectQGrp,
       "pwTemplateEgrQoSPortRedirectQGrp": pwTemplateEgrQoSPortRedirectQGrp,
       "pwTemplateIngQoSInstanceId": pwTemplateIngQoSInstanceId,
       "pwTemplateEgrQoSInstanceId": pwTemplateEgrQoSInstanceId,
       "pwTemplateBlockOnPeerFault": pwTemplateBlockOnPeerFault,
       "pwTemplateForceQinqVcForwarding": pwTemplateForceQinqVcForwarding,
       "pwTemplatePreferProvSdp": pwTemplatePreferProvSdp,
       "pwTemplateEntropyLabel": pwTemplateEntropyLabel,
       "pwTemplateName": pwTemplateName,
       "pwTemplateGreDelivery": pwTemplateGreDelivery,
       "pwTemplateIngQoSNetworkPlcyName": pwTemplateIngQoSNetworkPlcyName,
       "pwTemplateEgrQoSNetworkPlcyName": pwTemplateEgrQoSNetworkPlcyName,
       "pwTemplateIngressIpFilterName": pwTemplateIngressIpFilterName,
       "pwTemplateIngressIpv6FilterName": pwTemplateIngressIpv6FilterName,
       "pwTemplateIngressMacFilterName": pwTemplateIngressMacFilterName,
       "pwTemplateEgressIpFilterName": pwTemplateEgressIpFilterName,
       "pwTemplateEgressIpv6FilterName": pwTemplateEgressIpv6FilterName,
       "pwTemplateEgressMacFilterName": pwTemplateEgressMacFilterName,
       "pwTemplateForceQinqVcFwding": pwTemplateForceQinqVcFwding,
       "pwTemplateIgmpSnpgGrpSrcTblLC": pwTemplateIgmpSnpgGrpSrcTblLC,
       "pwTemplateIgmpSnpgGrpSrcTable": pwTemplateIgmpSnpgGrpSrcTable,
       "pwTemplateIgmpSnpgGrpSrcEntry": pwTemplateIgmpSnpgGrpSrcEntry,
       "pwTemplateIgmpSnpgGrpAddrType": pwTemplateIgmpSnpgGrpAddrType,
       "pwTemplateIgmpSnpgGrpAddr": pwTemplateIgmpSnpgGrpAddr,
       "pwTemplateIgmpSnpgSrcAddrType": pwTemplateIgmpSnpgSrcAddrType,
       "pwTemplateIgmpSnpgSrcAddr": pwTemplateIgmpSnpgSrcAddr,
       "pwTemplateIgmpSnpgRowStatus": pwTemplateIgmpSnpgRowStatus,
       "pwTemplateIgmpSnpgLastChngd": pwTemplateIgmpSnpgLastChngd,
       "pwTemplateMfibAllowedMdaTblLC": pwTemplateMfibAllowedMdaTblLC,
       "pwTemplateMfibAllowedMdaTable": pwTemplateMfibAllowedMdaTable,
       "pwTemplateMfibAllowedMdaEntry": pwTemplateMfibAllowedMdaEntry,
       "pwTemplateMfibMdaRowStatus": pwTemplateMfibMdaRowStatus,
       "sdpBindTlsMrpTableLastChanged": sdpBindTlsMrpTableLastChanged,
       "sdpBindTlsMrpTable": sdpBindTlsMrpTable,
       "sdpBindTlsMrpEntry": sdpBindTlsMrpEntry,
       "sdpBindTlsMrpLastChngd": sdpBindTlsMrpLastChngd,
       "sdpBindTlsMrpJoinTime": sdpBindTlsMrpJoinTime,
       "sdpBindTlsMrpLeaveTime": sdpBindTlsMrpLeaveTime,
       "sdpBindTlsMrpLeaveAllTime": sdpBindTlsMrpLeaveAllTime,
       "sdpBindTlsMrpPeriodicTime": sdpBindTlsMrpPeriodicTime,
       "sdpBindTlsMrpPeriodicEnabled": sdpBindTlsMrpPeriodicEnabled,
       "sdpBindTlsMrpRxPdus": sdpBindTlsMrpRxPdus,
       "sdpBindTlsMrpDroppedPdus": sdpBindTlsMrpDroppedPdus,
       "sdpBindTlsMrpTxPdus": sdpBindTlsMrpTxPdus,
       "sdpBindTlsMrpRxNewEvent": sdpBindTlsMrpRxNewEvent,
       "sdpBindTlsMrpRxJoinInEvent": sdpBindTlsMrpRxJoinInEvent,
       "sdpBindTlsMrpRxInEvent": sdpBindTlsMrpRxInEvent,
       "sdpBindTlsMrpRxJoinEmptyEvent": sdpBindTlsMrpRxJoinEmptyEvent,
       "sdpBindTlsMrpRxEmptyEvent": sdpBindTlsMrpRxEmptyEvent,
       "sdpBindTlsMrpRxLeaveEvent": sdpBindTlsMrpRxLeaveEvent,
       "sdpBindTlsMrpTxNewEvent": sdpBindTlsMrpTxNewEvent,
       "sdpBindTlsMrpTxJoinInEvent": sdpBindTlsMrpTxJoinInEvent,
       "sdpBindTlsMrpTxInEvent": sdpBindTlsMrpTxInEvent,
       "sdpBindTlsMrpTxJoinEmptyEvent": sdpBindTlsMrpTxJoinEmptyEvent,
       "sdpBindTlsMrpTxEmptyEvent": sdpBindTlsMrpTxEmptyEvent,
       "sdpBindTlsMrpTxLeaveEvent": sdpBindTlsMrpTxLeaveEvent,
       "sdpBindTlsMrpPolicy": sdpBindTlsMrpPolicy,
       "sdpBindTlsMmrpTable": sdpBindTlsMmrpTable,
       "sdpBindTlsMmrpEntry": sdpBindTlsMmrpEntry,
       "sdpBindTlsMmrpMacAddr": sdpBindTlsMmrpMacAddr,
       "sdpBindTlsMmrpDeclared": sdpBindTlsMmrpDeclared,
       "sdpBindTlsMmrpRegistered": sdpBindTlsMmrpRegistered,
       "sdpBindTlsMmrpEndStation": sdpBindTlsMmrpEndStation,
       "sdpAutoBindBgpInfoTableLC": sdpAutoBindBgpInfoTableLC,
       "sdpAutoBindBgpInfoTable": sdpAutoBindBgpInfoTable,
       "sdpAutoBindBgpInfoEntry": sdpAutoBindBgpInfoEntry,
       "sdpAutoBindBgpInfoTemplateId": sdpAutoBindBgpInfoTemplateId,
       "sdpAutoBindBgpInfoAGI": sdpAutoBindBgpInfoAGI,
       "sdpAutoBindBgpInfoSAII": sdpAutoBindBgpInfoSAII,
       "sdpAutoBindBgpInfoTAII": sdpAutoBindBgpInfoTAII,
       "svcApplyEvalPwTemplate": svcApplyEvalPwTemplate,
       "svcApplyEvalPwTemplateSvcId": svcApplyEvalPwTemplateSvcId,
       "svcApplyEvalPwTemplateId": svcApplyEvalPwTemplateId,
       "svcApplyEvalPwTemplateAction": svcApplyEvalPwTemplateAction,
       "svcApplyEvalPwTemplateSuccess": svcApplyEvalPwTemplateSuccess,
       "svcApplyEvalPwTemplateErrorMsg": svcApplyEvalPwTemplateErrorMsg,
       "svcApplyEvalPwTemplateTime": svcApplyEvalPwTemplateTime,
       "sdpBindPbbTable": sdpBindPbbTable,
       "sdpBindPbbEntry": sdpBindPbbEntry,
       "sdpBindPbbSvcIdIVpls": sdpBindPbbSvcIdIVpls,
       "sdpBindPbbSvcIdBVpls": sdpBindPbbSvcIdBVpls,
       "sdpBindPbbId": sdpBindPbbId,
       "sdpBindPbbRowStatus": sdpBindPbbRowStatus,
       "sdpBindPbbLastMgmtChange": sdpBindPbbLastMgmtChange,
       "sdpBindPbbIgmpSnpgMRouter": sdpBindPbbIgmpSnpgMRouter,
       "sdpBindPbbMldSnpgMRouter": sdpBindPbbMldSnpgMRouter,
       "sdpBindFPropBMacAddrTblLastChgd": sdpBindFPropBMacAddrTblLastChgd,
       "sdpBindFPropBMacAddrTable": sdpBindFPropBMacAddrTable,
       "sdpBindFPropBMacAddrEntry": sdpBindFPropBMacAddrEntry,
       "sdpBindFPropBMacAddrOrMacNameTag": sdpBindFPropBMacAddrOrMacNameTag,
       "sdpBindFPropBMacAddrOrMacName": sdpBindFPropBMacAddrOrMacName,
       "sdpBindFPropBMacAddrRowStatus": sdpBindFPropBMacAddrRowStatus,
       "sdpAutoBindBgpVplsTableLC": sdpAutoBindBgpVplsTableLC,
       "sdpAutoBindBgpVplsTable": sdpAutoBindBgpVplsTable,
       "sdpAutoBindBgpVplsEntry": sdpAutoBindBgpVplsEntry,
       "sdpAutoBindBgpVplsTemplateId": sdpAutoBindBgpVplsTemplateId,
       "sdpAtBndBgp129Type2TableLC": sdpAtBndBgp129Type2TableLC,
       "sdpAtBndBgp129Type2Table": sdpAtBndBgp129Type2Table,
       "sdpAtBndBgp129Type2Entry": sdpAtBndBgp129Type2Entry,
       "sdpAtBndBgp129Type2TemplateId": sdpAtBndBgp129Type2TemplateId,
       "sdpAtBndBgp129Type2SaiiGlobalId": sdpAtBndBgp129Type2SaiiGlobalId,
       "sdpAtBndBgp129Type2SaiiPrefix": sdpAtBndBgp129Type2SaiiPrefix,
       "sdpAtBndBgp129Type2SaiiAcId": sdpAtBndBgp129Type2SaiiAcId,
       "sdpAtBndBgp129Type2TaiiGlobalId": sdpAtBndBgp129Type2TaiiGlobalId,
       "sdpAtBndBgp129Type2TaiiPrefix": sdpAtBndBgp129Type2TaiiPrefix,
       "sdpAtBndBgp129Type2TaiiAcId": sdpAtBndBgp129Type2TaiiAcId,
       "sdpBindEthCfmTableLastChanged": sdpBindEthCfmTableLastChanged,
       "sdpBindEthCfmTable": sdpBindEthCfmTable,
       "sdpBindEthCfmEntry": sdpBindEthCfmEntry,
       "sdpBindEthCfmRowLastChanged": sdpBindEthCfmRowLastChanged,
       "sdpBindEthCfmVMepFilter": sdpBindEthCfmVMepFilter,
       "sdpBindEthCfmSquelchIngress": sdpBindEthCfmSquelchIngress,
       "sdpBindEthCfmCollectLmmStats": sdpBindEthCfmCollectLmmStats,
       "sdpBindEthCfmCollLmmFcSts": sdpBindEthCfmCollLmmFcSts,
       "sdpBindEthCfmCollLmmFcStsInP": sdpBindEthCfmCollLmmFcStsInP,
       "sdpBindEthCfmSquelchIngressCtag": sdpBindEthCfmSquelchIngressCtag,
       "sdpBindTlsSpbTblLastChanged": sdpBindTlsSpbTblLastChanged,
       "sdpBindTlsSpbTable": sdpBindTlsSpbTable,
       "sdpBindTlsSpbEntry": sdpBindTlsSpbEntry,
       "sdpBindTlsSpbRowStatus": sdpBindTlsSpbRowStatus,
       "sdpBindTlsSpbLastChgd": sdpBindTlsSpbLastChgd,
       "sdpBindTlsSpbIfIndex": sdpBindTlsSpbIfIndex,
       "sdpBindTlsSpbAdminState": sdpBindTlsSpbAdminState,
       "sdpPwPortTblLastChanged": sdpPwPortTblLastChanged,
       "sdpPwPortTable": sdpPwPortTable,
       "sdpPwPortEntry": sdpPwPortEntry,
       "sdpPwPortId": sdpPwPortId,
       "sdpPwPortRowStatus": sdpPwPortRowStatus,
       "sdpPwPortLastChgd": sdpPwPortLastChgd,
       "sdpPwPortAdminStatus": sdpPwPortAdminStatus,
       "sdpPwPortVcId": sdpPwPortVcId,
       "sdpPwPortEncapType": sdpPwPortEncapType,
       "sdpPwPortOperStatus": sdpPwPortOperStatus,
       "sdpPwPortOperFlags": sdpPwPortOperFlags,
       "sdpPwPortVcType": sdpPwPortVcType,
       "sdpPwPortVlanVcTag": sdpPwPortVlanVcTag,
       "sdpPwPortEgrShapVPort": sdpPwPortEgrShapVPort,
       "sdpPwPortEgrShapDefIntDestId": sdpPwPortEgrShapDefIntDestId,
       "sdpPwPortEgrShapSapSecShaper": sdpPwPortEgrShapSapSecShaper,
       "sdpPwPortMonOperGrp": sdpPwPortMonOperGrp,
       "sdpPwPortIngVcLabel": sdpPwPortIngVcLabel,
       "sdpPwPortEgrVcLabel": sdpPwPortEgrVcLabel,
       "sdpPwPortControlWord": sdpPwPortControlWord,
       "sdpPwPortEntropyLabel": sdpPwPortEntropyLabel,
       "sdpPwPortAdvSvcMtu": sdpPwPortAdvSvcMtu,
       "sdpGrpTblLastChanged": sdpGrpTblLastChanged,
       "sdpGrpTable": sdpGrpTable,
       "sdpGrpEntry": sdpGrpEntry,
       "sdpGrpName": sdpGrpName,
       "sdpGrpRowStatus": sdpGrpRowStatus,
       "sdpGrpLastChange": sdpGrpLastChange,
       "sdpGrpValue": sdpGrpValue,
       "sdpSdpGrpTblLastChanged": sdpSdpGrpTblLastChanged,
       "sdpSdpGrpTable": sdpSdpGrpTable,
       "sdpSdpGrpEntry": sdpSdpGrpEntry,
       "sdpSdpGrpRowStatus": sdpSdpGrpRowStatus,
       "sdpSdpGrpLastChange": sdpSdpGrpLastChange,
       "pwTempIncSdpGrpTableLastChanged": pwTempIncSdpGrpTableLastChanged,
       "pwTempIncSdpGrpTable": pwTempIncSdpGrpTable,
       "pwTempIncSdpGrpEntry": pwTempIncSdpGrpEntry,
       "pwTempIncSdpGrpRowStatus": pwTempIncSdpGrpRowStatus,
       "pwTempIncSdpGrpLastChanged": pwTempIncSdpGrpLastChanged,
       "pwTempExcSdpGrpTableLastChanged": pwTempExcSdpGrpTableLastChanged,
       "pwTempExcSdpGrpTable": pwTempExcSdpGrpTable,
       "pwTempExcSdpGrpEntry": pwTempExcSdpGrpEntry,
       "pwTempExcSdpGrpRowStatus": pwTempExcSdpGrpRowStatus,
       "pwTempExcSdpGrpLastChanged": pwTempExcSdpGrpLastChanged,
       "sdpBindPwPathTableLastChanged": sdpBindPwPathTableLastChanged,
       "sdpBindPwPathTable": sdpBindPwPathTable,
       "sdpBindPwPathEntry": sdpBindPwPathEntry,
       "sdpBindPwPathRowStatus": sdpBindPwPathRowStatus,
       "sdpBindPwPathLastChanged": sdpBindPwPathLastChanged,
       "sdpBindPwPathAgi": sdpBindPwPathAgi,
       "sdpBindPwPathSaiiGlobalId": sdpBindPwPathSaiiGlobalId,
       "sdpBindPwPathSaiiNodeId": sdpBindPwPathSaiiNodeId,
       "sdpBindPwPathSaiiAcId": sdpBindPwPathSaiiAcId,
       "sdpBindPwPathTaiiGlobalId": sdpBindPwPathTaiiGlobalId,
       "sdpBindPwPathTaiiNodeId": sdpBindPwPathTaiiNodeId,
       "sdpBindPwPathTaiiAcId": sdpBindPwPathTaiiAcId,
       "sdpBindCtrlChanPwTableLastChgd": sdpBindCtrlChanPwTableLastChgd,
       "sdpBindCtrlChanPwTable": sdpBindCtrlChanPwTable,
       "sdpBindCtrlChanPwEntry": sdpBindCtrlChanPwEntry,
       "sdpBindCtrlChanPwLastChanged": sdpBindCtrlChanPwLastChanged,
       "sdpBindCtrlChanPwStatus": sdpBindCtrlChanPwStatus,
       "sdpBindCtrlChanPwRefreshTimer": sdpBindCtrlChanPwRefreshTimer,
       "sdpBindCtrlChanPwPeerExpired": sdpBindCtrlChanPwPeerExpired,
       "sdpBindCtrlChanPwRequestTimer": sdpBindCtrlChanPwRequestTimer,
       "sdpBindCtrlChanPwRetryTimer": sdpBindCtrlChanPwRetryTimer,
       "sdpBindCtrlChanPwTimeoutMult": sdpBindCtrlChanPwTimeoutMult,
       "sdpBindCtrlChanPwAck": sdpBindCtrlChanPwAck,
       "sdpAutoBindBgpVpwsTable": sdpAutoBindBgpVpwsTable,
       "sdpAutoBindBgpVpwsEntry": sdpAutoBindBgpVpwsEntry,
       "sdpAutoBindBgpVpwsTemplateId": sdpAutoBindBgpVpwsTemplateId,
       "sdpBindL2tpv3Table": sdpBindL2tpv3Table,
       "sdpBindL2tpv3Entry": sdpBindL2tpv3Entry,
       "sdpBindL2tpv3IngressCookie": sdpBindL2tpv3IngressCookie,
       "sdpBindL2tpv3EgressCookie": sdpBindL2tpv3EgressCookie,
       "sdpBindL2tpv3SessMismatch": sdpBindL2tpv3SessMismatch,
       "sdpBindL2tpv3SessMismatchLstClrd": sdpBindL2tpv3SessMismatchLstClrd,
       "sdpBindL2tpv3IngressCookie2": sdpBindL2tpv3IngressCookie2,
       "sdpBindTlsStaticIsidRngTable": sdpBindTlsStaticIsidRngTable,
       "sdpBindTlsStaticIsidRngEntry": sdpBindTlsStaticIsidRngEntry,
       "sdpBindTlsStaticIsidRngId": sdpBindTlsStaticIsidRngId,
       "sdpBindTlsStaticIsidRngRowStatus": sdpBindTlsStaticIsidRngRowStatus,
       "sdpBindTlsStaticIsidRngLastChgd": sdpBindTlsStaticIsidRngLastChgd,
       "sdpBindTlsStaticIsidRngLow": sdpBindTlsStaticIsidRngLow,
       "sdpBindTlsStaticIsidRngHigh": sdpBindTlsStaticIsidRngHigh,
       "sdpBindDhcp6InfoTable": sdpBindDhcp6InfoTable,
       "sdpBindDhcp6InfoEntry": sdpBindDhcp6InfoEntry,
       "sdpBindDhcp6Description": sdpBindDhcp6Description,
       "sdpBindDhcp6Snoop": sdpBindDhcp6Snoop,
       "sdpBindTlsStaticIsidTable": sdpBindTlsStaticIsidTable,
       "sdpBindTlsStaticIsidEntry": sdpBindTlsStaticIsidEntry,
       "sdpBindTlsStaticIsid": sdpBindTlsStaticIsid,
       "sdpBindTlsStaticIsidStatus": sdpBindTlsStaticIsidStatus,
       "sdpBindEthLoopbackTable": sdpBindEthLoopbackTable,
       "sdpBindEthLoopbackEntry": sdpBindEthLoopbackEntry,
       "sdpBindEthLoopbackRowStatus": sdpBindEthLoopbackRowStatus,
       "sdpBindEthLoopbackMode": sdpBindEthLoopbackMode,
       "sdpBindEthLoopbackMacSwap": sdpBindEthLoopbackMacSwap,
       "sdpBindEthLoopbackMacSwapAddr": sdpBindEthLoopbackMacSwapAddr,
       "sdpBindEthLoopbackMacSwapAddrAll": sdpBindEthLoopbackMacSwapAddrAll,
       "sdpBindTlsFdbMacStatsTable": sdpBindTlsFdbMacStatsTable,
       "sdpBindTlsFdbMacStatsEntry": sdpBindTlsFdbMacStatsEntry,
       "sdpBindTlsFdbMacStatsNumEntries": sdpBindTlsFdbMacStatsNumEntries,
       "sdpBindPwLoopbackTable": sdpBindPwLoopbackTable,
       "sdpBindPwLoopbackEntry": sdpBindPwLoopbackEntry,
       "sdpBindPwLoopbackRowStatus": sdpBindPwLoopbackRowStatus,
       "sdpBindPwAdminLockTable": sdpBindPwAdminLockTable,
       "sdpBindPwAdminLockEntry": sdpBindPwAdminLockEntry,
       "sdpBindPwAdminLockRowStatus": sdpBindPwAdminLockRowStatus,
       "sdpBindPwAdminLockTestSvc": sdpBindPwAdminLockTestSvc,
       "pwTemplateAugTableLastChgd": pwTemplateAugTableLastChgd,
       "pwTemplateAugTable": pwTemplateAugTable,
       "pwTemplateAugEntry": pwTemplateAugEntry,
       "pwTemplateAugLastChgd": pwTemplateAugLastChgd,
       "pwTemplateAugStpAutoEdge": pwTemplateAugStpAutoEdge,
       "pwTemplateAugStpRapidStart": pwTemplateAugStpRapidStart,
       "pwTemplateAugStpAdminPtToPt": pwTemplateAugStpAdminPtToPt,
       "pwTemplateAugStpPathCost": pwTemplateAugStpPathCost,
       "pwTemplateAugStpPriority": pwTemplateAugStpPriority,
       "pwTemplateAugStpRootGuard": pwTemplateAugStpRootGuard,
       "pwTemplateAugStpAdminStatus": pwTemplateAugStpAdminStatus,
       "pwTemplateAugL2ptTermination": pwTemplateAugL2ptTermination,
       "pwTemplateAugL2ptProtocols": pwTemplateAugL2ptProtocols,
       "pwTemplateAugGreAllowFrag": pwTemplateAugGreAllowFrag,
       "pwTemplateAugAluNgeKeyGroupIn": pwTemplateAugAluNgeKeyGroupIn,
       "pwTemplateAugAluNgeKeyGroupOut": pwTemplateAugAluNgeKeyGroupOut,
       "pwTemplateAugAtLnMacPrtExcList": pwTemplateAugAtLnMacPrtExcList,
       "sdpSegRouteTableLastChgd": sdpSegRouteTableLastChgd,
       "sdpSegRouteTable": sdpSegRouteTable,
       "sdpSegRouteEntry": sdpSegRouteEntry,
       "sdpSegRouteIsIs": sdpSegRouteIsIs,
       "sdpSegRouteIsIsOperInstId": sdpSegRouteIsIsOperInstId,
       "sdpSegRouteIsIsLspId": sdpSegRouteIsIsLspId,
       "sdpSegRouteOspf": sdpSegRouteOspf,
       "sdpSegRouteOspfOperInstId": sdpSegRouteOspfOperInstId,
       "sdpSegRouteOspfLspId": sdpSegRouteOspfLspId,
       "sdpSegRouteTeOperInstId": sdpSegRouteTeOperInstId,
       "sdpEvpnMHEthSegTable": sdpEvpnMHEthSegTable,
       "sdpEvpnMHEthSegEntry": sdpEvpnMHEthSegEntry,
       "sdpEvpnMHEthSegName": sdpEvpnMHEthSegName,
       "sdpEvpnMHEthSegStatus": sdpEvpnMHEthSegStatus,
       "sdpBindExtTableLastChanged": sdpBindExtTableLastChanged,
       "sdpBindExtTable": sdpBindExtTable,
       "sdpBindExtEntry": sdpBindExtEntry,
       "sdpBindExtEntropyLabel": sdpBindExtEntropyLabel,
       "sdpBindExtLastMgmtChange": sdpBindExtLastMgmtChange,
       "sdpBindExtBfdFailAction": sdpBindExtBfdFailAction,
       "sdpBindExtBfdSessStatOperState": sdpBindExtBfdSessStatOperState,
       "sdpBindExtBfdWaitForUpTimer": sdpBindExtBfdWaitForUpTimer,
       "sdpBindExtBfdUpTimeRemain": sdpBindExtBfdUpTimeRemain,
       "sdpSegRouteTeLspTableLastChgd": sdpSegRouteTeLspTableLastChgd,
       "sdpSegRouteTeLspTable": sdpSegRouteTeLspTable,
       "sdpSegRouteTeLspEntry": sdpSegRouteTeLspEntry,
       "sdpSegRouteTeLspId": sdpSegRouteTeLspId,
       "sdpSegRouteTeLspRowStatus": sdpSegRouteTeLspRowStatus,
       "sdpSegRouteTeLspLastChanged": sdpSegRouteTeLspLastChanged,
       "sdpMplsLspTableLastChgd": sdpMplsLspTableLastChgd,
       "sdpMplsLspTable": sdpMplsLspTable,
       "sdpMplsLspEntry": sdpMplsLspEntry,
       "sdpMplsLspId": sdpMplsLspId,
       "sdpMplsLspRowStatus": sdpMplsLspRowStatus,
       "sdpMplsLspLastChanged": sdpMplsLspLastChanged,
       "sdpBindExt2TableLastChgd": sdpBindExt2TableLastChgd,
       "sdpBindExt2Table": sdpBindExt2Table,
       "sdpBindExt2Entry": sdpBindExt2Entry,
       "sdpBindExt2LastMgmtChange": sdpBindExt2LastMgmtChange,
       "sdpBindExt2AdvSvcMtu": sdpBindExt2AdvSvcMtu,
       "sdpBindTableLastChanged": sdpBindTableLastChanged,
       "sdpBindTlsTableLastChanged": sdpBindTlsTableLastChanged,
       "tmnxSdpNotifyObjs": tmnxSdpNotifyObjs,
       "sdpNotifySdpId": sdpNotifySdpId,
       "dynamicSdpStatus": dynamicSdpStatus,
       "dynamicSdpOrigin": dynamicSdpOrigin,
       "dynamicSdpCreationError": dynamicSdpCreationError,
       "dynamicSdpBindCreationError": dynamicSdpBindCreationError,
       "sdpBindNotifyMacAddr": sdpBindNotifyMacAddr,
       "sdpEgIfNetDomainInconsCount": sdpEgIfNetDomainInconsCount,
       "sdpMSPwPeId": sdpMSPwPeId,
       "sdpBindIpipeCeIpAddrType": sdpBindIpipeCeIpAddrType,
       "sdpBindIpipeCeIpAddress": sdpBindIpipeCeIpAddress,
       "sdpPbbActvPwWithNonActvCtrlPw": sdpPbbActvPwWithNonActvCtrlPw,
       "sdpTrapsPrefix": sdpTrapsPrefix,
       "sdpTraps": sdpTraps,
       "sdpCreated": sdpCreated,
       "sdpDeleted": sdpDeleted,
       "sdpStatusChanged": sdpStatusChanged,
       "sdpBindCreated": sdpBindCreated,
       "sdpBindDeleted": sdpBindDeleted,
       "sdpBindStatusChanged": sdpBindStatusChanged,
       "sdpTlsMacAddrLimitAlarmRaised": sdpTlsMacAddrLimitAlarmRaised,
       "sdpTlsMacAddrLimitAlarmCleared": sdpTlsMacAddrLimitAlarmCleared,
       "sdpTlsDHCPSuspiciousPcktRcvd": sdpTlsDHCPSuspiciousPcktRcvd,
       "sdpBindDHCPLeaseEntriesExceeded": sdpBindDHCPLeaseEntriesExceeded,
       "sdpBindDHCPLseStateOverride": sdpBindDHCPLseStateOverride,
       "sdpBindDHCPSuspiciousPcktRcvd": sdpBindDHCPSuspiciousPcktRcvd,
       "sdpBindDHCPLseStatePopulateErr": sdpBindDHCPLseStatePopulateErr,
       "sdpBindPwPeerStatusBitsChanged": sdpBindPwPeerStatusBitsChanged,
       "sdpBindTlsMacMoveExceeded": sdpBindTlsMacMoveExceeded,
       "sdpBindPwPeerFaultAddrChanged": sdpBindPwPeerFaultAddrChanged,
       "sdpBindDHCPProxyServerError": sdpBindDHCPProxyServerError,
       "sdpBindDHCPCoAError": sdpBindDHCPCoAError,
       "sdpBindDHCPSubAuthError": sdpBindDHCPSubAuthError,
       "sdpBindSdpStateChangeProcessed": sdpBindSdpStateChangeProcessed,
       "sdpBindDHCPLseStateMobilityErr": sdpBindDHCPLseStateMobilityErr,
       "sdpBandwidthOverbooked": sdpBandwidthOverbooked,
       "sdpBindInsufficientBandwidth": sdpBindInsufficientBandwidth,
       "dynamicSdpConfigChanged": dynamicSdpConfigChanged,
       "dynamicSdpBindConfigChanged": dynamicSdpBindConfigChanged,
       "dynamicSdpCreationFailed": dynamicSdpCreationFailed,
       "dynamicSdpBindCreationFailed": dynamicSdpBindCreationFailed,
       "sdpEgrIfsNetDomInconsCntChanged": sdpEgrIfsNetDomInconsCntChanged,
       "sdpBindIpipeCeIpAddressChange": sdpBindIpipeCeIpAddressChange,
       "sdpBindReceivedProtSrcMac": sdpBindReceivedProtSrcMac,
       "sdpBindPwLocalStatusBitsChanged": sdpBindPwLocalStatusBitsChanged,
       "sdpBindTlsMacMoveExceedNonBlock": sdpBindTlsMacMoveExceedNonBlock,
       "sdpBindEthLoopbackStarted": sdpBindEthLoopbackStarted,
       "sdpBindEthLoopbackStopped": sdpBindEthLoopbackStopped,
       "sdpPbbActvPwWithNonActvCtrlPwChg": sdpPbbActvPwWithNonActvCtrlPwChg,
       "sdpControlPwActiveStateChg": sdpControlPwActiveStateChg,
       "sdpBindReceivedPbbProtSrcMac": sdpBindReceivedPbbProtSrcMac,
       "unacknowledgedTCN": unacknowledgedTCN,
       "tmnxSvcTopoChgSdpBindMajorState": tmnxSvcTopoChgSdpBindMajorState,
       "tmnxSvcNewRootSdpBind": tmnxSvcNewRootSdpBind,
       "tmnxSvcTopoChgSdpBindState": tmnxSvcTopoChgSdpBindState,
       "tmnxSvcSdpBindRcvdTCN": tmnxSvcSdpBindRcvdTCN,
       "tmnxSvcSdpBindRcvdHigherBriPrio": tmnxSvcSdpBindRcvdHigherBriPrio,
       "tmnxSvcSdpBindEncapPVST": tmnxSvcSdpBindEncapPVST,
       "tmnxSvcSdpBindEncapDot1d": tmnxSvcSdpBindEncapDot1d,
       "tmnxSvcSdpActiveProtocolChange": tmnxSvcSdpActiveProtocolChange,
       "tmnxStpMeshNotInMstRegion": tmnxStpMeshNotInMstRegion,
       "tmnxSdpBndStpExcepCondStateChng": tmnxSdpBndStpExcepCondStateChng}
)
