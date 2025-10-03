# SNMP MIB module (TIMETRA-MPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\TIMETRA-MPLS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:17:22 2025
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
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType")

(MplsLSPID,
 MplsLabel,
 mplsInSegmentEntry,
 mplsOutSegmentEntry,
 mplsXCLspId) = mibBuilder.importSymbols(
    "MPLS-LSR-MIB",
    "MplsLSPID",
    "MplsLabel",
    "mplsInSegmentEntry",
    "mplsOutSegmentEntry",
    "mplsXCLspId")

(MplsTunnelIndex,
 mplsTunnelARHopEntry,
 mplsTunnelIndex,
 mplsTunnelIngressLSRId,
 mplsTunnelInstance) = mibBuilder.importSymbols(
    "MPLS-TE-MIB",
    "MplsTunnelIndex",
    "mplsTunnelARHopEntry",
    "mplsTunnelIndex",
    "mplsTunnelIngressLSRId",
    "mplsTunnelInstance")

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
 RowPointer,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TFCType,
 TLNamedItem,
 TLNamedItemOrEmpty,
 TNamedItem,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TmnxActionType,
 TmnxAdminState,
 TmnxCBFClasses,
 TmnxEnabledDisabled,
 TmnxMplsLabel,
 TmnxMplsLabelOrZero,
 TmnxMplsLspBandwidth,
 TmnxMplsTpGlobalID,
 TmnxMplsTpNodeID,
 TmnxNhgDownReason,
 TmnxOperState,
 TmnxRsvpDSTEClassType,
 TmnxTimeInterval,
 TmnxVRtrMplsLspID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TFCType",
    "TLNamedItem",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxCBFClasses",
    "TmnxEnabledDisabled",
    "TmnxMplsLabel",
    "TmnxMplsLabelOrZero",
    "TmnxMplsLspBandwidth",
    "TmnxMplsTpGlobalID",
    "TmnxMplsTpNodeID",
    "TmnxNhgDownReason",
    "TmnxOperState",
    "TmnxRsvpDSTEClassType",
    "TmnxTimeInterval",
    "TmnxVRtrMplsLspID")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraMplsMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    timetraMplsMIBModule.setRevisions(
        ("2017-01-01 00:00",
         "2016-01-01 00:00",
         "2015-01-01 00:00",
         "2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-03-23 00:00",
         "2005-08-31 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2000-09-07 00:00",
         "2000-08-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxMplsLspFailCode(TextualConvention, Integer32):
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
              64)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("admissionControlError", 1),
          ("noRouteToDestination", 2),
          ("trafficControlSystemError", 3),
          ("routingError", 4),
          ("noResourcesAvailable", 5),
          ("badNode", 6),
          ("routingLoop", 7),
          ("labelAllocationError", 8),
          ("badL3PID", 9),
          ("tunnelLocallyRepaired", 10),
          ("unknownObjectClass", 11),
          ("unknownCType", 12),
          ("noEgressMplsInterface", 13),
          ("noEgressRsvpInterface", 14),
          ("looseHopsInFRRLsp", 15),
          ("unknown", 16),
          ("retryExceeded", 17),
          ("noCspfRouteOwner", 18),
          ("noCspfRouteToDestination", 19),
          ("hopLimitExceeded", 20),
          ("looseHopsInManualBypassLsp", 21),
          ("emptyPathInManualBypassLsp", 22),
          ("lspFlowControlled", 23),
          ("srlgSecondaryNotDisjoint", 24),
          ("srlgPrimaryCspfDisabled", 25),
          ("srlgPrimaryPathDown", 26),
          ("localLinkMaintenance", 27),
          ("unexpectedCtObject", 28),
          ("unsupportedCt", 29),
          ("invalidCt", 30),
          ("invCtAndSetupPri", 31),
          ("invCtAndHoldPri", 32),
          ("invCtAndSetupAndHoldPri", 33),
          ("localNodeMaintenance", 34),
          ("softPreemption", 35),
          ("p2mpNotSupported", 36),
          ("badXro", 37),
          ("localNodeInXro", 38),
          ("routeBlockedByXro", 39),
          ("xroTooComplex", 40),
          ("rsvpNotSupported", 41),
          ("conflictingAdminGroups", 42),
          ("nodeInIgpOverload", 43),
          ("srTunnelDown", 44),
          ("fibAddFailed", 45),
          ("labelStackExceeded", 46),
          ("pccDown", 47),
          ("pccError", 48),
          ("pceDown", 49),
          ("pceError", 50),
          ("pceUpdateWithEmptyEro", 51),
          ("pceInitLspDisabled", 52),
          ("adminDown", 53),
          ("sidHopsInRsvpLsp", 54),
          ("ipv6HopsInRsvpLsp", 55),
          ("ipv4HopsInIpv6Lsp", 56),
          ("ipv6HopsInIpv4Lsp", 57),
          ("sidHopsInIpv6Lsp", 58),
          ("srlgPathWithSidHops", 59),
          ("mplsV4Down", 60),
          ("mplsV6Down", 61),
          ("lspAdminDown", 62),
          ("pathAdminDown", 63),
          ("templateAdminDown", 64))
    )



class TmnxMplsLabelOwner(TextualConvention, Integer32):
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
        *(("none", 0),
          ("rsvp", 1),
          ("tldp", 2),
          ("ildp", 3),
          ("svcmgr", 4),
          ("bgp", 5),
          ("mirror", 6),
          ("static", 7),
          ("vprn", 8),
          ("sr", 9))
    )



class TmnxMplsOperDownReasonCode(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("operUp", 0),
          ("adminDown", 1),
          ("noResources", 2),
          ("systemIpDown", 3),
          ("iomFailure", 4),
          ("clearDown", 5),
          ("ipv6TeRtrDown", 6),
          ("ipv6TeRtrAddrChanged", 7),
          ("ipv6TeRtrIdIntfDown", 8))
    )



class TmnxMplsMBBType(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("configChange", 1),
          ("timerBasedResignal", 2),
          ("manualResignal", 3),
          ("globalRevert", 4),
          ("delayedRetry", 5),
          ("gracefulShutdown", 6),
          ("softPreemption", 7),
          ("pathChange", 8),
          ("autoBandwidth", 9),
          ("pceLspUpdate", 10))
    )



class TmnxMplsP2mpInstFailCode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("noS2LOperational", 1))
    )



class TmnxMplsRouterId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class TmnxMplsLspAutoBWLastAdjCause(TextualConvention, Integer32):
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
        *(("none", 0),
          ("manual", 1),
          ("normal", 2),
          ("overflow", 3),
          ("vllCAC", 4),
          ("underflow", 5),
          ("activePathChange", 6))
    )



class TmnxMplsLspBgpRSVPLSPTunState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )



class TmnxMplsLspAddrType(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("ipv4", 1),
          ("nodeId", 2),
          ("ipv6", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxMplsConformance_ObjectIdentity = ObjectIdentity
tmnxMplsConformance = _TmnxMplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6)
)
_TmnxMplsCompliances_ObjectIdentity = ObjectIdentity
tmnxMplsCompliances = _TmnxMplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1)
)
_TmnxMplsGroups_ObjectIdentity = ObjectIdentity
tmnxMplsGroups = _TmnxMplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2)
)
_TmnxMplsObjs_ObjectIdentity = ObjectIdentity
tmnxMplsObjs = _TmnxMplsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6)
)
_VRtrMplsLspTable_Object = MibTable
vRtrMplsLspTable = _VRtrMplsLspTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsLspTable.setStatus("current")
_VRtrMplsLspEntry_Object = MibTableRow
vRtrMplsLspEntry = _VRtrMplsLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1)
)
vRtrMplsLspEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspEntry.setStatus("current")
_VRtrMplsLspIndex_Type = TmnxVRtrMplsLspID
_VRtrMplsLspIndex_Object = MibTableColumn
vRtrMplsLspIndex = _VRtrMplsLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 1),
    _VRtrMplsLspIndex_Type()
)
vRtrMplsLspIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspIndex.setStatus("current")
_VRtrMplsLspRowStatus_Type = RowStatus
_VRtrMplsLspRowStatus_Object = MibTableColumn
vRtrMplsLspRowStatus = _VRtrMplsLspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 2),
    _VRtrMplsLspRowStatus_Type()
)
vRtrMplsLspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRowStatus.setStatus("current")
_VRtrMplsLspLastChange_Type = TimeStamp
_VRtrMplsLspLastChange_Object = MibTableColumn
vRtrMplsLspLastChange = _VRtrMplsLspLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 3),
    _VRtrMplsLspLastChange_Type()
)
vRtrMplsLspLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspLastChange.setStatus("current")
_VRtrMplsLspName_Type = TLNamedItemOrEmpty
_VRtrMplsLspName_Object = MibTableColumn
vRtrMplsLspName = _VRtrMplsLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 4),
    _VRtrMplsLspName_Type()
)
vRtrMplsLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspName.setStatus("current")


class _VRtrMplsLspAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsLspAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsLspAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsLspAdminState_Object = MibTableColumn
vRtrMplsLspAdminState = _VRtrMplsLspAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 5),
    _VRtrMplsLspAdminState_Type()
)
vRtrMplsLspAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAdminState.setStatus("current")
_VRtrMplsLspOperState_Type = TmnxOperState
_VRtrMplsLspOperState_Object = MibTableColumn
vRtrMplsLspOperState = _VRtrMplsLspOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 6),
    _VRtrMplsLspOperState_Type()
)
vRtrMplsLspOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOperState.setStatus("current")
_VRtrMplsLspFromAddr_Type = IpAddress
_VRtrMplsLspFromAddr_Object = MibTableColumn
vRtrMplsLspFromAddr = _VRtrMplsLspFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 7),
    _VRtrMplsLspFromAddr_Type()
)
vRtrMplsLspFromAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFromAddr.setStatus("obsolete")
_VRtrMplsLspToAddr_Type = IpAddress
_VRtrMplsLspToAddr_Object = MibTableColumn
vRtrMplsLspToAddr = _VRtrMplsLspToAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 8),
    _VRtrMplsLspToAddr_Type()
)
vRtrMplsLspToAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspToAddr.setStatus("obsolete")


class _VRtrMplsLspType_Type(Integer32):
    """Custom type vRtrMplsLspType based on Integer32"""
    defaultValue = 2

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
              15)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("dynamic", 2),
          ("static", 3),
          ("bypassOnly", 4),
          ("p2mpLsp", 5),
          ("p2mpAuto", 6),
          ("mplsTp", 7),
          ("meshP2p", 8),
          ("oneHopP2p", 9),
          ("srTe", 10),
          ("meshP2pSrTe", 11),
          ("oneHopP2pSrTe", 12),
          ("pceInitP2pSrTe", 13),
          ("onDemandP2pSrTe", 15))
    )


_VRtrMplsLspType_Type.__name__ = "Integer32"
_VRtrMplsLspType_Object = MibTableColumn
vRtrMplsLspType = _VRtrMplsLspType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 9),
    _VRtrMplsLspType_Type()
)
vRtrMplsLspType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspType.setStatus("current")


class _VRtrMplsLspOutSegIndx_Type(Integer32):
    """Custom type vRtrMplsLspOutSegIndx based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrMplsLspOutSegIndx_Type.__name__ = "Integer32"
_VRtrMplsLspOutSegIndx_Object = MibTableColumn
vRtrMplsLspOutSegIndx = _VRtrMplsLspOutSegIndx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 10),
    _VRtrMplsLspOutSegIndx_Type()
)
vRtrMplsLspOutSegIndx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspOutSegIndx.setStatus("current")


class _VRtrMplsLspRetryTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspRetryTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_VRtrMplsLspRetryTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspRetryTimer_Object = MibTableColumn
vRtrMplsLspRetryTimer = _VRtrMplsLspRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 11),
    _VRtrMplsLspRetryTimer_Type()
)
vRtrMplsLspRetryTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspRetryTimer.setUnits("seconds")


class _VRtrMplsLspRetryLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspRetryLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VRtrMplsLspRetryLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspRetryLimit_Object = MibTableColumn
vRtrMplsLspRetryLimit = _VRtrMplsLspRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 12),
    _VRtrMplsLspRetryLimit_Type()
)
vRtrMplsLspRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRetryLimit.setStatus("current")


class _VRtrMplsLspMetric_Type(Unsigned32):
    """Custom type vRtrMplsLspMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16777215),
    )


_VRtrMplsLspMetric_Type.__name__ = "Unsigned32"
_VRtrMplsLspMetric_Object = MibTableColumn
vRtrMplsLspMetric = _VRtrMplsLspMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 13),
    _VRtrMplsLspMetric_Type()
)
vRtrMplsLspMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspMetric.setStatus("current")


class _VRtrMplsLspDecrementTtl_Type(TruthValue):
    """Custom type vRtrMplsLspDecrementTtl based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspDecrementTtl_Type.__name__ = "TruthValue"
_VRtrMplsLspDecrementTtl_Object = MibTableColumn
vRtrMplsLspDecrementTtl = _VRtrMplsLspDecrementTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 14),
    _VRtrMplsLspDecrementTtl_Type()
)
vRtrMplsLspDecrementTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspDecrementTtl.setStatus("obsolete")


class _VRtrMplsLspCspf_Type(TruthValue):
    """Custom type vRtrMplsLspCspf based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspCspf_Type.__name__ = "TruthValue"
_VRtrMplsLspCspf_Object = MibTableColumn
vRtrMplsLspCspf = _VRtrMplsLspCspf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 15),
    _VRtrMplsLspCspf_Type()
)
vRtrMplsLspCspf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspCspf.setStatus("obsolete")


class _VRtrMplsLspFastReroute_Type(TruthValue):
    """Custom type vRtrMplsLspFastReroute based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspFastReroute_Type.__name__ = "TruthValue"
_VRtrMplsLspFastReroute_Object = MibTableColumn
vRtrMplsLspFastReroute = _VRtrMplsLspFastReroute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 16),
    _VRtrMplsLspFastReroute_Type()
)
vRtrMplsLspFastReroute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFastReroute.setStatus("current")


class _VRtrMplsLspFRHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspFRHopLimit based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrMplsLspFRHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspFRHopLimit_Object = MibTableColumn
vRtrMplsLspFRHopLimit = _VRtrMplsLspFRHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 17),
    _VRtrMplsLspFRHopLimit_Type()
)
vRtrMplsLspFRHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRHopLimit.setStatus("current")


class _VRtrMplsLspFRBandwidth_Type(Unsigned32):
    """Custom type vRtrMplsLspFRBandwidth based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspFRBandwidth_Type.__name__ = "Unsigned32"
_VRtrMplsLspFRBandwidth_Object = MibTableColumn
vRtrMplsLspFRBandwidth = _VRtrMplsLspFRBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 18),
    _VRtrMplsLspFRBandwidth_Type()
)
vRtrMplsLspFRBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspFRBandwidth.setUnits("megabps")


class _VRtrMplsLspClassOfService_Type(TNamedItemOrEmpty):
    """Custom type vRtrMplsLspClassOfService based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrMplsLspClassOfService_Type.__name__ = "TNamedItemOrEmpty"
_VRtrMplsLspClassOfService_Object = MibTableColumn
vRtrMplsLspClassOfService = _VRtrMplsLspClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 19),
    _VRtrMplsLspClassOfService_Type()
)
vRtrMplsLspClassOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspClassOfService.setStatus("obsolete")


class _VRtrMplsLspSetupPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspSetupPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspSetupPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspSetupPriority_Object = MibTableColumn
vRtrMplsLspSetupPriority = _VRtrMplsLspSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 20),
    _VRtrMplsLspSetupPriority_Type()
)
vRtrMplsLspSetupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspSetupPriority.setStatus("current")


class _VRtrMplsLspHoldPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspHoldPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspHoldPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspHoldPriority_Object = MibTableColumn
vRtrMplsLspHoldPriority = _VRtrMplsLspHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 21),
    _VRtrMplsLspHoldPriority_Type()
)
vRtrMplsLspHoldPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspHoldPriority.setStatus("current")


class _VRtrMplsLspRecord_Type(TruthValue):
    """Custom type vRtrMplsLspRecord based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspRecord_Type.__name__ = "TruthValue"
_VRtrMplsLspRecord_Object = MibTableColumn
vRtrMplsLspRecord = _VRtrMplsLspRecord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 22),
    _VRtrMplsLspRecord_Type()
)
vRtrMplsLspRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRecord.setStatus("current")


class _VRtrMplsLspPreference_Type(Unsigned32):
    """Custom type vRtrMplsLspPreference based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrMplsLspPreference_Type.__name__ = "Unsigned32"
_VRtrMplsLspPreference_Object = MibTableColumn
vRtrMplsLspPreference = _VRtrMplsLspPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 23),
    _VRtrMplsLspPreference_Type()
)
vRtrMplsLspPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPreference.setStatus("obsolete")


class _VRtrMplsLspBandwidth_Type(Integer32):
    """Custom type vRtrMplsLspBandwidth based on Integer32"""
    defaultValue = 0


_VRtrMplsLspBandwidth_Type.__name__ = "Integer32"
_VRtrMplsLspBandwidth_Object = MibTableColumn
vRtrMplsLspBandwidth = _VRtrMplsLspBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 24),
    _VRtrMplsLspBandwidth_Type()
)
vRtrMplsLspBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBandwidth.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrMplsLspBandwidth.setUnits("megabps")


class _VRtrMplsLspBwProtect_Type(TruthValue):
    """Custom type vRtrMplsLspBwProtect based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspBwProtect_Type.__name__ = "TruthValue"
_VRtrMplsLspBwProtect_Object = MibTableColumn
vRtrMplsLspBwProtect = _VRtrMplsLspBwProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 25),
    _VRtrMplsLspBwProtect_Type()
)
vRtrMplsLspBwProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBwProtect.setStatus("obsolete")


class _VRtrMplsLspHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspHopLimit based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_VRtrMplsLspHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspHopLimit_Object = MibTableColumn
vRtrMplsLspHopLimit = _VRtrMplsLspHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 26),
    _VRtrMplsLspHopLimit_Type()
)
vRtrMplsLspHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspHopLimit.setStatus("current")


class _VRtrMplsLspNegotiatedMTU_Type(Unsigned32):
    """Custom type vRtrMplsLspNegotiatedMTU based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspNegotiatedMTU_Type.__name__ = "Unsigned32"
_VRtrMplsLspNegotiatedMTU_Object = MibTableColumn
vRtrMplsLspNegotiatedMTU = _VRtrMplsLspNegotiatedMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 27),
    _VRtrMplsLspNegotiatedMTU_Type()
)
vRtrMplsLspNegotiatedMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspNegotiatedMTU.setStatus("current")


class _VRtrMplsLspRsvpResvStyle_Type(Integer32):
    """Custom type vRtrMplsLspRsvpResvStyle based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("se", 1),
          ("ff", 2))
    )


_VRtrMplsLspRsvpResvStyle_Type.__name__ = "Integer32"
_VRtrMplsLspRsvpResvStyle_Object = MibTableColumn
vRtrMplsLspRsvpResvStyle = _VRtrMplsLspRsvpResvStyle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 28),
    _VRtrMplsLspRsvpResvStyle_Type()
)
vRtrMplsLspRsvpResvStyle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRsvpResvStyle.setStatus("current")


class _VRtrMplsLspRsvpAdspec_Type(TruthValue):
    """Custom type vRtrMplsLspRsvpAdspec based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspRsvpAdspec_Type.__name__ = "TruthValue"
_VRtrMplsLspRsvpAdspec_Object = MibTableColumn
vRtrMplsLspRsvpAdspec = _VRtrMplsLspRsvpAdspec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 29),
    _VRtrMplsLspRsvpAdspec_Type()
)
vRtrMplsLspRsvpAdspec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRsvpAdspec.setStatus("current")


class _VRtrMplsLspFRMethod_Type(Integer32):
    """Custom type vRtrMplsLspFRMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneToOneBackup", 1),
          ("facilityBackup", 2))
    )


_VRtrMplsLspFRMethod_Type.__name__ = "Integer32"
_VRtrMplsLspFRMethod_Object = MibTableColumn
vRtrMplsLspFRMethod = _VRtrMplsLspFRMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 30),
    _VRtrMplsLspFRMethod_Type()
)
vRtrMplsLspFRMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRMethod.setStatus("current")


class _VRtrMplsLspFRNodeProtect_Type(TruthValue):
    """Custom type vRtrMplsLspFRNodeProtect based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspFRNodeProtect_Type.__name__ = "TruthValue"
_VRtrMplsLspFRNodeProtect_Object = MibTableColumn
vRtrMplsLspFRNodeProtect = _VRtrMplsLspFRNodeProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 31),
    _VRtrMplsLspFRNodeProtect_Type()
)
vRtrMplsLspFRNodeProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRNodeProtect.setStatus("current")


class _VRtrMplsLspAdminGroupInclude_Type(Unsigned32):
    """Custom type vRtrMplsLspAdminGroupInclude based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspAdminGroupInclude_Type.__name__ = "Unsigned32"
_VRtrMplsLspAdminGroupInclude_Object = MibTableColumn
vRtrMplsLspAdminGroupInclude = _VRtrMplsLspAdminGroupInclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 32),
    _VRtrMplsLspAdminGroupInclude_Type()
)
vRtrMplsLspAdminGroupInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAdminGroupInclude.setStatus("current")


class _VRtrMplsLspAdminGroupExclude_Type(Unsigned32):
    """Custom type vRtrMplsLspAdminGroupExclude based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspAdminGroupExclude_Type.__name__ = "Unsigned32"
_VRtrMplsLspAdminGroupExclude_Object = MibTableColumn
vRtrMplsLspAdminGroupExclude = _VRtrMplsLspAdminGroupExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 33),
    _VRtrMplsLspAdminGroupExclude_Type()
)
vRtrMplsLspAdminGroupExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAdminGroupExclude.setStatus("current")


class _VRtrMplsLspAdaptive_Type(TruthValue):
    """Custom type vRtrMplsLspAdaptive based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspAdaptive_Type.__name__ = "TruthValue"
_VRtrMplsLspAdaptive_Object = MibTableColumn
vRtrMplsLspAdaptive = _VRtrMplsLspAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 34),
    _VRtrMplsLspAdaptive_Type()
)
vRtrMplsLspAdaptive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAdaptive.setStatus("current")


class _VRtrMplsLspInheritance_Type(Unsigned32):
    """Custom type vRtrMplsLspInheritance based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspInheritance_Type.__name__ = "Unsigned32"
_VRtrMplsLspInheritance_Object = MibTableColumn
vRtrMplsLspInheritance = _VRtrMplsLspInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 35),
    _VRtrMplsLspInheritance_Type()
)
vRtrMplsLspInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspInheritance.setStatus("current")


class _VRtrMplsLspOptimizeTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspOptimizeTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrMplsLspOptimizeTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspOptimizeTimer_Object = MibTableColumn
vRtrMplsLspOptimizeTimer = _VRtrMplsLspOptimizeTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 36),
    _VRtrMplsLspOptimizeTimer_Type()
)
vRtrMplsLspOptimizeTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspOptimizeTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspOptimizeTimer.setUnits("seconds")
_VRtrMplsLspOperFastReroute_Type = TruthValue
_VRtrMplsLspOperFastReroute_Object = MibTableColumn
vRtrMplsLspOperFastReroute = _VRtrMplsLspOperFastReroute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 37),
    _VRtrMplsLspOperFastReroute_Type()
)
vRtrMplsLspOperFastReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOperFastReroute.setStatus("current")


class _VRtrMplsLspFRObject_Type(TruthValue):
    """Custom type vRtrMplsLspFRObject based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspFRObject_Type.__name__ = "TruthValue"
_VRtrMplsLspFRObject_Object = MibTableColumn
vRtrMplsLspFRObject = _VRtrMplsLspFRObject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 38),
    _VRtrMplsLspFRObject_Type()
)
vRtrMplsLspFRObject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRObject.setStatus("current")


class _VRtrMplsLspHoldTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspHoldTimer based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_VRtrMplsLspHoldTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspHoldTimer_Object = MibTableColumn
vRtrMplsLspHoldTimer = _VRtrMplsLspHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 39),
    _VRtrMplsLspHoldTimer_Type()
)
vRtrMplsLspHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspHoldTimer.setUnits("seconds")


class _VRtrMplsLspCspfTeMetricEnabled_Type(TruthValue):
    """Custom type vRtrMplsLspCspfTeMetricEnabled based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspCspfTeMetricEnabled_Type.__name__ = "TruthValue"
_VRtrMplsLspCspfTeMetricEnabled_Object = MibTableColumn
vRtrMplsLspCspfTeMetricEnabled = _VRtrMplsLspCspfTeMetricEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 40),
    _VRtrMplsLspCspfTeMetricEnabled_Type()
)
vRtrMplsLspCspfTeMetricEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspCspfTeMetricEnabled.setStatus("obsolete")


class _VRtrMplsLspP2mpId_Type(Unsigned32):
    """Custom type vRtrMplsLspP2mpId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_VRtrMplsLspP2mpId_Type.__name__ = "Unsigned32"
_VRtrMplsLspP2mpId_Object = MibTableColumn
vRtrMplsLspP2mpId = _VRtrMplsLspP2mpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 41),
    _VRtrMplsLspP2mpId_Type()
)
vRtrMplsLspP2mpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspP2mpId.setStatus("current")


class _VRtrMplsLspClassType_Type(TmnxRsvpDSTEClassType):
    """Custom type vRtrMplsLspClassType based on TmnxRsvpDSTEClassType"""
    defaultValue = 0


_VRtrMplsLspClassType_Type.__name__ = "TmnxRsvpDSTEClassType"
_VRtrMplsLspClassType_Object = MibTableColumn
vRtrMplsLspClassType = _VRtrMplsLspClassType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 42),
    _VRtrMplsLspClassType_Type()
)
vRtrMplsLspClassType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspClassType.setStatus("current")
_VRtrMplsLspOperMetric_Type = Unsigned32
_VRtrMplsLspOperMetric_Object = MibTableColumn
vRtrMplsLspOperMetric = _VRtrMplsLspOperMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 43),
    _VRtrMplsLspOperMetric_Type()
)
vRtrMplsLspOperMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOperMetric.setStatus("current")


class _VRtrMplsLspLdpOverRsvpInclude_Type(TruthValue):
    """Custom type vRtrMplsLspLdpOverRsvpInclude based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspLdpOverRsvpInclude_Type.__name__ = "TruthValue"
_VRtrMplsLspLdpOverRsvpInclude_Object = MibTableColumn
vRtrMplsLspLdpOverRsvpInclude = _VRtrMplsLspLdpOverRsvpInclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 44),
    _VRtrMplsLspLdpOverRsvpInclude_Type()
)
vRtrMplsLspLdpOverRsvpInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspLdpOverRsvpInclude.setStatus("current")


class _VRtrMplsLspLeastFill_Type(TruthValue):
    """Custom type vRtrMplsLspLeastFill based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspLeastFill_Type.__name__ = "TruthValue"
_VRtrMplsLspLeastFill_Object = MibTableColumn
vRtrMplsLspLeastFill = _VRtrMplsLspLeastFill_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 45),
    _VRtrMplsLspLeastFill_Type()
)
vRtrMplsLspLeastFill.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspLeastFill.setStatus("current")


class _VRtrMplsLspVprnAutoBindInclude_Type(TruthValue):
    """Custom type vRtrMplsLspVprnAutoBindInclude based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspVprnAutoBindInclude_Type.__name__ = "TruthValue"
_VRtrMplsLspVprnAutoBindInclude_Object = MibTableColumn
vRtrMplsLspVprnAutoBindInclude = _VRtrMplsLspVprnAutoBindInclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 46),
    _VRtrMplsLspVprnAutoBindInclude_Type()
)
vRtrMplsLspVprnAutoBindInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspVprnAutoBindInclude.setStatus("current")


class _VRtrMplsLspMainCTRetryLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspMainCTRetryLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VRtrMplsLspMainCTRetryLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspMainCTRetryLimit_Object = MibTableColumn
vRtrMplsLspMainCTRetryLimit = _VRtrMplsLspMainCTRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 47),
    _VRtrMplsLspMainCTRetryLimit_Type()
)
vRtrMplsLspMainCTRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspMainCTRetryLimit.setStatus("current")


class _VRtrMplsLspIgpShortcut_Type(TruthValue):
    """Custom type vRtrMplsLspIgpShortcut based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspIgpShortcut_Type.__name__ = "TruthValue"
_VRtrMplsLspIgpShortcut_Object = MibTableColumn
vRtrMplsLspIgpShortcut = _VRtrMplsLspIgpShortcut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 48),
    _VRtrMplsLspIgpShortcut_Type()
)
vRtrMplsLspIgpShortcut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspIgpShortcut.setStatus("current")
_VRtrMplsLspOriginTemplate_Type = TNamedItemOrEmpty
_VRtrMplsLspOriginTemplate_Object = MibTableColumn
vRtrMplsLspOriginTemplate = _VRtrMplsLspOriginTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 49),
    _VRtrMplsLspOriginTemplate_Type()
)
vRtrMplsLspOriginTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOriginTemplate.setStatus("current")


class _VRtrMplsLspAutoBandwidth_Type(TruthValue):
    """Custom type vRtrMplsLspAutoBandwidth based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspAutoBandwidth_Type.__name__ = "TruthValue"
_VRtrMplsLspAutoBandwidth_Object = MibTableColumn
vRtrMplsLspAutoBandwidth = _VRtrMplsLspAutoBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 50),
    _VRtrMplsLspAutoBandwidth_Type()
)
vRtrMplsLspAutoBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBandwidth.setStatus("current")


class _VRtrMplsLspCspfToFirstLoose_Type(TruthValue):
    """Custom type vRtrMplsLspCspfToFirstLoose based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspCspfToFirstLoose_Type.__name__ = "TruthValue"
_VRtrMplsLspCspfToFirstLoose_Object = MibTableColumn
vRtrMplsLspCspfToFirstLoose = _VRtrMplsLspCspfToFirstLoose_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 51),
    _VRtrMplsLspCspfToFirstLoose_Type()
)
vRtrMplsLspCspfToFirstLoose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspCspfToFirstLoose.setStatus("obsolete")


class _VRtrMplsLspPropAdminGroup_Type(TruthValue):
    """Custom type vRtrMplsLspPropAdminGroup based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspPropAdminGroup_Type.__name__ = "TruthValue"
_VRtrMplsLspPropAdminGroup_Object = MibTableColumn
vRtrMplsLspPropAdminGroup = _VRtrMplsLspPropAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 52),
    _VRtrMplsLspPropAdminGroup_Type()
)
vRtrMplsLspPropAdminGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPropAdminGroup.setStatus("current")


class _VRtrMplsLspBgpShortcut_Type(TruthValue):
    """Custom type vRtrMplsLspBgpShortcut based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspBgpShortcut_Type.__name__ = "TruthValue"
_VRtrMplsLspBgpShortcut_Object = MibTableColumn
vRtrMplsLspBgpShortcut = _VRtrMplsLspBgpShortcut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 53),
    _VRtrMplsLspBgpShortcut_Type()
)
vRtrMplsLspBgpShortcut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBgpShortcut.setStatus("current")


class _VRtrMplsLspBgpTransportTunnel_Type(TmnxMplsLspBgpRSVPLSPTunState):
    """Custom type vRtrMplsLspBgpTransportTunnel based on TmnxMplsLspBgpRSVPLSPTunState"""
    defaultValue = 1


_VRtrMplsLspBgpTransportTunnel_Type.__name__ = "TmnxMplsLspBgpRSVPLSPTunState"
_VRtrMplsLspBgpTransportTunnel_Object = MibTableColumn
vRtrMplsLspBgpTransportTunnel = _VRtrMplsLspBgpTransportTunnel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 54),
    _VRtrMplsLspBgpTransportTunnel_Type()
)
vRtrMplsLspBgpTransportTunnel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBgpTransportTunnel.setStatus("current")
_VRtrMplsLspSwitchStbyPath_Type = TmnxActionType
_VRtrMplsLspSwitchStbyPath_Object = MibTableColumn
vRtrMplsLspSwitchStbyPath = _VRtrMplsLspSwitchStbyPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 55),
    _VRtrMplsLspSwitchStbyPath_Type()
)
vRtrMplsLspSwitchStbyPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspSwitchStbyPath.setStatus("current")


class _VRtrMplsLspSwitchStbyPathIndex_Type(MplsTunnelIndex):
    """Custom type vRtrMplsLspSwitchStbyPathIndex based on MplsTunnelIndex"""
    defaultValue = 0


_VRtrMplsLspSwitchStbyPathIndex_Type.__name__ = "MplsTunnelIndex"
_VRtrMplsLspSwitchStbyPathIndex_Object = MibTableColumn
vRtrMplsLspSwitchStbyPathIndex = _VRtrMplsLspSwitchStbyPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 56),
    _VRtrMplsLspSwitchStbyPathIndex_Type()
)
vRtrMplsLspSwitchStbyPathIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspSwitchStbyPathIndex.setStatus("current")


class _VRtrMplsLspSwitchStbyPathForce_Type(TruthValue):
    """Custom type vRtrMplsLspSwitchStbyPathForce based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspSwitchStbyPathForce_Type.__name__ = "TruthValue"
_VRtrMplsLspSwitchStbyPathForce_Object = MibTableColumn
vRtrMplsLspSwitchStbyPathForce = _VRtrMplsLspSwitchStbyPathForce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 57),
    _VRtrMplsLspSwitchStbyPathForce_Type()
)
vRtrMplsLspSwitchStbyPathForce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspSwitchStbyPathForce.setStatus("current")
_VRtrMplsLspExcludeNodeAddrType_Type = InetAddressType
_VRtrMplsLspExcludeNodeAddrType_Object = MibTableColumn
vRtrMplsLspExcludeNodeAddrType = _VRtrMplsLspExcludeNodeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 58),
    _VRtrMplsLspExcludeNodeAddrType_Type()
)
vRtrMplsLspExcludeNodeAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExcludeNodeAddrType.setStatus("current")


class _VRtrMplsLspExcludeNodeAddr_Type(InetAddress):
    """Custom type vRtrMplsLspExcludeNodeAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsLspExcludeNodeAddr_Type.__name__ = "InetAddress"
_VRtrMplsLspExcludeNodeAddr_Object = MibTableColumn
vRtrMplsLspExcludeNodeAddr = _VRtrMplsLspExcludeNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 59),
    _VRtrMplsLspExcludeNodeAddr_Type()
)
vRtrMplsLspExcludeNodeAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExcludeNodeAddr.setStatus("current")


class _VRtrMplsLspIgpShortcutLfaType_Type(Integer32):
    """Custom type vRtrMplsLspIgpShortcutLfaType based on Integer32"""
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
          ("lfaProtect", 1),
          ("lfaOnly", 2))
    )


_VRtrMplsLspIgpShortcutLfaType_Type.__name__ = "Integer32"
_VRtrMplsLspIgpShortcutLfaType_Object = MibTableColumn
vRtrMplsLspIgpShortcutLfaType = _VRtrMplsLspIgpShortcutLfaType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 60),
    _VRtrMplsLspIgpShortcutLfaType_Type()
)
vRtrMplsLspIgpShortcutLfaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspIgpShortcutLfaType.setStatus("current")


class _VRtrMplsLspToAddrType_Type(TmnxMplsLspAddrType):
    """Custom type vRtrMplsLspToAddrType based on TmnxMplsLspAddrType"""
    defaultValue = 0


_VRtrMplsLspToAddrType_Type.__name__ = "TmnxMplsLspAddrType"
_VRtrMplsLspToAddrType_Object = MibTableColumn
vRtrMplsLspToAddrType = _VRtrMplsLspToAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 61),
    _VRtrMplsLspToAddrType_Type()
)
vRtrMplsLspToAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspToAddrType.setStatus("current")


class _VRtrMplsLspFromAddrType_Type(TmnxMplsLspAddrType):
    """Custom type vRtrMplsLspFromAddrType based on TmnxMplsLspAddrType"""
    defaultValue = 0


_VRtrMplsLspFromAddrType_Type.__name__ = "TmnxMplsLspAddrType"
_VRtrMplsLspFromAddrType_Object = MibTableColumn
vRtrMplsLspFromAddrType = _VRtrMplsLspFromAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 62),
    _VRtrMplsLspFromAddrType_Type()
)
vRtrMplsLspFromAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFromAddrType.setStatus("current")


class _VRtrMplsLspToNodeId_Type(TmnxMplsTpNodeID):
    """Custom type vRtrMplsLspToNodeId based on TmnxMplsTpNodeID"""
    defaultValue = 0


_VRtrMplsLspToNodeId_Type.__name__ = "TmnxMplsTpNodeID"
_VRtrMplsLspToNodeId_Object = MibTableColumn
vRtrMplsLspToNodeId = _VRtrMplsLspToNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 63),
    _VRtrMplsLspToNodeId_Type()
)
vRtrMplsLspToNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspToNodeId.setStatus("current")
_VRtrMplsLspFromNodeId_Type = TmnxMplsTpNodeID
_VRtrMplsLspFromNodeId_Object = MibTableColumn
vRtrMplsLspFromNodeId = _VRtrMplsLspFromNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 64),
    _VRtrMplsLspFromNodeId_Type()
)
vRtrMplsLspFromNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspFromNodeId.setStatus("current")


class _VRtrMplsLspDestGlobalId_Type(TmnxMplsTpGlobalID):
    """Custom type vRtrMplsLspDestGlobalId based on TmnxMplsTpGlobalID"""
    defaultValue = 0


_VRtrMplsLspDestGlobalId_Type.__name__ = "TmnxMplsTpGlobalID"
_VRtrMplsLspDestGlobalId_Object = MibTableColumn
vRtrMplsLspDestGlobalId = _VRtrMplsLspDestGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 65),
    _VRtrMplsLspDestGlobalId_Type()
)
vRtrMplsLspDestGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspDestGlobalId.setStatus("current")


class _VRtrMplsLspDestTunnelNum_Type(Unsigned32):
    """Custom type vRtrMplsLspDestTunnelNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 61440),
    )


_VRtrMplsLspDestTunnelNum_Type.__name__ = "Unsigned32"
_VRtrMplsLspDestTunnelNum_Object = MibTableColumn
vRtrMplsLspDestTunnelNum = _VRtrMplsLspDestTunnelNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 66),
    _VRtrMplsLspDestTunnelNum_Type()
)
vRtrMplsLspDestTunnelNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspDestTunnelNum.setStatus("current")


class _VRtrMplsLspFRPropAdminGroup_Type(TruthValue):
    """Custom type vRtrMplsLspFRPropAdminGroup based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspFRPropAdminGroup_Type.__name__ = "TruthValue"
_VRtrMplsLspFRPropAdminGroup_Object = MibTableColumn
vRtrMplsLspFRPropAdminGroup = _VRtrMplsLspFRPropAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 67),
    _VRtrMplsLspFRPropAdminGroup_Type()
)
vRtrMplsLspFRPropAdminGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRPropAdminGroup.setStatus("current")


class _VRtrMplsLspIgpShortcutRelOffset_Type(Integer32):
    """Custom type vRtrMplsLspIgpShortcutRelOffset based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_VRtrMplsLspIgpShortcutRelOffset_Type.__name__ = "Integer32"
_VRtrMplsLspIgpShortcutRelOffset_Object = MibTableColumn
vRtrMplsLspIgpShortcutRelOffset = _VRtrMplsLspIgpShortcutRelOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 68),
    _VRtrMplsLspIgpShortcutRelOffset_Type()
)
vRtrMplsLspIgpShortcutRelOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspIgpShortcutRelOffset.setStatus("current")


class _VRtrMplsLspRevertTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspRevertTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4320),
    )


_VRtrMplsLspRevertTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspRevertTimer_Object = MibTableColumn
vRtrMplsLspRevertTimer = _VRtrMplsLspRevertTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 69),
    _VRtrMplsLspRevertTimer_Type()
)
vRtrMplsLspRevertTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRevertTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspRevertTimer.setUnits("minutes")
_VRtrMplsLspRevertTimeRemain_Type = Unsigned32
_VRtrMplsLspRevertTimeRemain_Object = MibTableColumn
vRtrMplsLspRevertTimeRemain = _VRtrMplsLspRevertTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 70),
    _VRtrMplsLspRevertTimeRemain_Type()
)
vRtrMplsLspRevertTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspRevertTimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspRevertTimeRemain.setUnits("minutes")


class _VRtrMplsLspLoadBalancingWeight_Type(Unsigned32):
    """Custom type vRtrMplsLspLoadBalancingWeight based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrMplsLspLoadBalancingWeight_Type.__name__ = "Unsigned32"
_VRtrMplsLspLoadBalancingWeight_Object = MibTableColumn
vRtrMplsLspLoadBalancingWeight = _VRtrMplsLspLoadBalancingWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 71),
    _VRtrMplsLspLoadBalancingWeight_Type()
)
vRtrMplsLspLoadBalancingWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspLoadBalancingWeight.setStatus("current")


class _VRtrMplsLspClassFwdingEnabled_Type(TruthValue):
    """Custom type vRtrMplsLspClassFwdingEnabled based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspClassFwdingEnabled_Type.__name__ = "TruthValue"
_VRtrMplsLspClassFwdingEnabled_Object = MibTableColumn
vRtrMplsLspClassFwdingEnabled = _VRtrMplsLspClassFwdingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 72),
    _VRtrMplsLspClassFwdingEnabled_Type()
)
vRtrMplsLspClassFwdingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspClassFwdingEnabled.setStatus("current")


class _VRtrMplsLspFC_Type(TmnxCBFClasses):
    """Custom type vRtrMplsLspFC based on TmnxCBFClasses"""
    defaultBinValue = "0"


_VRtrMplsLspFC_Type.__name__ = "TmnxCBFClasses"
_VRtrMplsLspFC_Object = MibTableColumn
vRtrMplsLspFC = _VRtrMplsLspFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 73),
    _VRtrMplsLspFC_Type()
)
vRtrMplsLspFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFC.setStatus("obsolete")
_VRtrMplsLspBfdTemplateName_Type = TNamedItemOrEmpty
_VRtrMplsLspBfdTemplateName_Object = MibTableColumn
vRtrMplsLspBfdTemplateName = _VRtrMplsLspBfdTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 74),
    _VRtrMplsLspBfdTemplateName_Type()
)
vRtrMplsLspBfdTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBfdTemplateName.setStatus("current")


class _VRtrMplsLspBfdEnable_Type(TruthValue):
    """Custom type vRtrMplsLspBfdEnable based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspBfdEnable_Type.__name__ = "TruthValue"
_VRtrMplsLspBfdEnable_Object = MibTableColumn
vRtrMplsLspBfdEnable = _VRtrMplsLspBfdEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 75),
    _VRtrMplsLspBfdEnable_Type()
)
vRtrMplsLspBfdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBfdEnable.setStatus("current")


class _VRtrMplsLspBfdPingIntvl_Type(Unsigned32):
    """Custom type vRtrMplsLspBfdPingIntvl based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 300),
    )


_VRtrMplsLspBfdPingIntvl_Type.__name__ = "Unsigned32"
_VRtrMplsLspBfdPingIntvl_Object = MibTableColumn
vRtrMplsLspBfdPingIntvl = _VRtrMplsLspBfdPingIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 76),
    _VRtrMplsLspBfdPingIntvl_Type()
)
vRtrMplsLspBfdPingIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBfdPingIntvl.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspBfdPingIntvl.setUnits("seconds")


class _VRtrMplsLspNgFromAddr_Type(InetAddress):
    """Custom type vRtrMplsLspNgFromAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsLspNgFromAddr_Type.__name__ = "InetAddress"
_VRtrMplsLspNgFromAddr_Object = MibTableColumn
vRtrMplsLspNgFromAddr = _VRtrMplsLspNgFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 77),
    _VRtrMplsLspNgFromAddr_Type()
)
vRtrMplsLspNgFromAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspNgFromAddr.setStatus("current")


class _VRtrMplsLspNgToAddr_Type(InetAddress):
    """Custom type vRtrMplsLspNgToAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsLspNgToAddr_Type.__name__ = "InetAddress"
_VRtrMplsLspNgToAddr_Object = MibTableColumn
vRtrMplsLspNgToAddr = _VRtrMplsLspNgToAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 78),
    _VRtrMplsLspNgToAddr_Type()
)
vRtrMplsLspNgToAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspNgToAddr.setStatus("current")
_VRtrMplsLspStatTable_Object = MibTable
vRtrMplsLspStatTable = _VRtrMplsLspStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    vRtrMplsLspStatTable.setStatus("current")
_VRtrMplsLspStatEntry_Object = MibTableRow
vRtrMplsLspStatEntry = _VRtrMplsLspStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsLspStatEntry.setStatus("current")
_VRtrMplsLspOctets_Type = Counter64
_VRtrMplsLspOctets_Object = MibTableColumn
vRtrMplsLspOctets = _VRtrMplsLspOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 1),
    _VRtrMplsLspOctets_Type()
)
vRtrMplsLspOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOctets.setStatus("obsolete")
_VRtrMplsLspPackets_Type = Counter64
_VRtrMplsLspPackets_Object = MibTableColumn
vRtrMplsLspPackets = _VRtrMplsLspPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 2),
    _VRtrMplsLspPackets_Type()
)
vRtrMplsLspPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPackets.setStatus("obsolete")
_VRtrMplsLspAge_Type = TmnxTimeInterval
_VRtrMplsLspAge_Object = MibTableColumn
vRtrMplsLspAge = _VRtrMplsLspAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 3),
    _VRtrMplsLspAge_Type()
)
vRtrMplsLspAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAge.setStatus("current")
_VRtrMplsLspTimeUp_Type = TmnxTimeInterval
_VRtrMplsLspTimeUp_Object = MibTableColumn
vRtrMplsLspTimeUp = _VRtrMplsLspTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 4),
    _VRtrMplsLspTimeUp_Type()
)
vRtrMplsLspTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTimeUp.setStatus("current")
_VRtrMplsLspTimeDown_Type = TmnxTimeInterval
_VRtrMplsLspTimeDown_Object = MibTableColumn
vRtrMplsLspTimeDown = _VRtrMplsLspTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 5),
    _VRtrMplsLspTimeDown_Type()
)
vRtrMplsLspTimeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTimeDown.setStatus("current")
_VRtrMplsLspPrimaryTimeUp_Type = TmnxTimeInterval
_VRtrMplsLspPrimaryTimeUp_Object = MibTableColumn
vRtrMplsLspPrimaryTimeUp = _VRtrMplsLspPrimaryTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 6),
    _VRtrMplsLspPrimaryTimeUp_Type()
)
vRtrMplsLspPrimaryTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPrimaryTimeUp.setStatus("current")
_VRtrMplsLspTransitions_Type = Counter32
_VRtrMplsLspTransitions_Object = MibTableColumn
vRtrMplsLspTransitions = _VRtrMplsLspTransitions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 7),
    _VRtrMplsLspTransitions_Type()
)
vRtrMplsLspTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTransitions.setStatus("current")
_VRtrMplsLspLastTransition_Type = TmnxTimeInterval
_VRtrMplsLspLastTransition_Object = MibTableColumn
vRtrMplsLspLastTransition = _VRtrMplsLspLastTransition_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 8),
    _VRtrMplsLspLastTransition_Type()
)
vRtrMplsLspLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspLastTransition.setStatus("current")
_VRtrMplsLspPathChanges_Type = Counter32
_VRtrMplsLspPathChanges_Object = MibTableColumn
vRtrMplsLspPathChanges = _VRtrMplsLspPathChanges_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 9),
    _VRtrMplsLspPathChanges_Type()
)
vRtrMplsLspPathChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathChanges.setStatus("current")
_VRtrMplsLspLastPathChange_Type = TmnxTimeInterval
_VRtrMplsLspLastPathChange_Object = MibTableColumn
vRtrMplsLspLastPathChange = _VRtrMplsLspLastPathChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 10),
    _VRtrMplsLspLastPathChange_Type()
)
vRtrMplsLspLastPathChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspLastPathChange.setStatus("current")
_VRtrMplsLspConfiguredPaths_Type = Integer32
_VRtrMplsLspConfiguredPaths_Object = MibTableColumn
vRtrMplsLspConfiguredPaths = _VRtrMplsLspConfiguredPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 11),
    _VRtrMplsLspConfiguredPaths_Type()
)
vRtrMplsLspConfiguredPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspConfiguredPaths.setStatus("current")
_VRtrMplsLspStandbyPaths_Type = Integer32
_VRtrMplsLspStandbyPaths_Object = MibTableColumn
vRtrMplsLspStandbyPaths = _VRtrMplsLspStandbyPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 12),
    _VRtrMplsLspStandbyPaths_Type()
)
vRtrMplsLspStandbyPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStandbyPaths.setStatus("current")
_VRtrMplsLspOperationalPaths_Type = Integer32
_VRtrMplsLspOperationalPaths_Object = MibTableColumn
vRtrMplsLspOperationalPaths = _VRtrMplsLspOperationalPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 13),
    _VRtrMplsLspOperationalPaths_Type()
)
vRtrMplsLspOperationalPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOperationalPaths.setStatus("current")
_VRtrMplsLspConfP2mpInstances_Type = Gauge32
_VRtrMplsLspConfP2mpInstances_Object = MibTableColumn
vRtrMplsLspConfP2mpInstances = _VRtrMplsLspConfP2mpInstances_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 14),
    _VRtrMplsLspConfP2mpInstances_Type()
)
vRtrMplsLspConfP2mpInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspConfP2mpInstances.setStatus("current")
_VRtrMplsLspStatsEgrIndexUnAvail_Type = TruthValue
_VRtrMplsLspStatsEgrIndexUnAvail_Object = MibTableColumn
vRtrMplsLspStatsEgrIndexUnAvail = _VRtrMplsLspStatsEgrIndexUnAvail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 15),
    _VRtrMplsLspStatsEgrIndexUnAvail_Type()
)
vRtrMplsLspStatsEgrIndexUnAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsEgrIndexUnAvail.setStatus("current")
_VRtrMplsLspSelfPingTimeouts_Type = Counter32
_VRtrMplsLspSelfPingTimeouts_Object = MibTableColumn
vRtrMplsLspSelfPingTimeouts = _VRtrMplsLspSelfPingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 16),
    _VRtrMplsLspSelfPingTimeouts_Type()
)
vRtrMplsLspSelfPingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspSelfPingTimeouts.setStatus("current")
_VRtrMplsLspSelfPingOamNoRsc_Type = Counter32
_VRtrMplsLspSelfPingOamNoRsc_Object = MibTableColumn
vRtrMplsLspSelfPingOamNoRsc = _VRtrMplsLspSelfPingOamNoRsc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 17),
    _VRtrMplsLspSelfPingOamNoRsc_Type()
)
vRtrMplsLspSelfPingOamNoRsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspSelfPingOamNoRsc.setStatus("current")


class _VRtrMplsLspPathTableSpinlock_Type(TestAndIncr):
    """Custom type vRtrMplsLspPathTableSpinlock based on TestAndIncr"""
    defaultValue = 0


_VRtrMplsLspPathTableSpinlock_Type.__name__ = "TestAndIncr"
_VRtrMplsLspPathTableSpinlock_Object = MibScalar
vRtrMplsLspPathTableSpinlock = _VRtrMplsLspPathTableSpinlock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 3),
    _VRtrMplsLspPathTableSpinlock_Type()
)
vRtrMplsLspPathTableSpinlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTableSpinlock.setStatus("current")
_VRtrMplsLspPathTable_Object = MibTable
vRtrMplsLspPathTable = _VRtrMplsLspPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4)
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathTable.setStatus("current")
_VRtrMplsLspPathEntry_Object = MibTableRow
vRtrMplsLspPathEntry = _VRtrMplsLspPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1)
)
vRtrMplsLspPathEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
    (0, "MPLS-TE-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathEntry.setStatus("current")
_VRtrMplsLspPathRowStatus_Type = RowStatus
_VRtrMplsLspPathRowStatus_Object = MibTableColumn
vRtrMplsLspPathRowStatus = _VRtrMplsLspPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 1),
    _VRtrMplsLspPathRowStatus_Type()
)
vRtrMplsLspPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathRowStatus.setStatus("current")
_VRtrMplsLspPathLastChange_Type = TimeStamp
_VRtrMplsLspPathLastChange_Object = MibTableColumn
vRtrMplsLspPathLastChange = _VRtrMplsLspPathLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 2),
    _VRtrMplsLspPathLastChange_Type()
)
vRtrMplsLspPathLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastChange.setStatus("current")


class _VRtrMplsLspPathType_Type(Integer32):
    """Custom type vRtrMplsLspPathType based on Integer32"""
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
        *(("other", 1),
          ("primary", 2),
          ("standby", 3),
          ("secondary", 4))
    )


_VRtrMplsLspPathType_Type.__name__ = "Integer32"
_VRtrMplsLspPathType_Object = MibTableColumn
vRtrMplsLspPathType = _VRtrMplsLspPathType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 3),
    _VRtrMplsLspPathType_Type()
)
vRtrMplsLspPathType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathType.setStatus("current")


class _VRtrMplsLspPathCos_Type(Integer32):
    """Custom type vRtrMplsLspPathCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_VRtrMplsLspPathCos_Type.__name__ = "Integer32"
_VRtrMplsLspPathCos_Object = MibTableColumn
vRtrMplsLspPathCos = _VRtrMplsLspPathCos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 4),
    _VRtrMplsLspPathCos_Type()
)
vRtrMplsLspPathCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathCos.setStatus("obsolete")


class _VRtrMplsLspPathProperties_Type(Bits):
    """Custom type vRtrMplsLspPathProperties based on Bits"""
    namedValues = NamedValues(
        *(("record-route", 0),
          ("adaptive", 1),
          ("cspf", 2),
          ("mergeable", 3),
          ("fast-reroute", 4),
          ("pce-reported", 5),
          ("pce-controlled", 6),
          ("pce-computed", 7))
    )

_VRtrMplsLspPathProperties_Type.__name__ = "Bits"
_VRtrMplsLspPathProperties_Object = MibTableColumn
vRtrMplsLspPathProperties = _VRtrMplsLspPathProperties_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 5),
    _VRtrMplsLspPathProperties_Type()
)
vRtrMplsLspPathProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathProperties.setStatus("current")


class _VRtrMplsLspPathBandwidth_Type(Integer32):
    """Custom type vRtrMplsLspPathBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6400000),
    )


_VRtrMplsLspPathBandwidth_Type.__name__ = "Integer32"
_VRtrMplsLspPathBandwidth_Object = MibTableColumn
vRtrMplsLspPathBandwidth = _VRtrMplsLspPathBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 6),
    _VRtrMplsLspPathBandwidth_Type()
)
vRtrMplsLspPathBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBandwidth.setUnits("megabps")


class _VRtrMplsLspPathBwProtect_Type(TruthValue):
    """Custom type vRtrMplsLspPathBwProtect based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspPathBwProtect_Type.__name__ = "TruthValue"
_VRtrMplsLspPathBwProtect_Object = MibTableColumn
vRtrMplsLspPathBwProtect = _VRtrMplsLspPathBwProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 7),
    _VRtrMplsLspPathBwProtect_Type()
)
vRtrMplsLspPathBwProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBwProtect.setStatus("obsolete")


class _VRtrMplsLspPathState_Type(Integer32):
    """Custom type vRtrMplsLspPathState based on Integer32"""
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
        *(("unknown", 1),
          ("active", 2),
          ("inactive", 3))
    )


_VRtrMplsLspPathState_Type.__name__ = "Integer32"
_VRtrMplsLspPathState_Object = MibTableColumn
vRtrMplsLspPathState = _VRtrMplsLspPathState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 8),
    _VRtrMplsLspPathState_Type()
)
vRtrMplsLspPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathState.setStatus("current")


class _VRtrMplsLspPathPreference_Type(Integer32):
    """Custom type vRtrMplsLspPathPreference based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrMplsLspPathPreference_Type.__name__ = "Integer32"
_VRtrMplsLspPathPreference_Object = MibTableColumn
vRtrMplsLspPathPreference = _VRtrMplsLspPathPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 9),
    _VRtrMplsLspPathPreference_Type()
)
vRtrMplsLspPathPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathPreference.setStatus("current")


class _VRtrMplsLspPathCosSource_Type(TruthValue):
    """Custom type vRtrMplsLspPathCosSource based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspPathCosSource_Type.__name__ = "TruthValue"
_VRtrMplsLspPathCosSource_Object = MibTableColumn
vRtrMplsLspPathCosSource = _VRtrMplsLspPathCosSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 10),
    _VRtrMplsLspPathCosSource_Type()
)
vRtrMplsLspPathCosSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathCosSource.setStatus("obsolete")


class _VRtrMplsLspPathClassOfService_Type(TNamedItemOrEmpty):
    """Custom type vRtrMplsLspPathClassOfService based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrMplsLspPathClassOfService_Type.__name__ = "TNamedItemOrEmpty"
_VRtrMplsLspPathClassOfService_Object = MibTableColumn
vRtrMplsLspPathClassOfService = _VRtrMplsLspPathClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 11),
    _VRtrMplsLspPathClassOfService_Type()
)
vRtrMplsLspPathClassOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathClassOfService.setStatus("obsolete")


class _VRtrMplsLspPathSetupPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspPathSetupPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspPathSetupPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathSetupPriority_Object = MibTableColumn
vRtrMplsLspPathSetupPriority = _VRtrMplsLspPathSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 12),
    _VRtrMplsLspPathSetupPriority_Type()
)
vRtrMplsLspPathSetupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathSetupPriority.setStatus("current")


class _VRtrMplsLspPathHoldPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspPathHoldPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspPathHoldPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathHoldPriority_Object = MibTableColumn
vRtrMplsLspPathHoldPriority = _VRtrMplsLspPathHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 13),
    _VRtrMplsLspPathHoldPriority_Type()
)
vRtrMplsLspPathHoldPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathHoldPriority.setStatus("current")


class _VRtrMplsLspPathRecord_Type(Integer32):
    """Custom type vRtrMplsLspPathRecord based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("record", 1),
          ("noRecord", 2))
    )


_VRtrMplsLspPathRecord_Type.__name__ = "Integer32"
_VRtrMplsLspPathRecord_Object = MibTableColumn
vRtrMplsLspPathRecord = _VRtrMplsLspPathRecord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 14),
    _VRtrMplsLspPathRecord_Type()
)
vRtrMplsLspPathRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathRecord.setStatus("current")


class _VRtrMplsLspPathHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspPathHopLimit based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_VRtrMplsLspPathHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathHopLimit_Object = MibTableColumn
vRtrMplsLspPathHopLimit = _VRtrMplsLspPathHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 15),
    _VRtrMplsLspPathHopLimit_Type()
)
vRtrMplsLspPathHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathHopLimit.setStatus("current")


class _VRtrMplsLspPathSharing_Type(TruthValue):
    """Custom type vRtrMplsLspPathSharing based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspPathSharing_Type.__name__ = "TruthValue"
_VRtrMplsLspPathSharing_Object = MibTableColumn
vRtrMplsLspPathSharing = _VRtrMplsLspPathSharing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 16),
    _VRtrMplsLspPathSharing_Type()
)
vRtrMplsLspPathSharing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathSharing.setStatus("obsolete")


class _VRtrMplsLspPathAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsLspPathAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrMplsLspPathAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsLspPathAdminState_Object = MibTableColumn
vRtrMplsLspPathAdminState = _VRtrMplsLspPathAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 17),
    _VRtrMplsLspPathAdminState_Type()
)
vRtrMplsLspPathAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathAdminState.setStatus("current")
_VRtrMplsLspPathOperState_Type = TmnxOperState
_VRtrMplsLspPathOperState_Object = MibTableColumn
vRtrMplsLspPathOperState = _VRtrMplsLspPathOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 18),
    _VRtrMplsLspPathOperState_Type()
)
vRtrMplsLspPathOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperState.setStatus("current")


class _VRtrMplsLspPathInheritance_Type(Unsigned32):
    """Custom type vRtrMplsLspPathInheritance based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspPathInheritance_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathInheritance_Object = MibTableColumn
vRtrMplsLspPathInheritance = _VRtrMplsLspPathInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 19),
    _VRtrMplsLspPathInheritance_Type()
)
vRtrMplsLspPathInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathInheritance.setStatus("current")
_VRtrMplsLspPathLspId_Type = MplsLSPID
_VRtrMplsLspPathLspId_Object = MibTableColumn
vRtrMplsLspPathLspId = _VRtrMplsLspPathLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 20),
    _VRtrMplsLspPathLspId_Type()
)
vRtrMplsLspPathLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLspId.setStatus("current")
_VRtrMplsLspPathRetryTimeRemaining_Type = Unsigned32
_VRtrMplsLspPathRetryTimeRemaining_Object = MibTableColumn
vRtrMplsLspPathRetryTimeRemaining = _VRtrMplsLspPathRetryTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 21),
    _VRtrMplsLspPathRetryTimeRemaining_Type()
)
vRtrMplsLspPathRetryTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathRetryTimeRemaining.setStatus("current")


class _VRtrMplsLspPathTunnelARHopListIndex_Type(Integer32):
    """Custom type vRtrMplsLspPathTunnelARHopListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsLspPathTunnelARHopListIndex_Type.__name__ = "Integer32"
_VRtrMplsLspPathTunnelARHopListIndex_Object = MibTableColumn
vRtrMplsLspPathTunnelARHopListIndex = _VRtrMplsLspPathTunnelARHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 22),
    _VRtrMplsLspPathTunnelARHopListIndex_Type()
)
vRtrMplsLspPathTunnelARHopListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTunnelARHopListIndex.setStatus("current")


class _VRtrMplsLspPathNegotiatedMTU_Type(Unsigned32):
    """Custom type vRtrMplsLspPathNegotiatedMTU based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspPathNegotiatedMTU_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathNegotiatedMTU_Object = MibTableColumn
vRtrMplsLspPathNegotiatedMTU = _VRtrMplsLspPathNegotiatedMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 23),
    _VRtrMplsLspPathNegotiatedMTU_Type()
)
vRtrMplsLspPathNegotiatedMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathNegotiatedMTU.setStatus("current")
_VRtrMplsLspPathFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsLspPathFailCode_Object = MibTableColumn
vRtrMplsLspPathFailCode = _VRtrMplsLspPathFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 24),
    _VRtrMplsLspPathFailCode_Type()
)
vRtrMplsLspPathFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathFailCode.setStatus("current")
_VRtrMplsLspPathFailNodeAddr_Type = IpAddress
_VRtrMplsLspPathFailNodeAddr_Object = MibTableColumn
vRtrMplsLspPathFailNodeAddr = _VRtrMplsLspPathFailNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 25),
    _VRtrMplsLspPathFailNodeAddr_Type()
)
vRtrMplsLspPathFailNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathFailNodeAddr.setStatus("current")


class _VRtrMplsLspPathAdminGroupInclude_Type(Unsigned32):
    """Custom type vRtrMplsLspPathAdminGroupInclude based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspPathAdminGroupInclude_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathAdminGroupInclude_Object = MibTableColumn
vRtrMplsLspPathAdminGroupInclude = _VRtrMplsLspPathAdminGroupInclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 26),
    _VRtrMplsLspPathAdminGroupInclude_Type()
)
vRtrMplsLspPathAdminGroupInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathAdminGroupInclude.setStatus("current")


class _VRtrMplsLspPathAdminGroupExclude_Type(Unsigned32):
    """Custom type vRtrMplsLspPathAdminGroupExclude based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspPathAdminGroupExclude_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathAdminGroupExclude_Object = MibTableColumn
vRtrMplsLspPathAdminGroupExclude = _VRtrMplsLspPathAdminGroupExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 27),
    _VRtrMplsLspPathAdminGroupExclude_Type()
)
vRtrMplsLspPathAdminGroupExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathAdminGroupExclude.setStatus("current")


class _VRtrMplsLspPathAdaptive_Type(TruthValue):
    """Custom type vRtrMplsLspPathAdaptive based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspPathAdaptive_Type.__name__ = "TruthValue"
_VRtrMplsLspPathAdaptive_Object = MibTableColumn
vRtrMplsLspPathAdaptive = _VRtrMplsLspPathAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 28),
    _VRtrMplsLspPathAdaptive_Type()
)
vRtrMplsLspPathAdaptive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathAdaptive.setStatus("current")


class _VRtrMplsLspPathOptimizeTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspPathOptimizeTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrMplsLspPathOptimizeTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathOptimizeTimer_Object = MibTableColumn
vRtrMplsLspPathOptimizeTimer = _VRtrMplsLspPathOptimizeTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 29),
    _VRtrMplsLspPathOptimizeTimer_Type()
)
vRtrMplsLspPathOptimizeTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOptimizeTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOptimizeTimer.setUnits("seconds")


class _VRtrMplsLspPathNextOptimize_Type(Unsigned32):
    """Custom type vRtrMplsLspPathNextOptimize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrMplsLspPathNextOptimize_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathNextOptimize_Object = MibTableColumn
vRtrMplsLspPathNextOptimize = _VRtrMplsLspPathNextOptimize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 30),
    _VRtrMplsLspPathNextOptimize_Type()
)
vRtrMplsLspPathNextOptimize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathNextOptimize.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathNextOptimize.setUnits("seconds")
_VRtrMplsLspPathOperBandwidth_Type = Integer32
_VRtrMplsLspPathOperBandwidth_Object = MibTableColumn
vRtrMplsLspPathOperBandwidth = _VRtrMplsLspPathOperBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 31),
    _VRtrMplsLspPathOperBandwidth_Type()
)
vRtrMplsLspPathOperBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperBandwidth.setUnits("megabps")


class _VRtrMplsLspPathMBBState_Type(Integer32):
    """Custom type vRtrMplsLspPathMBBState based on Integer32"""
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
          ("success", 2),
          ("inProgress", 3),
          ("fail", 4))
    )


_VRtrMplsLspPathMBBState_Type.__name__ = "Integer32"
_VRtrMplsLspPathMBBState_Object = MibTableColumn
vRtrMplsLspPathMBBState = _VRtrMplsLspPathMBBState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 32),
    _VRtrMplsLspPathMBBState_Type()
)
vRtrMplsLspPathMBBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBState.setStatus("obsolete")
_VRtrMplsLspPathResignal_Type = TmnxActionType
_VRtrMplsLspPathResignal_Object = MibTableColumn
vRtrMplsLspPathResignal = _VRtrMplsLspPathResignal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 33),
    _VRtrMplsLspPathResignal_Type()
)
vRtrMplsLspPathResignal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathResignal.setStatus("current")


class _VRtrMplsLspPathTunnelCRHopListIndex_Type(Integer32):
    """Custom type vRtrMplsLspPathTunnelCRHopListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsLspPathTunnelCRHopListIndex_Type.__name__ = "Integer32"
_VRtrMplsLspPathTunnelCRHopListIndex_Object = MibTableColumn
vRtrMplsLspPathTunnelCRHopListIndex = _VRtrMplsLspPathTunnelCRHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 34),
    _VRtrMplsLspPathTunnelCRHopListIndex_Type()
)
vRtrMplsLspPathTunnelCRHopListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTunnelCRHopListIndex.setStatus("current")
_VRtrMplsLspPathOperMTU_Type = Unsigned32
_VRtrMplsLspPathOperMTU_Object = MibTableColumn
vRtrMplsLspPathOperMTU = _VRtrMplsLspPathOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 35),
    _VRtrMplsLspPathOperMTU_Type()
)
vRtrMplsLspPathOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperMTU.setStatus("current")


class _VRtrMplsLspPathRecordLabel_Type(Integer32):
    """Custom type vRtrMplsLspPathRecordLabel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("record", 1),
          ("noRecord", 2))
    )


_VRtrMplsLspPathRecordLabel_Type.__name__ = "Integer32"
_VRtrMplsLspPathRecordLabel_Object = MibTableColumn
vRtrMplsLspPathRecordLabel = _VRtrMplsLspPathRecordLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 36),
    _VRtrMplsLspPathRecordLabel_Type()
)
vRtrMplsLspPathRecordLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathRecordLabel.setStatus("current")


class _VRtrMplsLspPathSrlg_Type(TruthValue):
    """Custom type vRtrMplsLspPathSrlg based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspPathSrlg_Type.__name__ = "TruthValue"
_VRtrMplsLspPathSrlg_Object = MibTableColumn
vRtrMplsLspPathSrlg = _VRtrMplsLspPathSrlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 37),
    _VRtrMplsLspPathSrlg_Type()
)
vRtrMplsLspPathSrlg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathSrlg.setStatus("current")
_VRtrMplsLspPathSrlgDisjoint_Type = TruthValue
_VRtrMplsLspPathSrlgDisjoint_Object = MibTableColumn
vRtrMplsLspPathSrlgDisjoint = _VRtrMplsLspPathSrlgDisjoint_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 38),
    _VRtrMplsLspPathSrlgDisjoint_Type()
)
vRtrMplsLspPathSrlgDisjoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathSrlgDisjoint.setStatus("current")
_VRtrMplsLspPathLastResigAttempt_Type = TimeStamp
_VRtrMplsLspPathLastResigAttempt_Object = MibTableColumn
vRtrMplsLspPathLastResigAttempt = _VRtrMplsLspPathLastResigAttempt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 39),
    _VRtrMplsLspPathLastResigAttempt_Type()
)
vRtrMplsLspPathLastResigAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastResigAttempt.setStatus("current")
_VRtrMplsLspPathMetric_Type = Unsigned32
_VRtrMplsLspPathMetric_Object = MibTableColumn
vRtrMplsLspPathMetric = _VRtrMplsLspPathMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 40),
    _VRtrMplsLspPathMetric_Type()
)
vRtrMplsLspPathMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMetric.setStatus("current")
_VRtrMplsLspPathLastMBBType_Type = TmnxMplsMBBType
_VRtrMplsLspPathLastMBBType_Object = MibTableColumn
vRtrMplsLspPathLastMBBType = _VRtrMplsLspPathLastMBBType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 41),
    _VRtrMplsLspPathLastMBBType_Type()
)
vRtrMplsLspPathLastMBBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastMBBType.setStatus("current")
_VRtrMplsLspPathLastMBBEnd_Type = TimeStamp
_VRtrMplsLspPathLastMBBEnd_Object = MibTableColumn
vRtrMplsLspPathLastMBBEnd = _VRtrMplsLspPathLastMBBEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 42),
    _VRtrMplsLspPathLastMBBEnd_Type()
)
vRtrMplsLspPathLastMBBEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastMBBEnd.setStatus("current")
_VRtrMplsLspPathLastMBBMetric_Type = Unsigned32
_VRtrMplsLspPathLastMBBMetric_Object = MibTableColumn
vRtrMplsLspPathLastMBBMetric = _VRtrMplsLspPathLastMBBMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 43),
    _VRtrMplsLspPathLastMBBMetric_Type()
)
vRtrMplsLspPathLastMBBMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastMBBMetric.setStatus("current")


class _VRtrMplsLspPathLastMBBState_Type(Integer32):
    """Custom type vRtrMplsLspPathLastMBBState based on Integer32"""
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
          ("success", 2),
          ("fail", 3))
    )


_VRtrMplsLspPathLastMBBState_Type.__name__ = "Integer32"
_VRtrMplsLspPathLastMBBState_Object = MibTableColumn
vRtrMplsLspPathLastMBBState = _VRtrMplsLspPathLastMBBState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 44),
    _VRtrMplsLspPathLastMBBState_Type()
)
vRtrMplsLspPathLastMBBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastMBBState.setStatus("current")
_VRtrMplsLspPathMBBTypeInProg_Type = TmnxMplsMBBType
_VRtrMplsLspPathMBBTypeInProg_Object = MibTableColumn
vRtrMplsLspPathMBBTypeInProg = _VRtrMplsLspPathMBBTypeInProg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 45),
    _VRtrMplsLspPathMBBTypeInProg_Type()
)
vRtrMplsLspPathMBBTypeInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBTypeInProg.setStatus("current")
_VRtrMplsLspPathMBBStarted_Type = TimeStamp
_VRtrMplsLspPathMBBStarted_Object = MibTableColumn
vRtrMplsLspPathMBBStarted = _VRtrMplsLspPathMBBStarted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 46),
    _VRtrMplsLspPathMBBStarted_Type()
)
vRtrMplsLspPathMBBStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBStarted.setStatus("current")
_VRtrMplsLspPathMBBNextRetry_Type = Unsigned32
_VRtrMplsLspPathMBBNextRetry_Object = MibTableColumn
vRtrMplsLspPathMBBNextRetry = _VRtrMplsLspPathMBBNextRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 47),
    _VRtrMplsLspPathMBBNextRetry_Type()
)
vRtrMplsLspPathMBBNextRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBNextRetry.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBNextRetry.setUnits("seconds")
_VRtrMplsLspPathMBBRetryAttempts_Type = Unsigned32
_VRtrMplsLspPathMBBRetryAttempts_Object = MibTableColumn
vRtrMplsLspPathMBBRetryAttempts = _VRtrMplsLspPathMBBRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 48),
    _VRtrMplsLspPathMBBRetryAttempts_Type()
)
vRtrMplsLspPathMBBRetryAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBRetryAttempts.setStatus("current")
_VRtrMplsLspPathMBBFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsLspPathMBBFailCode_Object = MibTableColumn
vRtrMplsLspPathMBBFailCode = _VRtrMplsLspPathMBBFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 49),
    _VRtrMplsLspPathMBBFailCode_Type()
)
vRtrMplsLspPathMBBFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBFailCode.setStatus("current")
_VRtrMplsLspPathMBBFailNodeArType_Type = InetAddressType
_VRtrMplsLspPathMBBFailNodeArType_Object = MibTableColumn
vRtrMplsLspPathMBBFailNodeArType = _VRtrMplsLspPathMBBFailNodeArType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 50),
    _VRtrMplsLspPathMBBFailNodeArType_Type()
)
vRtrMplsLspPathMBBFailNodeArType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBFailNodeArType.setStatus("current")


class _VRtrMplsLspPathMBBFailNodeAddr_Type(InetAddress):
    """Custom type vRtrMplsLspPathMBBFailNodeAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsLspPathMBBFailNodeAddr_Type.__name__ = "InetAddress"
_VRtrMplsLspPathMBBFailNodeAddr_Object = MibTableColumn
vRtrMplsLspPathMBBFailNodeAddr = _VRtrMplsLspPathMBBFailNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 51),
    _VRtrMplsLspPathMBBFailNodeAddr_Type()
)
vRtrMplsLspPathMBBFailNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBFailNodeAddr.setStatus("current")


class _VRtrMplsLspPathClassType_Type(TmnxRsvpDSTEClassType):
    """Custom type vRtrMplsLspPathClassType based on TmnxRsvpDSTEClassType"""
    defaultValue = 0


_VRtrMplsLspPathClassType_Type.__name__ = "TmnxRsvpDSTEClassType"
_VRtrMplsLspPathClassType_Object = MibTableColumn
vRtrMplsLspPathClassType = _VRtrMplsLspPathClassType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 52),
    _VRtrMplsLspPathClassType_Type()
)
vRtrMplsLspPathClassType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathClassType.setStatus("current")
_VRtrMplsLspPathOperMetric_Type = Unsigned32
_VRtrMplsLspPathOperMetric_Object = MibTableColumn
vRtrMplsLspPathOperMetric = _VRtrMplsLspPathOperMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 53),
    _VRtrMplsLspPathOperMetric_Type()
)
vRtrMplsLspPathOperMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperMetric.setStatus("current")
_VRtrMplsLspPathResignalEligible_Type = TruthValue
_VRtrMplsLspPathResignalEligible_Object = MibTableColumn
vRtrMplsLspPathResignalEligible = _VRtrMplsLspPathResignalEligible_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 54),
    _VRtrMplsLspPathResignalEligible_Type()
)
vRtrMplsLspPathResignalEligible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathResignalEligible.setStatus("current")
_VRtrMplsLspPathIsFastRetry_Type = TruthValue
_VRtrMplsLspPathIsFastRetry_Object = MibTableColumn
vRtrMplsLspPathIsFastRetry = _VRtrMplsLspPathIsFastRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 55),
    _VRtrMplsLspPathIsFastRetry_Type()
)
vRtrMplsLspPathIsFastRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathIsFastRetry.setStatus("current")


class _VRtrMplsLspPathBackupCT_Type(Integer32):
    """Custom type vRtrMplsLspPathBackupCT based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspPathBackupCT_Type.__name__ = "Integer32"
_VRtrMplsLspPathBackupCT_Object = MibTableColumn
vRtrMplsLspPathBackupCT = _VRtrMplsLspPathBackupCT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 56),
    _VRtrMplsLspPathBackupCT_Type()
)
vRtrMplsLspPathBackupCT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBackupCT.setStatus("current")
_VRtrMplsLspPathMainCTRetryRem_Type = Unsigned32
_VRtrMplsLspPathMainCTRetryRem_Object = MibTableColumn
vRtrMplsLspPathMainCTRetryRem = _VRtrMplsLspPathMainCTRetryRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 57),
    _VRtrMplsLspPathMainCTRetryRem_Type()
)
vRtrMplsLspPathMainCTRetryRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMainCTRetryRem.setStatus("current")


class _VRtrMplsLspPathOperCT_Type(Integer32):
    """Custom type vRtrMplsLspPathOperCT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspPathOperCT_Type.__name__ = "Integer32"
_VRtrMplsLspPathOperCT_Object = MibTableColumn
vRtrMplsLspPathOperCT = _VRtrMplsLspPathOperCT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 58),
    _VRtrMplsLspPathOperCT_Type()
)
vRtrMplsLspPathOperCT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperCT.setStatus("current")


class _VRtrMplsLspPathNewPathIndex_Type(MplsTunnelIndex):
    """Custom type vRtrMplsLspPathNewPathIndex based on MplsTunnelIndex"""
    defaultValue = 0


_VRtrMplsLspPathNewPathIndex_Type.__name__ = "MplsTunnelIndex"
_VRtrMplsLspPathNewPathIndex_Object = MibTableColumn
vRtrMplsLspPathNewPathIndex = _VRtrMplsLspPathNewPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 59),
    _VRtrMplsLspPathNewPathIndex_Type()
)
vRtrMplsLspPathNewPathIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathNewPathIndex.setStatus("current")
_VRtrMplsLspPathMBBMainCTRetryRem_Type = Unsigned32
_VRtrMplsLspPathMBBMainCTRetryRem_Object = MibTableColumn
vRtrMplsLspPathMBBMainCTRetryRem = _VRtrMplsLspPathMBBMainCTRetryRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 60),
    _VRtrMplsLspPathMBBMainCTRetryRem_Type()
)
vRtrMplsLspPathMBBMainCTRetryRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBMainCTRetryRem.setStatus("current")
_VRtrMplsLspPathSigBWMBBInProg_Type = Unsigned32
_VRtrMplsLspPathSigBWMBBInProg_Object = MibTableColumn
vRtrMplsLspPathSigBWMBBInProg = _VRtrMplsLspPathSigBWMBBInProg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 61),
    _VRtrMplsLspPathSigBWMBBInProg_Type()
)
vRtrMplsLspPathSigBWMBBInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathSigBWMBBInProg.setStatus("current")
_VRtrMplsLspPathSigBWLastMBB_Type = Unsigned32
_VRtrMplsLspPathSigBWLastMBB_Object = MibTableColumn
vRtrMplsLspPathSigBWLastMBB = _VRtrMplsLspPathSigBWLastMBB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 62),
    _VRtrMplsLspPathSigBWLastMBB_Type()
)
vRtrMplsLspPathSigBWLastMBB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathSigBWLastMBB.setStatus("current")


class _VRtrMplsLspPathActiveByManual_Type(Integer32):
    """Custom type vRtrMplsLspPathActiveByManual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("noForce", 1),
          ("force", 2))
    )


_VRtrMplsLspPathActiveByManual_Type.__name__ = "Integer32"
_VRtrMplsLspPathActiveByManual_Object = MibTableColumn
vRtrMplsLspPathActiveByManual = _VRtrMplsLspPathActiveByManual_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 63),
    _VRtrMplsLspPathActiveByManual_Type()
)
vRtrMplsLspPathActiveByManual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathActiveByManual.setStatus("current")
_VRtrMplsLspPathTimeoutIn_Type = Unsigned32
_VRtrMplsLspPathTimeoutIn_Object = MibTableColumn
vRtrMplsLspPathTimeoutIn = _VRtrMplsLspPathTimeoutIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 64),
    _VRtrMplsLspPathTimeoutIn_Type()
)
vRtrMplsLspPathTimeoutIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTimeoutIn.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTimeoutIn.setUnits("seconds")
_VRtrMplsLspPathMBBTimeoutIn_Type = Unsigned32
_VRtrMplsLspPathMBBTimeoutIn_Object = MibTableColumn
vRtrMplsLspPathMBBTimeoutIn = _VRtrMplsLspPathMBBTimeoutIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 65),
    _VRtrMplsLspPathMBBTimeoutIn_Type()
)
vRtrMplsLspPathMBBTimeoutIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBTimeoutIn.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBTimeoutIn.setUnits("seconds")
_VRtrMplsLspPathBfdTemplateName_Type = TNamedItemOrEmpty
_VRtrMplsLspPathBfdTemplateName_Object = MibTableColumn
vRtrMplsLspPathBfdTemplateName = _VRtrMplsLspPathBfdTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 66),
    _VRtrMplsLspPathBfdTemplateName_Type()
)
vRtrMplsLspPathBfdTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBfdTemplateName.setStatus("current")


class _VRtrMplsLspPathBfdEnable_Type(TruthValue):
    """Custom type vRtrMplsLspPathBfdEnable based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspPathBfdEnable_Type.__name__ = "TruthValue"
_VRtrMplsLspPathBfdEnable_Object = MibTableColumn
vRtrMplsLspPathBfdEnable = _VRtrMplsLspPathBfdEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 67),
    _VRtrMplsLspPathBfdEnable_Type()
)
vRtrMplsLspPathBfdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBfdEnable.setStatus("current")


class _VRtrMplsLspPathBfdPingIntvl_Type(Unsigned32):
    """Custom type vRtrMplsLspPathBfdPingIntvl based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 300),
    )


_VRtrMplsLspPathBfdPingIntvl_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathBfdPingIntvl_Object = MibTableColumn
vRtrMplsLspPathBfdPingIntvl = _VRtrMplsLspPathBfdPingIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 68),
    _VRtrMplsLspPathBfdPingIntvl_Type()
)
vRtrMplsLspPathBfdPingIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBfdPingIntvl.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBfdPingIntvl.setUnits("seconds")
_VRtrMplsLspPathLastUpdateTime_Type = TimeStamp
_VRtrMplsLspPathLastUpdateTime_Object = MibTableColumn
vRtrMplsLspPathLastUpdateTime = _VRtrMplsLspPathLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 69),
    _VRtrMplsLspPathLastUpdateTime_Type()
)
vRtrMplsLspPathLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastUpdateTime.setStatus("current")
_VRtrMplsLspPathLastUpdateId_Type = Unsigned32
_VRtrMplsLspPathLastUpdateId_Object = MibTableColumn
vRtrMplsLspPathLastUpdateId = _VRtrMplsLspPathLastUpdateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 70),
    _VRtrMplsLspPathLastUpdateId_Type()
)
vRtrMplsLspPathLastUpdateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastUpdateId.setStatus("current")


class _VRtrMplsLspPathLastUpdateState_Type(Integer32):
    """Custom type vRtrMplsLspPathLastUpdateState based on Integer32"""
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
          ("success", 2),
          ("fail", 3))
    )


_VRtrMplsLspPathLastUpdateState_Type.__name__ = "Integer32"
_VRtrMplsLspPathLastUpdateState_Object = MibTableColumn
vRtrMplsLspPathLastUpdateState = _VRtrMplsLspPathLastUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 71),
    _VRtrMplsLspPathLastUpdateState_Type()
)
vRtrMplsLspPathLastUpdateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastUpdateState.setStatus("current")
_VRtrMplsLspPathLastUpdFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsLspPathLastUpdFailCode_Object = MibTableColumn
vRtrMplsLspPathLastUpdFailCode = _VRtrMplsLspPathLastUpdFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 72),
    _VRtrMplsLspPathLastUpdFailCode_Type()
)
vRtrMplsLspPathLastUpdFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastUpdFailCode.setStatus("current")


class _VRtrMplsLspPathBfdUpWaitTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspPathBfdUpWaitTimer based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrMplsLspPathBfdUpWaitTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathBfdUpWaitTimer_Object = MibTableColumn
vRtrMplsLspPathBfdUpWaitTimer = _VRtrMplsLspPathBfdUpWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 73),
    _VRtrMplsLspPathBfdUpWaitTimer_Type()
)
vRtrMplsLspPathBfdUpWaitTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBfdUpWaitTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBfdUpWaitTimer.setUnits("seconds")


class _VRtrMplsLspPathBfdUpWaitTmLeft_Type(Unsigned32):
    """Custom type vRtrMplsLspPathBfdUpWaitTmLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrMplsLspPathBfdUpWaitTmLeft_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathBfdUpWaitTmLeft_Object = MibTableColumn
vRtrMplsLspPathBfdUpWaitTmLeft = _VRtrMplsLspPathBfdUpWaitTmLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 74),
    _VRtrMplsLspPathBfdUpWaitTmLeft_Type()
)
vRtrMplsLspPathBfdUpWaitTmLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBfdUpWaitTmLeft.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBfdUpWaitTmLeft.setUnits("seconds")


class _VRtrMplsLspPathBfdState_Type(Integer32):
    """Custom type vRtrMplsLspPathBfdState based on Integer32"""
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
        *(("notApplicable", 0),
          ("down", 1),
          ("up", 2),
          ("awaitToUp", 3),
          ("failToStart", 4))
    )


_VRtrMplsLspPathBfdState_Type.__name__ = "Integer32"
_VRtrMplsLspPathBfdState_Object = MibTableColumn
vRtrMplsLspPathBfdState = _VRtrMplsLspPathBfdState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 75),
    _VRtrMplsLspPathBfdState_Type()
)
vRtrMplsLspPathBfdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBfdState.setStatus("current")


class _VRtrMplsLspPathBfdStartFailRsn_Type(DisplayString):
    """Custom type vRtrMplsLspPathBfdStartFailRsn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_VRtrMplsLspPathBfdStartFailRsn_Type.__name__ = "DisplayString"
_VRtrMplsLspPathBfdStartFailRsn_Object = MibTableColumn
vRtrMplsLspPathBfdStartFailRsn = _VRtrMplsLspPathBfdStartFailRsn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 76),
    _VRtrMplsLspPathBfdStartFailRsn_Type()
)
vRtrMplsLspPathBfdStartFailRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBfdStartFailRsn.setStatus("current")


class _VRtrMplsLspPathBfdOperUpWaitTmr_Type(Unsigned32):
    """Custom type vRtrMplsLspPathBfdOperUpWaitTmr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrMplsLspPathBfdOperUpWaitTmr_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathBfdOperUpWaitTmr_Object = MibTableColumn
vRtrMplsLspPathBfdOperUpWaitTmr = _VRtrMplsLspPathBfdOperUpWaitTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 77),
    _VRtrMplsLspPathBfdOperUpWaitTmr_Type()
)
vRtrMplsLspPathBfdOperUpWaitTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBfdOperUpWaitTmr.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBfdOperUpWaitTmr.setUnits("seconds")
_VRtrMplsLspPathSelfPingOprState_Type = TmnxOperState
_VRtrMplsLspPathSelfPingOprState_Object = MibTableColumn
vRtrMplsLspPathSelfPingOprState = _VRtrMplsLspPathSelfPingOprState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 78),
    _VRtrMplsLspPathSelfPingOprState_Type()
)
vRtrMplsLspPathSelfPingOprState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathSelfPingOprState.setStatus("current")
_VRtrMplsLspPathLastMBBFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsLspPathLastMBBFailCode_Object = MibTableColumn
vRtrMplsLspPathLastMBBFailCode = _VRtrMplsLspPathLastMBBFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 79),
    _VRtrMplsLspPathLastMBBFailCode_Type()
)
vRtrMplsLspPathLastMBBFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastMBBFailCode.setStatus("current")
_VRtrMplsLspPathDegraded_Type = TruthValue
_VRtrMplsLspPathDegraded_Object = MibTableColumn
vRtrMplsLspPathDegraded = _VRtrMplsLspPathDegraded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 80),
    _VRtrMplsLspPathDegraded_Type()
)
vRtrMplsLspPathDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathDegraded.setStatus("current")


class _VRtrMplsLspPathDegradedReason_Type(Bits):
    """Custom type vRtrMplsLspPathDegradedReason based on Bits"""
    namedValues = NamedValues(
        *(("frrInUse", 0),
          ("softPreempted", 1),
          ("bfdDown", 2),
          ("manualSwitch", 3))
    )

_VRtrMplsLspPathDegradedReason_Type.__name__ = "Bits"
_VRtrMplsLspPathDegradedReason_Object = MibTableColumn
vRtrMplsLspPathDegradedReason = _VRtrMplsLspPathDegradedReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 81),
    _VRtrMplsLspPathDegradedReason_Type()
)
vRtrMplsLspPathDegradedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathDegradedReason.setStatus("current")


class _VRtrMplsLspPathReturnPathLabel_Type(Unsigned32):
    """Custom type vRtrMplsLspPathReturnPathLabel based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1048512),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_VRtrMplsLspPathReturnPathLabel_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathReturnPathLabel_Object = MibTableColumn
vRtrMplsLspPathReturnPathLabel = _VRtrMplsLspPathReturnPathLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 82),
    _VRtrMplsLspPathReturnPathLabel_Type()
)
vRtrMplsLspPathReturnPathLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathReturnPathLabel.setStatus("current")
_VRtrMplsLspPathStatTable_Object = MibTable
vRtrMplsLspPathStatTable = _VRtrMplsLspPathStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5)
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathStatTable.setStatus("current")
_VRtrMplsLspPathStatEntry_Object = MibTableRow
vRtrMplsLspPathStatEntry = _VRtrMplsLspPathStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathStatEntry.setStatus("current")
_VRtrMplsLspPathTimeUp_Type = TmnxTimeInterval
_VRtrMplsLspPathTimeUp_Object = MibTableColumn
vRtrMplsLspPathTimeUp = _VRtrMplsLspPathTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5, 1, 1),
    _VRtrMplsLspPathTimeUp_Type()
)
vRtrMplsLspPathTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTimeUp.setStatus("current")
_VRtrMplsLspPathTimeDown_Type = TmnxTimeInterval
_VRtrMplsLspPathTimeDown_Object = MibTableColumn
vRtrMplsLspPathTimeDown = _VRtrMplsLspPathTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5, 1, 2),
    _VRtrMplsLspPathTimeDown_Type()
)
vRtrMplsLspPathTimeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTimeDown.setStatus("current")
_VRtrMplsLspPathRetryAttempts_Type = Unsigned32
_VRtrMplsLspPathRetryAttempts_Object = MibTableColumn
vRtrMplsLspPathRetryAttempts = _VRtrMplsLspPathRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5, 1, 3),
    _VRtrMplsLspPathRetryAttempts_Type()
)
vRtrMplsLspPathRetryAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathRetryAttempts.setStatus("current")
_VRtrMplsLspPathTransitionCount_Type = Counter32
_VRtrMplsLspPathTransitionCount_Object = MibTableColumn
vRtrMplsLspPathTransitionCount = _VRtrMplsLspPathTransitionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5, 1, 4),
    _VRtrMplsLspPathTransitionCount_Type()
)
vRtrMplsLspPathTransitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTransitionCount.setStatus("current")
_VRtrMplsLspPathCspfQueries_Type = Counter32
_VRtrMplsLspPathCspfQueries_Object = MibTableColumn
vRtrMplsLspPathCspfQueries = _VRtrMplsLspPathCspfQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5, 1, 5),
    _VRtrMplsLspPathCspfQueries_Type()
)
vRtrMplsLspPathCspfQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathCspfQueries.setStatus("current")
_VRtrMplsXCTable_Object = MibTable
vRtrMplsXCTable = _VRtrMplsXCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6)
)
if mibBuilder.loadTexts:
    vRtrMplsXCTable.setStatus("current")
_VRtrMplsXCEntry_Object = MibTableRow
vRtrMplsXCEntry = _VRtrMplsXCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1)
)
vRtrMplsXCEntry.setIndexNames(
    (0, "MPLS-LSR-MIB", "mplsXCLspId"),
)
if mibBuilder.loadTexts:
    vRtrMplsXCEntry.setStatus("current")


class _VRtrMplsXCIndex_Type(Integer32):
    """Custom type vRtrMplsXCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsXCIndex_Type.__name__ = "Integer32"
_VRtrMplsXCIndex_Object = MibTableColumn
vRtrMplsXCIndex = _VRtrMplsXCIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 1),
    _VRtrMplsXCIndex_Type()
)
vRtrMplsXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsXCIndex.setStatus("current")
_VRtrMplsInSegmentIfIndex_Type = InterfaceIndexOrZero
_VRtrMplsInSegmentIfIndex_Object = MibTableColumn
vRtrMplsInSegmentIfIndex = _VRtrMplsInSegmentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 2),
    _VRtrMplsInSegmentIfIndex_Type()
)
vRtrMplsInSegmentIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInSegmentIfIndex.setStatus("current")
_VRtrMplsInSegmentLabel_Type = MplsLabel
_VRtrMplsInSegmentLabel_Object = MibTableColumn
vRtrMplsInSegmentLabel = _VRtrMplsInSegmentLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 3),
    _VRtrMplsInSegmentLabel_Type()
)
vRtrMplsInSegmentLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInSegmentLabel.setStatus("current")


class _VRtrMplsOutSegmentIndex_Type(Integer32):
    """Custom type vRtrMplsOutSegmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrMplsOutSegmentIndex_Type.__name__ = "Integer32"
_VRtrMplsOutSegmentIndex_Object = MibTableColumn
vRtrMplsOutSegmentIndex = _VRtrMplsOutSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 4),
    _VRtrMplsOutSegmentIndex_Type()
)
vRtrMplsOutSegmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutSegmentIndex.setStatus("current")
_VRtrMplsERHopTunnelIndex_Type = Integer32
_VRtrMplsERHopTunnelIndex_Object = MibTableColumn
vRtrMplsERHopTunnelIndex = _VRtrMplsERHopTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 5),
    _VRtrMplsERHopTunnelIndex_Type()
)
vRtrMplsERHopTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsERHopTunnelIndex.setStatus("current")
_VRtrMplsARHopTunnelIndex_Type = Integer32
_VRtrMplsARHopTunnelIndex_Object = MibTableColumn
vRtrMplsARHopTunnelIndex = _VRtrMplsARHopTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 6),
    _VRtrMplsARHopTunnelIndex_Type()
)
vRtrMplsARHopTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsARHopTunnelIndex.setStatus("current")
_VRtrMplsRsvpSessionIndex_Type = Unsigned32
_VRtrMplsRsvpSessionIndex_Object = MibTableColumn
vRtrMplsRsvpSessionIndex = _VRtrMplsRsvpSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 7),
    _VRtrMplsRsvpSessionIndex_Type()
)
vRtrMplsRsvpSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsRsvpSessionIndex.setStatus("current")
_VRtrMplsXCFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsXCFailCode_Object = MibTableColumn
vRtrMplsXCFailCode = _VRtrMplsXCFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 8),
    _VRtrMplsXCFailCode_Type()
)
vRtrMplsXCFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsXCFailCode.setStatus("current")
_VRtrMplsXCCHopTableIndex_Type = Integer32
_VRtrMplsXCCHopTableIndex_Object = MibTableColumn
vRtrMplsXCCHopTableIndex = _VRtrMplsXCCHopTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 9),
    _VRtrMplsXCCHopTableIndex_Type()
)
vRtrMplsXCCHopTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsXCCHopTableIndex.setStatus("current")
_VRtrMplsGeneralTable_Object = MibTable
vRtrMplsGeneralTable = _VRtrMplsGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7)
)
if mibBuilder.loadTexts:
    vRtrMplsGeneralTable.setStatus("current")
_VRtrMplsGeneralEntry_Object = MibTableRow
vRtrMplsGeneralEntry = _VRtrMplsGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1)
)
vRtrMplsGeneralEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrMplsGeneralEntry.setStatus("current")
_VRtrMplsGeneralLastChange_Type = TimeStamp
_VRtrMplsGeneralLastChange_Object = MibTableColumn
vRtrMplsGeneralLastChange = _VRtrMplsGeneralLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 1),
    _VRtrMplsGeneralLastChange_Type()
)
vRtrMplsGeneralLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralLastChange.setStatus("current")


class _VRtrMplsGeneralAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsGeneralAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsGeneralAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsGeneralAdminState_Object = MibTableColumn
vRtrMplsGeneralAdminState = _VRtrMplsGeneralAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 2),
    _VRtrMplsGeneralAdminState_Type()
)
vRtrMplsGeneralAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralAdminState.setStatus("current")
_VRtrMplsGeneralOperState_Type = TmnxOperState
_VRtrMplsGeneralOperState_Object = MibTableColumn
vRtrMplsGeneralOperState = _VRtrMplsGeneralOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 3),
    _VRtrMplsGeneralOperState_Type()
)
vRtrMplsGeneralOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralOperState.setStatus("current")


class _VRtrMplsGeneralPropagateTtl_Type(TruthValue):
    """Custom type vRtrMplsGeneralPropagateTtl based on TruthValue"""
    defaultValue = 1


_VRtrMplsGeneralPropagateTtl_Type.__name__ = "TruthValue"
_VRtrMplsGeneralPropagateTtl_Object = MibTableColumn
vRtrMplsGeneralPropagateTtl = _VRtrMplsGeneralPropagateTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 4),
    _VRtrMplsGeneralPropagateTtl_Type()
)
vRtrMplsGeneralPropagateTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralPropagateTtl.setStatus("obsolete")


class _VRtrMplsGeneralTE_Type(Integer32):
    """Custom type vRtrMplsGeneralTE based on Integer32"""
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
          ("bgp", 2),
          ("bgpigp", 3))
    )


_VRtrMplsGeneralTE_Type.__name__ = "Integer32"
_VRtrMplsGeneralTE_Object = MibTableColumn
vRtrMplsGeneralTE = _VRtrMplsGeneralTE_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 5),
    _VRtrMplsGeneralTE_Type()
)
vRtrMplsGeneralTE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralTE.setStatus("obsolete")
_VRtrMplsGeneralNewLspIndex_Type = TestAndIncr
_VRtrMplsGeneralNewLspIndex_Object = MibTableColumn
vRtrMplsGeneralNewLspIndex = _VRtrMplsGeneralNewLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 6),
    _VRtrMplsGeneralNewLspIndex_Type()
)
vRtrMplsGeneralNewLspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralNewLspIndex.setStatus("current")


class _VRtrMplsGeneralOptimizeTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralOptimizeTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrMplsGeneralOptimizeTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralOptimizeTimer_Object = MibTableColumn
vRtrMplsGeneralOptimizeTimer = _VRtrMplsGeneralOptimizeTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 7),
    _VRtrMplsGeneralOptimizeTimer_Type()
)
vRtrMplsGeneralOptimizeTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralOptimizeTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralOptimizeTimer.setUnits("seconds")


class _VRtrMplsGeneralFRObject_Type(TruthValue):
    """Custom type vRtrMplsGeneralFRObject based on TruthValue"""
    defaultValue = 1


_VRtrMplsGeneralFRObject_Type.__name__ = "TruthValue"
_VRtrMplsGeneralFRObject_Object = MibTableColumn
vRtrMplsGeneralFRObject = _VRtrMplsGeneralFRObject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 8),
    _VRtrMplsGeneralFRObject_Type()
)
vRtrMplsGeneralFRObject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralFRObject.setStatus("current")


class _VRtrMplsGeneralResignalTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralResignalTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 10080),
    )


_VRtrMplsGeneralResignalTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralResignalTimer_Object = MibTableColumn
vRtrMplsGeneralResignalTimer = _VRtrMplsGeneralResignalTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 9),
    _VRtrMplsGeneralResignalTimer_Type()
)
vRtrMplsGeneralResignalTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralResignalTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralResignalTimer.setUnits("minutes")


class _VRtrMplsGeneralHoldTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralHoldTimer based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_VRtrMplsGeneralHoldTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralHoldTimer_Object = MibTableColumn
vRtrMplsGeneralHoldTimer = _VRtrMplsGeneralHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 10),
    _VRtrMplsGeneralHoldTimer_Type()
)
vRtrMplsGeneralHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralHoldTimer.setUnits("seconds")


class _VRtrMplsGeneralDynamicBypass_Type(TruthValue):
    """Custom type vRtrMplsGeneralDynamicBypass based on TruthValue"""
    defaultValue = 1


_VRtrMplsGeneralDynamicBypass_Type.__name__ = "TruthValue"
_VRtrMplsGeneralDynamicBypass_Object = MibTableColumn
vRtrMplsGeneralDynamicBypass = _VRtrMplsGeneralDynamicBypass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 11),
    _VRtrMplsGeneralDynamicBypass_Type()
)
vRtrMplsGeneralDynamicBypass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDynamicBypass.setStatus("current")
_VRtrMplsGeneralNextResignal_Type = Unsigned32
_VRtrMplsGeneralNextResignal_Object = MibTableColumn
vRtrMplsGeneralNextResignal = _VRtrMplsGeneralNextResignal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 12),
    _VRtrMplsGeneralNextResignal_Type()
)
vRtrMplsGeneralNextResignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralNextResignal.setStatus("current")
_VRtrMplsGeneralOperDownReason_Type = TmnxMplsOperDownReasonCode
_VRtrMplsGeneralOperDownReason_Object = MibTableColumn
vRtrMplsGeneralOperDownReason = _VRtrMplsGeneralOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 13),
    _VRtrMplsGeneralOperDownReason_Type()
)
vRtrMplsGeneralOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralOperDownReason.setStatus("current")


class _VRtrMplsGeneralSrlgFrr_Type(TruthValue):
    """Custom type vRtrMplsGeneralSrlgFrr based on TruthValue"""
    defaultValue = 2


_VRtrMplsGeneralSrlgFrr_Type.__name__ = "TruthValue"
_VRtrMplsGeneralSrlgFrr_Object = MibTableColumn
vRtrMplsGeneralSrlgFrr = _VRtrMplsGeneralSrlgFrr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 14),
    _VRtrMplsGeneralSrlgFrr_Type()
)
vRtrMplsGeneralSrlgFrr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralSrlgFrr.setStatus("current")


class _VRtrMplsGeneralSrlgFrrStrict_Type(TruthValue):
    """Custom type vRtrMplsGeneralSrlgFrrStrict based on TruthValue"""
    defaultValue = 2


_VRtrMplsGeneralSrlgFrrStrict_Type.__name__ = "TruthValue"
_VRtrMplsGeneralSrlgFrrStrict_Object = MibTableColumn
vRtrMplsGeneralSrlgFrrStrict = _VRtrMplsGeneralSrlgFrrStrict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 15),
    _VRtrMplsGeneralSrlgFrrStrict_Type()
)
vRtrMplsGeneralSrlgFrrStrict.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralSrlgFrrStrict.setStatus("current")
_VRtrMplsGeneralNewP2mpInstIndex_Type = TestAndIncr
_VRtrMplsGeneralNewP2mpInstIndex_Object = MibTableColumn
vRtrMplsGeneralNewP2mpInstIndex = _VRtrMplsGeneralNewP2mpInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 16),
    _VRtrMplsGeneralNewP2mpInstIndex_Type()
)
vRtrMplsGeneralNewP2mpInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralNewP2mpInstIndex.setStatus("current")


class _VRtrMplsGeneralLeastFillMinThd_Type(Unsigned32):
    """Custom type vRtrMplsGeneralLeastFillMinThd based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VRtrMplsGeneralLeastFillMinThd_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralLeastFillMinThd_Object = MibTableColumn
vRtrMplsGeneralLeastFillMinThd = _VRtrMplsGeneralLeastFillMinThd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 17),
    _VRtrMplsGeneralLeastFillMinThd_Type()
)
vRtrMplsGeneralLeastFillMinThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralLeastFillMinThd.setStatus("current")


class _VRtrMplsGenLeastFillReoptiThd_Type(Unsigned32):
    """Custom type vRtrMplsGenLeastFillReoptiThd based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VRtrMplsGenLeastFillReoptiThd_Type.__name__ = "Unsigned32"
_VRtrMplsGenLeastFillReoptiThd_Object = MibTableColumn
vRtrMplsGenLeastFillReoptiThd = _VRtrMplsGenLeastFillReoptiThd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 18),
    _VRtrMplsGenLeastFillReoptiThd_Type()
)
vRtrMplsGenLeastFillReoptiThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenLeastFillReoptiThd.setStatus("current")


class _VRtrMplsGeneralUseSrlgDB_Type(TruthValue):
    """Custom type vRtrMplsGeneralUseSrlgDB based on TruthValue"""
    defaultValue = 2


_VRtrMplsGeneralUseSrlgDB_Type.__name__ = "TruthValue"
_VRtrMplsGeneralUseSrlgDB_Object = MibTableColumn
vRtrMplsGeneralUseSrlgDB = _VRtrMplsGeneralUseSrlgDB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 19),
    _VRtrMplsGeneralUseSrlgDB_Type()
)
vRtrMplsGeneralUseSrlgDB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralUseSrlgDB.setStatus("current")


class _VRtrMplsGeneralP2mpResigTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralP2mpResigTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 10080),
    )


_VRtrMplsGeneralP2mpResigTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralP2mpResigTimer_Object = MibTableColumn
vRtrMplsGeneralP2mpResigTimer = _VRtrMplsGeneralP2mpResigTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 20),
    _VRtrMplsGeneralP2mpResigTimer_Type()
)
vRtrMplsGeneralP2mpResigTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralP2mpResigTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralP2mpResigTimer.setUnits("minutes")
_VRtrMplsGeneralP2mpNextResignal_Type = Unsigned32
_VRtrMplsGeneralP2mpNextResignal_Object = MibTableColumn
vRtrMplsGeneralP2mpNextResignal = _VRtrMplsGeneralP2mpNextResignal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 21),
    _VRtrMplsGeneralP2mpNextResignal_Type()
)
vRtrMplsGeneralP2mpNextResignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralP2mpNextResignal.setStatus("current")


class _VRtrMplsGeneralSecFastRetryTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralSecFastRetryTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VRtrMplsGeneralSecFastRetryTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralSecFastRetryTimer_Object = MibTableColumn
vRtrMplsGeneralSecFastRetryTimer = _VRtrMplsGeneralSecFastRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 22),
    _VRtrMplsGeneralSecFastRetryTimer_Type()
)
vRtrMplsGeneralSecFastRetryTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralSecFastRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralSecFastRetryTimer.setUnits("seconds")


class _VRtrMplsGeneralShortTTLPropLocal_Type(TruthValue):
    """Custom type vRtrMplsGeneralShortTTLPropLocal based on TruthValue"""
    defaultValue = 1


_VRtrMplsGeneralShortTTLPropLocal_Type.__name__ = "TruthValue"
_VRtrMplsGeneralShortTTLPropLocal_Object = MibTableColumn
vRtrMplsGeneralShortTTLPropLocal = _VRtrMplsGeneralShortTTLPropLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 23),
    _VRtrMplsGeneralShortTTLPropLocal_Type()
)
vRtrMplsGeneralShortTTLPropLocal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralShortTTLPropLocal.setStatus("current")


class _VRtrMplsGeneralShortTTLPropTrans_Type(TruthValue):
    """Custom type vRtrMplsGeneralShortTTLPropTrans based on TruthValue"""
    defaultValue = 1


_VRtrMplsGeneralShortTTLPropTrans_Type.__name__ = "TruthValue"
_VRtrMplsGeneralShortTTLPropTrans_Object = MibTableColumn
vRtrMplsGeneralShortTTLPropTrans = _VRtrMplsGeneralShortTTLPropTrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 24),
    _VRtrMplsGeneralShortTTLPropTrans_Type()
)
vRtrMplsGeneralShortTTLPropTrans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralShortTTLPropTrans.setStatus("current")


class _VRtrMplsGeneralStaticLspFRTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralStaticLspFRTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_VRtrMplsGeneralStaticLspFRTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralStaticLspFRTimer_Object = MibTableColumn
vRtrMplsGeneralStaticLspFRTimer = _VRtrMplsGeneralStaticLspFRTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 25),
    _VRtrMplsGeneralStaticLspFRTimer_Type()
)
vRtrMplsGeneralStaticLspFRTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralStaticLspFRTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralStaticLspFRTimer.setUnits("seconds")


class _VRtrMplsGeneralAutoBWDefSampMul_Type(Unsigned32):
    """Custom type vRtrMplsGeneralAutoBWDefSampMul based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_VRtrMplsGeneralAutoBWDefSampMul_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralAutoBWDefSampMul_Object = MibTableColumn
vRtrMplsGeneralAutoBWDefSampMul = _VRtrMplsGeneralAutoBWDefSampMul_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 26),
    _VRtrMplsGeneralAutoBWDefSampMul_Type()
)
vRtrMplsGeneralAutoBWDefSampMul.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralAutoBWDefSampMul.setStatus("current")


class _VRtrMplsGeneralAutoBWDefAdjMul_Type(Unsigned32):
    """Custom type vRtrMplsGeneralAutoBWDefAdjMul based on Unsigned32"""
    defaultValue = 288

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_VRtrMplsGeneralAutoBWDefAdjMul_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralAutoBWDefAdjMul_Object = MibTableColumn
vRtrMplsGeneralAutoBWDefAdjMul = _VRtrMplsGeneralAutoBWDefAdjMul_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 27),
    _VRtrMplsGeneralAutoBWDefAdjMul_Type()
)
vRtrMplsGeneralAutoBWDefAdjMul.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralAutoBWDefAdjMul.setStatus("current")


class _VRtrMplsGeneralExpBackoffRetry_Type(TruthValue):
    """Custom type vRtrMplsGeneralExpBackoffRetry based on TruthValue"""
    defaultValue = 2


_VRtrMplsGeneralExpBackoffRetry_Type.__name__ = "TruthValue"
_VRtrMplsGeneralExpBackoffRetry_Object = MibTableColumn
vRtrMplsGeneralExpBackoffRetry = _VRtrMplsGeneralExpBackoffRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 28),
    _VRtrMplsGeneralExpBackoffRetry_Type()
)
vRtrMplsGeneralExpBackoffRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralExpBackoffRetry.setStatus("current")


class _VRtrMplsGeneralCspfOnLooseHop_Type(TruthValue):
    """Custom type vRtrMplsGeneralCspfOnLooseHop based on TruthValue"""
    defaultValue = 2


_VRtrMplsGeneralCspfOnLooseHop_Type.__name__ = "TruthValue"
_VRtrMplsGeneralCspfOnLooseHop_Object = MibTableColumn
vRtrMplsGeneralCspfOnLooseHop = _VRtrMplsGeneralCspfOnLooseHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 29),
    _VRtrMplsGeneralCspfOnLooseHop_Type()
)
vRtrMplsGeneralCspfOnLooseHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralCspfOnLooseHop.setStatus("current")


class _VRtrMplsGeneralP2PMaxByPassAssoc_Type(Unsigned32):
    """Custom type vRtrMplsGeneralP2PMaxByPassAssoc based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 131072),
    )


_VRtrMplsGeneralP2PMaxByPassAssoc_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralP2PMaxByPassAssoc_Object = MibTableColumn
vRtrMplsGeneralP2PMaxByPassAssoc = _VRtrMplsGeneralP2PMaxByPassAssoc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 30),
    _VRtrMplsGeneralP2PMaxByPassAssoc_Type()
)
vRtrMplsGeneralP2PMaxByPassAssoc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralP2PMaxByPassAssoc.setStatus("current")


class _VRtrMplsGenP2pActPathFastRetry_Type(Unsigned32):
    """Custom type vRtrMplsGenP2pActPathFastRetry based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VRtrMplsGenP2pActPathFastRetry_Type.__name__ = "Unsigned32"
_VRtrMplsGenP2pActPathFastRetry_Object = MibTableColumn
vRtrMplsGenP2pActPathFastRetry = _VRtrMplsGenP2pActPathFastRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 31),
    _VRtrMplsGenP2pActPathFastRetry_Type()
)
vRtrMplsGenP2pActPathFastRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenP2pActPathFastRetry.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGenP2pActPathFastRetry.setUnits("seconds")


class _VRtrMplsGenP2mpS2lFastRetry_Type(Unsigned32):
    """Custom type vRtrMplsGenP2mpS2lFastRetry based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VRtrMplsGenP2mpS2lFastRetry_Type.__name__ = "Unsigned32"
_VRtrMplsGenP2mpS2lFastRetry_Object = MibTableColumn
vRtrMplsGenP2mpS2lFastRetry = _VRtrMplsGenP2mpS2lFastRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 32),
    _VRtrMplsGenP2mpS2lFastRetry_Type()
)
vRtrMplsGenP2mpS2lFastRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenP2mpS2lFastRetry.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGenP2mpS2lFastRetry.setUnits("seconds")


class _VRtrMplsGenLspInitRetryTimeout_Type(Unsigned32):
    """Custom type vRtrMplsGenLspInitRetryTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_VRtrMplsGenLspInitRetryTimeout_Type.__name__ = "Unsigned32"
_VRtrMplsGenLspInitRetryTimeout_Object = MibTableColumn
vRtrMplsGenLspInitRetryTimeout = _VRtrMplsGenLspInitRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 33),
    _VRtrMplsGenLspInitRetryTimeout_Type()
)
vRtrMplsGenLspInitRetryTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenLspInitRetryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGenLspInitRetryTimeout.setUnits("seconds")


class _VRtrMplsLoggerEventBundling_Type(TruthValue):
    """Custom type vRtrMplsLoggerEventBundling based on TruthValue"""
    defaultValue = 2


_VRtrMplsLoggerEventBundling_Type.__name__ = "TruthValue"
_VRtrMplsLoggerEventBundling_Object = MibTableColumn
vRtrMplsLoggerEventBundling = _VRtrMplsLoggerEventBundling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 34),
    _VRtrMplsLoggerEventBundling_Type()
)
vRtrMplsLoggerEventBundling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLoggerEventBundling.setStatus("current")
_VRtrMplsGenIssuMplsLockdown_Type = TruthValue
_VRtrMplsGenIssuMplsLockdown_Object = MibTableColumn
vRtrMplsGenIssuMplsLockdown = _VRtrMplsGenIssuMplsLockdown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 39),
    _VRtrMplsGenIssuMplsLockdown_Type()
)
vRtrMplsGenIssuMplsLockdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenIssuMplsLockdown.setStatus("current")


class _VRtrMplsGenFRAdminGroup_Type(TruthValue):
    """Custom type vRtrMplsGenFRAdminGroup based on TruthValue"""
    defaultValue = 2


_VRtrMplsGenFRAdminGroup_Type.__name__ = "TruthValue"
_VRtrMplsGenFRAdminGroup_Object = MibTableColumn
vRtrMplsGenFRAdminGroup = _VRtrMplsGenFRAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 40),
    _VRtrMplsGenFRAdminGroup_Type()
)
vRtrMplsGenFRAdminGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenFRAdminGroup.setStatus("current")


class _VRtrMplsGenRetryOnIgpOverload_Type(TruthValue):
    """Custom type vRtrMplsGenRetryOnIgpOverload based on TruthValue"""
    defaultValue = 2


_VRtrMplsGenRetryOnIgpOverload_Type.__name__ = "TruthValue"
_VRtrMplsGenRetryOnIgpOverload_Object = MibTableColumn
vRtrMplsGenRetryOnIgpOverload = _VRtrMplsGenRetryOnIgpOverload_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 41),
    _VRtrMplsGenRetryOnIgpOverload_Type()
)
vRtrMplsGenRetryOnIgpOverload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenRetryOnIgpOverload.setStatus("current")


class _VRtrMplsGenMbbPrefCurrentHops_Type(TruthValue):
    """Custom type vRtrMplsGenMbbPrefCurrentHops based on TruthValue"""
    defaultValue = 2


_VRtrMplsGenMbbPrefCurrentHops_Type.__name__ = "TruthValue"
_VRtrMplsGenMbbPrefCurrentHops_Object = MibTableColumn
vRtrMplsGenMbbPrefCurrentHops = _VRtrMplsGenMbbPrefCurrentHops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 42),
    _VRtrMplsGenMbbPrefCurrentHops_Type()
)
vRtrMplsGenMbbPrefCurrentHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenMbbPrefCurrentHops.setStatus("current")


class _VRtrMplsGeneralBypassResigTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralBypassResigTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10080),
    )


_VRtrMplsGeneralBypassResigTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralBypassResigTimer_Object = MibTableColumn
vRtrMplsGeneralBypassResigTimer = _VRtrMplsGeneralBypassResigTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 43),
    _VRtrMplsGeneralBypassResigTimer_Type()
)
vRtrMplsGeneralBypassResigTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralBypassResigTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralBypassResigTimer.setUnits("minutes")
_VRtrMplsGenBypassNextResignal_Type = Unsigned32
_VRtrMplsGenBypassNextResignal_Object = MibTableColumn
vRtrMplsGenBypassNextResignal = _VRtrMplsGenBypassNextResignal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 44),
    _VRtrMplsGenBypassNextResignal_Type()
)
vRtrMplsGenBypassNextResignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenBypassNextResignal.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGenBypassNextResignal.setUnits("minutes")
_VRtrMplsGeneralNewLspSRIndex_Type = TestAndIncr
_VRtrMplsGeneralNewLspSRIndex_Object = MibTableColumn
vRtrMplsGeneralNewLspSRIndex = _VRtrMplsGeneralNewLspSRIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 45),
    _VRtrMplsGeneralNewLspSRIndex_Type()
)
vRtrMplsGeneralNewLspSRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralNewLspSRIndex.setStatus("current")


class _VRtrMplsGeneralPceReport_Type(Bits):
    """Custom type vRtrMplsGeneralPceReport based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("srTe", 0),
          ("rsvpTe", 1))
    )

_VRtrMplsGeneralPceReport_Type.__name__ = "Bits"
_VRtrMplsGeneralPceReport_Object = MibTableColumn
vRtrMplsGeneralPceReport = _VRtrMplsGeneralPceReport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 46),
    _VRtrMplsGeneralPceReport_Type()
)
vRtrMplsGeneralPceReport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralPceReport.setStatus("current")


class _VRtrMplsGeneralEntropyLblRsvpTe_Type(Integer32):
    """Custom type vRtrMplsGeneralEntropyLblRsvpTe based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceDisable", 1),
          ("enable", 2))
    )


_VRtrMplsGeneralEntropyLblRsvpTe_Type.__name__ = "Integer32"
_VRtrMplsGeneralEntropyLblRsvpTe_Object = MibTableColumn
vRtrMplsGeneralEntropyLblRsvpTe = _VRtrMplsGeneralEntropyLblRsvpTe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 47),
    _VRtrMplsGeneralEntropyLblRsvpTe_Type()
)
vRtrMplsGeneralEntropyLblRsvpTe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralEntropyLblRsvpTe.setStatus("current")


class _VRtrMplsGeneralEntropyLblSrTe_Type(Integer32):
    """Custom type vRtrMplsGeneralEntropyLblSrTe based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceDisable", 1),
          ("enable", 2))
    )


_VRtrMplsGeneralEntropyLblSrTe_Type.__name__ = "Integer32"
_VRtrMplsGeneralEntropyLblSrTe_Object = MibTableColumn
vRtrMplsGeneralEntropyLblSrTe = _VRtrMplsGeneralEntropyLblSrTe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 48),
    _VRtrMplsGeneralEntropyLblSrTe_Type()
)
vRtrMplsGeneralEntropyLblSrTe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralEntropyLblSrTe.setStatus("current")


class _VRtrMplsGeneralAuxStats_Type(Bits):
    """Custom type vRtrMplsGeneralAuxStats based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("sr", 0)
    )

_VRtrMplsGeneralAuxStats_Type.__name__ = "Bits"
_VRtrMplsGeneralAuxStats_Object = MibTableColumn
vRtrMplsGeneralAuxStats = _VRtrMplsGeneralAuxStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 49),
    _VRtrMplsGeneralAuxStats_Type()
)
vRtrMplsGeneralAuxStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralAuxStats.setStatus("current")


class _VRtrMplsGenSrTeResignalTimer_Type(Unsigned32):
    """Custom type vRtrMplsGenSrTeResignalTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 10080),
    )


_VRtrMplsGenSrTeResignalTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGenSrTeResignalTimer_Object = MibTableColumn
vRtrMplsGenSrTeResignalTimer = _VRtrMplsGenSrTeResignalTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 50),
    _VRtrMplsGenSrTeResignalTimer_Type()
)
vRtrMplsGenSrTeResignalTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenSrTeResignalTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGenSrTeResignalTimer.setUnits("minutes")


class _VRtrMplsGenMaxBypassPlrAssoc_Type(Unsigned32):
    """Custom type vRtrMplsGenMaxBypassPlrAssoc based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VRtrMplsGenMaxBypassPlrAssoc_Type.__name__ = "Unsigned32"
_VRtrMplsGenMaxBypassPlrAssoc_Object = MibTableColumn
vRtrMplsGenMaxBypassPlrAssoc = _VRtrMplsGenMaxBypassPlrAssoc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 51),
    _VRtrMplsGenMaxBypassPlrAssoc_Type()
)
vRtrMplsGenMaxBypassPlrAssoc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenMaxBypassPlrAssoc.setStatus("current")


class _VRtrMplsGenLspSelfPingInterval_Type(TimeInterval):
    """Custom type vRtrMplsGenLspSelfPingInterval based on TimeInterval"""
    defaultValue = 1

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_VRtrMplsGenLspSelfPingInterval_Type.__name__ = "TimeInterval"
_VRtrMplsGenLspSelfPingInterval_Object = MibTableColumn
vRtrMplsGenLspSelfPingInterval = _VRtrMplsGenLspSelfPingInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 52),
    _VRtrMplsGenLspSelfPingInterval_Type()
)
vRtrMplsGenLspSelfPingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenLspSelfPingInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGenLspSelfPingInterval.setUnits("seconds")


class _VRtrMplsGenLspSelfPingTimeout_Type(TimeInterval):
    """Custom type vRtrMplsGenLspSelfPingTimeout based on TimeInterval"""
    defaultValue = 300

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3600),
    )


_VRtrMplsGenLspSelfPingTimeout_Type.__name__ = "TimeInterval"
_VRtrMplsGenLspSelfPingTimeout_Object = MibTableColumn
vRtrMplsGenLspSelfPingTimeout = _VRtrMplsGenLspSelfPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 53),
    _VRtrMplsGenLspSelfPingTimeout_Type()
)
vRtrMplsGenLspSelfPingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenLspSelfPingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGenLspSelfPingTimeout.setUnits("seconds")


class _VRtrMplsGenLspSelfPingRsvpTe_Type(Integer32):
    """Custom type vRtrMplsGenLspSelfPingRsvpTe based on Integer32"""
    defaultValue = 2

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


_VRtrMplsGenLspSelfPingRsvpTe_Type.__name__ = "Integer32"
_VRtrMplsGenLspSelfPingRsvpTe_Object = MibTableColumn
vRtrMplsGenLspSelfPingRsvpTe = _VRtrMplsGenLspSelfPingRsvpTe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 54),
    _VRtrMplsGenLspSelfPingRsvpTe_Type()
)
vRtrMplsGenLspSelfPingRsvpTe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenLspSelfPingRsvpTe.setStatus("current")


class _VRtrMplsGenSrTeResigOnIgpEvent_Type(TruthValue):
    """Custom type vRtrMplsGenSrTeResigOnIgpEvent based on TruthValue"""
    defaultValue = 2


_VRtrMplsGenSrTeResigOnIgpEvent_Type.__name__ = "TruthValue"
_VRtrMplsGenSrTeResigOnIgpEvent_Object = MibTableColumn
vRtrMplsGenSrTeResigOnIgpEvent = _VRtrMplsGenSrTeResigOnIgpEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 55),
    _VRtrMplsGenSrTeResigOnIgpEvent_Type()
)
vRtrMplsGenSrTeResigOnIgpEvent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenSrTeResigOnIgpEvent.setStatus("current")
_VRtrMplsGeneralV6OperState_Type = TmnxOperState
_VRtrMplsGeneralV6OperState_Object = MibTableColumn
vRtrMplsGeneralV6OperState = _VRtrMplsGeneralV6OperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 56),
    _VRtrMplsGeneralV6OperState_Type()
)
vRtrMplsGeneralV6OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralV6OperState.setStatus("current")
_VRtrMplsGeneralV6OperDownReason_Type = TmnxMplsOperDownReasonCode
_VRtrMplsGeneralV6OperDownReason_Object = MibTableColumn
vRtrMplsGeneralV6OperDownReason = _VRtrMplsGeneralV6OperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 57),
    _VRtrMplsGeneralV6OperDownReason_Type()
)
vRtrMplsGeneralV6OperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralV6OperDownReason.setStatus("current")
_VRtrMplsGenSrteNextResignal_Type = Unsigned32
_VRtrMplsGenSrteNextResignal_Object = MibTableColumn
vRtrMplsGenSrteNextResignal = _VRtrMplsGenSrteNextResignal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 58),
    _VRtrMplsGenSrteNextResignal_Type()
)
vRtrMplsGenSrteNextResignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenSrteNextResignal.setStatus("current")


class _VRtrMplsLspSelfPingTimeoutAction_Type(Integer32):
    """Custom type vRtrMplsLspSelfPingTimeoutAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("retry", 1),
          ("switch", 2))
    )


_VRtrMplsLspSelfPingTimeoutAction_Type.__name__ = "Integer32"
_VRtrMplsLspSelfPingTimeoutAction_Object = MibTableColumn
vRtrMplsLspSelfPingTimeoutAction = _VRtrMplsLspSelfPingTimeoutAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 59),
    _VRtrMplsLspSelfPingTimeoutAction_Type()
)
vRtrMplsLspSelfPingTimeoutAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspSelfPingTimeoutAction.setStatus("current")


class _VRtrMplsGenResignalOnIgpOverload_Type(TruthValue):
    """Custom type vRtrMplsGenResignalOnIgpOverload based on TruthValue"""
    defaultValue = 2


_VRtrMplsGenResignalOnIgpOverload_Type.__name__ = "TruthValue"
_VRtrMplsGenResignalOnIgpOverload_Object = MibTableColumn
vRtrMplsGenResignalOnIgpOverload = _VRtrMplsGenResignalOnIgpOverload_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 60),
    _VRtrMplsGenResignalOnIgpOverload_Type()
)
vRtrMplsGenResignalOnIgpOverload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenResignalOnIgpOverload.setStatus("current")


class _VRtrMplsGenTunnelTablePrefRsvpTe_Type(Unsigned32):
    """Custom type vRtrMplsGenTunnelTablePrefRsvpTe based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrMplsGenTunnelTablePrefRsvpTe_Type.__name__ = "Unsigned32"
_VRtrMplsGenTunnelTablePrefRsvpTe_Object = MibTableColumn
vRtrMplsGenTunnelTablePrefRsvpTe = _VRtrMplsGenTunnelTablePrefRsvpTe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 61),
    _VRtrMplsGenTunnelTablePrefRsvpTe_Type()
)
vRtrMplsGenTunnelTablePrefRsvpTe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenTunnelTablePrefRsvpTe.setStatus("current")


class _VRtrMplsGenTunnelTablePrefSrTe_Type(Unsigned32):
    """Custom type vRtrMplsGenTunnelTablePrefSrTe based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrMplsGenTunnelTablePrefSrTe_Type.__name__ = "Unsigned32"
_VRtrMplsGenTunnelTablePrefSrTe_Object = MibTableColumn
vRtrMplsGenTunnelTablePrefSrTe = _VRtrMplsGenTunnelTablePrefSrTe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 62),
    _VRtrMplsGenTunnelTablePrefSrTe_Type()
)
vRtrMplsGenTunnelTablePrefSrTe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenTunnelTablePrefSrTe.setStatus("current")
_VRtrMplsGenRsvpPccOperState_Type = TmnxOperState
_VRtrMplsGenRsvpPccOperState_Object = MibTableColumn
vRtrMplsGenRsvpPccOperState = _VRtrMplsGenRsvpPccOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 63),
    _VRtrMplsGenRsvpPccOperState_Type()
)
vRtrMplsGenRsvpPccOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenRsvpPccOperState.setStatus("current")
_VRtrMplsGenRsvpPceOperState_Type = TmnxOperState
_VRtrMplsGenRsvpPceOperState_Object = MibTableColumn
vRtrMplsGenRsvpPceOperState = _VRtrMplsGenRsvpPceOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 64),
    _VRtrMplsGenRsvpPceOperState_Type()
)
vRtrMplsGenRsvpPceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenRsvpPceOperState.setStatus("current")
_VRtrMplsGenSrTePccOperState_Type = TmnxOperState
_VRtrMplsGenSrTePccOperState_Object = MibTableColumn
vRtrMplsGenSrTePccOperState = _VRtrMplsGenSrTePccOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 65),
    _VRtrMplsGenSrTePccOperState_Type()
)
vRtrMplsGenSrTePccOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenSrTePccOperState.setStatus("current")
_VRtrMplsGenSrTePceOperState_Type = TmnxOperState
_VRtrMplsGenSrTePceOperState_Object = MibTableColumn
vRtrMplsGenSrTePceOperState = _VRtrMplsGenSrTePceOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 66),
    _VRtrMplsGenSrTePceOperState_Type()
)
vRtrMplsGenSrTePceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenSrTePceOperState.setStatus("current")
_VRtrMplsGeneralStatTable_Object = MibTable
vRtrMplsGeneralStatTable = _VRtrMplsGeneralStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8)
)
if mibBuilder.loadTexts:
    vRtrMplsGeneralStatTable.setStatus("current")
_VRtrMplsGeneralStatEntry_Object = MibTableRow
vRtrMplsGeneralStatEntry = _VRtrMplsGeneralStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsGeneralStatEntry.setStatus("current")
_VRtrMplsGeneralStaticLspOriginate_Type = Gauge32
_VRtrMplsGeneralStaticLspOriginate_Object = MibTableColumn
vRtrMplsGeneralStaticLspOriginate = _VRtrMplsGeneralStaticLspOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 1),
    _VRtrMplsGeneralStaticLspOriginate_Type()
)
vRtrMplsGeneralStaticLspOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralStaticLspOriginate.setStatus("current")
_VRtrMplsGeneralStaticLspTransit_Type = Gauge32
_VRtrMplsGeneralStaticLspTransit_Object = MibTableColumn
vRtrMplsGeneralStaticLspTransit = _VRtrMplsGeneralStaticLspTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 2),
    _VRtrMplsGeneralStaticLspTransit_Type()
)
vRtrMplsGeneralStaticLspTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralStaticLspTransit.setStatus("current")
_VRtrMplsGeneralStaticLspTerminate_Type = Gauge32
_VRtrMplsGeneralStaticLspTerminate_Object = MibTableColumn
vRtrMplsGeneralStaticLspTerminate = _VRtrMplsGeneralStaticLspTerminate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 3),
    _VRtrMplsGeneralStaticLspTerminate_Type()
)
vRtrMplsGeneralStaticLspTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralStaticLspTerminate.setStatus("current")
_VRtrMplsGeneralDynamicLspOriginate_Type = Gauge32
_VRtrMplsGeneralDynamicLspOriginate_Object = MibTableColumn
vRtrMplsGeneralDynamicLspOriginate = _VRtrMplsGeneralDynamicLspOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 4),
    _VRtrMplsGeneralDynamicLspOriginate_Type()
)
vRtrMplsGeneralDynamicLspOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDynamicLspOriginate.setStatus("current")
_VRtrMplsGeneralDynamicLspTransit_Type = Gauge32
_VRtrMplsGeneralDynamicLspTransit_Object = MibTableColumn
vRtrMplsGeneralDynamicLspTransit = _VRtrMplsGeneralDynamicLspTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 5),
    _VRtrMplsGeneralDynamicLspTransit_Type()
)
vRtrMplsGeneralDynamicLspTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDynamicLspTransit.setStatus("current")
_VRtrMplsGeneralDynamicLspTerminate_Type = Gauge32
_VRtrMplsGeneralDynamicLspTerminate_Object = MibTableColumn
vRtrMplsGeneralDynamicLspTerminate = _VRtrMplsGeneralDynamicLspTerminate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 6),
    _VRtrMplsGeneralDynamicLspTerminate_Type()
)
vRtrMplsGeneralDynamicLspTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDynamicLspTerminate.setStatus("current")
_VRtrMplsGeneralDetourLspOriginate_Type = Gauge32
_VRtrMplsGeneralDetourLspOriginate_Object = MibTableColumn
vRtrMplsGeneralDetourLspOriginate = _VRtrMplsGeneralDetourLspOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 7),
    _VRtrMplsGeneralDetourLspOriginate_Type()
)
vRtrMplsGeneralDetourLspOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDetourLspOriginate.setStatus("current")
_VRtrMplsGeneralDetourLspTransit_Type = Gauge32
_VRtrMplsGeneralDetourLspTransit_Object = MibTableColumn
vRtrMplsGeneralDetourLspTransit = _VRtrMplsGeneralDetourLspTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 8),
    _VRtrMplsGeneralDetourLspTransit_Type()
)
vRtrMplsGeneralDetourLspTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDetourLspTransit.setStatus("current")
_VRtrMplsGeneralDetourLspTerminate_Type = Gauge32
_VRtrMplsGeneralDetourLspTerminate_Object = MibTableColumn
vRtrMplsGeneralDetourLspTerminate = _VRtrMplsGeneralDetourLspTerminate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 9),
    _VRtrMplsGeneralDetourLspTerminate_Type()
)
vRtrMplsGeneralDetourLspTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDetourLspTerminate.setStatus("current")
_VRtrMplsGeneralS2lOriginate_Type = Gauge32
_VRtrMplsGeneralS2lOriginate_Object = MibTableColumn
vRtrMplsGeneralS2lOriginate = _VRtrMplsGeneralS2lOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 10),
    _VRtrMplsGeneralS2lOriginate_Type()
)
vRtrMplsGeneralS2lOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralS2lOriginate.setStatus("current")
_VRtrMplsGeneralS2lTransit_Type = Gauge32
_VRtrMplsGeneralS2lTransit_Object = MibTableColumn
vRtrMplsGeneralS2lTransit = _VRtrMplsGeneralS2lTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 11),
    _VRtrMplsGeneralS2lTransit_Type()
)
vRtrMplsGeneralS2lTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralS2lTransit.setStatus("current")
_VRtrMplsGeneralS2lTerminate_Type = Gauge32
_VRtrMplsGeneralS2lTerminate_Object = MibTableColumn
vRtrMplsGeneralS2lTerminate = _VRtrMplsGeneralS2lTerminate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 12),
    _VRtrMplsGeneralS2lTerminate_Type()
)
vRtrMplsGeneralS2lTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralS2lTerminate.setStatus("current")
_VRtrMplsGeneralLspEgrStatCount_Type = Counter32
_VRtrMplsGeneralLspEgrStatCount_Object = MibTableColumn
vRtrMplsGeneralLspEgrStatCount = _VRtrMplsGeneralLspEgrStatCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 13),
    _VRtrMplsGeneralLspEgrStatCount_Type()
)
vRtrMplsGeneralLspEgrStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralLspEgrStatCount.setStatus("current")
_VRtrMplsGeneralLspIgrStatCount_Type = Counter32
_VRtrMplsGeneralLspIgrStatCount_Object = MibTableColumn
vRtrMplsGeneralLspIgrStatCount = _VRtrMplsGeneralLspIgrStatCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 14),
    _VRtrMplsGeneralLspIgrStatCount_Type()
)
vRtrMplsGeneralLspIgrStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralLspIgrStatCount.setStatus("current")
_VRtrMplsGenMplsTpLspOriginate_Type = Gauge32
_VRtrMplsGenMplsTpLspOriginate_Object = MibTableColumn
vRtrMplsGenMplsTpLspOriginate = _VRtrMplsGenMplsTpLspOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 15),
    _VRtrMplsGenMplsTpLspOriginate_Type()
)
vRtrMplsGenMplsTpLspOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenMplsTpLspOriginate.setStatus("current")
_VRtrMplsGenMplsTpLspTransit_Type = Gauge32
_VRtrMplsGenMplsTpLspTransit_Object = MibTableColumn
vRtrMplsGenMplsTpLspTransit = _VRtrMplsGenMplsTpLspTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 16),
    _VRtrMplsGenMplsTpLspTransit_Type()
)
vRtrMplsGenMplsTpLspTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenMplsTpLspTransit.setStatus("current")
_VRtrMplsGenMplsTpLspTerminate_Type = Gauge32
_VRtrMplsGenMplsTpLspTerminate_Object = MibTableColumn
vRtrMplsGenMplsTpLspTerminate = _VRtrMplsGenMplsTpLspTerminate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 17),
    _VRtrMplsGenMplsTpLspTerminate_Type()
)
vRtrMplsGenMplsTpLspTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenMplsTpLspTerminate.setStatus("current")
_VRtrMplsGenMplsTpOrigPathInst_Type = Gauge32
_VRtrMplsGenMplsTpOrigPathInst_Object = MibTableColumn
vRtrMplsGenMplsTpOrigPathInst = _VRtrMplsGenMplsTpOrigPathInst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 18),
    _VRtrMplsGenMplsTpOrigPathInst_Type()
)
vRtrMplsGenMplsTpOrigPathInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenMplsTpOrigPathInst.setStatus("current")
_VRtrMplsGenMplsTpTranPathInst_Type = Gauge32
_VRtrMplsGenMplsTpTranPathInst_Object = MibTableColumn
vRtrMplsGenMplsTpTranPathInst = _VRtrMplsGenMplsTpTranPathInst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 19),
    _VRtrMplsGenMplsTpTranPathInst_Type()
)
vRtrMplsGenMplsTpTranPathInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenMplsTpTranPathInst.setStatus("current")
_VRtrMplsGenMplsTpTermPathInst_Type = Gauge32
_VRtrMplsGenMplsTpTermPathInst_Object = MibTableColumn
vRtrMplsGenMplsTpTermPathInst = _VRtrMplsGenMplsTpTermPathInst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 20),
    _VRtrMplsGenMplsTpTermPathInst_Type()
)
vRtrMplsGenMplsTpTermPathInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenMplsTpTermPathInst.setStatus("current")
_VRtrMplsGeneralMeshP2pOriginate_Type = Gauge32
_VRtrMplsGeneralMeshP2pOriginate_Object = MibTableColumn
vRtrMplsGeneralMeshP2pOriginate = _VRtrMplsGeneralMeshP2pOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 21),
    _VRtrMplsGeneralMeshP2pOriginate_Type()
)
vRtrMplsGeneralMeshP2pOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralMeshP2pOriginate.setStatus("current")
_VRtrMplsGeneralOneHopP2pOrigin_Type = Gauge32
_VRtrMplsGeneralOneHopP2pOrigin_Object = MibTableColumn
vRtrMplsGeneralOneHopP2pOrigin = _VRtrMplsGeneralOneHopP2pOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 22),
    _VRtrMplsGeneralOneHopP2pOrigin_Type()
)
vRtrMplsGeneralOneHopP2pOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralOneHopP2pOrigin.setStatus("current")
_VRtrMplsGeneralSrTeLspOriginate_Type = Gauge32
_VRtrMplsGeneralSrTeLspOriginate_Object = MibTableColumn
vRtrMplsGeneralSrTeLspOriginate = _VRtrMplsGeneralSrTeLspOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 23),
    _VRtrMplsGeneralSrTeLspOriginate_Type()
)
vRtrMplsGeneralSrTeLspOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralSrTeLspOriginate.setStatus("current")
_VRtrMplsGenMeshP2PSrTeLspOrig_Type = Gauge32
_VRtrMplsGenMeshP2PSrTeLspOrig_Object = MibTableColumn
vRtrMplsGenMeshP2PSrTeLspOrig = _VRtrMplsGenMeshP2PSrTeLspOrig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 24),
    _VRtrMplsGenMeshP2PSrTeLspOrig_Type()
)
vRtrMplsGenMeshP2PSrTeLspOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenMeshP2PSrTeLspOrig.setStatus("current")
_VRtrMplsGenOneHopP2PSrTeLspOrig_Type = Gauge32
_VRtrMplsGenOneHopP2PSrTeLspOrig_Object = MibTableColumn
vRtrMplsGenOneHopP2PSrTeLspOrig = _VRtrMplsGenOneHopP2PSrTeLspOrig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 25),
    _VRtrMplsGenOneHopP2PSrTeLspOrig_Type()
)
vRtrMplsGenOneHopP2PSrTeLspOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenOneHopP2PSrTeLspOrig.setStatus("current")
_VRtrMplsGenPceInitP2PSrTeLspOrig_Type = Gauge32
_VRtrMplsGenPceInitP2PSrTeLspOrig_Object = MibTableColumn
vRtrMplsGenPceInitP2PSrTeLspOrig = _VRtrMplsGenPceInitP2PSrTeLspOrig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 26),
    _VRtrMplsGenPceInitP2PSrTeLspOrig_Type()
)
vRtrMplsGenPceInitP2PSrTeLspOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenPceInitP2PSrTeLspOrig.setStatus("current")
_VRtrMplsGenLspSelfPingTimeouts_Type = Counter32
_VRtrMplsGenLspSelfPingTimeouts_Object = MibTableColumn
vRtrMplsGenLspSelfPingTimeouts = _VRtrMplsGenLspSelfPingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 27),
    _VRtrMplsGenLspSelfPingTimeouts_Type()
)
vRtrMplsGenLspSelfPingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenLspSelfPingTimeouts.setStatus("current")
_VRtrMplsGenLspSelfPingOamNoRsc_Type = Counter32
_VRtrMplsGenLspSelfPingOamNoRsc_Object = MibTableColumn
vRtrMplsGenLspSelfPingOamNoRsc = _VRtrMplsGenLspSelfPingOamNoRsc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 28),
    _VRtrMplsGenLspSelfPingOamNoRsc_Type()
)
vRtrMplsGenLspSelfPingOamNoRsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenLspSelfPingOamNoRsc.setStatus("current")
_VRtrMplsGenDynP2pLspUp_Type = Gauge32
_VRtrMplsGenDynP2pLspUp_Object = MibTableColumn
vRtrMplsGenDynP2pLspUp = _VRtrMplsGenDynP2pLspUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 29),
    _VRtrMplsGenDynP2pLspUp_Type()
)
vRtrMplsGenDynP2pLspUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenDynP2pLspUp.setStatus("current")
_VRtrMplsGenSrTeIpv4LspUp_Type = Gauge32
_VRtrMplsGenSrTeIpv4LspUp_Object = MibTableColumn
vRtrMplsGenSrTeIpv4LspUp = _VRtrMplsGenSrTeIpv4LspUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 30),
    _VRtrMplsGenSrTeIpv4LspUp_Type()
)
vRtrMplsGenSrTeIpv4LspUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenSrTeIpv4LspUp.setStatus("current")
_VRtrMplsGenSrTeIpv6LspUp_Type = Gauge32
_VRtrMplsGenSrTeIpv6LspUp_Object = MibTableColumn
vRtrMplsGenSrTeIpv6LspUp = _VRtrMplsGenSrTeIpv6LspUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 31),
    _VRtrMplsGenSrTeIpv6LspUp_Type()
)
vRtrMplsGenSrTeIpv6LspUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenSrTeIpv6LspUp.setStatus("current")
_VRtrMplsGenMeshSrTeIpv4LspUp_Type = Gauge32
_VRtrMplsGenMeshSrTeIpv4LspUp_Object = MibTableColumn
vRtrMplsGenMeshSrTeIpv4LspUp = _VRtrMplsGenMeshSrTeIpv4LspUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 32),
    _VRtrMplsGenMeshSrTeIpv4LspUp_Type()
)
vRtrMplsGenMeshSrTeIpv4LspUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenMeshSrTeIpv4LspUp.setStatus("current")
_VRtrMplsGenMeshSrTeIpv6LspUp_Type = Gauge32
_VRtrMplsGenMeshSrTeIpv6LspUp_Object = MibTableColumn
vRtrMplsGenMeshSrTeIpv6LspUp = _VRtrMplsGenMeshSrTeIpv6LspUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 33),
    _VRtrMplsGenMeshSrTeIpv6LspUp_Type()
)
vRtrMplsGenMeshSrTeIpv6LspUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenMeshSrTeIpv6LspUp.setStatus("current")
_VRtrMplsGenOneHopSrTeIpv4LspUp_Type = Gauge32
_VRtrMplsGenOneHopSrTeIpv4LspUp_Object = MibTableColumn
vRtrMplsGenOneHopSrTeIpv4LspUp = _VRtrMplsGenOneHopSrTeIpv4LspUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 34),
    _VRtrMplsGenOneHopSrTeIpv4LspUp_Type()
)
vRtrMplsGenOneHopSrTeIpv4LspUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenOneHopSrTeIpv4LspUp.setStatus("current")
_VRtrMplsGenOneHopSrTeIpv6LspUp_Type = Gauge32
_VRtrMplsGenOneHopSrTeIpv6LspUp_Object = MibTableColumn
vRtrMplsGenOneHopSrTeIpv6LspUp = _VRtrMplsGenOneHopSrTeIpv6LspUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 35),
    _VRtrMplsGenOneHopSrTeIpv6LspUp_Type()
)
vRtrMplsGenOneHopSrTeIpv6LspUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenOneHopSrTeIpv6LspUp.setStatus("current")
_VRtrMplsGenPceInitSrTeIpv4LspUp_Type = Gauge32
_VRtrMplsGenPceInitSrTeIpv4LspUp_Object = MibTableColumn
vRtrMplsGenPceInitSrTeIpv4LspUp = _VRtrMplsGenPceInitSrTeIpv4LspUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 36),
    _VRtrMplsGenPceInitSrTeIpv4LspUp_Type()
)
vRtrMplsGenPceInitSrTeIpv4LspUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenPceInitSrTeIpv4LspUp.setStatus("current")
_VRtrMplsGenPceInitSrTeIpv6LspUp_Type = Gauge32
_VRtrMplsGenPceInitSrTeIpv6LspUp_Object = MibTableColumn
vRtrMplsGenPceInitSrTeIpv6LspUp = _VRtrMplsGenPceInitSrTeIpv6LspUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 37),
    _VRtrMplsGenPceInitSrTeIpv6LspUp_Type()
)
vRtrMplsGenPceInitSrTeIpv6LspUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenPceInitSrTeIpv6LspUp.setStatus("current")
_VRtrMplsGenOnDemandSrTeLspOrig_Type = Gauge32
_VRtrMplsGenOnDemandSrTeLspOrig_Object = MibTableColumn
vRtrMplsGenOnDemandSrTeLspOrig = _VRtrMplsGenOnDemandSrTeLspOrig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 38),
    _VRtrMplsGenOnDemandSrTeLspOrig_Type()
)
vRtrMplsGenOnDemandSrTeLspOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenOnDemandSrTeLspOrig.setStatus("current")
_VRtrMplsGenOnDemandSrTeIpv4LspUp_Type = Gauge32
_VRtrMplsGenOnDemandSrTeIpv4LspUp_Object = MibTableColumn
vRtrMplsGenOnDemandSrTeIpv4LspUp = _VRtrMplsGenOnDemandSrTeIpv4LspUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 39),
    _VRtrMplsGenOnDemandSrTeIpv4LspUp_Type()
)
vRtrMplsGenOnDemandSrTeIpv4LspUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenOnDemandSrTeIpv4LspUp.setStatus("current")
_VRtrMplsGenOnDemandSrTeIpv6LspUp_Type = Gauge32
_VRtrMplsGenOnDemandSrTeIpv6LspUp_Object = MibTableColumn
vRtrMplsGenOnDemandSrTeIpv6LspUp = _VRtrMplsGenOnDemandSrTeIpv6LspUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 40),
    _VRtrMplsGenOnDemandSrTeIpv6LspUp_Type()
)
vRtrMplsGenOnDemandSrTeIpv6LspUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenOnDemandSrTeIpv6LspUp.setStatus("current")
_VRtrMplsIfTable_Object = MibTable
vRtrMplsIfTable = _VRtrMplsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9)
)
if mibBuilder.loadTexts:
    vRtrMplsIfTable.setStatus("current")
_VRtrMplsIfEntry_Object = MibTableRow
vRtrMplsIfEntry = _VRtrMplsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9, 1)
)
vRtrMplsIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsIfEntry.setStatus("current")


class _VRtrMplsIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsIfAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsIfAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsIfAdminState_Object = MibTableColumn
vRtrMplsIfAdminState = _VRtrMplsIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9, 1, 1),
    _VRtrMplsIfAdminState_Type()
)
vRtrMplsIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsIfAdminState.setStatus("current")
_VRtrMplsIfOperState_Type = TmnxOperState
_VRtrMplsIfOperState_Object = MibTableColumn
vRtrMplsIfOperState = _VRtrMplsIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9, 1, 2),
    _VRtrMplsIfOperState_Type()
)
vRtrMplsIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfOperState.setStatus("current")


class _VRtrMplsIfAdminGroup_Type(Unsigned32):
    """Custom type vRtrMplsIfAdminGroup based on Unsigned32"""
    defaultValue = 0


_VRtrMplsIfAdminGroup_Type.__name__ = "Unsigned32"
_VRtrMplsIfAdminGroup_Object = MibTableColumn
vRtrMplsIfAdminGroup = _VRtrMplsIfAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9, 1, 3),
    _VRtrMplsIfAdminGroup_Type()
)
vRtrMplsIfAdminGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsIfAdminGroup.setStatus("current")


class _VRtrMplsIfTeMetric_Type(Unsigned32):
    """Custom type vRtrMplsIfTeMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16777215),
    )


_VRtrMplsIfTeMetric_Type.__name__ = "Unsigned32"
_VRtrMplsIfTeMetric_Object = MibTableColumn
vRtrMplsIfTeMetric = _VRtrMplsIfTeMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9, 1, 4),
    _VRtrMplsIfTeMetric_Type()
)
vRtrMplsIfTeMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsIfTeMetric.setStatus("current")
_VRtrMplsIfV6OperState_Type = TmnxOperState
_VRtrMplsIfV6OperState_Object = MibTableColumn
vRtrMplsIfV6OperState = _VRtrMplsIfV6OperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9, 1, 5),
    _VRtrMplsIfV6OperState_Type()
)
vRtrMplsIfV6OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfV6OperState.setStatus("current")
_VRtrMplsIfStatTable_Object = MibTable
vRtrMplsIfStatTable = _VRtrMplsIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10)
)
if mibBuilder.loadTexts:
    vRtrMplsIfStatTable.setStatus("current")
_VRtrMplsIfStatEntry_Object = MibTableRow
vRtrMplsIfStatEntry = _VRtrMplsIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsIfStatEntry.setStatus("current")
_VRtrMplsIfTxPktCount_Type = Counter64
_VRtrMplsIfTxPktCount_Object = MibTableColumn
vRtrMplsIfTxPktCount = _VRtrMplsIfTxPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1, 1),
    _VRtrMplsIfTxPktCount_Type()
)
vRtrMplsIfTxPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfTxPktCount.setStatus("current")
_VRtrMplsIfRxPktCount_Type = Counter64
_VRtrMplsIfRxPktCount_Object = MibTableColumn
vRtrMplsIfRxPktCount = _VRtrMplsIfRxPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1, 2),
    _VRtrMplsIfRxPktCount_Type()
)
vRtrMplsIfRxPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfRxPktCount.setStatus("current")
_VRtrMplsIfTxOctetCount_Type = Counter64
_VRtrMplsIfTxOctetCount_Object = MibTableColumn
vRtrMplsIfTxOctetCount = _VRtrMplsIfTxOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1, 3),
    _VRtrMplsIfTxOctetCount_Type()
)
vRtrMplsIfTxOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfTxOctetCount.setStatus("current")
_VRtrMplsIfRxOctetCount_Type = Counter64
_VRtrMplsIfRxOctetCount_Object = MibTableColumn
vRtrMplsIfRxOctetCount = _VRtrMplsIfRxOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1, 4),
    _VRtrMplsIfRxOctetCount_Type()
)
vRtrMplsIfRxOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfRxOctetCount.setStatus("current")
_VRtrMplsIfAltTxPktCount_Type = Counter64
_VRtrMplsIfAltTxPktCount_Object = MibTableColumn
vRtrMplsIfAltTxPktCount = _VRtrMplsIfAltTxPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1, 5),
    _VRtrMplsIfAltTxPktCount_Type()
)
vRtrMplsIfAltTxPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfAltTxPktCount.setStatus("current")
_VRtrMplsIfAltRxPktCount_Type = Counter64
_VRtrMplsIfAltRxPktCount_Object = MibTableColumn
vRtrMplsIfAltRxPktCount = _VRtrMplsIfAltRxPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1, 6),
    _VRtrMplsIfAltRxPktCount_Type()
)
vRtrMplsIfAltRxPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfAltRxPktCount.setStatus("current")
_VRtrMplsIfAltTxOctetCount_Type = Counter64
_VRtrMplsIfAltTxOctetCount_Object = MibTableColumn
vRtrMplsIfAltTxOctetCount = _VRtrMplsIfAltTxOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1, 7),
    _VRtrMplsIfAltTxOctetCount_Type()
)
vRtrMplsIfAltTxOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfAltTxOctetCount.setStatus("current")
_VRtrMplsIfAltRxOctetCount_Type = Counter64
_VRtrMplsIfAltRxOctetCount_Object = MibTableColumn
vRtrMplsIfAltRxOctetCount = _VRtrMplsIfAltRxOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1, 8),
    _VRtrMplsIfAltRxOctetCount_Type()
)
vRtrMplsIfAltRxOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfAltRxOctetCount.setStatus("current")
_VRtrMplsTunnelARHopTable_Object = MibTable
vRtrMplsTunnelARHopTable = _VRtrMplsTunnelARHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11)
)
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopTable.setStatus("current")
_VRtrMplsTunnelARHopEntry_Object = MibTableRow
vRtrMplsTunnelARHopEntry = _VRtrMplsTunnelARHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopEntry.setStatus("current")


class _VRtrMplsTunnelARHopProtection_Type(Bits):
    """Custom type vRtrMplsTunnelARHopProtection based on Bits"""
    namedValues = NamedValues(
        *(("localAvailable", 0),
          ("localInUse", 1),
          ("bandwidthProtected", 2),
          ("nodeProtected", 3),
          ("preemptionPending", 4),
          ("nodeId", 5))
    )

_VRtrMplsTunnelARHopProtection_Type.__name__ = "Bits"
_VRtrMplsTunnelARHopProtection_Object = MibTableColumn
vRtrMplsTunnelARHopProtection = _VRtrMplsTunnelARHopProtection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11, 1, 1),
    _VRtrMplsTunnelARHopProtection_Type()
)
vRtrMplsTunnelARHopProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopProtection.setStatus("current")
_VRtrMplsTunnelARHopRecordLabel_Type = MplsLabel
_VRtrMplsTunnelARHopRecordLabel_Object = MibTableColumn
vRtrMplsTunnelARHopRecordLabel = _VRtrMplsTunnelARHopRecordLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11, 1, 2),
    _VRtrMplsTunnelARHopRecordLabel_Type()
)
vRtrMplsTunnelARHopRecordLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopRecordLabel.setStatus("current")
_VRtrMplsTunnelARHopRouterId_Type = IpAddress
_VRtrMplsTunnelARHopRouterId_Object = MibTableColumn
vRtrMplsTunnelARHopRouterId = _VRtrMplsTunnelARHopRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11, 1, 3),
    _VRtrMplsTunnelARHopRouterId_Type()
)
vRtrMplsTunnelARHopRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopRouterId.setStatus("obsolete")
_VRtrMplsTunnelARHopUnnumIfID_Type = Unsigned32
_VRtrMplsTunnelARHopUnnumIfID_Object = MibTableColumn
vRtrMplsTunnelARHopUnnumIfID = _VRtrMplsTunnelARHopUnnumIfID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11, 1, 4),
    _VRtrMplsTunnelARHopUnnumIfID_Type()
)
vRtrMplsTunnelARHopUnnumIfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopUnnumIfID.setStatus("current")


class _VRtrMplsTunnelARHopSIDType_Type(Integer32):
    """Custom type vRtrMplsTunnelARHopSIDType based on Integer32"""
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
          ("nodeSid", 2),
          ("adjacencySid", 3))
    )


_VRtrMplsTunnelARHopSIDType_Type.__name__ = "Integer32"
_VRtrMplsTunnelARHopSIDType_Object = MibTableColumn
vRtrMplsTunnelARHopSIDType = _VRtrMplsTunnelARHopSIDType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11, 1, 5),
    _VRtrMplsTunnelARHopSIDType_Type()
)
vRtrMplsTunnelARHopSIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopSIDType.setStatus("current")


class _VRtrMplsTunnelARHopNgRouterId_Type(InetAddress):
    """Custom type vRtrMplsTunnelARHopNgRouterId based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsTunnelARHopNgRouterId_Type.__name__ = "InetAddress"
_VRtrMplsTunnelARHopNgRouterId_Object = MibTableColumn
vRtrMplsTunnelARHopNgRouterId = _VRtrMplsTunnelARHopNgRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11, 1, 6),
    _VRtrMplsTunnelARHopNgRouterId_Type()
)
vRtrMplsTunnelARHopNgRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopNgRouterId.setStatus("current")
_VRtrMplsTunnelARHopNgRtrIdType_Type = InetAddressType
_VRtrMplsTunnelARHopNgRtrIdType_Object = MibTableColumn
vRtrMplsTunnelARHopNgRtrIdType = _VRtrMplsTunnelARHopNgRtrIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11, 1, 7),
    _VRtrMplsTunnelARHopNgRtrIdType_Type()
)
vRtrMplsTunnelARHopNgRtrIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopNgRtrIdType.setStatus("current")
_VRtrMplsTunnelCHopTable_Object = MibTable
vRtrMplsTunnelCHopTable = _VRtrMplsTunnelCHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12)
)
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopTable.setStatus("current")
_VRtrMplsTunnelCHopEntry_Object = MibTableRow
vRtrMplsTunnelCHopEntry = _VRtrMplsTunnelCHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1)
)
vRtrMplsTunnelCHopEntry.setIndexNames(
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopListIndex"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopEntry.setStatus("current")


class _VRtrMplsTunnelCHopListIndex_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsTunnelCHopListIndex_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopListIndex_Object = MibTableColumn
vRtrMplsTunnelCHopListIndex = _VRtrMplsTunnelCHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 1),
    _VRtrMplsTunnelCHopListIndex_Type()
)
vRtrMplsTunnelCHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopListIndex.setStatus("current")


class _VRtrMplsTunnelCHopIndex_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsTunnelCHopIndex_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopIndex_Object = MibTableColumn
vRtrMplsTunnelCHopIndex = _VRtrMplsTunnelCHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 2),
    _VRtrMplsTunnelCHopIndex_Type()
)
vRtrMplsTunnelCHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopIndex.setStatus("current")


class _VRtrMplsTunnelCHopAddrType_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopAddrType based on Integer32"""
    defaultValue = 1

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
        *(("unknown", 0),
          ("ipV4", 1),
          ("ipV6", 2),
          ("asNumber", 3),
          ("lspid", 4),
          ("unnum", 5))
    )


_VRtrMplsTunnelCHopAddrType_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopAddrType_Object = MibTableColumn
vRtrMplsTunnelCHopAddrType = _VRtrMplsTunnelCHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 3),
    _VRtrMplsTunnelCHopAddrType_Type()
)
vRtrMplsTunnelCHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopAddrType.setStatus("current")
_VRtrMplsTunnelCHopIpv4Addr_Type = IpAddress
_VRtrMplsTunnelCHopIpv4Addr_Object = MibTableColumn
vRtrMplsTunnelCHopIpv4Addr = _VRtrMplsTunnelCHopIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 4),
    _VRtrMplsTunnelCHopIpv4Addr_Type()
)
vRtrMplsTunnelCHopIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopIpv4Addr.setStatus("current")


class _VRtrMplsTunnelCHopIpv4PrefixLen_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopIpv4PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VRtrMplsTunnelCHopIpv4PrefixLen_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopIpv4PrefixLen_Object = MibTableColumn
vRtrMplsTunnelCHopIpv4PrefixLen = _VRtrMplsTunnelCHopIpv4PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 5),
    _VRtrMplsTunnelCHopIpv4PrefixLen_Type()
)
vRtrMplsTunnelCHopIpv4PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopIpv4PrefixLen.setStatus("current")
_VRtrMplsTunnelCHopIpv6Addr_Type = InetAddressIPv6
_VRtrMplsTunnelCHopIpv6Addr_Object = MibTableColumn
vRtrMplsTunnelCHopIpv6Addr = _VRtrMplsTunnelCHopIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 6),
    _VRtrMplsTunnelCHopIpv6Addr_Type()
)
vRtrMplsTunnelCHopIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopIpv6Addr.setStatus("current")


class _VRtrMplsTunnelCHopIpv6PrefixLen_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopIpv6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_VRtrMplsTunnelCHopIpv6PrefixLen_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopIpv6PrefixLen_Object = MibTableColumn
vRtrMplsTunnelCHopIpv6PrefixLen = _VRtrMplsTunnelCHopIpv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 7),
    _VRtrMplsTunnelCHopIpv6PrefixLen_Type()
)
vRtrMplsTunnelCHopIpv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopIpv6PrefixLen.setStatus("current")


class _VRtrMplsTunnelCHopAsNumber_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopAsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrMplsTunnelCHopAsNumber_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopAsNumber_Object = MibTableColumn
vRtrMplsTunnelCHopAsNumber = _VRtrMplsTunnelCHopAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 8),
    _VRtrMplsTunnelCHopAsNumber_Type()
)
vRtrMplsTunnelCHopAsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopAsNumber.setStatus("current")
_VRtrMplsTunnelCHopLspId_Type = MplsLSPID
_VRtrMplsTunnelCHopLspId_Object = MibTableColumn
vRtrMplsTunnelCHopLspId = _VRtrMplsTunnelCHopLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 9),
    _VRtrMplsTunnelCHopLspId_Type()
)
vRtrMplsTunnelCHopLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopLspId.setStatus("current")


class _VRtrMplsTunnelCHopStrictOrLoose_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopStrictOrLoose based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("loose", 2))
    )


_VRtrMplsTunnelCHopStrictOrLoose_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopStrictOrLoose_Object = MibTableColumn
vRtrMplsTunnelCHopStrictOrLoose = _VRtrMplsTunnelCHopStrictOrLoose_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 10),
    _VRtrMplsTunnelCHopStrictOrLoose_Type()
)
vRtrMplsTunnelCHopStrictOrLoose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopStrictOrLoose.setStatus("current")
_VRtrMplsTunnelCHopEgressAdmGrp_Type = Unsigned32
_VRtrMplsTunnelCHopEgressAdmGrp_Object = MibTableColumn
vRtrMplsTunnelCHopEgressAdmGrp = _VRtrMplsTunnelCHopEgressAdmGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 11),
    _VRtrMplsTunnelCHopEgressAdmGrp_Type()
)
vRtrMplsTunnelCHopEgressAdmGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopEgressAdmGrp.setStatus("current")
_VRtrMplsTunnelCHopUnnumIfID_Type = Unsigned32
_VRtrMplsTunnelCHopUnnumIfID_Object = MibTableColumn
vRtrMplsTunnelCHopUnnumIfID = _VRtrMplsTunnelCHopUnnumIfID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 12),
    _VRtrMplsTunnelCHopUnnumIfID_Type()
)
vRtrMplsTunnelCHopUnnumIfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopUnnumIfID.setStatus("current")
_VRtrMplsTunnelCHopRtrID_Type = IpAddress
_VRtrMplsTunnelCHopRtrID_Object = MibTableColumn
vRtrMplsTunnelCHopRtrID = _VRtrMplsTunnelCHopRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 13),
    _VRtrMplsTunnelCHopRtrID_Type()
)
vRtrMplsTunnelCHopRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopRtrID.setStatus("current")
_VRtrMplsTunnelCHopIsABR_Type = TruthValue
_VRtrMplsTunnelCHopIsABR_Object = MibTableColumn
vRtrMplsTunnelCHopIsABR = _VRtrMplsTunnelCHopIsABR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 14),
    _VRtrMplsTunnelCHopIsABR_Type()
)
vRtrMplsTunnelCHopIsABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopIsABR.setStatus("current")
_VRtrMplsAdminGroupTable_Object = MibTable
vRtrMplsAdminGroupTable = _VRtrMplsAdminGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 13)
)
if mibBuilder.loadTexts:
    vRtrMplsAdminGroupTable.setStatus("obsolete")
_VRtrMplsAdminGroupEntry_Object = MibTableRow
vRtrMplsAdminGroupEntry = _VRtrMplsAdminGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 13, 1)
)
vRtrMplsAdminGroupEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-MPLS-MIB", "vRtrMplsAdminGroupName"),
)
if mibBuilder.loadTexts:
    vRtrMplsAdminGroupEntry.setStatus("obsolete")
_VRtrMplsAdminGroupName_Type = TNamedItem
_VRtrMplsAdminGroupName_Object = MibTableColumn
vRtrMplsAdminGroupName = _VRtrMplsAdminGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 13, 1, 1),
    _VRtrMplsAdminGroupName_Type()
)
vRtrMplsAdminGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsAdminGroupName.setStatus("obsolete")
_VRtrMplsAdminGroupRowStatus_Type = RowStatus
_VRtrMplsAdminGroupRowStatus_Object = MibTableColumn
vRtrMplsAdminGroupRowStatus = _VRtrMplsAdminGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 13, 1, 2),
    _VRtrMplsAdminGroupRowStatus_Type()
)
vRtrMplsAdminGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsAdminGroupRowStatus.setStatus("obsolete")


class _VRtrMplsAdminGroupValue_Type(Integer32):
    """Custom type vRtrMplsAdminGroupValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31),
    )


_VRtrMplsAdminGroupValue_Type.__name__ = "Integer32"
_VRtrMplsAdminGroupValue_Object = MibTableColumn
vRtrMplsAdminGroupValue = _VRtrMplsAdminGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 13, 1, 3),
    _VRtrMplsAdminGroupValue_Type()
)
vRtrMplsAdminGroupValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsAdminGroupValue.setStatus("obsolete")
_VRtrMplsFSGroupTable_Object = MibTable
vRtrMplsFSGroupTable = _VRtrMplsFSGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 14)
)
if mibBuilder.loadTexts:
    vRtrMplsFSGroupTable.setStatus("obsolete")
_VRtrMplsFSGroupEntry_Object = MibTableRow
vRtrMplsFSGroupEntry = _VRtrMplsFSGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 14, 1)
)
vRtrMplsFSGroupEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsFSGroupName"),
)
if mibBuilder.loadTexts:
    vRtrMplsFSGroupEntry.setStatus("obsolete")
_VRtrMplsFSGroupName_Type = TNamedItem
_VRtrMplsFSGroupName_Object = MibTableColumn
vRtrMplsFSGroupName = _VRtrMplsFSGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 14, 1, 1),
    _VRtrMplsFSGroupName_Type()
)
vRtrMplsFSGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsFSGroupName.setStatus("obsolete")
_VRtrMplsFSGroupRowStatus_Type = RowStatus
_VRtrMplsFSGroupRowStatus_Object = MibTableColumn
vRtrMplsFSGroupRowStatus = _VRtrMplsFSGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 14, 1, 2),
    _VRtrMplsFSGroupRowStatus_Type()
)
vRtrMplsFSGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFSGroupRowStatus.setStatus("obsolete")


class _VRtrMplsFSGroupCost_Type(Unsigned32):
    """Custom type vRtrMplsFSGroupCost based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrMplsFSGroupCost_Type.__name__ = "Unsigned32"
_VRtrMplsFSGroupCost_Object = MibTableColumn
vRtrMplsFSGroupCost = _VRtrMplsFSGroupCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 14, 1, 3),
    _VRtrMplsFSGroupCost_Type()
)
vRtrMplsFSGroupCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFSGroupCost.setStatus("obsolete")
_VRtrMplsFSGroupParamsTable_Object = MibTable
vRtrMplsFSGroupParamsTable = _VRtrMplsFSGroupParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 15)
)
if mibBuilder.loadTexts:
    vRtrMplsFSGroupParamsTable.setStatus("obsolete")
_VRtrMplsFSGroupParamsEntry_Object = MibTableRow
vRtrMplsFSGroupParamsEntry = _VRtrMplsFSGroupParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 15, 1)
)
vRtrMplsFSGroupParamsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsFSGroupName"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsFSGroupParamsFromAddr"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsFSGroupParamsToAddr"),
)
if mibBuilder.loadTexts:
    vRtrMplsFSGroupParamsEntry.setStatus("obsolete")
_VRtrMplsFSGroupParamsFromAddr_Type = IpAddress
_VRtrMplsFSGroupParamsFromAddr_Object = MibTableColumn
vRtrMplsFSGroupParamsFromAddr = _VRtrMplsFSGroupParamsFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 15, 1, 1),
    _VRtrMplsFSGroupParamsFromAddr_Type()
)
vRtrMplsFSGroupParamsFromAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsFSGroupParamsFromAddr.setStatus("obsolete")
_VRtrMplsFSGroupParamsToAddr_Type = IpAddress
_VRtrMplsFSGroupParamsToAddr_Object = MibTableColumn
vRtrMplsFSGroupParamsToAddr = _VRtrMplsFSGroupParamsToAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 15, 1, 2),
    _VRtrMplsFSGroupParamsToAddr_Type()
)
vRtrMplsFSGroupParamsToAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsFSGroupParamsToAddr.setStatus("obsolete")
_VRtrMplsFSGroupParamsRowStatus_Type = RowStatus
_VRtrMplsFSGroupParamsRowStatus_Object = MibTableColumn
vRtrMplsFSGroupParamsRowStatus = _VRtrMplsFSGroupParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 15, 1, 3),
    _VRtrMplsFSGroupParamsRowStatus_Type()
)
vRtrMplsFSGroupParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFSGroupParamsRowStatus.setStatus("obsolete")
_TmnxMplsNotificationObjects_ObjectIdentity = ObjectIdentity
tmnxMplsNotificationObjects = _TmnxMplsNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16)
)


class _VRtrMplsLspNotificationReasonCode_Type(Integer32):
    """Custom type vRtrMplsLspNotificationReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("noPathIsOperational", 1))
    )


_VRtrMplsLspNotificationReasonCode_Type.__name__ = "Integer32"
_VRtrMplsLspNotificationReasonCode_Object = MibScalar
vRtrMplsLspNotificationReasonCode = _VRtrMplsLspNotificationReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 1),
    _VRtrMplsLspNotificationReasonCode_Type()
)
vRtrMplsLspNotificationReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspNotificationReasonCode.setStatus("current")
_VRtrMplsLspPathNotificationReasonCode_Type = TmnxMplsLspFailCode
_VRtrMplsLspPathNotificationReasonCode_Object = MibScalar
vRtrMplsLspPathNotificationReasonCode = _VRtrMplsLspPathNotificationReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 2),
    _VRtrMplsLspPathNotificationReasonCode_Type()
)
vRtrMplsLspPathNotificationReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspPathNotificationReasonCode.setStatus("current")
_VRtrMplsNotifyRow_Type = RowPointer
_VRtrMplsNotifyRow_Object = MibScalar
vRtrMplsNotifyRow = _VRtrMplsNotifyRow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 3),
    _VRtrMplsNotifyRow_Type()
)
vRtrMplsNotifyRow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsNotifyRow.setStatus("current")
_VRtrMplsP2mpInstNotifIndex_Type = TmnxVRtrMplsLspID
_VRtrMplsP2mpInstNotifIndex_Object = MibScalar
vRtrMplsP2mpInstNotifIndex = _VRtrMplsP2mpInstNotifIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 4),
    _VRtrMplsP2mpInstNotifIndex_Type()
)
vRtrMplsP2mpInstNotifIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstNotifIndex.setStatus("current")
_VRtrMplsP2mpInstNotifReasonCode_Type = TmnxMplsP2mpInstFailCode
_VRtrMplsP2mpInstNotifReasonCode_Object = MibScalar
vRtrMplsP2mpInstNotifReasonCode = _VRtrMplsP2mpInstNotifReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 5),
    _VRtrMplsP2mpInstNotifReasonCode_Type()
)
vRtrMplsP2mpInstNotifReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstNotifReasonCode.setStatus("current")
_VRtrMplsS2lSubLspNtDstAddrType_Type = InetAddressType
_VRtrMplsS2lSubLspNtDstAddrType_Object = MibScalar
vRtrMplsS2lSubLspNtDstAddrType = _VRtrMplsS2lSubLspNtDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 6),
    _VRtrMplsS2lSubLspNtDstAddrType_Type()
)
vRtrMplsS2lSubLspNtDstAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspNtDstAddrType.setStatus("current")


class _VRtrMplsS2lSubLspNtDstAddr_Type(InetAddress):
    """Custom type vRtrMplsS2lSubLspNtDstAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsS2lSubLspNtDstAddr_Type.__name__ = "InetAddress"
_VRtrMplsS2lSubLspNtDstAddr_Object = MibScalar
vRtrMplsS2lSubLspNtDstAddr = _VRtrMplsS2lSubLspNtDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 7),
    _VRtrMplsS2lSubLspNtDstAddr_Type()
)
vRtrMplsS2lSubLspNtDstAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspNtDstAddr.setStatus("current")
_VRtrMplsLspPathCongChgPercent_Type = Unsigned32
_VRtrMplsLspPathCongChgPercent_Object = MibScalar
vRtrMplsLspPathCongChgPercent = _VRtrMplsLspPathCongChgPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 8),
    _VRtrMplsLspPathCongChgPercent_Type()
)
vRtrMplsLspPathCongChgPercent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspPathCongChgPercent.setStatus("current")


class _VRtrMplsLspPathMbbStatus_Type(Integer32):
    """Custom type vRtrMplsLspPathMbbStatus based on Integer32"""
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
        *(("successful", 0),
          ("failed", 1),
          ("aborted", 2),
          ("ignored", 3))
    )


_VRtrMplsLspPathMbbStatus_Type.__name__ = "Integer32"
_VRtrMplsLspPathMbbStatus_Object = MibScalar
vRtrMplsLspPathMbbStatus = _VRtrMplsLspPathMbbStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 9),
    _VRtrMplsLspPathMbbStatus_Type()
)
vRtrMplsLspPathMbbStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMbbStatus.setStatus("current")


class _VRtrMplsLspPathMbbReasonCode_Type(Integer32):
    """Custom type vRtrMplsLspPathMbbReasonCode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("mbbRetryExceeded", 1),
          ("lspPathGoingDown", 2),
          ("startingHighPriMbb", 3),
          ("restartingMbb", 4),
          ("mbbAlreadyInProg", 5),
          ("lspPceControlled", 6),
          ("lspNotPceControlled", 7),
          ("lspTypeNotSupported", 8))
    )


_VRtrMplsLspPathMbbReasonCode_Type.__name__ = "Integer32"
_VRtrMplsLspPathMbbReasonCode_Object = MibScalar
vRtrMplsLspPathMbbReasonCode = _VRtrMplsLspPathMbbReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 10),
    _VRtrMplsLspPathMbbReasonCode_Type()
)
vRtrMplsLspPathMbbReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMbbReasonCode.setStatus("current")


class _VRtrMplsLspSwitchStbyReasonCode_Type(Integer32):
    """Custom type vRtrMplsLspSwitchStbyReasonCode based on Integer32"""
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
        *(("none", 0),
          ("lspIsDown", 1),
          ("lspIsNotDynamic", 2),
          ("lspHasNoActivePath", 3),
          ("lspActivePathIsNotStandby", 4),
          ("pathSpecifiedIsNotLspPath", 5),
          ("pathSpecifiedIsNotStandby", 6),
          ("pathSpecifiedIsDown", 7),
          ("pathHasDiffPrefThanActLspPath", 8),
          ("lspHoldTimerIsRunning", 9),
          ("currentLspPathActiveByForce", 10),
          ("lspPathInPreemption", 11),
          ("lspActivePathIsPrimary", 12),
          ("currentActivePathIsBest", 13),
          ("betterPathFound", 14),
          ("currentActivePathWentDown", 15),
          ("lspPathIsDegraded", 16),
          ("lspAlreadyManuallySwitched", 17))
    )


_VRtrMplsLspSwitchStbyReasonCode_Type.__name__ = "Integer32"
_VRtrMplsLspSwitchStbyReasonCode_Object = MibScalar
vRtrMplsLspSwitchStbyReasonCode = _VRtrMplsLspSwitchStbyReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 13),
    _VRtrMplsLspSwitchStbyReasonCode_Type()
)
vRtrMplsLspSwitchStbyReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspSwitchStbyReasonCode.setStatus("current")
_VRtrMplsLspOldTunnelIndex_Type = MplsTunnelIndex
_VRtrMplsLspOldTunnelIndex_Object = MibScalar
vRtrMplsLspOldTunnelIndex = _VRtrMplsLspOldTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 14),
    _VRtrMplsLspOldTunnelIndex_Type()
)
vRtrMplsLspOldTunnelIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspOldTunnelIndex.setStatus("current")


class _VRtrMplsXCNotifRednIndicesBitMap_Type(OctetString):
    """Custom type vRtrMplsXCNotifRednIndicesBitMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1000),
    )


_VRtrMplsXCNotifRednIndicesBitMap_Type.__name__ = "OctetString"
_VRtrMplsXCNotifRednIndicesBitMap_Object = MibScalar
vRtrMplsXCNotifRednIndicesBitMap = _VRtrMplsXCNotifRednIndicesBitMap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 15),
    _VRtrMplsXCNotifRednIndicesBitMap_Type()
)
vRtrMplsXCNotifRednIndicesBitMap.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsXCNotifRednIndicesBitMap.setStatus("current")


class _VRtrMplsXCNotifyRednBundlingType_Type(Integer32):
    """Custom type vRtrMplsXCNotifyRednBundlingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("create", 2))
    )


_VRtrMplsXCNotifyRednBundlingType_Type.__name__ = "Integer32"
_VRtrMplsXCNotifyRednBundlingType_Object = MibScalar
vRtrMplsXCNotifyRednBundlingType = _VRtrMplsXCNotifyRednBundlingType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 16),
    _VRtrMplsXCNotifyRednBundlingType_Type()
)
vRtrMplsXCNotifyRednBundlingType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsXCNotifyRednBundlingType.setStatus("current")
_VRtrMplsXCNotifyRednNumOfBitsSet_Type = Unsigned32
_VRtrMplsXCNotifyRednNumOfBitsSet_Object = MibScalar
vRtrMplsXCNotifyRednNumOfBitsSet = _VRtrMplsXCNotifyRednNumOfBitsSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 17),
    _VRtrMplsXCNotifyRednNumOfBitsSet_Type()
)
vRtrMplsXCNotifyRednNumOfBitsSet.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsXCNotifyRednNumOfBitsSet.setStatus("current")
_VRtrMplsXCNotifyRednStartIndex_Type = Unsigned32
_VRtrMplsXCNotifyRednStartIndex_Object = MibScalar
vRtrMplsXCNotifyRednStartIndex = _VRtrMplsXCNotifyRednStartIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 18),
    _VRtrMplsXCNotifyRednStartIndex_Type()
)
vRtrMplsXCNotifyRednStartIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsXCNotifyRednStartIndex.setStatus("current")
_VRtrMplsXCNotifyRednEndIndex_Type = Unsigned32
_VRtrMplsXCNotifyRednEndIndex_Object = MibScalar
vRtrMplsXCNotifyRednEndIndex = _VRtrMplsXCNotifyRednEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 19),
    _VRtrMplsXCNotifyRednEndIndex_Type()
)
vRtrMplsXCNotifyRednEndIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsXCNotifyRednEndIndex.setStatus("current")
_VRtrMplsIgpOverloadRtrAddrType_Type = InetAddressType
_VRtrMplsIgpOverloadRtrAddrType_Object = MibScalar
vRtrMplsIgpOverloadRtrAddrType = _VRtrMplsIgpOverloadRtrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 20),
    _VRtrMplsIgpOverloadRtrAddrType_Type()
)
vRtrMplsIgpOverloadRtrAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsIgpOverloadRtrAddrType.setStatus("current")


class _VRtrMplsIgpOverloadRtrAddr_Type(InetAddress):
    """Custom type vRtrMplsIgpOverloadRtrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsIgpOverloadRtrAddr_Type.__name__ = "InetAddress"
_VRtrMplsIgpOverloadRtrAddr_Object = MibScalar
vRtrMplsIgpOverloadRtrAddr = _VRtrMplsIgpOverloadRtrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 21),
    _VRtrMplsIgpOverloadRtrAddr_Type()
)
vRtrMplsIgpOverloadRtrAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsIgpOverloadRtrAddr.setStatus("current")


class _VRtrMplsIgpOverloadIgpType_Type(Integer32):
    """Custom type vRtrMplsIgpOverloadIgpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isis", 1),
          ("ospf", 2))
    )


_VRtrMplsIgpOverloadIgpType_Type.__name__ = "Integer32"
_VRtrMplsIgpOverloadIgpType_Object = MibScalar
vRtrMplsIgpOverloadIgpType = _VRtrMplsIgpOverloadIgpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 22),
    _VRtrMplsIgpOverloadIgpType_Type()
)
vRtrMplsIgpOverloadIgpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsIgpOverloadIgpType.setStatus("current")


class _VRtrMplsResourceType_Type(Integer32):
    """Custom type vRtrMplsResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("egressStatistics", 1)
    )


_VRtrMplsResourceType_Type.__name__ = "Integer32"
_VRtrMplsResourceType_Object = MibScalar
vRtrMplsResourceType = _VRtrMplsResourceType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 23),
    _VRtrMplsResourceType_Type()
)
vRtrMplsResourceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsResourceType.setStatus("current")


class _VRtrMplsLspManualSwFailReason_Type(Integer32):
    """Custom type vRtrMplsLspManualSwFailReason based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("lspIsDown", 1),
          ("lspActivePathChanged", 2),
          ("lspRevertOrHoldTimerIsRunning", 3),
          ("lspIsAlreadyManuallySwitched", 4),
          ("lspIsNotManuallySwitched", 5),
          ("lspHasInsufficientPaths", 6),
          ("lspActivePathIsSecondary", 7),
          ("lspActivePathIsActiveByForce", 8))
    )


_VRtrMplsLspManualSwFailReason_Type.__name__ = "Integer32"
_VRtrMplsLspManualSwFailReason_Object = MibScalar
vRtrMplsLspManualSwFailReason = _VRtrMplsLspManualSwFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 24),
    _VRtrMplsLspManualSwFailReason_Type()
)
vRtrMplsLspManualSwFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspManualSwFailReason.setStatus("current")
_VRtrMplsLspPathManDegState_Type = TruthValue
_VRtrMplsLspPathManDegState_Object = MibScalar
vRtrMplsLspPathManDegState = _VRtrMplsLspPathManDegState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 25),
    _VRtrMplsLspPathManDegState_Type()
)
vRtrMplsLspPathManDegState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspPathManDegState.setStatus("current")
_VRtrMplsLabelRangeTable_Object = MibTable
vRtrMplsLabelRangeTable = _VRtrMplsLabelRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17)
)
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeTable.setStatus("current")
_VRtrMplsLabelRangeEntry_Object = MibTableRow
vRtrMplsLabelRangeEntry = _VRtrMplsLabelRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17, 1)
)
vRtrMplsLabelRangeEntry.setIndexNames(
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLabelType"),
)
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeEntry.setStatus("current")


class _VRtrMplsLabelType_Type(Integer32):
    """Custom type vRtrMplsLabelType based on Integer32"""
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
        *(("staticLsp", 1),
          ("staticSvc", 2),
          ("dynamic", 3),
          ("segmentRoute", 4),
          ("static", 5))
    )


_VRtrMplsLabelType_Type.__name__ = "Integer32"
_VRtrMplsLabelType_Object = MibTableColumn
vRtrMplsLabelType = _VRtrMplsLabelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17, 1, 1),
    _VRtrMplsLabelType_Type()
)
vRtrMplsLabelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLabelType.setStatus("current")
_VRtrMplsLabelRangeMin_Type = Unsigned32
_VRtrMplsLabelRangeMin_Object = MibTableColumn
vRtrMplsLabelRangeMin = _VRtrMplsLabelRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17, 1, 2),
    _VRtrMplsLabelRangeMin_Type()
)
vRtrMplsLabelRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeMin.setStatus("current")
_VRtrMplsLabelRangeMax_Type = Unsigned32
_VRtrMplsLabelRangeMax_Object = MibTableColumn
vRtrMplsLabelRangeMax = _VRtrMplsLabelRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17, 1, 3),
    _VRtrMplsLabelRangeMax_Type()
)
vRtrMplsLabelRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeMax.setStatus("current")
_VRtrMplsLabelRangeAging_Type = Unsigned32
_VRtrMplsLabelRangeAging_Object = MibTableColumn
vRtrMplsLabelRangeAging = _VRtrMplsLabelRangeAging_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17, 1, 4),
    _VRtrMplsLabelRangeAging_Type()
)
vRtrMplsLabelRangeAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeAging.setStatus("current")
_VRtrMplsLabelRangeAvailable_Type = Unsigned32
_VRtrMplsLabelRangeAvailable_Object = MibTableColumn
vRtrMplsLabelRangeAvailable = _VRtrMplsLabelRangeAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17, 1, 5),
    _VRtrMplsLabelRangeAvailable_Type()
)
vRtrMplsLabelRangeAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeAvailable.setStatus("current")
_VRtrMplsStaticLSPLabelTable_Object = MibTable
vRtrMplsStaticLSPLabelTable = _VRtrMplsStaticLSPLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 18)
)
if mibBuilder.loadTexts:
    vRtrMplsStaticLSPLabelTable.setStatus("current")
_VRtrMplsStaticLSPLabelEntry_Object = MibTableRow
vRtrMplsStaticLSPLabelEntry = _VRtrMplsStaticLSPLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 18, 1)
)
vRtrMplsStaticLSPLabelEntry.setIndexNames(
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsStaticLSPLabel"),
)
if mibBuilder.loadTexts:
    vRtrMplsStaticLSPLabelEntry.setStatus("current")


class _VRtrMplsStaticLSPLabel_Type(MplsLabel):
    """Custom type vRtrMplsStaticLSPLabel based on MplsLabel"""
    subtypeSpec = MplsLabel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 262112),
    )


_VRtrMplsStaticLSPLabel_Type.__name__ = "MplsLabel"
_VRtrMplsStaticLSPLabel_Object = MibTableColumn
vRtrMplsStaticLSPLabel = _VRtrMplsStaticLSPLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 18, 1, 1),
    _VRtrMplsStaticLSPLabel_Type()
)
vRtrMplsStaticLSPLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsStaticLSPLabel.setStatus("current")
_VRtrMplsStaticLSPLabelOwner_Type = TmnxMplsLabelOwner
_VRtrMplsStaticLSPLabelOwner_Object = MibTableColumn
vRtrMplsStaticLSPLabelOwner = _VRtrMplsStaticLSPLabelOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 18, 1, 2),
    _VRtrMplsStaticLSPLabelOwner_Type()
)
vRtrMplsStaticLSPLabelOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsStaticLSPLabelOwner.setStatus("current")
_VRtrMplsStaticSvcLabelTable_Object = MibTable
vRtrMplsStaticSvcLabelTable = _VRtrMplsStaticSvcLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 19)
)
if mibBuilder.loadTexts:
    vRtrMplsStaticSvcLabelTable.setStatus("current")
_VRtrMplsStaticSvcLabelEntry_Object = MibTableRow
vRtrMplsStaticSvcLabelEntry = _VRtrMplsStaticSvcLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 19, 1)
)
vRtrMplsStaticSvcLabelEntry.setIndexNames(
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsStaticSvcLabel"),
)
if mibBuilder.loadTexts:
    vRtrMplsStaticSvcLabelEntry.setStatus("current")


class _VRtrMplsStaticSvcLabel_Type(MplsLabel):
    """Custom type vRtrMplsStaticSvcLabel based on MplsLabel"""
    subtypeSpec = MplsLabel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 262112),
    )


_VRtrMplsStaticSvcLabel_Type.__name__ = "MplsLabel"
_VRtrMplsStaticSvcLabel_Object = MibTableColumn
vRtrMplsStaticSvcLabel = _VRtrMplsStaticSvcLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 19, 1, 1),
    _VRtrMplsStaticSvcLabel_Type()
)
vRtrMplsStaticSvcLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsStaticSvcLabel.setStatus("current")


class _VRtrMplsStaticSvcLabelOwner_Type(TmnxMplsLabelOwner):
    """Custom type vRtrMplsStaticSvcLabelOwner based on TmnxMplsLabelOwner"""
    defaultValue = 0


_VRtrMplsStaticSvcLabelOwner_Type.__name__ = "TmnxMplsLabelOwner"
_VRtrMplsStaticSvcLabelOwner_Object = MibTableColumn
vRtrMplsStaticSvcLabelOwner = _VRtrMplsStaticSvcLabelOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 19, 1, 2),
    _VRtrMplsStaticSvcLabelOwner_Type()
)
vRtrMplsStaticSvcLabelOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsStaticSvcLabelOwner.setStatus("current")
_VRtrMplsSrlgGrpTableLastChanged_Type = TimeStamp
_VRtrMplsSrlgGrpTableLastChanged_Object = MibScalar
vRtrMplsSrlgGrpTableLastChanged = _VRtrMplsSrlgGrpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 20),
    _VRtrMplsSrlgGrpTableLastChanged_Type()
)
vRtrMplsSrlgGrpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpTableLastChanged.setStatus("obsolete")
_VRtrMplsSrlgGrpTable_Object = MibTable
vRtrMplsSrlgGrpTable = _VRtrMplsSrlgGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 21)
)
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpTable.setStatus("obsolete")
_VRtrMplsSrlgGrpEntry_Object = MibTableRow
vRtrMplsSrlgGrpEntry = _VRtrMplsSrlgGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 21, 1)
)
vRtrMplsSrlgGrpEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpName"),
)
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpEntry.setStatus("obsolete")
_VRtrMplsSrlgGrpName_Type = TNamedItem
_VRtrMplsSrlgGrpName_Object = MibTableColumn
vRtrMplsSrlgGrpName = _VRtrMplsSrlgGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 21, 1, 1),
    _VRtrMplsSrlgGrpName_Type()
)
vRtrMplsSrlgGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpName.setStatus("obsolete")
_VRtrMplsSrlgGrpRowStatus_Type = RowStatus
_VRtrMplsSrlgGrpRowStatus_Object = MibTableColumn
vRtrMplsSrlgGrpRowStatus = _VRtrMplsSrlgGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 21, 1, 2),
    _VRtrMplsSrlgGrpRowStatus_Type()
)
vRtrMplsSrlgGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpRowStatus.setStatus("obsolete")
_VRtrMplsSrlgGrpLastChanged_Type = TimeStamp
_VRtrMplsSrlgGrpLastChanged_Object = MibTableColumn
vRtrMplsSrlgGrpLastChanged = _VRtrMplsSrlgGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 21, 1, 3),
    _VRtrMplsSrlgGrpLastChanged_Type()
)
vRtrMplsSrlgGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpLastChanged.setStatus("obsolete")
_VRtrMplsSrlgGrpValue_Type = Unsigned32
_VRtrMplsSrlgGrpValue_Object = MibTableColumn
vRtrMplsSrlgGrpValue = _VRtrMplsSrlgGrpValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 21, 1, 4),
    _VRtrMplsSrlgGrpValue_Type()
)
vRtrMplsSrlgGrpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpValue.setStatus("obsolete")
_VRtrMplsIfSrlgGrpTblLastChanged_Type = TimeStamp
_VRtrMplsIfSrlgGrpTblLastChanged_Object = MibScalar
vRtrMplsIfSrlgGrpTblLastChanged = _VRtrMplsIfSrlgGrpTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 22),
    _VRtrMplsIfSrlgGrpTblLastChanged_Type()
)
vRtrMplsIfSrlgGrpTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfSrlgGrpTblLastChanged.setStatus("current")
_VRtrMplsIfSrlgGrpTable_Object = MibTable
vRtrMplsIfSrlgGrpTable = _VRtrMplsIfSrlgGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 23)
)
if mibBuilder.loadTexts:
    vRtrMplsIfSrlgGrpTable.setStatus("current")
_VRtrMplsIfSrlgGrpEntry_Object = MibTableRow
vRtrMplsIfSrlgGrpEntry = _VRtrMplsIfSrlgGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 23, 1)
)
vRtrMplsIfSrlgGrpEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (1, "TIMETRA-MPLS-MIB", "vRtrMplsIfSrlgGrpName"),
)
if mibBuilder.loadTexts:
    vRtrMplsIfSrlgGrpEntry.setStatus("current")
_VRtrMplsIfSrlgGrpName_Type = TNamedItem
_VRtrMplsIfSrlgGrpName_Object = MibTableColumn
vRtrMplsIfSrlgGrpName = _VRtrMplsIfSrlgGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 23, 1, 1),
    _VRtrMplsIfSrlgGrpName_Type()
)
vRtrMplsIfSrlgGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsIfSrlgGrpName.setStatus("current")
_VRtrMplsIfSrlgGrpRowStatus_Type = RowStatus
_VRtrMplsIfSrlgGrpRowStatus_Object = MibTableColumn
vRtrMplsIfSrlgGrpRowStatus = _VRtrMplsIfSrlgGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 23, 1, 2),
    _VRtrMplsIfSrlgGrpRowStatus_Type()
)
vRtrMplsIfSrlgGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsIfSrlgGrpRowStatus.setStatus("current")
_VRtrMplsIfSrlgGrpLastChanged_Type = TimeStamp
_VRtrMplsIfSrlgGrpLastChanged_Object = MibTableColumn
vRtrMplsIfSrlgGrpLastChanged = _VRtrMplsIfSrlgGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 23, 1, 3),
    _VRtrMplsIfSrlgGrpLastChanged_Type()
)
vRtrMplsIfSrlgGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfSrlgGrpLastChanged.setStatus("current")
_VRtrMplsP2mpInstTblLastChanged_Type = TimeStamp
_VRtrMplsP2mpInstTblLastChanged_Object = MibScalar
vRtrMplsP2mpInstTblLastChanged = _VRtrMplsP2mpInstTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 24),
    _VRtrMplsP2mpInstTblLastChanged_Type()
)
vRtrMplsP2mpInstTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstTblLastChanged.setStatus("current")
_VRtrMplsP2mpInstTable_Object = MibTable
vRtrMplsP2mpInstTable = _VRtrMplsP2mpInstTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25)
)
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstTable.setStatus("current")
_VRtrMplsP2mpInstEntry_Object = MibTableRow
vRtrMplsP2mpInstEntry = _VRtrMplsP2mpInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1)
)
vRtrMplsP2mpInstEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstEntry.setStatus("current")
_VRtrMplsP2mpInstIndex_Type = TmnxVRtrMplsLspID
_VRtrMplsP2mpInstIndex_Object = MibTableColumn
vRtrMplsP2mpInstIndex = _VRtrMplsP2mpInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 1),
    _VRtrMplsP2mpInstIndex_Type()
)
vRtrMplsP2mpInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstIndex.setStatus("current")
_VRtrMplsP2mpInstRowStatus_Type = RowStatus
_VRtrMplsP2mpInstRowStatus_Object = MibTableColumn
vRtrMplsP2mpInstRowStatus = _VRtrMplsP2mpInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 2),
    _VRtrMplsP2mpInstRowStatus_Type()
)
vRtrMplsP2mpInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstRowStatus.setStatus("current")
_VRtrMplsP2mpInstLastChange_Type = TimeStamp
_VRtrMplsP2mpInstLastChange_Object = MibTableColumn
vRtrMplsP2mpInstLastChange = _VRtrMplsP2mpInstLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 3),
    _VRtrMplsP2mpInstLastChange_Type()
)
vRtrMplsP2mpInstLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstLastChange.setStatus("current")
_VRtrMplsP2mpInstName_Type = TNamedItemOrEmpty
_VRtrMplsP2mpInstName_Object = MibTableColumn
vRtrMplsP2mpInstName = _VRtrMplsP2mpInstName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 4),
    _VRtrMplsP2mpInstName_Type()
)
vRtrMplsP2mpInstName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstName.setStatus("current")


class _VRtrMplsP2mpInstType_Type(Integer32):
    """Custom type vRtrMplsP2mpInstType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("primary", 2))
    )


_VRtrMplsP2mpInstType_Type.__name__ = "Integer32"
_VRtrMplsP2mpInstType_Object = MibTableColumn
vRtrMplsP2mpInstType = _VRtrMplsP2mpInstType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 5),
    _VRtrMplsP2mpInstType_Type()
)
vRtrMplsP2mpInstType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstType.setStatus("current")


class _VRtrMplsP2mpInstProperties_Type(Bits):
    """Custom type vRtrMplsP2mpInstProperties based on Bits"""
    namedValues = NamedValues(
        *(("recordRoute", 0),
          ("adaptive", 1),
          ("cspf", 2),
          ("mergeable", 3),
          ("fastReroute", 4))
    )

_VRtrMplsP2mpInstProperties_Type.__name__ = "Bits"
_VRtrMplsP2mpInstProperties_Object = MibTableColumn
vRtrMplsP2mpInstProperties = _VRtrMplsP2mpInstProperties_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 6),
    _VRtrMplsP2mpInstProperties_Type()
)
vRtrMplsP2mpInstProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstProperties.setStatus("current")


class _VRtrMplsP2mpInstBandwidth_Type(TmnxMplsLspBandwidth):
    """Custom type vRtrMplsP2mpInstBandwidth based on TmnxMplsLspBandwidth"""
    defaultValue = 0


_VRtrMplsP2mpInstBandwidth_Type.__name__ = "TmnxMplsLspBandwidth"
_VRtrMplsP2mpInstBandwidth_Object = MibTableColumn
vRtrMplsP2mpInstBandwidth = _VRtrMplsP2mpInstBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 7),
    _VRtrMplsP2mpInstBandwidth_Type()
)
vRtrMplsP2mpInstBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstBandwidth.setUnits("megabps")


class _VRtrMplsP2mpInstState_Type(Integer32):
    """Custom type vRtrMplsP2mpInstState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("active", 2),
          ("inactive", 3))
    )


_VRtrMplsP2mpInstState_Type.__name__ = "Integer32"
_VRtrMplsP2mpInstState_Object = MibTableColumn
vRtrMplsP2mpInstState = _VRtrMplsP2mpInstState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 8),
    _VRtrMplsP2mpInstState_Type()
)
vRtrMplsP2mpInstState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstState.setStatus("current")


class _VRtrMplsP2mpInstSetupPriority_Type(Unsigned32):
    """Custom type vRtrMplsP2mpInstSetupPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsP2mpInstSetupPriority_Type.__name__ = "Unsigned32"
_VRtrMplsP2mpInstSetupPriority_Object = MibTableColumn
vRtrMplsP2mpInstSetupPriority = _VRtrMplsP2mpInstSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 9),
    _VRtrMplsP2mpInstSetupPriority_Type()
)
vRtrMplsP2mpInstSetupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstSetupPriority.setStatus("current")


class _VRtrMplsP2mpInstHoldPriority_Type(Unsigned32):
    """Custom type vRtrMplsP2mpInstHoldPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsP2mpInstHoldPriority_Type.__name__ = "Unsigned32"
_VRtrMplsP2mpInstHoldPriority_Object = MibTableColumn
vRtrMplsP2mpInstHoldPriority = _VRtrMplsP2mpInstHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 10),
    _VRtrMplsP2mpInstHoldPriority_Type()
)
vRtrMplsP2mpInstHoldPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstHoldPriority.setStatus("current")


class _VRtrMplsP2mpInstRecord_Type(TruthValue):
    """Custom type vRtrMplsP2mpInstRecord based on TruthValue"""
    defaultValue = 1


_VRtrMplsP2mpInstRecord_Type.__name__ = "TruthValue"
_VRtrMplsP2mpInstRecord_Object = MibTableColumn
vRtrMplsP2mpInstRecord = _VRtrMplsP2mpInstRecord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 11),
    _VRtrMplsP2mpInstRecord_Type()
)
vRtrMplsP2mpInstRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstRecord.setStatus("current")


class _VRtrMplsP2mpInstHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsP2mpInstHopLimit based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_VRtrMplsP2mpInstHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsP2mpInstHopLimit_Object = MibTableColumn
vRtrMplsP2mpInstHopLimit = _VRtrMplsP2mpInstHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 12),
    _VRtrMplsP2mpInstHopLimit_Type()
)
vRtrMplsP2mpInstHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstHopLimit.setStatus("current")


class _VRtrMplsP2mpInstAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsP2mpInstAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrMplsP2mpInstAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsP2mpInstAdminState_Object = MibTableColumn
vRtrMplsP2mpInstAdminState = _VRtrMplsP2mpInstAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 13),
    _VRtrMplsP2mpInstAdminState_Type()
)
vRtrMplsP2mpInstAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstAdminState.setStatus("current")
_VRtrMplsP2mpInstOperState_Type = TmnxOperState
_VRtrMplsP2mpInstOperState_Object = MibTableColumn
vRtrMplsP2mpInstOperState = _VRtrMplsP2mpInstOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 14),
    _VRtrMplsP2mpInstOperState_Type()
)
vRtrMplsP2mpInstOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstOperState.setStatus("current")


class _VRtrMplsP2mpInstInheritance_Type(Unsigned32):
    """Custom type vRtrMplsP2mpInstInheritance based on Unsigned32"""
    defaultValue = 0


_VRtrMplsP2mpInstInheritance_Type.__name__ = "Unsigned32"
_VRtrMplsP2mpInstInheritance_Object = MibTableColumn
vRtrMplsP2mpInstInheritance = _VRtrMplsP2mpInstInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 15),
    _VRtrMplsP2mpInstInheritance_Type()
)
vRtrMplsP2mpInstInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstInheritance.setStatus("current")
_VRtrMplsP2mpInstLspId_Type = MplsLSPID
_VRtrMplsP2mpInstLspId_Object = MibTableColumn
vRtrMplsP2mpInstLspId = _VRtrMplsP2mpInstLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 16),
    _VRtrMplsP2mpInstLspId_Type()
)
vRtrMplsP2mpInstLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstLspId.setStatus("current")
_VRtrMplsP2mpInstNegotiatedMTU_Type = Unsigned32
_VRtrMplsP2mpInstNegotiatedMTU_Object = MibTableColumn
vRtrMplsP2mpInstNegotiatedMTU = _VRtrMplsP2mpInstNegotiatedMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 17),
    _VRtrMplsP2mpInstNegotiatedMTU_Type()
)
vRtrMplsP2mpInstNegotiatedMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstNegotiatedMTU.setStatus("current")
_VRtrMplsP2mpInstFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsP2mpInstFailCode_Object = MibTableColumn
vRtrMplsP2mpInstFailCode = _VRtrMplsP2mpInstFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 18),
    _VRtrMplsP2mpInstFailCode_Type()
)
vRtrMplsP2mpInstFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstFailCode.setStatus("current")
_VRtrMplsP2mpInstFailNodeArType_Type = InetAddressType
_VRtrMplsP2mpInstFailNodeArType_Object = MibTableColumn
vRtrMplsP2mpInstFailNodeArType = _VRtrMplsP2mpInstFailNodeArType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 19),
    _VRtrMplsP2mpInstFailNodeArType_Type()
)
vRtrMplsP2mpInstFailNodeArType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstFailNodeArType.setStatus("current")


class _VRtrMplsP2mpInstFailNodeAddr_Type(InetAddress):
    """Custom type vRtrMplsP2mpInstFailNodeAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsP2mpInstFailNodeAddr_Type.__name__ = "InetAddress"
_VRtrMplsP2mpInstFailNodeAddr_Object = MibTableColumn
vRtrMplsP2mpInstFailNodeAddr = _VRtrMplsP2mpInstFailNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 20),
    _VRtrMplsP2mpInstFailNodeAddr_Type()
)
vRtrMplsP2mpInstFailNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstFailNodeAddr.setStatus("current")


class _VRtrMplsP2mpInstAdminGrpInclude_Type(Unsigned32):
    """Custom type vRtrMplsP2mpInstAdminGrpInclude based on Unsigned32"""
    defaultValue = 0


_VRtrMplsP2mpInstAdminGrpInclude_Type.__name__ = "Unsigned32"
_VRtrMplsP2mpInstAdminGrpInclude_Object = MibTableColumn
vRtrMplsP2mpInstAdminGrpInclude = _VRtrMplsP2mpInstAdminGrpInclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 21),
    _VRtrMplsP2mpInstAdminGrpInclude_Type()
)
vRtrMplsP2mpInstAdminGrpInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstAdminGrpInclude.setStatus("current")


class _VRtrMplsP2mpInstAdminGrpExclude_Type(Unsigned32):
    """Custom type vRtrMplsP2mpInstAdminGrpExclude based on Unsigned32"""
    defaultValue = 0


_VRtrMplsP2mpInstAdminGrpExclude_Type.__name__ = "Unsigned32"
_VRtrMplsP2mpInstAdminGrpExclude_Object = MibTableColumn
vRtrMplsP2mpInstAdminGrpExclude = _VRtrMplsP2mpInstAdminGrpExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 22),
    _VRtrMplsP2mpInstAdminGrpExclude_Type()
)
vRtrMplsP2mpInstAdminGrpExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstAdminGrpExclude.setStatus("current")


class _VRtrMplsP2mpInstAdaptive_Type(TruthValue):
    """Custom type vRtrMplsP2mpInstAdaptive based on TruthValue"""
    defaultValue = 1


_VRtrMplsP2mpInstAdaptive_Type.__name__ = "TruthValue"
_VRtrMplsP2mpInstAdaptive_Object = MibTableColumn
vRtrMplsP2mpInstAdaptive = _VRtrMplsP2mpInstAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 23),
    _VRtrMplsP2mpInstAdaptive_Type()
)
vRtrMplsP2mpInstAdaptive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstAdaptive.setStatus("current")
_VRtrMplsP2mpInstOperBandwidth_Type = Integer32
_VRtrMplsP2mpInstOperBandwidth_Object = MibTableColumn
vRtrMplsP2mpInstOperBandwidth = _VRtrMplsP2mpInstOperBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 24),
    _VRtrMplsP2mpInstOperBandwidth_Type()
)
vRtrMplsP2mpInstOperBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstOperBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstOperBandwidth.setUnits("megabps")


class _VRtrMplsP2mpInstResignal_Type(TmnxActionType):
    """Custom type vRtrMplsP2mpInstResignal based on TmnxActionType"""
    defaultValue = 2


_VRtrMplsP2mpInstResignal_Type.__name__ = "TmnxActionType"
_VRtrMplsP2mpInstResignal_Object = MibTableColumn
vRtrMplsP2mpInstResignal = _VRtrMplsP2mpInstResignal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 25),
    _VRtrMplsP2mpInstResignal_Type()
)
vRtrMplsP2mpInstResignal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstResignal.setStatus("current")
_VRtrMplsP2mpInstOperMTU_Type = Unsigned32
_VRtrMplsP2mpInstOperMTU_Object = MibTableColumn
vRtrMplsP2mpInstOperMTU = _VRtrMplsP2mpInstOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 26),
    _VRtrMplsP2mpInstOperMTU_Type()
)
vRtrMplsP2mpInstOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstOperMTU.setStatus("current")


class _VRtrMplsP2mpInstRecordLabel_Type(Integer32):
    """Custom type vRtrMplsP2mpInstRecordLabel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("record", 1),
          ("noRecord", 2))
    )


_VRtrMplsP2mpInstRecordLabel_Type.__name__ = "Integer32"
_VRtrMplsP2mpInstRecordLabel_Object = MibTableColumn
vRtrMplsP2mpInstRecordLabel = _VRtrMplsP2mpInstRecordLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 27),
    _VRtrMplsP2mpInstRecordLabel_Type()
)
vRtrMplsP2mpInstRecordLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstRecordLabel.setStatus("current")
_VRtrMplsP2mpInstLastResigAttpt_Type = TimeStamp
_VRtrMplsP2mpInstLastResigAttpt_Object = MibTableColumn
vRtrMplsP2mpInstLastResigAttpt = _VRtrMplsP2mpInstLastResigAttpt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 28),
    _VRtrMplsP2mpInstLastResigAttpt_Type()
)
vRtrMplsP2mpInstLastResigAttpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstLastResigAttpt.setStatus("current")
_VRtrMplsP2mpInstMetric_Type = Unsigned32
_VRtrMplsP2mpInstMetric_Object = MibTableColumn
vRtrMplsP2mpInstMetric = _VRtrMplsP2mpInstMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 29),
    _VRtrMplsP2mpInstMetric_Type()
)
vRtrMplsP2mpInstMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstMetric.setStatus("current")
_VRtrMplsP2mpInstLastMBBType_Type = TmnxMplsMBBType
_VRtrMplsP2mpInstLastMBBType_Object = MibTableColumn
vRtrMplsP2mpInstLastMBBType = _VRtrMplsP2mpInstLastMBBType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 30),
    _VRtrMplsP2mpInstLastMBBType_Type()
)
vRtrMplsP2mpInstLastMBBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstLastMBBType.setStatus("current")
_VRtrMplsP2mpInstLastMBBEnd_Type = TimeStamp
_VRtrMplsP2mpInstLastMBBEnd_Object = MibTableColumn
vRtrMplsP2mpInstLastMBBEnd = _VRtrMplsP2mpInstLastMBBEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 31),
    _VRtrMplsP2mpInstLastMBBEnd_Type()
)
vRtrMplsP2mpInstLastMBBEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstLastMBBEnd.setStatus("current")
_VRtrMplsP2mpInstLastMBBMetric_Type = Unsigned32
_VRtrMplsP2mpInstLastMBBMetric_Object = MibTableColumn
vRtrMplsP2mpInstLastMBBMetric = _VRtrMplsP2mpInstLastMBBMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 32),
    _VRtrMplsP2mpInstLastMBBMetric_Type()
)
vRtrMplsP2mpInstLastMBBMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstLastMBBMetric.setStatus("current")


class _VRtrMplsP2mpInstLastMBBState_Type(Integer32):
    """Custom type vRtrMplsP2mpInstLastMBBState based on Integer32"""
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
          ("success", 2),
          ("fail", 3))
    )


_VRtrMplsP2mpInstLastMBBState_Type.__name__ = "Integer32"
_VRtrMplsP2mpInstLastMBBState_Object = MibTableColumn
vRtrMplsP2mpInstLastMBBState = _VRtrMplsP2mpInstLastMBBState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 33),
    _VRtrMplsP2mpInstLastMBBState_Type()
)
vRtrMplsP2mpInstLastMBBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstLastMBBState.setStatus("current")
_VRtrMplsP2mpInstMBBTypeInProg_Type = TmnxMplsMBBType
_VRtrMplsP2mpInstMBBTypeInProg_Object = MibTableColumn
vRtrMplsP2mpInstMBBTypeInProg = _VRtrMplsP2mpInstMBBTypeInProg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 34),
    _VRtrMplsP2mpInstMBBTypeInProg_Type()
)
vRtrMplsP2mpInstMBBTypeInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstMBBTypeInProg.setStatus("current")
_VRtrMplsP2mpInstMBBStarted_Type = TimeStamp
_VRtrMplsP2mpInstMBBStarted_Object = MibTableColumn
vRtrMplsP2mpInstMBBStarted = _VRtrMplsP2mpInstMBBStarted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 35),
    _VRtrMplsP2mpInstMBBStarted_Type()
)
vRtrMplsP2mpInstMBBStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstMBBStarted.setStatus("current")
_VRtrMplsP2mpInstMBBNextRetry_Type = Unsigned32
_VRtrMplsP2mpInstMBBNextRetry_Object = MibTableColumn
vRtrMplsP2mpInstMBBNextRetry = _VRtrMplsP2mpInstMBBNextRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 36),
    _VRtrMplsP2mpInstMBBNextRetry_Type()
)
vRtrMplsP2mpInstMBBNextRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstMBBNextRetry.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstMBBNextRetry.setUnits("seconds")
_VRtrMplsP2mpInstMBBRetryAttpts_Type = Unsigned32
_VRtrMplsP2mpInstMBBRetryAttpts_Object = MibTableColumn
vRtrMplsP2mpInstMBBRetryAttpts = _VRtrMplsP2mpInstMBBRetryAttpts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 37),
    _VRtrMplsP2mpInstMBBRetryAttpts_Type()
)
vRtrMplsP2mpInstMBBRetryAttpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstMBBRetryAttpts.setStatus("current")
_VRtrMplsP2mpInstMBBFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsP2mpInstMBBFailCode_Object = MibTableColumn
vRtrMplsP2mpInstMBBFailCode = _VRtrMplsP2mpInstMBBFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 38),
    _VRtrMplsP2mpInstMBBFailCode_Type()
)
vRtrMplsP2mpInstMBBFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstMBBFailCode.setStatus("current")
_VRtrMplsP2mpInstMBBFailNodeType_Type = InetAddressType
_VRtrMplsP2mpInstMBBFailNodeType_Object = MibTableColumn
vRtrMplsP2mpInstMBBFailNodeType = _VRtrMplsP2mpInstMBBFailNodeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 39),
    _VRtrMplsP2mpInstMBBFailNodeType_Type()
)
vRtrMplsP2mpInstMBBFailNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstMBBFailNodeType.setStatus("current")


class _VRtrMplsP2mpInstMBBFailNodeAddr_Type(InetAddress):
    """Custom type vRtrMplsP2mpInstMBBFailNodeAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsP2mpInstMBBFailNodeAddr_Type.__name__ = "InetAddress"
_VRtrMplsP2mpInstMBBFailNodeAddr_Object = MibTableColumn
vRtrMplsP2mpInstMBBFailNodeAddr = _VRtrMplsP2mpInstMBBFailNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 40),
    _VRtrMplsP2mpInstMBBFailNodeAddr_Type()
)
vRtrMplsP2mpInstMBBFailNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstMBBFailNodeAddr.setStatus("current")
_VRtrMplsP2mpInstStatTable_Object = MibTable
vRtrMplsP2mpInstStatTable = _VRtrMplsP2mpInstStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26)
)
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatTable.setStatus("current")
_VRtrMplsP2mpInstStatEntry_Object = MibTableRow
vRtrMplsP2mpInstStatEntry = _VRtrMplsP2mpInstStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatEntry.setStatus("current")
_VRtrMplsP2mpInstStatS2lChanges_Type = Counter32
_VRtrMplsP2mpInstStatS2lChanges_Object = MibTableColumn
vRtrMplsP2mpInstStatS2lChanges = _VRtrMplsP2mpInstStatS2lChanges_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 1),
    _VRtrMplsP2mpInstStatS2lChanges_Type()
)
vRtrMplsP2mpInstStatS2lChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatS2lChanges.setStatus("current")
_VRtrMplsP2mpInstStatLastS2lChange_Type = TmnxTimeInterval
_VRtrMplsP2mpInstStatLastS2lChange_Object = MibTableColumn
vRtrMplsP2mpInstStatLastS2lChange = _VRtrMplsP2mpInstStatLastS2lChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 2),
    _VRtrMplsP2mpInstStatLastS2lChange_Type()
)
vRtrMplsP2mpInstStatLastS2lChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatLastS2lChange.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatLastS2lChange.setUnits("centiseconds")
_VRtrMplsP2mpInstStatConfiguredS2ls_Type = Gauge32
_VRtrMplsP2mpInstStatConfiguredS2ls_Object = MibTableColumn
vRtrMplsP2mpInstStatConfiguredS2ls = _VRtrMplsP2mpInstStatConfiguredS2ls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 3),
    _VRtrMplsP2mpInstStatConfiguredS2ls_Type()
)
vRtrMplsP2mpInstStatConfiguredS2ls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatConfiguredS2ls.setStatus("current")
_VRtrMplsP2mpInstStatOperationalS2ls_Type = Gauge32
_VRtrMplsP2mpInstStatOperationalS2ls_Object = MibTableColumn
vRtrMplsP2mpInstStatOperationalS2ls = _VRtrMplsP2mpInstStatOperationalS2ls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 4),
    _VRtrMplsP2mpInstStatOperationalS2ls_Type()
)
vRtrMplsP2mpInstStatOperationalS2ls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatOperationalS2ls.setStatus("current")
_VRtrMplsP2mpInstStatLastS2lTimeUp_Type = TmnxTimeInterval
_VRtrMplsP2mpInstStatLastS2lTimeUp_Object = MibTableColumn
vRtrMplsP2mpInstStatLastS2lTimeUp = _VRtrMplsP2mpInstStatLastS2lTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 5),
    _VRtrMplsP2mpInstStatLastS2lTimeUp_Type()
)
vRtrMplsP2mpInstStatLastS2lTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatLastS2lTimeUp.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatLastS2lTimeUp.setUnits("centiseconds")
_VRtrMplsP2mpInstStatLastS2lTimeDown_Type = TmnxTimeInterval
_VRtrMplsP2mpInstStatLastS2lTimeDown_Object = MibTableColumn
vRtrMplsP2mpInstStatLastS2lTimeDown = _VRtrMplsP2mpInstStatLastS2lTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 6),
    _VRtrMplsP2mpInstStatLastS2lTimeDown_Type()
)
vRtrMplsP2mpInstStatLastS2lTimeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatLastS2lTimeDown.setStatus("current")
_VRtrMplsP2mpInstStatTimeUp_Type = TmnxTimeInterval
_VRtrMplsP2mpInstStatTimeUp_Object = MibTableColumn
vRtrMplsP2mpInstStatTimeUp = _VRtrMplsP2mpInstStatTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 7),
    _VRtrMplsP2mpInstStatTimeUp_Type()
)
vRtrMplsP2mpInstStatTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatTimeUp.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatTimeUp.setUnits("centiseconds")
_VRtrMplsP2mpInstStatTimeDown_Type = TmnxTimeInterval
_VRtrMplsP2mpInstStatTimeDown_Object = MibTableColumn
vRtrMplsP2mpInstStatTimeDown = _VRtrMplsP2mpInstStatTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 8),
    _VRtrMplsP2mpInstStatTimeDown_Type()
)
vRtrMplsP2mpInstStatTimeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatTimeDown.setStatus("current")
_VRtrMplsP2mpInstStatTransitions_Type = Counter32
_VRtrMplsP2mpInstStatTransitions_Object = MibTableColumn
vRtrMplsP2mpInstStatTransitions = _VRtrMplsP2mpInstStatTransitions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 9),
    _VRtrMplsP2mpInstStatTransitions_Type()
)
vRtrMplsP2mpInstStatTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatTransitions.setStatus("current")
_VRtrMplsP2mpInstStatLastTrans_Type = TmnxTimeInterval
_VRtrMplsP2mpInstStatLastTrans_Object = MibTableColumn
vRtrMplsP2mpInstStatLastTrans = _VRtrMplsP2mpInstStatLastTrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 10),
    _VRtrMplsP2mpInstStatLastTrans_Type()
)
vRtrMplsP2mpInstStatLastTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatLastTrans.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatLastTrans.setUnits("ten-milliseconds")
_VRtrMplsS2lSubLspTblLastChanged_Type = TimeStamp
_VRtrMplsS2lSubLspTblLastChanged_Object = MibScalar
vRtrMplsS2lSubLspTblLastChanged = _VRtrMplsS2lSubLspTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 27),
    _VRtrMplsS2lSubLspTblLastChanged_Type()
)
vRtrMplsS2lSubLspTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTblLastChanged.setStatus("current")
_VRtrMplsS2lSubLspTable_Object = MibTable
vRtrMplsS2lSubLspTable = _VRtrMplsS2lSubLspTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28)
)
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTable.setStatus("current")
_VRtrMplsS2lSubLspEntry_Object = MibTableRow
vRtrMplsS2lSubLspEntry = _VRtrMplsS2lSubLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1)
)
vRtrMplsS2lSubLspEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstIndex"),
    (0, "MPLS-TE-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspDstAddrType"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspDstAddr"),
)
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspEntry.setStatus("current")
_VRtrMplsS2lSubLspDstAddrType_Type = InetAddressType
_VRtrMplsS2lSubLspDstAddrType_Object = MibTableColumn
vRtrMplsS2lSubLspDstAddrType = _VRtrMplsS2lSubLspDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 1),
    _VRtrMplsS2lSubLspDstAddrType_Type()
)
vRtrMplsS2lSubLspDstAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspDstAddrType.setStatus("current")


class _VRtrMplsS2lSubLspDstAddr_Type(InetAddress):
    """Custom type vRtrMplsS2lSubLspDstAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsS2lSubLspDstAddr_Type.__name__ = "InetAddress"
_VRtrMplsS2lSubLspDstAddr_Object = MibTableColumn
vRtrMplsS2lSubLspDstAddr = _VRtrMplsS2lSubLspDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 2),
    _VRtrMplsS2lSubLspDstAddr_Type()
)
vRtrMplsS2lSubLspDstAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspDstAddr.setStatus("current")
_VRtrMplsS2lSubLspRowStatus_Type = RowStatus
_VRtrMplsS2lSubLspRowStatus_Object = MibTableColumn
vRtrMplsS2lSubLspRowStatus = _VRtrMplsS2lSubLspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 3),
    _VRtrMplsS2lSubLspRowStatus_Type()
)
vRtrMplsS2lSubLspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspRowStatus.setStatus("current")
_VRtrMplsS2lSubLspLastChange_Type = TimeStamp
_VRtrMplsS2lSubLspLastChange_Object = MibTableColumn
vRtrMplsS2lSubLspLastChange = _VRtrMplsS2lSubLspLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 4),
    _VRtrMplsS2lSubLspLastChange_Type()
)
vRtrMplsS2lSubLspLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspLastChange.setStatus("current")


class _VRtrMplsS2lSubLspType_Type(Integer32):
    """Custom type vRtrMplsS2lSubLspType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("s2lPath", 1)
    )


_VRtrMplsS2lSubLspType_Type.__name__ = "Integer32"
_VRtrMplsS2lSubLspType_Object = MibTableColumn
vRtrMplsS2lSubLspType = _VRtrMplsS2lSubLspType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 5),
    _VRtrMplsS2lSubLspType_Type()
)
vRtrMplsS2lSubLspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspType.setStatus("current")


class _VRtrMplsS2lSubLspProperties_Type(Bits):
    """Custom type vRtrMplsS2lSubLspProperties based on Bits"""
    namedValues = NamedValues(
        *(("recordRoute", 0),
          ("adaptive", 1),
          ("cspf", 2),
          ("mergeable", 3),
          ("fastReroute", 4))
    )

_VRtrMplsS2lSubLspProperties_Type.__name__ = "Bits"
_VRtrMplsS2lSubLspProperties_Object = MibTableColumn
vRtrMplsS2lSubLspProperties = _VRtrMplsS2lSubLspProperties_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 6),
    _VRtrMplsS2lSubLspProperties_Type()
)
vRtrMplsS2lSubLspProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspProperties.setStatus("current")


class _VRtrMplsS2lSubLspState_Type(Integer32):
    """Custom type vRtrMplsS2lSubLspState based on Integer32"""
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
        *(("unknown", 1),
          ("active", 2),
          ("inactive", 3))
    )


_VRtrMplsS2lSubLspState_Type.__name__ = "Integer32"
_VRtrMplsS2lSubLspState_Object = MibTableColumn
vRtrMplsS2lSubLspState = _VRtrMplsS2lSubLspState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 7),
    _VRtrMplsS2lSubLspState_Type()
)
vRtrMplsS2lSubLspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspState.setStatus("current")


class _VRtrMplsS2lSubLspAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsS2lSubLspAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrMplsS2lSubLspAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsS2lSubLspAdminState_Object = MibTableColumn
vRtrMplsS2lSubLspAdminState = _VRtrMplsS2lSubLspAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 8),
    _VRtrMplsS2lSubLspAdminState_Type()
)
vRtrMplsS2lSubLspAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspAdminState.setStatus("current")
_VRtrMplsS2lSubLspOperState_Type = TmnxOperState
_VRtrMplsS2lSubLspOperState_Object = MibTableColumn
vRtrMplsS2lSubLspOperState = _VRtrMplsS2lSubLspOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 9),
    _VRtrMplsS2lSubLspOperState_Type()
)
vRtrMplsS2lSubLspOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspOperState.setStatus("current")
_VRtrMplsS2lSubGroupId_Type = Unsigned32
_VRtrMplsS2lSubGroupId_Object = MibTableColumn
vRtrMplsS2lSubGroupId = _VRtrMplsS2lSubGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 10),
    _VRtrMplsS2lSubGroupId_Type()
)
vRtrMplsS2lSubGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubGroupId.setStatus("current")
_VRtrMplsS2lSubLspId_Type = MplsLSPID
_VRtrMplsS2lSubLspId_Object = MibTableColumn
vRtrMplsS2lSubLspId = _VRtrMplsS2lSubLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 11),
    _VRtrMplsS2lSubLspId_Type()
)
vRtrMplsS2lSubLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspId.setStatus("current")
_VRtrMplsS2lSubLspRetryTimeRemain_Type = Unsigned32
_VRtrMplsS2lSubLspRetryTimeRemain_Object = MibTableColumn
vRtrMplsS2lSubLspRetryTimeRemain = _VRtrMplsS2lSubLspRetryTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 12),
    _VRtrMplsS2lSubLspRetryTimeRemain_Type()
)
vRtrMplsS2lSubLspRetryTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspRetryTimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspRetryTimeRemain.setUnits("centiseconds")


class _VRtrMplsS2lSubLspTunARHopLtIndex_Type(Integer32):
    """Custom type vRtrMplsS2lSubLspTunARHopLtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsS2lSubLspTunARHopLtIndex_Type.__name__ = "Integer32"
_VRtrMplsS2lSubLspTunARHopLtIndex_Object = MibTableColumn
vRtrMplsS2lSubLspTunARHopLtIndex = _VRtrMplsS2lSubLspTunARHopLtIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 13),
    _VRtrMplsS2lSubLspTunARHopLtIndex_Type()
)
vRtrMplsS2lSubLspTunARHopLtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTunARHopLtIndex.setStatus("current")


class _VRtrMplsS2lSubLspNegotiatedMTU_Type(Unsigned32):
    """Custom type vRtrMplsS2lSubLspNegotiatedMTU based on Unsigned32"""
    defaultValue = 0


_VRtrMplsS2lSubLspNegotiatedMTU_Type.__name__ = "Unsigned32"
_VRtrMplsS2lSubLspNegotiatedMTU_Object = MibTableColumn
vRtrMplsS2lSubLspNegotiatedMTU = _VRtrMplsS2lSubLspNegotiatedMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 14),
    _VRtrMplsS2lSubLspNegotiatedMTU_Type()
)
vRtrMplsS2lSubLspNegotiatedMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspNegotiatedMTU.setStatus("current")
_VRtrMplsS2lSubLspFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsS2lSubLspFailCode_Object = MibTableColumn
vRtrMplsS2lSubLspFailCode = _VRtrMplsS2lSubLspFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 15),
    _VRtrMplsS2lSubLspFailCode_Type()
)
vRtrMplsS2lSubLspFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspFailCode.setStatus("current")
_VRtrMplsS2lSubLspFailNodeArType_Type = InetAddressType
_VRtrMplsS2lSubLspFailNodeArType_Object = MibTableColumn
vRtrMplsS2lSubLspFailNodeArType = _VRtrMplsS2lSubLspFailNodeArType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 16),
    _VRtrMplsS2lSubLspFailNodeArType_Type()
)
vRtrMplsS2lSubLspFailNodeArType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspFailNodeArType.setStatus("current")


class _VRtrMplsS2lSubLspFailNodeAddr_Type(InetAddress):
    """Custom type vRtrMplsS2lSubLspFailNodeAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsS2lSubLspFailNodeAddr_Type.__name__ = "InetAddress"
_VRtrMplsS2lSubLspFailNodeAddr_Object = MibTableColumn
vRtrMplsS2lSubLspFailNodeAddr = _VRtrMplsS2lSubLspFailNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 17),
    _VRtrMplsS2lSubLspFailNodeAddr_Type()
)
vRtrMplsS2lSubLspFailNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspFailNodeAddr.setStatus("current")
_VRtrMplsS2lSubLspOperBandwidth_Type = Integer32
_VRtrMplsS2lSubLspOperBandwidth_Object = MibTableColumn
vRtrMplsS2lSubLspOperBandwidth = _VRtrMplsS2lSubLspOperBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 18),
    _VRtrMplsS2lSubLspOperBandwidth_Type()
)
vRtrMplsS2lSubLspOperBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspOperBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspOperBandwidth.setUnits("megabps")


class _VRtrMplsS2lSubLspTunCRHopLtIndex_Type(Integer32):
    """Custom type vRtrMplsS2lSubLspTunCRHopLtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsS2lSubLspTunCRHopLtIndex_Type.__name__ = "Integer32"
_VRtrMplsS2lSubLspTunCRHopLtIndex_Object = MibTableColumn
vRtrMplsS2lSubLspTunCRHopLtIndex = _VRtrMplsS2lSubLspTunCRHopLtIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 19),
    _VRtrMplsS2lSubLspTunCRHopLtIndex_Type()
)
vRtrMplsS2lSubLspTunCRHopLtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTunCRHopLtIndex.setStatus("current")
_VRtrMplsS2lSubLspOperMTU_Type = Unsigned32
_VRtrMplsS2lSubLspOperMTU_Object = MibTableColumn
vRtrMplsS2lSubLspOperMTU = _VRtrMplsS2lSubLspOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 20),
    _VRtrMplsS2lSubLspOperMTU_Type()
)
vRtrMplsS2lSubLspOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspOperMTU.setStatus("current")
_VRtrMplsS2lSubLspLastResigAttpt_Type = TimeStamp
_VRtrMplsS2lSubLspLastResigAttpt_Object = MibTableColumn
vRtrMplsS2lSubLspLastResigAttpt = _VRtrMplsS2lSubLspLastResigAttpt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 21),
    _VRtrMplsS2lSubLspLastResigAttpt_Type()
)
vRtrMplsS2lSubLspLastResigAttpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspLastResigAttpt.setStatus("current")
_VRtrMplsS2lSubLspLastMBBType_Type = TmnxMplsMBBType
_VRtrMplsS2lSubLspLastMBBType_Object = MibTableColumn
vRtrMplsS2lSubLspLastMBBType = _VRtrMplsS2lSubLspLastMBBType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 22),
    _VRtrMplsS2lSubLspLastMBBType_Type()
)
vRtrMplsS2lSubLspLastMBBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspLastMBBType.setStatus("current")
_VRtrMplsS2lSubLspLastMBBEnd_Type = TimeStamp
_VRtrMplsS2lSubLspLastMBBEnd_Object = MibTableColumn
vRtrMplsS2lSubLspLastMBBEnd = _VRtrMplsS2lSubLspLastMBBEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 23),
    _VRtrMplsS2lSubLspLastMBBEnd_Type()
)
vRtrMplsS2lSubLspLastMBBEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspLastMBBEnd.setStatus("current")
_VRtrMplsS2lSubLspLastMBBMetric_Type = Unsigned32
_VRtrMplsS2lSubLspLastMBBMetric_Object = MibTableColumn
vRtrMplsS2lSubLspLastMBBMetric = _VRtrMplsS2lSubLspLastMBBMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 24),
    _VRtrMplsS2lSubLspLastMBBMetric_Type()
)
vRtrMplsS2lSubLspLastMBBMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspLastMBBMetric.setStatus("current")


class _VRtrMplsS2lSubLspLastMBBState_Type(Integer32):
    """Custom type vRtrMplsS2lSubLspLastMBBState based on Integer32"""
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
          ("success", 2),
          ("fail", 3))
    )


_VRtrMplsS2lSubLspLastMBBState_Type.__name__ = "Integer32"
_VRtrMplsS2lSubLspLastMBBState_Object = MibTableColumn
vRtrMplsS2lSubLspLastMBBState = _VRtrMplsS2lSubLspLastMBBState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 25),
    _VRtrMplsS2lSubLspLastMBBState_Type()
)
vRtrMplsS2lSubLspLastMBBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspLastMBBState.setStatus("current")
_VRtrMplsS2lSubLspMBBTypeInProg_Type = TmnxMplsMBBType
_VRtrMplsS2lSubLspMBBTypeInProg_Object = MibTableColumn
vRtrMplsS2lSubLspMBBTypeInProg = _VRtrMplsS2lSubLspMBBTypeInProg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 26),
    _VRtrMplsS2lSubLspMBBTypeInProg_Type()
)
vRtrMplsS2lSubLspMBBTypeInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBTypeInProg.setStatus("current")
_VRtrMplsS2lSubLspMBBStarted_Type = TimeStamp
_VRtrMplsS2lSubLspMBBStarted_Object = MibTableColumn
vRtrMplsS2lSubLspMBBStarted = _VRtrMplsS2lSubLspMBBStarted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 27),
    _VRtrMplsS2lSubLspMBBStarted_Type()
)
vRtrMplsS2lSubLspMBBStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBStarted.setStatus("current")
_VRtrMplsS2lSubLspMBBNextRetry_Type = Unsigned32
_VRtrMplsS2lSubLspMBBNextRetry_Object = MibTableColumn
vRtrMplsS2lSubLspMBBNextRetry = _VRtrMplsS2lSubLspMBBNextRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 28),
    _VRtrMplsS2lSubLspMBBNextRetry_Type()
)
vRtrMplsS2lSubLspMBBNextRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBNextRetry.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBNextRetry.setUnits("seconds")
_VRtrMplsS2lSubLspMBBRetryAttpts_Type = Unsigned32
_VRtrMplsS2lSubLspMBBRetryAttpts_Object = MibTableColumn
vRtrMplsS2lSubLspMBBRetryAttpts = _VRtrMplsS2lSubLspMBBRetryAttpts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 29),
    _VRtrMplsS2lSubLspMBBRetryAttpts_Type()
)
vRtrMplsS2lSubLspMBBRetryAttpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBRetryAttpts.setStatus("current")
_VRtrMplsS2lSubLspMBBFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsS2lSubLspMBBFailCode_Object = MibTableColumn
vRtrMplsS2lSubLspMBBFailCode = _VRtrMplsS2lSubLspMBBFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 30),
    _VRtrMplsS2lSubLspMBBFailCode_Type()
)
vRtrMplsS2lSubLspMBBFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBFailCode.setStatus("current")
_VRtrMplsS2lSubLspMBBFailNodeType_Type = InetAddressType
_VRtrMplsS2lSubLspMBBFailNodeType_Object = MibTableColumn
vRtrMplsS2lSubLspMBBFailNodeType = _VRtrMplsS2lSubLspMBBFailNodeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 31),
    _VRtrMplsS2lSubLspMBBFailNodeType_Type()
)
vRtrMplsS2lSubLspMBBFailNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBFailNodeType.setStatus("current")


class _VRtrMplsS2lSubLspMBBFailNodeAddr_Type(InetAddress):
    """Custom type vRtrMplsS2lSubLspMBBFailNodeAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsS2lSubLspMBBFailNodeAddr_Type.__name__ = "InetAddress"
_VRtrMplsS2lSubLspMBBFailNodeAddr_Object = MibTableColumn
vRtrMplsS2lSubLspMBBFailNodeAddr = _VRtrMplsS2lSubLspMBBFailNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 32),
    _VRtrMplsS2lSubLspMBBFailNodeAddr_Type()
)
vRtrMplsS2lSubLspMBBFailNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBFailNodeAddr.setStatus("current")
_VRtrMplsS2lSubLspUpTime_Type = TimeStamp
_VRtrMplsS2lSubLspUpTime_Object = MibTableColumn
vRtrMplsS2lSubLspUpTime = _VRtrMplsS2lSubLspUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 33),
    _VRtrMplsS2lSubLspUpTime_Type()
)
vRtrMplsS2lSubLspUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspUpTime.setStatus("current")
_VRtrMplsS2lSubLspDownTime_Type = TimeStamp
_VRtrMplsS2lSubLspDownTime_Object = MibTableColumn
vRtrMplsS2lSubLspDownTime = _VRtrMplsS2lSubLspDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 34),
    _VRtrMplsS2lSubLspDownTime_Type()
)
vRtrMplsS2lSubLspDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspDownTime.setStatus("current")
_VRtrMplsS2lSubLspIsFastRetry_Type = TruthValue
_VRtrMplsS2lSubLspIsFastRetry_Object = MibTableColumn
vRtrMplsS2lSubLspIsFastRetry = _VRtrMplsS2lSubLspIsFastRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 35),
    _VRtrMplsS2lSubLspIsFastRetry_Type()
)
vRtrMplsS2lSubLspIsFastRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspIsFastRetry.setStatus("current")
_VRtrMplsS2lSubLspTimeoutIn_Type = Unsigned32
_VRtrMplsS2lSubLspTimeoutIn_Object = MibTableColumn
vRtrMplsS2lSubLspTimeoutIn = _VRtrMplsS2lSubLspTimeoutIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 36),
    _VRtrMplsS2lSubLspTimeoutIn_Type()
)
vRtrMplsS2lSubLspTimeoutIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTimeoutIn.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTimeoutIn.setUnits("seconds")
_VRtrMplsS2lSubLspMBBTimeoutIn_Type = Unsigned32
_VRtrMplsS2lSubLspMBBTimeoutIn_Object = MibTableColumn
vRtrMplsS2lSubLspMBBTimeoutIn = _VRtrMplsS2lSubLspMBBTimeoutIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 37),
    _VRtrMplsS2lSubLspMBBTimeoutIn_Type()
)
vRtrMplsS2lSubLspMBBTimeoutIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBTimeoutIn.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBTimeoutIn.setUnits("seconds")
_VRtrMplsS2lSubLspInterArea_Type = TruthValue
_VRtrMplsS2lSubLspInterArea_Object = MibTableColumn
vRtrMplsS2lSubLspInterArea = _VRtrMplsS2lSubLspInterArea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 38),
    _VRtrMplsS2lSubLspInterArea_Type()
)
vRtrMplsS2lSubLspInterArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspInterArea.setStatus("current")
_VRtrMplsS2lSubLspStatTable_Object = MibTable
vRtrMplsS2lSubLspStatTable = _VRtrMplsS2lSubLspStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 29)
)
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspStatTable.setStatus("current")
_VRtrMplsS2lSubLspStatEntry_Object = MibTableRow
vRtrMplsS2lSubLspStatEntry = _VRtrMplsS2lSubLspStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 29, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspStatEntry.setStatus("current")
_VRtrMplsS2lSubLspTimeUp_Type = TimeInterval
_VRtrMplsS2lSubLspTimeUp_Object = MibTableColumn
vRtrMplsS2lSubLspTimeUp = _VRtrMplsS2lSubLspTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 29, 1, 1),
    _VRtrMplsS2lSubLspTimeUp_Type()
)
vRtrMplsS2lSubLspTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTimeUp.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTimeUp.setUnits("centiseconds")
_VRtrMplsS2lSubLspTimeDown_Type = TimeInterval
_VRtrMplsS2lSubLspTimeDown_Object = MibTableColumn
vRtrMplsS2lSubLspTimeDown = _VRtrMplsS2lSubLspTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 29, 1, 2),
    _VRtrMplsS2lSubLspTimeDown_Type()
)
vRtrMplsS2lSubLspTimeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTimeDown.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTimeDown.setUnits("centiseconds")
_VRtrMplsS2lSubLspRetryAttempts_Type = Counter32
_VRtrMplsS2lSubLspRetryAttempts_Object = MibTableColumn
vRtrMplsS2lSubLspRetryAttempts = _VRtrMplsS2lSubLspRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 29, 1, 3),
    _VRtrMplsS2lSubLspRetryAttempts_Type()
)
vRtrMplsS2lSubLspRetryAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspRetryAttempts.setStatus("current")
_VRtrMplsS2lSubLspTransitionCount_Type = Counter32
_VRtrMplsS2lSubLspTransitionCount_Object = MibTableColumn
vRtrMplsS2lSubLspTransitionCount = _VRtrMplsS2lSubLspTransitionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 29, 1, 4),
    _VRtrMplsS2lSubLspTransitionCount_Type()
)
vRtrMplsS2lSubLspTransitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTransitionCount.setStatus("current")
_VRtrMplsS2lSubLspCspfQueries_Type = Counter32
_VRtrMplsS2lSubLspCspfQueries_Object = MibTableColumn
vRtrMplsS2lSubLspCspfQueries = _VRtrMplsS2lSubLspCspfQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 29, 1, 5),
    _VRtrMplsS2lSubLspCspfQueries_Type()
)
vRtrMplsS2lSubLspCspfQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspCspfQueries.setStatus("current")
_VRtrMplsSrlgDBRtrIdTblLastChg_Type = TimeStamp
_VRtrMplsSrlgDBRtrIdTblLastChg_Object = MibScalar
vRtrMplsSrlgDBRtrIdTblLastChg = _VRtrMplsSrlgDBRtrIdTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 30),
    _VRtrMplsSrlgDBRtrIdTblLastChg_Type()
)
vRtrMplsSrlgDBRtrIdTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBRtrIdTblLastChg.setStatus("current")
_VRtrMplsSrlgDBRtrIdTable_Object = MibTable
vRtrMplsSrlgDBRtrIdTable = _VRtrMplsSrlgDBRtrIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 31)
)
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBRtrIdTable.setStatus("current")
_VRtrMplsSrlgDBRtrIdEntry_Object = MibTableRow
vRtrMplsSrlgDBRtrIdEntry = _VRtrMplsSrlgDBRtrIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 31, 1)
)
vRtrMplsSrlgDBRtrIdEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBRtrIdRouterID"),
)
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBRtrIdEntry.setStatus("current")
_VRtrMplsSrlgDBRtrIdRouterID_Type = TmnxMplsRouterId
_VRtrMplsSrlgDBRtrIdRouterID_Object = MibTableColumn
vRtrMplsSrlgDBRtrIdRouterID = _VRtrMplsSrlgDBRtrIdRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 31, 1, 1),
    _VRtrMplsSrlgDBRtrIdRouterID_Type()
)
vRtrMplsSrlgDBRtrIdRouterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBRtrIdRouterID.setStatus("current")
_VRtrMplsSrlgDBRtrIdRowStatus_Type = RowStatus
_VRtrMplsSrlgDBRtrIdRowStatus_Object = MibTableColumn
vRtrMplsSrlgDBRtrIdRowStatus = _VRtrMplsSrlgDBRtrIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 31, 1, 2),
    _VRtrMplsSrlgDBRtrIdRowStatus_Type()
)
vRtrMplsSrlgDBRtrIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBRtrIdRowStatus.setStatus("current")


class _VRtrMplsSrlgDBRtrIdAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsSrlgDBRtrIdAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsSrlgDBRtrIdAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsSrlgDBRtrIdAdminState_Object = MibTableColumn
vRtrMplsSrlgDBRtrIdAdminState = _VRtrMplsSrlgDBRtrIdAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 31, 1, 3),
    _VRtrMplsSrlgDBRtrIdAdminState_Type()
)
vRtrMplsSrlgDBRtrIdAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBRtrIdAdminState.setStatus("current")
_VRtrMplsSrlgDBRtrIdLastChanged_Type = TimeStamp
_VRtrMplsSrlgDBRtrIdLastChanged_Object = MibTableColumn
vRtrMplsSrlgDBRtrIdLastChanged = _VRtrMplsSrlgDBRtrIdLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 31, 1, 4),
    _VRtrMplsSrlgDBRtrIdLastChanged_Type()
)
vRtrMplsSrlgDBRtrIdLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBRtrIdLastChanged.setStatus("current")
_VRtrMplsSrlgDBIfTblLastChanged_Type = TimeStamp
_VRtrMplsSrlgDBIfTblLastChanged_Object = MibScalar
vRtrMplsSrlgDBIfTblLastChanged = _VRtrMplsSrlgDBIfTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 32),
    _VRtrMplsSrlgDBIfTblLastChanged_Type()
)
vRtrMplsSrlgDBIfTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBIfTblLastChanged.setStatus("current")
_VRtrMplsSrlgDBIfTable_Object = MibTable
vRtrMplsSrlgDBIfTable = _VRtrMplsSrlgDBIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 33)
)
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBIfTable.setStatus("current")
_VRtrMplsSrlgDBIfEntry_Object = MibTableRow
vRtrMplsSrlgDBIfEntry = _VRtrMplsSrlgDBIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 33, 1)
)
vRtrMplsSrlgDBIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBRtrIdRouterID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBIfIntIpAddrType"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBIfIntIpAddr"),
    (1, "TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBIfSrlgGroupName"),
)
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBIfEntry.setStatus("current")
_VRtrMplsSrlgDBIfIntIpAddrType_Type = InetAddressType
_VRtrMplsSrlgDBIfIntIpAddrType_Object = MibTableColumn
vRtrMplsSrlgDBIfIntIpAddrType = _VRtrMplsSrlgDBIfIntIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 33, 1, 1),
    _VRtrMplsSrlgDBIfIntIpAddrType_Type()
)
vRtrMplsSrlgDBIfIntIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBIfIntIpAddrType.setStatus("current")


class _VRtrMplsSrlgDBIfIntIpAddr_Type(InetAddress):
    """Custom type vRtrMplsSrlgDBIfIntIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsSrlgDBIfIntIpAddr_Type.__name__ = "InetAddress"
_VRtrMplsSrlgDBIfIntIpAddr_Object = MibTableColumn
vRtrMplsSrlgDBIfIntIpAddr = _VRtrMplsSrlgDBIfIntIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 33, 1, 2),
    _VRtrMplsSrlgDBIfIntIpAddr_Type()
)
vRtrMplsSrlgDBIfIntIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBIfIntIpAddr.setStatus("current")
_VRtrMplsSrlgDBIfSrlgGroupName_Type = TNamedItem
_VRtrMplsSrlgDBIfSrlgGroupName_Object = MibTableColumn
vRtrMplsSrlgDBIfSrlgGroupName = _VRtrMplsSrlgDBIfSrlgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 33, 1, 3),
    _VRtrMplsSrlgDBIfSrlgGroupName_Type()
)
vRtrMplsSrlgDBIfSrlgGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBIfSrlgGroupName.setStatus("current")
_VRtrMplsSrlgDBIfRowStatus_Type = RowStatus
_VRtrMplsSrlgDBIfRowStatus_Object = MibTableColumn
vRtrMplsSrlgDBIfRowStatus = _VRtrMplsSrlgDBIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 33, 1, 4),
    _VRtrMplsSrlgDBIfRowStatus_Type()
)
vRtrMplsSrlgDBIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBIfRowStatus.setStatus("current")
_VRtrMplsSrlgDBIfLastChanged_Type = TimeStamp
_VRtrMplsSrlgDBIfLastChanged_Object = MibTableColumn
vRtrMplsSrlgDBIfLastChanged = _VRtrMplsSrlgDBIfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 33, 1, 5),
    _VRtrMplsSrlgDBIfLastChanged_Type()
)
vRtrMplsSrlgDBIfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBIfLastChanged.setStatus("current")
_VRtrMplsInSegmentTable_Object = MibTable
vRtrMplsInSegmentTable = _VRtrMplsInSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 34)
)
if mibBuilder.loadTexts:
    vRtrMplsInSegmentTable.setStatus("current")
_VRtrMplsInSegmentEntry_Object = MibTableRow
vRtrMplsInSegmentEntry = _VRtrMplsInSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 34, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsInSegmentEntry.setStatus("current")
_VRtrMplsInSegmentNumS2ls_Type = Unsigned32
_VRtrMplsInSegmentNumS2ls_Object = MibTableColumn
vRtrMplsInSegmentNumS2ls = _VRtrMplsInSegmentNumS2ls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 34, 1, 1),
    _VRtrMplsInSegmentNumS2ls_Type()
)
vRtrMplsInSegmentNumS2ls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInSegmentNumS2ls.setStatus("current")
_VRtrMplsOutSegmentTable_Object = MibTable
vRtrMplsOutSegmentTable = _VRtrMplsOutSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 35)
)
if mibBuilder.loadTexts:
    vRtrMplsOutSegmentTable.setStatus("current")
_VRtrMplsOutSegmentEntry_Object = MibTableRow
vRtrMplsOutSegmentEntry = _VRtrMplsOutSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 35, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsOutSegmentEntry.setStatus("current")
_VRtrMplsOutSegmentNumS2ls_Type = Unsigned32
_VRtrMplsOutSegmentNumS2ls_Object = MibTableColumn
vRtrMplsOutSegmentNumS2ls = _VRtrMplsOutSegmentNumS2ls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 35, 1, 1),
    _VRtrMplsOutSegmentNumS2ls_Type()
)
vRtrMplsOutSegmentNumS2ls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutSegmentNumS2ls.setStatus("current")
_VRtrMplsLspStatsTblLastChgd_Type = TimeStamp
_VRtrMplsLspStatsTblLastChgd_Object = MibScalar
vRtrMplsLspStatsTblLastChgd = _VRtrMplsLspStatsTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 37),
    _VRtrMplsLspStatsTblLastChgd_Type()
)
vRtrMplsLspStatsTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsTblLastChgd.setStatus("current")
_VRtrMplsLspStatsTable_Object = MibTable
vRtrMplsLspStatsTable = _VRtrMplsLspStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38)
)
if mibBuilder.loadTexts:
    vRtrMplsLspStatsTable.setStatus("current")
_VRtrMplsLspStatsEntry_Object = MibTableRow
vRtrMplsLspStatsEntry = _VRtrMplsLspStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1)
)
vRtrMplsLspStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspStatsType"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspStatsSenderAddrType"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspStatsSenderAddr"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspStatsLspName"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspStatsEntry.setStatus("current")


class _VRtrMplsLspStatsType_Type(Integer32):
    """Custom type vRtrMplsLspStatsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 0),
          ("ingress", 1),
          ("srTeEgress", 2))
    )


_VRtrMplsLspStatsType_Type.__name__ = "Integer32"
_VRtrMplsLspStatsType_Object = MibTableColumn
vRtrMplsLspStatsType = _VRtrMplsLspStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 1),
    _VRtrMplsLspStatsType_Type()
)
vRtrMplsLspStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsType.setStatus("current")
_VRtrMplsLspStatsSenderAddrType_Type = InetAddressType
_VRtrMplsLspStatsSenderAddrType_Object = MibTableColumn
vRtrMplsLspStatsSenderAddrType = _VRtrMplsLspStatsSenderAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 2),
    _VRtrMplsLspStatsSenderAddrType_Type()
)
vRtrMplsLspStatsSenderAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsSenderAddrType.setStatus("current")


class _VRtrMplsLspStatsSenderAddr_Type(InetAddress):
    """Custom type vRtrMplsLspStatsSenderAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsLspStatsSenderAddr_Type.__name__ = "InetAddress"
_VRtrMplsLspStatsSenderAddr_Object = MibTableColumn
vRtrMplsLspStatsSenderAddr = _VRtrMplsLspStatsSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 3),
    _VRtrMplsLspStatsSenderAddr_Type()
)
vRtrMplsLspStatsSenderAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsSenderAddr.setStatus("current")
_VRtrMplsLspStatsLspName_Type = TLNamedItem
_VRtrMplsLspStatsLspName_Object = MibTableColumn
vRtrMplsLspStatsLspName = _VRtrMplsLspStatsLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 4),
    _VRtrMplsLspStatsLspName_Type()
)
vRtrMplsLspStatsLspName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsLspName.setStatus("current")
_VRtrMplsLspStatsRowStatus_Type = RowStatus
_VRtrMplsLspStatsRowStatus_Object = MibTableColumn
vRtrMplsLspStatsRowStatus = _VRtrMplsLspStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 5),
    _VRtrMplsLspStatsRowStatus_Type()
)
vRtrMplsLspStatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsRowStatus.setStatus("current")
_VRtrMplsLspStatsLastChanged_Type = TimeStamp
_VRtrMplsLspStatsLastChanged_Object = MibTableColumn
vRtrMplsLspStatsLastChanged = _VRtrMplsLspStatsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 6),
    _VRtrMplsLspStatsLastChanged_Type()
)
vRtrMplsLspStatsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsLastChanged.setStatus("current")


class _VRtrMplsLspStatsCollectStats_Type(TruthValue):
    """Custom type vRtrMplsLspStatsCollectStats based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspStatsCollectStats_Type.__name__ = "TruthValue"
_VRtrMplsLspStatsCollectStats_Object = MibTableColumn
vRtrMplsLspStatsCollectStats = _VRtrMplsLspStatsCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 7),
    _VRtrMplsLspStatsCollectStats_Type()
)
vRtrMplsLspStatsCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsCollectStats.setStatus("current")


class _VRtrMplsLspStatsAccntingPolicy_Type(Unsigned32):
    """Custom type vRtrMplsLspStatsAccntingPolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 99),
    )


_VRtrMplsLspStatsAccntingPolicy_Type.__name__ = "Unsigned32"
_VRtrMplsLspStatsAccntingPolicy_Object = MibTableColumn
vRtrMplsLspStatsAccntingPolicy = _VRtrMplsLspStatsAccntingPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 8),
    _VRtrMplsLspStatsAccntingPolicy_Type()
)
vRtrMplsLspStatsAccntingPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsAccntingPolicy.setStatus("current")


class _VRtrMplsLspStatsAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsLspStatsAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsLspStatsAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsLspStatsAdminState_Object = MibTableColumn
vRtrMplsLspStatsAdminState = _VRtrMplsLspStatsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 9),
    _VRtrMplsLspStatsAdminState_Type()
)
vRtrMplsLspStatsAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsAdminState.setStatus("current")


class _VRtrMplsLspStatsMode_Type(Integer32):
    """Custom type vRtrMplsLspStatsMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("per-fc", 0),
          ("aggregate", 1))
    )


_VRtrMplsLspStatsMode_Type.__name__ = "Integer32"
_VRtrMplsLspStatsMode_Object = MibTableColumn
vRtrMplsLspStatsMode = _VRtrMplsLspStatsMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 10),
    _VRtrMplsLspStatsMode_Type()
)
vRtrMplsLspStatsMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsMode.setStatus("current")
_VRtrMplsLspStatisticsTable_Object = MibTable
vRtrMplsLspStatisticsTable = _VRtrMplsLspStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39)
)
if mibBuilder.loadTexts:
    vRtrMplsLspStatisticsTable.setStatus("current")
_VRtrMplsLspStatisticsEntry_Object = MibTableRow
vRtrMplsLspStatisticsEntry = _VRtrMplsLspStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsLspStatisticsEntry.setStatus("current")
_VRtrMplsInProfilePktsFc0_Type = Counter64
_VRtrMplsInProfilePktsFc0_Object = MibTableColumn
vRtrMplsInProfilePktsFc0 = _VRtrMplsInProfilePktsFc0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 1),
    _VRtrMplsInProfilePktsFc0_Type()
)
vRtrMplsInProfilePktsFc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc0.setStatus("current")
_VRtrMplsInProfilePktsFc0Low32_Type = Counter32
_VRtrMplsInProfilePktsFc0Low32_Object = MibTableColumn
vRtrMplsInProfilePktsFc0Low32 = _VRtrMplsInProfilePktsFc0Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 2),
    _VRtrMplsInProfilePktsFc0Low32_Type()
)
vRtrMplsInProfilePktsFc0Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc0Low32.setStatus("current")
_VRtrMplsInProfilePktsFc0High32_Type = Counter32
_VRtrMplsInProfilePktsFc0High32_Object = MibTableColumn
vRtrMplsInProfilePktsFc0High32 = _VRtrMplsInProfilePktsFc0High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 3),
    _VRtrMplsInProfilePktsFc0High32_Type()
)
vRtrMplsInProfilePktsFc0High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc0High32.setStatus("current")
_VRtrMplsInProfilePktsFc1_Type = Counter64
_VRtrMplsInProfilePktsFc1_Object = MibTableColumn
vRtrMplsInProfilePktsFc1 = _VRtrMplsInProfilePktsFc1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 4),
    _VRtrMplsInProfilePktsFc1_Type()
)
vRtrMplsInProfilePktsFc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc1.setStatus("current")
_VRtrMplsInProfilePktsFc1Low32_Type = Counter32
_VRtrMplsInProfilePktsFc1Low32_Object = MibTableColumn
vRtrMplsInProfilePktsFc1Low32 = _VRtrMplsInProfilePktsFc1Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 5),
    _VRtrMplsInProfilePktsFc1Low32_Type()
)
vRtrMplsInProfilePktsFc1Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc1Low32.setStatus("current")
_VRtrMplsInProfilePktsFc1High32_Type = Counter32
_VRtrMplsInProfilePktsFc1High32_Object = MibTableColumn
vRtrMplsInProfilePktsFc1High32 = _VRtrMplsInProfilePktsFc1High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 6),
    _VRtrMplsInProfilePktsFc1High32_Type()
)
vRtrMplsInProfilePktsFc1High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc1High32.setStatus("current")
_VRtrMplsInProfilePktsFc2_Type = Counter64
_VRtrMplsInProfilePktsFc2_Object = MibTableColumn
vRtrMplsInProfilePktsFc2 = _VRtrMplsInProfilePktsFc2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 7),
    _VRtrMplsInProfilePktsFc2_Type()
)
vRtrMplsInProfilePktsFc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc2.setStatus("current")
_VRtrMplsInProfilePktsFc2Low32_Type = Counter32
_VRtrMplsInProfilePktsFc2Low32_Object = MibTableColumn
vRtrMplsInProfilePktsFc2Low32 = _VRtrMplsInProfilePktsFc2Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 8),
    _VRtrMplsInProfilePktsFc2Low32_Type()
)
vRtrMplsInProfilePktsFc2Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc2Low32.setStatus("current")
_VRtrMplsInProfilePktsFc2High32_Type = Counter32
_VRtrMplsInProfilePktsFc2High32_Object = MibTableColumn
vRtrMplsInProfilePktsFc2High32 = _VRtrMplsInProfilePktsFc2High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 9),
    _VRtrMplsInProfilePktsFc2High32_Type()
)
vRtrMplsInProfilePktsFc2High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc2High32.setStatus("current")
_VRtrMplsInProfilePktsFc3_Type = Counter64
_VRtrMplsInProfilePktsFc3_Object = MibTableColumn
vRtrMplsInProfilePktsFc3 = _VRtrMplsInProfilePktsFc3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 10),
    _VRtrMplsInProfilePktsFc3_Type()
)
vRtrMplsInProfilePktsFc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc3.setStatus("current")
_VRtrMplsInProfilePktsFc3Low32_Type = Counter32
_VRtrMplsInProfilePktsFc3Low32_Object = MibTableColumn
vRtrMplsInProfilePktsFc3Low32 = _VRtrMplsInProfilePktsFc3Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 11),
    _VRtrMplsInProfilePktsFc3Low32_Type()
)
vRtrMplsInProfilePktsFc3Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc3Low32.setStatus("current")
_VRtrMplsInProfilePktsFc3High32_Type = Counter32
_VRtrMplsInProfilePktsFc3High32_Object = MibTableColumn
vRtrMplsInProfilePktsFc3High32 = _VRtrMplsInProfilePktsFc3High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 12),
    _VRtrMplsInProfilePktsFc3High32_Type()
)
vRtrMplsInProfilePktsFc3High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc3High32.setStatus("current")
_VRtrMplsInProfilePktsFc4_Type = Counter64
_VRtrMplsInProfilePktsFc4_Object = MibTableColumn
vRtrMplsInProfilePktsFc4 = _VRtrMplsInProfilePktsFc4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 13),
    _VRtrMplsInProfilePktsFc4_Type()
)
vRtrMplsInProfilePktsFc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc4.setStatus("current")
_VRtrMplsInProfilePktsFc4Low32_Type = Counter32
_VRtrMplsInProfilePktsFc4Low32_Object = MibTableColumn
vRtrMplsInProfilePktsFc4Low32 = _VRtrMplsInProfilePktsFc4Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 14),
    _VRtrMplsInProfilePktsFc4Low32_Type()
)
vRtrMplsInProfilePktsFc4Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc4Low32.setStatus("current")
_VRtrMplsInProfilePktsFc4High32_Type = Counter32
_VRtrMplsInProfilePktsFc4High32_Object = MibTableColumn
vRtrMplsInProfilePktsFc4High32 = _VRtrMplsInProfilePktsFc4High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 15),
    _VRtrMplsInProfilePktsFc4High32_Type()
)
vRtrMplsInProfilePktsFc4High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc4High32.setStatus("current")
_VRtrMplsInProfilePktsFc5_Type = Counter64
_VRtrMplsInProfilePktsFc5_Object = MibTableColumn
vRtrMplsInProfilePktsFc5 = _VRtrMplsInProfilePktsFc5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 16),
    _VRtrMplsInProfilePktsFc5_Type()
)
vRtrMplsInProfilePktsFc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc5.setStatus("current")
_VRtrMplsInProfilePktsFc5Low32_Type = Counter32
_VRtrMplsInProfilePktsFc5Low32_Object = MibTableColumn
vRtrMplsInProfilePktsFc5Low32 = _VRtrMplsInProfilePktsFc5Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 17),
    _VRtrMplsInProfilePktsFc5Low32_Type()
)
vRtrMplsInProfilePktsFc5Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc5Low32.setStatus("current")
_VRtrMplsInProfilePktsFc5High32_Type = Counter32
_VRtrMplsInProfilePktsFc5High32_Object = MibTableColumn
vRtrMplsInProfilePktsFc5High32 = _VRtrMplsInProfilePktsFc5High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 18),
    _VRtrMplsInProfilePktsFc5High32_Type()
)
vRtrMplsInProfilePktsFc5High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc5High32.setStatus("current")
_VRtrMplsInProfilePktsFc6_Type = Counter64
_VRtrMplsInProfilePktsFc6_Object = MibTableColumn
vRtrMplsInProfilePktsFc6 = _VRtrMplsInProfilePktsFc6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 19),
    _VRtrMplsInProfilePktsFc6_Type()
)
vRtrMplsInProfilePktsFc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc6.setStatus("current")
_VRtrMplsInProfilePktsFc6Low32_Type = Counter32
_VRtrMplsInProfilePktsFc6Low32_Object = MibTableColumn
vRtrMplsInProfilePktsFc6Low32 = _VRtrMplsInProfilePktsFc6Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 20),
    _VRtrMplsInProfilePktsFc6Low32_Type()
)
vRtrMplsInProfilePktsFc6Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc6Low32.setStatus("current")
_VRtrMplsInProfilePktsFc6High32_Type = Counter32
_VRtrMplsInProfilePktsFc6High32_Object = MibTableColumn
vRtrMplsInProfilePktsFc6High32 = _VRtrMplsInProfilePktsFc6High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 21),
    _VRtrMplsInProfilePktsFc6High32_Type()
)
vRtrMplsInProfilePktsFc6High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc6High32.setStatus("current")
_VRtrMplsInProfilePktsFc7_Type = Counter64
_VRtrMplsInProfilePktsFc7_Object = MibTableColumn
vRtrMplsInProfilePktsFc7 = _VRtrMplsInProfilePktsFc7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 22),
    _VRtrMplsInProfilePktsFc7_Type()
)
vRtrMplsInProfilePktsFc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc7.setStatus("current")
_VRtrMplsInProfilePktsFc7Low32_Type = Counter32
_VRtrMplsInProfilePktsFc7Low32_Object = MibTableColumn
vRtrMplsInProfilePktsFc7Low32 = _VRtrMplsInProfilePktsFc7Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 23),
    _VRtrMplsInProfilePktsFc7Low32_Type()
)
vRtrMplsInProfilePktsFc7Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc7Low32.setStatus("current")
_VRtrMplsInProfilePktsFc7High32_Type = Counter32
_VRtrMplsInProfilePktsFc7High32_Object = MibTableColumn
vRtrMplsInProfilePktsFc7High32 = _VRtrMplsInProfilePktsFc7High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 24),
    _VRtrMplsInProfilePktsFc7High32_Type()
)
vRtrMplsInProfilePktsFc7High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc7High32.setStatus("current")
_VRtrMplsInProfileOctetsFc0_Type = Counter64
_VRtrMplsInProfileOctetsFc0_Object = MibTableColumn
vRtrMplsInProfileOctetsFc0 = _VRtrMplsInProfileOctetsFc0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 25),
    _VRtrMplsInProfileOctetsFc0_Type()
)
vRtrMplsInProfileOctetsFc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc0.setStatus("current")
_VRtrMplsInProfileOctetsFc0Low32_Type = Counter32
_VRtrMplsInProfileOctetsFc0Low32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc0Low32 = _VRtrMplsInProfileOctetsFc0Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 26),
    _VRtrMplsInProfileOctetsFc0Low32_Type()
)
vRtrMplsInProfileOctetsFc0Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc0Low32.setStatus("current")
_VRtrMplsInProfileOctetsFc0High32_Type = Counter32
_VRtrMplsInProfileOctetsFc0High32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc0High32 = _VRtrMplsInProfileOctetsFc0High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 27),
    _VRtrMplsInProfileOctetsFc0High32_Type()
)
vRtrMplsInProfileOctetsFc0High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc0High32.setStatus("current")
_VRtrMplsInProfileOctetsFc1_Type = Counter64
_VRtrMplsInProfileOctetsFc1_Object = MibTableColumn
vRtrMplsInProfileOctetsFc1 = _VRtrMplsInProfileOctetsFc1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 28),
    _VRtrMplsInProfileOctetsFc1_Type()
)
vRtrMplsInProfileOctetsFc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc1.setStatus("current")
_VRtrMplsInProfileOctetsFc1Low32_Type = Counter32
_VRtrMplsInProfileOctetsFc1Low32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc1Low32 = _VRtrMplsInProfileOctetsFc1Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 29),
    _VRtrMplsInProfileOctetsFc1Low32_Type()
)
vRtrMplsInProfileOctetsFc1Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc1Low32.setStatus("current")
_VRtrMplsInProfileOctetsFc1High32_Type = Counter32
_VRtrMplsInProfileOctetsFc1High32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc1High32 = _VRtrMplsInProfileOctetsFc1High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 30),
    _VRtrMplsInProfileOctetsFc1High32_Type()
)
vRtrMplsInProfileOctetsFc1High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc1High32.setStatus("current")
_VRtrMplsInProfileOctetsFc2_Type = Counter64
_VRtrMplsInProfileOctetsFc2_Object = MibTableColumn
vRtrMplsInProfileOctetsFc2 = _VRtrMplsInProfileOctetsFc2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 31),
    _VRtrMplsInProfileOctetsFc2_Type()
)
vRtrMplsInProfileOctetsFc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc2.setStatus("current")
_VRtrMplsInProfileOctetsFc2Low32_Type = Counter32
_VRtrMplsInProfileOctetsFc2Low32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc2Low32 = _VRtrMplsInProfileOctetsFc2Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 32),
    _VRtrMplsInProfileOctetsFc2Low32_Type()
)
vRtrMplsInProfileOctetsFc2Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc2Low32.setStatus("current")
_VRtrMplsInProfileOctetsFc2High32_Type = Counter32
_VRtrMplsInProfileOctetsFc2High32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc2High32 = _VRtrMplsInProfileOctetsFc2High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 33),
    _VRtrMplsInProfileOctetsFc2High32_Type()
)
vRtrMplsInProfileOctetsFc2High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc2High32.setStatus("current")
_VRtrMplsInProfileOctetsFc3_Type = Counter64
_VRtrMplsInProfileOctetsFc3_Object = MibTableColumn
vRtrMplsInProfileOctetsFc3 = _VRtrMplsInProfileOctetsFc3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 34),
    _VRtrMplsInProfileOctetsFc3_Type()
)
vRtrMplsInProfileOctetsFc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc3.setStatus("current")
_VRtrMplsInProfileOctetsFc3Low32_Type = Counter32
_VRtrMplsInProfileOctetsFc3Low32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc3Low32 = _VRtrMplsInProfileOctetsFc3Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 35),
    _VRtrMplsInProfileOctetsFc3Low32_Type()
)
vRtrMplsInProfileOctetsFc3Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc3Low32.setStatus("current")
_VRtrMplsInProfileOctetsFc3High32_Type = Counter32
_VRtrMplsInProfileOctetsFc3High32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc3High32 = _VRtrMplsInProfileOctetsFc3High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 36),
    _VRtrMplsInProfileOctetsFc3High32_Type()
)
vRtrMplsInProfileOctetsFc3High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc3High32.setStatus("current")
_VRtrMplsInProfileOctetsFc4_Type = Counter64
_VRtrMplsInProfileOctetsFc4_Object = MibTableColumn
vRtrMplsInProfileOctetsFc4 = _VRtrMplsInProfileOctetsFc4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 37),
    _VRtrMplsInProfileOctetsFc4_Type()
)
vRtrMplsInProfileOctetsFc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc4.setStatus("current")
_VRtrMplsInProfileOctetsFc4Low32_Type = Counter32
_VRtrMplsInProfileOctetsFc4Low32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc4Low32 = _VRtrMplsInProfileOctetsFc4Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 38),
    _VRtrMplsInProfileOctetsFc4Low32_Type()
)
vRtrMplsInProfileOctetsFc4Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc4Low32.setStatus("current")
_VRtrMplsInProfileOctetsFc4High32_Type = Counter32
_VRtrMplsInProfileOctetsFc4High32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc4High32 = _VRtrMplsInProfileOctetsFc4High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 39),
    _VRtrMplsInProfileOctetsFc4High32_Type()
)
vRtrMplsInProfileOctetsFc4High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc4High32.setStatus("current")
_VRtrMplsInProfileOctetsFc5_Type = Counter64
_VRtrMplsInProfileOctetsFc5_Object = MibTableColumn
vRtrMplsInProfileOctetsFc5 = _VRtrMplsInProfileOctetsFc5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 40),
    _VRtrMplsInProfileOctetsFc5_Type()
)
vRtrMplsInProfileOctetsFc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc5.setStatus("current")
_VRtrMplsInProfileOctetsFc5Low32_Type = Counter32
_VRtrMplsInProfileOctetsFc5Low32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc5Low32 = _VRtrMplsInProfileOctetsFc5Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 41),
    _VRtrMplsInProfileOctetsFc5Low32_Type()
)
vRtrMplsInProfileOctetsFc5Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc5Low32.setStatus("current")
_VRtrMplsInProfileOctetsFc5High32_Type = Counter32
_VRtrMplsInProfileOctetsFc5High32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc5High32 = _VRtrMplsInProfileOctetsFc5High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 42),
    _VRtrMplsInProfileOctetsFc5High32_Type()
)
vRtrMplsInProfileOctetsFc5High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc5High32.setStatus("current")
_VRtrMplsInProfileOctetsFc6_Type = Counter64
_VRtrMplsInProfileOctetsFc6_Object = MibTableColumn
vRtrMplsInProfileOctetsFc6 = _VRtrMplsInProfileOctetsFc6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 43),
    _VRtrMplsInProfileOctetsFc6_Type()
)
vRtrMplsInProfileOctetsFc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc6.setStatus("current")
_VRtrMplsInProfileOctetsFc6Low32_Type = Counter32
_VRtrMplsInProfileOctetsFc6Low32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc6Low32 = _VRtrMplsInProfileOctetsFc6Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 44),
    _VRtrMplsInProfileOctetsFc6Low32_Type()
)
vRtrMplsInProfileOctetsFc6Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc6Low32.setStatus("current")
_VRtrMplsInProfileOctetsFc6High32_Type = Counter32
_VRtrMplsInProfileOctetsFc6High32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc6High32 = _VRtrMplsInProfileOctetsFc6High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 45),
    _VRtrMplsInProfileOctetsFc6High32_Type()
)
vRtrMplsInProfileOctetsFc6High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc6High32.setStatus("current")
_VRtrMplsInProfileOctetsFc7_Type = Counter64
_VRtrMplsInProfileOctetsFc7_Object = MibTableColumn
vRtrMplsInProfileOctetsFc7 = _VRtrMplsInProfileOctetsFc7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 46),
    _VRtrMplsInProfileOctetsFc7_Type()
)
vRtrMplsInProfileOctetsFc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc7.setStatus("current")
_VRtrMplsInProfileOctetsFc7Low32_Type = Counter32
_VRtrMplsInProfileOctetsFc7Low32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc7Low32 = _VRtrMplsInProfileOctetsFc7Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 47),
    _VRtrMplsInProfileOctetsFc7Low32_Type()
)
vRtrMplsInProfileOctetsFc7Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc7Low32.setStatus("current")
_VRtrMplsInProfileOctetsFc7High32_Type = Counter32
_VRtrMplsInProfileOctetsFc7High32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc7High32 = _VRtrMplsInProfileOctetsFc7High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 48),
    _VRtrMplsInProfileOctetsFc7High32_Type()
)
vRtrMplsInProfileOctetsFc7High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc7High32.setStatus("current")
_VRtrMplsOutOfProfPktsFc0_Type = Counter64
_VRtrMplsOutOfProfPktsFc0_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc0 = _VRtrMplsOutOfProfPktsFc0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 49),
    _VRtrMplsOutOfProfPktsFc0_Type()
)
vRtrMplsOutOfProfPktsFc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc0.setStatus("current")
_VRtrMplsOutOfProfPktsFc0Low32_Type = Counter32
_VRtrMplsOutOfProfPktsFc0Low32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc0Low32 = _VRtrMplsOutOfProfPktsFc0Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 50),
    _VRtrMplsOutOfProfPktsFc0Low32_Type()
)
vRtrMplsOutOfProfPktsFc0Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc0Low32.setStatus("current")
_VRtrMplsOutOfProfPktsFc0High32_Type = Counter32
_VRtrMplsOutOfProfPktsFc0High32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc0High32 = _VRtrMplsOutOfProfPktsFc0High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 51),
    _VRtrMplsOutOfProfPktsFc0High32_Type()
)
vRtrMplsOutOfProfPktsFc0High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc0High32.setStatus("current")
_VRtrMplsOutOfProfPktsFc1_Type = Counter64
_VRtrMplsOutOfProfPktsFc1_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc1 = _VRtrMplsOutOfProfPktsFc1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 52),
    _VRtrMplsOutOfProfPktsFc1_Type()
)
vRtrMplsOutOfProfPktsFc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc1.setStatus("current")
_VRtrMplsOutOfProfPktsFc1Low32_Type = Counter32
_VRtrMplsOutOfProfPktsFc1Low32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc1Low32 = _VRtrMplsOutOfProfPktsFc1Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 53),
    _VRtrMplsOutOfProfPktsFc1Low32_Type()
)
vRtrMplsOutOfProfPktsFc1Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc1Low32.setStatus("current")
_VRtrMplsOutOfProfPktsFc1High32_Type = Counter32
_VRtrMplsOutOfProfPktsFc1High32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc1High32 = _VRtrMplsOutOfProfPktsFc1High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 54),
    _VRtrMplsOutOfProfPktsFc1High32_Type()
)
vRtrMplsOutOfProfPktsFc1High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc1High32.setStatus("current")
_VRtrMplsOutOfProfPktsFc2_Type = Counter64
_VRtrMplsOutOfProfPktsFc2_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc2 = _VRtrMplsOutOfProfPktsFc2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 55),
    _VRtrMplsOutOfProfPktsFc2_Type()
)
vRtrMplsOutOfProfPktsFc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc2.setStatus("current")
_VRtrMplsOutOfProfPktsFc2Low32_Type = Counter32
_VRtrMplsOutOfProfPktsFc2Low32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc2Low32 = _VRtrMplsOutOfProfPktsFc2Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 56),
    _VRtrMplsOutOfProfPktsFc2Low32_Type()
)
vRtrMplsOutOfProfPktsFc2Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc2Low32.setStatus("current")
_VRtrMplsOutOfProfPktsFc2High32_Type = Counter32
_VRtrMplsOutOfProfPktsFc2High32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc2High32 = _VRtrMplsOutOfProfPktsFc2High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 57),
    _VRtrMplsOutOfProfPktsFc2High32_Type()
)
vRtrMplsOutOfProfPktsFc2High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc2High32.setStatus("current")
_VRtrMplsOutOfProfPktsFc3_Type = Counter64
_VRtrMplsOutOfProfPktsFc3_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc3 = _VRtrMplsOutOfProfPktsFc3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 58),
    _VRtrMplsOutOfProfPktsFc3_Type()
)
vRtrMplsOutOfProfPktsFc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc3.setStatus("current")
_VRtrMplsOutOfProfPktsFc3Low32_Type = Counter32
_VRtrMplsOutOfProfPktsFc3Low32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc3Low32 = _VRtrMplsOutOfProfPktsFc3Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 59),
    _VRtrMplsOutOfProfPktsFc3Low32_Type()
)
vRtrMplsOutOfProfPktsFc3Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc3Low32.setStatus("current")
_VRtrMplsOutOfProfPktsFc3High32_Type = Counter32
_VRtrMplsOutOfProfPktsFc3High32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc3High32 = _VRtrMplsOutOfProfPktsFc3High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 60),
    _VRtrMplsOutOfProfPktsFc3High32_Type()
)
vRtrMplsOutOfProfPktsFc3High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc3High32.setStatus("current")
_VRtrMplsOutOfProfPktsFc4_Type = Counter64
_VRtrMplsOutOfProfPktsFc4_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc4 = _VRtrMplsOutOfProfPktsFc4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 61),
    _VRtrMplsOutOfProfPktsFc4_Type()
)
vRtrMplsOutOfProfPktsFc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc4.setStatus("current")
_VRtrMplsOutOfProfPktsFc4Low32_Type = Counter32
_VRtrMplsOutOfProfPktsFc4Low32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc4Low32 = _VRtrMplsOutOfProfPktsFc4Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 62),
    _VRtrMplsOutOfProfPktsFc4Low32_Type()
)
vRtrMplsOutOfProfPktsFc4Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc4Low32.setStatus("current")
_VRtrMplsOutOfProfPktsFc4High32_Type = Counter32
_VRtrMplsOutOfProfPktsFc4High32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc4High32 = _VRtrMplsOutOfProfPktsFc4High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 63),
    _VRtrMplsOutOfProfPktsFc4High32_Type()
)
vRtrMplsOutOfProfPktsFc4High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc4High32.setStatus("current")
_VRtrMplsOutOfProfPktsFc5_Type = Counter64
_VRtrMplsOutOfProfPktsFc5_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc5 = _VRtrMplsOutOfProfPktsFc5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 64),
    _VRtrMplsOutOfProfPktsFc5_Type()
)
vRtrMplsOutOfProfPktsFc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc5.setStatus("current")
_VRtrMplsOutOfProfPktsFc5Low32_Type = Counter32
_VRtrMplsOutOfProfPktsFc5Low32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc5Low32 = _VRtrMplsOutOfProfPktsFc5Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 65),
    _VRtrMplsOutOfProfPktsFc5Low32_Type()
)
vRtrMplsOutOfProfPktsFc5Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc5Low32.setStatus("current")
_VRtrMplsOutOfProfPktsFc5High32_Type = Counter32
_VRtrMplsOutOfProfPktsFc5High32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc5High32 = _VRtrMplsOutOfProfPktsFc5High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 66),
    _VRtrMplsOutOfProfPktsFc5High32_Type()
)
vRtrMplsOutOfProfPktsFc5High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc5High32.setStatus("current")
_VRtrMplsOutOfProfPktsFc6_Type = Counter64
_VRtrMplsOutOfProfPktsFc6_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc6 = _VRtrMplsOutOfProfPktsFc6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 67),
    _VRtrMplsOutOfProfPktsFc6_Type()
)
vRtrMplsOutOfProfPktsFc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc6.setStatus("current")
_VRtrMplsOutOfProfPktsFc6Low32_Type = Counter32
_VRtrMplsOutOfProfPktsFc6Low32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc6Low32 = _VRtrMplsOutOfProfPktsFc6Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 68),
    _VRtrMplsOutOfProfPktsFc6Low32_Type()
)
vRtrMplsOutOfProfPktsFc6Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc6Low32.setStatus("current")
_VRtrMplsOutOfProfPktsFc6High32_Type = Counter32
_VRtrMplsOutOfProfPktsFc6High32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc6High32 = _VRtrMplsOutOfProfPktsFc6High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 69),
    _VRtrMplsOutOfProfPktsFc6High32_Type()
)
vRtrMplsOutOfProfPktsFc6High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc6High32.setStatus("current")
_VRtrMplsOutOfProfPktsFc7_Type = Counter64
_VRtrMplsOutOfProfPktsFc7_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc7 = _VRtrMplsOutOfProfPktsFc7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 70),
    _VRtrMplsOutOfProfPktsFc7_Type()
)
vRtrMplsOutOfProfPktsFc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc7.setStatus("current")
_VRtrMplsOutOfProfPktsFc7Low32_Type = Counter32
_VRtrMplsOutOfProfPktsFc7Low32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc7Low32 = _VRtrMplsOutOfProfPktsFc7Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 71),
    _VRtrMplsOutOfProfPktsFc7Low32_Type()
)
vRtrMplsOutOfProfPktsFc7Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc7Low32.setStatus("current")
_VRtrMplsOutOfProfPktsFc7High32_Type = Counter32
_VRtrMplsOutOfProfPktsFc7High32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc7High32 = _VRtrMplsOutOfProfPktsFc7High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 72),
    _VRtrMplsOutOfProfPktsFc7High32_Type()
)
vRtrMplsOutOfProfPktsFc7High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc7High32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc0_Type = Counter64
_VRtrMplsOutOfProfOctetsFc0_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc0 = _VRtrMplsOutOfProfOctetsFc0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 73),
    _VRtrMplsOutOfProfOctetsFc0_Type()
)
vRtrMplsOutOfProfOctetsFc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc0.setStatus("current")
_VRtrMplsOutOfProfOctetsFc0Low32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc0Low32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc0Low32 = _VRtrMplsOutOfProfOctetsFc0Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 74),
    _VRtrMplsOutOfProfOctetsFc0Low32_Type()
)
vRtrMplsOutOfProfOctetsFc0Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc0Low32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc0High32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc0High32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc0High32 = _VRtrMplsOutOfProfOctetsFc0High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 75),
    _VRtrMplsOutOfProfOctetsFc0High32_Type()
)
vRtrMplsOutOfProfOctetsFc0High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc0High32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc1_Type = Counter64
_VRtrMplsOutOfProfOctetsFc1_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc1 = _VRtrMplsOutOfProfOctetsFc1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 76),
    _VRtrMplsOutOfProfOctetsFc1_Type()
)
vRtrMplsOutOfProfOctetsFc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc1.setStatus("current")
_VRtrMplsOutOfProfOctetsFc1Low32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc1Low32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc1Low32 = _VRtrMplsOutOfProfOctetsFc1Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 77),
    _VRtrMplsOutOfProfOctetsFc1Low32_Type()
)
vRtrMplsOutOfProfOctetsFc1Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc1Low32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc1High32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc1High32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc1High32 = _VRtrMplsOutOfProfOctetsFc1High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 78),
    _VRtrMplsOutOfProfOctetsFc1High32_Type()
)
vRtrMplsOutOfProfOctetsFc1High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc1High32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc2_Type = Counter64
_VRtrMplsOutOfProfOctetsFc2_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc2 = _VRtrMplsOutOfProfOctetsFc2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 79),
    _VRtrMplsOutOfProfOctetsFc2_Type()
)
vRtrMplsOutOfProfOctetsFc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc2.setStatus("current")
_VRtrMplsOutOfProfOctetsFc2Low32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc2Low32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc2Low32 = _VRtrMplsOutOfProfOctetsFc2Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 80),
    _VRtrMplsOutOfProfOctetsFc2Low32_Type()
)
vRtrMplsOutOfProfOctetsFc2Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc2Low32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc2High32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc2High32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc2High32 = _VRtrMplsOutOfProfOctetsFc2High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 81),
    _VRtrMplsOutOfProfOctetsFc2High32_Type()
)
vRtrMplsOutOfProfOctetsFc2High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc2High32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc3_Type = Counter64
_VRtrMplsOutOfProfOctetsFc3_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc3 = _VRtrMplsOutOfProfOctetsFc3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 82),
    _VRtrMplsOutOfProfOctetsFc3_Type()
)
vRtrMplsOutOfProfOctetsFc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc3.setStatus("current")
_VRtrMplsOutOfProfOctetsFc3Low32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc3Low32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc3Low32 = _VRtrMplsOutOfProfOctetsFc3Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 83),
    _VRtrMplsOutOfProfOctetsFc3Low32_Type()
)
vRtrMplsOutOfProfOctetsFc3Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc3Low32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc3High32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc3High32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc3High32 = _VRtrMplsOutOfProfOctetsFc3High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 84),
    _VRtrMplsOutOfProfOctetsFc3High32_Type()
)
vRtrMplsOutOfProfOctetsFc3High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc3High32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc4_Type = Counter64
_VRtrMplsOutOfProfOctetsFc4_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc4 = _VRtrMplsOutOfProfOctetsFc4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 85),
    _VRtrMplsOutOfProfOctetsFc4_Type()
)
vRtrMplsOutOfProfOctetsFc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc4.setStatus("current")
_VRtrMplsOutOfProfOctetsFc4Low32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc4Low32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc4Low32 = _VRtrMplsOutOfProfOctetsFc4Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 86),
    _VRtrMplsOutOfProfOctetsFc4Low32_Type()
)
vRtrMplsOutOfProfOctetsFc4Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc4Low32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc4High32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc4High32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc4High32 = _VRtrMplsOutOfProfOctetsFc4High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 87),
    _VRtrMplsOutOfProfOctetsFc4High32_Type()
)
vRtrMplsOutOfProfOctetsFc4High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc4High32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc5_Type = Counter64
_VRtrMplsOutOfProfOctetsFc5_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc5 = _VRtrMplsOutOfProfOctetsFc5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 88),
    _VRtrMplsOutOfProfOctetsFc5_Type()
)
vRtrMplsOutOfProfOctetsFc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc5.setStatus("current")
_VRtrMplsOutOfProfOctetsFc5Low32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc5Low32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc5Low32 = _VRtrMplsOutOfProfOctetsFc5Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 89),
    _VRtrMplsOutOfProfOctetsFc5Low32_Type()
)
vRtrMplsOutOfProfOctetsFc5Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc5Low32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc5High32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc5High32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc5High32 = _VRtrMplsOutOfProfOctetsFc5High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 90),
    _VRtrMplsOutOfProfOctetsFc5High32_Type()
)
vRtrMplsOutOfProfOctetsFc5High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc5High32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc6_Type = Counter64
_VRtrMplsOutOfProfOctetsFc6_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc6 = _VRtrMplsOutOfProfOctetsFc6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 91),
    _VRtrMplsOutOfProfOctetsFc6_Type()
)
vRtrMplsOutOfProfOctetsFc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc6.setStatus("current")
_VRtrMplsOutOfProfOctetsFc6Low32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc6Low32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc6Low32 = _VRtrMplsOutOfProfOctetsFc6Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 92),
    _VRtrMplsOutOfProfOctetsFc6Low32_Type()
)
vRtrMplsOutOfProfOctetsFc6Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc6Low32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc6High32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc6High32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc6High32 = _VRtrMplsOutOfProfOctetsFc6High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 93),
    _VRtrMplsOutOfProfOctetsFc6High32_Type()
)
vRtrMplsOutOfProfOctetsFc6High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc6High32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc7_Type = Counter64
_VRtrMplsOutOfProfOctetsFc7_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc7 = _VRtrMplsOutOfProfOctetsFc7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 94),
    _VRtrMplsOutOfProfOctetsFc7_Type()
)
vRtrMplsOutOfProfOctetsFc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc7.setStatus("current")
_VRtrMplsOutOfProfOctetsFc7Low32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc7Low32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc7Low32 = _VRtrMplsOutOfProfOctetsFc7Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 95),
    _VRtrMplsOutOfProfOctetsFc7Low32_Type()
)
vRtrMplsOutOfProfOctetsFc7Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc7Low32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc7High32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc7High32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc7High32 = _VRtrMplsOutOfProfOctetsFc7High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 96),
    _VRtrMplsOutOfProfOctetsFc7High32_Type()
)
vRtrMplsOutOfProfOctetsFc7High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc7High32.setStatus("current")
_VRtrMplsLspStatsPSBMatch_Type = TruthValue
_VRtrMplsLspStatsPSBMatch_Object = MibTableColumn
vRtrMplsLspStatsPSBMatch = _VRtrMplsLspStatsPSBMatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 97),
    _VRtrMplsLspStatsPSBMatch_Type()
)
vRtrMplsLspStatsPSBMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsPSBMatch.setStatus("current")
_VRtrMplsLspStatsTpOnly_Type = TruthValue
_VRtrMplsLspStatsTpOnly_Object = MibTableColumn
vRtrMplsLspStatsTpOnly = _VRtrMplsLspStatsTpOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 98),
    _VRtrMplsLspStatsTpOnly_Type()
)
vRtrMplsLspStatsTpOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsTpOnly.setStatus("current")


class _VRtrMplsLspStatsLspType_Type(Integer32):
    """Custom type vRtrMplsLspStatsLspType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("p2p", 1),
          ("p2mp", 2),
          ("autoP2p", 3),
          ("autoP2mp", 4),
          ("tpLsp", 5),
          ("srTe", 6),
          ("autoSrTe", 7),
          ("pceInitSrTe", 8))
    )


_VRtrMplsLspStatsLspType_Type.__name__ = "Integer32"
_VRtrMplsLspStatsLspType_Object = MibTableColumn
vRtrMplsLspStatsLspType = _VRtrMplsLspStatsLspType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 99),
    _VRtrMplsLspStatsLspType_Type()
)
vRtrMplsLspStatsLspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsLspType.setStatus("current")
_VRtrMplsLspAggregatePkts_Type = Counter64
_VRtrMplsLspAggregatePkts_Object = MibTableColumn
vRtrMplsLspAggregatePkts = _VRtrMplsLspAggregatePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 100),
    _VRtrMplsLspAggregatePkts_Type()
)
vRtrMplsLspAggregatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAggregatePkts.setStatus("current")
_VRtrMplsLspAggregateOctets_Type = Counter64
_VRtrMplsLspAggregateOctets_Object = MibTableColumn
vRtrMplsLspAggregateOctets = _VRtrMplsLspAggregateOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 101),
    _VRtrMplsLspAggregateOctets_Type()
)
vRtrMplsLspAggregateOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAggregateOctets.setStatus("current")
_VRtrMplsLspStatsAggregateOnly_Type = TruthValue
_VRtrMplsLspStatsAggregateOnly_Object = MibTableColumn
vRtrMplsLspStatsAggregateOnly = _VRtrMplsLspStatsAggregateOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 102),
    _VRtrMplsLspStatsAggregateOnly_Type()
)
vRtrMplsLspStatsAggregateOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsAggregateOnly.setStatus("current")
_VRtrMplsLspStatsRateEnabled_Type = TruthValue
_VRtrMplsLspStatsRateEnabled_Object = MibTableColumn
vRtrMplsLspStatsRateEnabled = _VRtrMplsLspStatsRateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 103),
    _VRtrMplsLspStatsRateEnabled_Type()
)
vRtrMplsLspStatsRateEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsRateEnabled.setStatus("current")
_VRtrMplsLspStatsRatePkts_Type = Unsigned32
_VRtrMplsLspStatsRatePkts_Object = MibTableColumn
vRtrMplsLspStatsRatePkts = _VRtrMplsLspStatsRatePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 104),
    _VRtrMplsLspStatsRatePkts_Type()
)
vRtrMplsLspStatsRatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsRatePkts.setStatus("current")
_VRtrMplsLspStatsRateMbps_Type = Unsigned32
_VRtrMplsLspStatsRateMbps_Object = MibTableColumn
vRtrMplsLspStatsRateMbps = _VRtrMplsLspStatsRateMbps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 105),
    _VRtrMplsLspStatsRateMbps_Type()
)
vRtrMplsLspStatsRateMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsRateMbps.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsRateMbps.setUnits("megabps")
_VRtrMplsLspTemplateTblLastChgd_Type = TimeStamp
_VRtrMplsLspTemplateTblLastChgd_Object = MibScalar
vRtrMplsLspTemplateTblLastChgd = _VRtrMplsLspTemplateTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 40),
    _VRtrMplsLspTemplateTblLastChgd_Type()
)
vRtrMplsLspTemplateTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateTblLastChgd.setStatus("current")
_VRtrMplsLspTemplateTable_Object = MibTable
vRtrMplsLspTemplateTable = _VRtrMplsLspTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41)
)
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateTable.setStatus("current")
_VRtrMplsLspTemplateEntry_Object = MibTableRow
vRtrMplsLspTemplateEntry = _VRtrMplsLspTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1)
)
vRtrMplsLspTemplateEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateName"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateEntry.setStatus("current")
_VRtrMplsLspTemplateName_Type = TNamedItem
_VRtrMplsLspTemplateName_Object = MibTableColumn
vRtrMplsLspTemplateName = _VRtrMplsLspTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 1),
    _VRtrMplsLspTemplateName_Type()
)
vRtrMplsLspTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateName.setStatus("current")
_VRtrMplsLspTemplateRowStatus_Type = RowStatus
_VRtrMplsLspTemplateRowStatus_Object = MibTableColumn
vRtrMplsLspTemplateRowStatus = _VRtrMplsLspTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 2),
    _VRtrMplsLspTemplateRowStatus_Type()
)
vRtrMplsLspTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateRowStatus.setStatus("current")
_VRtrMplsLspTemplateLastChanged_Type = TimeStamp
_VRtrMplsLspTemplateLastChanged_Object = MibTableColumn
vRtrMplsLspTemplateLastChanged = _VRtrMplsLspTemplateLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 3),
    _VRtrMplsLspTemplateLastChanged_Type()
)
vRtrMplsLspTemplateLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateLastChanged.setStatus("current")


class _VRtrMplsLspTemplateAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsLspTemplateAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsLspTemplateAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsLspTemplateAdminState_Object = MibTableColumn
vRtrMplsLspTemplateAdminState = _VRtrMplsLspTemplateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 4),
    _VRtrMplsLspTemplateAdminState_Type()
)
vRtrMplsLspTemplateAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateAdminState.setStatus("current")


class _VRtrMplsLspTemplateType_Type(Integer32):
    """Custom type vRtrMplsLspTemplateType based on Integer32"""
    defaultValue = 0

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("p2mp", 1),
          ("onehopP2P", 2),
          ("meshP2P", 3),
          ("onehopP2PSrTe", 4),
          ("meshP2PSrTe", 5),
          ("pceInitP2PSrTe", 6),
          ("onDemandP2pSrTe", 8))
    )


_VRtrMplsLspTemplateType_Type.__name__ = "Integer32"
_VRtrMplsLspTemplateType_Object = MibTableColumn
vRtrMplsLspTemplateType = _VRtrMplsLspTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 5),
    _VRtrMplsLspTemplateType_Type()
)
vRtrMplsLspTemplateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateType.setStatus("current")


class _VRtrMplsLspTemplateAdaptive_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateAdaptive based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspTemplateAdaptive_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateAdaptive_Object = MibTableColumn
vRtrMplsLspTemplateAdaptive = _VRtrMplsLspTemplateAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 6),
    _VRtrMplsLspTemplateAdaptive_Type()
)
vRtrMplsLspTemplateAdaptive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateAdaptive.setStatus("current")


class _VRtrMplsLspTemplateBandwidth_Type(Integer32):
    """Custom type vRtrMplsLspTemplateBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6400000),
    )


_VRtrMplsLspTemplateBandwidth_Type.__name__ = "Integer32"
_VRtrMplsLspTemplateBandwidth_Object = MibTableColumn
vRtrMplsLspTemplateBandwidth = _VRtrMplsLspTemplateBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 7),
    _VRtrMplsLspTemplateBandwidth_Type()
)
vRtrMplsLspTemplateBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateBandwidth.setUnits("megabps")


class _VRtrMplsLspTemplateCspf_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateCspf based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTemplateCspf_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateCspf_Object = MibTableColumn
vRtrMplsLspTemplateCspf = _VRtrMplsLspTemplateCspf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 8),
    _VRtrMplsLspTemplateCspf_Type()
)
vRtrMplsLspTemplateCspf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateCspf.setStatus("obsolete")


class _VRtrMplsLspTemplateDefaultPath_Type(MplsTunnelIndex):
    """Custom type vRtrMplsLspTemplateDefaultPath based on MplsTunnelIndex"""
    defaultValue = 0


_VRtrMplsLspTemplateDefaultPath_Type.__name__ = "MplsTunnelIndex"
_VRtrMplsLspTemplateDefaultPath_Object = MibTableColumn
vRtrMplsLspTemplateDefaultPath = _VRtrMplsLspTemplateDefaultPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 9),
    _VRtrMplsLspTemplateDefaultPath_Type()
)
vRtrMplsLspTemplateDefaultPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateDefaultPath.setStatus("current")


class _VRtrMplsLspTemplateAdmGrpIncl_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateAdmGrpIncl based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspTemplateAdmGrpIncl_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateAdmGrpIncl_Object = MibTableColumn
vRtrMplsLspTemplateAdmGrpIncl = _VRtrMplsLspTemplateAdmGrpIncl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 10),
    _VRtrMplsLspTemplateAdmGrpIncl_Type()
)
vRtrMplsLspTemplateAdmGrpIncl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateAdmGrpIncl.setStatus("current")


class _VRtrMplsLspTemplateAdmGrpExcl_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateAdmGrpExcl based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspTemplateAdmGrpExcl_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateAdmGrpExcl_Object = MibTableColumn
vRtrMplsLspTemplateAdmGrpExcl = _VRtrMplsLspTemplateAdmGrpExcl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 11),
    _VRtrMplsLspTemplateAdmGrpExcl_Type()
)
vRtrMplsLspTemplateAdmGrpExcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateAdmGrpExcl.setStatus("current")


class _VRtrMplsLspTemplateFastReroute_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateFastReroute based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTemplateFastReroute_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateFastReroute_Object = MibTableColumn
vRtrMplsLspTemplateFastReroute = _VRtrMplsLspTemplateFastReroute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 12),
    _VRtrMplsLspTemplateFastReroute_Type()
)
vRtrMplsLspTemplateFastReroute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateFastReroute.setStatus("current")


class _VRtrMplsLspTemplateFRMethod_Type(Integer32):
    """Custom type vRtrMplsLspTemplateFRMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneToOneBackup", 1),
          ("facilityBackup", 2))
    )


_VRtrMplsLspTemplateFRMethod_Type.__name__ = "Integer32"
_VRtrMplsLspTemplateFRMethod_Object = MibTableColumn
vRtrMplsLspTemplateFRMethod = _VRtrMplsLspTemplateFRMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 13),
    _VRtrMplsLspTemplateFRMethod_Type()
)
vRtrMplsLspTemplateFRMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateFRMethod.setStatus("current")


class _VRtrMplsLspTemplateFRHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateFRHopLimit based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrMplsLspTemplateFRHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateFRHopLimit_Object = MibTableColumn
vRtrMplsLspTemplateFRHopLimit = _VRtrMplsLspTemplateFRHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 14),
    _VRtrMplsLspTemplateFRHopLimit_Type()
)
vRtrMplsLspTemplateFRHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateFRHopLimit.setStatus("current")


class _VRtrMplsLspTemplateHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateHopLimit based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_VRtrMplsLspTemplateHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateHopLimit_Object = MibTableColumn
vRtrMplsLspTemplateHopLimit = _VRtrMplsLspTemplateHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 15),
    _VRtrMplsLspTemplateHopLimit_Type()
)
vRtrMplsLspTemplateHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateHopLimit.setStatus("current")


class _VRtrMplsLspTemplateRecord_Type(Integer32):
    """Custom type vRtrMplsLspTemplateRecord based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("record", 1),
          ("noRecord", 2))
    )


_VRtrMplsLspTemplateRecord_Type.__name__ = "Integer32"
_VRtrMplsLspTemplateRecord_Object = MibTableColumn
vRtrMplsLspTemplateRecord = _VRtrMplsLspTemplateRecord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 16),
    _VRtrMplsLspTemplateRecord_Type()
)
vRtrMplsLspTemplateRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateRecord.setStatus("current")


class _VRtrMplsLspTemplateRecordLabel_Type(Integer32):
    """Custom type vRtrMplsLspTemplateRecordLabel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("record", 1),
          ("noRecord", 2))
    )


_VRtrMplsLspTemplateRecordLabel_Type.__name__ = "Integer32"
_VRtrMplsLspTemplateRecordLabel_Object = MibTableColumn
vRtrMplsLspTemplateRecordLabel = _VRtrMplsLspTemplateRecordLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 17),
    _VRtrMplsLspTemplateRecordLabel_Type()
)
vRtrMplsLspTemplateRecordLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateRecordLabel.setStatus("current")


class _VRtrMplsLspTemplateRetryLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateRetryLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VRtrMplsLspTemplateRetryLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateRetryLimit_Object = MibTableColumn
vRtrMplsLspTemplateRetryLimit = _VRtrMplsLspTemplateRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 18),
    _VRtrMplsLspTemplateRetryLimit_Type()
)
vRtrMplsLspTemplateRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateRetryLimit.setStatus("current")


class _VRtrMplsLspTemplateRetryTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateRetryTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_VRtrMplsLspTemplateRetryTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateRetryTimer_Object = MibTableColumn
vRtrMplsLspTemplateRetryTimer = _VRtrMplsLspTemplateRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 19),
    _VRtrMplsLspTemplateRetryTimer_Type()
)
vRtrMplsLspTemplateRetryTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateRetryTimer.setUnits("seconds")


class _VRtrMplsLspTemplateCspfTeMetric_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateCspfTeMetric based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTemplateCspfTeMetric_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateCspfTeMetric_Object = MibTableColumn
vRtrMplsLspTemplateCspfTeMetric = _VRtrMplsLspTemplateCspfTeMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 20),
    _VRtrMplsLspTemplateCspfTeMetric_Type()
)
vRtrMplsLspTemplateCspfTeMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateCspfTeMetric.setStatus("obsolete")
_VRtrMplsLspTemplateLspCount_Type = Gauge32
_VRtrMplsLspTemplateLspCount_Object = MibTableColumn
vRtrMplsLspTemplateLspCount = _VRtrMplsLspTemplateLspCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 21),
    _VRtrMplsLspTemplateLspCount_Type()
)
vRtrMplsLspTemplateLspCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateLspCount.setStatus("current")
_VRtrMplsLspTemplateMvpnRefCount_Type = Gauge32
_VRtrMplsLspTemplateMvpnRefCount_Object = MibTableColumn
vRtrMplsLspTemplateMvpnRefCount = _VRtrMplsLspTemplateMvpnRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 22),
    _VRtrMplsLspTemplateMvpnRefCount_Type()
)
vRtrMplsLspTemplateMvpnRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateMvpnRefCount.setStatus("current")


class _VRtrMplsLspTemplateFRPropAdmGrp_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateFRPropAdmGrp based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTemplateFRPropAdmGrp_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateFRPropAdmGrp_Object = MibTableColumn
vRtrMplsLspTemplateFRPropAdmGrp = _VRtrMplsLspTemplateFRPropAdmGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 23),
    _VRtrMplsLspTemplateFRPropAdmGrp_Type()
)
vRtrMplsLspTemplateFRPropAdmGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateFRPropAdmGrp.setStatus("current")


class _VRtrMplsLspTemplatePropAdmGrp_Type(TruthValue):
    """Custom type vRtrMplsLspTemplatePropAdmGrp based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTemplatePropAdmGrp_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplatePropAdmGrp_Object = MibTableColumn
vRtrMplsLspTemplatePropAdmGrp = _VRtrMplsLspTemplatePropAdmGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 24),
    _VRtrMplsLspTemplatePropAdmGrp_Type()
)
vRtrMplsLspTemplatePropAdmGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplatePropAdmGrp.setStatus("current")


class _VRtrMplsLspTemplateBgpShortcut_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateBgpShortcut based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspTemplateBgpShortcut_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateBgpShortcut_Object = MibTableColumn
vRtrMplsLspTemplateBgpShortcut = _VRtrMplsLspTemplateBgpShortcut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 25),
    _VRtrMplsLspTemplateBgpShortcut_Type()
)
vRtrMplsLspTemplateBgpShortcut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateBgpShortcut.setStatus("current")


class _VRtrMplsLspTemplateIgpShortcut_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateIgpShortcut based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspTemplateIgpShortcut_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateIgpShortcut_Object = MibTableColumn
vRtrMplsLspTemplateIgpShortcut = _VRtrMplsLspTemplateIgpShortcut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 26),
    _VRtrMplsLspTemplateIgpShortcut_Type()
)
vRtrMplsLspTemplateIgpShortcut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateIgpShortcut.setStatus("current")


class _VRtrMplsLspTemplateLdpOverRsvp_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateLdpOverRsvp based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspTemplateLdpOverRsvp_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateLdpOverRsvp_Object = MibTableColumn
vRtrMplsLspTemplateLdpOverRsvp = _VRtrMplsLspTemplateLdpOverRsvp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 27),
    _VRtrMplsLspTemplateLdpOverRsvp_Type()
)
vRtrMplsLspTemplateLdpOverRsvp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateLdpOverRsvp.setStatus("current")


class _VRtrMplsLspTemplateLeastFill_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateLeastFill based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTemplateLeastFill_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateLeastFill_Object = MibTableColumn
vRtrMplsLspTemplateLeastFill = _VRtrMplsLspTemplateLeastFill_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 28),
    _VRtrMplsLspTemplateLeastFill_Type()
)
vRtrMplsLspTemplateLeastFill.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateLeastFill.setStatus("current")


class _VRtrMplsLspTemplateMetric_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16777215),
    )


_VRtrMplsLspTemplateMetric_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateMetric_Object = MibTableColumn
vRtrMplsLspTemplateMetric = _VRtrMplsLspTemplateMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 29),
    _VRtrMplsLspTemplateMetric_Type()
)
vRtrMplsLspTemplateMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateMetric.setStatus("current")


class _VRtrMplsLspTemplateSetupPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateSetupPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspTemplateSetupPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateSetupPriority_Object = MibTableColumn
vRtrMplsLspTemplateSetupPriority = _VRtrMplsLspTemplateSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 30),
    _VRtrMplsLspTemplateSetupPriority_Type()
)
vRtrMplsLspTemplateSetupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateSetupPriority.setStatus("current")


class _VRtrMplsLspTemplateHoldPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateHoldPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspTemplateHoldPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateHoldPriority_Object = MibTableColumn
vRtrMplsLspTemplateHoldPriority = _VRtrMplsLspTemplateHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 31),
    _VRtrMplsLspTemplateHoldPriority_Type()
)
vRtrMplsLspTemplateHoldPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateHoldPriority.setStatus("current")


class _VRtrMplsLspTemplateVprnAutoBind_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateVprnAutoBind based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspTemplateVprnAutoBind_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateVprnAutoBind_Object = MibTableColumn
vRtrMplsLspTemplateVprnAutoBind = _VRtrMplsLspTemplateVprnAutoBind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 32),
    _VRtrMplsLspTemplateVprnAutoBind_Type()
)
vRtrMplsLspTemplateVprnAutoBind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateVprnAutoBind.setStatus("current")


class _VRtrMplsLspTempIgpSCutLfaType_Type(Integer32):
    """Custom type vRtrMplsLspTempIgpSCutLfaType based on Integer32"""
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
          ("lfaProtect", 1),
          ("lfaOnly", 2))
    )


_VRtrMplsLspTempIgpSCutLfaType_Type.__name__ = "Integer32"
_VRtrMplsLspTempIgpSCutLfaType_Object = MibTableColumn
vRtrMplsLspTempIgpSCutLfaType = _VRtrMplsLspTempIgpSCutLfaType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 33),
    _VRtrMplsLspTempIgpSCutLfaType_Type()
)
vRtrMplsLspTempIgpSCutLfaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempIgpSCutLfaType.setStatus("current")


class _VRtrMplsLspTempIgpSCutRelOffset_Type(Integer32):
    """Custom type vRtrMplsLspTempIgpSCutRelOffset based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_VRtrMplsLspTempIgpSCutRelOffset_Type.__name__ = "Integer32"
_VRtrMplsLspTempIgpSCutRelOffset_Object = MibTableColumn
vRtrMplsLspTempIgpSCutRelOffset = _VRtrMplsLspTempIgpSCutRelOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 34),
    _VRtrMplsLspTempIgpSCutRelOffset_Type()
)
vRtrMplsLspTempIgpSCutRelOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempIgpSCutRelOffset.setStatus("current")


class _VRtrMplsLspTempAutoBandwidth_Type(TruthValue):
    """Custom type vRtrMplsLspTempAutoBandwidth based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempAutoBandwidth_Type.__name__ = "TruthValue"
_VRtrMplsLspTempAutoBandwidth_Object = MibTableColumn
vRtrMplsLspTempAutoBandwidth = _VRtrMplsLspTempAutoBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 35),
    _VRtrMplsLspTempAutoBandwidth_Type()
)
vRtrMplsLspTempAutoBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBandwidth.setStatus("current")


class _VRtrMplsLspTempFRNodeProtect_Type(TruthValue):
    """Custom type vRtrMplsLspTempFRNodeProtect based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempFRNodeProtect_Type.__name__ = "TruthValue"
_VRtrMplsLspTempFRNodeProtect_Object = MibTableColumn
vRtrMplsLspTempFRNodeProtect = _VRtrMplsLspTempFRNodeProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 36),
    _VRtrMplsLspTempFRNodeProtect_Type()
)
vRtrMplsLspTempFRNodeProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempFRNodeProtect.setStatus("current")


class _VRtrMplsLspTemplateEgrStats_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateEgrStats based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTemplateEgrStats_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateEgrStats_Object = MibTableColumn
vRtrMplsLspTemplateEgrStats = _VRtrMplsLspTemplateEgrStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 37),
    _VRtrMplsLspTemplateEgrStats_Type()
)
vRtrMplsLspTemplateEgrStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateEgrStats.setStatus("current")


class _VRtrMplsLspTempCollectStats_Type(TruthValue):
    """Custom type vRtrMplsLspTempCollectStats based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempCollectStats_Type.__name__ = "TruthValue"
_VRtrMplsLspTempCollectStats_Object = MibTableColumn
vRtrMplsLspTempCollectStats = _VRtrMplsLspTempCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 38),
    _VRtrMplsLspTempCollectStats_Type()
)
vRtrMplsLspTempCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempCollectStats.setStatus("current")


class _VRtrMplsLspTempAccntingPolicy_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAccntingPolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 99),
    )


_VRtrMplsLspTempAccntingPolicy_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAccntingPolicy_Object = MibTableColumn
vRtrMplsLspTempAccntingPolicy = _VRtrMplsLspTempAccntingPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 39),
    _VRtrMplsLspTempAccntingPolicy_Type()
)
vRtrMplsLspTempAccntingPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAccntingPolicy.setStatus("current")


class _VRtrMplsLspTemplateFromAddrType_Type(InetAddressType):
    """Custom type vRtrMplsLspTemplateFromAddrType based on InetAddressType"""
    defaultValue = 0


_VRtrMplsLspTemplateFromAddrType_Type.__name__ = "InetAddressType"
_VRtrMplsLspTemplateFromAddrType_Object = MibTableColumn
vRtrMplsLspTemplateFromAddrType = _VRtrMplsLspTemplateFromAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 40),
    _VRtrMplsLspTemplateFromAddrType_Type()
)
vRtrMplsLspTemplateFromAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateFromAddrType.setStatus("current")


class _VRtrMplsLspTemplateFromAddr_Type(InetAddress):
    """Custom type vRtrMplsLspTemplateFromAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsLspTemplateFromAddr_Type.__name__ = "InetAddress"
_VRtrMplsLspTemplateFromAddr_Object = MibTableColumn
vRtrMplsLspTemplateFromAddr = _VRtrMplsLspTemplateFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 41),
    _VRtrMplsLspTemplateFromAddr_Type()
)
vRtrMplsLspTemplateFromAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateFromAddr.setStatus("current")


class _VRtrMplsLspTemplateClassType_Type(TmnxRsvpDSTEClassType):
    """Custom type vRtrMplsLspTemplateClassType based on TmnxRsvpDSTEClassType"""
    defaultValue = 0


_VRtrMplsLspTemplateClassType_Type.__name__ = "TmnxRsvpDSTEClassType"
_VRtrMplsLspTemplateClassType_Object = MibTableColumn
vRtrMplsLspTemplateClassType = _VRtrMplsLspTemplateClassType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 42),
    _VRtrMplsLspTemplateClassType_Type()
)
vRtrMplsLspTemplateClassType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateClassType.setStatus("current")


class _VRtrMplsLspTempBkupClassType_Type(TmnxRsvpDSTEClassType):
    """Custom type vRtrMplsLspTempBkupClassType based on TmnxRsvpDSTEClassType"""
    defaultValue = 0


_VRtrMplsLspTempBkupClassType_Type.__name__ = "TmnxRsvpDSTEClassType"
_VRtrMplsLspTempBkupClassType_Object = MibTableColumn
vRtrMplsLspTempBkupClassType = _VRtrMplsLspTempBkupClassType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 43),
    _VRtrMplsLspTempBkupClassType_Type()
)
vRtrMplsLspTempBkupClassType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempBkupClassType.setStatus("current")


class _VRtrMplsLspTempBgpTransportTunn_Type(TmnxMplsLspBgpRSVPLSPTunState):
    """Custom type vRtrMplsLspTempBgpTransportTunn based on TmnxMplsLspBgpRSVPLSPTunState"""
    defaultValue = 1


_VRtrMplsLspTempBgpTransportTunn_Type.__name__ = "TmnxMplsLspBgpRSVPLSPTunState"
_VRtrMplsLspTempBgpTransportTunn_Object = MibTableColumn
vRtrMplsLspTempBgpTransportTunn = _VRtrMplsLspTempBgpTransportTunn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 44),
    _VRtrMplsLspTempBgpTransportTunn_Type()
)
vRtrMplsLspTempBgpTransportTunn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempBgpTransportTunn.setStatus("current")


class _VRtrMplsLspTempMainCTRetryLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspTempMainCTRetryLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VRtrMplsLspTempMainCTRetryLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempMainCTRetryLimit_Object = MibTableColumn
vRtrMplsLspTempMainCTRetryLimit = _VRtrMplsLspTempMainCTRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 45),
    _VRtrMplsLspTempMainCTRetryLimit_Type()
)
vRtrMplsLspTempMainCTRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempMainCTRetryLimit.setStatus("current")


class _VRtrMplsLspTemplateRsvpAdspec_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateRsvpAdspec based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTemplateRsvpAdspec_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateRsvpAdspec_Object = MibTableColumn
vRtrMplsLspTemplateRsvpAdspec = _VRtrMplsLspTemplateRsvpAdspec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 46),
    _VRtrMplsLspTemplateRsvpAdspec_Type()
)
vRtrMplsLspTemplateRsvpAdspec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateRsvpAdspec.setStatus("current")


class _VRtrMplsLspTempLoadBalancingWt_Type(Unsigned32):
    """Custom type vRtrMplsLspTempLoadBalancingWt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrMplsLspTempLoadBalancingWt_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempLoadBalancingWt_Object = MibTableColumn
vRtrMplsLspTempLoadBalancingWt = _VRtrMplsLspTempLoadBalancingWt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 47),
    _VRtrMplsLspTempLoadBalancingWt_Type()
)
vRtrMplsLspTempLoadBalancingWt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempLoadBalancingWt.setStatus("current")


class _VRtrMplsLspTempClassFwdEnabled_Type(TruthValue):
    """Custom type vRtrMplsLspTempClassFwdEnabled based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempClassFwdEnabled_Type.__name__ = "TruthValue"
_VRtrMplsLspTempClassFwdEnabled_Object = MibTableColumn
vRtrMplsLspTempClassFwdEnabled = _VRtrMplsLspTempClassFwdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 48),
    _VRtrMplsLspTempClassFwdEnabled_Type()
)
vRtrMplsLspTempClassFwdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempClassFwdEnabled.setStatus("current")


class _VRtrMplsLspTempFC_Type(TmnxCBFClasses):
    """Custom type vRtrMplsLspTempFC based on TmnxCBFClasses"""
    defaultBinValue = "0"


_VRtrMplsLspTempFC_Type.__name__ = "TmnxCBFClasses"
_VRtrMplsLspTempFC_Object = MibTableColumn
vRtrMplsLspTempFC = _VRtrMplsLspTempFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 49),
    _VRtrMplsLspTempFC_Type()
)
vRtrMplsLspTempFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempFC.setStatus("obsolete")
_VRtrMplsLspTempBfdTemplateName_Type = TNamedItemOrEmpty
_VRtrMplsLspTempBfdTemplateName_Object = MibTableColumn
vRtrMplsLspTempBfdTemplateName = _VRtrMplsLspTempBfdTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 50),
    _VRtrMplsLspTempBfdTemplateName_Type()
)
vRtrMplsLspTempBfdTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempBfdTemplateName.setStatus("current")


class _VRtrMplsLspTempBfdEnable_Type(TruthValue):
    """Custom type vRtrMplsLspTempBfdEnable based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempBfdEnable_Type.__name__ = "TruthValue"
_VRtrMplsLspTempBfdEnable_Object = MibTableColumn
vRtrMplsLspTempBfdEnable = _VRtrMplsLspTempBfdEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 51),
    _VRtrMplsLspTempBfdEnable_Type()
)
vRtrMplsLspTempBfdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempBfdEnable.setStatus("current")


class _VRtrMplsLspTempBfdPingIntvl_Type(Unsigned32):
    """Custom type vRtrMplsLspTempBfdPingIntvl based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 300),
    )


_VRtrMplsLspTempBfdPingIntvl_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempBfdPingIntvl_Object = MibTableColumn
vRtrMplsLspTempBfdPingIntvl = _VRtrMplsLspTempBfdPingIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 52),
    _VRtrMplsLspTempBfdPingIntvl_Type()
)
vRtrMplsLspTempBfdPingIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempBfdPingIntvl.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempBfdPingIntvl.setUnits("seconds")


class _VRtrMplsLspTempEntropyLabel_Type(Integer32):
    """Custom type vRtrMplsLspTempEntropyLabel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forceDisable", 1),
          ("enable", 2),
          ("inherit", 3))
    )


_VRtrMplsLspTempEntropyLabel_Type.__name__ = "Integer32"
_VRtrMplsLspTempEntropyLabel_Object = MibTableColumn
vRtrMplsLspTempEntropyLabel = _VRtrMplsLspTempEntropyLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 53),
    _VRtrMplsLspTempEntropyLabel_Type()
)
vRtrMplsLspTempEntropyLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempEntropyLabel.setStatus("current")


class _VRtrMplsLspTemplatePceReport_Type(Integer32):
    """Custom type vRtrMplsLspTemplatePceReport based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("inherit", 3))
    )


_VRtrMplsLspTemplatePceReport_Type.__name__ = "Integer32"
_VRtrMplsLspTemplatePceReport_Object = MibTableColumn
vRtrMplsLspTemplatePceReport = _VRtrMplsLspTemplatePceReport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 54),
    _VRtrMplsLspTemplatePceReport_Type()
)
vRtrMplsLspTemplatePceReport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplatePceReport.setStatus("current")


class _VRtrMplsLspTempMaxSrLabels_Type(Unsigned32):
    """Custom type vRtrMplsLspTempMaxSrLabels based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_VRtrMplsLspTempMaxSrLabels_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempMaxSrLabels_Object = MibTableColumn
vRtrMplsLspTempMaxSrLabels = _VRtrMplsLspTempMaxSrLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 55),
    _VRtrMplsLspTempMaxSrLabels_Type()
)
vRtrMplsLspTempMaxSrLabels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempMaxSrLabels.setStatus("current")


class _VRtrMplsLspTempFrrOverheadLabel_Type(Unsigned32):
    """Custom type vRtrMplsLspTempFrrOverheadLabel based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VRtrMplsLspTempFrrOverheadLabel_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempFrrOverheadLabel_Object = MibTableColumn
vRtrMplsLspTempFrrOverheadLabel = _VRtrMplsLspTempFrrOverheadLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 56),
    _VRtrMplsLspTempFrrOverheadLabel_Type()
)
vRtrMplsLspTempFrrOverheadLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempFrrOverheadLabel.setStatus("current")


class _VRtrMplsLspTempBfdFailureAction_Type(Integer32):
    """Custom type vRtrMplsLspTempBfdFailureAction based on Integer32"""
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
          ("down", 1),
          ("failoverOrDown", 2))
    )


_VRtrMplsLspTempBfdFailureAction_Type.__name__ = "Integer32"
_VRtrMplsLspTempBfdFailureAction_Object = MibTableColumn
vRtrMplsLspTempBfdFailureAction = _VRtrMplsLspTempBfdFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 57),
    _VRtrMplsLspTempBfdFailureAction_Type()
)
vRtrMplsLspTempBfdFailureAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempBfdFailureAction.setStatus("current")


class _VRtrMplsLspTempCbfFwdingPlcy_Type(TNamedItemOrEmpty):
    """Custom type vRtrMplsLspTempCbfFwdingPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_VRtrMplsLspTempCbfFwdingPlcy_Type.__name__ = "TNamedItemOrEmpty"
_VRtrMplsLspTempCbfFwdingPlcy_Object = MibTableColumn
vRtrMplsLspTempCbfFwdingPlcy = _VRtrMplsLspTempCbfFwdingPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 58),
    _VRtrMplsLspTempCbfFwdingPlcy_Type()
)
vRtrMplsLspTempCbfFwdingPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempCbfFwdingPlcy.setStatus("current")


class _VRtrMplsLspTempCbfFwdingSet_Type(Unsigned32):
    """Custom type vRtrMplsLspTempCbfFwdingSet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_VRtrMplsLspTempCbfFwdingSet_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempCbfFwdingSet_Object = MibTableColumn
vRtrMplsLspTempCbfFwdingSet = _VRtrMplsLspTempCbfFwdingSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 59),
    _VRtrMplsLspTempCbfFwdingSet_Type()
)
vRtrMplsLspTempCbfFwdingSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempCbfFwdingSet.setStatus("current")


class _VRtrMplsLspTemplateId_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrMplsLspTemplateId_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateId_Object = MibTableColumn
vRtrMplsLspTemplateId = _VRtrMplsLspTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 60),
    _VRtrMplsLspTemplateId_Type()
)
vRtrMplsLspTemplateId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateId.setStatus("current")


class _VRtrMplsLspTempPathCompMeth_Type(Integer32):
    """Custom type vRtrMplsLspTempPathCompMeth based on Integer32"""
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
          ("localCspf", 2),
          ("pce", 3))
    )


_VRtrMplsLspTempPathCompMeth_Type.__name__ = "Integer32"
_VRtrMplsLspTempPathCompMeth_Object = MibTableColumn
vRtrMplsLspTempPathCompMeth = _VRtrMplsLspTempPathCompMeth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 61),
    _VRtrMplsLspTempPathCompMeth_Type()
)
vRtrMplsLspTempPathCompMeth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempPathCompMeth.setStatus("current")


class _VRtrMplsLspTempMetricType_Type(Integer32):
    """Custom type vRtrMplsLspTempMetricType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igp", 1),
          ("te", 2))
    )


_VRtrMplsLspTempMetricType_Type.__name__ = "Integer32"
_VRtrMplsLspTempMetricType_Object = MibTableColumn
vRtrMplsLspTempMetricType = _VRtrMplsLspTempMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 62),
    _VRtrMplsLspTempMetricType_Type()
)
vRtrMplsLspTempMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempMetricType.setStatus("current")


class _VRtrMplsLspTempLocalSrProt_Type(Integer32):
    """Custom type vRtrMplsLspTempLocalSrProt based on Integer32"""
    defaultValue = 2

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
          ("preferred", 2),
          ("mandatory", 3))
    )


_VRtrMplsLspTempLocalSrProt_Type.__name__ = "Integer32"
_VRtrMplsLspTempLocalSrProt_Object = MibTableColumn
vRtrMplsLspTempLocalSrProt = _VRtrMplsLspTempLocalSrProt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 63),
    _VRtrMplsLspTempLocalSrProt_Type()
)
vRtrMplsLspTempLocalSrProt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempLocalSrProt.setStatus("current")


class _VRtrMplsLspTempLabelStackRed_Type(TruthValue):
    """Custom type vRtrMplsLspTempLabelStackRed based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempLabelStackRed_Type.__name__ = "TruthValue"
_VRtrMplsLspTempLabelStackRed_Object = MibTableColumn
vRtrMplsLspTempLabelStackRed = _VRtrMplsLspTempLabelStackRed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 64),
    _VRtrMplsLspTempLabelStackRed_Type()
)
vRtrMplsLspTempLabelStackRed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempLabelStackRed.setStatus("current")


class _VRtrMplsLspTempBfdUpWaitTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspTempBfdUpWaitTimer based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrMplsLspTempBfdUpWaitTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempBfdUpWaitTimer_Object = MibTableColumn
vRtrMplsLspTempBfdUpWaitTimer = _VRtrMplsLspTempBfdUpWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 65),
    _VRtrMplsLspTempBfdUpWaitTimer_Type()
)
vRtrMplsLspTempBfdUpWaitTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempBfdUpWaitTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempBfdUpWaitTimer.setUnits("seconds")


class _VRtrMplsLspTempSelfPing_Type(Integer32):
    """Custom type vRtrMplsLspTempSelfPing based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("inherit", 3))
    )


_VRtrMplsLspTempSelfPing_Type.__name__ = "Integer32"
_VRtrMplsLspTempSelfPing_Object = MibTableColumn
vRtrMplsLspTempSelfPing = _VRtrMplsLspTempSelfPing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 66),
    _VRtrMplsLspTempSelfPing_Type()
)
vRtrMplsLspTempSelfPing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempSelfPing.setStatus("current")


class _VRtrMplsLspTempAddrFamily_Type(Integer32):
    """Custom type vRtrMplsLspTempAddrFamily based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("ipv4", 1),
          ("ipv6", 2))
    )


_VRtrMplsLspTempAddrFamily_Type.__name__ = "Integer32"
_VRtrMplsLspTempAddrFamily_Object = MibTableColumn
vRtrMplsLspTempAddrFamily = _VRtrMplsLspTempAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 67),
    _VRtrMplsLspTempAddrFamily_Type()
)
vRtrMplsLspTempAddrFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAddrFamily.setStatus("current")


class _VRtrMplsLspTemplateEgrStatsMode_Type(Integer32):
    """Custom type vRtrMplsLspTemplateEgrStatsMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("per-fc", 0),
          ("aggregate", 1))
    )


_VRtrMplsLspTemplateEgrStatsMode_Type.__name__ = "Integer32"
_VRtrMplsLspTemplateEgrStatsMode_Object = MibTableColumn
vRtrMplsLspTemplateEgrStatsMode = _VRtrMplsLspTemplateEgrStatsMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 68),
    _VRtrMplsLspTemplateEgrStatsMode_Type()
)
vRtrMplsLspTemplateEgrStatsMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateEgrStatsMode.setStatus("current")
_VRtrMplsLspAutoBWTableLastChg_Type = TimeStamp
_VRtrMplsLspAutoBWTableLastChg_Object = MibScalar
vRtrMplsLspAutoBWTableLastChg = _VRtrMplsLspAutoBWTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 42),
    _VRtrMplsLspAutoBWTableLastChg_Type()
)
vRtrMplsLspAutoBWTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWTableLastChg.setStatus("current")
_VRtrMplsLspAutoBandwidthTable_Object = MibTable
vRtrMplsLspAutoBandwidthTable = _VRtrMplsLspAutoBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43)
)
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBandwidthTable.setStatus("current")
_VRtrMplsLspAutoBandwidthEntry_Object = MibTableRow
vRtrMplsLspAutoBandwidthEntry = _VRtrMplsLspAutoBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1)
)
vRtrMplsLspAutoBandwidthEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWLspName"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBandwidthEntry.setStatus("current")
_VRtrMplsLspAutoBWLspName_Type = TLNamedItem
_VRtrMplsLspAutoBWLspName_Object = MibTableColumn
vRtrMplsLspAutoBWLspName = _VRtrMplsLspAutoBWLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 1),
    _VRtrMplsLspAutoBWLspName_Type()
)
vRtrMplsLspAutoBWLspName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWLspName.setStatus("current")
_VRtrMplsLspAutoBWLastChange_Type = TimeStamp
_VRtrMplsLspAutoBWLastChange_Object = MibTableColumn
vRtrMplsLspAutoBWLastChange = _VRtrMplsLspAutoBWLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 2),
    _VRtrMplsLspAutoBWLastChange_Type()
)
vRtrMplsLspAutoBWLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWLastChange.setStatus("current")


class _VRtrMplsLspAutoBWAdjDNPercent_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWAdjDNPercent based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWAdjDNPercent_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWAdjDNPercent_Object = MibTableColumn
vRtrMplsLspAutoBWAdjDNPercent = _VRtrMplsLspAutoBWAdjDNPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 3),
    _VRtrMplsLspAutoBWAdjDNPercent_Type()
)
vRtrMplsLspAutoBWAdjDNPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjDNPercent.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjDNPercent.setUnits("percent")


class _VRtrMplsLspAutoBWAdjDNMbps_Type(TmnxMplsLspBandwidth):
    """Custom type vRtrMplsLspAutoBWAdjDNMbps based on TmnxMplsLspBandwidth"""
    defaultValue = 0


_VRtrMplsLspAutoBWAdjDNMbps_Type.__name__ = "TmnxMplsLspBandwidth"
_VRtrMplsLspAutoBWAdjDNMbps_Object = MibTableColumn
vRtrMplsLspAutoBWAdjDNMbps = _VRtrMplsLspAutoBWAdjDNMbps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 4),
    _VRtrMplsLspAutoBWAdjDNMbps_Type()
)
vRtrMplsLspAutoBWAdjDNMbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjDNMbps.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjDNMbps.setUnits("megabps")


class _VRtrMplsLspAutoBWAdjMultiplier_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWAdjMultiplier based on Unsigned32"""
    defaultValue = 288

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_VRtrMplsLspAutoBWAdjMultiplier_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWAdjMultiplier_Object = MibTableColumn
vRtrMplsLspAutoBWAdjMultiplier = _VRtrMplsLspAutoBWAdjMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 5),
    _VRtrMplsLspAutoBWAdjMultiplier_Type()
)
vRtrMplsLspAutoBWAdjMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjMultiplier.setStatus("current")


class _VRtrMplsLspAutoBWAdjUPPercent_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWAdjUPPercent based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWAdjUPPercent_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWAdjUPPercent_Object = MibTableColumn
vRtrMplsLspAutoBWAdjUPPercent = _VRtrMplsLspAutoBWAdjUPPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 6),
    _VRtrMplsLspAutoBWAdjUPPercent_Type()
)
vRtrMplsLspAutoBWAdjUPPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjUPPercent.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjUPPercent.setUnits("percent")


class _VRtrMplsLspAutoBWAdjUPMbps_Type(TmnxMplsLspBandwidth):
    """Custom type vRtrMplsLspAutoBWAdjUPMbps based on TmnxMplsLspBandwidth"""
    defaultValue = 0


_VRtrMplsLspAutoBWAdjUPMbps_Type.__name__ = "TmnxMplsLspBandwidth"
_VRtrMplsLspAutoBWAdjUPMbps_Object = MibTableColumn
vRtrMplsLspAutoBWAdjUPMbps = _VRtrMplsLspAutoBWAdjUPMbps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 7),
    _VRtrMplsLspAutoBWAdjUPMbps_Type()
)
vRtrMplsLspAutoBWAdjUPMbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjUPMbps.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjUPMbps.setUnits("megabps")


class _VRtrMplsLspAutoBWMaxBW_Type(TmnxMplsLspBandwidth):
    """Custom type vRtrMplsLspAutoBWMaxBW based on TmnxMplsLspBandwidth"""
    defaultValue = 100000


_VRtrMplsLspAutoBWMaxBW_Type.__name__ = "TmnxMplsLspBandwidth"
_VRtrMplsLspAutoBWMaxBW_Object = MibTableColumn
vRtrMplsLspAutoBWMaxBW = _VRtrMplsLspAutoBWMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 8),
    _VRtrMplsLspAutoBWMaxBW_Type()
)
vRtrMplsLspAutoBWMaxBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMaxBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMaxBW.setUnits("megabps")


class _VRtrMplsLspAutoBWMinBW_Type(TmnxMplsLspBandwidth):
    """Custom type vRtrMplsLspAutoBWMinBW based on TmnxMplsLspBandwidth"""
    defaultValue = 0


_VRtrMplsLspAutoBWMinBW_Type.__name__ = "TmnxMplsLspBandwidth"
_VRtrMplsLspAutoBWMinBW_Object = MibTableColumn
vRtrMplsLspAutoBWMinBW = _VRtrMplsLspAutoBWMinBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 9),
    _VRtrMplsLspAutoBWMinBW_Type()
)
vRtrMplsLspAutoBWMinBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMinBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMinBW.setUnits("megabps")


class _VRtrMplsLspAutoBWMonitorBW_Type(TruthValue):
    """Custom type vRtrMplsLspAutoBWMonitorBW based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspAutoBWMonitorBW_Type.__name__ = "TruthValue"
_VRtrMplsLspAutoBWMonitorBW_Object = MibTableColumn
vRtrMplsLspAutoBWMonitorBW = _VRtrMplsLspAutoBWMonitorBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 10),
    _VRtrMplsLspAutoBWMonitorBW_Type()
)
vRtrMplsLspAutoBWMonitorBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMonitorBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMonitorBW.setUnits("megabps")


class _VRtrMplsLspAutoBWOverFlow_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWOverFlow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_VRtrMplsLspAutoBWOverFlow_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWOverFlow_Object = MibTableColumn
vRtrMplsLspAutoBWOverFlow = _VRtrMplsLspAutoBWOverFlow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 11),
    _VRtrMplsLspAutoBWOverFlow_Type()
)
vRtrMplsLspAutoBWOverFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWOverFlow.setStatus("current")


class _VRtrMplsLspAutoBWOvrFlwThreshold_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWOvrFlwThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWOvrFlwThreshold_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWOvrFlwThreshold_Object = MibTableColumn
vRtrMplsLspAutoBWOvrFlwThreshold = _VRtrMplsLspAutoBWOvrFlwThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 12),
    _VRtrMplsLspAutoBWOvrFlwThreshold_Type()
)
vRtrMplsLspAutoBWOvrFlwThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWOvrFlwThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWOvrFlwThreshold.setUnits("percent")


class _VRtrMplsLspAutoBWOvrFlwBW_Type(TmnxMplsLspBandwidth):
    """Custom type vRtrMplsLspAutoBWOvrFlwBW based on TmnxMplsLspBandwidth"""
    defaultValue = 0


_VRtrMplsLspAutoBWOvrFlwBW_Type.__name__ = "TmnxMplsLspBandwidth"
_VRtrMplsLspAutoBWOvrFlwBW_Object = MibTableColumn
vRtrMplsLspAutoBWOvrFlwBW = _VRtrMplsLspAutoBWOvrFlwBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 13),
    _VRtrMplsLspAutoBWOvrFlwBW_Type()
)
vRtrMplsLspAutoBWOvrFlwBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWOvrFlwBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWOvrFlwBW.setUnits("megabps")


class _VRtrMplsLspAutoBWSampMultiplier_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWSampMultiplier based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_VRtrMplsLspAutoBWSampMultiplier_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWSampMultiplier_Object = MibTableColumn
vRtrMplsLspAutoBWSampMultiplier = _VRtrMplsLspAutoBWSampMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 14),
    _VRtrMplsLspAutoBWSampMultiplier_Type()
)
vRtrMplsLspAutoBWSampMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWSampMultiplier.setStatus("current")
_VRtrMplsLspAutoBWSampTime_Type = Unsigned32
_VRtrMplsLspAutoBWSampTime_Object = MibTableColumn
vRtrMplsLspAutoBWSampTime = _VRtrMplsLspAutoBWSampTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 15),
    _VRtrMplsLspAutoBWSampTime_Type()
)
vRtrMplsLspAutoBWSampTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWSampTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWSampTime.setUnits("minutes")
_VRtrMplsLspAutoBWLastAdj_Type = TimeStamp
_VRtrMplsLspAutoBWLastAdj_Object = MibTableColumn
vRtrMplsLspAutoBWLastAdj = _VRtrMplsLspAutoBWLastAdj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 16),
    _VRtrMplsLspAutoBWLastAdj_Type()
)
vRtrMplsLspAutoBWLastAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWLastAdj.setStatus("current")
_VRtrMplsLspAutoBWLastAdjCause_Type = TmnxMplsLspAutoBWLastAdjCause
_VRtrMplsLspAutoBWLastAdjCause_Object = MibTableColumn
vRtrMplsLspAutoBWLastAdjCause = _VRtrMplsLspAutoBWLastAdjCause_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 17),
    _VRtrMplsLspAutoBWLastAdjCause_Type()
)
vRtrMplsLspAutoBWLastAdjCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWLastAdjCause.setStatus("current")
_VRtrMplsLspAutoBWNextAdj_Type = Unsigned32
_VRtrMplsLspAutoBWNextAdj_Object = MibTableColumn
vRtrMplsLspAutoBWNextAdj = _VRtrMplsLspAutoBWNextAdj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 18),
    _VRtrMplsLspAutoBWNextAdj_Type()
)
vRtrMplsLspAutoBWNextAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWNextAdj.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWNextAdj.setUnits("minutes")
_VRtrMplsLspAutoBWMaxAvgRate_Type = Unsigned32
_VRtrMplsLspAutoBWMaxAvgRate_Object = MibTableColumn
vRtrMplsLspAutoBWMaxAvgRate = _VRtrMplsLspAutoBWMaxAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 19),
    _VRtrMplsLspAutoBWMaxAvgRate_Type()
)
vRtrMplsLspAutoBWMaxAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMaxAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMaxAvgRate.setUnits("megabps")
_VRtrMplsLspAutoBWLastAvgRate_Type = Unsigned32
_VRtrMplsLspAutoBWLastAvgRate_Object = MibTableColumn
vRtrMplsLspAutoBWLastAvgRate = _VRtrMplsLspAutoBWLastAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 20),
    _VRtrMplsLspAutoBWLastAvgRate_Type()
)
vRtrMplsLspAutoBWLastAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWLastAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWLastAvgRate.setUnits("megabps")


class _VRtrMplsLspAutoBWInheritance_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWInheritance based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspAutoBWInheritance_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWInheritance_Object = MibTableColumn
vRtrMplsLspAutoBWInheritance = _VRtrMplsLspAutoBWInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 21),
    _VRtrMplsLspAutoBWInheritance_Type()
)
vRtrMplsLspAutoBWInheritance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWInheritance.setStatus("current")
_VRtrMplsLspAutoBWCurrentBW_Type = Unsigned32
_VRtrMplsLspAutoBWCurrentBW_Object = MibTableColumn
vRtrMplsLspAutoBWCurrentBW = _VRtrMplsLspAutoBWCurrentBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 22),
    _VRtrMplsLspAutoBWCurrentBW_Type()
)
vRtrMplsLspAutoBWCurrentBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWCurrentBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWCurrentBW.setUnits("megabps")
_VRtrMplsLspAutoBWAdjTime_Type = Unsigned32
_VRtrMplsLspAutoBWAdjTime_Object = MibTableColumn
vRtrMplsLspAutoBWAdjTime = _VRtrMplsLspAutoBWAdjTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 23),
    _VRtrMplsLspAutoBWAdjTime_Type()
)
vRtrMplsLspAutoBWAdjTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjTime.setUnits("minutes")
_VRtrMplsLspAutoBWOvrFlwCount_Type = Unsigned32
_VRtrMplsLspAutoBWOvrFlwCount_Object = MibTableColumn
vRtrMplsLspAutoBWOvrFlwCount = _VRtrMplsLspAutoBWOvrFlwCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 24),
    _VRtrMplsLspAutoBWOvrFlwCount_Type()
)
vRtrMplsLspAutoBWOvrFlwCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWOvrFlwCount.setStatus("current")
_VRtrMplsLspAutoBWSampCount_Type = Unsigned32
_VRtrMplsLspAutoBWSampCount_Object = MibTableColumn
vRtrMplsLspAutoBWSampCount = _VRtrMplsLspAutoBWSampCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 25),
    _VRtrMplsLspAutoBWSampCount_Type()
)
vRtrMplsLspAutoBWSampCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWSampCount.setStatus("current")
_VRtrMplsLspAutoBWAdjCount_Type = Unsigned32
_VRtrMplsLspAutoBWAdjCount_Object = MibTableColumn
vRtrMplsLspAutoBWAdjCount = _VRtrMplsLspAutoBWAdjCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 26),
    _VRtrMplsLspAutoBWAdjCount_Type()
)
vRtrMplsLspAutoBWAdjCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjCount.setStatus("current")
_VRtrMplsLspAutoBWOperState_Type = TmnxEnabledDisabled
_VRtrMplsLspAutoBWOperState_Object = MibTableColumn
vRtrMplsLspAutoBWOperState = _VRtrMplsLspAutoBWOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 27),
    _VRtrMplsLspAutoBWOperState_Type()
)
vRtrMplsLspAutoBWOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWOperState.setStatus("current")
_VRtrMplsLspAutoBWSampInterval_Type = Unsigned32
_VRtrMplsLspAutoBWSampInterval_Object = MibTableColumn
vRtrMplsLspAutoBWSampInterval = _VRtrMplsLspAutoBWSampInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 28),
    _VRtrMplsLspAutoBWSampInterval_Type()
)
vRtrMplsLspAutoBWSampInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWSampInterval.setStatus("current")


class _VRtrMplsLspAutoBWBeWeight_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWBeWeight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWBeWeight_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWBeWeight_Object = MibTableColumn
vRtrMplsLspAutoBWBeWeight = _VRtrMplsLspAutoBWBeWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 29),
    _VRtrMplsLspAutoBWBeWeight_Type()
)
vRtrMplsLspAutoBWBeWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWBeWeight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWBeWeight.setUnits("percent")


class _VRtrMplsLspAutoBWL2Weight_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWL2Weight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWL2Weight_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWL2Weight_Object = MibTableColumn
vRtrMplsLspAutoBWL2Weight = _VRtrMplsLspAutoBWL2Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 30),
    _VRtrMplsLspAutoBWL2Weight_Type()
)
vRtrMplsLspAutoBWL2Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWL2Weight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWL2Weight.setUnits("percent")


class _VRtrMplsLspAutoBWAfWeight_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWAfWeight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWAfWeight_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWAfWeight_Object = MibTableColumn
vRtrMplsLspAutoBWAfWeight = _VRtrMplsLspAutoBWAfWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 31),
    _VRtrMplsLspAutoBWAfWeight_Type()
)
vRtrMplsLspAutoBWAfWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAfWeight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAfWeight.setUnits("percent")


class _VRtrMplsLspAutoBWL1Weight_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWL1Weight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWL1Weight_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWL1Weight_Object = MibTableColumn
vRtrMplsLspAutoBWL1Weight = _VRtrMplsLspAutoBWL1Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 32),
    _VRtrMplsLspAutoBWL1Weight_Type()
)
vRtrMplsLspAutoBWL1Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWL1Weight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWL1Weight.setUnits("percent")


class _VRtrMplsLspAutoBWH2Weight_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWH2Weight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWH2Weight_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWH2Weight_Object = MibTableColumn
vRtrMplsLspAutoBWH2Weight = _VRtrMplsLspAutoBWH2Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 33),
    _VRtrMplsLspAutoBWH2Weight_Type()
)
vRtrMplsLspAutoBWH2Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWH2Weight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWH2Weight.setUnits("percent")


class _VRtrMplsLspAutoBWEfWeight_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWEfWeight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWEfWeight_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWEfWeight_Object = MibTableColumn
vRtrMplsLspAutoBWEfWeight = _VRtrMplsLspAutoBWEfWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 34),
    _VRtrMplsLspAutoBWEfWeight_Type()
)
vRtrMplsLspAutoBWEfWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWEfWeight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWEfWeight.setUnits("percent")


class _VRtrMplsLspAutoBWH1Weight_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWH1Weight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWH1Weight_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWH1Weight_Object = MibTableColumn
vRtrMplsLspAutoBWH1Weight = _VRtrMplsLspAutoBWH1Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 35),
    _VRtrMplsLspAutoBWH1Weight_Type()
)
vRtrMplsLspAutoBWH1Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWH1Weight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWH1Weight.setUnits("percent")


class _VRtrMplsLspAutoBWNcWeight_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWNcWeight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWNcWeight_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWNcWeight_Object = MibTableColumn
vRtrMplsLspAutoBWNcWeight = _VRtrMplsLspAutoBWNcWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 36),
    _VRtrMplsLspAutoBWNcWeight_Type()
)
vRtrMplsLspAutoBWNcWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWNcWeight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWNcWeight.setUnits("percent")


class _VRtrMplsLspAutoBWUnderFlow_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWUnderFlow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_VRtrMplsLspAutoBWUnderFlow_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWUnderFlow_Object = MibTableColumn
vRtrMplsLspAutoBWUnderFlow = _VRtrMplsLspAutoBWUnderFlow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 37),
    _VRtrMplsLspAutoBWUnderFlow_Type()
)
vRtrMplsLspAutoBWUnderFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWUnderFlow.setStatus("current")


class _VRtrMplsLspAutoBWUndFlwThreshold_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWUndFlwThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_VRtrMplsLspAutoBWUndFlwThreshold_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWUndFlwThreshold_Object = MibTableColumn
vRtrMplsLspAutoBWUndFlwThreshold = _VRtrMplsLspAutoBWUndFlwThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 38),
    _VRtrMplsLspAutoBWUndFlwThreshold_Type()
)
vRtrMplsLspAutoBWUndFlwThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWUndFlwThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWUndFlwThreshold.setUnits("percent")


class _VRtrMplsLspAutoBWUndFlwBW_Type(TmnxMplsLspBandwidth):
    """Custom type vRtrMplsLspAutoBWUndFlwBW based on TmnxMplsLspBandwidth"""
    defaultValue = 0


_VRtrMplsLspAutoBWUndFlwBW_Type.__name__ = "TmnxMplsLspBandwidth"
_VRtrMplsLspAutoBWUndFlwBW_Object = MibTableColumn
vRtrMplsLspAutoBWUndFlwBW = _VRtrMplsLspAutoBWUndFlwBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 39),
    _VRtrMplsLspAutoBWUndFlwBW_Type()
)
vRtrMplsLspAutoBWUndFlwBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWUndFlwBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWUndFlwBW.setUnits("megabps")
_VRtrMplsLspAutoBWUndFlwCount_Type = Counter32
_VRtrMplsLspAutoBWUndFlwCount_Object = MibTableColumn
vRtrMplsLspAutoBWUndFlwCount = _VRtrMplsLspAutoBWUndFlwCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 40),
    _VRtrMplsLspAutoBWUndFlwCount_Type()
)
vRtrMplsLspAutoBWUndFlwCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWUndFlwCount.setStatus("current")
_VRtrMplsLspAutoBWMaxUndFlwBw_Type = Unsigned32
_VRtrMplsLspAutoBWMaxUndFlwBw_Object = MibTableColumn
vRtrMplsLspAutoBWMaxUndFlwBw = _VRtrMplsLspAutoBWMaxUndFlwBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 41),
    _VRtrMplsLspAutoBWMaxUndFlwBw_Type()
)
vRtrMplsLspAutoBWMaxUndFlwBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMaxUndFlwBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMaxUndFlwBw.setUnits("megabps")


class _VRtrMplsLspAutoBWUseLastAdjBW_Type(TruthValue):
    """Custom type vRtrMplsLspAutoBWUseLastAdjBW based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspAutoBWUseLastAdjBW_Type.__name__ = "TruthValue"
_VRtrMplsLspAutoBWUseLastAdjBW_Object = MibTableColumn
vRtrMplsLspAutoBWUseLastAdjBW = _VRtrMplsLspAutoBWUseLastAdjBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 42),
    _VRtrMplsLspAutoBWUseLastAdjBW_Type()
)
vRtrMplsLspAutoBWUseLastAdjBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWUseLastAdjBW.setStatus("current")


class _VRtrMplsLspAutoBWSecRetryLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWSecRetryLimit based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VRtrMplsLspAutoBWSecRetryLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWSecRetryLimit_Object = MibTableColumn
vRtrMplsLspAutoBWSecRetryLimit = _VRtrMplsLspAutoBWSecRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 43),
    _VRtrMplsLspAutoBWSecRetryLimit_Type()
)
vRtrMplsLspAutoBWSecRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWSecRetryLimit.setStatus("current")
_VRtrMplsLspAutoBWLastAdjBW_Type = Integer32
_VRtrMplsLspAutoBWLastAdjBW_Object = MibTableColumn
vRtrMplsLspAutoBWLastAdjBW = _VRtrMplsLspAutoBWLastAdjBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 44),
    _VRtrMplsLspAutoBWLastAdjBW_Type()
)
vRtrMplsLspAutoBWLastAdjBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWLastAdjBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWLastAdjBW.setUnits("megabps")
_VRtrMplsLspPathOperTable_Object = MibTable
vRtrMplsLspPathOperTable = _VRtrMplsLspPathOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44)
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperTable.setStatus("current")
_VRtrMplsLspPathOperEntry_Object = MibTableRow
vRtrMplsLspPathOperEntry = _VRtrMplsLspPathOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperEntry.setStatus("current")


class _VRtrMplsLspPathOperSetupPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspPathOperSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspPathOperSetupPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathOperSetupPriority_Object = MibTableColumn
vRtrMplsLspPathOperSetupPriority = _VRtrMplsLspPathOperSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 1),
    _VRtrMplsLspPathOperSetupPriority_Type()
)
vRtrMplsLspPathOperSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperSetupPriority.setStatus("current")


class _VRtrMplsLspPathOperHoldPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspPathOperHoldPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspPathOperHoldPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathOperHoldPriority_Object = MibTableColumn
vRtrMplsLspPathOperHoldPriority = _VRtrMplsLspPathOperHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 2),
    _VRtrMplsLspPathOperHoldPriority_Type()
)
vRtrMplsLspPathOperHoldPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperHoldPriority.setStatus("current")


class _VRtrMplsLspPathOperRecord_Type(Integer32):
    """Custom type vRtrMplsLspPathOperRecord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("record", 1),
          ("noRecord", 2))
    )


_VRtrMplsLspPathOperRecord_Type.__name__ = "Integer32"
_VRtrMplsLspPathOperRecord_Object = MibTableColumn
vRtrMplsLspPathOperRecord = _VRtrMplsLspPathOperRecord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 3),
    _VRtrMplsLspPathOperRecord_Type()
)
vRtrMplsLspPathOperRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperRecord.setStatus("current")


class _VRtrMplsLspPathOperRecordLabel_Type(Integer32):
    """Custom type vRtrMplsLspPathOperRecordLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("record", 1),
          ("noRecord", 2))
    )


_VRtrMplsLspPathOperRecordLabel_Type.__name__ = "Integer32"
_VRtrMplsLspPathOperRecordLabel_Object = MibTableColumn
vRtrMplsLspPathOperRecordLabel = _VRtrMplsLspPathOperRecordLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 4),
    _VRtrMplsLspPathOperRecordLabel_Type()
)
vRtrMplsLspPathOperRecordLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperRecordLabel.setStatus("current")


class _VRtrMplsLspPathOperHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspPathOperHopLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_VRtrMplsLspPathOperHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathOperHopLimit_Object = MibTableColumn
vRtrMplsLspPathOperHopLimit = _VRtrMplsLspPathOperHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 5),
    _VRtrMplsLspPathOperHopLimit_Type()
)
vRtrMplsLspPathOperHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperHopLimit.setStatus("current")
_VRtrMplsLspPathOperAdminGrpIncl_Type = Unsigned32
_VRtrMplsLspPathOperAdminGrpIncl_Object = MibTableColumn
vRtrMplsLspPathOperAdminGrpIncl = _VRtrMplsLspPathOperAdminGrpIncl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 6),
    _VRtrMplsLspPathOperAdminGrpIncl_Type()
)
vRtrMplsLspPathOperAdminGrpIncl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperAdminGrpIncl.setStatus("current")
_VRtrMplsLspPathOperAdminGrExcld_Type = Unsigned32
_VRtrMplsLspPathOperAdminGrExcld_Object = MibTableColumn
vRtrMplsLspPathOperAdminGrExcld = _VRtrMplsLspPathOperAdminGrExcld_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 7),
    _VRtrMplsLspPathOperAdminGrExcld_Type()
)
vRtrMplsLspPathOperAdminGrExcld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperAdminGrExcld.setStatus("current")
_VRtrMplsLspPathOperCspf_Type = TruthValue
_VRtrMplsLspPathOperCspf_Object = MibTableColumn
vRtrMplsLspPathOperCspf = _VRtrMplsLspPathOperCspf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 8),
    _VRtrMplsLspPathOperCspf_Type()
)
vRtrMplsLspPathOperCspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperCspf.setStatus("obsolete")
_VRtrMplsLspPathOperCspfToFrstLs_Type = TruthValue
_VRtrMplsLspPathOperCspfToFrstLs_Object = MibTableColumn
vRtrMplsLspPathOperCspfToFrstLs = _VRtrMplsLspPathOperCspfToFrstLs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 9),
    _VRtrMplsLspPathOperCspfToFrstLs_Type()
)
vRtrMplsLspPathOperCspfToFrstLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperCspfToFrstLs.setStatus("obsolete")
_VRtrMplsLspPathOperLeastFill_Type = TruthValue
_VRtrMplsLspPathOperLeastFill_Object = MibTableColumn
vRtrMplsLspPathOperLeastFill = _VRtrMplsLspPathOperLeastFill_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 10),
    _VRtrMplsLspPathOperLeastFill_Type()
)
vRtrMplsLspPathOperLeastFill.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperLeastFill.setStatus("current")
_VRtrMplsLspPathOperRsvpAdspec_Type = TruthValue
_VRtrMplsLspPathOperRsvpAdspec_Object = MibTableColumn
vRtrMplsLspPathOperRsvpAdspec = _VRtrMplsLspPathOperRsvpAdspec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 11),
    _VRtrMplsLspPathOperRsvpAdspec_Type()
)
vRtrMplsLspPathOperRsvpAdspec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperRsvpAdspec.setStatus("current")
_VRtrMplsLspPathOperFRNodeProtect_Type = TruthValue
_VRtrMplsLspPathOperFRNodeProtect_Object = MibTableColumn
vRtrMplsLspPathOperFRNodeProtect = _VRtrMplsLspPathOperFRNodeProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 12),
    _VRtrMplsLspPathOperFRNodeProtect_Type()
)
vRtrMplsLspPathOperFRNodeProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperFRNodeProtect.setStatus("current")
_VRtrMplsLspPathOperPropAdminGrp_Type = TruthValue
_VRtrMplsLspPathOperPropAdminGrp_Object = MibTableColumn
vRtrMplsLspPathOperPropAdminGrp = _VRtrMplsLspPathOperPropAdminGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 13),
    _VRtrMplsLspPathOperPropAdminGrp_Type()
)
vRtrMplsLspPathOperPropAdminGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperPropAdminGrp.setStatus("current")


class _VRtrMplsLspPathOperFRHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspPathOperFRHopLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrMplsLspPathOperFRHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathOperFRHopLimit_Object = MibTableColumn
vRtrMplsLspPathOperFRHopLimit = _VRtrMplsLspPathOperFRHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 14),
    _VRtrMplsLspPathOperFRHopLimit_Type()
)
vRtrMplsLspPathOperFRHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperFRHopLimit.setStatus("current")
_VRtrMplsLspPathOperFRPropAdmGrp_Type = TruthValue
_VRtrMplsLspPathOperFRPropAdmGrp_Object = MibTableColumn
vRtrMplsLspPathOperFRPropAdmGrp = _VRtrMplsLspPathOperFRPropAdmGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 15),
    _VRtrMplsLspPathOperFRPropAdmGrp_Type()
)
vRtrMplsLspPathOperFRPropAdmGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperFRPropAdmGrp.setStatus("current")
_VRtrMplsLspPathOperInterArea_Type = TruthValue
_VRtrMplsLspPathOperInterArea_Object = MibTableColumn
vRtrMplsLspPathOperInterArea = _VRtrMplsLspPathOperInterArea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 16),
    _VRtrMplsLspPathOperInterArea_Type()
)
vRtrMplsLspPathOperInterArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperInterArea.setStatus("current")


class _VRtrMplsLspPathOperCompMeth_Type(Integer32):
    """Custom type vRtrMplsLspPathOperCompMeth based on Integer32"""
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
        *(("notApplicable", 0),
          ("none", 1),
          ("localCspf", 2),
          ("pce", 3))
    )


_VRtrMplsLspPathOperCompMeth_Type.__name__ = "Integer32"
_VRtrMplsLspPathOperCompMeth_Object = MibTableColumn
vRtrMplsLspPathOperCompMeth = _VRtrMplsLspPathOperCompMeth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 17),
    _VRtrMplsLspPathOperCompMeth_Type()
)
vRtrMplsLspPathOperCompMeth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperCompMeth.setStatus("current")


class _VRtrMplsLspPathOperMetricType_Type(Integer32):
    """Custom type vRtrMplsLspPathOperMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("igp", 1),
          ("te", 2))
    )


_VRtrMplsLspPathOperMetricType_Type.__name__ = "Integer32"
_VRtrMplsLspPathOperMetricType_Object = MibTableColumn
vRtrMplsLspPathOperMetricType = _VRtrMplsLspPathOperMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 18),
    _VRtrMplsLspPathOperMetricType_Type()
)
vRtrMplsLspPathOperMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperMetricType.setStatus("current")


class _VRtrMplsLspPathOperLocalSrProt_Type(Integer32):
    """Custom type vRtrMplsLspPathOperLocalSrProt based on Integer32"""
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
        *(("notApplicable", 0),
          ("none", 1),
          ("preferred", 2),
          ("mandatory", 3))
    )


_VRtrMplsLspPathOperLocalSrProt_Type.__name__ = "Integer32"
_VRtrMplsLspPathOperLocalSrProt_Object = MibTableColumn
vRtrMplsLspPathOperLocalSrProt = _VRtrMplsLspPathOperLocalSrProt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 19),
    _VRtrMplsLspPathOperLocalSrProt_Type()
)
vRtrMplsLspPathOperLocalSrProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperLocalSrProt.setStatus("current")


class _VRtrMplsLspPathOperLabelStackRed_Type(Integer32):
    """Custom type vRtrMplsLspPathOperLabelStackRed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("true", 1),
          ("false", 2))
    )


_VRtrMplsLspPathOperLabelStackRed_Type.__name__ = "Integer32"
_VRtrMplsLspPathOperLabelStackRed_Object = MibTableColumn
vRtrMplsLspPathOperLabelStackRed = _VRtrMplsLspPathOperLabelStackRed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 20),
    _VRtrMplsLspPathOperLabelStackRed_Type()
)
vRtrMplsLspPathOperLabelStackRed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperLabelStackRed.setStatus("current")
_VRtrMplsLspPathNgFNAddrType_Type = InetAddressType
_VRtrMplsLspPathNgFNAddrType_Object = MibTableColumn
vRtrMplsLspPathNgFNAddrType = _VRtrMplsLspPathNgFNAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 21),
    _VRtrMplsLspPathNgFNAddrType_Type()
)
vRtrMplsLspPathNgFNAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathNgFNAddrType.setStatus("current")


class _VRtrMplsLspPathNgFNAddr_Type(InetAddress):
    """Custom type vRtrMplsLspPathNgFNAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsLspPathNgFNAddr_Type.__name__ = "InetAddress"
_VRtrMplsLspPathNgFNAddr_Object = MibTableColumn
vRtrMplsLspPathNgFNAddr = _VRtrMplsLspPathNgFNAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 22),
    _VRtrMplsLspPathNgFNAddr_Type()
)
vRtrMplsLspPathNgFNAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathNgFNAddr.setStatus("current")
_VRtrMplsLabelObjs_ObjectIdentity = ObjectIdentity
vRtrMplsLabelObjs = _VRtrMplsLabelObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 45)
)


class _VRtrMplsLabelMaxStaticLspLabels_Type(Unsigned32):
    """Custom type vRtrMplsLabelMaxStaticLspLabels based on Unsigned32"""
    defaultValue = 2016

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262112),
    )


_VRtrMplsLabelMaxStaticLspLabels_Type.__name__ = "Unsigned32"
_VRtrMplsLabelMaxStaticLspLabels_Object = MibScalar
vRtrMplsLabelMaxStaticLspLabels = _VRtrMplsLabelMaxStaticLspLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 45, 1),
    _VRtrMplsLabelMaxStaticLspLabels_Type()
)
vRtrMplsLabelMaxStaticLspLabels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLabelMaxStaticLspLabels.setStatus("obsolete")


class _VRtrMplsLabelMaxStaticSvcLabels_Type(Unsigned32):
    """Custom type vRtrMplsLabelMaxStaticSvcLabels based on Unsigned32"""
    defaultValue = 16384

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262112),
    )


_VRtrMplsLabelMaxStaticSvcLabels_Type.__name__ = "Unsigned32"
_VRtrMplsLabelMaxStaticSvcLabels_Object = MibScalar
vRtrMplsLabelMaxStaticSvcLabels = _VRtrMplsLabelMaxStaticSvcLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 45, 2),
    _VRtrMplsLabelMaxStaticSvcLabels_Type()
)
vRtrMplsLabelMaxStaticSvcLabels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLabelMaxStaticSvcLabels.setStatus("obsolete")


class _VRtrMplsLabelBgpLabelsHoldTimer_Type(Unsigned32):
    """Custom type vRtrMplsLabelBgpLabelsHoldTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrMplsLabelBgpLabelsHoldTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLabelBgpLabelsHoldTimer_Object = MibScalar
vRtrMplsLabelBgpLabelsHoldTimer = _VRtrMplsLabelBgpLabelsHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 45, 3),
    _VRtrMplsLabelBgpLabelsHoldTimer_Type()
)
vRtrMplsLabelBgpLabelsHoldTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLabelBgpLabelsHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLabelBgpLabelsHoldTimer.setUnits("seconds")


class _VRtrMplsLabelSegRouteStartLabel_Type(TmnxMplsLabelOrZero):
    """Custom type vRtrMplsLabelSegRouteStartLabel based on TmnxMplsLabelOrZero"""
    defaultValue = 0


_VRtrMplsLabelSegRouteStartLabel_Type.__name__ = "TmnxMplsLabelOrZero"
_VRtrMplsLabelSegRouteStartLabel_Object = MibScalar
vRtrMplsLabelSegRouteStartLabel = _VRtrMplsLabelSegRouteStartLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 45, 4),
    _VRtrMplsLabelSegRouteStartLabel_Type()
)
vRtrMplsLabelSegRouteStartLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLabelSegRouteStartLabel.setStatus("current")


class _VRtrMplsLabelSegRouteEndLabel_Type(TmnxMplsLabelOrZero):
    """Custom type vRtrMplsLabelSegRouteEndLabel based on TmnxMplsLabelOrZero"""
    defaultValue = 0


_VRtrMplsLabelSegRouteEndLabel_Type.__name__ = "TmnxMplsLabelOrZero"
_VRtrMplsLabelSegRouteEndLabel_Object = MibScalar
vRtrMplsLabelSegRouteEndLabel = _VRtrMplsLabelSegRouteEndLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 45, 5),
    _VRtrMplsLabelSegRouteEndLabel_Type()
)
vRtrMplsLabelSegRouteEndLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLabelSegRouteEndLabel.setStatus("current")


class _VRtrMplsLabelStaticLabelRange_Type(Unsigned32):
    """Custom type vRtrMplsLabelStaticLabelRange based on Unsigned32"""
    defaultValue = 18400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048544),
    )


_VRtrMplsLabelStaticLabelRange_Type.__name__ = "Unsigned32"
_VRtrMplsLabelStaticLabelRange_Object = MibScalar
vRtrMplsLabelStaticLabelRange = _VRtrMplsLabelStaticLabelRange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 45, 6),
    _VRtrMplsLabelStaticLabelRange_Type()
)
vRtrMplsLabelStaticLabelRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLabelStaticLabelRange.setStatus("current")
_VRtrMplsLspTempAutoBWTblLastChg_Type = TimeStamp
_VRtrMplsLspTempAutoBWTblLastChg_Object = MibScalar
vRtrMplsLspTempAutoBWTblLastChg = _VRtrMplsLspTempAutoBWTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 46),
    _VRtrMplsLspTempAutoBWTblLastChg_Type()
)
vRtrMplsLspTempAutoBWTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWTblLastChg.setStatus("current")
_VRtrMplsLspTempAutoBWTable_Object = MibTable
vRtrMplsLspTempAutoBWTable = _VRtrMplsLspTempAutoBWTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47)
)
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWTable.setStatus("current")
_VRtrMplsLspTempAutoBWEntry_Object = MibTableRow
vRtrMplsLspTempAutoBWEntry = _VRtrMplsLspTempAutoBWEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1)
)
vRtrMplsLspTempAutoBWEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateName"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWEntry.setStatus("current")
_VRtrMplsLspTempAutoBWLastChg_Type = TimeStamp
_VRtrMplsLspTempAutoBWLastChg_Object = MibTableColumn
vRtrMplsLspTempAutoBWLastChg = _VRtrMplsLspTempAutoBWLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 1),
    _VRtrMplsLspTempAutoBWLastChg_Type()
)
vRtrMplsLspTempAutoBWLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWLastChg.setStatus("current")


class _VRtrMplsLspTempAutoBWAdjDNPer_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWAdjDNPer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWAdjDNPer_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWAdjDNPer_Object = MibTableColumn
vRtrMplsLspTempAutoBWAdjDNPer = _VRtrMplsLspTempAutoBWAdjDNPer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 2),
    _VRtrMplsLspTempAutoBWAdjDNPer_Type()
)
vRtrMplsLspTempAutoBWAdjDNPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAdjDNPer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAdjDNPer.setUnits("percent")


class _VRtrMplsLspTempAutoBWAdjDNMbps_Type(TmnxMplsLspBandwidth):
    """Custom type vRtrMplsLspTempAutoBWAdjDNMbps based on TmnxMplsLspBandwidth"""
    defaultValue = 0


_VRtrMplsLspTempAutoBWAdjDNMbps_Type.__name__ = "TmnxMplsLspBandwidth"
_VRtrMplsLspTempAutoBWAdjDNMbps_Object = MibTableColumn
vRtrMplsLspTempAutoBWAdjDNMbps = _VRtrMplsLspTempAutoBWAdjDNMbps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 3),
    _VRtrMplsLspTempAutoBWAdjDNMbps_Type()
)
vRtrMplsLspTempAutoBWAdjDNMbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAdjDNMbps.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAdjDNMbps.setUnits("megabps")


class _VRtrMplsLspTempAutoBWAdjUPPer_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWAdjUPPer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWAdjUPPer_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWAdjUPPer_Object = MibTableColumn
vRtrMplsLspTempAutoBWAdjUPPer = _VRtrMplsLspTempAutoBWAdjUPPer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 4),
    _VRtrMplsLspTempAutoBWAdjUPPer_Type()
)
vRtrMplsLspTempAutoBWAdjUPPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAdjUPPer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAdjUPPer.setUnits("percent")


class _VRtrMplsLspTempAutoBWAdjUPMbps_Type(TmnxMplsLspBandwidth):
    """Custom type vRtrMplsLspTempAutoBWAdjUPMbps based on TmnxMplsLspBandwidth"""
    defaultValue = 0


_VRtrMplsLspTempAutoBWAdjUPMbps_Type.__name__ = "TmnxMplsLspBandwidth"
_VRtrMplsLspTempAutoBWAdjUPMbps_Object = MibTableColumn
vRtrMplsLspTempAutoBWAdjUPMbps = _VRtrMplsLspTempAutoBWAdjUPMbps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 5),
    _VRtrMplsLspTempAutoBWAdjUPMbps_Type()
)
vRtrMplsLspTempAutoBWAdjUPMbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAdjUPMbps.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAdjUPMbps.setUnits("megabps")


class _VRtrMplsLspTempAutoBWMaxBW_Type(TmnxMplsLspBandwidth):
    """Custom type vRtrMplsLspTempAutoBWMaxBW based on TmnxMplsLspBandwidth"""
    defaultValue = 100000


_VRtrMplsLspTempAutoBWMaxBW_Type.__name__ = "TmnxMplsLspBandwidth"
_VRtrMplsLspTempAutoBWMaxBW_Object = MibTableColumn
vRtrMplsLspTempAutoBWMaxBW = _VRtrMplsLspTempAutoBWMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 6),
    _VRtrMplsLspTempAutoBWMaxBW_Type()
)
vRtrMplsLspTempAutoBWMaxBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWMaxBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWMaxBW.setUnits("megabps")


class _VRtrMplsLspTempAutoBWMinBW_Type(TmnxMplsLspBandwidth):
    """Custom type vRtrMplsLspTempAutoBWMinBW based on TmnxMplsLspBandwidth"""
    defaultValue = 0


_VRtrMplsLspTempAutoBWMinBW_Type.__name__ = "TmnxMplsLspBandwidth"
_VRtrMplsLspTempAutoBWMinBW_Object = MibTableColumn
vRtrMplsLspTempAutoBWMinBW = _VRtrMplsLspTempAutoBWMinBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 7),
    _VRtrMplsLspTempAutoBWMinBW_Type()
)
vRtrMplsLspTempAutoBWMinBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWMinBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWMinBW.setUnits("megabps")


class _VRtrMplsLspTempAutoBWMntrBW_Type(TruthValue):
    """Custom type vRtrMplsLspTempAutoBWMntrBW based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempAutoBWMntrBW_Type.__name__ = "TruthValue"
_VRtrMplsLspTempAutoBWMntrBW_Object = MibTableColumn
vRtrMplsLspTempAutoBWMntrBW = _VRtrMplsLspTempAutoBWMntrBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 8),
    _VRtrMplsLspTempAutoBWMntrBW_Type()
)
vRtrMplsLspTempAutoBWMntrBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWMntrBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWMntrBW.setUnits("megabps")


class _VRtrMplsLspTempAutoBWAdjMult_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWAdjMult based on Unsigned32"""
    defaultValue = 288

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_VRtrMplsLspTempAutoBWAdjMult_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWAdjMult_Object = MibTableColumn
vRtrMplsLspTempAutoBWAdjMult = _VRtrMplsLspTempAutoBWAdjMult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 9),
    _VRtrMplsLspTempAutoBWAdjMult_Type()
)
vRtrMplsLspTempAutoBWAdjMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAdjMult.setStatus("current")


class _VRtrMplsLspTempAutoBWOverFlow_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWOverFlow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_VRtrMplsLspTempAutoBWOverFlow_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWOverFlow_Object = MibTableColumn
vRtrMplsLspTempAutoBWOverFlow = _VRtrMplsLspTempAutoBWOverFlow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 10),
    _VRtrMplsLspTempAutoBWOverFlow_Type()
)
vRtrMplsLspTempAutoBWOverFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWOverFlow.setStatus("current")


class _VRtrMplsLspTempAutoBWOvrFlwThr_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWOvrFlwThr based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_VRtrMplsLspTempAutoBWOvrFlwThr_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWOvrFlwThr_Object = MibTableColumn
vRtrMplsLspTempAutoBWOvrFlwThr = _VRtrMplsLspTempAutoBWOvrFlwThr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 11),
    _VRtrMplsLspTempAutoBWOvrFlwThr_Type()
)
vRtrMplsLspTempAutoBWOvrFlwThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWOvrFlwThr.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWOvrFlwThr.setUnits("percent")


class _VRtrMplsLspTempAutoBWOvrFlwBW_Type(TmnxMplsLspBandwidth):
    """Custom type vRtrMplsLspTempAutoBWOvrFlwBW based on TmnxMplsLspBandwidth"""
    defaultValue = 0


_VRtrMplsLspTempAutoBWOvrFlwBW_Type.__name__ = "TmnxMplsLspBandwidth"
_VRtrMplsLspTempAutoBWOvrFlwBW_Object = MibTableColumn
vRtrMplsLspTempAutoBWOvrFlwBW = _VRtrMplsLspTempAutoBWOvrFlwBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 12),
    _VRtrMplsLspTempAutoBWOvrFlwBW_Type()
)
vRtrMplsLspTempAutoBWOvrFlwBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWOvrFlwBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWOvrFlwBW.setUnits("megabps")


class _VRtrMplsLspTempAutoBWSampMult_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWSampMult based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_VRtrMplsLspTempAutoBWSampMult_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWSampMult_Object = MibTableColumn
vRtrMplsLspTempAutoBWSampMult = _VRtrMplsLspTempAutoBWSampMult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 13),
    _VRtrMplsLspTempAutoBWSampMult_Type()
)
vRtrMplsLspTempAutoBWSampMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWSampMult.setStatus("current")
_VRtrMplsLspTempAutoBWSampTime_Type = Unsigned32
_VRtrMplsLspTempAutoBWSampTime_Object = MibTableColumn
vRtrMplsLspTempAutoBWSampTime = _VRtrMplsLspTempAutoBWSampTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 14),
    _VRtrMplsLspTempAutoBWSampTime_Type()
)
vRtrMplsLspTempAutoBWSampTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWSampTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWSampTime.setUnits("minutes")


class _VRtrMplsLspTempAutoBWInherit_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWInherit based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspTempAutoBWInherit_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWInherit_Object = MibTableColumn
vRtrMplsLspTempAutoBWInherit = _VRtrMplsLspTempAutoBWInherit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 15),
    _VRtrMplsLspTempAutoBWInherit_Type()
)
vRtrMplsLspTempAutoBWInherit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWInherit.setStatus("current")


class _VRtrMplsLspTempAutoBWBeWeight_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWBeWeight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWBeWeight_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWBeWeight_Object = MibTableColumn
vRtrMplsLspTempAutoBWBeWeight = _VRtrMplsLspTempAutoBWBeWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 16),
    _VRtrMplsLspTempAutoBWBeWeight_Type()
)
vRtrMplsLspTempAutoBWBeWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWBeWeight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWBeWeight.setUnits("percent")


class _VRtrMplsLspTempAutoBWL2Weight_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWL2Weight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWL2Weight_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWL2Weight_Object = MibTableColumn
vRtrMplsLspTempAutoBWL2Weight = _VRtrMplsLspTempAutoBWL2Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 17),
    _VRtrMplsLspTempAutoBWL2Weight_Type()
)
vRtrMplsLspTempAutoBWL2Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWL2Weight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWL2Weight.setUnits("percent")


class _VRtrMplsLspTempAutoBWAfWeight_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWAfWeight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWAfWeight_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWAfWeight_Object = MibTableColumn
vRtrMplsLspTempAutoBWAfWeight = _VRtrMplsLspTempAutoBWAfWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 18),
    _VRtrMplsLspTempAutoBWAfWeight_Type()
)
vRtrMplsLspTempAutoBWAfWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAfWeight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAfWeight.setUnits("percent")


class _VRtrMplsLspTempAutoBWL1Weight_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWL1Weight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWL1Weight_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWL1Weight_Object = MibTableColumn
vRtrMplsLspTempAutoBWL1Weight = _VRtrMplsLspTempAutoBWL1Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 19),
    _VRtrMplsLspTempAutoBWL1Weight_Type()
)
vRtrMplsLspTempAutoBWL1Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWL1Weight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWL1Weight.setUnits("percent")


class _VRtrMplsLspTempAutoBWH2Weight_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWH2Weight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWH2Weight_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWH2Weight_Object = MibTableColumn
vRtrMplsLspTempAutoBWH2Weight = _VRtrMplsLspTempAutoBWH2Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 20),
    _VRtrMplsLspTempAutoBWH2Weight_Type()
)
vRtrMplsLspTempAutoBWH2Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWH2Weight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWH2Weight.setUnits("percent")


class _VRtrMplsLspTempAutoBWEfWeight_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWEfWeight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWEfWeight_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWEfWeight_Object = MibTableColumn
vRtrMplsLspTempAutoBWEfWeight = _VRtrMplsLspTempAutoBWEfWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 21),
    _VRtrMplsLspTempAutoBWEfWeight_Type()
)
vRtrMplsLspTempAutoBWEfWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWEfWeight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWEfWeight.setUnits("percent")


class _VRtrMplsLspTempAutoBWH1Weight_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWH1Weight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWH1Weight_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWH1Weight_Object = MibTableColumn
vRtrMplsLspTempAutoBWH1Weight = _VRtrMplsLspTempAutoBWH1Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 22),
    _VRtrMplsLspTempAutoBWH1Weight_Type()
)
vRtrMplsLspTempAutoBWH1Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWH1Weight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWH1Weight.setUnits("percent")


class _VRtrMplsLspTempAutoBWNcWeight_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWNcWeight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWNcWeight_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWNcWeight_Object = MibTableColumn
vRtrMplsLspTempAutoBWNcWeight = _VRtrMplsLspTempAutoBWNcWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 23),
    _VRtrMplsLspTempAutoBWNcWeight_Type()
)
vRtrMplsLspTempAutoBWNcWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWNcWeight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWNcWeight.setUnits("percent")


class _VRtrMplsLspTempAutoBWUnderFlow_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWUnderFlow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_VRtrMplsLspTempAutoBWUnderFlow_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWUnderFlow_Object = MibTableColumn
vRtrMplsLspTempAutoBWUnderFlow = _VRtrMplsLspTempAutoBWUnderFlow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 24),
    _VRtrMplsLspTempAutoBWUnderFlow_Type()
)
vRtrMplsLspTempAutoBWUnderFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWUnderFlow.setStatus("current")


class _VRtrMplsLspTempAutoBWUndFlwThr_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWUndFlwThr based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_VRtrMplsLspTempAutoBWUndFlwThr_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWUndFlwThr_Object = MibTableColumn
vRtrMplsLspTempAutoBWUndFlwThr = _VRtrMplsLspTempAutoBWUndFlwThr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 25),
    _VRtrMplsLspTempAutoBWUndFlwThr_Type()
)
vRtrMplsLspTempAutoBWUndFlwThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWUndFlwThr.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWUndFlwThr.setUnits("percent")


class _VRtrMplsLspTempAutoBWUndFlwBW_Type(TmnxMplsLspBandwidth):
    """Custom type vRtrMplsLspTempAutoBWUndFlwBW based on TmnxMplsLspBandwidth"""
    defaultValue = 0


_VRtrMplsLspTempAutoBWUndFlwBW_Type.__name__ = "TmnxMplsLspBandwidth"
_VRtrMplsLspTempAutoBWUndFlwBW_Object = MibTableColumn
vRtrMplsLspTempAutoBWUndFlwBW = _VRtrMplsLspTempAutoBWUndFlwBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 26),
    _VRtrMplsLspTempAutoBWUndFlwBW_Type()
)
vRtrMplsLspTempAutoBWUndFlwBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWUndFlwBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWUndFlwBW.setUnits("megabps")
_VRtrMplsTemplPlcyBindTblLastChg_Type = TimeStamp
_VRtrMplsTemplPlcyBindTblLastChg_Object = MibScalar
vRtrMplsTemplPlcyBindTblLastChg = _VRtrMplsTemplPlcyBindTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 48),
    _VRtrMplsTemplPlcyBindTblLastChg_Type()
)
vRtrMplsTemplPlcyBindTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTemplPlcyBindTblLastChg.setStatus("current")
_VRtrMplsLspTemplPlcyBindTable_Object = MibTable
vRtrMplsLspTemplPlcyBindTable = _VRtrMplsLspTemplPlcyBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49)
)
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBindTable.setStatus("current")
_VRtrMplsLspTemplPlcyBindEntry_Object = MibTableRow
vRtrMplsLspTemplPlcyBindEntry = _VRtrMplsLspTemplPlcyBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49, 1)
)
vRtrMplsLspTemplPlcyBindEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateName"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBindEntry.setStatus("current")
_VRtrMplsLspTemplPlcyBindLastChg_Type = TimeStamp
_VRtrMplsLspTemplPlcyBindLastChg_Object = MibTableColumn
vRtrMplsLspTemplPlcyBindLastChg = _VRtrMplsLspTemplPlcyBindLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49, 1, 1),
    _VRtrMplsLspTemplPlcyBindLastChg_Type()
)
vRtrMplsLspTemplPlcyBindLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBindLastChg.setStatus("current")
_VRtrMplsLspTemplPlcyBindRowStat_Type = RowStatus
_VRtrMplsLspTemplPlcyBindRowStat_Object = MibTableColumn
vRtrMplsLspTemplPlcyBindRowStat = _VRtrMplsLspTemplPlcyBindRowStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49, 1, 2),
    _VRtrMplsLspTemplPlcyBindRowStat_Type()
)
vRtrMplsLspTemplPlcyBindRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBindRowStat.setStatus("current")


class _VRtrMplsLspTemplPlcyBind1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrMplsLspTemplPlcyBind1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrMplsLspTemplPlcyBind1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrMplsLspTemplPlcyBind1_Object = MibTableColumn
vRtrMplsLspTemplPlcyBind1 = _VRtrMplsLspTemplPlcyBind1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49, 1, 3),
    _VRtrMplsLspTemplPlcyBind1_Type()
)
vRtrMplsLspTemplPlcyBind1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBind1.setStatus("current")


class _VRtrMplsLspTemplPlcyBind2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrMplsLspTemplPlcyBind2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrMplsLspTemplPlcyBind2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrMplsLspTemplPlcyBind2_Object = MibTableColumn
vRtrMplsLspTemplPlcyBind2 = _VRtrMplsLspTemplPlcyBind2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49, 1, 4),
    _VRtrMplsLspTemplPlcyBind2_Type()
)
vRtrMplsLspTemplPlcyBind2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBind2.setStatus("current")


class _VRtrMplsLspTemplPlcyBind3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrMplsLspTemplPlcyBind3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrMplsLspTemplPlcyBind3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrMplsLspTemplPlcyBind3_Object = MibTableColumn
vRtrMplsLspTemplPlcyBind3 = _VRtrMplsLspTemplPlcyBind3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49, 1, 5),
    _VRtrMplsLspTemplPlcyBind3_Type()
)
vRtrMplsLspTemplPlcyBind3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBind3.setStatus("current")


class _VRtrMplsLspTemplPlcyBind4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrMplsLspTemplPlcyBind4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrMplsLspTemplPlcyBind4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrMplsLspTemplPlcyBind4_Object = MibTableColumn
vRtrMplsLspTemplPlcyBind4 = _VRtrMplsLspTemplPlcyBind4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49, 1, 6),
    _VRtrMplsLspTemplPlcyBind4_Type()
)
vRtrMplsLspTemplPlcyBind4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBind4.setStatus("current")


class _VRtrMplsLspTemplPlcyBind5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrMplsLspTemplPlcyBind5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrMplsLspTemplPlcyBind5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrMplsLspTemplPlcyBind5_Object = MibTableColumn
vRtrMplsLspTemplPlcyBind5 = _VRtrMplsLspTemplPlcyBind5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49, 1, 7),
    _VRtrMplsLspTemplPlcyBind5_Type()
)
vRtrMplsLspTemplPlcyBind5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBind5.setStatus("current")


class _VRtrMplsLspTemplPlcyBindOneHop_Type(TruthValue):
    """Custom type vRtrMplsLspTemplPlcyBindOneHop based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTemplPlcyBindOneHop_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplPlcyBindOneHop_Object = MibTableColumn
vRtrMplsLspTemplPlcyBindOneHop = _VRtrMplsLspTemplPlcyBindOneHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49, 1, 8),
    _VRtrMplsLspTemplPlcyBindOneHop_Type()
)
vRtrMplsLspTemplPlcyBindOneHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBindOneHop.setStatus("current")
_VRtrMplsLspTempInStatTblLstChg_Type = TimeStamp
_VRtrMplsLspTempInStatTblLstChg_Object = MibScalar
vRtrMplsLspTempInStatTblLstChg = _VRtrMplsLspTempInStatTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 50),
    _VRtrMplsLspTempInStatTblLstChg_Type()
)
vRtrMplsLspTempInStatTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatTblLstChg.setStatus("current")
_VRtrMplsLspTempInStatTable_Object = MibTable
vRtrMplsLspTempInStatTable = _VRtrMplsLspTempInStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51)
)
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatTable.setStatus("current")
_VRtrMplsLspTempInStatEntry_Object = MibTableRow
vRtrMplsLspTempInStatEntry = _VRtrMplsLspTempInStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1)
)
vRtrMplsLspTempInStatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatType"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatSndrAddrTyp"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatSndrAddr"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatLspNamePref"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatEntry.setStatus("current")


class _VRtrMplsLspTempInStatType_Type(Integer32):
    """Custom type vRtrMplsLspTempInStatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("p2p", 1),
          ("p2mp", 2))
    )


_VRtrMplsLspTempInStatType_Type.__name__ = "Integer32"
_VRtrMplsLspTempInStatType_Object = MibTableColumn
vRtrMplsLspTempInStatType = _VRtrMplsLspTempInStatType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 1),
    _VRtrMplsLspTempInStatType_Type()
)
vRtrMplsLspTempInStatType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatType.setStatus("current")
_VRtrMplsLspTempInStatSndrAddrTyp_Type = InetAddressType
_VRtrMplsLspTempInStatSndrAddrTyp_Object = MibTableColumn
vRtrMplsLspTempInStatSndrAddrTyp = _VRtrMplsLspTempInStatSndrAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 2),
    _VRtrMplsLspTempInStatSndrAddrTyp_Type()
)
vRtrMplsLspTempInStatSndrAddrTyp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatSndrAddrTyp.setStatus("current")


class _VRtrMplsLspTempInStatSndrAddr_Type(InetAddress):
    """Custom type vRtrMplsLspTempInStatSndrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsLspTempInStatSndrAddr_Type.__name__ = "InetAddress"
_VRtrMplsLspTempInStatSndrAddr_Object = MibTableColumn
vRtrMplsLspTempInStatSndrAddr = _VRtrMplsLspTempInStatSndrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 3),
    _VRtrMplsLspTempInStatSndrAddr_Type()
)
vRtrMplsLspTempInStatSndrAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatSndrAddr.setStatus("current")
_VRtrMplsLspTempInStatLspNamePref_Type = TLNamedItem
_VRtrMplsLspTempInStatLspNamePref_Object = MibTableColumn
vRtrMplsLspTempInStatLspNamePref = _VRtrMplsLspTempInStatLspNamePref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 4),
    _VRtrMplsLspTempInStatLspNamePref_Type()
)
vRtrMplsLspTempInStatLspNamePref.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatLspNamePref.setStatus("current")
_VRtrMplsLspTempInStatRowStatus_Type = RowStatus
_VRtrMplsLspTempInStatRowStatus_Object = MibTableColumn
vRtrMplsLspTempInStatRowStatus = _VRtrMplsLspTempInStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 5),
    _VRtrMplsLspTempInStatRowStatus_Type()
)
vRtrMplsLspTempInStatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatRowStatus.setStatus("current")
_VRtrMplsLspTempInStatLastChanged_Type = TimeStamp
_VRtrMplsLspTempInStatLastChanged_Object = MibTableColumn
vRtrMplsLspTempInStatLastChanged = _VRtrMplsLspTempInStatLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 6),
    _VRtrMplsLspTempInStatLastChanged_Type()
)
vRtrMplsLspTempInStatLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatLastChanged.setStatus("current")


class _VRtrMplsLspTempInStatCollectStat_Type(TruthValue):
    """Custom type vRtrMplsLspTempInStatCollectStat based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempInStatCollectStat_Type.__name__ = "TruthValue"
_VRtrMplsLspTempInStatCollectStat_Object = MibTableColumn
vRtrMplsLspTempInStatCollectStat = _VRtrMplsLspTempInStatCollectStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 7),
    _VRtrMplsLspTempInStatCollectStat_Type()
)
vRtrMplsLspTempInStatCollectStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatCollectStat.setStatus("current")


class _VRtrMplsLspTempInStatAccntPolicy_Type(Unsigned32):
    """Custom type vRtrMplsLspTempInStatAccntPolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 99),
    )


_VRtrMplsLspTempInStatAccntPolicy_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempInStatAccntPolicy_Object = MibTableColumn
vRtrMplsLspTempInStatAccntPolicy = _VRtrMplsLspTempInStatAccntPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 8),
    _VRtrMplsLspTempInStatAccntPolicy_Type()
)
vRtrMplsLspTempInStatAccntPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatAccntPolicy.setStatus("current")


class _VRtrMplsLspTempInStatAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsLspTempInStatAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsLspTempInStatAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsLspTempInStatAdminState_Object = MibTableColumn
vRtrMplsLspTempInStatAdminState = _VRtrMplsLspTempInStatAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 9),
    _VRtrMplsLspTempInStatAdminState_Type()
)
vRtrMplsLspTempInStatAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatAdminState.setStatus("current")


class _VRtrMplsLspTempInStatMaxStats_Type(Unsigned32):
    """Custom type vRtrMplsLspTempInStatMaxStats based on Unsigned32"""
    defaultValue = 8191

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_VRtrMplsLspTempInStatMaxStats_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempInStatMaxStats_Object = MibTableColumn
vRtrMplsLspTempInStatMaxStats = _VRtrMplsLspTempInStatMaxStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 10),
    _VRtrMplsLspTempInStatMaxStats_Type()
)
vRtrMplsLspTempInStatMaxStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatMaxStats.setStatus("current")
_VRtrMplsLspTempInStatTotlSession_Type = Unsigned32
_VRtrMplsLspTempInStatTotlSession_Object = MibTableColumn
vRtrMplsLspTempInStatTotlSession = _VRtrMplsLspTempInStatTotlSession_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 11),
    _VRtrMplsLspTempInStatTotlSession_Type()
)
vRtrMplsLspTempInStatTotlSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatTotlSession.setStatus("current")


class _VRtrMplsLspTempInStatsMode_Type(Integer32):
    """Custom type vRtrMplsLspTempInStatsMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("per-fc", 0),
          ("aggregate", 1))
    )


_VRtrMplsLspTempInStatsMode_Type.__name__ = "Integer32"
_VRtrMplsLspTempInStatsMode_Object = MibTableColumn
vRtrMplsLspTempInStatsMode = _VRtrMplsLspTempInStatsMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 12),
    _VRtrMplsLspTempInStatsMode_Type()
)
vRtrMplsLspTempInStatsMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatsMode.setStatus("current")
_VRtrMplsLspExtTable_Object = MibTable
vRtrMplsLspExtTable = _VRtrMplsLspExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52)
)
if mibBuilder.loadTexts:
    vRtrMplsLspExtTable.setStatus("current")
_VRtrMplsLspExtEntry_Object = MibTableRow
vRtrMplsLspExtEntry = _VRtrMplsLspExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsLspExtEntry.setStatus("current")


class _VRtrMplsLspExtPceCompute_Type(TruthValue):
    """Custom type vRtrMplsLspExtPceCompute based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspExtPceCompute_Type.__name__ = "TruthValue"
_VRtrMplsLspExtPceCompute_Object = MibTableColumn
vRtrMplsLspExtPceCompute = _VRtrMplsLspExtPceCompute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 1),
    _VRtrMplsLspExtPceCompute_Type()
)
vRtrMplsLspExtPceCompute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtPceCompute.setStatus("obsolete")


class _VRtrMplsLspExtPceControl_Type(TruthValue):
    """Custom type vRtrMplsLspExtPceControl based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspExtPceControl_Type.__name__ = "TruthValue"
_VRtrMplsLspExtPceControl_Object = MibTableColumn
vRtrMplsLspExtPceControl = _VRtrMplsLspExtPceControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 2),
    _VRtrMplsLspExtPceControl_Type()
)
vRtrMplsLspExtPceControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtPceControl.setStatus("current")


class _VRtrMplsLspExtPceReport_Type(Integer32):
    """Custom type vRtrMplsLspExtPceReport based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("inherit", 3))
    )


_VRtrMplsLspExtPceReport_Type.__name__ = "Integer32"
_VRtrMplsLspExtPceReport_Object = MibTableColumn
vRtrMplsLspExtPceReport = _VRtrMplsLspExtPceReport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 3),
    _VRtrMplsLspExtPceReport_Type()
)
vRtrMplsLspExtPceReport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtPceReport.setStatus("current")
_VRtrMplsLspExtTtmTunnelId_Type = Unsigned32
_VRtrMplsLspExtTtmTunnelId_Object = MibTableColumn
vRtrMplsLspExtTtmTunnelId = _VRtrMplsLspExtTtmTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 4),
    _VRtrMplsLspExtTtmTunnelId_Type()
)
vRtrMplsLspExtTtmTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspExtTtmTunnelId.setStatus("current")


class _VRtrMplsLspExtMaxSrLabels_Type(Unsigned32):
    """Custom type vRtrMplsLspExtMaxSrLabels based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_VRtrMplsLspExtMaxSrLabels_Type.__name__ = "Unsigned32"
_VRtrMplsLspExtMaxSrLabels_Object = MibTableColumn
vRtrMplsLspExtMaxSrLabels = _VRtrMplsLspExtMaxSrLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 5),
    _VRtrMplsLspExtMaxSrLabels_Type()
)
vRtrMplsLspExtMaxSrLabels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtMaxSrLabels.setStatus("current")
_VRtrMplsLspExtTunnelId_Type = Unsigned32
_VRtrMplsLspExtTunnelId_Object = MibTableColumn
vRtrMplsLspExtTunnelId = _VRtrMplsLspExtTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 6),
    _VRtrMplsLspExtTunnelId_Type()
)
vRtrMplsLspExtTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspExtTunnelId.setStatus("current")


class _VRtrMplsLspExtEntropyLabel_Type(Integer32):
    """Custom type vRtrMplsLspExtEntropyLabel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forceDisable", 1),
          ("enable", 2),
          ("inherit", 3))
    )


_VRtrMplsLspExtEntropyLabel_Type.__name__ = "Integer32"
_VRtrMplsLspExtEntropyLabel_Object = MibTableColumn
vRtrMplsLspExtEntropyLabel = _VRtrMplsLspExtEntropyLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 7),
    _VRtrMplsLspExtEntropyLabel_Type()
)
vRtrMplsLspExtEntropyLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtEntropyLabel.setStatus("current")


class _VRtrMplsLspExtOperEntropyLabel_Type(Integer32):
    """Custom type vRtrMplsLspExtOperEntropyLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceDisable", 1),
          ("enable", 2))
    )


_VRtrMplsLspExtOperEntropyLabel_Type.__name__ = "Integer32"
_VRtrMplsLspExtOperEntropyLabel_Object = MibTableColumn
vRtrMplsLspExtOperEntropyLabel = _VRtrMplsLspExtOperEntropyLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 8),
    _VRtrMplsLspExtOperEntropyLabel_Type()
)
vRtrMplsLspExtOperEntropyLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspExtOperEntropyLabel.setStatus("current")


class _VRtrMplsLspExtFrrOverheadLabel_Type(Unsigned32):
    """Custom type vRtrMplsLspExtFrrOverheadLabel based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VRtrMplsLspExtFrrOverheadLabel_Type.__name__ = "Unsigned32"
_VRtrMplsLspExtFrrOverheadLabel_Object = MibTableColumn
vRtrMplsLspExtFrrOverheadLabel = _VRtrMplsLspExtFrrOverheadLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 9),
    _VRtrMplsLspExtFrrOverheadLabel_Type()
)
vRtrMplsLspExtFrrOverheadLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtFrrOverheadLabel.setStatus("current")


class _VRtrMplsLspExtNegEntropyLbl_Type(Integer32):
    """Custom type vRtrMplsLspExtNegEntropyLbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceDisable", 1),
          ("enable", 2))
    )


_VRtrMplsLspExtNegEntropyLbl_Type.__name__ = "Integer32"
_VRtrMplsLspExtNegEntropyLbl_Object = MibTableColumn
vRtrMplsLspExtNegEntropyLbl = _VRtrMplsLspExtNegEntropyLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 10),
    _VRtrMplsLspExtNegEntropyLbl_Type()
)
vRtrMplsLspExtNegEntropyLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspExtNegEntropyLbl.setStatus("current")


class _VRtrMplsLspExtBfdFailureAction_Type(Integer32):
    """Custom type vRtrMplsLspExtBfdFailureAction based on Integer32"""
    defaultValue = 0

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
          ("down", 1),
          ("failover", 2),
          ("failoverOrDown", 3))
    )


_VRtrMplsLspExtBfdFailureAction_Type.__name__ = "Integer32"
_VRtrMplsLspExtBfdFailureAction_Object = MibTableColumn
vRtrMplsLspExtBfdFailureAction = _VRtrMplsLspExtBfdFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 11),
    _VRtrMplsLspExtBfdFailureAction_Type()
)
vRtrMplsLspExtBfdFailureAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtBfdFailureAction.setStatus("current")


class _VRtrMplsLspExtCbfFwdingPlcy_Type(TNamedItemOrEmpty):
    """Custom type vRtrMplsLspExtCbfFwdingPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_VRtrMplsLspExtCbfFwdingPlcy_Type.__name__ = "TNamedItemOrEmpty"
_VRtrMplsLspExtCbfFwdingPlcy_Object = MibTableColumn
vRtrMplsLspExtCbfFwdingPlcy = _VRtrMplsLspExtCbfFwdingPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 12),
    _VRtrMplsLspExtCbfFwdingPlcy_Type()
)
vRtrMplsLspExtCbfFwdingPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtCbfFwdingPlcy.setStatus("current")


class _VRtrMplsLspExtCbfFwdingSet_Type(Unsigned32):
    """Custom type vRtrMplsLspExtCbfFwdingSet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_VRtrMplsLspExtCbfFwdingSet_Type.__name__ = "Unsigned32"
_VRtrMplsLspExtCbfFwdingSet_Object = MibTableColumn
vRtrMplsLspExtCbfFwdingSet = _VRtrMplsLspExtCbfFwdingSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 13),
    _VRtrMplsLspExtCbfFwdingSet_Type()
)
vRtrMplsLspExtCbfFwdingSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtCbfFwdingSet.setStatus("current")


class _VRtrMplsLspExtPathCompMeth_Type(Integer32):
    """Custom type vRtrMplsLspExtPathCompMeth based on Integer32"""
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
          ("localCspf", 2),
          ("pce", 3))
    )


_VRtrMplsLspExtPathCompMeth_Type.__name__ = "Integer32"
_VRtrMplsLspExtPathCompMeth_Object = MibTableColumn
vRtrMplsLspExtPathCompMeth = _VRtrMplsLspExtPathCompMeth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 14),
    _VRtrMplsLspExtPathCompMeth_Type()
)
vRtrMplsLspExtPathCompMeth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtPathCompMeth.setStatus("current")


class _VRtrMplsLspExtMetricType_Type(Integer32):
    """Custom type vRtrMplsLspExtMetricType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igp", 1),
          ("te", 2))
    )


_VRtrMplsLspExtMetricType_Type.__name__ = "Integer32"
_VRtrMplsLspExtMetricType_Object = MibTableColumn
vRtrMplsLspExtMetricType = _VRtrMplsLspExtMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 15),
    _VRtrMplsLspExtMetricType_Type()
)
vRtrMplsLspExtMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtMetricType.setStatus("current")


class _VRtrMplsLspExtLocalSrProt_Type(Integer32):
    """Custom type vRtrMplsLspExtLocalSrProt based on Integer32"""
    defaultValue = 2

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
          ("preferred", 2),
          ("mandatory", 3))
    )


_VRtrMplsLspExtLocalSrProt_Type.__name__ = "Integer32"
_VRtrMplsLspExtLocalSrProt_Object = MibTableColumn
vRtrMplsLspExtLocalSrProt = _VRtrMplsLspExtLocalSrProt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 16),
    _VRtrMplsLspExtLocalSrProt_Type()
)
vRtrMplsLspExtLocalSrProt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtLocalSrProt.setStatus("current")


class _VRtrMplsLspExtLabelStackRed_Type(TruthValue):
    """Custom type vRtrMplsLspExtLabelStackRed based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspExtLabelStackRed_Type.__name__ = "TruthValue"
_VRtrMplsLspExtLabelStackRed_Object = MibTableColumn
vRtrMplsLspExtLabelStackRed = _VRtrMplsLspExtLabelStackRed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 17),
    _VRtrMplsLspExtLabelStackRed_Type()
)
vRtrMplsLspExtLabelStackRed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtLabelStackRed.setStatus("current")


class _VRtrMplsLspExtBfdUpWaitTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspExtBfdUpWaitTimer based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrMplsLspExtBfdUpWaitTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspExtBfdUpWaitTimer_Object = MibTableColumn
vRtrMplsLspExtBfdUpWaitTimer = _VRtrMplsLspExtBfdUpWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 18),
    _VRtrMplsLspExtBfdUpWaitTimer_Type()
)
vRtrMplsLspExtBfdUpWaitTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtBfdUpWaitTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspExtBfdUpWaitTimer.setUnits("seconds")


class _VRtrMplsLspExtSelfPing_Type(Integer32):
    """Custom type vRtrMplsLspExtSelfPing based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("inherit", 3))
    )


_VRtrMplsLspExtSelfPing_Type.__name__ = "Integer32"
_VRtrMplsLspExtSelfPing_Object = MibTableColumn
vRtrMplsLspExtSelfPing = _VRtrMplsLspExtSelfPing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 19),
    _VRtrMplsLspExtSelfPing_Type()
)
vRtrMplsLspExtSelfPing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtSelfPing.setStatus("current")


class _VRtrMplsLspExtFallbkPathComp_Type(Integer32):
    """Custom type vRtrMplsLspExtFallbkPathComp based on Integer32"""
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
        *(("notApplicable", 0),
          ("none", 1),
          ("localCspf", 2))
    )


_VRtrMplsLspExtFallbkPathComp_Type.__name__ = "Integer32"
_VRtrMplsLspExtFallbkPathComp_Object = MibTableColumn
vRtrMplsLspExtFallbkPathComp = _VRtrMplsLspExtFallbkPathComp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 20),
    _VRtrMplsLspExtFallbkPathComp_Type()
)
vRtrMplsLspExtFallbkPathComp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtFallbkPathComp.setStatus("current")


class _VRtrMplsLspExtTriggerManualSw_Type(Integer32):
    """Custom type vRtrMplsLspExtTriggerManualSw based on Integer32"""
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
        *(("noAction", 0),
          ("switchAway", 1),
          ("switchBack", 2))
    )


_VRtrMplsLspExtTriggerManualSw_Type.__name__ = "Integer32"
_VRtrMplsLspExtTriggerManualSw_Object = MibTableColumn
vRtrMplsLspExtTriggerManualSw = _VRtrMplsLspExtTriggerManualSw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 21),
    _VRtrMplsLspExtTriggerManualSw_Type()
)
vRtrMplsLspExtTriggerManualSw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtTriggerManualSw.setStatus("current")
_VRtrMplsLspExtActivePathIndex_Type = MplsTunnelIndex
_VRtrMplsLspExtActivePathIndex_Object = MibTableColumn
vRtrMplsLspExtActivePathIndex = _VRtrMplsLspExtActivePathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 22),
    _VRtrMplsLspExtActivePathIndex_Type()
)
vRtrMplsLspExtActivePathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspExtActivePathIndex.setStatus("current")


class _VRtrMplsLspExtOverrideTunElc_Type(TruthValue):
    """Custom type vRtrMplsLspExtOverrideTunElc based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspExtOverrideTunElc_Type.__name__ = "TruthValue"
_VRtrMplsLspExtOverrideTunElc_Object = MibTableColumn
vRtrMplsLspExtOverrideTunElc = _VRtrMplsLspExtOverrideTunElc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 23),
    _VRtrMplsLspExtOverrideTunElc_Type()
)
vRtrMplsLspExtOverrideTunElc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtOverrideTunElc.setStatus("current")


class _VRtrMplsLspExtPrefTransFrr_Type(TruthValue):
    """Custom type vRtrMplsLspExtPrefTransFrr based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspExtPrefTransFrr_Type.__name__ = "TruthValue"
_VRtrMplsLspExtPrefTransFrr_Object = MibTableColumn
vRtrMplsLspExtPrefTransFrr = _VRtrMplsLspExtPrefTransFrr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 24),
    _VRtrMplsLspExtPrefTransFrr_Type()
)
vRtrMplsLspExtPrefTransFrr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtPrefTransFrr.setStatus("current")


class _VRtrMplsLspExtBfdReturnPathLabel_Type(Unsigned32):
    """Custom type vRtrMplsLspExtBfdReturnPathLabel based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1048512),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_VRtrMplsLspExtBfdReturnPathLabel_Type.__name__ = "Unsigned32"
_VRtrMplsLspExtBfdReturnPathLabel_Object = MibTableColumn
vRtrMplsLspExtBfdReturnPathLabel = _VRtrMplsLspExtBfdReturnPathLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 25),
    _VRtrMplsLspExtBfdReturnPathLabel_Type()
)
vRtrMplsLspExtBfdReturnPathLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtBfdReturnPathLabel.setStatus("current")


class _VRtrMplsLspExtSoftPreemption_Type(TruthValue):
    """Custom type vRtrMplsLspExtSoftPreemption based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspExtSoftPreemption_Type.__name__ = "TruthValue"
_VRtrMplsLspExtSoftPreemption_Object = MibTableColumn
vRtrMplsLspExtSoftPreemption = _VRtrMplsLspExtSoftPreemption_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 26),
    _VRtrMplsLspExtSoftPreemption_Type()
)
vRtrMplsLspExtSoftPreemption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtSoftPreemption.setStatus("current")
_VRtrMplsLspPathProfTblLstChg_Type = TimeStamp
_VRtrMplsLspPathProfTblLstChg_Object = MibScalar
vRtrMplsLspPathProfTblLstChg = _VRtrMplsLspPathProfTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 53),
    _VRtrMplsLspPathProfTblLstChg_Type()
)
vRtrMplsLspPathProfTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathProfTblLstChg.setStatus("current")
_VRtrMplsLspPathProfTable_Object = MibTable
vRtrMplsLspPathProfTable = _VRtrMplsLspPathProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 54)
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathProfTable.setStatus("current")
_VRtrMplsLspPathProfEntry_Object = MibTableRow
vRtrMplsLspPathProfEntry = _VRtrMplsLspPathProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 54, 1)
)
vRtrMplsLspPathProfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspPathProfId"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathProfEntry.setStatus("current")


class _VRtrMplsLspPathProfId_Type(Unsigned32):
    """Custom type vRtrMplsLspPathProfId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VRtrMplsLspPathProfId_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathProfId_Object = MibTableColumn
vRtrMplsLspPathProfId = _VRtrMplsLspPathProfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 54, 1, 1),
    _VRtrMplsLspPathProfId_Type()
)
vRtrMplsLspPathProfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspPathProfId.setStatus("current")
_VRtrMplsLspPathProfRowStatus_Type = RowStatus
_VRtrMplsLspPathProfRowStatus_Object = MibTableColumn
vRtrMplsLspPathProfRowStatus = _VRtrMplsLspPathProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 54, 1, 2),
    _VRtrMplsLspPathProfRowStatus_Type()
)
vRtrMplsLspPathProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathProfRowStatus.setStatus("current")
_VRtrMplsLspPathProfLastChange_Type = TimeStamp
_VRtrMplsLspPathProfLastChange_Object = MibTableColumn
vRtrMplsLspPathProfLastChange = _VRtrMplsLspPathProfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 54, 1, 3),
    _VRtrMplsLspPathProfLastChange_Type()
)
vRtrMplsLspPathProfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathProfLastChange.setStatus("current")


class _VRtrMplsLspPathProfGroupId_Type(Unsigned32):
    """Custom type vRtrMplsLspPathProfGroupId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrMplsLspPathProfGroupId_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathProfGroupId_Object = MibTableColumn
vRtrMplsLspPathProfGroupId = _VRtrMplsLspPathProfGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 54, 1, 4),
    _VRtrMplsLspPathProfGroupId_Type()
)
vRtrMplsLspPathProfGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathProfGroupId.setStatus("current")
_VRtrMplsClassFwdPlcyTblLstChg_Type = TimeStamp
_VRtrMplsClassFwdPlcyTblLstChg_Object = MibScalar
vRtrMplsClassFwdPlcyTblLstChg = _VRtrMplsClassFwdPlcyTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 55),
    _VRtrMplsClassFwdPlcyTblLstChg_Type()
)
vRtrMplsClassFwdPlcyTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyTblLstChg.setStatus("current")
_VRtrMplsClassFwdPlcyTable_Object = MibTable
vRtrMplsClassFwdPlcyTable = _VRtrMplsClassFwdPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56)
)
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyTable.setStatus("current")
_VRtrMplsClassFwdPlcyEntry_Object = MibTableRow
vRtrMplsClassFwdPlcyEntry = _VRtrMplsClassFwdPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1)
)
vRtrMplsClassFwdPlcyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyName"),
)
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyEntry.setStatus("current")
_VRtrMplsClassFwdPlcyName_Type = TNamedItem
_VRtrMplsClassFwdPlcyName_Object = MibTableColumn
vRtrMplsClassFwdPlcyName = _VRtrMplsClassFwdPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1, 1),
    _VRtrMplsClassFwdPlcyName_Type()
)
vRtrMplsClassFwdPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyName.setStatus("current")
_VRtrMplsClassFwdPlcyRowStatus_Type = RowStatus
_VRtrMplsClassFwdPlcyRowStatus_Object = MibTableColumn
vRtrMplsClassFwdPlcyRowStatus = _VRtrMplsClassFwdPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1, 2),
    _VRtrMplsClassFwdPlcyRowStatus_Type()
)
vRtrMplsClassFwdPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyRowStatus.setStatus("current")
_VRtrMplsClassFwdPlcyLastChanged_Type = TimeStamp
_VRtrMplsClassFwdPlcyLastChanged_Object = MibTableColumn
vRtrMplsClassFwdPlcyLastChanged = _VRtrMplsClassFwdPlcyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1, 3),
    _VRtrMplsClassFwdPlcyLastChanged_Type()
)
vRtrMplsClassFwdPlcyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyLastChanged.setStatus("current")


class _VRtrMplsClassFwdPlcyDefSetId_Type(Unsigned32):
    """Custom type vRtrMplsClassFwdPlcyDefSetId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_VRtrMplsClassFwdPlcyDefSetId_Type.__name__ = "Unsigned32"
_VRtrMplsClassFwdPlcyDefSetId_Object = MibTableColumn
vRtrMplsClassFwdPlcyDefSetId = _VRtrMplsClassFwdPlcyDefSetId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1, 4),
    _VRtrMplsClassFwdPlcyDefSetId_Type()
)
vRtrMplsClassFwdPlcyDefSetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyDefSetId.setStatus("current")
_VRtrMplsClassFwdPlcyRefCount_Type = Gauge32
_VRtrMplsClassFwdPlcyRefCount_Object = MibTableColumn
vRtrMplsClassFwdPlcyRefCount = _VRtrMplsClassFwdPlcyRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1, 5),
    _VRtrMplsClassFwdPlcyRefCount_Type()
)
vRtrMplsClassFwdPlcyRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyRefCount.setStatus("current")
_VRtrMplsClassFwdPlcyFCTblLstChg_Type = TimeStamp
_VRtrMplsClassFwdPlcyFCTblLstChg_Object = MibScalar
vRtrMplsClassFwdPlcyFCTblLstChg = _VRtrMplsClassFwdPlcyFCTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 57),
    _VRtrMplsClassFwdPlcyFCTblLstChg_Type()
)
vRtrMplsClassFwdPlcyFCTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyFCTblLstChg.setStatus("current")
_VRtrMplsClassFwdPlcyFCTable_Object = MibTable
vRtrMplsClassFwdPlcyFCTable = _VRtrMplsClassFwdPlcyFCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 58)
)
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyFCTable.setStatus("current")
_VRtrMplsClassFwdPlcyFCEntry_Object = MibTableRow
vRtrMplsClassFwdPlcyFCEntry = _VRtrMplsClassFwdPlcyFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 58, 1)
)
vRtrMplsClassFwdPlcyFCEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyName"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyFC"),
)
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyFCEntry.setStatus("current")
_VRtrMplsClassFwdPlcyFC_Type = TFCType
_VRtrMplsClassFwdPlcyFC_Object = MibTableColumn
vRtrMplsClassFwdPlcyFC = _VRtrMplsClassFwdPlcyFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 58, 1, 1),
    _VRtrMplsClassFwdPlcyFC_Type()
)
vRtrMplsClassFwdPlcyFC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyFC.setStatus("current")


class _VRtrMplsClassFwdPlcyFCSetId_Type(Unsigned32):
    """Custom type vRtrMplsClassFwdPlcyFCSetId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_VRtrMplsClassFwdPlcyFCSetId_Type.__name__ = "Unsigned32"
_VRtrMplsClassFwdPlcyFCSetId_Object = MibTableColumn
vRtrMplsClassFwdPlcyFCSetId = _VRtrMplsClassFwdPlcyFCSetId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 58, 1, 2),
    _VRtrMplsClassFwdPlcyFCSetId_Type()
)
vRtrMplsClassFwdPlcyFCSetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyFCSetId.setStatus("current")
_VRtrMplsReservedLblBlkTblLastChg_Type = TimeStamp
_VRtrMplsReservedLblBlkTblLastChg_Object = MibScalar
vRtrMplsReservedLblBlkTblLastChg = _VRtrMplsReservedLblBlkTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 59),
    _VRtrMplsReservedLblBlkTblLastChg_Type()
)
vRtrMplsReservedLblBlkTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsReservedLblBlkTblLastChg.setStatus("current")
_VRtrMplsReservedLblBlkTable_Object = MibTable
vRtrMplsReservedLblBlkTable = _VRtrMplsReservedLblBlkTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 60)
)
if mibBuilder.loadTexts:
    vRtrMplsReservedLblBlkTable.setStatus("current")
_VRtrMplsReservedLblBlkEntry_Object = MibTableRow
vRtrMplsReservedLblBlkEntry = _VRtrMplsReservedLblBlkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 60, 1)
)
vRtrMplsReservedLblBlkEntry.setIndexNames(
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsReservedLblBlkName"),
)
if mibBuilder.loadTexts:
    vRtrMplsReservedLblBlkEntry.setStatus("current")
_VRtrMplsReservedLblBlkName_Type = TLNamedItem
_VRtrMplsReservedLblBlkName_Object = MibTableColumn
vRtrMplsReservedLblBlkName = _VRtrMplsReservedLblBlkName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 60, 1, 1),
    _VRtrMplsReservedLblBlkName_Type()
)
vRtrMplsReservedLblBlkName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsReservedLblBlkName.setStatus("current")
_VRtrMplsReservedLblBlkRowStatus_Type = RowStatus
_VRtrMplsReservedLblBlkRowStatus_Object = MibTableColumn
vRtrMplsReservedLblBlkRowStatus = _VRtrMplsReservedLblBlkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 60, 1, 2),
    _VRtrMplsReservedLblBlkRowStatus_Type()
)
vRtrMplsReservedLblBlkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsReservedLblBlkRowStatus.setStatus("current")
_VRtrMplsReservedLblBlkLastChg_Type = TimeStamp
_VRtrMplsReservedLblBlkLastChg_Object = MibTableColumn
vRtrMplsReservedLblBlkLastChg = _VRtrMplsReservedLblBlkLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 60, 1, 3),
    _VRtrMplsReservedLblBlkLastChg_Type()
)
vRtrMplsReservedLblBlkLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsReservedLblBlkLastChg.setStatus("current")
_VRtrMplsReservedLblBlkStartLbl_Type = TmnxMplsLabelOrZero
_VRtrMplsReservedLblBlkStartLbl_Object = MibTableColumn
vRtrMplsReservedLblBlkStartLbl = _VRtrMplsReservedLblBlkStartLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 60, 1, 4),
    _VRtrMplsReservedLblBlkStartLbl_Type()
)
vRtrMplsReservedLblBlkStartLbl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsReservedLblBlkStartLbl.setStatus("current")
_VRtrMplsReservedLblBlkEndLbl_Type = TmnxMplsLabelOrZero
_VRtrMplsReservedLblBlkEndLbl_Object = MibTableColumn
vRtrMplsReservedLblBlkEndLbl = _VRtrMplsReservedLblBlkEndLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 60, 1, 5),
    _VRtrMplsReservedLblBlkEndLbl_Type()
)
vRtrMplsReservedLblBlkEndLbl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsReservedLblBlkEndLbl.setStatus("current")
_VRtrMplsLspAdminTagTblLastChg_Type = TimeStamp
_VRtrMplsLspAdminTagTblLastChg_Object = MibScalar
vRtrMplsLspAdminTagTblLastChg = _VRtrMplsLspAdminTagTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 61),
    _VRtrMplsLspAdminTagTblLastChg_Type()
)
vRtrMplsLspAdminTagTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAdminTagTblLastChg.setStatus("current")
_VRtrMplsLspAdminTagTable_Object = MibTable
vRtrMplsLspAdminTagTable = _VRtrMplsLspAdminTagTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 62)
)
if mibBuilder.loadTexts:
    vRtrMplsLspAdminTagTable.setStatus("current")
_VRtrMplsLspAdminTagEntry_Object = MibTableRow
vRtrMplsLspAdminTagEntry = _VRtrMplsLspAdminTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 62, 1)
)
vRtrMplsLspAdminTagEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspAdminTagName"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspAdminTagEntry.setStatus("current")
_VRtrMplsLspAdminTagName_Type = TNamedItem
_VRtrMplsLspAdminTagName_Object = MibTableColumn
vRtrMplsLspAdminTagName = _VRtrMplsLspAdminTagName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 62, 1, 1),
    _VRtrMplsLspAdminTagName_Type()
)
vRtrMplsLspAdminTagName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspAdminTagName.setStatus("current")
_VRtrMplsLspAdminTagRowStatus_Type = RowStatus
_VRtrMplsLspAdminTagRowStatus_Object = MibTableColumn
vRtrMplsLspAdminTagRowStatus = _VRtrMplsLspAdminTagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 62, 1, 2),
    _VRtrMplsLspAdminTagRowStatus_Type()
)
vRtrMplsLspAdminTagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAdminTagRowStatus.setStatus("current")
_VRtrMplsLspAdminTagLastChanged_Type = TimeStamp
_VRtrMplsLspAdminTagLastChanged_Object = MibTableColumn
vRtrMplsLspAdminTagLastChanged = _VRtrMplsLspAdminTagLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 62, 1, 3),
    _VRtrMplsLspAdminTagLastChanged_Type()
)
vRtrMplsLspAdminTagLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAdminTagLastChanged.setStatus("current")
_VRtrMplsLspTempAdminTagTblLstChg_Type = TimeStamp
_VRtrMplsLspTempAdminTagTblLstChg_Object = MibScalar
vRtrMplsLspTempAdminTagTblLstChg = _VRtrMplsLspTempAdminTagTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 63),
    _VRtrMplsLspTempAdminTagTblLstChg_Type()
)
vRtrMplsLspTempAdminTagTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAdminTagTblLstChg.setStatus("current")
_VRtrMplsLspTempAdminTagTable_Object = MibTable
vRtrMplsLspTempAdminTagTable = _VRtrMplsLspTempAdminTagTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 64)
)
if mibBuilder.loadTexts:
    vRtrMplsLspTempAdminTagTable.setStatus("current")
_VRtrMplsLspTempAdminTagEntry_Object = MibTableRow
vRtrMplsLspTempAdminTagEntry = _VRtrMplsLspTempAdminTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 64, 1)
)
vRtrMplsLspTempAdminTagEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateName"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspTempAdminTagName"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspTempAdminTagEntry.setStatus("current")
_VRtrMplsLspTempAdminTagName_Type = TNamedItem
_VRtrMplsLspTempAdminTagName_Object = MibTableColumn
vRtrMplsLspTempAdminTagName = _VRtrMplsLspTempAdminTagName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 64, 1, 1),
    _VRtrMplsLspTempAdminTagName_Type()
)
vRtrMplsLspTempAdminTagName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAdminTagName.setStatus("current")
_VRtrMplsLspTempAdminTagRowStatus_Type = RowStatus
_VRtrMplsLspTempAdminTagRowStatus_Object = MibTableColumn
vRtrMplsLspTempAdminTagRowStatus = _VRtrMplsLspTempAdminTagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 64, 1, 2),
    _VRtrMplsLspTempAdminTagRowStatus_Type()
)
vRtrMplsLspTempAdminTagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAdminTagRowStatus.setStatus("current")
_VRtrMplsLspTempAdminTagLastChg_Type = TimeStamp
_VRtrMplsLspTempAdminTagLastChg_Object = MibTableColumn
vRtrMplsLspTempAdminTagLastChg = _VRtrMplsLspTempAdminTagLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 64, 1, 3),
    _VRtrMplsLspTempAdminTagLastChg_Type()
)
vRtrMplsLspTempAdminTagLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAdminTagLastChg.setStatus("current")
_VRtrMplsFwdPlcyTblLastChg_Type = TimeStamp
_VRtrMplsFwdPlcyTblLastChg_Object = MibScalar
vRtrMplsFwdPlcyTblLastChg = _VRtrMplsFwdPlcyTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 65),
    _VRtrMplsFwdPlcyTblLastChg_Type()
)
vRtrMplsFwdPlcyTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyTblLastChg.setStatus("current")
_VRtrMplsFwdPlcyTable_Object = MibTable
vRtrMplsFwdPlcyTable = _VRtrMplsFwdPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 66)
)
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyTable.setStatus("current")
_VRtrMplsFwdPlcyEntry_Object = MibTableRow
vRtrMplsFwdPlcyEntry = _VRtrMplsFwdPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 66, 1)
)
vRtrMplsFwdPlcyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyName"),
)
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyEntry.setStatus("current")
_VRtrMplsFwdPlcyName_Type = TLNamedItem
_VRtrMplsFwdPlcyName_Object = MibTableColumn
vRtrMplsFwdPlcyName = _VRtrMplsFwdPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 66, 1, 1),
    _VRtrMplsFwdPlcyName_Type()
)
vRtrMplsFwdPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyName.setStatus("current")
_VRtrMplsFwdPlcyRowStatus_Type = RowStatus
_VRtrMplsFwdPlcyRowStatus_Object = MibTableColumn
vRtrMplsFwdPlcyRowStatus = _VRtrMplsFwdPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 66, 1, 2),
    _VRtrMplsFwdPlcyRowStatus_Type()
)
vRtrMplsFwdPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyRowStatus.setStatus("current")
_VRtrMplsFwdPlcyLastChanged_Type = TimeStamp
_VRtrMplsFwdPlcyLastChanged_Object = MibTableColumn
vRtrMplsFwdPlcyLastChanged = _VRtrMplsFwdPlcyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 66, 1, 3),
    _VRtrMplsFwdPlcyLastChanged_Type()
)
vRtrMplsFwdPlcyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyLastChanged.setStatus("current")


class _VRtrMplsFwdPlcyAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsFwdPlcyAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsFwdPlcyAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsFwdPlcyAdminState_Object = MibTableColumn
vRtrMplsFwdPlcyAdminState = _VRtrMplsFwdPlcyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 66, 1, 4),
    _VRtrMplsFwdPlcyAdminState_Type()
)
vRtrMplsFwdPlcyAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyAdminState.setStatus("current")
_VRtrMplsFwdPlcyOperState_Type = TmnxOperState
_VRtrMplsFwdPlcyOperState_Object = MibTableColumn
vRtrMplsFwdPlcyOperState = _VRtrMplsFwdPlcyOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 66, 1, 5),
    _VRtrMplsFwdPlcyOperState_Type()
)
vRtrMplsFwdPlcyOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyOperState.setStatus("current")


class _VRtrMplsFwdPlcyBindingLabel_Type(TmnxMplsLabelOrZero):
    """Custom type vRtrMplsFwdPlcyBindingLabel based on TmnxMplsLabelOrZero"""
    defaultValue = 0


_VRtrMplsFwdPlcyBindingLabel_Type.__name__ = "TmnxMplsLabelOrZero"
_VRtrMplsFwdPlcyBindingLabel_Object = MibTableColumn
vRtrMplsFwdPlcyBindingLabel = _VRtrMplsFwdPlcyBindingLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 66, 1, 6),
    _VRtrMplsFwdPlcyBindingLabel_Type()
)
vRtrMplsFwdPlcyBindingLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyBindingLabel.setStatus("current")


class _VRtrMplsFwdPlcyEndpointAddrType_Type(InetAddressType):
    """Custom type vRtrMplsFwdPlcyEndpointAddrType based on InetAddressType"""
    defaultValue = 0


_VRtrMplsFwdPlcyEndpointAddrType_Type.__name__ = "InetAddressType"
_VRtrMplsFwdPlcyEndpointAddrType_Object = MibTableColumn
vRtrMplsFwdPlcyEndpointAddrType = _VRtrMplsFwdPlcyEndpointAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 66, 1, 7),
    _VRtrMplsFwdPlcyEndpointAddrType_Type()
)
vRtrMplsFwdPlcyEndpointAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyEndpointAddrType.setStatus("current")


class _VRtrMplsFwdPlcyEndpointAddr_Type(InetAddress):
    """Custom type vRtrMplsFwdPlcyEndpointAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsFwdPlcyEndpointAddr_Type.__name__ = "InetAddress"
_VRtrMplsFwdPlcyEndpointAddr_Object = MibTableColumn
vRtrMplsFwdPlcyEndpointAddr = _VRtrMplsFwdPlcyEndpointAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 66, 1, 8),
    _VRtrMplsFwdPlcyEndpointAddr_Type()
)
vRtrMplsFwdPlcyEndpointAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyEndpointAddr.setStatus("current")


class _VRtrMplsFwdPlcyRevertTimer_Type(Unsigned32):
    """Custom type vRtrMplsFwdPlcyRevertTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_VRtrMplsFwdPlcyRevertTimer_Type.__name__ = "Unsigned32"
_VRtrMplsFwdPlcyRevertTimer_Object = MibTableColumn
vRtrMplsFwdPlcyRevertTimer = _VRtrMplsFwdPlcyRevertTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 66, 1, 9),
    _VRtrMplsFwdPlcyRevertTimer_Type()
)
vRtrMplsFwdPlcyRevertTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyRevertTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyRevertTimer.setUnits("seconds")


class _VRtrMplsFwdPlcyPreference_Type(Unsigned32):
    """Custom type vRtrMplsFwdPlcyPreference based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrMplsFwdPlcyPreference_Type.__name__ = "Unsigned32"
_VRtrMplsFwdPlcyPreference_Object = MibTableColumn
vRtrMplsFwdPlcyPreference = _VRtrMplsFwdPlcyPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 66, 1, 10),
    _VRtrMplsFwdPlcyPreference_Type()
)
vRtrMplsFwdPlcyPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyPreference.setStatus("current")


class _VRtrMplsFwdPlcyMetric_Type(Unsigned32):
    """Custom type vRtrMplsFwdPlcyMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrMplsFwdPlcyMetric_Type.__name__ = "Unsigned32"
_VRtrMplsFwdPlcyMetric_Object = MibTableColumn
vRtrMplsFwdPlcyMetric = _VRtrMplsFwdPlcyMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 66, 1, 11),
    _VRtrMplsFwdPlcyMetric_Type()
)
vRtrMplsFwdPlcyMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyMetric.setStatus("current")


class _VRtrMplsFwdPlcyTtmPreference_Type(Unsigned32):
    """Custom type vRtrMplsFwdPlcyTtmPreference based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrMplsFwdPlcyTtmPreference_Type.__name__ = "Unsigned32"
_VRtrMplsFwdPlcyTtmPreference_Object = MibTableColumn
vRtrMplsFwdPlcyTtmPreference = _VRtrMplsFwdPlcyTtmPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 66, 1, 12),
    _VRtrMplsFwdPlcyTtmPreference_Type()
)
vRtrMplsFwdPlcyTtmPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyTtmPreference.setStatus("current")
_VRtrMplsFwdPlcyNHGrpTblLastChg_Type = TimeStamp
_VRtrMplsFwdPlcyNHGrpTblLastChg_Object = MibScalar
vRtrMplsFwdPlcyNHGrpTblLastChg = _VRtrMplsFwdPlcyNHGrpTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 67),
    _VRtrMplsFwdPlcyNHGrpTblLastChg_Type()
)
vRtrMplsFwdPlcyNHGrpTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNHGrpTblLastChg.setStatus("current")
_VRtrMplsFwdPlcyNHGrpTable_Object = MibTable
vRtrMplsFwdPlcyNHGrpTable = _VRtrMplsFwdPlcyNHGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 68)
)
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNHGrpTable.setStatus("current")
_VRtrMplsFwdPlcyNHGrpEntry_Object = MibTableRow
vRtrMplsFwdPlcyNHGrpEntry = _VRtrMplsFwdPlcyNHGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 68, 1)
)
vRtrMplsFwdPlcyNHGrpEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyName"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNHGrpIdx"),
)
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNHGrpEntry.setStatus("current")


class _VRtrMplsFwdPlcyNHGrpIdx_Type(Unsigned32):
    """Custom type vRtrMplsFwdPlcyNHGrpIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VRtrMplsFwdPlcyNHGrpIdx_Type.__name__ = "Unsigned32"
_VRtrMplsFwdPlcyNHGrpIdx_Object = MibTableColumn
vRtrMplsFwdPlcyNHGrpIdx = _VRtrMplsFwdPlcyNHGrpIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 68, 1, 1),
    _VRtrMplsFwdPlcyNHGrpIdx_Type()
)
vRtrMplsFwdPlcyNHGrpIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNHGrpIdx.setStatus("current")
_VRtrMplsFwdPlcyNHGrpRowStatus_Type = RowStatus
_VRtrMplsFwdPlcyNHGrpRowStatus_Object = MibTableColumn
vRtrMplsFwdPlcyNHGrpRowStatus = _VRtrMplsFwdPlcyNHGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 68, 1, 2),
    _VRtrMplsFwdPlcyNHGrpRowStatus_Type()
)
vRtrMplsFwdPlcyNHGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNHGrpRowStatus.setStatus("current")
_VRtrMplsFwdPlcyNHGrpLastChanged_Type = TimeStamp
_VRtrMplsFwdPlcyNHGrpLastChanged_Object = MibTableColumn
vRtrMplsFwdPlcyNHGrpLastChanged = _VRtrMplsFwdPlcyNHGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 68, 1, 3),
    _VRtrMplsFwdPlcyNHGrpLastChanged_Type()
)
vRtrMplsFwdPlcyNHGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNHGrpLastChanged.setStatus("current")


class _VRtrMplsFwdPlcyNHGrpAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsFwdPlcyNHGrpAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsFwdPlcyNHGrpAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsFwdPlcyNHGrpAdminState_Object = MibTableColumn
vRtrMplsFwdPlcyNHGrpAdminState = _VRtrMplsFwdPlcyNHGrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 68, 1, 4),
    _VRtrMplsFwdPlcyNHGrpAdminState_Type()
)
vRtrMplsFwdPlcyNHGrpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNHGrpAdminState.setStatus("current")
_VRtrMplsFwdPlcyNHGrpOperState_Type = TmnxOperState
_VRtrMplsFwdPlcyNHGrpOperState_Object = MibTableColumn
vRtrMplsFwdPlcyNHGrpOperState = _VRtrMplsFwdPlcyNHGrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 68, 1, 5),
    _VRtrMplsFwdPlcyNHGrpOperState_Type()
)
vRtrMplsFwdPlcyNHGrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNHGrpOperState.setStatus("current")


class _VRtrMplsFwdPlcyNHGrpResType_Type(Integer32):
    """Custom type vRtrMplsFwdPlcyNHGrpResType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("indirect", 2))
    )


_VRtrMplsFwdPlcyNHGrpResType_Type.__name__ = "Integer32"
_VRtrMplsFwdPlcyNHGrpResType_Object = MibTableColumn
vRtrMplsFwdPlcyNHGrpResType = _VRtrMplsFwdPlcyNHGrpResType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 68, 1, 6),
    _VRtrMplsFwdPlcyNHGrpResType_Type()
)
vRtrMplsFwdPlcyNHGrpResType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNHGrpResType.setStatus("current")


class _VRtrMplsFwdPlcyNHGrpLoadBalWt_Type(Unsigned32):
    """Custom type vRtrMplsFwdPlcyNHGrpLoadBalWt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrMplsFwdPlcyNHGrpLoadBalWt_Type.__name__ = "Unsigned32"
_VRtrMplsFwdPlcyNHGrpLoadBalWt_Object = MibTableColumn
vRtrMplsFwdPlcyNHGrpLoadBalWt = _VRtrMplsFwdPlcyNHGrpLoadBalWt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 68, 1, 7),
    _VRtrMplsFwdPlcyNHGrpLoadBalWt_Type()
)
vRtrMplsFwdPlcyNHGrpLoadBalWt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNHGrpLoadBalWt.setStatus("current")
_VRtrMplsFwdPlcyNhgNHTblLastChg_Type = TimeStamp
_VRtrMplsFwdPlcyNhgNHTblLastChg_Object = MibScalar
vRtrMplsFwdPlcyNhgNHTblLastChg = _VRtrMplsFwdPlcyNhgNHTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 69),
    _VRtrMplsFwdPlcyNhgNHTblLastChg_Type()
)
vRtrMplsFwdPlcyNhgNHTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHTblLastChg.setStatus("current")
_VRtrMplsFwdPlcyNhgNHTable_Object = MibTable
vRtrMplsFwdPlcyNhgNHTable = _VRtrMplsFwdPlcyNhgNHTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 70)
)
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHTable.setStatus("current")
_VRtrMplsFwdPlcyNhgNHEntry_Object = MibTableRow
vRtrMplsFwdPlcyNhgNHEntry = _VRtrMplsFwdPlcyNhgNHEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 70, 1)
)
vRtrMplsFwdPlcyNhgNHEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyName"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNHGrpIdx"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNhgNHType"),
)
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHEntry.setStatus("current")


class _VRtrMplsFwdPlcyNhgNHType_Type(Integer32):
    """Custom type vRtrMplsFwdPlcyNhgNHType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2))
    )


_VRtrMplsFwdPlcyNhgNHType_Type.__name__ = "Integer32"
_VRtrMplsFwdPlcyNhgNHType_Object = MibTableColumn
vRtrMplsFwdPlcyNhgNHType = _VRtrMplsFwdPlcyNhgNHType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 70, 1, 1),
    _VRtrMplsFwdPlcyNhgNHType_Type()
)
vRtrMplsFwdPlcyNhgNHType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHType.setStatus("current")
_VRtrMplsFwdPlcyNhgNHRowStatus_Type = RowStatus
_VRtrMplsFwdPlcyNhgNHRowStatus_Object = MibTableColumn
vRtrMplsFwdPlcyNhgNHRowStatus = _VRtrMplsFwdPlcyNhgNHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 70, 1, 2),
    _VRtrMplsFwdPlcyNhgNHRowStatus_Type()
)
vRtrMplsFwdPlcyNhgNHRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHRowStatus.setStatus("current")
_VRtrMplsFwdPlcyNhgNHLastChanged_Type = TimeStamp
_VRtrMplsFwdPlcyNhgNHLastChanged_Object = MibTableColumn
vRtrMplsFwdPlcyNhgNHLastChanged = _VRtrMplsFwdPlcyNhgNHLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 70, 1, 3),
    _VRtrMplsFwdPlcyNhgNHLastChanged_Type()
)
vRtrMplsFwdPlcyNhgNHLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHLastChanged.setStatus("current")
_VRtrMplsFwdPlcyNhgNHOperState_Type = TmnxOperState
_VRtrMplsFwdPlcyNhgNHOperState_Object = MibTableColumn
vRtrMplsFwdPlcyNhgNHOperState = _VRtrMplsFwdPlcyNhgNHOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 70, 1, 4),
    _VRtrMplsFwdPlcyNhgNHOperState_Type()
)
vRtrMplsFwdPlcyNhgNHOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHOperState.setStatus("current")


class _VRtrMplsFwdPlcyNhgNHAddrType_Type(InetAddressType):
    """Custom type vRtrMplsFwdPlcyNhgNHAddrType based on InetAddressType"""
    defaultValue = 0


_VRtrMplsFwdPlcyNhgNHAddrType_Type.__name__ = "InetAddressType"
_VRtrMplsFwdPlcyNhgNHAddrType_Object = MibTableColumn
vRtrMplsFwdPlcyNhgNHAddrType = _VRtrMplsFwdPlcyNhgNHAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 70, 1, 5),
    _VRtrMplsFwdPlcyNhgNHAddrType_Type()
)
vRtrMplsFwdPlcyNhgNHAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHAddrType.setStatus("current")


class _VRtrMplsFwdPlcyNhgNHAddr_Type(InetAddress):
    """Custom type vRtrMplsFwdPlcyNhgNHAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsFwdPlcyNhgNHAddr_Type.__name__ = "InetAddress"
_VRtrMplsFwdPlcyNhgNHAddr_Object = MibTableColumn
vRtrMplsFwdPlcyNhgNHAddr = _VRtrMplsFwdPlcyNhgNHAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 70, 1, 6),
    _VRtrMplsFwdPlcyNhgNHAddr_Type()
)
vRtrMplsFwdPlcyNhgNHAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHAddr.setStatus("current")
_VRtrMplsFwdPlcyGenTblLastChg_Type = TimeStamp
_VRtrMplsFwdPlcyGenTblLastChg_Object = MibScalar
vRtrMplsFwdPlcyGenTblLastChg = _VRtrMplsFwdPlcyGenTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 71),
    _VRtrMplsFwdPlcyGenTblLastChg_Type()
)
vRtrMplsFwdPlcyGenTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyGenTblLastChg.setStatus("current")
_VRtrMplsFwdPlcyGenTable_Object = MibTable
vRtrMplsFwdPlcyGenTable = _VRtrMplsFwdPlcyGenTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 72)
)
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyGenTable.setStatus("current")
_VRtrMplsFwdPlcyGenEntry_Object = MibTableRow
vRtrMplsFwdPlcyGenEntry = _VRtrMplsFwdPlcyGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 72, 1)
)
vRtrMplsFwdPlcyGenEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyGenEntry.setStatus("current")
_VRtrMplsFwdPlcyGenRowStatus_Type = RowStatus
_VRtrMplsFwdPlcyGenRowStatus_Object = MibTableColumn
vRtrMplsFwdPlcyGenRowStatus = _VRtrMplsFwdPlcyGenRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 72, 1, 1),
    _VRtrMplsFwdPlcyGenRowStatus_Type()
)
vRtrMplsFwdPlcyGenRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyGenRowStatus.setStatus("current")
_VRtrMplsFwdPlcyGenLastChanged_Type = TimeStamp
_VRtrMplsFwdPlcyGenLastChanged_Object = MibTableColumn
vRtrMplsFwdPlcyGenLastChanged = _VRtrMplsFwdPlcyGenLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 72, 1, 2),
    _VRtrMplsFwdPlcyGenLastChanged_Type()
)
vRtrMplsFwdPlcyGenLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyGenLastChanged.setStatus("current")


class _VRtrMplsFwdPlcyGenAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsFwdPlcyGenAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsFwdPlcyGenAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsFwdPlcyGenAdminState_Object = MibTableColumn
vRtrMplsFwdPlcyGenAdminState = _VRtrMplsFwdPlcyGenAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 72, 1, 3),
    _VRtrMplsFwdPlcyGenAdminState_Type()
)
vRtrMplsFwdPlcyGenAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyGenAdminState.setStatus("current")
_VRtrMplsFwdPlcyGenOperState_Type = TmnxOperState
_VRtrMplsFwdPlcyGenOperState_Object = MibTableColumn
vRtrMplsFwdPlcyGenOperState = _VRtrMplsFwdPlcyGenOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 72, 1, 4),
    _VRtrMplsFwdPlcyGenOperState_Type()
)
vRtrMplsFwdPlcyGenOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyGenOperState.setStatus("current")


class _VRtrMplsFwdPlcyGenOperDownReason_Type(Integer32):
    """Custom type vRtrMplsFwdPlcyGenOperDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("adminDown", 1),
          ("mplsOperDown", 2))
    )


_VRtrMplsFwdPlcyGenOperDownReason_Type.__name__ = "Integer32"
_VRtrMplsFwdPlcyGenOperDownReason_Object = MibTableColumn
vRtrMplsFwdPlcyGenOperDownReason = _VRtrMplsFwdPlcyGenOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 72, 1, 5),
    _VRtrMplsFwdPlcyGenOperDownReason_Type()
)
vRtrMplsFwdPlcyGenOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyGenOperDownReason.setStatus("current")


class _VRtrMplsFwdPlcyGenReservedLblBlk_Type(TLNamedItemOrEmpty):
    """Custom type vRtrMplsFwdPlcyGenReservedLblBlk based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_VRtrMplsFwdPlcyGenReservedLblBlk_Type.__name__ = "TLNamedItemOrEmpty"
_VRtrMplsFwdPlcyGenReservedLblBlk_Object = MibTableColumn
vRtrMplsFwdPlcyGenReservedLblBlk = _VRtrMplsFwdPlcyGenReservedLblBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 72, 1, 6),
    _VRtrMplsFwdPlcyGenReservedLblBlk_Type()
)
vRtrMplsFwdPlcyGenReservedLblBlk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyGenReservedLblBlk.setStatus("current")
_VRtrMplsFwdPlcyStatsTblLastChg_Type = TimeStamp
_VRtrMplsFwdPlcyStatsTblLastChg_Object = MibScalar
vRtrMplsFwdPlcyStatsTblLastChg = _VRtrMplsFwdPlcyStatsTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 73),
    _VRtrMplsFwdPlcyStatsTblLastChg_Type()
)
vRtrMplsFwdPlcyStatsTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyStatsTblLastChg.setStatus("current")
_VRtrMplsFwdPlcyStatsTable_Object = MibTable
vRtrMplsFwdPlcyStatsTable = _VRtrMplsFwdPlcyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 74)
)
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyStatsTable.setStatus("current")
_VRtrMplsFwdPlcyStatsEntry_Object = MibTableRow
vRtrMplsFwdPlcyStatsEntry = _VRtrMplsFwdPlcyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 74, 1)
)
vRtrMplsFwdPlcyStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyName"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyStatsType"),
)
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyStatsEntry.setStatus("current")


class _VRtrMplsFwdPlcyStatsType_Type(Integer32):
    """Custom type vRtrMplsFwdPlcyStatsType based on Integer32"""
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


_VRtrMplsFwdPlcyStatsType_Type.__name__ = "Integer32"
_VRtrMplsFwdPlcyStatsType_Object = MibTableColumn
vRtrMplsFwdPlcyStatsType = _VRtrMplsFwdPlcyStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 74, 1, 1),
    _VRtrMplsFwdPlcyStatsType_Type()
)
vRtrMplsFwdPlcyStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyStatsType.setStatus("current")
_VRtrMplsFwdPlcyStatsRowStatus_Type = RowStatus
_VRtrMplsFwdPlcyStatsRowStatus_Object = MibTableColumn
vRtrMplsFwdPlcyStatsRowStatus = _VRtrMplsFwdPlcyStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 74, 1, 2),
    _VRtrMplsFwdPlcyStatsRowStatus_Type()
)
vRtrMplsFwdPlcyStatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyStatsRowStatus.setStatus("current")
_VRtrMplsFwdPlcyStatsLastChanged_Type = TimeStamp
_VRtrMplsFwdPlcyStatsLastChanged_Object = MibTableColumn
vRtrMplsFwdPlcyStatsLastChanged = _VRtrMplsFwdPlcyStatsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 74, 1, 3),
    _VRtrMplsFwdPlcyStatsLastChanged_Type()
)
vRtrMplsFwdPlcyStatsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyStatsLastChanged.setStatus("current")


class _VRtrMplsFwdPlcyStatsAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsFwdPlcyStatsAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsFwdPlcyStatsAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsFwdPlcyStatsAdminState_Object = MibTableColumn
vRtrMplsFwdPlcyStatsAdminState = _VRtrMplsFwdPlcyStatsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 74, 1, 4),
    _VRtrMplsFwdPlcyStatsAdminState_Type()
)
vRtrMplsFwdPlcyStatsAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyStatsAdminState.setStatus("current")
_VRtrMplsBindLblPathTable_Object = MibTable
vRtrMplsBindLblPathTable = _VRtrMplsBindLblPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 75)
)
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathTable.setStatus("current")
_VRtrMplsBindLblPathEntry_Object = MibTableRow
vRtrMplsBindLblPathEntry = _VRtrMplsBindLblPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 75, 1)
)
vRtrMplsBindLblPathEntry.setIndexNames(
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathOwner"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLbl"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathId"),
)
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathEntry.setStatus("current")
_VRtrMplsBindLbl_Type = TmnxMplsLabel
_VRtrMplsBindLbl_Object = MibTableColumn
vRtrMplsBindLbl = _VRtrMplsBindLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 75, 1, 1),
    _VRtrMplsBindLbl_Type()
)
vRtrMplsBindLbl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsBindLbl.setStatus("current")
_VRtrMplsBindLblPathId_Type = Unsigned32
_VRtrMplsBindLblPathId_Object = MibTableColumn
vRtrMplsBindLblPathId = _VRtrMplsBindLblPathId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 75, 1, 2),
    _VRtrMplsBindLblPathId_Type()
)
vRtrMplsBindLblPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathId.setStatus("current")


class _VRtrMplsBindLblPathOwner_Type(Integer32):
    """Custom type vRtrMplsBindLblPathOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mplsFwdPlcy", 1)
    )


_VRtrMplsBindLblPathOwner_Type.__name__ = "Integer32"
_VRtrMplsBindLblPathOwner_Object = MibTableColumn
vRtrMplsBindLblPathOwner = _VRtrMplsBindLblPathOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 75, 1, 3),
    _VRtrMplsBindLblPathOwner_Type()
)
vRtrMplsBindLblPathOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathOwner.setStatus("current")
_VRtrMplsBindLblPathName_Type = TLNamedItem
_VRtrMplsBindLblPathName_Object = MibTableColumn
vRtrMplsBindLblPathName = _VRtrMplsBindLblPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 75, 1, 4),
    _VRtrMplsBindLblPathName_Type()
)
vRtrMplsBindLblPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathName.setStatus("current")
_VRtrMplsBindLblPathOperState_Type = TmnxOperState
_VRtrMplsBindLblPathOperState_Object = MibTableColumn
vRtrMplsBindLblPathOperState = _VRtrMplsBindLblPathOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 75, 1, 5),
    _VRtrMplsBindLblPathOperState_Type()
)
vRtrMplsBindLblPathOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathOperState.setStatus("current")
_VRtrMplsBindLblPathLastOperChg_Type = TimeStamp
_VRtrMplsBindLblPathLastOperChg_Object = MibTableColumn
vRtrMplsBindLblPathLastOperChg = _VRtrMplsBindLblPathLastOperChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 75, 1, 6),
    _VRtrMplsBindLblPathLastOperChg_Type()
)
vRtrMplsBindLblPathLastOperChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathLastOperChg.setStatus("current")


class _VRtrMplsBindLblOperDownReason_Type(Integer32):
    """Custom type vRtrMplsBindLblOperDownReason based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("memAllocFailed", 1),
          ("invEndPointAddr", 2),
          ("invBindingLbl", 3),
          ("duplicatePlcy", 4),
          ("invalidNextHop", 5),
          ("iomPgmFailed", 6),
          ("backpressured", 7),
          ("higherPrefPlcyPgmed", 8),
          ("lblNotAvailable", 9),
          ("statsAllocFailed", 10),
          ("maxPlcyExceeded", 11))
    )


_VRtrMplsBindLblOperDownReason_Type.__name__ = "Integer32"
_VRtrMplsBindLblOperDownReason_Object = MibTableColumn
vRtrMplsBindLblOperDownReason = _VRtrMplsBindLblOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 75, 1, 7),
    _VRtrMplsBindLblOperDownReason_Type()
)
vRtrMplsBindLblOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblOperDownReason.setStatus("current")


class _VRtrMplsBindLblPathNumNHGrpCnt_Type(Unsigned32):
    """Custom type vRtrMplsBindLblPathNumNHGrpCnt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VRtrMplsBindLblPathNumNHGrpCnt_Type.__name__ = "Unsigned32"
_VRtrMplsBindLblPathNumNHGrpCnt_Object = MibTableColumn
vRtrMplsBindLblPathNumNHGrpCnt = _VRtrMplsBindLblPathNumNHGrpCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 75, 1, 8),
    _VRtrMplsBindLblPathNumNHGrpCnt_Type()
)
vRtrMplsBindLblPathNumNHGrpCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNumNHGrpCnt.setStatus("current")
_VRtrMplsBindLblPathRetryCount_Type = Counter32
_VRtrMplsBindLblPathRetryCount_Object = MibTableColumn
vRtrMplsBindLblPathRetryCount = _VRtrMplsBindLblPathRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 75, 1, 9),
    _VRtrMplsBindLblPathRetryCount_Type()
)
vRtrMplsBindLblPathRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathRetryCount.setStatus("current")
_VRtrMplsBindLblPathRetryTimeRem_Type = Unsigned32
_VRtrMplsBindLblPathRetryTimeRem_Object = MibTableColumn
vRtrMplsBindLblPathRetryTimeRem = _VRtrMplsBindLblPathRetryTimeRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 75, 1, 10),
    _VRtrMplsBindLblPathRetryTimeRem_Type()
)
vRtrMplsBindLblPathRetryTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathRetryTimeRem.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathRetryTimeRem.setUnits("seconds")


class _VRtrMplsBindLblPathRevertTimer_Type(Unsigned32):
    """Custom type vRtrMplsBindLblPathRevertTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_VRtrMplsBindLblPathRevertTimer_Type.__name__ = "Unsigned32"
_VRtrMplsBindLblPathRevertTimer_Object = MibTableColumn
vRtrMplsBindLblPathRevertTimer = _VRtrMplsBindLblPathRevertTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 75, 1, 11),
    _VRtrMplsBindLblPathRevertTimer_Type()
)
vRtrMplsBindLblPathRevertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathRevertTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathRevertTimer.setUnits("minutes")
_VRtrMplsBindLblPathIngStatsEnabl_Type = TruthValue
_VRtrMplsBindLblPathIngStatsEnabl_Object = MibTableColumn
vRtrMplsBindLblPathIngStatsEnabl = _VRtrMplsBindLblPathIngStatsEnabl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 75, 1, 12),
    _VRtrMplsBindLblPathIngStatsEnabl_Type()
)
vRtrMplsBindLblPathIngStatsEnabl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathIngStatsEnabl.setStatus("current")


class _VRtrMplsBindLblPathPref_Type(Unsigned32):
    """Custom type vRtrMplsBindLblPathPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrMplsBindLblPathPref_Type.__name__ = "Unsigned32"
_VRtrMplsBindLblPathPref_Object = MibTableColumn
vRtrMplsBindLblPathPref = _VRtrMplsBindLblPathPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 75, 1, 13),
    _VRtrMplsBindLblPathPref_Type()
)
vRtrMplsBindLblPathPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathPref.setStatus("current")
_VRtrMplsBLPathIngStatOperState_Type = TmnxOperState
_VRtrMplsBLPathIngStatOperState_Object = MibTableColumn
vRtrMplsBLPathIngStatOperState = _VRtrMplsBLPathIngStatOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 75, 1, 14),
    _VRtrMplsBLPathIngStatOperState_Type()
)
vRtrMplsBLPathIngStatOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBLPathIngStatOperState.setStatus("current")
_VRtrMplsBindLblPathEgrStatsEnabl_Type = TruthValue
_VRtrMplsBindLblPathEgrStatsEnabl_Object = MibTableColumn
vRtrMplsBindLblPathEgrStatsEnabl = _VRtrMplsBindLblPathEgrStatsEnabl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 75, 1, 15),
    _VRtrMplsBindLblPathEgrStatsEnabl_Type()
)
vRtrMplsBindLblPathEgrStatsEnabl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathEgrStatsEnabl.setStatus("current")
_VRtrMplsBLPathEgrStatOperState_Type = TmnxOperState
_VRtrMplsBLPathEgrStatOperState_Object = MibTableColumn
vRtrMplsBLPathEgrStatOperState = _VRtrMplsBLPathEgrStatOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 75, 1, 16),
    _VRtrMplsBLPathEgrStatOperState_Type()
)
vRtrMplsBLPathEgrStatOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBLPathEgrStatOperState.setStatus("current")
_VRtrMplsBindLblPathNhgTable_Object = MibTable
vRtrMplsBindLblPathNhgTable = _VRtrMplsBindLblPathNhgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 76)
)
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgTable.setStatus("current")
_VRtrMplsBindLblPathNhgEntry_Object = MibTableRow
vRtrMplsBindLblPathNhgEntry = _VRtrMplsBindLblPathNhgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 76, 1)
)
vRtrMplsBindLblPathNhgEntry.setIndexNames(
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathOwner"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLbl"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathId"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNhgIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgEntry.setStatus("current")


class _VRtrMplsBindLblPathNhgIndex_Type(Unsigned32):
    """Custom type vRtrMplsBindLblPathNhgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VRtrMplsBindLblPathNhgIndex_Type.__name__ = "Unsigned32"
_VRtrMplsBindLblPathNhgIndex_Object = MibTableColumn
vRtrMplsBindLblPathNhgIndex = _VRtrMplsBindLblPathNhgIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 76, 1, 1),
    _VRtrMplsBindLblPathNhgIndex_Type()
)
vRtrMplsBindLblPathNhgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgIndex.setStatus("current")
_VRtrMplsBindLblPathNhgOperState_Type = TmnxOperState
_VRtrMplsBindLblPathNhgOperState_Object = MibTableColumn
vRtrMplsBindLblPathNhgOperState = _VRtrMplsBindLblPathNhgOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 76, 1, 2),
    _VRtrMplsBindLblPathNhgOperState_Type()
)
vRtrMplsBindLblPathNhgOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgOperState.setStatus("current")


class _VRtrMplsBindLblPathNHgResType_Type(Integer32):
    """Custom type vRtrMplsBindLblPathNHgResType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("indirect", 2))
    )


_VRtrMplsBindLblPathNHgResType_Type.__name__ = "Integer32"
_VRtrMplsBindLblPathNHgResType_Object = MibTableColumn
vRtrMplsBindLblPathNHgResType = _VRtrMplsBindLblPathNHgResType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 76, 1, 3),
    _VRtrMplsBindLblPathNHgResType_Type()
)
vRtrMplsBindLblPathNHgResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNHgResType.setStatus("current")
_VRtrMplsBindLblPathNhgLoadBalWt_Type = Unsigned32
_VRtrMplsBindLblPathNhgLoadBalWt_Object = MibTableColumn
vRtrMplsBindLblPathNhgLoadBalWt = _VRtrMplsBindLblPathNhgLoadBalWt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 76, 1, 4),
    _VRtrMplsBindLblPathNhgLoadBalWt_Type()
)
vRtrMplsBindLblPathNhgLoadBalWt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgLoadBalWt.setStatus("current")
_VRtrMplsBindLblPathNhgFailovrCnt_Type = Counter32
_VRtrMplsBindLblPathNhgFailovrCnt_Object = MibTableColumn
vRtrMplsBindLblPathNhgFailovrCnt = _VRtrMplsBindLblPathNhgFailovrCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 76, 1, 5),
    _VRtrMplsBindLblPathNhgFailovrCnt_Type()
)
vRtrMplsBindLblPathNhgFailovrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgFailovrCnt.setStatus("current")
_VRtrMplsBindLblPathNhgRevertCnt_Type = Counter32
_VRtrMplsBindLblPathNhgRevertCnt_Object = MibTableColumn
vRtrMplsBindLblPathNhgRevertCnt = _VRtrMplsBindLblPathNhgRevertCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 76, 1, 6),
    _VRtrMplsBindLblPathNhgRevertCnt_Type()
)
vRtrMplsBindLblPathNhgRevertCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgRevertCnt.setStatus("current")
_VRtrMplsBindLblPathNhgRevTimeRem_Type = Counter32
_VRtrMplsBindLblPathNhgRevTimeRem_Object = MibTableColumn
vRtrMplsBindLblPathNhgRevTimeRem = _VRtrMplsBindLblPathNhgRevTimeRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 76, 1, 7),
    _VRtrMplsBindLblPathNhgRevTimeRem_Type()
)
vRtrMplsBindLblPathNhgRevTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgRevTimeRem.setStatus("current")


class _VRtrMplsBindLblPathNhgDownReason_Type(Integer32):
    """Custom type vRtrMplsBindLblPathNhgDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("nextHopNotResolved", 1),
          ("nextHopIsLocal", 3),
          ("nextHopIsMcast", 4),
          ("resTypeMismatch", 5))
    )


_VRtrMplsBindLblPathNhgDownReason_Type.__name__ = "Integer32"
_VRtrMplsBindLblPathNhgDownReason_Object = MibTableColumn
vRtrMplsBindLblPathNhgDownReason = _VRtrMplsBindLblPathNhgDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 76, 1, 8),
    _VRtrMplsBindLblPathNhgDownReason_Type()
)
vRtrMplsBindLblPathNhgDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgDownReason.setStatus("current")
_VRtrMplsBindLblPathNhgWeights_Type = Unsigned32
_VRtrMplsBindLblPathNhgWeights_Object = MibTableColumn
vRtrMplsBindLblPathNhgWeights = _VRtrMplsBindLblPathNhgWeights_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 76, 1, 9),
    _VRtrMplsBindLblPathNhgWeights_Type()
)
vRtrMplsBindLblPathNhgWeights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgWeights.setStatus("current")
_VRtrMplsBindLblPathNhgNHTable_Object = MibTable
vRtrMplsBindLblPathNhgNHTable = _VRtrMplsBindLblPathNhgNHTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 77)
)
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgNHTable.setStatus("current")
_VRtrMplsBindLblPathNhgNHEntry_Object = MibTableRow
vRtrMplsBindLblPathNhgNHEntry = _VRtrMplsBindLblPathNhgNHEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 77, 1)
)
vRtrMplsBindLblPathNhgNHEntry.setIndexNames(
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathOwner"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLbl"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathId"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNhgIndex"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNhgNHType"),
)
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgNHEntry.setStatus("current")


class _VRtrMplsBindLblPathNhgNHType_Type(Integer32):
    """Custom type vRtrMplsBindLblPathNhgNHType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2))
    )


_VRtrMplsBindLblPathNhgNHType_Type.__name__ = "Integer32"
_VRtrMplsBindLblPathNhgNHType_Object = MibTableColumn
vRtrMplsBindLblPathNhgNHType = _VRtrMplsBindLblPathNhgNHType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 77, 1, 1),
    _VRtrMplsBindLblPathNhgNHType_Type()
)
vRtrMplsBindLblPathNhgNHType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgNHType.setStatus("current")
_VRtrMplsBindLblPathNhgNHAddrType_Type = InetAddressType
_VRtrMplsBindLblPathNhgNHAddrType_Object = MibTableColumn
vRtrMplsBindLblPathNhgNHAddrType = _VRtrMplsBindLblPathNhgNHAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 77, 1, 2),
    _VRtrMplsBindLblPathNhgNHAddrType_Type()
)
vRtrMplsBindLblPathNhgNHAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgNHAddrType.setStatus("current")


class _VRtrMplsBindLblPathNhgNHAddr_Type(InetAddress):
    """Custom type vRtrMplsBindLblPathNhgNHAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsBindLblPathNhgNHAddr_Type.__name__ = "InetAddress"
_VRtrMplsBindLblPathNhgNHAddr_Object = MibTableColumn
vRtrMplsBindLblPathNhgNHAddr = _VRtrMplsBindLblPathNhgNHAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 77, 1, 3),
    _VRtrMplsBindLblPathNhgNHAddr_Type()
)
vRtrMplsBindLblPathNhgNHAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgNHAddr.setStatus("current")
_VRtrMplsBindLblPathNhgNHResolved_Type = TruthValue
_VRtrMplsBindLblPathNhgNHResolved_Object = MibTableColumn
vRtrMplsBindLblPathNhgNHResolved = _VRtrMplsBindLblPathNhgNHResolved_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 77, 1, 4),
    _VRtrMplsBindLblPathNhgNHResolved_Type()
)
vRtrMplsBindLblPathNhgNHResolved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgNHResolved.setStatus("current")
_VRtrMplsBindLblPathNhgNHOutIf_Type = InterfaceIndexOrZero
_VRtrMplsBindLblPathNhgNHOutIf_Object = MibTableColumn
vRtrMplsBindLblPathNhgNHOutIf = _VRtrMplsBindLblPathNhgNHOutIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 77, 1, 5),
    _VRtrMplsBindLblPathNhgNHOutIf_Type()
)
vRtrMplsBindLblPathNhgNHOutIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgNHOutIf.setStatus("current")


class _VRtrMplsBindLblPathNhgNHDownCode_Type(Integer32):
    """Custom type vRtrMplsBindLblPathNhgNHDownCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("nextHopNotResolved", 1),
          ("nextHopIsLocal", 3),
          ("nextHopIsMcast", 4),
          ("resTypeMismatch", 5))
    )


_VRtrMplsBindLblPathNhgNHDownCode_Type.__name__ = "Integer32"
_VRtrMplsBindLblPathNhgNHDownCode_Object = MibTableColumn
vRtrMplsBindLblPathNhgNHDownCode = _VRtrMplsBindLblPathNhgNHDownCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 77, 1, 6),
    _VRtrMplsBindLblPathNhgNHDownCode_Type()
)
vRtrMplsBindLblPathNhgNHDownCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgNHDownCode.setStatus("current")
_VRtrMplsBindLblPathNhgNHEgrOper_Type = TmnxOperState
_VRtrMplsBindLblPathNhgNHEgrOper_Object = MibTableColumn
vRtrMplsBindLblPathNhgNHEgrOper = _VRtrMplsBindLblPathNhgNHEgrOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 77, 1, 7),
    _VRtrMplsBindLblPathNhgNHEgrOper_Type()
)
vRtrMplsBindLblPathNhgNHEgrOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgNHEgrOper.setStatus("current")
_VRtrMplsBindLblIngrStatsTable_Object = MibTable
vRtrMplsBindLblIngrStatsTable = _VRtrMplsBindLblIngrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 78)
)
if mibBuilder.loadTexts:
    vRtrMplsBindLblIngrStatsTable.setStatus("current")
_VRtrMplsBindLblIngrStatsEntry_Object = MibTableRow
vRtrMplsBindLblIngrStatsEntry = _VRtrMplsBindLblIngrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 78, 1)
)
vRtrMplsBindLblIngrStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathOwner"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLbl"),
)
if mibBuilder.loadTexts:
    vRtrMplsBindLblIngrStatsEntry.setStatus("current")
_VRtrMplsBindLblIngrAggPkts_Type = Counter64
_VRtrMplsBindLblIngrAggPkts_Object = MibTableColumn
vRtrMplsBindLblIngrAggPkts = _VRtrMplsBindLblIngrAggPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 78, 1, 1),
    _VRtrMplsBindLblIngrAggPkts_Type()
)
vRtrMplsBindLblIngrAggPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblIngrAggPkts.setStatus("current")
_VRtrMplsBindLblIngrAggOctets_Type = Counter64
_VRtrMplsBindLblIngrAggOctets_Object = MibTableColumn
vRtrMplsBindLblIngrAggOctets = _VRtrMplsBindLblIngrAggOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 78, 1, 2),
    _VRtrMplsBindLblIngrAggOctets_Type()
)
vRtrMplsBindLblIngrAggOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblIngrAggOctets.setStatus("current")
_VRtrMplsEndptPathTable_Object = MibTable
vRtrMplsEndptPathTable = _VRtrMplsEndptPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79)
)
if mibBuilder.loadTexts:
    vRtrMplsEndptPathTable.setStatus("current")
_VRtrMplsEndptPathEntry_Object = MibTableRow
vRtrMplsEndptPathEntry = _VRtrMplsEndptPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79, 1)
)
vRtrMplsEndptPathEntry.setIndexNames(
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptPathOwner"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptAddrType"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptAddress"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptPathId"),
)
if mibBuilder.loadTexts:
    vRtrMplsEndptPathEntry.setStatus("current")
_VRtrMplsEndptAddrType_Type = InetAddressType
_VRtrMplsEndptAddrType_Object = MibTableColumn
vRtrMplsEndptAddrType = _VRtrMplsEndptAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79, 1, 1),
    _VRtrMplsEndptAddrType_Type()
)
vRtrMplsEndptAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsEndptAddrType.setStatus("current")


class _VRtrMplsEndptAddress_Type(InetAddress):
    """Custom type vRtrMplsEndptAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsEndptAddress_Type.__name__ = "InetAddress"
_VRtrMplsEndptAddress_Object = MibTableColumn
vRtrMplsEndptAddress = _VRtrMplsEndptAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79, 1, 2),
    _VRtrMplsEndptAddress_Type()
)
vRtrMplsEndptAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsEndptAddress.setStatus("current")
_VRtrMplsEndptPathId_Type = Unsigned32
_VRtrMplsEndptPathId_Object = MibTableColumn
vRtrMplsEndptPathId = _VRtrMplsEndptPathId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79, 1, 3),
    _VRtrMplsEndptPathId_Type()
)
vRtrMplsEndptPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathId.setStatus("current")


class _VRtrMplsEndptPathOwner_Type(Integer32):
    """Custom type vRtrMplsEndptPathOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mplsFwdPlcy", 1)
    )


_VRtrMplsEndptPathOwner_Type.__name__ = "Integer32"
_VRtrMplsEndptPathOwner_Object = MibTableColumn
vRtrMplsEndptPathOwner = _VRtrMplsEndptPathOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79, 1, 4),
    _VRtrMplsEndptPathOwner_Type()
)
vRtrMplsEndptPathOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathOwner.setStatus("current")
_VRtrMplsEndptPathName_Type = TLNamedItem
_VRtrMplsEndptPathName_Object = MibTableColumn
vRtrMplsEndptPathName = _VRtrMplsEndptPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79, 1, 5),
    _VRtrMplsEndptPathName_Type()
)
vRtrMplsEndptPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathName.setStatus("current")
_VRtrMplsEndptPathOperState_Type = TmnxOperState
_VRtrMplsEndptPathOperState_Object = MibTableColumn
vRtrMplsEndptPathOperState = _VRtrMplsEndptPathOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79, 1, 6),
    _VRtrMplsEndptPathOperState_Type()
)
vRtrMplsEndptPathOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathOperState.setStatus("current")
_VRtrMplsEndptPathLastOperChg_Type = TimeStamp
_VRtrMplsEndptPathLastOperChg_Object = MibTableColumn
vRtrMplsEndptPathLastOperChg = _VRtrMplsEndptPathLastOperChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79, 1, 7),
    _VRtrMplsEndptPathLastOperChg_Type()
)
vRtrMplsEndptPathLastOperChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathLastOperChg.setStatus("current")


class _VRtrMplsEndptPathOperDownReason_Type(Integer32):
    """Custom type vRtrMplsEndptPathOperDownReason based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("memAllocFailed", 1),
          ("invEndPointAddr", 2),
          ("duplicatePlcy", 3),
          ("invalidNextHop", 4),
          ("iomPgmFailed", 5),
          ("backpressured", 6),
          ("higherPrefPlcyPgmed", 7),
          ("statsAllocFailed", 8),
          ("maxPlcyExceeded", 9),
          ("noNextHops", 10))
    )


_VRtrMplsEndptPathOperDownReason_Type.__name__ = "Integer32"
_VRtrMplsEndptPathOperDownReason_Object = MibTableColumn
vRtrMplsEndptPathOperDownReason = _VRtrMplsEndptPathOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79, 1, 8),
    _VRtrMplsEndptPathOperDownReason_Type()
)
vRtrMplsEndptPathOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathOperDownReason.setStatus("current")


class _VRtrMplsEndptPathNHGrpCnt_Type(Unsigned32):
    """Custom type vRtrMplsEndptPathNHGrpCnt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VRtrMplsEndptPathNHGrpCnt_Type.__name__ = "Unsigned32"
_VRtrMplsEndptPathNHGrpCnt_Object = MibTableColumn
vRtrMplsEndptPathNHGrpCnt = _VRtrMplsEndptPathNHGrpCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79, 1, 9),
    _VRtrMplsEndptPathNHGrpCnt_Type()
)
vRtrMplsEndptPathNHGrpCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNHGrpCnt.setStatus("current")
_VRtrMplsEndptPathRetryCount_Type = Counter32
_VRtrMplsEndptPathRetryCount_Object = MibTableColumn
vRtrMplsEndptPathRetryCount = _VRtrMplsEndptPathRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79, 1, 10),
    _VRtrMplsEndptPathRetryCount_Type()
)
vRtrMplsEndptPathRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathRetryCount.setStatus("current")
_VRtrMplsEndptPathRetryTimeRem_Type = Unsigned32
_VRtrMplsEndptPathRetryTimeRem_Object = MibTableColumn
vRtrMplsEndptPathRetryTimeRem = _VRtrMplsEndptPathRetryTimeRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79, 1, 11),
    _VRtrMplsEndptPathRetryTimeRem_Type()
)
vRtrMplsEndptPathRetryTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathRetryTimeRem.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathRetryTimeRem.setUnits("seconds")


class _VRtrMplsEndptPathRevertTimer_Type(Unsigned32):
    """Custom type vRtrMplsEndptPathRevertTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_VRtrMplsEndptPathRevertTimer_Type.__name__ = "Unsigned32"
_VRtrMplsEndptPathRevertTimer_Object = MibTableColumn
vRtrMplsEndptPathRevertTimer = _VRtrMplsEndptPathRevertTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79, 1, 12),
    _VRtrMplsEndptPathRevertTimer_Type()
)
vRtrMplsEndptPathRevertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathRevertTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathRevertTimer.setUnits("minutes")


class _VRtrMplsEndptPathPref_Type(Unsigned32):
    """Custom type vRtrMplsEndptPathPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrMplsEndptPathPref_Type.__name__ = "Unsigned32"
_VRtrMplsEndptPathPref_Object = MibTableColumn
vRtrMplsEndptPathPref = _VRtrMplsEndptPathPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79, 1, 13),
    _VRtrMplsEndptPathPref_Type()
)
vRtrMplsEndptPathPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathPref.setStatus("current")


class _VRtrMplsEndptPathTTMPref_Type(Unsigned32):
    """Custom type vRtrMplsEndptPathTTMPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrMplsEndptPathTTMPref_Type.__name__ = "Unsigned32"
_VRtrMplsEndptPathTTMPref_Object = MibTableColumn
vRtrMplsEndptPathTTMPref = _VRtrMplsEndptPathTTMPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79, 1, 14),
    _VRtrMplsEndptPathTTMPref_Type()
)
vRtrMplsEndptPathTTMPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathTTMPref.setStatus("current")


class _VRtrMplsEndptPathMetric_Type(Unsigned32):
    """Custom type vRtrMplsEndptPathMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrMplsEndptPathMetric_Type.__name__ = "Unsigned32"
_VRtrMplsEndptPathMetric_Object = MibTableColumn
vRtrMplsEndptPathMetric = _VRtrMplsEndptPathMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79, 1, 15),
    _VRtrMplsEndptPathMetric_Type()
)
vRtrMplsEndptPathMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathMetric.setStatus("current")
_VRtrMplsEndptPathEgrStatsEnabl_Type = TruthValue
_VRtrMplsEndptPathEgrStatsEnabl_Object = MibTableColumn
vRtrMplsEndptPathEgrStatsEnabl = _VRtrMplsEndptPathEgrStatsEnabl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79, 1, 16),
    _VRtrMplsEndptPathEgrStatsEnabl_Type()
)
vRtrMplsEndptPathEgrStatsEnabl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathEgrStatsEnabl.setStatus("current")
_VRtrMplsEndptPathEgrStatsOper_Type = TmnxOperState
_VRtrMplsEndptPathEgrStatsOper_Object = MibTableColumn
vRtrMplsEndptPathEgrStatsOper = _VRtrMplsEndptPathEgrStatsOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 79, 1, 17),
    _VRtrMplsEndptPathEgrStatsOper_Type()
)
vRtrMplsEndptPathEgrStatsOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathEgrStatsOper.setStatus("current")
_VRtrMplsEndptPathNhgTable_Object = MibTable
vRtrMplsEndptPathNhgTable = _VRtrMplsEndptPathNhgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 80)
)
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgTable.setStatus("current")
_VRtrMplsEndptPathNhgEntry_Object = MibTableRow
vRtrMplsEndptPathNhgEntry = _VRtrMplsEndptPathNhgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 80, 1)
)
vRtrMplsEndptPathNhgEntry.setIndexNames(
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptPathOwner"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptAddrType"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptAddress"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptPathId"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgEntry.setStatus("current")


class _VRtrMplsEndptPathNhgIndex_Type(Unsigned32):
    """Custom type vRtrMplsEndptPathNhgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VRtrMplsEndptPathNhgIndex_Type.__name__ = "Unsigned32"
_VRtrMplsEndptPathNhgIndex_Object = MibTableColumn
vRtrMplsEndptPathNhgIndex = _VRtrMplsEndptPathNhgIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 80, 1, 1),
    _VRtrMplsEndptPathNhgIndex_Type()
)
vRtrMplsEndptPathNhgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgIndex.setStatus("current")
_VRtrMplsEndptPathNhgOperState_Type = TmnxOperState
_VRtrMplsEndptPathNhgOperState_Object = MibTableColumn
vRtrMplsEndptPathNhgOperState = _VRtrMplsEndptPathNhgOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 80, 1, 2),
    _VRtrMplsEndptPathNhgOperState_Type()
)
vRtrMplsEndptPathNhgOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgOperState.setStatus("current")


class _VRtrMplsEndptPathNhgResType_Type(Integer32):
    """Custom type vRtrMplsEndptPathNhgResType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("indirect", 2))
    )


_VRtrMplsEndptPathNhgResType_Type.__name__ = "Integer32"
_VRtrMplsEndptPathNhgResType_Object = MibTableColumn
vRtrMplsEndptPathNhgResType = _VRtrMplsEndptPathNhgResType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 80, 1, 3),
    _VRtrMplsEndptPathNhgResType_Type()
)
vRtrMplsEndptPathNhgResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgResType.setStatus("current")
_VRtrMplsEndptPathNhgLoadBalWt_Type = Unsigned32
_VRtrMplsEndptPathNhgLoadBalWt_Object = MibTableColumn
vRtrMplsEndptPathNhgLoadBalWt = _VRtrMplsEndptPathNhgLoadBalWt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 80, 1, 4),
    _VRtrMplsEndptPathNhgLoadBalWt_Type()
)
vRtrMplsEndptPathNhgLoadBalWt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgLoadBalWt.setStatus("current")
_VRtrMplsEndptPathNhgFailovrCnt_Type = Counter32
_VRtrMplsEndptPathNhgFailovrCnt_Object = MibTableColumn
vRtrMplsEndptPathNhgFailovrCnt = _VRtrMplsEndptPathNhgFailovrCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 80, 1, 5),
    _VRtrMplsEndptPathNhgFailovrCnt_Type()
)
vRtrMplsEndptPathNhgFailovrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgFailovrCnt.setStatus("current")
_VRtrMplsEndptPathNhgRevertCnt_Type = Counter32
_VRtrMplsEndptPathNhgRevertCnt_Object = MibTableColumn
vRtrMplsEndptPathNhgRevertCnt = _VRtrMplsEndptPathNhgRevertCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 80, 1, 6),
    _VRtrMplsEndptPathNhgRevertCnt_Type()
)
vRtrMplsEndptPathNhgRevertCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgRevertCnt.setStatus("current")
_VRtrMplsEndptPathNhgRevTimeRem_Type = Counter32
_VRtrMplsEndptPathNhgRevTimeRem_Object = MibTableColumn
vRtrMplsEndptPathNhgRevTimeRem = _VRtrMplsEndptPathNhgRevTimeRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 80, 1, 7),
    _VRtrMplsEndptPathNhgRevTimeRem_Type()
)
vRtrMplsEndptPathNhgRevTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgRevTimeRem.setStatus("current")
_VRtrMplsEndptPathNhgDownReason_Type = TmnxNhgDownReason
_VRtrMplsEndptPathNhgDownReason_Object = MibTableColumn
vRtrMplsEndptPathNhgDownReason = _VRtrMplsEndptPathNhgDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 80, 1, 8),
    _VRtrMplsEndptPathNhgDownReason_Type()
)
vRtrMplsEndptPathNhgDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgDownReason.setStatus("current")
_VRtrMplsEndptPathNhgWeights_Type = Unsigned32
_VRtrMplsEndptPathNhgWeights_Object = MibTableColumn
vRtrMplsEndptPathNhgWeights = _VRtrMplsEndptPathNhgWeights_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 80, 1, 9),
    _VRtrMplsEndptPathNhgWeights_Type()
)
vRtrMplsEndptPathNhgWeights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgWeights.setStatus("current")
_VRtrMplsEndptPathNhgNHTable_Object = MibTable
vRtrMplsEndptPathNhgNHTable = _VRtrMplsEndptPathNhgNHTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 81)
)
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgNHTable.setStatus("current")
_VRtrMplsEndptPathNhgNHEntry_Object = MibTableRow
vRtrMplsEndptPathNhgNHEntry = _VRtrMplsEndptPathNhgNHEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 81, 1)
)
vRtrMplsEndptPathNhgNHEntry.setIndexNames(
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptPathOwner"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptAddrType"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptAddress"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptPathId"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgIndex"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgNHType"),
)
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgNHEntry.setStatus("current")


class _VRtrMplsEndptPathNhgNHType_Type(Integer32):
    """Custom type vRtrMplsEndptPathNhgNHType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2))
    )


_VRtrMplsEndptPathNhgNHType_Type.__name__ = "Integer32"
_VRtrMplsEndptPathNhgNHType_Object = MibTableColumn
vRtrMplsEndptPathNhgNHType = _VRtrMplsEndptPathNhgNHType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 81, 1, 1),
    _VRtrMplsEndptPathNhgNHType_Type()
)
vRtrMplsEndptPathNhgNHType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgNHType.setStatus("current")
_VRtrMplsEndptPathNhgNHAddrType_Type = InetAddressType
_VRtrMplsEndptPathNhgNHAddrType_Object = MibTableColumn
vRtrMplsEndptPathNhgNHAddrType = _VRtrMplsEndptPathNhgNHAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 81, 1, 2),
    _VRtrMplsEndptPathNhgNHAddrType_Type()
)
vRtrMplsEndptPathNhgNHAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgNHAddrType.setStatus("current")


class _VRtrMplsEndptPathNhgNHAddr_Type(InetAddress):
    """Custom type vRtrMplsEndptPathNhgNHAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsEndptPathNhgNHAddr_Type.__name__ = "InetAddress"
_VRtrMplsEndptPathNhgNHAddr_Object = MibTableColumn
vRtrMplsEndptPathNhgNHAddr = _VRtrMplsEndptPathNhgNHAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 81, 1, 3),
    _VRtrMplsEndptPathNhgNHAddr_Type()
)
vRtrMplsEndptPathNhgNHAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgNHAddr.setStatus("current")
_VRtrMplsEndptPathNhgNHResolved_Type = TruthValue
_VRtrMplsEndptPathNhgNHResolved_Object = MibTableColumn
vRtrMplsEndptPathNhgNHResolved = _VRtrMplsEndptPathNhgNHResolved_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 81, 1, 4),
    _VRtrMplsEndptPathNhgNHResolved_Type()
)
vRtrMplsEndptPathNhgNHResolved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgNHResolved.setStatus("current")
_VRtrMplsEndptPathNhgNHOutIf_Type = InterfaceIndexOrZero
_VRtrMplsEndptPathNhgNHOutIf_Object = MibTableColumn
vRtrMplsEndptPathNhgNHOutIf = _VRtrMplsEndptPathNhgNHOutIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 81, 1, 5),
    _VRtrMplsEndptPathNhgNHOutIf_Type()
)
vRtrMplsEndptPathNhgNHOutIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgNHOutIf.setStatus("current")
_VRtrMplsEndptPathNhgNHDownCode_Type = TmnxNhgDownReason
_VRtrMplsEndptPathNhgNHDownCode_Object = MibTableColumn
vRtrMplsEndptPathNhgNHDownCode = _VRtrMplsEndptPathNhgNHDownCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 81, 1, 6),
    _VRtrMplsEndptPathNhgNHDownCode_Type()
)
vRtrMplsEndptPathNhgNHDownCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgNHDownCode.setStatus("current")
_VRtrMplsEndptPathNhgNHEgrOper_Type = TmnxOperState
_VRtrMplsEndptPathNhgNHEgrOper_Object = MibTableColumn
vRtrMplsEndptPathNhgNHEgrOper = _VRtrMplsEndptPathNhgNHEgrOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 81, 1, 7),
    _VRtrMplsEndptPathNhgNHEgrOper_Type()
)
vRtrMplsEndptPathNhgNHEgrOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgNHEgrOper.setStatus("current")
_VRtrMplsFwdPlcyNhgNHPushLblTable_Object = MibTable
vRtrMplsFwdPlcyNhgNHPushLblTable = _VRtrMplsFwdPlcyNhgNHPushLblTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 82)
)
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHPushLblTable.setStatus("current")
_VRtrMplsFwdPlcyNhgNHPushLblEntry_Object = MibTableRow
vRtrMplsFwdPlcyNhgNHPushLblEntry = _VRtrMplsFwdPlcyNhgNHPushLblEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 82, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHPushLblEntry.setStatus("current")


class _VRtrMplsFwdPlcyNhgNHPushLabel1_Type(Unsigned32):
    """Custom type vRtrMplsFwdPlcyNhgNHPushLabel1 based on Unsigned32"""
    defaultValue = 0


_VRtrMplsFwdPlcyNhgNHPushLabel1_Type.__name__ = "Unsigned32"
_VRtrMplsFwdPlcyNhgNHPushLabel1_Object = MibTableColumn
vRtrMplsFwdPlcyNhgNHPushLabel1 = _VRtrMplsFwdPlcyNhgNHPushLabel1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 82, 1, 1),
    _VRtrMplsFwdPlcyNhgNHPushLabel1_Type()
)
vRtrMplsFwdPlcyNhgNHPushLabel1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHPushLabel1.setStatus("current")


class _VRtrMplsFwdPlcyNhgNHPushLabel2_Type(Unsigned32):
    """Custom type vRtrMplsFwdPlcyNhgNHPushLabel2 based on Unsigned32"""
    defaultValue = 0


_VRtrMplsFwdPlcyNhgNHPushLabel2_Type.__name__ = "Unsigned32"
_VRtrMplsFwdPlcyNhgNHPushLabel2_Object = MibTableColumn
vRtrMplsFwdPlcyNhgNHPushLabel2 = _VRtrMplsFwdPlcyNhgNHPushLabel2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 82, 1, 2),
    _VRtrMplsFwdPlcyNhgNHPushLabel2_Type()
)
vRtrMplsFwdPlcyNhgNHPushLabel2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHPushLabel2.setStatus("current")


class _VRtrMplsFwdPlcyNhgNHPushLabel3_Type(Unsigned32):
    """Custom type vRtrMplsFwdPlcyNhgNHPushLabel3 based on Unsigned32"""
    defaultValue = 0


_VRtrMplsFwdPlcyNhgNHPushLabel3_Type.__name__ = "Unsigned32"
_VRtrMplsFwdPlcyNhgNHPushLabel3_Object = MibTableColumn
vRtrMplsFwdPlcyNhgNHPushLabel3 = _VRtrMplsFwdPlcyNhgNHPushLabel3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 82, 1, 3),
    _VRtrMplsFwdPlcyNhgNHPushLabel3_Type()
)
vRtrMplsFwdPlcyNhgNHPushLabel3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHPushLabel3.setStatus("current")


class _VRtrMplsFwdPlcyNhgNHPushLabel4_Type(Unsigned32):
    """Custom type vRtrMplsFwdPlcyNhgNHPushLabel4 based on Unsigned32"""
    defaultValue = 0


_VRtrMplsFwdPlcyNhgNHPushLabel4_Type.__name__ = "Unsigned32"
_VRtrMplsFwdPlcyNhgNHPushLabel4_Object = MibTableColumn
vRtrMplsFwdPlcyNhgNHPushLabel4 = _VRtrMplsFwdPlcyNhgNHPushLabel4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 82, 1, 4),
    _VRtrMplsFwdPlcyNhgNHPushLabel4_Type()
)
vRtrMplsFwdPlcyNhgNHPushLabel4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHPushLabel4.setStatus("current")


class _VRtrMplsFwdPlcyNhgNHPushLabel5_Type(Unsigned32):
    """Custom type vRtrMplsFwdPlcyNhgNHPushLabel5 based on Unsigned32"""
    defaultValue = 0


_VRtrMplsFwdPlcyNhgNHPushLabel5_Type.__name__ = "Unsigned32"
_VRtrMplsFwdPlcyNhgNHPushLabel5_Object = MibTableColumn
vRtrMplsFwdPlcyNhgNHPushLabel5 = _VRtrMplsFwdPlcyNhgNHPushLabel5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 82, 1, 5),
    _VRtrMplsFwdPlcyNhgNHPushLabel5_Type()
)
vRtrMplsFwdPlcyNhgNHPushLabel5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHPushLabel5.setStatus("current")


class _VRtrMplsFwdPlcyNhgNHPushLabel6_Type(Unsigned32):
    """Custom type vRtrMplsFwdPlcyNhgNHPushLabel6 based on Unsigned32"""
    defaultValue = 0


_VRtrMplsFwdPlcyNhgNHPushLabel6_Type.__name__ = "Unsigned32"
_VRtrMplsFwdPlcyNhgNHPushLabel6_Object = MibTableColumn
vRtrMplsFwdPlcyNhgNHPushLabel6 = _VRtrMplsFwdPlcyNhgNHPushLabel6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 82, 1, 6),
    _VRtrMplsFwdPlcyNhgNHPushLabel6_Type()
)
vRtrMplsFwdPlcyNhgNHPushLabel6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHPushLabel6.setStatus("current")


class _VRtrMplsFwdPlcyNhgNHPushLabel7_Type(Unsigned32):
    """Custom type vRtrMplsFwdPlcyNhgNHPushLabel7 based on Unsigned32"""
    defaultValue = 0


_VRtrMplsFwdPlcyNhgNHPushLabel7_Type.__name__ = "Unsigned32"
_VRtrMplsFwdPlcyNhgNHPushLabel7_Object = MibTableColumn
vRtrMplsFwdPlcyNhgNHPushLabel7 = _VRtrMplsFwdPlcyNhgNHPushLabel7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 82, 1, 7),
    _VRtrMplsFwdPlcyNhgNHPushLabel7_Type()
)
vRtrMplsFwdPlcyNhgNHPushLabel7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHPushLabel7.setStatus("current")


class _VRtrMplsFwdPlcyNhgNHPushLabel8_Type(Unsigned32):
    """Custom type vRtrMplsFwdPlcyNhgNHPushLabel8 based on Unsigned32"""
    defaultValue = 0


_VRtrMplsFwdPlcyNhgNHPushLabel8_Type.__name__ = "Unsigned32"
_VRtrMplsFwdPlcyNhgNHPushLabel8_Object = MibTableColumn
vRtrMplsFwdPlcyNhgNHPushLabel8 = _VRtrMplsFwdPlcyNhgNHPushLabel8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 82, 1, 8),
    _VRtrMplsFwdPlcyNhgNHPushLabel8_Type()
)
vRtrMplsFwdPlcyNhgNHPushLabel8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHPushLabel8.setStatus("current")


class _VRtrMplsFwdPlcyNhgNHPushLabel9_Type(Unsigned32):
    """Custom type vRtrMplsFwdPlcyNhgNHPushLabel9 based on Unsigned32"""
    defaultValue = 0


_VRtrMplsFwdPlcyNhgNHPushLabel9_Type.__name__ = "Unsigned32"
_VRtrMplsFwdPlcyNhgNHPushLabel9_Object = MibTableColumn
vRtrMplsFwdPlcyNhgNHPushLabel9 = _VRtrMplsFwdPlcyNhgNHPushLabel9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 82, 1, 9),
    _VRtrMplsFwdPlcyNhgNHPushLabel9_Type()
)
vRtrMplsFwdPlcyNhgNHPushLabel9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHPushLabel9.setStatus("current")


class _VRtrMplsFwdPlcyNhgNHPushLabel10_Type(Unsigned32):
    """Custom type vRtrMplsFwdPlcyNhgNHPushLabel10 based on Unsigned32"""
    defaultValue = 0


_VRtrMplsFwdPlcyNhgNHPushLabel10_Type.__name__ = "Unsigned32"
_VRtrMplsFwdPlcyNhgNHPushLabel10_Object = MibTableColumn
vRtrMplsFwdPlcyNhgNHPushLabel10 = _VRtrMplsFwdPlcyNhgNHPushLabel10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 82, 1, 10),
    _VRtrMplsFwdPlcyNhgNHPushLabel10_Type()
)
vRtrMplsFwdPlcyNhgNHPushLabel10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHPushLabel10.setStatus("current")
_VRtrMplsBindLblPathNhgNHPLTable_Object = MibTable
vRtrMplsBindLblPathNhgNHPLTable = _VRtrMplsBindLblPathNhgNHPLTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 83)
)
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgNHPLTable.setStatus("current")
_VRtrMplsBindLblPathNhgNHPLEntry_Object = MibTableRow
vRtrMplsBindLblPathNhgNHPLEntry = _VRtrMplsBindLblPathNhgNHPLEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 83, 1)
)
vRtrMplsBindLblPathNhgNHPLEntry.setIndexNames(
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathOwner"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLbl"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathId"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNhgIndex"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNhgNHType"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNHgNHPLIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNhgNHPLEntry.setStatus("current")
_VRtrMplsBindLblPathNHgNHPLIndex_Type = Unsigned32
_VRtrMplsBindLblPathNHgNHPLIndex_Object = MibTableColumn
vRtrMplsBindLblPathNHgNHPLIndex = _VRtrMplsBindLblPathNHgNHPLIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 83, 1, 1),
    _VRtrMplsBindLblPathNHgNHPLIndex_Type()
)
vRtrMplsBindLblPathNHgNHPLIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNHgNHPLIndex.setStatus("current")
_VRtrMplsBindLblPathNHgNHPLabel_Type = Unsigned32
_VRtrMplsBindLblPathNHgNHPLabel_Object = MibTableColumn
vRtrMplsBindLblPathNHgNHPLabel = _VRtrMplsBindLblPathNHgNHPLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 83, 1, 2),
    _VRtrMplsBindLblPathNHgNHPLabel_Type()
)
vRtrMplsBindLblPathNHgNHPLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblPathNHgNHPLabel.setStatus("current")
_VRtrMplsEndptPathNhgNHPLlbTable_Object = MibTable
vRtrMplsEndptPathNhgNHPLlbTable = _VRtrMplsEndptPathNhgNHPLlbTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 84)
)
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgNHPLlbTable.setStatus("current")
_VRtrMplsEndptPathNhgNHPLlbEntry_Object = MibTableRow
vRtrMplsEndptPathNhgNHPLlbEntry = _VRtrMplsEndptPathNhgNHPLlbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 84, 1)
)
vRtrMplsEndptPathNhgNHPLlbEntry.setIndexNames(
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptPathOwner"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptAddrType"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptAddress"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptPathId"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgIndex"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgNHType"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgNHPLblIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgNHPLlbEntry.setStatus("current")
_VRtrMplsEndptPathNhgNHPLblIndex_Type = Unsigned32
_VRtrMplsEndptPathNhgNHPLblIndex_Object = MibTableColumn
vRtrMplsEndptPathNhgNHPLblIndex = _VRtrMplsEndptPathNhgNHPLblIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 84, 1, 1),
    _VRtrMplsEndptPathNhgNHPLblIndex_Type()
)
vRtrMplsEndptPathNhgNHPLblIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgNHPLblIndex.setStatus("current")
_VRtrMplsEndptPathNhgNHPLabel_Type = Unsigned32
_VRtrMplsEndptPathNhgNHPLabel_Object = MibTableColumn
vRtrMplsEndptPathNhgNHPLabel = _VRtrMplsEndptPathNhgNHPLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 84, 1, 2),
    _VRtrMplsEndptPathNhgNHPLabel_Type()
)
vRtrMplsEndptPathNhgNHPLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptPathNhgNHPLabel.setStatus("current")
_VRtrMplsPceInitGenTblLastChg_Type = TimeStamp
_VRtrMplsPceInitGenTblLastChg_Object = MibScalar
vRtrMplsPceInitGenTblLastChg = _VRtrMplsPceInitGenTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 85),
    _VRtrMplsPceInitGenTblLastChg_Type()
)
vRtrMplsPceInitGenTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsPceInitGenTblLastChg.setStatus("current")
_VRtrMplsPceInitGenTable_Object = MibTable
vRtrMplsPceInitGenTable = _VRtrMplsPceInitGenTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 86)
)
if mibBuilder.loadTexts:
    vRtrMplsPceInitGenTable.setStatus("current")
_VRtrMplsPceInitGenEntry_Object = MibTableRow
vRtrMplsPceInitGenEntry = _VRtrMplsPceInitGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 86, 1)
)
vRtrMplsPceInitGenEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrMplsPceInitGenEntry.setStatus("current")
_VRtrMplsPceInitGenRowStatus_Type = RowStatus
_VRtrMplsPceInitGenRowStatus_Object = MibTableColumn
vRtrMplsPceInitGenRowStatus = _VRtrMplsPceInitGenRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 86, 1, 1),
    _VRtrMplsPceInitGenRowStatus_Type()
)
vRtrMplsPceInitGenRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsPceInitGenRowStatus.setStatus("current")


class _VRtrMplsPceInitGenSrte_Type(TruthValue):
    """Custom type vRtrMplsPceInitGenSrte based on TruthValue"""
    defaultValue = 2


_VRtrMplsPceInitGenSrte_Type.__name__ = "TruthValue"
_VRtrMplsPceInitGenSrte_Object = MibTableColumn
vRtrMplsPceInitGenSrte = _VRtrMplsPceInitGenSrte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 86, 1, 2),
    _VRtrMplsPceInitGenSrte_Type()
)
vRtrMplsPceInitGenSrte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsPceInitGenSrte.setStatus("current")


class _VRtrMplsPceInitGenSrteAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsPceInitGenSrteAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsPceInitGenSrteAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsPceInitGenSrteAdminState_Object = MibTableColumn
vRtrMplsPceInitGenSrteAdminState = _VRtrMplsPceInitGenSrteAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 86, 1, 3),
    _VRtrMplsPceInitGenSrteAdminState_Type()
)
vRtrMplsPceInitGenSrteAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsPceInitGenSrteAdminState.setStatus("current")
_VRtrMplsPceInitGenSrteOperState_Type = TmnxOperState
_VRtrMplsPceInitGenSrteOperState_Object = MibTableColumn
vRtrMplsPceInitGenSrteOperState = _VRtrMplsPceInitGenSrteOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 86, 1, 4),
    _VRtrMplsPceInitGenSrteOperState_Type()
)
vRtrMplsPceInitGenSrteOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsPceInitGenSrteOperState.setStatus("current")


class _VRtrMplsPceInitGenSrteOperDnRsn_Type(Integer32):
    """Custom type vRtrMplsPceInitGenSrteOperDnRsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("adminDown", 1),
          ("mplsOperDown", 2))
    )


_VRtrMplsPceInitGenSrteOperDnRsn_Type.__name__ = "Integer32"
_VRtrMplsPceInitGenSrteOperDnRsn_Object = MibTableColumn
vRtrMplsPceInitGenSrteOperDnRsn = _VRtrMplsPceInitGenSrteOperDnRsn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 86, 1, 5),
    _VRtrMplsPceInitGenSrteOperDnRsn_Type()
)
vRtrMplsPceInitGenSrteOperDnRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsPceInitGenSrteOperDnRsn.setStatus("current")
_VRtrMplsBindLblNHEgrStatsTable_Object = MibTable
vRtrMplsBindLblNHEgrStatsTable = _VRtrMplsBindLblNHEgrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 87)
)
if mibBuilder.loadTexts:
    vRtrMplsBindLblNHEgrStatsTable.setStatus("current")
_VRtrMplsBindLblNHEgrStatsEntry_Object = MibTableRow
vRtrMplsBindLblNHEgrStatsEntry = _VRtrMplsBindLblNHEgrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 87, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsBindLblNHEgrStatsEntry.setStatus("current")
_VRtrMplsBindLblEgrStatsAggPkts_Type = Counter64
_VRtrMplsBindLblEgrStatsAggPkts_Object = MibTableColumn
vRtrMplsBindLblEgrStatsAggPkts = _VRtrMplsBindLblEgrStatsAggPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 87, 1, 1),
    _VRtrMplsBindLblEgrStatsAggPkts_Type()
)
vRtrMplsBindLblEgrStatsAggPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblEgrStatsAggPkts.setStatus("current")
_VRtrMplsBindLblEgrStatsAggOctets_Type = Counter64
_VRtrMplsBindLblEgrStatsAggOctets_Object = MibTableColumn
vRtrMplsBindLblEgrStatsAggOctets = _VRtrMplsBindLblEgrStatsAggOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 87, 1, 2),
    _VRtrMplsBindLblEgrStatsAggOctets_Type()
)
vRtrMplsBindLblEgrStatsAggOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsBindLblEgrStatsAggOctets.setStatus("current")
_VRtrMplsEndptNHEgrStatsTable_Object = MibTable
vRtrMplsEndptNHEgrStatsTable = _VRtrMplsEndptNHEgrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 88)
)
if mibBuilder.loadTexts:
    vRtrMplsEndptNHEgrStatsTable.setStatus("current")
_VRtrMplsEndptNHEgrStatsEntry_Object = MibTableRow
vRtrMplsEndptNHEgrStatsEntry = _VRtrMplsEndptNHEgrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 88, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsEndptNHEgrStatsEntry.setStatus("current")
_VRtrMplsEndptEgrStatsAggPkts_Type = Counter64
_VRtrMplsEndptEgrStatsAggPkts_Object = MibTableColumn
vRtrMplsEndptEgrStatsAggPkts = _VRtrMplsEndptEgrStatsAggPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 88, 1, 1),
    _VRtrMplsEndptEgrStatsAggPkts_Type()
)
vRtrMplsEndptEgrStatsAggPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptEgrStatsAggPkts.setStatus("current")
_VRtrMplsEndptEgrStatsAggOctets_Type = Counter64
_VRtrMplsEndptEgrStatsAggOctets_Object = MibTableColumn
vRtrMplsEndptEgrStatsAggOctets = _VRtrMplsEndptEgrStatsAggOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 88, 1, 2),
    _VRtrMplsEndptEgrStatsAggOctets_Type()
)
vRtrMplsEndptEgrStatsAggOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsEndptEgrStatsAggOctets.setStatus("current")
_VRtrMplsLspPathEgressStatsTable_Object = MibTable
vRtrMplsLspPathEgressStatsTable = _VRtrMplsLspPathEgressStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 89)
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathEgressStatsTable.setStatus("current")
_VRtrMplsLspPathEgressStatsEntry_Object = MibTableRow
vRtrMplsLspPathEgressStatsEntry = _VRtrMplsLspPathEgressStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 89, 1)
)
vRtrMplsLspPathEgressStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
    (0, "MPLS-TE-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathEgressStatsEntry.setStatus("current")
_VRtrMplsLspPathEgrStatsOperState_Type = TmnxOperState
_VRtrMplsLspPathEgrStatsOperState_Object = MibTableColumn
vRtrMplsLspPathEgrStatsOperState = _VRtrMplsLspPathEgrStatsOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 89, 1, 1),
    _VRtrMplsLspPathEgrStatsOperState_Type()
)
vRtrMplsLspPathEgrStatsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathEgrStatsOperState.setStatus("current")
_VRtrMplsLspEgressStatsAggrPkts_Type = Counter64
_VRtrMplsLspEgressStatsAggrPkts_Object = MibTableColumn
vRtrMplsLspEgressStatsAggrPkts = _VRtrMplsLspEgressStatsAggrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 89, 1, 2),
    _VRtrMplsLspEgressStatsAggrPkts_Type()
)
vRtrMplsLspEgressStatsAggrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspEgressStatsAggrPkts.setStatus("current")
_VRtrMplsLspEgressStatsAggrOctets_Type = Counter64
_VRtrMplsLspEgressStatsAggrOctets_Object = MibTableColumn
vRtrMplsLspEgressStatsAggrOctets = _VRtrMplsLspEgressStatsAggrOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 89, 1, 3),
    _VRtrMplsLspEgressStatsAggrOctets_Type()
)
vRtrMplsLspEgressStatsAggrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspEgressStatsAggrOctets.setStatus("current")
_VRtrMplsPathHopTableLastChg_Type = TimeStamp
_VRtrMplsPathHopTableLastChg_Object = MibScalar
vRtrMplsPathHopTableLastChg = _VRtrMplsPathHopTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 90),
    _VRtrMplsPathHopTableLastChg_Type()
)
vRtrMplsPathHopTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsPathHopTableLastChg.setStatus("current")
_VRtrMplsPathHopTable_Object = MibTable
vRtrMplsPathHopTable = _VRtrMplsPathHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 91)
)
if mibBuilder.loadTexts:
    vRtrMplsPathHopTable.setStatus("current")
_VRtrMplsPathHopEntry_Object = MibTableRow
vRtrMplsPathHopEntry = _VRtrMplsPathHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 91, 1)
)
vRtrMplsPathHopEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsPathIndex"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsPathHopIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsPathHopEntry.setStatus("current")


class _VRtrMplsPathIndex_Type(Unsigned32):
    """Custom type vRtrMplsPathIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsPathIndex_Type.__name__ = "Unsigned32"
_VRtrMplsPathIndex_Object = MibTableColumn
vRtrMplsPathIndex = _VRtrMplsPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 91, 1, 1),
    _VRtrMplsPathIndex_Type()
)
vRtrMplsPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsPathIndex.setStatus("current")


class _VRtrMplsPathHopIndex_Type(Unsigned32):
    """Custom type vRtrMplsPathHopIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsPathHopIndex_Type.__name__ = "Unsigned32"
_VRtrMplsPathHopIndex_Object = MibTableColumn
vRtrMplsPathHopIndex = _VRtrMplsPathHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 91, 1, 2),
    _VRtrMplsPathHopIndex_Type()
)
vRtrMplsPathHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsPathHopIndex.setStatus("current")
_VRtrMplsPathHopRowStatus_Type = RowStatus
_VRtrMplsPathHopRowStatus_Object = MibTableColumn
vRtrMplsPathHopRowStatus = _VRtrMplsPathHopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 91, 1, 3),
    _VRtrMplsPathHopRowStatus_Type()
)
vRtrMplsPathHopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsPathHopRowStatus.setStatus("current")
_VRtrMplsPathHopLastChange_Type = TimeStamp
_VRtrMplsPathHopLastChange_Object = MibTableColumn
vRtrMplsPathHopLastChange = _VRtrMplsPathHopLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 91, 1, 4),
    _VRtrMplsPathHopLastChange_Type()
)
vRtrMplsPathHopLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsPathHopLastChange.setStatus("current")


class _VRtrMplsPathHopAddrType_Type(InetAddressType):
    """Custom type vRtrMplsPathHopAddrType based on InetAddressType"""
    defaultValue = 0


_VRtrMplsPathHopAddrType_Type.__name__ = "InetAddressType"
_VRtrMplsPathHopAddrType_Object = MibTableColumn
vRtrMplsPathHopAddrType = _VRtrMplsPathHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 91, 1, 5),
    _VRtrMplsPathHopAddrType_Type()
)
vRtrMplsPathHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsPathHopAddrType.setStatus("current")


class _VRtrMplsPathHopAddr_Type(InetAddress):
    """Custom type vRtrMplsPathHopAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsPathHopAddr_Type.__name__ = "InetAddress"
_VRtrMplsPathHopAddr_Object = MibTableColumn
vRtrMplsPathHopAddr = _VRtrMplsPathHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 91, 1, 6),
    _VRtrMplsPathHopAddr_Type()
)
vRtrMplsPathHopAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsPathHopAddr.setStatus("current")


class _VRtrMplsPathHopStrictOrLoose_Type(Integer32):
    """Custom type vRtrMplsPathHopStrictOrLoose based on Integer32"""
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
        *(("notApplicable", 0),
          ("strict", 1),
          ("loose", 2))
    )


_VRtrMplsPathHopStrictOrLoose_Type.__name__ = "Integer32"
_VRtrMplsPathHopStrictOrLoose_Object = MibTableColumn
vRtrMplsPathHopStrictOrLoose = _VRtrMplsPathHopStrictOrLoose_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 91, 1, 7),
    _VRtrMplsPathHopStrictOrLoose_Type()
)
vRtrMplsPathHopStrictOrLoose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsPathHopStrictOrLoose.setStatus("current")


class _VRtrMplsPathHopSidLabel_Type(Unsigned32):
    """Custom type vRtrMplsPathHopSidLabel based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1048575),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_VRtrMplsPathHopSidLabel_Type.__name__ = "Unsigned32"
_VRtrMplsPathHopSidLabel_Object = MibTableColumn
vRtrMplsPathHopSidLabel = _VRtrMplsPathHopSidLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 91, 1, 8),
    _VRtrMplsPathHopSidLabel_Type()
)
vRtrMplsPathHopSidLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsPathHopSidLabel.setStatus("current")
_VRtrMplsLspTemplateExtTable_Object = MibTable
vRtrMplsLspTemplateExtTable = _VRtrMplsLspTemplateExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 92)
)
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateExtTable.setStatus("current")
_VRtrMplsLspTemplateExtEntry_Object = MibTableRow
vRtrMplsLspTemplateExtEntry = _VRtrMplsLspTemplateExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 92, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateExtEntry.setStatus("current")


class _VRtrMplsLspTempExtFallbkPathComp_Type(Integer32):
    """Custom type vRtrMplsLspTempExtFallbkPathComp based on Integer32"""
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
        *(("notApplicable", 0),
          ("none", 1),
          ("localCspf", 2))
    )


_VRtrMplsLspTempExtFallbkPathComp_Type.__name__ = "Integer32"
_VRtrMplsLspTempExtFallbkPathComp_Object = MibTableColumn
vRtrMplsLspTempExtFallbkPathComp = _VRtrMplsLspTempExtFallbkPathComp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 92, 1, 1),
    _VRtrMplsLspTempExtFallbkPathComp_Type()
)
vRtrMplsLspTempExtFallbkPathComp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempExtFallbkPathComp.setStatus("current")


class _VRtrMplsLspTempExtPceControl_Type(TruthValue):
    """Custom type vRtrMplsLspTempExtPceControl based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempExtPceControl_Type.__name__ = "TruthValue"
_VRtrMplsLspTempExtPceControl_Object = MibTableColumn
vRtrMplsLspTempExtPceControl = _VRtrMplsLspTempExtPceControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 92, 1, 2),
    _VRtrMplsLspTempExtPceControl_Type()
)
vRtrMplsLspTempExtPceControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempExtPceControl.setStatus("current")


class _VRtrMplsLspTempExtOverrideTunElc_Type(TruthValue):
    """Custom type vRtrMplsLspTempExtOverrideTunElc based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempExtOverrideTunElc_Type.__name__ = "TruthValue"
_VRtrMplsLspTempExtOverrideTunElc_Object = MibTableColumn
vRtrMplsLspTempExtOverrideTunElc = _VRtrMplsLspTempExtOverrideTunElc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 92, 1, 3),
    _VRtrMplsLspTempExtOverrideTunElc_Type()
)
vRtrMplsLspTempExtOverrideTunElc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempExtOverrideTunElc.setStatus("current")


class _VRtrMplsLspTempExtPrefTransFrr_Type(TruthValue):
    """Custom type vRtrMplsLspTempExtPrefTransFrr based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempExtPrefTransFrr_Type.__name__ = "TruthValue"
_VRtrMplsLspTempExtPrefTransFrr_Object = MibTableColumn
vRtrMplsLspTempExtPrefTransFrr = _VRtrMplsLspTempExtPrefTransFrr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 92, 1, 4),
    _VRtrMplsLspTempExtPrefTransFrr_Type()
)
vRtrMplsLspTempExtPrefTransFrr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempExtPrefTransFrr.setStatus("current")


class _VRtrMplsLspTempExtReturnPathLbl_Type(Unsigned32):
    """Custom type vRtrMplsLspTempExtReturnPathLbl based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1048512),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_VRtrMplsLspTempExtReturnPathLbl_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempExtReturnPathLbl_Object = MibTableColumn
vRtrMplsLspTempExtReturnPathLbl = _VRtrMplsLspTempExtReturnPathLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 92, 1, 5),
    _VRtrMplsLspTempExtReturnPathLbl_Type()
)
vRtrMplsLspTempExtReturnPathLbl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempExtReturnPathLbl.setStatus("current")


class _VRtrMplsLspTempExtSoftPreemption_Type(TruthValue):
    """Custom type vRtrMplsLspTempExtSoftPreemption based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempExtSoftPreemption_Type.__name__ = "TruthValue"
_VRtrMplsLspTempExtSoftPreemption_Object = MibTableColumn
vRtrMplsLspTempExtSoftPreemption = _VRtrMplsLspTempExtSoftPreemption_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 92, 1, 6),
    _VRtrMplsLspTempExtSoftPreemption_Type()
)
vRtrMplsLspTempExtSoftPreemption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempExtSoftPreemption.setStatus("current")
_VRtrMplsLspTempPathProTblLastChg_Type = TimeStamp
_VRtrMplsLspTempPathProTblLastChg_Object = MibScalar
vRtrMplsLspTempPathProTblLastChg = _VRtrMplsLspTempPathProTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 95),
    _VRtrMplsLspTempPathProTblLastChg_Type()
)
vRtrMplsLspTempPathProTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTempPathProTblLastChg.setStatus("current")
_VRtrMplsLspTempPathProfTable_Object = MibTable
vRtrMplsLspTempPathProfTable = _VRtrMplsLspTempPathProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 96)
)
if mibBuilder.loadTexts:
    vRtrMplsLspTempPathProfTable.setStatus("current")
_VRtrMplsLspTempPathProfEntry_Object = MibTableRow
vRtrMplsLspTempPathProfEntry = _VRtrMplsLspTempPathProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 96, 1)
)
vRtrMplsLspTempPathProfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateName"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspTempPathProfId"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspTempPathProfEntry.setStatus("current")


class _VRtrMplsLspTempPathProfId_Type(Unsigned32):
    """Custom type vRtrMplsLspTempPathProfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VRtrMplsLspTempPathProfId_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempPathProfId_Object = MibTableColumn
vRtrMplsLspTempPathProfId = _VRtrMplsLspTempPathProfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 96, 1, 1),
    _VRtrMplsLspTempPathProfId_Type()
)
vRtrMplsLspTempPathProfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspTempPathProfId.setStatus("current")
_VRtrMplsLspTempPathProfRowStatus_Type = RowStatus
_VRtrMplsLspTempPathProfRowStatus_Object = MibTableColumn
vRtrMplsLspTempPathProfRowStatus = _VRtrMplsLspTempPathProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 96, 1, 2),
    _VRtrMplsLspTempPathProfRowStatus_Type()
)
vRtrMplsLspTempPathProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempPathProfRowStatus.setStatus("current")
_VRtrMplsLspTempPathProfLastChg_Type = TimeStamp
_VRtrMplsLspTempPathProfLastChg_Object = MibTableColumn
vRtrMplsLspTempPathProfLastChg = _VRtrMplsLspTempPathProfLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 96, 1, 3),
    _VRtrMplsLspTempPathProfLastChg_Type()
)
vRtrMplsLspTempPathProfLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTempPathProfLastChg.setStatus("current")


class _VRtrMplsLspTempPathProfGroupId_Type(Unsigned32):
    """Custom type vRtrMplsLspTempPathProfGroupId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrMplsLspTempPathProfGroupId_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempPathProfGroupId_Object = MibTableColumn
vRtrMplsLspTempPathProfGroupId = _VRtrMplsLspTempPathProfGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 96, 1, 4),
    _VRtrMplsLspTempPathProfGroupId_Type()
)
vRtrMplsLspTempPathProfGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempPathProfGroupId.setStatus("current")
_TmnxMplsNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxMplsNotifyPrefix = _TmnxMplsNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6)
)
_TmnxMplsNotifications_ObjectIdentity = ObjectIdentity
tmnxMplsNotifications = _TmnxMplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0)
)
vRtrMplsLspEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsLspStatEntry")
)
vRtrMplsLspStatEntry.setIndexNames(*vRtrMplsLspEntry.getIndexNames())
vRtrMplsLspPathEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsLspPathStatEntry")
)
vRtrMplsLspPathStatEntry.setIndexNames(*vRtrMplsLspPathEntry.getIndexNames())
vRtrMplsGeneralEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsGeneralStatEntry")
)
vRtrMplsGeneralStatEntry.setIndexNames(*vRtrMplsGeneralEntry.getIndexNames())
vRtrMplsIfEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsIfStatEntry")
)
vRtrMplsIfStatEntry.setIndexNames(*vRtrMplsIfEntry.getIndexNames())
mplsTunnelARHopEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsTunnelARHopEntry")
)
vRtrMplsTunnelARHopEntry.setIndexNames(*mplsTunnelARHopEntry.getIndexNames())
vRtrMplsP2mpInstEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsP2mpInstStatEntry")
)
vRtrMplsP2mpInstStatEntry.setIndexNames(*vRtrMplsP2mpInstEntry.getIndexNames())
vRtrMplsS2lSubLspEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsS2lSubLspStatEntry")
)
vRtrMplsS2lSubLspStatEntry.setIndexNames(*vRtrMplsS2lSubLspEntry.getIndexNames())
mplsInSegmentEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsInSegmentEntry")
)
vRtrMplsInSegmentEntry.setIndexNames(*mplsInSegmentEntry.getIndexNames())
mplsOutSegmentEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsOutSegmentEntry")
)
vRtrMplsOutSegmentEntry.setIndexNames(*mplsOutSegmentEntry.getIndexNames())
vRtrMplsLspStatsEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsLspStatisticsEntry")
)
vRtrMplsLspStatisticsEntry.setIndexNames(*vRtrMplsLspStatsEntry.getIndexNames())
vRtrMplsLspPathEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsLspPathOperEntry")
)
vRtrMplsLspPathOperEntry.setIndexNames(*vRtrMplsLspPathEntry.getIndexNames())
vRtrMplsLspEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsLspExtEntry")
)
vRtrMplsLspExtEntry.setIndexNames(*vRtrMplsLspEntry.getIndexNames())
vRtrMplsFwdPlcyNhgNHEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsFwdPlcyNhgNHPushLblEntry")
)
vRtrMplsFwdPlcyNhgNHPushLblEntry.setIndexNames(*vRtrMplsFwdPlcyNhgNHEntry.getIndexNames())
vRtrMplsBindLblPathNhgNHEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsBindLblNHEgrStatsEntry")
)
vRtrMplsBindLblNHEgrStatsEntry.setIndexNames(*vRtrMplsBindLblPathNhgNHEntry.getIndexNames())
vRtrMplsEndptPathNhgNHEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsEndptNHEgrStatsEntry")
)
vRtrMplsEndptNHEgrStatsEntry.setIndexNames(*vRtrMplsEndptPathNhgNHEntry.getIndexNames())
vRtrMplsLspTemplateEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsLspTemplateExtEntry")
)
vRtrMplsLspTemplateExtEntry.setIndexNames(*vRtrMplsLspTemplateEntry.getIndexNames())

# Managed Objects groups

tmnxMplsLspPathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 3)
)
tmnxMplsLspPathGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTableSpinlock"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCos"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProperties"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBwProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathPreference"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCosSource"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathClassOfService"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSharing"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLspId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryTimeRemaining"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelARHopListIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNextOptimize"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelCRHopListIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryAttempts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTransitionCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCspfQueries"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspPathGroup.setStatus("obsolete")

tmnxMplsXCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 4)
)
tmnxMplsXCGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsXCIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInSegmentIfIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInSegmentLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutSegmentIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsERHopTunnelIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsARHopTunnelIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsRsvpSessionIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCCHopTableIndex"))
)
if mibBuilder.loadTexts:
    tmnxMplsXCGroup.setStatus("current")

tmnxMplsIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 5)
)
tmnxMplsIfGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsIfAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfAdminGroup"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfTxPktCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfRxPktCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfTxOctetCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfRxOctetCount"))
)
if mibBuilder.loadTexts:
    tmnxMplsIfGroup.setStatus("current")

tmnxMplsTunnelARHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 6)
)
tmnxMplsTunnelARHopGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopProtection"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopRouterId"))
)
if mibBuilder.loadTexts:
    tmnxMplsTunnelARHopGroup.setStatus("obsolete")

tmnxMplsTunnelCHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 7)
)
tmnxMplsTunnelCHopGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIpv4Addr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIpv4PrefixLen"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIpv6Addr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIpv6PrefixLen"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopAsNumber"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopLspId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopStrictOrLoose"))
)
if mibBuilder.loadTexts:
    tmnxMplsTunnelCHopGroup.setStatus("current")

tmnxMplsAdminGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 8)
)
tmnxMplsAdminGroupGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsAdminGroupRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsAdminGroupValue"))
)
if mibBuilder.loadTexts:
    tmnxMplsAdminGroupGroup.setStatus("obsolete")

tmnxMplsFSGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 9)
)
tmnxMplsFSGroupGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsFSGroupRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFSGroupCost"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFSGroupParamsRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxMplsFSGroupGroup.setStatus("obsolete")

tmnxMplsNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 10)
)
tmnxMplsNotifyObjsGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspNotificationReasonCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNotificationReasonCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsNotifyRow"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyObjsGroup.setStatus("current")

tmnxMplsGlobalR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 12)
)
tmnxMplsGlobalR2r1Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralPropagateTtl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralTE"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNewLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralResignalTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTerminate"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalR2r1Group.setStatus("obsolete")

tmnxMplsLspR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 13)
)
tmnxMplsLspR2r1Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFromAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspToAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOutSegIndx"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspDecrementTtl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspClassOfService"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPreference"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspBwProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpResvStyle"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpAdspec"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRMethod"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOctets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPackets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAge"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPrimaryTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTransitions"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastTransition"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathChanges"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastPathChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspConfiguredPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStandbyPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperationalPaths"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspR2r1Group.setStatus("obsolete")

tmnxMplsLabelRangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 15)
)
tmnxMplsLabelRangeGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLabelRangeMin"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelRangeMax"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelRangeAging"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelRangeAvailable"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsStaticLSPLabelOwner"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsStaticSvcLabelOwner"))
)
if mibBuilder.loadTexts:
    tmnxMplsLabelRangeGroup.setStatus("current")

tmnxMplsGlobalV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 16)
)
tmnxMplsGlobalV5v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralPropagateTtl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralTE"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNewLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralResignalTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralHoldTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicBypass"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV5v0Group.setStatus("obsolete")

tmnxMplsLspV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 17)
)
tmnxMplsLspV5v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFromAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspToAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOutSegIndx"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspDecrementTtl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspClassOfService"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPreference"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspBwProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpResvStyle"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpAdspec"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRMethod"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOctets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPackets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAge"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPrimaryTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTransitions"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastTransition"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathChanges"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastPathChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspConfiguredPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStandbyPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperationalPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHoldTimer"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspV5v0Group.setStatus("obsolete")

tmnxMplsGlobalV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 18)
)
tmnxMplsGlobalV6v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralPropagateTtl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralTE"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNewLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralResignalTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralHoldTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicBypass"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNextResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperDownReason"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralSrlgFrr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralSrlgFrrStrict"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV6v0Group.setStatus("obsolete")

tmnxMplsSrlgV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 19)
)
tmnxMplsSrlgV6v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpTableLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpValue"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfSrlgGrpTblLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfSrlgGrpRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfSrlgGrpLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxMplsSrlgV6v0Group.setStatus("obsolete")

tmnxMplsLspPathV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 20)
)
tmnxMplsLspPathV6v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSrlg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSrlgDisjoint"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspPathV6v0Group.setStatus("current")

tmnxMplsIfV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 21)
)
tmnxMplsIfV6v0Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsIfTeMetric")
)
if mibBuilder.loadTexts:
    tmnxMplsIfV6v0Group.setStatus("current")

tmnxMplsLspV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 22)
)
tmnxMplsLspV6v0Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspCspfTeMetricEnabled")
)
if mibBuilder.loadTexts:
    tmnxMplsLspV6v0Group.setStatus("obsolete")

tmnxMplsLspPathV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 23)
)
tmnxMplsLspPathV6v1Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTableSpinlock"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCos"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProperties"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBwProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathPreference"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCosSource"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathClassOfService"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSharing"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLspId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryTimeRemaining"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelARHopListIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNextOptimize"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelCRHopListIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryAttempts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTransitionCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCspfQueries"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastResigAttempt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBEnd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBTypeInProg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBStarted"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBNextRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBRetryAttempts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailNodeArType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailNodeAddr"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspPathV6v1Group.setStatus("obsolete")

tmnxMplsObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 24)
)
tmnxMplsObsoleteGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFSGroupCost"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFSGroupParamsRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFSGroupRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxMplsObsoleteGroup.setStatus("current")

tmnxMplsLspV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 25)
)
tmnxMplsLspV7v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspP2mpId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspClassType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLdpOverRsvpInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLeastFill"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspVprnAutoBindInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspConfP2mpInstances"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspV7v0Group.setStatus("current")

tmnxMplsGlobalV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 26)
)
tmnxMplsGlobalV7v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNewP2mpInstIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralS2lOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralS2lTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralS2lTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralLeastFillMinThd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenLeastFillReoptiThd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralUseSrlgDB"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInSegmentNumS2ls"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutSegmentNumS2ls"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralP2mpResigTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralP2mpNextResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralSecFastRetryTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspFRTimer"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV7v0Group.setStatus("current")

tmnxMplsP2mpInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 27)
)
tmnxMplsP2mpInstanceGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstTblLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstProperties"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstLspId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstFailNodeArType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstAdminGrpInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstAdminGrpExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstOperBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstOperMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstLastResigAttpt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstLastMBBType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstLastMBBEnd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstLastMBBMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstLastMBBState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstMBBTypeInProg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstMBBStarted"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstMBBNextRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstMBBRetryAttpts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstMBBFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstMBBFailNodeType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstMBBFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatS2lChanges"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatLastS2lChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatConfiguredS2ls"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatOperationalS2ls"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatLastS2lTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatLastS2lTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatTransitions"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatLastTrans"))
)
if mibBuilder.loadTexts:
    tmnxMplsP2mpInstanceGroup.setStatus("current")

tmnxMplsP2mpS2lGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 28)
)
tmnxMplsP2mpS2lGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTblLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspProperties"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubGroupId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspRetryTimeRemain"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspFailNodeArType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspOperBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspOperMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspLastResigAttpt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspLastMBBType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspLastMBBEnd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspLastMBBMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspLastMBBState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBTypeInProg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBStarted"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBNextRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBRetryAttpts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBFailNodeType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspUpTime"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspDownTime"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspRetryAttempts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTransitionCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspCspfQueries"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTunARHopLtIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTunCRHopLtIndex"))
)
if mibBuilder.loadTexts:
    tmnxMplsP2mpS2lGroup.setStatus("current")

tmnxMplsNotifyObjsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 29)
)
tmnxMplsNotifyObjsV7v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNotifIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspNtDstAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspNtDstAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNotifReasonCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCongChgPercent"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyObjsV7v0Group.setStatus("current")

tmnxMplsLspPathV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 31)
)
tmnxMplsLspPathV7v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathClassType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathResignalEligible"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathIsFastRetry"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspPathV7v0Group.setStatus("current")

tmnxMplsSrlgV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 32)
)
tmnxMplsSrlgV7v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBRtrIdRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBRtrIdAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBRtrIdLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBRtrIdTblLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBIfRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBIfLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBIfTblLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxMplsSrlgV7v0Group.setStatus("current")

tmnxMplsLspStatsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 33)
)
tmnxMplsLspStatsV7v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsAccntingPolicy"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsCollectStats"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsTblLastChgd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc0"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc0High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc0Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc1"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc1High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc1Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc2"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc2High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc2Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc3"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc3High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc3Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc4"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc4High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc4Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc5"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc5High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc5Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc6"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc6High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc6Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc7"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc7High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc7Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc0"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc0High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc0Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc1"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc1High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc1Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc2"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc2High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc2Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc3"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc3High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc3Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc4"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc4High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc4Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc5"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc5High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc5Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc6"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc6High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc6Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc7"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc7High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc7Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc0"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc0High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc0Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc1"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc1High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc1Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc2"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc2High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc2Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc3"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc3High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc3Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc4"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc4High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc4Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc5"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc5High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc5Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc6"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc6High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc6Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc7"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc7High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc7Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc0"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc0High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc0Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc1"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc1High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc1Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc2"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc2High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc2Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc3"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc3High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc3Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc4"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc4High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc4Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc5"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc5High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc5Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc6"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc6High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc6Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc7"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc7High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc7Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsPSBMatch"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralLspEgrStatCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralLspIgrStatCount"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspStatsV7v0Group.setStatus("current")

tmnxMplsLspV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 34)
)
tmnxMplsLspV8v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspMainCTRetryLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcut"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspV8v0Group.setStatus("current")

tmnxMplsLspPathV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 35)
)
tmnxMplsLspPathV8v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBackupCT"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMainCTRetryRem"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperCT"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNewPathIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBMainCTRetryRem"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspPathV8v0Group.setStatus("current")

tmnxMplsNotifyObjsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 36)
)
tmnxMplsNotifyObjsV8v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMbbStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMbbReasonCode"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyObjsV8v0Group.setStatus("current")

tmnxMplsGlobalV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 38)
)
tmnxMplsGlobalV8v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralShortTTLPropLocal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralShortTTLPropTrans"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralAutoBWDefSampMul"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralAutoBWDefAdjMul"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralExpBackoffRetry"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV8v0Group.setStatus("current")

tmnxMplsLspTemplateV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 39)
)
tmnxMplsLspTemplateV8v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateTblLastChgd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateDefaultPath"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateAdmGrpIncl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateAdmGrpExcl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateFRMethod"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateFRHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateRetryLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateRetryTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateCspfTeMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOriginTemplate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateLspCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateMvpnRefCount"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspTemplateV8v0Group.setStatus("obsolete")

tmnxMplsLspAutoBWV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 40)
)
tmnxMplsLspAutoBWV8v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWTableLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWAdjDNPercent"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWAdjDNMbps"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWAdjMultiplier"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWAdjUPPercent"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWAdjUPMbps"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWMaxBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWMinBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWMonitorBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWOverFlow"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWOvrFlwThreshold"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWOvrFlwBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWSampMultiplier"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWSampTime"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWLastAdj"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWLastAdjCause"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWNextAdj"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWMaxAvgRate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWLastAvgRate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWCurrentBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWAdjTime"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWOvrFlwCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWSampCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWAdjCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWSampInterval"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSigBWMBBInProg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSigBWLastMBB"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspAutoBWV8v0Group.setStatus("current")

tmnxMplsGlobalV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 41)
)
tmnxMplsGlobalV9v0Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralCspfOnLooseHop")
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV9v0Group.setStatus("current")

tmnxMplsLspV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 42)
)
tmnxMplsLspV9v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspCspfToFirstLoose"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPropAdminGroup"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspV9v0Group.setStatus("obsolete")

tmnxMplsLspV9v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 43)
)
tmnxMplsLspV9v0R4Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspBgpShortcut"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspBgpTransportTunnel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSwitchStbyPath"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSwitchStbyPathIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSwitchStbyPathForce"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralP2PMaxByPassAssoc"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExcludeNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExcludeNodeAddrType"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspV9v0R4Group.setStatus("current")

tmnxMplsNotifyObjsV9v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 44)
)
tmnxMplsNotifyObjsV9v0R4Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspSwitchStbyReasonCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOldTunnelIndex"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyObjsV9v0R4Group.setStatus("current")

tmnxMplsLspPathV9v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 46)
)
tmnxMplsLspPathV9v0R4Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathActiveByManual")
)
if mibBuilder.loadTexts:
    tmnxMplsLspPathV9v0R4Group.setStatus("current")

tmnxMplsGlobalV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 47)
)
tmnxMplsGlobalV10v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGenP2pActPathFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenP2mpS2lFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspIsFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperAdminGrpIncl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperAdminGrExcld"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperCspfToFrstLs"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperLeastFill"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRsvpAdspec"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperPropAdminGrp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperFRHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenLspInitRetryTimeout"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcutLfaType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLoggerEventBundling"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenIssuMplsLockdown"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV10v0Group.setStatus("obsolete")

tmnxMplsTpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 48)
)
tmnxMplsTpGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspToAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFromAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspToNodeId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFromNodeId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspDestGlobalId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspDestTunnelNum"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenMplsTpLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenMplsTpLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenMplsTpLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenMplsTpOrigPathInst"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenMplsTpTranPathInst"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenMplsTpTermPathInst"))
)
if mibBuilder.loadTexts:
    tmnxMplsTpGroup.setStatus("current")

tmnxMplsNotifyObjsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 49)
)
tmnxMplsNotifyObjsV10v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifRednIndicesBitMap"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifyRednBundlingType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifyRednNumOfBitsSet"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifyRednStartIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifyRednEndIndex"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyObjsV10v0Group.setStatus("current")

tmnxMplsFRAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 51)
)
tmnxMplsFRAdminGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGenFRAdminGroup"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateFRPropAdmGrp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRPropAdminGroup"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopEgressAdmGrp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperFRPropAdmGrp"))
)
if mibBuilder.loadTexts:
    tmnxMplsFRAdminGroup.setStatus("current")

tmnxMplsGlobalV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 52)
)
tmnxMplsGlobalV11v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperInterArea"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopUnnumIfID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIsABR"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopUnnumIfID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFromAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspToAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOutSegIndx"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpResvStyle"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpAdspec"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRMethod"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOctets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPackets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAge"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPrimaryTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTransitions"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastTransition"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathChanges"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastPathChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspConfiguredPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStandbyPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperationalPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHoldTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTableSpinlock"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProperties"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathPreference"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLspId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryTimeRemaining"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelARHopListIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNextOptimize"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelCRHopListIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryAttempts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTransitionCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCspfQueries"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastResigAttempt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBEnd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBTypeInProg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBStarted"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBNextRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBRetryAttempts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailNodeArType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNewLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralResignalTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralHoldTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicBypass"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNextResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperDownReason"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralSrlgFrr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralSrlgFrrStrict"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplatePropAdmGrp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelMaxStaticLspLabels"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelMaxStaticSvcLabels"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspInterArea"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenP2pActPathFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenP2mpS2lFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspIsFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperAdminGrpIncl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperAdminGrExcld"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperLeastFill"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRsvpAdspec"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperPropAdminGrp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperFRHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenLspInitRetryTimeout"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcutLfaType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLoggerEventBundling"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenIssuMplsLockdown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPropAdminGroup"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcutRelOffset"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV11v0Group.setStatus("obsolete")

tmnxMplsV11v0ObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 53)
)
tmnxMplsV11v0ObsoleteGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspDecrementTtl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspClassOfService"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCos"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCosSource"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathClassOfService"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspBwProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBwProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPreference"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSharing"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralPropagateTtl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralTE"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperCspfToFrstLs"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspCspfToFirstLoose"))
)
if mibBuilder.loadTexts:
    tmnxMplsV11v0ObsoleteGroup.setStatus("current")

tmnxMplsLspTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 54)
)
tmnxMplsLspTemplateGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateBgpShortcut"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateIgpShortcut"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateLdpOverRsvp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateLeastFill"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateVprnAutoBind"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempIgpSCutLfaType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempIgpSCutRelOffset"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWTblLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWAdjDNPer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWAdjDNMbps"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWAdjUPPer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWAdjUPMbps"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWMaxBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWMinBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWMntrBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWAdjMult"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWOverFlow"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWOvrFlwThr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWOvrFlwBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWSampMult"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWSampTime"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWInherit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateEgrStats"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempCollectStats"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAccntingPolicy"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTemplPlcyBindTblLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplPlcyBindLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplPlcyBindRowStat"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplPlcyBind1"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplPlcyBind2"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplPlcyBind3"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplPlcyBind4"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplPlcyBind5"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplPlcyBindOneHop"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWBeWeight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWL2Weight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWAfWeight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWL1Weight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWH2Weight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWEfWeight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWH1Weight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWNcWeight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateFromAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateFromAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateClassType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempBkupClassType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempBgpTransportTunn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempMainCTRetryLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateRsvpAdspec"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspTemplateGroup.setStatus("current")

tmnxMplsLspAutoBWFcWtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 56)
)
tmnxMplsLspAutoBWFcWtGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWBeWeight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWL2Weight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWAfWeight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWL1Weight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWH2Weight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWEfWeight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWH1Weight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWNcWeight"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspAutoBWFcWtGroup.setStatus("current")

tmnxMplsGlobalV11v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 57)
)
tmnxMplsGlobalV11v0R4Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsTpOnly"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralMeshP2pOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOneHopP2pOrigin"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenRetryOnIgpOverload"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV11v0R4Group.setStatus("current")

tmnxMplsV12v0ObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 58)
)
tmnxMplsV12v0ObsoleteGroup.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspBandwidth")
)
if mibBuilder.loadTexts:
    tmnxMplsV12v0ObsoleteGroup.setStatus("current")

tmnxMplsNotifyObjsIgpOverload = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 59)
)
tmnxMplsNotifyObjsIgpOverload.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsIgpOverloadRtrAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIgpOverloadRtrAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIgpOverloadIgpType"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyObjsIgpOverload.setStatus("current")

tmnxMplsLspTempInStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 61)
)
tmnxMplsLspTempInStatsGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatTblLstChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatCollectStat"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatAccntPolicy"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatMaxStats"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsLspType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatTotlSession"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsEgrIndexUnAvail"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspTempInStatsGroup.setStatus("current")

tmnxMplsAutoBwUnderflowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 62)
)
tmnxMplsAutoBwUnderflowGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWUnderFlow"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWUndFlwThreshold"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWUndFlwBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWUndFlwCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWMaxUndFlwBw"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWUnderFlow"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWUndFlwThr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWUndFlwBW"))
)
if mibBuilder.loadTexts:
    tmnxMplsAutoBwUnderflowGroup.setStatus("current")

tmnxMplsBgpLabelRetentionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 63)
)
tmnxMplsBgpLabelRetentionGroup.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLabelBgpLabelsHoldTimer")
)
if mibBuilder.loadTexts:
    tmnxMplsBgpLabelRetentionGroup.setStatus("current")

tmnxMplsGlobalV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 64)
)
tmnxMplsGlobalV12v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopUnnumIfID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIsABR"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopUnnumIfID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplatePropAdmGrp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelMaxStaticLspLabels"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelMaxStaticSvcLabels"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspInterArea"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspIsFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLoggerEventBundling"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcutRelOffset"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV12v0Group.setStatus("obsolete")

tmnxMplsBypassOptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 65)
)
tmnxMplsBypassOptGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralBypassResigTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenBypassNextResignal"))
)
if mibBuilder.loadTexts:
    tmnxMplsBypassOptGroup.setStatus("current")

tmnxMplsGenV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 66)
)
tmnxMplsGenV12v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNewLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralResignalTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralHoldTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicBypass"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNextResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperDownReason"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralSrlgFrr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralSrlgFrrStrict"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenMbbPrefCurrentHops"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenP2pActPathFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenP2mpS2lFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenLspInitRetryTimeout"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenIssuMplsLockdown"))
)
if mibBuilder.loadTexts:
    tmnxMplsGenV12v0Group.setStatus("current")

tmnxMplsLSPPathV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 67)
)
tmnxMplsLSPPathV12v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTableSpinlock"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProperties"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathPreference"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLspId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryTimeRemaining"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelARHopListIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNextOptimize"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelCRHopListIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryAttempts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTransitionCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCspfQueries"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastResigAttempt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBEnd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBTypeInProg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBStarted"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBNextRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBRetryAttempts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailNodeArType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperInterArea"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathChanges"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperAdminGrpIncl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperAdminGrExcld"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperLeastFill"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRsvpAdspec"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperPropAdminGrp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperFRHopLimit"))
)
if mibBuilder.loadTexts:
    tmnxMplsLSPPathV12v0Group.setStatus("obsolete")

tmnxMplsLSPV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 68)
)
tmnxMplsLSPV12v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFromAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspToAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOutSegIndx"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpResvStyle"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpAdspec"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRMethod"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOctets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPackets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAge"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPrimaryTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTransitions"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastTransition"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastPathChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspConfiguredPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStandbyPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperationalPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHoldTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcutLfaType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPropAdminGroup"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcutRelOffset"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRevertTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRevertTimeRemain"))
)
if mibBuilder.loadTexts:
    tmnxMplsLSPV12v0Group.setStatus("obsolete")

tmnxMplsLoadBalanceWtV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 70)
)
tmnxMplsLoadBalanceWtV13v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspLoadBalancingWeight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempLoadBalancingWt"))
)
if mibBuilder.loadTexts:
    tmnxMplsLoadBalanceWtV13v0Group.setStatus("current")

tmnxMplsLabelSegRouteV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 71)
)
tmnxMplsLabelSegRouteV13v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLabelSegRouteStartLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelSegRouteEndLabel"))
)
if mibBuilder.loadTexts:
    tmnxMplsLabelSegRouteV13v0Group.setStatus("current")

tmnxMplsLabelStaticRgeV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 72)
)
tmnxMplsLabelStaticRgeV13v0Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLabelStaticLabelRange")
)
if mibBuilder.loadTexts:
    tmnxMplsLabelStaticRgeV13v0Group.setStatus("current")

tmnxMpls13v0ObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 73)
)
tmnxMpls13v0ObsoleteGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLabelMaxStaticLspLabels"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelMaxStaticSvcLabels"))
)
if mibBuilder.loadTexts:
    tmnxMpls13v0ObsoleteGroup.setStatus("current")

tmnxMplsGlobalV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 74)
)
tmnxMplsGlobalV13v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopUnnumIfID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIsABR"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopUnnumIfID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplatePropAdmGrp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspInterArea"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspIsFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLoggerEventBundling"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcutRelOffset"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV13v0Group.setStatus("current")

tmnxMplsClassBasedFwdV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 75)
)
tmnxMplsClassBasedFwdV13v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspClassFwdingEnabled"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFC"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempClassFwdEnabled"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempFC"))
)
if mibBuilder.loadTexts:
    tmnxMplsClassBasedFwdV13v0Group.setStatus("obsolete")

tmnxMplsBfdOnLspV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 76)
)
tmnxMplsBfdOnLspV13v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspBfdTemplateName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspBfdEnable"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspBfdPingIntvl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBfdTemplateName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBfdEnable"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBfdPingIntvl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempBfdTemplateName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempBfdEnable"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempBfdPingIntvl"))
)
if mibBuilder.loadTexts:
    tmnxMplsBfdOnLspV13v0Group.setStatus("current")

tmnxMplsAdminGroupObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 77)
)
tmnxMplsAdminGroupObsoleteGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsAdminGroupRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsAdminGroupValue"))
)
if mibBuilder.loadTexts:
    tmnxMplsAdminGroupObsoleteGroup.setStatus("current")

tmnxMplsIfSrlgV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 78)
)
tmnxMplsIfSrlgV14v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsIfSrlgGrpTblLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfSrlgGrpRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfSrlgGrpLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxMplsIfSrlgV14v0Group.setStatus("current")

tmnxMplsSrlgObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 79)
)
tmnxMplsSrlgObsoleteGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpTableLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpValue"))
)
if mibBuilder.loadTexts:
    tmnxMplsSrlgObsoleteGroup.setStatus("current")

tmnxMplsSegRouting14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 80)
)
tmnxMplsSegRouting14v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNewLspSRIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralSrTeLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralPceReport"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtPceCompute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtPceControl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtPceReport"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtTtmTunnelId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtMaxSrLabels"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtTunnelId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProfTblLstChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProfRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProfLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProfGroupId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastUpdateTime"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastUpdateId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastUpdateState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastUpdFailCode"))
)
if mibBuilder.loadTexts:
    tmnxMplsSegRouting14v0Group.setStatus("obsolete")

tmnxMplsEntropyLabel14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 81)
)
tmnxMplsEntropyLabel14v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralEntropyLblRsvpTe"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtEntropyLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtOperEntropyLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtNegEntropyLbl"))
)
if mibBuilder.loadTexts:
    tmnxMplsEntropyLabel14v0Group.setStatus("current")

tmnxMplsLspTemplEL14v4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 82)
)
tmnxMplsLspTemplEL14v4Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempEntropyLabel")
)
if mibBuilder.loadTexts:
    tmnxMplsLspTemplEL14v4Group.setStatus("current")

tmnxMplsSRLfaOvrhd14v4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 83)
)
tmnxMplsSRLfaOvrhd14v4Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtFrrOverheadLabel")
)
if mibBuilder.loadTexts:
    tmnxMplsSRLfaOvrhd14v4Group.setStatus("current")

tmnxMplsLspTempPceReportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 84)
)
tmnxMplsLspTempPceReportGroup.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplatePceReport")
)
if mibBuilder.loadTexts:
    tmnxMplsLspTempPceReportGroup.setStatus("current")

tmnxMplsLspTempSrLbl15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 85)
)
tmnxMplsLspTempSrLbl15v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspTempMaxSrLabels"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempFrrOverheadLabel"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspTempSrLbl15v0Group.setStatus("current")

tmnxMplsBfdFailureActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 86)
)
tmnxMplsBfdFailureActionGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspExtBfdFailureAction"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempBfdFailureAction"))
)
if mibBuilder.loadTexts:
    tmnxMplsBfdFailureActionGroup.setStatus("current")

tmnxMplsClassFwdPlcy15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 87)
)
tmnxMplsClassFwdPlcy15v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyTblLstChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyDefSetId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyRefCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyFCTblLstChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyFCSetId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtCbfFwdingPlcy"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtCbfFwdingSet"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempCbfFwdingPlcy"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempCbfFwdingSet"))
)
if mibBuilder.loadTexts:
    tmnxMplsClassFwdPlcy15v0Group.setStatus("current")

tmnxMplsP2PSrTe15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 88)
)
tmnxMplsP2PSrTe15v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGenMeshP2PSrTeLspOrig"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenOneHopP2PSrTeLspOrig"))
)
if mibBuilder.loadTexts:
    tmnxMplsP2PSrTe15v0Group.setStatus("current")

tmnxMplsLspStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 89)
)
tmnxMplsLspStatsGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspAggregatePkts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAggregateOctets"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspStatsGroup.setStatus("current")

tmnxMplsTunnelARHopSIDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 90)
)
tmnxMplsTunnelARHopSIDGroup.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopSIDType")
)
if mibBuilder.loadTexts:
    tmnxMplsTunnelARHopSIDGroup.setStatus("current")

tmnxMplsLSPV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 91)
)
tmnxMplsLSPV15v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFromAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspToAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOutSegIndx"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpResvStyle"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpAdspec"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRMethod"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAge"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPrimaryTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTransitions"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastTransition"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastPathChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspConfiguredPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStandbyPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperationalPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHoldTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcutLfaType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPropAdminGroup"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcutRelOffset"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRevertTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRevertTimeRemain"))
)
if mibBuilder.loadTexts:
    tmnxMplsLSPV15v0Group.setStatus("obsolete")

tmnxMplsLSPV15v0ObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 92)
)
tmnxMplsLSPV15v0ObsoleteGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspOctets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPackets"))
)
if mibBuilder.loadTexts:
    tmnxMplsLSPV15v0ObsoleteGroup.setStatus("current")

tmnxMplsEntropyLabelSrteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 93)
)
tmnxMplsEntropyLabelSrteGroup.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralEntropyLblSrTe")
)
if mibBuilder.loadTexts:
    tmnxMplsEntropyLabelSrteGroup.setStatus("current")

tmnxMplsReservedLblBlkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 94)
)
tmnxMplsReservedLblBlkGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsReservedLblBlkTblLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsReservedLblBlkRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsReservedLblBlkLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsReservedLblBlkStartLbl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsReservedLblBlkEndLbl"))
)
if mibBuilder.loadTexts:
    tmnxMplsReservedLblBlkGroup.setStatus("current")

tmnxMplsIfAltStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 95)
)
tmnxMplsIfAltStatsGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsIfAltTxPktCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfAltRxPktCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfAltTxOctetCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfAltRxOctetCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralAuxStats"))
)
if mibBuilder.loadTexts:
    tmnxMplsIfAltStatsGroup.setStatus("current")

vRtrMplsLspAdminTagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 96)
)
vRtrMplsLspAdminTagGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminTagTblLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminTagRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminTagLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAdminTagTblLstChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAdminTagRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAdminTagLastChg"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspAdminTagGroup.setStatus("current")

vRtrMplsFwdPlcyV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 97)
)
vRtrMplsFwdPlcyV16v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyTblLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyBindingLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyEndpointAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyEndpointAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyRevertTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyPreference"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNHGrpTblLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNHGrpRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNHGrpLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNHGrpAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNHGrpOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNHGrpResType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNHGrpLoadBalWt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNhgNHTblLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNhgNHRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNhgNHLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNhgNHOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNhgNHAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNhgNHAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyGenTblLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyGenRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyGenLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyGenAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyGenOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyGenOperDownReason"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyGenReservedLblBlk"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyStatsTblLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyStatsRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyStatsLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyStatsAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathLastOperChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblOperDownReason"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNumNHGrpCnt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathRetryCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathRetryTimeRem"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathRevertTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathIngStatsEnabl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathPref"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBLPathIngStatOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNhgOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNHgResType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNhgLoadBalWt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNhgFailovrCnt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNhgRevertCnt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNhgRevTimeRem"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNhgNHAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNhgNHAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNhgNHResolved"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNhgNHOutIf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNhgDownReason"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNhgNHDownCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblIngrAggPkts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblIngrAggOctets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathLastOperChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathOperDownReason"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNHGrpCnt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathRetryCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathRetryTimeRem"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathRevertTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathPref"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathTTMPref"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgResType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgLoadBalWt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgFailovrCnt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgRevertCnt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgRevTimeRem"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgDownReason"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgNHAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgNHAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgNHResolved"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgNHOutIf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgNHDownCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNHgNHPLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgNHPLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNhgWeights"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgWeights"))
)
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyV16v0Group.setStatus("current")

vRtrMplsFwdPlcyNhgNHPushLblGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 98)
)
vRtrMplsFwdPlcyNhgNHPushLblGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNhgNHPushLabel1"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNhgNHPushLabel2"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNhgNHPushLabel3"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNhgNHPushLabel4"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNhgNHPushLabel5"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNhgNHPushLabel6"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNhgNHPushLabel7"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNhgNHPushLabel8"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNhgNHPushLabel9"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNhgNHPushLabel10"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyTtmPreference"))
)
if mibBuilder.loadTexts:
    vRtrMplsFwdPlcyNhgNHPushLblGroup.setStatus("current")

vRtrMplsPceInitSrteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 99)
)
vRtrMplsPceInitSrteGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsPceInitGenTblLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsPceInitGenRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsPceInitGenSrte"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsPceInitGenSrteAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsPceInitGenSrteOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenPceInitP2PSrTeLspOrig"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsPceInitGenSrteOperDnRsn"))
)
if mibBuilder.loadTexts:
    vRtrMplsPceInitSrteGroup.setStatus("current")

vRtrMplsAutoBwUseLastAdjBWGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 100)
)
vRtrMplsAutoBwUseLastAdjBWGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWUseLastAdjBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWSecRetryLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWLastAdjBW"))
)
if mibBuilder.loadTexts:
    vRtrMplsAutoBwUseLastAdjBWGroup.setStatus("current")

tmnxMplsGeneralSrTeLspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 101)
)
tmnxMplsGeneralSrTeLspGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGenSrTeResignalTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtPathCompMeth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtMetricType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtLocalSrProt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtLabelStackRed"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempPathCompMeth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempMetricType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempLocalSrProt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempLabelStackRed"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperCompMeth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperMetricType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperLocalSrProt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperLabelStackRed"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenSrTeResigOnIgpEvent"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenSrteNextResignal"))
)
if mibBuilder.loadTexts:
    tmnxMplsGeneralSrTeLspGroup.setStatus("current")

tmnxMplsFwdPlcyEgressStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 102)
)
tmnxMplsFwdPlcyEgressStatsGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathNhgNHEgrOper"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblEgrStatsAggPkts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblEgrStatsAggOctets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBindLblPathEgrStatsEnabl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsBLPathEgrStatOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathNhgNHEgrOper"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptEgrStatsAggPkts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptEgrStatsAggOctets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathEgrStatsEnabl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsEndptPathEgrStatsOper"))
)
if mibBuilder.loadTexts:
    tmnxMplsFwdPlcyEgressStatsGroup.setStatus("current")

tmnxMplsSrteSBfdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 103)
)
tmnxMplsSrteSBfdGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspExtBfdUpWaitTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBfdUpWaitTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBfdUpWaitTmLeft"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBfdState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBfdStartFailRsn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempBfdUpWaitTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBfdOperUpWaitTmr"))
)
if mibBuilder.loadTexts:
    tmnxMplsSrteSBfdGroup.setStatus("current")

tmnxMplsGenMaxBypassPlrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 104)
)
tmnxMplsGenMaxBypassPlrGroup.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsGenMaxBypassPlrAssoc")
)
if mibBuilder.loadTexts:
    tmnxMplsGenMaxBypassPlrGroup.setStatus("current")

tmnxMplsLspPathEgressStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 105)
)
tmnxMplsLspPathEgressStatsGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathEgrStatsOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspEgressStatsAggrPkts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspEgressStatsAggrOctets"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspPathEgressStatsGroup.setStatus("current")

tmnxMplsLspSelfPingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 106)
)
tmnxMplsLspSelfPingGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGenLspSelfPingInterval"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenLspSelfPingTimeout"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenLspSelfPingRsvpTe"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempSelfPing"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtSelfPing"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspSelfPingGroup.setStatus("current")

tmnxMplsLspSrTeIpv6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 107)
)
tmnxMplsLspSrTeIpv6Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralV6OperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralV6OperDownReason"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfV6OperState"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspSrTeIpv6Group.setStatus("current")

tmnxMplsPathHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 108)
)
tmnxMplsPathHopGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsPathHopTableLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsPathHopRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsPathHopLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsPathHopAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsPathHopAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsPathHopStrictOrLoose"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsPathHopSidLabel"))
)
if mibBuilder.loadTexts:
    tmnxMplsPathHopGroup.setStatus("current")

tmnxMplsLspNgAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 109)
)
tmnxMplsLspNgAddrGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspNgFromAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspNgToAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopNgRouterId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNgFNAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNgFNAddr"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspNgAddrGroup.setStatus("current")

tmnxMplsLspSelfPingOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 110)
)
tmnxMplsLspSelfPingOperGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGenLspSelfPingTimeouts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSelfPingTimeouts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSelfPingOprState"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspSelfPingOperGroup.setStatus("current")

tmnxMplsNotifyObjsLspResource = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 112)
)
tmnxMplsNotifyObjsLspResource.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsResourceType")
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyObjsLspResource.setStatus("current")

tmnxMplsV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 114)
)
tmnxMplsV20v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopProtection"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOutSegIndx"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpResvStyle"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpAdspec"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRMethod"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAge"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPrimaryTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTransitions"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastTransition"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastPathChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspConfiguredPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStandbyPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperationalPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHoldTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcutLfaType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPropAdminGroup"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcutRelOffset"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRevertTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRevertTimeRemain"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateTblLastChgd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateDefaultPath"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateAdmGrpIncl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateAdmGrpExcl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateFRMethod"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateFRHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateRetryLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateRetryTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateCspfTeMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOriginTemplate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateLspCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateMvpnRefCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNewLspSRIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralSrTeLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralPceReport"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtPceControl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtPceReport"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtTtmTunnelId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtMaxSrLabels"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtTunnelId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProfTblLstChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProfRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProfLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProfGroupId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastUpdateTime"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastUpdateId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastUpdateState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastUpdFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTableSpinlock"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProperties"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathPreference"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLspId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryTimeRemaining"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelARHopListIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNextOptimize"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelCRHopListIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryAttempts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTransitionCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCspfQueries"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastResigAttempt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBEnd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBTypeInProg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBStarted"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBNextRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBRetryAttempts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailNodeArType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperInterArea"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathChanges"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperAdminGrpIncl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperAdminGrExcld"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperLeastFill"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRsvpAdspec"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperPropAdminGrp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperFRHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspClassFwdingEnabled"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempClassFwdEnabled"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBFailCode"))
)
if mibBuilder.loadTexts:
    tmnxMplsV20v0Group.setStatus("current")

tmnxMplsObsoletedV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 115)
)
tmnxMplsObsoletedV20v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopRouterId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFromAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspToAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspCspfTeMetricEnabled"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateCspfTeMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtPceCompute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperCspf"))
)
if mibBuilder.loadTexts:
    tmnxMplsObsoletedV20v0Group.setStatus("current")

tmnxMplsLspSelfPingV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 116)
)
tmnxMplsLspSelfPingV20v0Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspSelfPingTimeoutAction")
)
if mibBuilder.loadTexts:
    tmnxMplsLspSelfPingV20v0Group.setStatus("current")

tmnxMplsClassFwdObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 117)
)
tmnxMplsClassFwdObsoleteGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspFC"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempFC"))
)
if mibBuilder.loadTexts:
    tmnxMplsClassFwdObsoleteGroup.setStatus("current")

tmnxMplsSrTeIpv6LspTempGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 118)
)
tmnxMplsSrTeIpv6LspTempGroup.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAddrFamily")
)
if mibBuilder.loadTexts:
    tmnxMplsSrTeIpv6LspTempGroup.setStatus("current")

tmnxMplsTunnelARHopIdTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 119)
)
tmnxMplsTunnelARHopIdTypeGroup.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopNgRtrIdType")
)
if mibBuilder.loadTexts:
    tmnxMplsTunnelARHopIdTypeGroup.setStatus("current")

tmnxMplsLspPcepToLocalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 120)
)
tmnxMplsLspPcepToLocalGroup.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtFallbkPathComp")
)
if mibBuilder.loadTexts:
    tmnxMplsLspPcepToLocalGroup.setStatus("current")

tmnxMplsGenV20Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 121)
)
tmnxMplsGenV20Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsGenResignalOnIgpOverload")
)
if mibBuilder.loadTexts:
    tmnxMplsGenV20Group.setStatus("current")

tmnxMplsGenLspSelfPingV20Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 122)
)
tmnxMplsGenLspSelfPingV20Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspSelfPingOamNoRsc"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenLspSelfPingOamNoRsc"))
)
if mibBuilder.loadTexts:
    tmnxMplsGenLspSelfPingV20Group.setStatus("current")

tmnxMplsGenSrTeLspCountV21Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 123)
)
tmnxMplsGenSrTeLspCountV21Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGenDynP2pLspUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenSrTeIpv4LspUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenSrTeIpv6LspUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenMeshSrTeIpv4LspUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenMeshSrTeIpv6LspUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenOneHopSrTeIpv4LspUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenOneHopSrTeIpv6LspUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenPceInitSrTeIpv4LspUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenPceInitSrTeIpv6LspUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenOnDemandSrTeLspOrig"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenOnDemandSrTeIpv4LspUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenOnDemandSrTeIpv6LspUp"))
)
if mibBuilder.loadTexts:
    tmnxMplsGenSrTeLspCountV21Group.setStatus("current")

tmnxMplsLspV21Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 124)
)
tmnxMplsLspV21Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtTriggerManualSw")
)
if mibBuilder.loadTexts:
    tmnxMplsLspV21Group.setStatus("current")

tmnxMplsGenTTMV21Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 125)
)
tmnxMplsGenTTMV21Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGenTunnelTablePrefRsvpTe"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenTunnelTablePrefSrTe"))
)
if mibBuilder.loadTexts:
    tmnxMplsGenTTMV21Group.setStatus("current")

tmnxMplsLspPathDegradeV21Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 126)
)
tmnxMplsLspPathDegradeV21Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathDegraded"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathDegradedReason"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtActivePathIndex"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspPathDegradeV21Group.setStatus("current")

tmnxMplsNotifyObjsLspPathFailure = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 127)
)
tmnxMplsNotifyObjsLspPathFailure.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspManualSwFailReason"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathManDegState"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyObjsLspPathFailure.setStatus("current")

tmnxMplsPccPceOperStateV21Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 129)
)
tmnxMplsPccPceOperStateV21Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGenRsvpPccOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenRsvpPceOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenSrTePccOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenSrTePceOperState"))
)
if mibBuilder.loadTexts:
    tmnxMplsPccPceOperStateV21Group.setStatus("current")

tmnxMplsLspTempExtV21Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 130)
)
tmnxMplsLspTempExtV21Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspTempExtFallbkPathComp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempExtPceControl"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspTempExtV21Group.setStatus("current")

tmnxMplsLspStatsModeV21Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 131)
)
tmnxMplsLspStatsModeV21Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsMode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateEgrStatsMode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatsMode"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspStatsModeV21Group.setStatus("current")

tmnxMplsLspOvrTunnelElcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 133)
)
tmnxMplsLspOvrTunnelElcGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspExtOverrideTunElc"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempExtOverrideTunElc"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspOvrTunnelElcGroup.setStatus("current")

tmnxMplsLspTransportFrrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 134)
)
tmnxMplsLspTransportFrrGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspTempExtPrefTransFrr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtPrefTransFrr"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspTransportFrrGroup.setStatus("current")

tmnxMplsLspTempPathProfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 135)
)
tmnxMplsLspTempPathProfGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspTempPathProTblLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempPathProfRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempPathProfLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempPathProfGroupId"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspTempPathProfGroup.setStatus("current")

tmnxMplsLspExtBfdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 136)
)
tmnxMplsLspExtBfdGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspExtBfdReturnPathLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathReturnPathLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempExtReturnPathLbl"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspExtBfdGroup.setStatus("current")

tmnxMplsLspRateCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 137)
)
tmnxMplsLspRateCountersGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsAggregateOnly"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsRateEnabled"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsRatePkts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsRateMbps"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspRateCountersGroup.setStatus("current")

tmnxP2mpMplsLspSoftPreemptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 138)
)
tmnxP2mpMplsLspSoftPreemptGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspExtSoftPreemption"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempExtSoftPreemption"))
)
if mibBuilder.loadTexts:
    tmnxP2mpMplsLspSoftPreemptGroup.setStatus("current")


# Notification objects

vRtrMplsStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 1)
)
vRtrMplsStateChange.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsStateChange.setStatus(
        "current"
    )

vRtrMplsIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 2)
)
vRtrMplsIfStateChange.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsIfStateChange.setStatus(
        "current"
    )

vRtrMplsLspUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 3)
)
vRtrMplsLspUp.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspUp.setStatus(
        "current"
    )

vRtrMplsLspDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 4)
)
vRtrMplsLspDown.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspNotificationReasonCode"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspDown.setStatus(
        "current"
    )

vRtrMplsLspPathUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 5)
)
vRtrMplsLspPathUp.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("MPLS-TE-MIB", "mplsTunnelIndex"),
        ("MPLS-TE-MIB", "mplsTunnelInstance"),
        ("MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathUp.setStatus(
        "current"
    )

vRtrMplsLspPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 6)
)
vRtrMplsLspPathDown.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("MPLS-TE-MIB", "mplsTunnelIndex"),
        ("MPLS-TE-MIB", "mplsTunnelInstance"),
        ("MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNotificationReasonCode"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathDown.setStatus(
        "current"
    )

vRtrMplsLspPathRerouted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 7)
)
vRtrMplsLspPathRerouted.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathRerouted.setStatus(
        "current"
    )

vRtrMplsLspPathResignaled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 8)
)
vRtrMplsLspPathResignaled.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBType"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathResignaled.setStatus(
        "current"
    )

vRtrMplsP2mpInstanceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 9)
)
vRtrMplsP2mpInstanceUp.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNotifIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstanceUp.setStatus(
        "current"
    )

vRtrMplsP2mpInstanceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 10)
)
vRtrMplsP2mpInstanceDown.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNotifIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNotifReasonCode"))
)
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstanceDown.setStatus(
        "current"
    )

vRtrMplsS2lSubLspUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 11)
)
vRtrMplsS2lSubLspUp.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNotifIndex"),
        ("MPLS-TE-MIB", "mplsTunnelIndex"),
        ("MPLS-TE-MIB", "mplsTunnelInstance"),
        ("MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspNtDstAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspNtDstAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspUp.setStatus(
        "current"
    )

vRtrMplsS2lSubLspDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 12)
)
vRtrMplsS2lSubLspDown.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNotifIndex"),
        ("MPLS-TE-MIB", "mplsTunnelIndex"),
        ("MPLS-TE-MIB", "mplsTunnelInstance"),
        ("MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspNtDstAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspNtDstAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNotifReasonCode"))
)
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspDown.setStatus(
        "current"
    )

vRtrMplsS2lSubLspRerouted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 13)
)
vRtrMplsS2lSubLspRerouted.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspRerouted.setStatus(
        "current"
    )

vRtrMplsS2lSubLspResignaled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 14)
)
vRtrMplsS2lSubLspResignaled.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspLastMBBType"))
)
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspResignaled.setStatus(
        "current"
    )

vRtrMplsLspPathSoftPreempted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 15)
)
vRtrMplsLspPathSoftPreempted.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathSoftPreempted.setStatus(
        "current"
    )

vRtrMplsLspPathLstFillReoptElig = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 16)
)
vRtrMplsLspPathLstFillReoptElig.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathResignalEligible"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCongChgPercent"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathLstFillReoptElig.setStatus(
        "current"
    )

vRtrMplsP2mpInstanceResignaled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 17)
)
vRtrMplsP2mpInstanceResignaled.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNotifIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstLastMBBType"))
)
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstanceResignaled.setStatus(
        "current"
    )

vRtrMplsResignalTimerExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 18)
)
vRtrMplsResignalTimerExpired.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralResignalTimer")
)
if mibBuilder.loadTexts:
    vRtrMplsResignalTimerExpired.setStatus(
        "current"
    )

vRtrMplsLspPathMbbStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 19)
)
vRtrMplsLspPathMbbStatusEvent.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMbbStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMbbReasonCode"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathMbbStatusEvent.setStatus(
        "current"
    )

vRtrMplsLspSwitchStbyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 20)
)
vRtrMplsLspSwitchStbyFailure.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSwitchStbyPathForce"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSwitchStbyPathIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSwitchStbyReasonCode"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspSwitchStbyFailure.setStatus(
        "current"
    )

vRtrMplsLspActivePathChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 21)
)
vRtrMplsLspActivePathChanged.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathActiveByManual"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOldTunnelIndex"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspActivePathChanged.setStatus(
        "current"
    )

vRtrMplsXCBundleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 22)
)
vRtrMplsXCBundleChange.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifRednIndicesBitMap"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifyRednBundlingType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifyRednNumOfBitsSet"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifyRednStartIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifyRednEndIndex"))
)
if mibBuilder.loadTexts:
    vRtrMplsXCBundleChange.setStatus(
        "current"
    )

vRtrMplsLblRangeModify = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 23)
)
vRtrMplsLblRangeModify.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLabelMaxStaticLspLabels"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelMaxStaticSvcLabels"))
)
if mibBuilder.loadTexts:
    vRtrMplsLblRangeModify.setStatus(
        "obsolete"
    )

vRtrMplsNodeInIgpOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 24)
)
vRtrMplsNodeInIgpOverload.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGenRetryOnIgpOverload"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIgpOverloadRtrAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIgpOverloadRtrAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIgpOverloadIgpType"))
)
if mibBuilder.loadTexts:
    vRtrMplsNodeInIgpOverload.setStatus(
        "current"
    )

vRtrMplsIPv6StateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 25)
)
vRtrMplsIPv6StateChange.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralV6OperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsIPv6StateChange.setStatus(
        "current"
    )

vRtrMplsIfIPv6StateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 26)
)
vRtrMplsIfIPv6StateChange.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfV6OperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsIfIPv6StateChange.setStatus(
        "current"
    )

vRtrMplsLspResourceExhaustion = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 27)
)
vRtrMplsLspResourceExhaustion.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsResourceType"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspResourceExhaustion.setStatus(
        "current"
    )

vRtrMplsLspManualSwitchFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 28)
)
vRtrMplsLspManualSwitchFailure.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtTriggerManualSw"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspManualSwFailReason"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspManualSwitchFailure.setStatus(
        "current"
    )

vRtrMplsLspPathManualDegStateChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 29)
)
vRtrMplsLspPathManualDegStateChg.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathManDegState"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathManualDegStateChg.setStatus(
        "current"
    )

vRtrMplsS2lSubLspPreempted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 30)
)
vRtrMplsS2lSubLspPreempted.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspPreempted.setStatus(
        "current"
    )


# Notifications groups

tmnxMplsNotificationR2r1Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 14)
)
tmnxMplsNotificationR2r1Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsStateChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfStateChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRerouted"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathResignaled"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotificationR2r1Group.setStatus(
        "current"
    )

tmnxMplsNotificationV7v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 30)
)
tmnxMplsNotificationV7v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstanceUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstanceDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspRerouted"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspResignaled"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSoftPreempted"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLstFillReoptElig"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstanceResignaled"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsResignalTimerExpired"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotificationV7v0Group.setStatus(
        "current"
    )

tmnxMplsNotificationV8v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 37)
)
tmnxMplsNotificationV8v0Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMbbStatusEvent")
)
if mibBuilder.loadTexts:
    tmnxMplsNotificationV8v0Group.setStatus(
        "current"
    )

tmnxMplsNotifV9v0R4Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 45)
)
tmnxMplsNotifV9v0R4Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspSwitchStbyFailure"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspActivePathChanged"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotifV9v0R4Group.setStatus(
        "current"
    )

tmnxMplsNotifyV10v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 50)
)
tmnxMplsNotifyV10v0Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsXCBundleChange")
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyV10v0Group.setStatus(
        "current"
    )

tmnxMplsNotifyV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 55)
)
tmnxMplsNotifyV11v0Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLblRangeModify")
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyV11v0Group.setStatus(
        "obsolete"
    )

tmnxMplsIgpOverloadNotify = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 60)
)
tmnxMplsIgpOverloadNotify.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsNodeInIgpOverload")
)
if mibBuilder.loadTexts:
    tmnxMplsIgpOverloadNotify.setStatus(
        "current"
    )

tmnxMplsObsoleteNotifyV12Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 69)
)
tmnxMplsObsoleteNotifyV12Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLblRangeModify")
)
if mibBuilder.loadTexts:
    tmnxMplsObsoleteNotifyV12Group.setStatus(
        "current"
    )

tmnxMplsNotificationIPv6Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 111)
)
tmnxMplsNotificationIPv6Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsIPv6StateChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfIPv6StateChange"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotificationIPv6Group.setStatus(
        "current"
    )

tmnxMplsNotifyV20v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 113)
)
tmnxMplsNotifyV20v0Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspResourceExhaustion")
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyV20v0Group.setStatus(
        "current"
    )

tmnxMplsNotifyLspPathV21v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 128)
)
tmnxMplsNotifyLspPathV21v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspManualSwitchFailure"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathManualDegStateChg"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyLspPathV21v0Group.setStatus(
        "current"
    )

tmnxMplsNotifyV22v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 139)
)
tmnxMplsNotifyV22v0Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspPreempted")
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyV22v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxMplsV3v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 3)
)
tmnxMplsV3v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsGlobalR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"))
)
if mibBuilder.loadTexts:
    tmnxMplsV3v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 4)
)
tmnxMplsV5v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV5v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV5v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"))
)
if mibBuilder.loadTexts:
    tmnxMplsV5v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 5)
)
tmnxMplsV6v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV5v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV6v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 6)
)
tmnxMplsV6v1Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV5v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV6v1Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 7)
)
tmnxMplsV7v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV5v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 8)
)
tmnxMplsV8v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV5v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 9)
)
tmnxMplsV9v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV5v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV9v0R4Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 10)
)
tmnxMplsV10v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV5v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 11)
)
tmnxMplsV11v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTpGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsFRAdminGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV11v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyV11v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWFcWtGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV11v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsIgpOverload"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIgpOverloadNotify"))
)
if mibBuilder.loadTexts:
    tmnxMplsV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 12)
)
tmnxMplsV12v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTpGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsFRAdminGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWFcWtGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV11v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsIgpOverload"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIgpOverloadNotify"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTempInStatsGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAutoBwUnderflowGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBgpLabelRetentionGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBypassOptGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLSPPathV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGenV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLSPV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV12v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 13)
)
tmnxMplsV13v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTpGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsFRAdminGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWFcWtGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV11v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsIgpOverload"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIgpOverloadNotify"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTempInStatsGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAutoBwUnderflowGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBgpLabelRetentionGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBypassOptGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLSPPathV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGenV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLSPV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLoadBalanceWtV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelSegRouteV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelStaticRgeV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsClassBasedFwdV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBfdOnLspV13v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV13v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 14)
)
tmnxMplsV14v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTpGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsFRAdminGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWFcWtGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV11v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsIgpOverload"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIgpOverloadNotify"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTempInStatsGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAutoBwUnderflowGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBgpLabelRetentionGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBypassOptGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLSPPathV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGenV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLSPV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLoadBalanceWtV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelSegRouteV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelStaticRgeV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsClassBasedFwdV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfSrlgV14v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBfdOnLspV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSegRouting14v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsEntropyLabel14v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplEL14v4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSRLfaOvrhd14v4Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV14v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 15)
)
tmnxMplsV15v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTpGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsFRAdminGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWFcWtGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV11v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsIgpOverload"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIgpOverloadNotify"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTempInStatsGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAutoBwUnderflowGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBgpLabelRetentionGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBypassOptGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLSPPathV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGenV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLoadBalanceWtV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelSegRouteV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelStaticRgeV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsClassBasedFwdV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfSrlgV14v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBfdOnLspV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSegRouting14v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsEntropyLabel14v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplEL14v4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSRLfaOvrhd14v4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTempPceReportGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTempSrLbl15v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBfdFailureActionGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsClassFwdPlcy15v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2PSrTe15v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopSIDGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLSPV15v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsEntropyLabelSrteGroup"))
)
if mibBuilder.loadTexts:
    tmnxMplsV15v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 16)
)
tmnxMplsV16v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsReservedLblBlkGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfAltStatsGroup"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminTagGroup"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyV16v0Group"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFwdPlcyNhgNHPushLblGroup"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsPceInitSrteGroup"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsAutoBwUseLastAdjBWGroup"))
)
if mibBuilder.loadTexts:
    tmnxMplsV16v0Compliance.setStatus(
        "current"
    )

tmnxMplsV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 17)
)
tmnxMplsV19v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsGeneralSrTeLspGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsFwdPlcyEgressStatsGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrteSBfdGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGenMaxBypassPlrGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathEgressStatsGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspSelfPingGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspNgAddrGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspSrTeIpv6Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsPathHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspSelfPingOperGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationIPv6Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV19v0Compliance.setStatus(
        "current"
    )

tmnxMplsV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 18)
)
tmnxMplsV20v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTpGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsFRAdminGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWFcWtGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV11v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsIgpOverload"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIgpOverloadNotify"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTempInStatsGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAutoBwUnderflowGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBgpLabelRetentionGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBypassOptGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGenV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLoadBalanceWtV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelSegRouteV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelStaticRgeV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfSrlgV14v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBfdOnLspV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsEntropyLabel14v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplEL14v4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSRLfaOvrhd14v4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTempPceReportGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTempSrLbl15v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBfdFailureActionGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsClassFwdPlcy15v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2PSrTe15v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopSIDGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsEntropyLabelSrteGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsLspResource"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyV20v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsV20v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspSelfPingV20v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrTeIpv6LspTempGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopIdTypeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPcepToLocalGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGenV20Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGenLspSelfPingV20Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV20v0Compliance.setStatus(
        "current"
    )

tmnxMplsV21v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 19)
)
tmnxMplsV21v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTpGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsFRAdminGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWFcWtGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV11v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsIgpOverload"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIgpOverloadNotify"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTempInStatsGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAutoBwUnderflowGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBgpLabelRetentionGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBypassOptGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGenV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLoadBalanceWtV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelSegRouteV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelStaticRgeV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfSrlgV14v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBfdOnLspV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsEntropyLabel14v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplEL14v4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSRLfaOvrhd14v4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTempPceReportGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTempSrLbl15v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBfdFailureActionGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsClassFwdPlcy15v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2PSrTe15v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopSIDGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsEntropyLabelSrteGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsLspResource"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyV20v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsV20v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspSelfPingV20v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrTeIpv6LspTempGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopIdTypeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPcepToLocalGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGenV20Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGenLspSelfPingV20Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGenSrTeLspCountV21Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV21Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGenTTMV21Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathDegradeV21Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsLspPathFailure"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyLspPathV21v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsPccPceOperStateV21Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTempExtV21Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsModeV21Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspOvrTunnelElcGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTransportFrrGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTempPathProfGroup"))
)
if mibBuilder.loadTexts:
    tmnxMplsV21v0Compliance.setStatus(
        "current"
    )

tmnxMplsV22v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 20)
)
tmnxMplsV22v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsLspExtBfdGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspRateCountersGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxP2mpMplsLspSoftPreemptGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyV22v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV22v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-MPLS-MIB",
    **{"TmnxMplsLspFailCode": TmnxMplsLspFailCode,
       "TmnxMplsLabelOwner": TmnxMplsLabelOwner,
       "TmnxMplsOperDownReasonCode": TmnxMplsOperDownReasonCode,
       "TmnxMplsMBBType": TmnxMplsMBBType,
       "TmnxMplsP2mpInstFailCode": TmnxMplsP2mpInstFailCode,
       "TmnxMplsRouterId": TmnxMplsRouterId,
       "TmnxMplsLspAutoBWLastAdjCause": TmnxMplsLspAutoBWLastAdjCause,
       "TmnxMplsLspBgpRSVPLSPTunState": TmnxMplsLspBgpRSVPLSPTunState,
       "TmnxMplsLspAddrType": TmnxMplsLspAddrType,
       "timetraMplsMIBModule": timetraMplsMIBModule,
       "tmnxMplsConformance": tmnxMplsConformance,
       "tmnxMplsCompliances": tmnxMplsCompliances,
       "tmnxMplsV3v0Compliance": tmnxMplsV3v0Compliance,
       "tmnxMplsV5v0Compliance": tmnxMplsV5v0Compliance,
       "tmnxMplsV6v0Compliance": tmnxMplsV6v0Compliance,
       "tmnxMplsV6v1Compliance": tmnxMplsV6v1Compliance,
       "tmnxMplsV7v0Compliance": tmnxMplsV7v0Compliance,
       "tmnxMplsV8v0Compliance": tmnxMplsV8v0Compliance,
       "tmnxMplsV9v0Compliance": tmnxMplsV9v0Compliance,
       "tmnxMplsV10v0Compliance": tmnxMplsV10v0Compliance,
       "tmnxMplsV11v0Compliance": tmnxMplsV11v0Compliance,
       "tmnxMplsV12v0Compliance": tmnxMplsV12v0Compliance,
       "tmnxMplsV13v0Compliance": tmnxMplsV13v0Compliance,
       "tmnxMplsV14v0Compliance": tmnxMplsV14v0Compliance,
       "tmnxMplsV15v0Compliance": tmnxMplsV15v0Compliance,
       "tmnxMplsV16v0Compliance": tmnxMplsV16v0Compliance,
       "tmnxMplsV19v0Compliance": tmnxMplsV19v0Compliance,
       "tmnxMplsV20v0Compliance": tmnxMplsV20v0Compliance,
       "tmnxMplsV21v0Compliance": tmnxMplsV21v0Compliance,
       "tmnxMplsV22v0Compliance": tmnxMplsV22v0Compliance,
       "tmnxMplsGroups": tmnxMplsGroups,
       "tmnxMplsLspPathGroup": tmnxMplsLspPathGroup,
       "tmnxMplsXCGroup": tmnxMplsXCGroup,
       "tmnxMplsIfGroup": tmnxMplsIfGroup,
       "tmnxMplsTunnelARHopGroup": tmnxMplsTunnelARHopGroup,
       "tmnxMplsTunnelCHopGroup": tmnxMplsTunnelCHopGroup,
       "tmnxMplsAdminGroupGroup": tmnxMplsAdminGroupGroup,
       "tmnxMplsFSGroupGroup": tmnxMplsFSGroupGroup,
       "tmnxMplsNotifyObjsGroup": tmnxMplsNotifyObjsGroup,
       "tmnxMplsGlobalR2r1Group": tmnxMplsGlobalR2r1Group,
       "tmnxMplsLspR2r1Group": tmnxMplsLspR2r1Group,
       "tmnxMplsNotificationR2r1Group": tmnxMplsNotificationR2r1Group,
       "tmnxMplsLabelRangeGroup": tmnxMplsLabelRangeGroup,
       "tmnxMplsGlobalV5v0Group": tmnxMplsGlobalV5v0Group,
       "tmnxMplsLspV5v0Group": tmnxMplsLspV5v0Group,
       "tmnxMplsGlobalV6v0Group": tmnxMplsGlobalV6v0Group,
       "tmnxMplsSrlgV6v0Group": tmnxMplsSrlgV6v0Group,
       "tmnxMplsLspPathV6v0Group": tmnxMplsLspPathV6v0Group,
       "tmnxMplsIfV6v0Group": tmnxMplsIfV6v0Group,
       "tmnxMplsLspV6v0Group": tmnxMplsLspV6v0Group,
       "tmnxMplsLspPathV6v1Group": tmnxMplsLspPathV6v1Group,
       "tmnxMplsObsoleteGroup": tmnxMplsObsoleteGroup,
       "tmnxMplsLspV7v0Group": tmnxMplsLspV7v0Group,
       "tmnxMplsGlobalV7v0Group": tmnxMplsGlobalV7v0Group,
       "tmnxMplsP2mpInstanceGroup": tmnxMplsP2mpInstanceGroup,
       "tmnxMplsP2mpS2lGroup": tmnxMplsP2mpS2lGroup,
       "tmnxMplsNotifyObjsV7v0Group": tmnxMplsNotifyObjsV7v0Group,
       "tmnxMplsNotificationV7v0Group": tmnxMplsNotificationV7v0Group,
       "tmnxMplsLspPathV7v0Group": tmnxMplsLspPathV7v0Group,
       "tmnxMplsSrlgV7v0Group": tmnxMplsSrlgV7v0Group,
       "tmnxMplsLspStatsV7v0Group": tmnxMplsLspStatsV7v0Group,
       "tmnxMplsLspV8v0Group": tmnxMplsLspV8v0Group,
       "tmnxMplsLspPathV8v0Group": tmnxMplsLspPathV8v0Group,
       "tmnxMplsNotifyObjsV8v0Group": tmnxMplsNotifyObjsV8v0Group,
       "tmnxMplsNotificationV8v0Group": tmnxMplsNotificationV8v0Group,
       "tmnxMplsGlobalV8v0Group": tmnxMplsGlobalV8v0Group,
       "tmnxMplsLspTemplateV8v0Group": tmnxMplsLspTemplateV8v0Group,
       "tmnxMplsLspAutoBWV8v0Group": tmnxMplsLspAutoBWV8v0Group,
       "tmnxMplsGlobalV9v0Group": tmnxMplsGlobalV9v0Group,
       "tmnxMplsLspV9v0Group": tmnxMplsLspV9v0Group,
       "tmnxMplsLspV9v0R4Group": tmnxMplsLspV9v0R4Group,
       "tmnxMplsNotifyObjsV9v0R4Group": tmnxMplsNotifyObjsV9v0R4Group,
       "tmnxMplsNotifV9v0R4Group": tmnxMplsNotifV9v0R4Group,
       "tmnxMplsLspPathV9v0R4Group": tmnxMplsLspPathV9v0R4Group,
       "tmnxMplsGlobalV10v0Group": tmnxMplsGlobalV10v0Group,
       "tmnxMplsTpGroup": tmnxMplsTpGroup,
       "tmnxMplsNotifyObjsV10v0Group": tmnxMplsNotifyObjsV10v0Group,
       "tmnxMplsNotifyV10v0Group": tmnxMplsNotifyV10v0Group,
       "tmnxMplsFRAdminGroup": tmnxMplsFRAdminGroup,
       "tmnxMplsGlobalV11v0Group": tmnxMplsGlobalV11v0Group,
       "tmnxMplsV11v0ObsoleteGroup": tmnxMplsV11v0ObsoleteGroup,
       "tmnxMplsLspTemplateGroup": tmnxMplsLspTemplateGroup,
       "tmnxMplsNotifyV11v0Group": tmnxMplsNotifyV11v0Group,
       "tmnxMplsLspAutoBWFcWtGroup": tmnxMplsLspAutoBWFcWtGroup,
       "tmnxMplsGlobalV11v0R4Group": tmnxMplsGlobalV11v0R4Group,
       "tmnxMplsV12v0ObsoleteGroup": tmnxMplsV12v0ObsoleteGroup,
       "tmnxMplsNotifyObjsIgpOverload": tmnxMplsNotifyObjsIgpOverload,
       "tmnxMplsIgpOverloadNotify": tmnxMplsIgpOverloadNotify,
       "tmnxMplsLspTempInStatsGroup": tmnxMplsLspTempInStatsGroup,
       "tmnxMplsAutoBwUnderflowGroup": tmnxMplsAutoBwUnderflowGroup,
       "tmnxMplsBgpLabelRetentionGroup": tmnxMplsBgpLabelRetentionGroup,
       "tmnxMplsGlobalV12v0Group": tmnxMplsGlobalV12v0Group,
       "tmnxMplsBypassOptGroup": tmnxMplsBypassOptGroup,
       "tmnxMplsGenV12v0Group": tmnxMplsGenV12v0Group,
       "tmnxMplsLSPPathV12v0Group": tmnxMplsLSPPathV12v0Group,
       "tmnxMplsLSPV12v0Group": tmnxMplsLSPV12v0Group,
       "tmnxMplsObsoleteNotifyV12Group": tmnxMplsObsoleteNotifyV12Group,
       "tmnxMplsLoadBalanceWtV13v0Group": tmnxMplsLoadBalanceWtV13v0Group,
       "tmnxMplsLabelSegRouteV13v0Group": tmnxMplsLabelSegRouteV13v0Group,
       "tmnxMplsLabelStaticRgeV13v0Group": tmnxMplsLabelStaticRgeV13v0Group,
       "tmnxMpls13v0ObsoleteGroup": tmnxMpls13v0ObsoleteGroup,
       "tmnxMplsGlobalV13v0Group": tmnxMplsGlobalV13v0Group,
       "tmnxMplsClassBasedFwdV13v0Group": tmnxMplsClassBasedFwdV13v0Group,
       "tmnxMplsBfdOnLspV13v0Group": tmnxMplsBfdOnLspV13v0Group,
       "tmnxMplsAdminGroupObsoleteGroup": tmnxMplsAdminGroupObsoleteGroup,
       "tmnxMplsIfSrlgV14v0Group": tmnxMplsIfSrlgV14v0Group,
       "tmnxMplsSrlgObsoleteGroup": tmnxMplsSrlgObsoleteGroup,
       "tmnxMplsSegRouting14v0Group": tmnxMplsSegRouting14v0Group,
       "tmnxMplsEntropyLabel14v0Group": tmnxMplsEntropyLabel14v0Group,
       "tmnxMplsLspTemplEL14v4Group": tmnxMplsLspTemplEL14v4Group,
       "tmnxMplsSRLfaOvrhd14v4Group": tmnxMplsSRLfaOvrhd14v4Group,
       "tmnxMplsLspTempPceReportGroup": tmnxMplsLspTempPceReportGroup,
       "tmnxMplsLspTempSrLbl15v0Group": tmnxMplsLspTempSrLbl15v0Group,
       "tmnxMplsBfdFailureActionGroup": tmnxMplsBfdFailureActionGroup,
       "tmnxMplsClassFwdPlcy15v0Group": tmnxMplsClassFwdPlcy15v0Group,
       "tmnxMplsP2PSrTe15v0Group": tmnxMplsP2PSrTe15v0Group,
       "tmnxMplsLspStatsGroup": tmnxMplsLspStatsGroup,
       "tmnxMplsTunnelARHopSIDGroup": tmnxMplsTunnelARHopSIDGroup,
       "tmnxMplsLSPV15v0Group": tmnxMplsLSPV15v0Group,
       "tmnxMplsLSPV15v0ObsoleteGroup": tmnxMplsLSPV15v0ObsoleteGroup,
       "tmnxMplsEntropyLabelSrteGroup": tmnxMplsEntropyLabelSrteGroup,
       "tmnxMplsReservedLblBlkGroup": tmnxMplsReservedLblBlkGroup,
       "tmnxMplsIfAltStatsGroup": tmnxMplsIfAltStatsGroup,
       "vRtrMplsLspAdminTagGroup": vRtrMplsLspAdminTagGroup,
       "vRtrMplsFwdPlcyV16v0Group": vRtrMplsFwdPlcyV16v0Group,
       "vRtrMplsFwdPlcyNhgNHPushLblGroup": vRtrMplsFwdPlcyNhgNHPushLblGroup,
       "vRtrMplsPceInitSrteGroup": vRtrMplsPceInitSrteGroup,
       "vRtrMplsAutoBwUseLastAdjBWGroup": vRtrMplsAutoBwUseLastAdjBWGroup,
       "tmnxMplsGeneralSrTeLspGroup": tmnxMplsGeneralSrTeLspGroup,
       "tmnxMplsFwdPlcyEgressStatsGroup": tmnxMplsFwdPlcyEgressStatsGroup,
       "tmnxMplsSrteSBfdGroup": tmnxMplsSrteSBfdGroup,
       "tmnxMplsGenMaxBypassPlrGroup": tmnxMplsGenMaxBypassPlrGroup,
       "tmnxMplsLspPathEgressStatsGroup": tmnxMplsLspPathEgressStatsGroup,
       "tmnxMplsLspSelfPingGroup": tmnxMplsLspSelfPingGroup,
       "tmnxMplsLspSrTeIpv6Group": tmnxMplsLspSrTeIpv6Group,
       "tmnxMplsPathHopGroup": tmnxMplsPathHopGroup,
       "tmnxMplsLspNgAddrGroup": tmnxMplsLspNgAddrGroup,
       "tmnxMplsLspSelfPingOperGroup": tmnxMplsLspSelfPingOperGroup,
       "tmnxMplsNotificationIPv6Group": tmnxMplsNotificationIPv6Group,
       "tmnxMplsNotifyObjsLspResource": tmnxMplsNotifyObjsLspResource,
       "tmnxMplsNotifyV20v0Group": tmnxMplsNotifyV20v0Group,
       "tmnxMplsV20v0Group": tmnxMplsV20v0Group,
       "tmnxMplsObsoletedV20v0Group": tmnxMplsObsoletedV20v0Group,
       "tmnxMplsLspSelfPingV20v0Group": tmnxMplsLspSelfPingV20v0Group,
       "tmnxMplsClassFwdObsoleteGroup": tmnxMplsClassFwdObsoleteGroup,
       "tmnxMplsSrTeIpv6LspTempGroup": tmnxMplsSrTeIpv6LspTempGroup,
       "tmnxMplsTunnelARHopIdTypeGroup": tmnxMplsTunnelARHopIdTypeGroup,
       "tmnxMplsLspPcepToLocalGroup": tmnxMplsLspPcepToLocalGroup,
       "tmnxMplsGenV20Group": tmnxMplsGenV20Group,
       "tmnxMplsGenLspSelfPingV20Group": tmnxMplsGenLspSelfPingV20Group,
       "tmnxMplsGenSrTeLspCountV21Group": tmnxMplsGenSrTeLspCountV21Group,
       "tmnxMplsLspV21Group": tmnxMplsLspV21Group,
       "tmnxMplsGenTTMV21Group": tmnxMplsGenTTMV21Group,
       "tmnxMplsLspPathDegradeV21Group": tmnxMplsLspPathDegradeV21Group,
       "tmnxMplsNotifyObjsLspPathFailure": tmnxMplsNotifyObjsLspPathFailure,
       "tmnxMplsNotifyLspPathV21v0Group": tmnxMplsNotifyLspPathV21v0Group,
       "tmnxMplsPccPceOperStateV21Group": tmnxMplsPccPceOperStateV21Group,
       "tmnxMplsLspTempExtV21Group": tmnxMplsLspTempExtV21Group,
       "tmnxMplsLspStatsModeV21Group": tmnxMplsLspStatsModeV21Group,
       "tmnxMplsLspOvrTunnelElcGroup": tmnxMplsLspOvrTunnelElcGroup,
       "tmnxMplsLspTransportFrrGroup": tmnxMplsLspTransportFrrGroup,
       "tmnxMplsLspTempPathProfGroup": tmnxMplsLspTempPathProfGroup,
       "tmnxMplsLspExtBfdGroup": tmnxMplsLspExtBfdGroup,
       "tmnxMplsLspRateCountersGroup": tmnxMplsLspRateCountersGroup,
       "tmnxP2mpMplsLspSoftPreemptGroup": tmnxP2mpMplsLspSoftPreemptGroup,
       "tmnxMplsNotifyV22v0Group": tmnxMplsNotifyV22v0Group,
       "tmnxMplsObjs": tmnxMplsObjs,
       "vRtrMplsLspTable": vRtrMplsLspTable,
       "vRtrMplsLspEntry": vRtrMplsLspEntry,
       "vRtrMplsLspIndex": vRtrMplsLspIndex,
       "vRtrMplsLspRowStatus": vRtrMplsLspRowStatus,
       "vRtrMplsLspLastChange": vRtrMplsLspLastChange,
       "vRtrMplsLspName": vRtrMplsLspName,
       "vRtrMplsLspAdminState": vRtrMplsLspAdminState,
       "vRtrMplsLspOperState": vRtrMplsLspOperState,
       "vRtrMplsLspFromAddr": vRtrMplsLspFromAddr,
       "vRtrMplsLspToAddr": vRtrMplsLspToAddr,
       "vRtrMplsLspType": vRtrMplsLspType,
       "vRtrMplsLspOutSegIndx": vRtrMplsLspOutSegIndx,
       "vRtrMplsLspRetryTimer": vRtrMplsLspRetryTimer,
       "vRtrMplsLspRetryLimit": vRtrMplsLspRetryLimit,
       "vRtrMplsLspMetric": vRtrMplsLspMetric,
       "vRtrMplsLspDecrementTtl": vRtrMplsLspDecrementTtl,
       "vRtrMplsLspCspf": vRtrMplsLspCspf,
       "vRtrMplsLspFastReroute": vRtrMplsLspFastReroute,
       "vRtrMplsLspFRHopLimit": vRtrMplsLspFRHopLimit,
       "vRtrMplsLspFRBandwidth": vRtrMplsLspFRBandwidth,
       "vRtrMplsLspClassOfService": vRtrMplsLspClassOfService,
       "vRtrMplsLspSetupPriority": vRtrMplsLspSetupPriority,
       "vRtrMplsLspHoldPriority": vRtrMplsLspHoldPriority,
       "vRtrMplsLspRecord": vRtrMplsLspRecord,
       "vRtrMplsLspPreference": vRtrMplsLspPreference,
       "vRtrMplsLspBandwidth": vRtrMplsLspBandwidth,
       "vRtrMplsLspBwProtect": vRtrMplsLspBwProtect,
       "vRtrMplsLspHopLimit": vRtrMplsLspHopLimit,
       "vRtrMplsLspNegotiatedMTU": vRtrMplsLspNegotiatedMTU,
       "vRtrMplsLspRsvpResvStyle": vRtrMplsLspRsvpResvStyle,
       "vRtrMplsLspRsvpAdspec": vRtrMplsLspRsvpAdspec,
       "vRtrMplsLspFRMethod": vRtrMplsLspFRMethod,
       "vRtrMplsLspFRNodeProtect": vRtrMplsLspFRNodeProtect,
       "vRtrMplsLspAdminGroupInclude": vRtrMplsLspAdminGroupInclude,
       "vRtrMplsLspAdminGroupExclude": vRtrMplsLspAdminGroupExclude,
       "vRtrMplsLspAdaptive": vRtrMplsLspAdaptive,
       "vRtrMplsLspInheritance": vRtrMplsLspInheritance,
       "vRtrMplsLspOptimizeTimer": vRtrMplsLspOptimizeTimer,
       "vRtrMplsLspOperFastReroute": vRtrMplsLspOperFastReroute,
       "vRtrMplsLspFRObject": vRtrMplsLspFRObject,
       "vRtrMplsLspHoldTimer": vRtrMplsLspHoldTimer,
       "vRtrMplsLspCspfTeMetricEnabled": vRtrMplsLspCspfTeMetricEnabled,
       "vRtrMplsLspP2mpId": vRtrMplsLspP2mpId,
       "vRtrMplsLspClassType": vRtrMplsLspClassType,
       "vRtrMplsLspOperMetric": vRtrMplsLspOperMetric,
       "vRtrMplsLspLdpOverRsvpInclude": vRtrMplsLspLdpOverRsvpInclude,
       "vRtrMplsLspLeastFill": vRtrMplsLspLeastFill,
       "vRtrMplsLspVprnAutoBindInclude": vRtrMplsLspVprnAutoBindInclude,
       "vRtrMplsLspMainCTRetryLimit": vRtrMplsLspMainCTRetryLimit,
       "vRtrMplsLspIgpShortcut": vRtrMplsLspIgpShortcut,
       "vRtrMplsLspOriginTemplate": vRtrMplsLspOriginTemplate,
       "vRtrMplsLspAutoBandwidth": vRtrMplsLspAutoBandwidth,
       "vRtrMplsLspCspfToFirstLoose": vRtrMplsLspCspfToFirstLoose,
       "vRtrMplsLspPropAdminGroup": vRtrMplsLspPropAdminGroup,
       "vRtrMplsLspBgpShortcut": vRtrMplsLspBgpShortcut,
       "vRtrMplsLspBgpTransportTunnel": vRtrMplsLspBgpTransportTunnel,
       "vRtrMplsLspSwitchStbyPath": vRtrMplsLspSwitchStbyPath,
       "vRtrMplsLspSwitchStbyPathIndex": vRtrMplsLspSwitchStbyPathIndex,
       "vRtrMplsLspSwitchStbyPathForce": vRtrMplsLspSwitchStbyPathForce,
       "vRtrMplsLspExcludeNodeAddrType": vRtrMplsLspExcludeNodeAddrType,
       "vRtrMplsLspExcludeNodeAddr": vRtrMplsLspExcludeNodeAddr,
       "vRtrMplsLspIgpShortcutLfaType": vRtrMplsLspIgpShortcutLfaType,
       "vRtrMplsLspToAddrType": vRtrMplsLspToAddrType,
       "vRtrMplsLspFromAddrType": vRtrMplsLspFromAddrType,
       "vRtrMplsLspToNodeId": vRtrMplsLspToNodeId,
       "vRtrMplsLspFromNodeId": vRtrMplsLspFromNodeId,
       "vRtrMplsLspDestGlobalId": vRtrMplsLspDestGlobalId,
       "vRtrMplsLspDestTunnelNum": vRtrMplsLspDestTunnelNum,
       "vRtrMplsLspFRPropAdminGroup": vRtrMplsLspFRPropAdminGroup,
       "vRtrMplsLspIgpShortcutRelOffset": vRtrMplsLspIgpShortcutRelOffset,
       "vRtrMplsLspRevertTimer": vRtrMplsLspRevertTimer,
       "vRtrMplsLspRevertTimeRemain": vRtrMplsLspRevertTimeRemain,
       "vRtrMplsLspLoadBalancingWeight": vRtrMplsLspLoadBalancingWeight,
       "vRtrMplsLspClassFwdingEnabled": vRtrMplsLspClassFwdingEnabled,
       "vRtrMplsLspFC": vRtrMplsLspFC,
       "vRtrMplsLspBfdTemplateName": vRtrMplsLspBfdTemplateName,
       "vRtrMplsLspBfdEnable": vRtrMplsLspBfdEnable,
       "vRtrMplsLspBfdPingIntvl": vRtrMplsLspBfdPingIntvl,
       "vRtrMplsLspNgFromAddr": vRtrMplsLspNgFromAddr,
       "vRtrMplsLspNgToAddr": vRtrMplsLspNgToAddr,
       "vRtrMplsLspStatTable": vRtrMplsLspStatTable,
       "vRtrMplsLspStatEntry": vRtrMplsLspStatEntry,
       "vRtrMplsLspOctets": vRtrMplsLspOctets,
       "vRtrMplsLspPackets": vRtrMplsLspPackets,
       "vRtrMplsLspAge": vRtrMplsLspAge,
       "vRtrMplsLspTimeUp": vRtrMplsLspTimeUp,
       "vRtrMplsLspTimeDown": vRtrMplsLspTimeDown,
       "vRtrMplsLspPrimaryTimeUp": vRtrMplsLspPrimaryTimeUp,
       "vRtrMplsLspTransitions": vRtrMplsLspTransitions,
       "vRtrMplsLspLastTransition": vRtrMplsLspLastTransition,
       "vRtrMplsLspPathChanges": vRtrMplsLspPathChanges,
       "vRtrMplsLspLastPathChange": vRtrMplsLspLastPathChange,
       "vRtrMplsLspConfiguredPaths": vRtrMplsLspConfiguredPaths,
       "vRtrMplsLspStandbyPaths": vRtrMplsLspStandbyPaths,
       "vRtrMplsLspOperationalPaths": vRtrMplsLspOperationalPaths,
       "vRtrMplsLspConfP2mpInstances": vRtrMplsLspConfP2mpInstances,
       "vRtrMplsLspStatsEgrIndexUnAvail": vRtrMplsLspStatsEgrIndexUnAvail,
       "vRtrMplsLspSelfPingTimeouts": vRtrMplsLspSelfPingTimeouts,
       "vRtrMplsLspSelfPingOamNoRsc": vRtrMplsLspSelfPingOamNoRsc,
       "vRtrMplsLspPathTableSpinlock": vRtrMplsLspPathTableSpinlock,
       "vRtrMplsLspPathTable": vRtrMplsLspPathTable,
       "vRtrMplsLspPathEntry": vRtrMplsLspPathEntry,
       "vRtrMplsLspPathRowStatus": vRtrMplsLspPathRowStatus,
       "vRtrMplsLspPathLastChange": vRtrMplsLspPathLastChange,
       "vRtrMplsLspPathType": vRtrMplsLspPathType,
       "vRtrMplsLspPathCos": vRtrMplsLspPathCos,
       "vRtrMplsLspPathProperties": vRtrMplsLspPathProperties,
       "vRtrMplsLspPathBandwidth": vRtrMplsLspPathBandwidth,
       "vRtrMplsLspPathBwProtect": vRtrMplsLspPathBwProtect,
       "vRtrMplsLspPathState": vRtrMplsLspPathState,
       "vRtrMplsLspPathPreference": vRtrMplsLspPathPreference,
       "vRtrMplsLspPathCosSource": vRtrMplsLspPathCosSource,
       "vRtrMplsLspPathClassOfService": vRtrMplsLspPathClassOfService,
       "vRtrMplsLspPathSetupPriority": vRtrMplsLspPathSetupPriority,
       "vRtrMplsLspPathHoldPriority": vRtrMplsLspPathHoldPriority,
       "vRtrMplsLspPathRecord": vRtrMplsLspPathRecord,
       "vRtrMplsLspPathHopLimit": vRtrMplsLspPathHopLimit,
       "vRtrMplsLspPathSharing": vRtrMplsLspPathSharing,
       "vRtrMplsLspPathAdminState": vRtrMplsLspPathAdminState,
       "vRtrMplsLspPathOperState": vRtrMplsLspPathOperState,
       "vRtrMplsLspPathInheritance": vRtrMplsLspPathInheritance,
       "vRtrMplsLspPathLspId": vRtrMplsLspPathLspId,
       "vRtrMplsLspPathRetryTimeRemaining": vRtrMplsLspPathRetryTimeRemaining,
       "vRtrMplsLspPathTunnelARHopListIndex": vRtrMplsLspPathTunnelARHopListIndex,
       "vRtrMplsLspPathNegotiatedMTU": vRtrMplsLspPathNegotiatedMTU,
       "vRtrMplsLspPathFailCode": vRtrMplsLspPathFailCode,
       "vRtrMplsLspPathFailNodeAddr": vRtrMplsLspPathFailNodeAddr,
       "vRtrMplsLspPathAdminGroupInclude": vRtrMplsLspPathAdminGroupInclude,
       "vRtrMplsLspPathAdminGroupExclude": vRtrMplsLspPathAdminGroupExclude,
       "vRtrMplsLspPathAdaptive": vRtrMplsLspPathAdaptive,
       "vRtrMplsLspPathOptimizeTimer": vRtrMplsLspPathOptimizeTimer,
       "vRtrMplsLspPathNextOptimize": vRtrMplsLspPathNextOptimize,
       "vRtrMplsLspPathOperBandwidth": vRtrMplsLspPathOperBandwidth,
       "vRtrMplsLspPathMBBState": vRtrMplsLspPathMBBState,
       "vRtrMplsLspPathResignal": vRtrMplsLspPathResignal,
       "vRtrMplsLspPathTunnelCRHopListIndex": vRtrMplsLspPathTunnelCRHopListIndex,
       "vRtrMplsLspPathOperMTU": vRtrMplsLspPathOperMTU,
       "vRtrMplsLspPathRecordLabel": vRtrMplsLspPathRecordLabel,
       "vRtrMplsLspPathSrlg": vRtrMplsLspPathSrlg,
       "vRtrMplsLspPathSrlgDisjoint": vRtrMplsLspPathSrlgDisjoint,
       "vRtrMplsLspPathLastResigAttempt": vRtrMplsLspPathLastResigAttempt,
       "vRtrMplsLspPathMetric": vRtrMplsLspPathMetric,
       "vRtrMplsLspPathLastMBBType": vRtrMplsLspPathLastMBBType,
       "vRtrMplsLspPathLastMBBEnd": vRtrMplsLspPathLastMBBEnd,
       "vRtrMplsLspPathLastMBBMetric": vRtrMplsLspPathLastMBBMetric,
       "vRtrMplsLspPathLastMBBState": vRtrMplsLspPathLastMBBState,
       "vRtrMplsLspPathMBBTypeInProg": vRtrMplsLspPathMBBTypeInProg,
       "vRtrMplsLspPathMBBStarted": vRtrMplsLspPathMBBStarted,
       "vRtrMplsLspPathMBBNextRetry": vRtrMplsLspPathMBBNextRetry,
       "vRtrMplsLspPathMBBRetryAttempts": vRtrMplsLspPathMBBRetryAttempts,
       "vRtrMplsLspPathMBBFailCode": vRtrMplsLspPathMBBFailCode,
       "vRtrMplsLspPathMBBFailNodeArType": vRtrMplsLspPathMBBFailNodeArType,
       "vRtrMplsLspPathMBBFailNodeAddr": vRtrMplsLspPathMBBFailNodeAddr,
       "vRtrMplsLspPathClassType": vRtrMplsLspPathClassType,
       "vRtrMplsLspPathOperMetric": vRtrMplsLspPathOperMetric,
       "vRtrMplsLspPathResignalEligible": vRtrMplsLspPathResignalEligible,
       "vRtrMplsLspPathIsFastRetry": vRtrMplsLspPathIsFastRetry,
       "vRtrMplsLspPathBackupCT": vRtrMplsLspPathBackupCT,
       "vRtrMplsLspPathMainCTRetryRem": vRtrMplsLspPathMainCTRetryRem,
       "vRtrMplsLspPathOperCT": vRtrMplsLspPathOperCT,
       "vRtrMplsLspPathNewPathIndex": vRtrMplsLspPathNewPathIndex,
       "vRtrMplsLspPathMBBMainCTRetryRem": vRtrMplsLspPathMBBMainCTRetryRem,
       "vRtrMplsLspPathSigBWMBBInProg": vRtrMplsLspPathSigBWMBBInProg,
       "vRtrMplsLspPathSigBWLastMBB": vRtrMplsLspPathSigBWLastMBB,
       "vRtrMplsLspPathActiveByManual": vRtrMplsLspPathActiveByManual,
       "vRtrMplsLspPathTimeoutIn": vRtrMplsLspPathTimeoutIn,
       "vRtrMplsLspPathMBBTimeoutIn": vRtrMplsLspPathMBBTimeoutIn,
       "vRtrMplsLspPathBfdTemplateName": vRtrMplsLspPathBfdTemplateName,
       "vRtrMplsLspPathBfdEnable": vRtrMplsLspPathBfdEnable,
       "vRtrMplsLspPathBfdPingIntvl": vRtrMplsLspPathBfdPingIntvl,
       "vRtrMplsLspPathLastUpdateTime": vRtrMplsLspPathLastUpdateTime,
       "vRtrMplsLspPathLastUpdateId": vRtrMplsLspPathLastUpdateId,
       "vRtrMplsLspPathLastUpdateState": vRtrMplsLspPathLastUpdateState,
       "vRtrMplsLspPathLastUpdFailCode": vRtrMplsLspPathLastUpdFailCode,
       "vRtrMplsLspPathBfdUpWaitTimer": vRtrMplsLspPathBfdUpWaitTimer,
       "vRtrMplsLspPathBfdUpWaitTmLeft": vRtrMplsLspPathBfdUpWaitTmLeft,
       "vRtrMplsLspPathBfdState": vRtrMplsLspPathBfdState,
       "vRtrMplsLspPathBfdStartFailRsn": vRtrMplsLspPathBfdStartFailRsn,
       "vRtrMplsLspPathBfdOperUpWaitTmr": vRtrMplsLspPathBfdOperUpWaitTmr,
       "vRtrMplsLspPathSelfPingOprState": vRtrMplsLspPathSelfPingOprState,
       "vRtrMplsLspPathLastMBBFailCode": vRtrMplsLspPathLastMBBFailCode,
       "vRtrMplsLspPathDegraded": vRtrMplsLspPathDegraded,
       "vRtrMplsLspPathDegradedReason": vRtrMplsLspPathDegradedReason,
       "vRtrMplsLspPathReturnPathLabel": vRtrMplsLspPathReturnPathLabel,
       "vRtrMplsLspPathStatTable": vRtrMplsLspPathStatTable,
       "vRtrMplsLspPathStatEntry": vRtrMplsLspPathStatEntry,
       "vRtrMplsLspPathTimeUp": vRtrMplsLspPathTimeUp,
       "vRtrMplsLspPathTimeDown": vRtrMplsLspPathTimeDown,
       "vRtrMplsLspPathRetryAttempts": vRtrMplsLspPathRetryAttempts,
       "vRtrMplsLspPathTransitionCount": vRtrMplsLspPathTransitionCount,
       "vRtrMplsLspPathCspfQueries": vRtrMplsLspPathCspfQueries,
       "vRtrMplsXCTable": vRtrMplsXCTable,
       "vRtrMplsXCEntry": vRtrMplsXCEntry,
       "vRtrMplsXCIndex": vRtrMplsXCIndex,
       "vRtrMplsInSegmentIfIndex": vRtrMplsInSegmentIfIndex,
       "vRtrMplsInSegmentLabel": vRtrMplsInSegmentLabel,
       "vRtrMplsOutSegmentIndex": vRtrMplsOutSegmentIndex,
       "vRtrMplsERHopTunnelIndex": vRtrMplsERHopTunnelIndex,
       "vRtrMplsARHopTunnelIndex": vRtrMplsARHopTunnelIndex,
       "vRtrMplsRsvpSessionIndex": vRtrMplsRsvpSessionIndex,
       "vRtrMplsXCFailCode": vRtrMplsXCFailCode,
       "vRtrMplsXCCHopTableIndex": vRtrMplsXCCHopTableIndex,
       "vRtrMplsGeneralTable": vRtrMplsGeneralTable,
       "vRtrMplsGeneralEntry": vRtrMplsGeneralEntry,
       "vRtrMplsGeneralLastChange": vRtrMplsGeneralLastChange,
       "vRtrMplsGeneralAdminState": vRtrMplsGeneralAdminState,
       "vRtrMplsGeneralOperState": vRtrMplsGeneralOperState,
       "vRtrMplsGeneralPropagateTtl": vRtrMplsGeneralPropagateTtl,
       "vRtrMplsGeneralTE": vRtrMplsGeneralTE,
       "vRtrMplsGeneralNewLspIndex": vRtrMplsGeneralNewLspIndex,
       "vRtrMplsGeneralOptimizeTimer": vRtrMplsGeneralOptimizeTimer,
       "vRtrMplsGeneralFRObject": vRtrMplsGeneralFRObject,
       "vRtrMplsGeneralResignalTimer": vRtrMplsGeneralResignalTimer,
       "vRtrMplsGeneralHoldTimer": vRtrMplsGeneralHoldTimer,
       "vRtrMplsGeneralDynamicBypass": vRtrMplsGeneralDynamicBypass,
       "vRtrMplsGeneralNextResignal": vRtrMplsGeneralNextResignal,
       "vRtrMplsGeneralOperDownReason": vRtrMplsGeneralOperDownReason,
       "vRtrMplsGeneralSrlgFrr": vRtrMplsGeneralSrlgFrr,
       "vRtrMplsGeneralSrlgFrrStrict": vRtrMplsGeneralSrlgFrrStrict,
       "vRtrMplsGeneralNewP2mpInstIndex": vRtrMplsGeneralNewP2mpInstIndex,
       "vRtrMplsGeneralLeastFillMinThd": vRtrMplsGeneralLeastFillMinThd,
       "vRtrMplsGenLeastFillReoptiThd": vRtrMplsGenLeastFillReoptiThd,
       "vRtrMplsGeneralUseSrlgDB": vRtrMplsGeneralUseSrlgDB,
       "vRtrMplsGeneralP2mpResigTimer": vRtrMplsGeneralP2mpResigTimer,
       "vRtrMplsGeneralP2mpNextResignal": vRtrMplsGeneralP2mpNextResignal,
       "vRtrMplsGeneralSecFastRetryTimer": vRtrMplsGeneralSecFastRetryTimer,
       "vRtrMplsGeneralShortTTLPropLocal": vRtrMplsGeneralShortTTLPropLocal,
       "vRtrMplsGeneralShortTTLPropTrans": vRtrMplsGeneralShortTTLPropTrans,
       "vRtrMplsGeneralStaticLspFRTimer": vRtrMplsGeneralStaticLspFRTimer,
       "vRtrMplsGeneralAutoBWDefSampMul": vRtrMplsGeneralAutoBWDefSampMul,
       "vRtrMplsGeneralAutoBWDefAdjMul": vRtrMplsGeneralAutoBWDefAdjMul,
       "vRtrMplsGeneralExpBackoffRetry": vRtrMplsGeneralExpBackoffRetry,
       "vRtrMplsGeneralCspfOnLooseHop": vRtrMplsGeneralCspfOnLooseHop,
       "vRtrMplsGeneralP2PMaxByPassAssoc": vRtrMplsGeneralP2PMaxByPassAssoc,
       "vRtrMplsGenP2pActPathFastRetry": vRtrMplsGenP2pActPathFastRetry,
       "vRtrMplsGenP2mpS2lFastRetry": vRtrMplsGenP2mpS2lFastRetry,
       "vRtrMplsGenLspInitRetryTimeout": vRtrMplsGenLspInitRetryTimeout,
       "vRtrMplsLoggerEventBundling": vRtrMplsLoggerEventBundling,
       "vRtrMplsGenIssuMplsLockdown": vRtrMplsGenIssuMplsLockdown,
       "vRtrMplsGenFRAdminGroup": vRtrMplsGenFRAdminGroup,
       "vRtrMplsGenRetryOnIgpOverload": vRtrMplsGenRetryOnIgpOverload,
       "vRtrMplsGenMbbPrefCurrentHops": vRtrMplsGenMbbPrefCurrentHops,
       "vRtrMplsGeneralBypassResigTimer": vRtrMplsGeneralBypassResigTimer,
       "vRtrMplsGenBypassNextResignal": vRtrMplsGenBypassNextResignal,
       "vRtrMplsGeneralNewLspSRIndex": vRtrMplsGeneralNewLspSRIndex,
       "vRtrMplsGeneralPceReport": vRtrMplsGeneralPceReport,
       "vRtrMplsGeneralEntropyLblRsvpTe": vRtrMplsGeneralEntropyLblRsvpTe,
       "vRtrMplsGeneralEntropyLblSrTe": vRtrMplsGeneralEntropyLblSrTe,
       "vRtrMplsGeneralAuxStats": vRtrMplsGeneralAuxStats,
       "vRtrMplsGenSrTeResignalTimer": vRtrMplsGenSrTeResignalTimer,
       "vRtrMplsGenMaxBypassPlrAssoc": vRtrMplsGenMaxBypassPlrAssoc,
       "vRtrMplsGenLspSelfPingInterval": vRtrMplsGenLspSelfPingInterval,
       "vRtrMplsGenLspSelfPingTimeout": vRtrMplsGenLspSelfPingTimeout,
       "vRtrMplsGenLspSelfPingRsvpTe": vRtrMplsGenLspSelfPingRsvpTe,
       "vRtrMplsGenSrTeResigOnIgpEvent": vRtrMplsGenSrTeResigOnIgpEvent,
       "vRtrMplsGeneralV6OperState": vRtrMplsGeneralV6OperState,
       "vRtrMplsGeneralV6OperDownReason": vRtrMplsGeneralV6OperDownReason,
       "vRtrMplsGenSrteNextResignal": vRtrMplsGenSrteNextResignal,
       "vRtrMplsLspSelfPingTimeoutAction": vRtrMplsLspSelfPingTimeoutAction,
       "vRtrMplsGenResignalOnIgpOverload": vRtrMplsGenResignalOnIgpOverload,
       "vRtrMplsGenTunnelTablePrefRsvpTe": vRtrMplsGenTunnelTablePrefRsvpTe,
       "vRtrMplsGenTunnelTablePrefSrTe": vRtrMplsGenTunnelTablePrefSrTe,
       "vRtrMplsGenRsvpPccOperState": vRtrMplsGenRsvpPccOperState,
       "vRtrMplsGenRsvpPceOperState": vRtrMplsGenRsvpPceOperState,
       "vRtrMplsGenSrTePccOperState": vRtrMplsGenSrTePccOperState,
       "vRtrMplsGenSrTePceOperState": vRtrMplsGenSrTePceOperState,
       "vRtrMplsGeneralStatTable": vRtrMplsGeneralStatTable,
       "vRtrMplsGeneralStatEntry": vRtrMplsGeneralStatEntry,
       "vRtrMplsGeneralStaticLspOriginate": vRtrMplsGeneralStaticLspOriginate,
       "vRtrMplsGeneralStaticLspTransit": vRtrMplsGeneralStaticLspTransit,
       "vRtrMplsGeneralStaticLspTerminate": vRtrMplsGeneralStaticLspTerminate,
       "vRtrMplsGeneralDynamicLspOriginate": vRtrMplsGeneralDynamicLspOriginate,
       "vRtrMplsGeneralDynamicLspTransit": vRtrMplsGeneralDynamicLspTransit,
       "vRtrMplsGeneralDynamicLspTerminate": vRtrMplsGeneralDynamicLspTerminate,
       "vRtrMplsGeneralDetourLspOriginate": vRtrMplsGeneralDetourLspOriginate,
       "vRtrMplsGeneralDetourLspTransit": vRtrMplsGeneralDetourLspTransit,
       "vRtrMplsGeneralDetourLspTerminate": vRtrMplsGeneralDetourLspTerminate,
       "vRtrMplsGeneralS2lOriginate": vRtrMplsGeneralS2lOriginate,
       "vRtrMplsGeneralS2lTransit": vRtrMplsGeneralS2lTransit,
       "vRtrMplsGeneralS2lTerminate": vRtrMplsGeneralS2lTerminate,
       "vRtrMplsGeneralLspEgrStatCount": vRtrMplsGeneralLspEgrStatCount,
       "vRtrMplsGeneralLspIgrStatCount": vRtrMplsGeneralLspIgrStatCount,
       "vRtrMplsGenMplsTpLspOriginate": vRtrMplsGenMplsTpLspOriginate,
       "vRtrMplsGenMplsTpLspTransit": vRtrMplsGenMplsTpLspTransit,
       "vRtrMplsGenMplsTpLspTerminate": vRtrMplsGenMplsTpLspTerminate,
       "vRtrMplsGenMplsTpOrigPathInst": vRtrMplsGenMplsTpOrigPathInst,
       "vRtrMplsGenMplsTpTranPathInst": vRtrMplsGenMplsTpTranPathInst,
       "vRtrMplsGenMplsTpTermPathInst": vRtrMplsGenMplsTpTermPathInst,
       "vRtrMplsGeneralMeshP2pOriginate": vRtrMplsGeneralMeshP2pOriginate,
       "vRtrMplsGeneralOneHopP2pOrigin": vRtrMplsGeneralOneHopP2pOrigin,
       "vRtrMplsGeneralSrTeLspOriginate": vRtrMplsGeneralSrTeLspOriginate,
       "vRtrMplsGenMeshP2PSrTeLspOrig": vRtrMplsGenMeshP2PSrTeLspOrig,
       "vRtrMplsGenOneHopP2PSrTeLspOrig": vRtrMplsGenOneHopP2PSrTeLspOrig,
       "vRtrMplsGenPceInitP2PSrTeLspOrig": vRtrMplsGenPceInitP2PSrTeLspOrig,
       "vRtrMplsGenLspSelfPingTimeouts": vRtrMplsGenLspSelfPingTimeouts,
       "vRtrMplsGenLspSelfPingOamNoRsc": vRtrMplsGenLspSelfPingOamNoRsc,
       "vRtrMplsGenDynP2pLspUp": vRtrMplsGenDynP2pLspUp,
       "vRtrMplsGenSrTeIpv4LspUp": vRtrMplsGenSrTeIpv4LspUp,
       "vRtrMplsGenSrTeIpv6LspUp": vRtrMplsGenSrTeIpv6LspUp,
       "vRtrMplsGenMeshSrTeIpv4LspUp": vRtrMplsGenMeshSrTeIpv4LspUp,
       "vRtrMplsGenMeshSrTeIpv6LspUp": vRtrMplsGenMeshSrTeIpv6LspUp,
       "vRtrMplsGenOneHopSrTeIpv4LspUp": vRtrMplsGenOneHopSrTeIpv4LspUp,
       "vRtrMplsGenOneHopSrTeIpv6LspUp": vRtrMplsGenOneHopSrTeIpv6LspUp,
       "vRtrMplsGenPceInitSrTeIpv4LspUp": vRtrMplsGenPceInitSrTeIpv4LspUp,
       "vRtrMplsGenPceInitSrTeIpv6LspUp": vRtrMplsGenPceInitSrTeIpv6LspUp,
       "vRtrMplsGenOnDemandSrTeLspOrig": vRtrMplsGenOnDemandSrTeLspOrig,
       "vRtrMplsGenOnDemandSrTeIpv4LspUp": vRtrMplsGenOnDemandSrTeIpv4LspUp,
       "vRtrMplsGenOnDemandSrTeIpv6LspUp": vRtrMplsGenOnDemandSrTeIpv6LspUp,
       "vRtrMplsIfTable": vRtrMplsIfTable,
       "vRtrMplsIfEntry": vRtrMplsIfEntry,
       "vRtrMplsIfAdminState": vRtrMplsIfAdminState,
       "vRtrMplsIfOperState": vRtrMplsIfOperState,
       "vRtrMplsIfAdminGroup": vRtrMplsIfAdminGroup,
       "vRtrMplsIfTeMetric": vRtrMplsIfTeMetric,
       "vRtrMplsIfV6OperState": vRtrMplsIfV6OperState,
       "vRtrMplsIfStatTable": vRtrMplsIfStatTable,
       "vRtrMplsIfStatEntry": vRtrMplsIfStatEntry,
       "vRtrMplsIfTxPktCount": vRtrMplsIfTxPktCount,
       "vRtrMplsIfRxPktCount": vRtrMplsIfRxPktCount,
       "vRtrMplsIfTxOctetCount": vRtrMplsIfTxOctetCount,
       "vRtrMplsIfRxOctetCount": vRtrMplsIfRxOctetCount,
       "vRtrMplsIfAltTxPktCount": vRtrMplsIfAltTxPktCount,
       "vRtrMplsIfAltRxPktCount": vRtrMplsIfAltRxPktCount,
       "vRtrMplsIfAltTxOctetCount": vRtrMplsIfAltTxOctetCount,
       "vRtrMplsIfAltRxOctetCount": vRtrMplsIfAltRxOctetCount,
       "vRtrMplsTunnelARHopTable": vRtrMplsTunnelARHopTable,
       "vRtrMplsTunnelARHopEntry": vRtrMplsTunnelARHopEntry,
       "vRtrMplsTunnelARHopProtection": vRtrMplsTunnelARHopProtection,
       "vRtrMplsTunnelARHopRecordLabel": vRtrMplsTunnelARHopRecordLabel,
       "vRtrMplsTunnelARHopRouterId": vRtrMplsTunnelARHopRouterId,
       "vRtrMplsTunnelARHopUnnumIfID": vRtrMplsTunnelARHopUnnumIfID,
       "vRtrMplsTunnelARHopSIDType": vRtrMplsTunnelARHopSIDType,
       "vRtrMplsTunnelARHopNgRouterId": vRtrMplsTunnelARHopNgRouterId,
       "vRtrMplsTunnelARHopNgRtrIdType": vRtrMplsTunnelARHopNgRtrIdType,
       "vRtrMplsTunnelCHopTable": vRtrMplsTunnelCHopTable,
       "vRtrMplsTunnelCHopEntry": vRtrMplsTunnelCHopEntry,
       "vRtrMplsTunnelCHopListIndex": vRtrMplsTunnelCHopListIndex,
       "vRtrMplsTunnelCHopIndex": vRtrMplsTunnelCHopIndex,
       "vRtrMplsTunnelCHopAddrType": vRtrMplsTunnelCHopAddrType,
       "vRtrMplsTunnelCHopIpv4Addr": vRtrMplsTunnelCHopIpv4Addr,
       "vRtrMplsTunnelCHopIpv4PrefixLen": vRtrMplsTunnelCHopIpv4PrefixLen,
       "vRtrMplsTunnelCHopIpv6Addr": vRtrMplsTunnelCHopIpv6Addr,
       "vRtrMplsTunnelCHopIpv6PrefixLen": vRtrMplsTunnelCHopIpv6PrefixLen,
       "vRtrMplsTunnelCHopAsNumber": vRtrMplsTunnelCHopAsNumber,
       "vRtrMplsTunnelCHopLspId": vRtrMplsTunnelCHopLspId,
       "vRtrMplsTunnelCHopStrictOrLoose": vRtrMplsTunnelCHopStrictOrLoose,
       "vRtrMplsTunnelCHopEgressAdmGrp": vRtrMplsTunnelCHopEgressAdmGrp,
       "vRtrMplsTunnelCHopUnnumIfID": vRtrMplsTunnelCHopUnnumIfID,
       "vRtrMplsTunnelCHopRtrID": vRtrMplsTunnelCHopRtrID,
       "vRtrMplsTunnelCHopIsABR": vRtrMplsTunnelCHopIsABR,
       "vRtrMplsAdminGroupTable": vRtrMplsAdminGroupTable,
       "vRtrMplsAdminGroupEntry": vRtrMplsAdminGroupEntry,
       "vRtrMplsAdminGroupName": vRtrMplsAdminGroupName,
       "vRtrMplsAdminGroupRowStatus": vRtrMplsAdminGroupRowStatus,
       "vRtrMplsAdminGroupValue": vRtrMplsAdminGroupValue,
       "vRtrMplsFSGroupTable": vRtrMplsFSGroupTable,
       "vRtrMplsFSGroupEntry": vRtrMplsFSGroupEntry,
       "vRtrMplsFSGroupName": vRtrMplsFSGroupName,
       "vRtrMplsFSGroupRowStatus": vRtrMplsFSGroupRowStatus,
       "vRtrMplsFSGroupCost": vRtrMplsFSGroupCost,
       "vRtrMplsFSGroupParamsTable": vRtrMplsFSGroupParamsTable,
       "vRtrMplsFSGroupParamsEntry": vRtrMplsFSGroupParamsEntry,
       "vRtrMplsFSGroupParamsFromAddr": vRtrMplsFSGroupParamsFromAddr,
       "vRtrMplsFSGroupParamsToAddr": vRtrMplsFSGroupParamsToAddr,
       "vRtrMplsFSGroupParamsRowStatus": vRtrMplsFSGroupParamsRowStatus,
       "tmnxMplsNotificationObjects": tmnxMplsNotificationObjects,
       "vRtrMplsLspNotificationReasonCode": vRtrMplsLspNotificationReasonCode,
       "vRtrMplsLspPathNotificationReasonCode": vRtrMplsLspPathNotificationReasonCode,
       "vRtrMplsNotifyRow": vRtrMplsNotifyRow,
       "vRtrMplsP2mpInstNotifIndex": vRtrMplsP2mpInstNotifIndex,
       "vRtrMplsP2mpInstNotifReasonCode": vRtrMplsP2mpInstNotifReasonCode,
       "vRtrMplsS2lSubLspNtDstAddrType": vRtrMplsS2lSubLspNtDstAddrType,
       "vRtrMplsS2lSubLspNtDstAddr": vRtrMplsS2lSubLspNtDstAddr,
       "vRtrMplsLspPathCongChgPercent": vRtrMplsLspPathCongChgPercent,
       "vRtrMplsLspPathMbbStatus": vRtrMplsLspPathMbbStatus,
       "vRtrMplsLspPathMbbReasonCode": vRtrMplsLspPathMbbReasonCode,
       "vRtrMplsLspSwitchStbyReasonCode": vRtrMplsLspSwitchStbyReasonCode,
       "vRtrMplsLspOldTunnelIndex": vRtrMplsLspOldTunnelIndex,
       "vRtrMplsXCNotifRednIndicesBitMap": vRtrMplsXCNotifRednIndicesBitMap,
       "vRtrMplsXCNotifyRednBundlingType": vRtrMplsXCNotifyRednBundlingType,
       "vRtrMplsXCNotifyRednNumOfBitsSet": vRtrMplsXCNotifyRednNumOfBitsSet,
       "vRtrMplsXCNotifyRednStartIndex": vRtrMplsXCNotifyRednStartIndex,
       "vRtrMplsXCNotifyRednEndIndex": vRtrMplsXCNotifyRednEndIndex,
       "vRtrMplsIgpOverloadRtrAddrType": vRtrMplsIgpOverloadRtrAddrType,
       "vRtrMplsIgpOverloadRtrAddr": vRtrMplsIgpOverloadRtrAddr,
       "vRtrMplsIgpOverloadIgpType": vRtrMplsIgpOverloadIgpType,
       "vRtrMplsResourceType": vRtrMplsResourceType,
       "vRtrMplsLspManualSwFailReason": vRtrMplsLspManualSwFailReason,
       "vRtrMplsLspPathManDegState": vRtrMplsLspPathManDegState,
       "vRtrMplsLabelRangeTable": vRtrMplsLabelRangeTable,
       "vRtrMplsLabelRangeEntry": vRtrMplsLabelRangeEntry,
       "vRtrMplsLabelType": vRtrMplsLabelType,
       "vRtrMplsLabelRangeMin": vRtrMplsLabelRangeMin,
       "vRtrMplsLabelRangeMax": vRtrMplsLabelRangeMax,
       "vRtrMplsLabelRangeAging": vRtrMplsLabelRangeAging,
       "vRtrMplsLabelRangeAvailable": vRtrMplsLabelRangeAvailable,
       "vRtrMplsStaticLSPLabelTable": vRtrMplsStaticLSPLabelTable,
       "vRtrMplsStaticLSPLabelEntry": vRtrMplsStaticLSPLabelEntry,
       "vRtrMplsStaticLSPLabel": vRtrMplsStaticLSPLabel,
       "vRtrMplsStaticLSPLabelOwner": vRtrMplsStaticLSPLabelOwner,
       "vRtrMplsStaticSvcLabelTable": vRtrMplsStaticSvcLabelTable,
       "vRtrMplsStaticSvcLabelEntry": vRtrMplsStaticSvcLabelEntry,
       "vRtrMplsStaticSvcLabel": vRtrMplsStaticSvcLabel,
       "vRtrMplsStaticSvcLabelOwner": vRtrMplsStaticSvcLabelOwner,
       "vRtrMplsSrlgGrpTableLastChanged": vRtrMplsSrlgGrpTableLastChanged,
       "vRtrMplsSrlgGrpTable": vRtrMplsSrlgGrpTable,
       "vRtrMplsSrlgGrpEntry": vRtrMplsSrlgGrpEntry,
       "vRtrMplsSrlgGrpName": vRtrMplsSrlgGrpName,
       "vRtrMplsSrlgGrpRowStatus": vRtrMplsSrlgGrpRowStatus,
       "vRtrMplsSrlgGrpLastChanged": vRtrMplsSrlgGrpLastChanged,
       "vRtrMplsSrlgGrpValue": vRtrMplsSrlgGrpValue,
       "vRtrMplsIfSrlgGrpTblLastChanged": vRtrMplsIfSrlgGrpTblLastChanged,
       "vRtrMplsIfSrlgGrpTable": vRtrMplsIfSrlgGrpTable,
       "vRtrMplsIfSrlgGrpEntry": vRtrMplsIfSrlgGrpEntry,
       "vRtrMplsIfSrlgGrpName": vRtrMplsIfSrlgGrpName,
       "vRtrMplsIfSrlgGrpRowStatus": vRtrMplsIfSrlgGrpRowStatus,
       "vRtrMplsIfSrlgGrpLastChanged": vRtrMplsIfSrlgGrpLastChanged,
       "vRtrMplsP2mpInstTblLastChanged": vRtrMplsP2mpInstTblLastChanged,
       "vRtrMplsP2mpInstTable": vRtrMplsP2mpInstTable,
       "vRtrMplsP2mpInstEntry": vRtrMplsP2mpInstEntry,
       "vRtrMplsP2mpInstIndex": vRtrMplsP2mpInstIndex,
       "vRtrMplsP2mpInstRowStatus": vRtrMplsP2mpInstRowStatus,
       "vRtrMplsP2mpInstLastChange": vRtrMplsP2mpInstLastChange,
       "vRtrMplsP2mpInstName": vRtrMplsP2mpInstName,
       "vRtrMplsP2mpInstType": vRtrMplsP2mpInstType,
       "vRtrMplsP2mpInstProperties": vRtrMplsP2mpInstProperties,
       "vRtrMplsP2mpInstBandwidth": vRtrMplsP2mpInstBandwidth,
       "vRtrMplsP2mpInstState": vRtrMplsP2mpInstState,
       "vRtrMplsP2mpInstSetupPriority": vRtrMplsP2mpInstSetupPriority,
       "vRtrMplsP2mpInstHoldPriority": vRtrMplsP2mpInstHoldPriority,
       "vRtrMplsP2mpInstRecord": vRtrMplsP2mpInstRecord,
       "vRtrMplsP2mpInstHopLimit": vRtrMplsP2mpInstHopLimit,
       "vRtrMplsP2mpInstAdminState": vRtrMplsP2mpInstAdminState,
       "vRtrMplsP2mpInstOperState": vRtrMplsP2mpInstOperState,
       "vRtrMplsP2mpInstInheritance": vRtrMplsP2mpInstInheritance,
       "vRtrMplsP2mpInstLspId": vRtrMplsP2mpInstLspId,
       "vRtrMplsP2mpInstNegotiatedMTU": vRtrMplsP2mpInstNegotiatedMTU,
       "vRtrMplsP2mpInstFailCode": vRtrMplsP2mpInstFailCode,
       "vRtrMplsP2mpInstFailNodeArType": vRtrMplsP2mpInstFailNodeArType,
       "vRtrMplsP2mpInstFailNodeAddr": vRtrMplsP2mpInstFailNodeAddr,
       "vRtrMplsP2mpInstAdminGrpInclude": vRtrMplsP2mpInstAdminGrpInclude,
       "vRtrMplsP2mpInstAdminGrpExclude": vRtrMplsP2mpInstAdminGrpExclude,
       "vRtrMplsP2mpInstAdaptive": vRtrMplsP2mpInstAdaptive,
       "vRtrMplsP2mpInstOperBandwidth": vRtrMplsP2mpInstOperBandwidth,
       "vRtrMplsP2mpInstResignal": vRtrMplsP2mpInstResignal,
       "vRtrMplsP2mpInstOperMTU": vRtrMplsP2mpInstOperMTU,
       "vRtrMplsP2mpInstRecordLabel": vRtrMplsP2mpInstRecordLabel,
       "vRtrMplsP2mpInstLastResigAttpt": vRtrMplsP2mpInstLastResigAttpt,
       "vRtrMplsP2mpInstMetric": vRtrMplsP2mpInstMetric,
       "vRtrMplsP2mpInstLastMBBType": vRtrMplsP2mpInstLastMBBType,
       "vRtrMplsP2mpInstLastMBBEnd": vRtrMplsP2mpInstLastMBBEnd,
       "vRtrMplsP2mpInstLastMBBMetric": vRtrMplsP2mpInstLastMBBMetric,
       "vRtrMplsP2mpInstLastMBBState": vRtrMplsP2mpInstLastMBBState,
       "vRtrMplsP2mpInstMBBTypeInProg": vRtrMplsP2mpInstMBBTypeInProg,
       "vRtrMplsP2mpInstMBBStarted": vRtrMplsP2mpInstMBBStarted,
       "vRtrMplsP2mpInstMBBNextRetry": vRtrMplsP2mpInstMBBNextRetry,
       "vRtrMplsP2mpInstMBBRetryAttpts": vRtrMplsP2mpInstMBBRetryAttpts,
       "vRtrMplsP2mpInstMBBFailCode": vRtrMplsP2mpInstMBBFailCode,
       "vRtrMplsP2mpInstMBBFailNodeType": vRtrMplsP2mpInstMBBFailNodeType,
       "vRtrMplsP2mpInstMBBFailNodeAddr": vRtrMplsP2mpInstMBBFailNodeAddr,
       "vRtrMplsP2mpInstStatTable": vRtrMplsP2mpInstStatTable,
       "vRtrMplsP2mpInstStatEntry": vRtrMplsP2mpInstStatEntry,
       "vRtrMplsP2mpInstStatS2lChanges": vRtrMplsP2mpInstStatS2lChanges,
       "vRtrMplsP2mpInstStatLastS2lChange": vRtrMplsP2mpInstStatLastS2lChange,
       "vRtrMplsP2mpInstStatConfiguredS2ls": vRtrMplsP2mpInstStatConfiguredS2ls,
       "vRtrMplsP2mpInstStatOperationalS2ls": vRtrMplsP2mpInstStatOperationalS2ls,
       "vRtrMplsP2mpInstStatLastS2lTimeUp": vRtrMplsP2mpInstStatLastS2lTimeUp,
       "vRtrMplsP2mpInstStatLastS2lTimeDown": vRtrMplsP2mpInstStatLastS2lTimeDown,
       "vRtrMplsP2mpInstStatTimeUp": vRtrMplsP2mpInstStatTimeUp,
       "vRtrMplsP2mpInstStatTimeDown": vRtrMplsP2mpInstStatTimeDown,
       "vRtrMplsP2mpInstStatTransitions": vRtrMplsP2mpInstStatTransitions,
       "vRtrMplsP2mpInstStatLastTrans": vRtrMplsP2mpInstStatLastTrans,
       "vRtrMplsS2lSubLspTblLastChanged": vRtrMplsS2lSubLspTblLastChanged,
       "vRtrMplsS2lSubLspTable": vRtrMplsS2lSubLspTable,
       "vRtrMplsS2lSubLspEntry": vRtrMplsS2lSubLspEntry,
       "vRtrMplsS2lSubLspDstAddrType": vRtrMplsS2lSubLspDstAddrType,
       "vRtrMplsS2lSubLspDstAddr": vRtrMplsS2lSubLspDstAddr,
       "vRtrMplsS2lSubLspRowStatus": vRtrMplsS2lSubLspRowStatus,
       "vRtrMplsS2lSubLspLastChange": vRtrMplsS2lSubLspLastChange,
       "vRtrMplsS2lSubLspType": vRtrMplsS2lSubLspType,
       "vRtrMplsS2lSubLspProperties": vRtrMplsS2lSubLspProperties,
       "vRtrMplsS2lSubLspState": vRtrMplsS2lSubLspState,
       "vRtrMplsS2lSubLspAdminState": vRtrMplsS2lSubLspAdminState,
       "vRtrMplsS2lSubLspOperState": vRtrMplsS2lSubLspOperState,
       "vRtrMplsS2lSubGroupId": vRtrMplsS2lSubGroupId,
       "vRtrMplsS2lSubLspId": vRtrMplsS2lSubLspId,
       "vRtrMplsS2lSubLspRetryTimeRemain": vRtrMplsS2lSubLspRetryTimeRemain,
       "vRtrMplsS2lSubLspTunARHopLtIndex": vRtrMplsS2lSubLspTunARHopLtIndex,
       "vRtrMplsS2lSubLspNegotiatedMTU": vRtrMplsS2lSubLspNegotiatedMTU,
       "vRtrMplsS2lSubLspFailCode": vRtrMplsS2lSubLspFailCode,
       "vRtrMplsS2lSubLspFailNodeArType": vRtrMplsS2lSubLspFailNodeArType,
       "vRtrMplsS2lSubLspFailNodeAddr": vRtrMplsS2lSubLspFailNodeAddr,
       "vRtrMplsS2lSubLspOperBandwidth": vRtrMplsS2lSubLspOperBandwidth,
       "vRtrMplsS2lSubLspTunCRHopLtIndex": vRtrMplsS2lSubLspTunCRHopLtIndex,
       "vRtrMplsS2lSubLspOperMTU": vRtrMplsS2lSubLspOperMTU,
       "vRtrMplsS2lSubLspLastResigAttpt": vRtrMplsS2lSubLspLastResigAttpt,
       "vRtrMplsS2lSubLspLastMBBType": vRtrMplsS2lSubLspLastMBBType,
       "vRtrMplsS2lSubLspLastMBBEnd": vRtrMplsS2lSubLspLastMBBEnd,
       "vRtrMplsS2lSubLspLastMBBMetric": vRtrMplsS2lSubLspLastMBBMetric,
       "vRtrMplsS2lSubLspLastMBBState": vRtrMplsS2lSubLspLastMBBState,
       "vRtrMplsS2lSubLspMBBTypeInProg": vRtrMplsS2lSubLspMBBTypeInProg,
       "vRtrMplsS2lSubLspMBBStarted": vRtrMplsS2lSubLspMBBStarted,
       "vRtrMplsS2lSubLspMBBNextRetry": vRtrMplsS2lSubLspMBBNextRetry,
       "vRtrMplsS2lSubLspMBBRetryAttpts": vRtrMplsS2lSubLspMBBRetryAttpts,
       "vRtrMplsS2lSubLspMBBFailCode": vRtrMplsS2lSubLspMBBFailCode,
       "vRtrMplsS2lSubLspMBBFailNodeType": vRtrMplsS2lSubLspMBBFailNodeType,
       "vRtrMplsS2lSubLspMBBFailNodeAddr": vRtrMplsS2lSubLspMBBFailNodeAddr,
       "vRtrMplsS2lSubLspUpTime": vRtrMplsS2lSubLspUpTime,
       "vRtrMplsS2lSubLspDownTime": vRtrMplsS2lSubLspDownTime,
       "vRtrMplsS2lSubLspIsFastRetry": vRtrMplsS2lSubLspIsFastRetry,
       "vRtrMplsS2lSubLspTimeoutIn": vRtrMplsS2lSubLspTimeoutIn,
       "vRtrMplsS2lSubLspMBBTimeoutIn": vRtrMplsS2lSubLspMBBTimeoutIn,
       "vRtrMplsS2lSubLspInterArea": vRtrMplsS2lSubLspInterArea,
       "vRtrMplsS2lSubLspStatTable": vRtrMplsS2lSubLspStatTable,
       "vRtrMplsS2lSubLspStatEntry": vRtrMplsS2lSubLspStatEntry,
       "vRtrMplsS2lSubLspTimeUp": vRtrMplsS2lSubLspTimeUp,
       "vRtrMplsS2lSubLspTimeDown": vRtrMplsS2lSubLspTimeDown,
       "vRtrMplsS2lSubLspRetryAttempts": vRtrMplsS2lSubLspRetryAttempts,
       "vRtrMplsS2lSubLspTransitionCount": vRtrMplsS2lSubLspTransitionCount,
       "vRtrMplsS2lSubLspCspfQueries": vRtrMplsS2lSubLspCspfQueries,
       "vRtrMplsSrlgDBRtrIdTblLastChg": vRtrMplsSrlgDBRtrIdTblLastChg,
       "vRtrMplsSrlgDBRtrIdTable": vRtrMplsSrlgDBRtrIdTable,
       "vRtrMplsSrlgDBRtrIdEntry": vRtrMplsSrlgDBRtrIdEntry,
       "vRtrMplsSrlgDBRtrIdRouterID": vRtrMplsSrlgDBRtrIdRouterID,
       "vRtrMplsSrlgDBRtrIdRowStatus": vRtrMplsSrlgDBRtrIdRowStatus,
       "vRtrMplsSrlgDBRtrIdAdminState": vRtrMplsSrlgDBRtrIdAdminState,
       "vRtrMplsSrlgDBRtrIdLastChanged": vRtrMplsSrlgDBRtrIdLastChanged,
       "vRtrMplsSrlgDBIfTblLastChanged": vRtrMplsSrlgDBIfTblLastChanged,
       "vRtrMplsSrlgDBIfTable": vRtrMplsSrlgDBIfTable,
       "vRtrMplsSrlgDBIfEntry": vRtrMplsSrlgDBIfEntry,
       "vRtrMplsSrlgDBIfIntIpAddrType": vRtrMplsSrlgDBIfIntIpAddrType,
       "vRtrMplsSrlgDBIfIntIpAddr": vRtrMplsSrlgDBIfIntIpAddr,
       "vRtrMplsSrlgDBIfSrlgGroupName": vRtrMplsSrlgDBIfSrlgGroupName,
       "vRtrMplsSrlgDBIfRowStatus": vRtrMplsSrlgDBIfRowStatus,
       "vRtrMplsSrlgDBIfLastChanged": vRtrMplsSrlgDBIfLastChanged,
       "vRtrMplsInSegmentTable": vRtrMplsInSegmentTable,
       "vRtrMplsInSegmentEntry": vRtrMplsInSegmentEntry,
       "vRtrMplsInSegmentNumS2ls": vRtrMplsInSegmentNumS2ls,
       "vRtrMplsOutSegmentTable": vRtrMplsOutSegmentTable,
       "vRtrMplsOutSegmentEntry": vRtrMplsOutSegmentEntry,
       "vRtrMplsOutSegmentNumS2ls": vRtrMplsOutSegmentNumS2ls,
       "vRtrMplsLspStatsTblLastChgd": vRtrMplsLspStatsTblLastChgd,
       "vRtrMplsLspStatsTable": vRtrMplsLspStatsTable,
       "vRtrMplsLspStatsEntry": vRtrMplsLspStatsEntry,
       "vRtrMplsLspStatsType": vRtrMplsLspStatsType,
       "vRtrMplsLspStatsSenderAddrType": vRtrMplsLspStatsSenderAddrType,
       "vRtrMplsLspStatsSenderAddr": vRtrMplsLspStatsSenderAddr,
       "vRtrMplsLspStatsLspName": vRtrMplsLspStatsLspName,
       "vRtrMplsLspStatsRowStatus": vRtrMplsLspStatsRowStatus,
       "vRtrMplsLspStatsLastChanged": vRtrMplsLspStatsLastChanged,
       "vRtrMplsLspStatsCollectStats": vRtrMplsLspStatsCollectStats,
       "vRtrMplsLspStatsAccntingPolicy": vRtrMplsLspStatsAccntingPolicy,
       "vRtrMplsLspStatsAdminState": vRtrMplsLspStatsAdminState,
       "vRtrMplsLspStatsMode": vRtrMplsLspStatsMode,
       "vRtrMplsLspStatisticsTable": vRtrMplsLspStatisticsTable,
       "vRtrMplsLspStatisticsEntry": vRtrMplsLspStatisticsEntry,
       "vRtrMplsInProfilePktsFc0": vRtrMplsInProfilePktsFc0,
       "vRtrMplsInProfilePktsFc0Low32": vRtrMplsInProfilePktsFc0Low32,
       "vRtrMplsInProfilePktsFc0High32": vRtrMplsInProfilePktsFc0High32,
       "vRtrMplsInProfilePktsFc1": vRtrMplsInProfilePktsFc1,
       "vRtrMplsInProfilePktsFc1Low32": vRtrMplsInProfilePktsFc1Low32,
       "vRtrMplsInProfilePktsFc1High32": vRtrMplsInProfilePktsFc1High32,
       "vRtrMplsInProfilePktsFc2": vRtrMplsInProfilePktsFc2,
       "vRtrMplsInProfilePktsFc2Low32": vRtrMplsInProfilePktsFc2Low32,
       "vRtrMplsInProfilePktsFc2High32": vRtrMplsInProfilePktsFc2High32,
       "vRtrMplsInProfilePktsFc3": vRtrMplsInProfilePktsFc3,
       "vRtrMplsInProfilePktsFc3Low32": vRtrMplsInProfilePktsFc3Low32,
       "vRtrMplsInProfilePktsFc3High32": vRtrMplsInProfilePktsFc3High32,
       "vRtrMplsInProfilePktsFc4": vRtrMplsInProfilePktsFc4,
       "vRtrMplsInProfilePktsFc4Low32": vRtrMplsInProfilePktsFc4Low32,
       "vRtrMplsInProfilePktsFc4High32": vRtrMplsInProfilePktsFc4High32,
       "vRtrMplsInProfilePktsFc5": vRtrMplsInProfilePktsFc5,
       "vRtrMplsInProfilePktsFc5Low32": vRtrMplsInProfilePktsFc5Low32,
       "vRtrMplsInProfilePktsFc5High32": vRtrMplsInProfilePktsFc5High32,
       "vRtrMplsInProfilePktsFc6": vRtrMplsInProfilePktsFc6,
       "vRtrMplsInProfilePktsFc6Low32": vRtrMplsInProfilePktsFc6Low32,
       "vRtrMplsInProfilePktsFc6High32": vRtrMplsInProfilePktsFc6High32,
       "vRtrMplsInProfilePktsFc7": vRtrMplsInProfilePktsFc7,
       "vRtrMplsInProfilePktsFc7Low32": vRtrMplsInProfilePktsFc7Low32,
       "vRtrMplsInProfilePktsFc7High32": vRtrMplsInProfilePktsFc7High32,
       "vRtrMplsInProfileOctetsFc0": vRtrMplsInProfileOctetsFc0,
       "vRtrMplsInProfileOctetsFc0Low32": vRtrMplsInProfileOctetsFc0Low32,
       "vRtrMplsInProfileOctetsFc0High32": vRtrMplsInProfileOctetsFc0High32,
       "vRtrMplsInProfileOctetsFc1": vRtrMplsInProfileOctetsFc1,
       "vRtrMplsInProfileOctetsFc1Low32": vRtrMplsInProfileOctetsFc1Low32,
       "vRtrMplsInProfileOctetsFc1High32": vRtrMplsInProfileOctetsFc1High32,
       "vRtrMplsInProfileOctetsFc2": vRtrMplsInProfileOctetsFc2,
       "vRtrMplsInProfileOctetsFc2Low32": vRtrMplsInProfileOctetsFc2Low32,
       "vRtrMplsInProfileOctetsFc2High32": vRtrMplsInProfileOctetsFc2High32,
       "vRtrMplsInProfileOctetsFc3": vRtrMplsInProfileOctetsFc3,
       "vRtrMplsInProfileOctetsFc3Low32": vRtrMplsInProfileOctetsFc3Low32,
       "vRtrMplsInProfileOctetsFc3High32": vRtrMplsInProfileOctetsFc3High32,
       "vRtrMplsInProfileOctetsFc4": vRtrMplsInProfileOctetsFc4,
       "vRtrMplsInProfileOctetsFc4Low32": vRtrMplsInProfileOctetsFc4Low32,
       "vRtrMplsInProfileOctetsFc4High32": vRtrMplsInProfileOctetsFc4High32,
       "vRtrMplsInProfileOctetsFc5": vRtrMplsInProfileOctetsFc5,
       "vRtrMplsInProfileOctetsFc5Low32": vRtrMplsInProfileOctetsFc5Low32,
       "vRtrMplsInProfileOctetsFc5High32": vRtrMplsInProfileOctetsFc5High32,
       "vRtrMplsInProfileOctetsFc6": vRtrMplsInProfileOctetsFc6,
       "vRtrMplsInProfileOctetsFc6Low32": vRtrMplsInProfileOctetsFc6Low32,
       "vRtrMplsInProfileOctetsFc6High32": vRtrMplsInProfileOctetsFc6High32,
       "vRtrMplsInProfileOctetsFc7": vRtrMplsInProfileOctetsFc7,
       "vRtrMplsInProfileOctetsFc7Low32": vRtrMplsInProfileOctetsFc7Low32,
       "vRtrMplsInProfileOctetsFc7High32": vRtrMplsInProfileOctetsFc7High32,
       "vRtrMplsOutOfProfPktsFc0": vRtrMplsOutOfProfPktsFc0,
       "vRtrMplsOutOfProfPktsFc0Low32": vRtrMplsOutOfProfPktsFc0Low32,
       "vRtrMplsOutOfProfPktsFc0High32": vRtrMplsOutOfProfPktsFc0High32,
       "vRtrMplsOutOfProfPktsFc1": vRtrMplsOutOfProfPktsFc1,
       "vRtrMplsOutOfProfPktsFc1Low32": vRtrMplsOutOfProfPktsFc1Low32,
       "vRtrMplsOutOfProfPktsFc1High32": vRtrMplsOutOfProfPktsFc1High32,
       "vRtrMplsOutOfProfPktsFc2": vRtrMplsOutOfProfPktsFc2,
       "vRtrMplsOutOfProfPktsFc2Low32": vRtrMplsOutOfProfPktsFc2Low32,
       "vRtrMplsOutOfProfPktsFc2High32": vRtrMplsOutOfProfPktsFc2High32,
       "vRtrMplsOutOfProfPktsFc3": vRtrMplsOutOfProfPktsFc3,
       "vRtrMplsOutOfProfPktsFc3Low32": vRtrMplsOutOfProfPktsFc3Low32,
       "vRtrMplsOutOfProfPktsFc3High32": vRtrMplsOutOfProfPktsFc3High32,
       "vRtrMplsOutOfProfPktsFc4": vRtrMplsOutOfProfPktsFc4,
       "vRtrMplsOutOfProfPktsFc4Low32": vRtrMplsOutOfProfPktsFc4Low32,
       "vRtrMplsOutOfProfPktsFc4High32": vRtrMplsOutOfProfPktsFc4High32,
       "vRtrMplsOutOfProfPktsFc5": vRtrMplsOutOfProfPktsFc5,
       "vRtrMplsOutOfProfPktsFc5Low32": vRtrMplsOutOfProfPktsFc5Low32,
       "vRtrMplsOutOfProfPktsFc5High32": vRtrMplsOutOfProfPktsFc5High32,
       "vRtrMplsOutOfProfPktsFc6": vRtrMplsOutOfProfPktsFc6,
       "vRtrMplsOutOfProfPktsFc6Low32": vRtrMplsOutOfProfPktsFc6Low32,
       "vRtrMplsOutOfProfPktsFc6High32": vRtrMplsOutOfProfPktsFc6High32,
       "vRtrMplsOutOfProfPktsFc7": vRtrMplsOutOfProfPktsFc7,
       "vRtrMplsOutOfProfPktsFc7Low32": vRtrMplsOutOfProfPktsFc7Low32,
       "vRtrMplsOutOfProfPktsFc7High32": vRtrMplsOutOfProfPktsFc7High32,
       "vRtrMplsOutOfProfOctetsFc0": vRtrMplsOutOfProfOctetsFc0,
       "vRtrMplsOutOfProfOctetsFc0Low32": vRtrMplsOutOfProfOctetsFc0Low32,
       "vRtrMplsOutOfProfOctetsFc0High32": vRtrMplsOutOfProfOctetsFc0High32,
       "vRtrMplsOutOfProfOctetsFc1": vRtrMplsOutOfProfOctetsFc1,
       "vRtrMplsOutOfProfOctetsFc1Low32": vRtrMplsOutOfProfOctetsFc1Low32,
       "vRtrMplsOutOfProfOctetsFc1High32": vRtrMplsOutOfProfOctetsFc1High32,
       "vRtrMplsOutOfProfOctetsFc2": vRtrMplsOutOfProfOctetsFc2,
       "vRtrMplsOutOfProfOctetsFc2Low32": vRtrMplsOutOfProfOctetsFc2Low32,
       "vRtrMplsOutOfProfOctetsFc2High32": vRtrMplsOutOfProfOctetsFc2High32,
       "vRtrMplsOutOfProfOctetsFc3": vRtrMplsOutOfProfOctetsFc3,
       "vRtrMplsOutOfProfOctetsFc3Low32": vRtrMplsOutOfProfOctetsFc3Low32,
       "vRtrMplsOutOfProfOctetsFc3High32": vRtrMplsOutOfProfOctetsFc3High32,
       "vRtrMplsOutOfProfOctetsFc4": vRtrMplsOutOfProfOctetsFc4,
       "vRtrMplsOutOfProfOctetsFc4Low32": vRtrMplsOutOfProfOctetsFc4Low32,
       "vRtrMplsOutOfProfOctetsFc4High32": vRtrMplsOutOfProfOctetsFc4High32,
       "vRtrMplsOutOfProfOctetsFc5": vRtrMplsOutOfProfOctetsFc5,
       "vRtrMplsOutOfProfOctetsFc5Low32": vRtrMplsOutOfProfOctetsFc5Low32,
       "vRtrMplsOutOfProfOctetsFc5High32": vRtrMplsOutOfProfOctetsFc5High32,
       "vRtrMplsOutOfProfOctetsFc6": vRtrMplsOutOfProfOctetsFc6,
       "vRtrMplsOutOfProfOctetsFc6Low32": vRtrMplsOutOfProfOctetsFc6Low32,
       "vRtrMplsOutOfProfOctetsFc6High32": vRtrMplsOutOfProfOctetsFc6High32,
       "vRtrMplsOutOfProfOctetsFc7": vRtrMplsOutOfProfOctetsFc7,
       "vRtrMplsOutOfProfOctetsFc7Low32": vRtrMplsOutOfProfOctetsFc7Low32,
       "vRtrMplsOutOfProfOctetsFc7High32": vRtrMplsOutOfProfOctetsFc7High32,
       "vRtrMplsLspStatsPSBMatch": vRtrMplsLspStatsPSBMatch,
       "vRtrMplsLspStatsTpOnly": vRtrMplsLspStatsTpOnly,
       "vRtrMplsLspStatsLspType": vRtrMplsLspStatsLspType,
       "vRtrMplsLspAggregatePkts": vRtrMplsLspAggregatePkts,
       "vRtrMplsLspAggregateOctets": vRtrMplsLspAggregateOctets,
       "vRtrMplsLspStatsAggregateOnly": vRtrMplsLspStatsAggregateOnly,
       "vRtrMplsLspStatsRateEnabled": vRtrMplsLspStatsRateEnabled,
       "vRtrMplsLspStatsRatePkts": vRtrMplsLspStatsRatePkts,
       "vRtrMplsLspStatsRateMbps": vRtrMplsLspStatsRateMbps,
       "vRtrMplsLspTemplateTblLastChgd": vRtrMplsLspTemplateTblLastChgd,
       "vRtrMplsLspTemplateTable": vRtrMplsLspTemplateTable,
       "vRtrMplsLspTemplateEntry": vRtrMplsLspTemplateEntry,
       "vRtrMplsLspTemplateName": vRtrMplsLspTemplateName,
       "vRtrMplsLspTemplateRowStatus": vRtrMplsLspTemplateRowStatus,
       "vRtrMplsLspTemplateLastChanged": vRtrMplsLspTemplateLastChanged,
       "vRtrMplsLspTemplateAdminState": vRtrMplsLspTemplateAdminState,
       "vRtrMplsLspTemplateType": vRtrMplsLspTemplateType,
       "vRtrMplsLspTemplateAdaptive": vRtrMplsLspTemplateAdaptive,
       "vRtrMplsLspTemplateBandwidth": vRtrMplsLspTemplateBandwidth,
       "vRtrMplsLspTemplateCspf": vRtrMplsLspTemplateCspf,
       "vRtrMplsLspTemplateDefaultPath": vRtrMplsLspTemplateDefaultPath,
       "vRtrMplsLspTemplateAdmGrpIncl": vRtrMplsLspTemplateAdmGrpIncl,
       "vRtrMplsLspTemplateAdmGrpExcl": vRtrMplsLspTemplateAdmGrpExcl,
       "vRtrMplsLspTemplateFastReroute": vRtrMplsLspTemplateFastReroute,
       "vRtrMplsLspTemplateFRMethod": vRtrMplsLspTemplateFRMethod,
       "vRtrMplsLspTemplateFRHopLimit": vRtrMplsLspTemplateFRHopLimit,
       "vRtrMplsLspTemplateHopLimit": vRtrMplsLspTemplateHopLimit,
       "vRtrMplsLspTemplateRecord": vRtrMplsLspTemplateRecord,
       "vRtrMplsLspTemplateRecordLabel": vRtrMplsLspTemplateRecordLabel,
       "vRtrMplsLspTemplateRetryLimit": vRtrMplsLspTemplateRetryLimit,
       "vRtrMplsLspTemplateRetryTimer": vRtrMplsLspTemplateRetryTimer,
       "vRtrMplsLspTemplateCspfTeMetric": vRtrMplsLspTemplateCspfTeMetric,
       "vRtrMplsLspTemplateLspCount": vRtrMplsLspTemplateLspCount,
       "vRtrMplsLspTemplateMvpnRefCount": vRtrMplsLspTemplateMvpnRefCount,
       "vRtrMplsLspTemplateFRPropAdmGrp": vRtrMplsLspTemplateFRPropAdmGrp,
       "vRtrMplsLspTemplatePropAdmGrp": vRtrMplsLspTemplatePropAdmGrp,
       "vRtrMplsLspTemplateBgpShortcut": vRtrMplsLspTemplateBgpShortcut,
       "vRtrMplsLspTemplateIgpShortcut": vRtrMplsLspTemplateIgpShortcut,
       "vRtrMplsLspTemplateLdpOverRsvp": vRtrMplsLspTemplateLdpOverRsvp,
       "vRtrMplsLspTemplateLeastFill": vRtrMplsLspTemplateLeastFill,
       "vRtrMplsLspTemplateMetric": vRtrMplsLspTemplateMetric,
       "vRtrMplsLspTemplateSetupPriority": vRtrMplsLspTemplateSetupPriority,
       "vRtrMplsLspTemplateHoldPriority": vRtrMplsLspTemplateHoldPriority,
       "vRtrMplsLspTemplateVprnAutoBind": vRtrMplsLspTemplateVprnAutoBind,
       "vRtrMplsLspTempIgpSCutLfaType": vRtrMplsLspTempIgpSCutLfaType,
       "vRtrMplsLspTempIgpSCutRelOffset": vRtrMplsLspTempIgpSCutRelOffset,
       "vRtrMplsLspTempAutoBandwidth": vRtrMplsLspTempAutoBandwidth,
       "vRtrMplsLspTempFRNodeProtect": vRtrMplsLspTempFRNodeProtect,
       "vRtrMplsLspTemplateEgrStats": vRtrMplsLspTemplateEgrStats,
       "vRtrMplsLspTempCollectStats": vRtrMplsLspTempCollectStats,
       "vRtrMplsLspTempAccntingPolicy": vRtrMplsLspTempAccntingPolicy,
       "vRtrMplsLspTemplateFromAddrType": vRtrMplsLspTemplateFromAddrType,
       "vRtrMplsLspTemplateFromAddr": vRtrMplsLspTemplateFromAddr,
       "vRtrMplsLspTemplateClassType": vRtrMplsLspTemplateClassType,
       "vRtrMplsLspTempBkupClassType": vRtrMplsLspTempBkupClassType,
       "vRtrMplsLspTempBgpTransportTunn": vRtrMplsLspTempBgpTransportTunn,
       "vRtrMplsLspTempMainCTRetryLimit": vRtrMplsLspTempMainCTRetryLimit,
       "vRtrMplsLspTemplateRsvpAdspec": vRtrMplsLspTemplateRsvpAdspec,
       "vRtrMplsLspTempLoadBalancingWt": vRtrMplsLspTempLoadBalancingWt,
       "vRtrMplsLspTempClassFwdEnabled": vRtrMplsLspTempClassFwdEnabled,
       "vRtrMplsLspTempFC": vRtrMplsLspTempFC,
       "vRtrMplsLspTempBfdTemplateName": vRtrMplsLspTempBfdTemplateName,
       "vRtrMplsLspTempBfdEnable": vRtrMplsLspTempBfdEnable,
       "vRtrMplsLspTempBfdPingIntvl": vRtrMplsLspTempBfdPingIntvl,
       "vRtrMplsLspTempEntropyLabel": vRtrMplsLspTempEntropyLabel,
       "vRtrMplsLspTemplatePceReport": vRtrMplsLspTemplatePceReport,
       "vRtrMplsLspTempMaxSrLabels": vRtrMplsLspTempMaxSrLabels,
       "vRtrMplsLspTempFrrOverheadLabel": vRtrMplsLspTempFrrOverheadLabel,
       "vRtrMplsLspTempBfdFailureAction": vRtrMplsLspTempBfdFailureAction,
       "vRtrMplsLspTempCbfFwdingPlcy": vRtrMplsLspTempCbfFwdingPlcy,
       "vRtrMplsLspTempCbfFwdingSet": vRtrMplsLspTempCbfFwdingSet,
       "vRtrMplsLspTemplateId": vRtrMplsLspTemplateId,
       "vRtrMplsLspTempPathCompMeth": vRtrMplsLspTempPathCompMeth,
       "vRtrMplsLspTempMetricType": vRtrMplsLspTempMetricType,
       "vRtrMplsLspTempLocalSrProt": vRtrMplsLspTempLocalSrProt,
       "vRtrMplsLspTempLabelStackRed": vRtrMplsLspTempLabelStackRed,
       "vRtrMplsLspTempBfdUpWaitTimer": vRtrMplsLspTempBfdUpWaitTimer,
       "vRtrMplsLspTempSelfPing": vRtrMplsLspTempSelfPing,
       "vRtrMplsLspTempAddrFamily": vRtrMplsLspTempAddrFamily,
       "vRtrMplsLspTemplateEgrStatsMode": vRtrMplsLspTemplateEgrStatsMode,
       "vRtrMplsLspAutoBWTableLastChg": vRtrMplsLspAutoBWTableLastChg,
       "vRtrMplsLspAutoBandwidthTable": vRtrMplsLspAutoBandwidthTable,
       "vRtrMplsLspAutoBandwidthEntry": vRtrMplsLspAutoBandwidthEntry,
       "vRtrMplsLspAutoBWLspName": vRtrMplsLspAutoBWLspName,
       "vRtrMplsLspAutoBWLastChange": vRtrMplsLspAutoBWLastChange,
       "vRtrMplsLspAutoBWAdjDNPercent": vRtrMplsLspAutoBWAdjDNPercent,
       "vRtrMplsLspAutoBWAdjDNMbps": vRtrMplsLspAutoBWAdjDNMbps,
       "vRtrMplsLspAutoBWAdjMultiplier": vRtrMplsLspAutoBWAdjMultiplier,
       "vRtrMplsLspAutoBWAdjUPPercent": vRtrMplsLspAutoBWAdjUPPercent,
       "vRtrMplsLspAutoBWAdjUPMbps": vRtrMplsLspAutoBWAdjUPMbps,
       "vRtrMplsLspAutoBWMaxBW": vRtrMplsLspAutoBWMaxBW,
       "vRtrMplsLspAutoBWMinBW": vRtrMplsLspAutoBWMinBW,
       "vRtrMplsLspAutoBWMonitorBW": vRtrMplsLspAutoBWMonitorBW,
       "vRtrMplsLspAutoBWOverFlow": vRtrMplsLspAutoBWOverFlow,
       "vRtrMplsLspAutoBWOvrFlwThreshold": vRtrMplsLspAutoBWOvrFlwThreshold,
       "vRtrMplsLspAutoBWOvrFlwBW": vRtrMplsLspAutoBWOvrFlwBW,
       "vRtrMplsLspAutoBWSampMultiplier": vRtrMplsLspAutoBWSampMultiplier,
       "vRtrMplsLspAutoBWSampTime": vRtrMplsLspAutoBWSampTime,
       "vRtrMplsLspAutoBWLastAdj": vRtrMplsLspAutoBWLastAdj,
       "vRtrMplsLspAutoBWLastAdjCause": vRtrMplsLspAutoBWLastAdjCause,
       "vRtrMplsLspAutoBWNextAdj": vRtrMplsLspAutoBWNextAdj,
       "vRtrMplsLspAutoBWMaxAvgRate": vRtrMplsLspAutoBWMaxAvgRate,
       "vRtrMplsLspAutoBWLastAvgRate": vRtrMplsLspAutoBWLastAvgRate,
       "vRtrMplsLspAutoBWInheritance": vRtrMplsLspAutoBWInheritance,
       "vRtrMplsLspAutoBWCurrentBW": vRtrMplsLspAutoBWCurrentBW,
       "vRtrMplsLspAutoBWAdjTime": vRtrMplsLspAutoBWAdjTime,
       "vRtrMplsLspAutoBWOvrFlwCount": vRtrMplsLspAutoBWOvrFlwCount,
       "vRtrMplsLspAutoBWSampCount": vRtrMplsLspAutoBWSampCount,
       "vRtrMplsLspAutoBWAdjCount": vRtrMplsLspAutoBWAdjCount,
       "vRtrMplsLspAutoBWOperState": vRtrMplsLspAutoBWOperState,
       "vRtrMplsLspAutoBWSampInterval": vRtrMplsLspAutoBWSampInterval,
       "vRtrMplsLspAutoBWBeWeight": vRtrMplsLspAutoBWBeWeight,
       "vRtrMplsLspAutoBWL2Weight": vRtrMplsLspAutoBWL2Weight,
       "vRtrMplsLspAutoBWAfWeight": vRtrMplsLspAutoBWAfWeight,
       "vRtrMplsLspAutoBWL1Weight": vRtrMplsLspAutoBWL1Weight,
       "vRtrMplsLspAutoBWH2Weight": vRtrMplsLspAutoBWH2Weight,
       "vRtrMplsLspAutoBWEfWeight": vRtrMplsLspAutoBWEfWeight,
       "vRtrMplsLspAutoBWH1Weight": vRtrMplsLspAutoBWH1Weight,
       "vRtrMplsLspAutoBWNcWeight": vRtrMplsLspAutoBWNcWeight,
       "vRtrMplsLspAutoBWUnderFlow": vRtrMplsLspAutoBWUnderFlow,
       "vRtrMplsLspAutoBWUndFlwThreshold": vRtrMplsLspAutoBWUndFlwThreshold,
       "vRtrMplsLspAutoBWUndFlwBW": vRtrMplsLspAutoBWUndFlwBW,
       "vRtrMplsLspAutoBWUndFlwCount": vRtrMplsLspAutoBWUndFlwCount,
       "vRtrMplsLspAutoBWMaxUndFlwBw": vRtrMplsLspAutoBWMaxUndFlwBw,
       "vRtrMplsLspAutoBWUseLastAdjBW": vRtrMplsLspAutoBWUseLastAdjBW,
       "vRtrMplsLspAutoBWSecRetryLimit": vRtrMplsLspAutoBWSecRetryLimit,
       "vRtrMplsLspAutoBWLastAdjBW": vRtrMplsLspAutoBWLastAdjBW,
       "vRtrMplsLspPathOperTable": vRtrMplsLspPathOperTable,
       "vRtrMplsLspPathOperEntry": vRtrMplsLspPathOperEntry,
       "vRtrMplsLspPathOperSetupPriority": vRtrMplsLspPathOperSetupPriority,
       "vRtrMplsLspPathOperHoldPriority": vRtrMplsLspPathOperHoldPriority,
       "vRtrMplsLspPathOperRecord": vRtrMplsLspPathOperRecord,
       "vRtrMplsLspPathOperRecordLabel": vRtrMplsLspPathOperRecordLabel,
       "vRtrMplsLspPathOperHopLimit": vRtrMplsLspPathOperHopLimit,
       "vRtrMplsLspPathOperAdminGrpIncl": vRtrMplsLspPathOperAdminGrpIncl,
       "vRtrMplsLspPathOperAdminGrExcld": vRtrMplsLspPathOperAdminGrExcld,
       "vRtrMplsLspPathOperCspf": vRtrMplsLspPathOperCspf,
       "vRtrMplsLspPathOperCspfToFrstLs": vRtrMplsLspPathOperCspfToFrstLs,
       "vRtrMplsLspPathOperLeastFill": vRtrMplsLspPathOperLeastFill,
       "vRtrMplsLspPathOperRsvpAdspec": vRtrMplsLspPathOperRsvpAdspec,
       "vRtrMplsLspPathOperFRNodeProtect": vRtrMplsLspPathOperFRNodeProtect,
       "vRtrMplsLspPathOperPropAdminGrp": vRtrMplsLspPathOperPropAdminGrp,
       "vRtrMplsLspPathOperFRHopLimit": vRtrMplsLspPathOperFRHopLimit,
       "vRtrMplsLspPathOperFRPropAdmGrp": vRtrMplsLspPathOperFRPropAdmGrp,
       "vRtrMplsLspPathOperInterArea": vRtrMplsLspPathOperInterArea,
       "vRtrMplsLspPathOperCompMeth": vRtrMplsLspPathOperCompMeth,
       "vRtrMplsLspPathOperMetricType": vRtrMplsLspPathOperMetricType,
       "vRtrMplsLspPathOperLocalSrProt": vRtrMplsLspPathOperLocalSrProt,
       "vRtrMplsLspPathOperLabelStackRed": vRtrMplsLspPathOperLabelStackRed,
       "vRtrMplsLspPathNgFNAddrType": vRtrMplsLspPathNgFNAddrType,
       "vRtrMplsLspPathNgFNAddr": vRtrMplsLspPathNgFNAddr,
       "vRtrMplsLabelObjs": vRtrMplsLabelObjs,
       "vRtrMplsLabelMaxStaticLspLabels": vRtrMplsLabelMaxStaticLspLabels,
       "vRtrMplsLabelMaxStaticSvcLabels": vRtrMplsLabelMaxStaticSvcLabels,
       "vRtrMplsLabelBgpLabelsHoldTimer": vRtrMplsLabelBgpLabelsHoldTimer,
       "vRtrMplsLabelSegRouteStartLabel": vRtrMplsLabelSegRouteStartLabel,
       "vRtrMplsLabelSegRouteEndLabel": vRtrMplsLabelSegRouteEndLabel,
       "vRtrMplsLabelStaticLabelRange": vRtrMplsLabelStaticLabelRange,
       "vRtrMplsLspTempAutoBWTblLastChg": vRtrMplsLspTempAutoBWTblLastChg,
       "vRtrMplsLspTempAutoBWTable": vRtrMplsLspTempAutoBWTable,
       "vRtrMplsLspTempAutoBWEntry": vRtrMplsLspTempAutoBWEntry,
       "vRtrMplsLspTempAutoBWLastChg": vRtrMplsLspTempAutoBWLastChg,
       "vRtrMplsLspTempAutoBWAdjDNPer": vRtrMplsLspTempAutoBWAdjDNPer,
       "vRtrMplsLspTempAutoBWAdjDNMbps": vRtrMplsLspTempAutoBWAdjDNMbps,
       "vRtrMplsLspTempAutoBWAdjUPPer": vRtrMplsLspTempAutoBWAdjUPPer,
       "vRtrMplsLspTempAutoBWAdjUPMbps": vRtrMplsLspTempAutoBWAdjUPMbps,
       "vRtrMplsLspTempAutoBWMaxBW": vRtrMplsLspTempAutoBWMaxBW,
       "vRtrMplsLspTempAutoBWMinBW": vRtrMplsLspTempAutoBWMinBW,
       "vRtrMplsLspTempAutoBWMntrBW": vRtrMplsLspTempAutoBWMntrBW,
       "vRtrMplsLspTempAutoBWAdjMult": vRtrMplsLspTempAutoBWAdjMult,
       "vRtrMplsLspTempAutoBWOverFlow": vRtrMplsLspTempAutoBWOverFlow,
       "vRtrMplsLspTempAutoBWOvrFlwThr": vRtrMplsLspTempAutoBWOvrFlwThr,
       "vRtrMplsLspTempAutoBWOvrFlwBW": vRtrMplsLspTempAutoBWOvrFlwBW,
       "vRtrMplsLspTempAutoBWSampMult": vRtrMplsLspTempAutoBWSampMult,
       "vRtrMplsLspTempAutoBWSampTime": vRtrMplsLspTempAutoBWSampTime,
       "vRtrMplsLspTempAutoBWInherit": vRtrMplsLspTempAutoBWInherit,
       "vRtrMplsLspTempAutoBWBeWeight": vRtrMplsLspTempAutoBWBeWeight,
       "vRtrMplsLspTempAutoBWL2Weight": vRtrMplsLspTempAutoBWL2Weight,
       "vRtrMplsLspTempAutoBWAfWeight": vRtrMplsLspTempAutoBWAfWeight,
       "vRtrMplsLspTempAutoBWL1Weight": vRtrMplsLspTempAutoBWL1Weight,
       "vRtrMplsLspTempAutoBWH2Weight": vRtrMplsLspTempAutoBWH2Weight,
       "vRtrMplsLspTempAutoBWEfWeight": vRtrMplsLspTempAutoBWEfWeight,
       "vRtrMplsLspTempAutoBWH1Weight": vRtrMplsLspTempAutoBWH1Weight,
       "vRtrMplsLspTempAutoBWNcWeight": vRtrMplsLspTempAutoBWNcWeight,
       "vRtrMplsLspTempAutoBWUnderFlow": vRtrMplsLspTempAutoBWUnderFlow,
       "vRtrMplsLspTempAutoBWUndFlwThr": vRtrMplsLspTempAutoBWUndFlwThr,
       "vRtrMplsLspTempAutoBWUndFlwBW": vRtrMplsLspTempAutoBWUndFlwBW,
       "vRtrMplsTemplPlcyBindTblLastChg": vRtrMplsTemplPlcyBindTblLastChg,
       "vRtrMplsLspTemplPlcyBindTable": vRtrMplsLspTemplPlcyBindTable,
       "vRtrMplsLspTemplPlcyBindEntry": vRtrMplsLspTemplPlcyBindEntry,
       "vRtrMplsLspTemplPlcyBindLastChg": vRtrMplsLspTemplPlcyBindLastChg,
       "vRtrMplsLspTemplPlcyBindRowStat": vRtrMplsLspTemplPlcyBindRowStat,
       "vRtrMplsLspTemplPlcyBind1": vRtrMplsLspTemplPlcyBind1,
       "vRtrMplsLspTemplPlcyBind2": vRtrMplsLspTemplPlcyBind2,
       "vRtrMplsLspTemplPlcyBind3": vRtrMplsLspTemplPlcyBind3,
       "vRtrMplsLspTemplPlcyBind4": vRtrMplsLspTemplPlcyBind4,
       "vRtrMplsLspTemplPlcyBind5": vRtrMplsLspTemplPlcyBind5,
       "vRtrMplsLspTemplPlcyBindOneHop": vRtrMplsLspTemplPlcyBindOneHop,
       "vRtrMplsLspTempInStatTblLstChg": vRtrMplsLspTempInStatTblLstChg,
       "vRtrMplsLspTempInStatTable": vRtrMplsLspTempInStatTable,
       "vRtrMplsLspTempInStatEntry": vRtrMplsLspTempInStatEntry,
       "vRtrMplsLspTempInStatType": vRtrMplsLspTempInStatType,
       "vRtrMplsLspTempInStatSndrAddrTyp": vRtrMplsLspTempInStatSndrAddrTyp,
       "vRtrMplsLspTempInStatSndrAddr": vRtrMplsLspTempInStatSndrAddr,
       "vRtrMplsLspTempInStatLspNamePref": vRtrMplsLspTempInStatLspNamePref,
       "vRtrMplsLspTempInStatRowStatus": vRtrMplsLspTempInStatRowStatus,
       "vRtrMplsLspTempInStatLastChanged": vRtrMplsLspTempInStatLastChanged,
       "vRtrMplsLspTempInStatCollectStat": vRtrMplsLspTempInStatCollectStat,
       "vRtrMplsLspTempInStatAccntPolicy": vRtrMplsLspTempInStatAccntPolicy,
       "vRtrMplsLspTempInStatAdminState": vRtrMplsLspTempInStatAdminState,
       "vRtrMplsLspTempInStatMaxStats": vRtrMplsLspTempInStatMaxStats,
       "vRtrMplsLspTempInStatTotlSession": vRtrMplsLspTempInStatTotlSession,
       "vRtrMplsLspTempInStatsMode": vRtrMplsLspTempInStatsMode,
       "vRtrMplsLspExtTable": vRtrMplsLspExtTable,
       "vRtrMplsLspExtEntry": vRtrMplsLspExtEntry,
       "vRtrMplsLspExtPceCompute": vRtrMplsLspExtPceCompute,
       "vRtrMplsLspExtPceControl": vRtrMplsLspExtPceControl,
       "vRtrMplsLspExtPceReport": vRtrMplsLspExtPceReport,
       "vRtrMplsLspExtTtmTunnelId": vRtrMplsLspExtTtmTunnelId,
       "vRtrMplsLspExtMaxSrLabels": vRtrMplsLspExtMaxSrLabels,
       "vRtrMplsLspExtTunnelId": vRtrMplsLspExtTunnelId,
       "vRtrMplsLspExtEntropyLabel": vRtrMplsLspExtEntropyLabel,
       "vRtrMplsLspExtOperEntropyLabel": vRtrMplsLspExtOperEntropyLabel,
       "vRtrMplsLspExtFrrOverheadLabel": vRtrMplsLspExtFrrOverheadLabel,
       "vRtrMplsLspExtNegEntropyLbl": vRtrMplsLspExtNegEntropyLbl,
       "vRtrMplsLspExtBfdFailureAction": vRtrMplsLspExtBfdFailureAction,
       "vRtrMplsLspExtCbfFwdingPlcy": vRtrMplsLspExtCbfFwdingPlcy,
       "vRtrMplsLspExtCbfFwdingSet": vRtrMplsLspExtCbfFwdingSet,
       "vRtrMplsLspExtPathCompMeth": vRtrMplsLspExtPathCompMeth,
       "vRtrMplsLspExtMetricType": vRtrMplsLspExtMetricType,
       "vRtrMplsLspExtLocalSrProt": vRtrMplsLspExtLocalSrProt,
       "vRtrMplsLspExtLabelStackRed": vRtrMplsLspExtLabelStackRed,
       "vRtrMplsLspExtBfdUpWaitTimer": vRtrMplsLspExtBfdUpWaitTimer,
       "vRtrMplsLspExtSelfPing": vRtrMplsLspExtSelfPing,
       "vRtrMplsLspExtFallbkPathComp": vRtrMplsLspExtFallbkPathComp,
       "vRtrMplsLspExtTriggerManualSw": vRtrMplsLspExtTriggerManualSw,
       "vRtrMplsLspExtActivePathIndex": vRtrMplsLspExtActivePathIndex,
       "vRtrMplsLspExtOverrideTunElc": vRtrMplsLspExtOverrideTunElc,
       "vRtrMplsLspExtPrefTransFrr": vRtrMplsLspExtPrefTransFrr,
       "vRtrMplsLspExtBfdReturnPathLabel": vRtrMplsLspExtBfdReturnPathLabel,
       "vRtrMplsLspExtSoftPreemption": vRtrMplsLspExtSoftPreemption,
       "vRtrMplsLspPathProfTblLstChg": vRtrMplsLspPathProfTblLstChg,
       "vRtrMplsLspPathProfTable": vRtrMplsLspPathProfTable,
       "vRtrMplsLspPathProfEntry": vRtrMplsLspPathProfEntry,
       "vRtrMplsLspPathProfId": vRtrMplsLspPathProfId,
       "vRtrMplsLspPathProfRowStatus": vRtrMplsLspPathProfRowStatus,
       "vRtrMplsLspPathProfLastChange": vRtrMplsLspPathProfLastChange,
       "vRtrMplsLspPathProfGroupId": vRtrMplsLspPathProfGroupId,
       "vRtrMplsClassFwdPlcyTblLstChg": vRtrMplsClassFwdPlcyTblLstChg,
       "vRtrMplsClassFwdPlcyTable": vRtrMplsClassFwdPlcyTable,
       "vRtrMplsClassFwdPlcyEntry": vRtrMplsClassFwdPlcyEntry,
       "vRtrMplsClassFwdPlcyName": vRtrMplsClassFwdPlcyName,
       "vRtrMplsClassFwdPlcyRowStatus": vRtrMplsClassFwdPlcyRowStatus,
       "vRtrMplsClassFwdPlcyLastChanged": vRtrMplsClassFwdPlcyLastChanged,
       "vRtrMplsClassFwdPlcyDefSetId": vRtrMplsClassFwdPlcyDefSetId,
       "vRtrMplsClassFwdPlcyRefCount": vRtrMplsClassFwdPlcyRefCount,
       "vRtrMplsClassFwdPlcyFCTblLstChg": vRtrMplsClassFwdPlcyFCTblLstChg,
       "vRtrMplsClassFwdPlcyFCTable": vRtrMplsClassFwdPlcyFCTable,
       "vRtrMplsClassFwdPlcyFCEntry": vRtrMplsClassFwdPlcyFCEntry,
       "vRtrMplsClassFwdPlcyFC": vRtrMplsClassFwdPlcyFC,
       "vRtrMplsClassFwdPlcyFCSetId": vRtrMplsClassFwdPlcyFCSetId,
       "vRtrMplsReservedLblBlkTblLastChg": vRtrMplsReservedLblBlkTblLastChg,
       "vRtrMplsReservedLblBlkTable": vRtrMplsReservedLblBlkTable,
       "vRtrMplsReservedLblBlkEntry": vRtrMplsReservedLblBlkEntry,
       "vRtrMplsReservedLblBlkName": vRtrMplsReservedLblBlkName,
       "vRtrMplsReservedLblBlkRowStatus": vRtrMplsReservedLblBlkRowStatus,
       "vRtrMplsReservedLblBlkLastChg": vRtrMplsReservedLblBlkLastChg,
       "vRtrMplsReservedLblBlkStartLbl": vRtrMplsReservedLblBlkStartLbl,
       "vRtrMplsReservedLblBlkEndLbl": vRtrMplsReservedLblBlkEndLbl,
       "vRtrMplsLspAdminTagTblLastChg": vRtrMplsLspAdminTagTblLastChg,
       "vRtrMplsLspAdminTagTable": vRtrMplsLspAdminTagTable,
       "vRtrMplsLspAdminTagEntry": vRtrMplsLspAdminTagEntry,
       "vRtrMplsLspAdminTagName": vRtrMplsLspAdminTagName,
       "vRtrMplsLspAdminTagRowStatus": vRtrMplsLspAdminTagRowStatus,
       "vRtrMplsLspAdminTagLastChanged": vRtrMplsLspAdminTagLastChanged,
       "vRtrMplsLspTempAdminTagTblLstChg": vRtrMplsLspTempAdminTagTblLstChg,
       "vRtrMplsLspTempAdminTagTable": vRtrMplsLspTempAdminTagTable,
       "vRtrMplsLspTempAdminTagEntry": vRtrMplsLspTempAdminTagEntry,
       "vRtrMplsLspTempAdminTagName": vRtrMplsLspTempAdminTagName,
       "vRtrMplsLspTempAdminTagRowStatus": vRtrMplsLspTempAdminTagRowStatus,
       "vRtrMplsLspTempAdminTagLastChg": vRtrMplsLspTempAdminTagLastChg,
       "vRtrMplsFwdPlcyTblLastChg": vRtrMplsFwdPlcyTblLastChg,
       "vRtrMplsFwdPlcyTable": vRtrMplsFwdPlcyTable,
       "vRtrMplsFwdPlcyEntry": vRtrMplsFwdPlcyEntry,
       "vRtrMplsFwdPlcyName": vRtrMplsFwdPlcyName,
       "vRtrMplsFwdPlcyRowStatus": vRtrMplsFwdPlcyRowStatus,
       "vRtrMplsFwdPlcyLastChanged": vRtrMplsFwdPlcyLastChanged,
       "vRtrMplsFwdPlcyAdminState": vRtrMplsFwdPlcyAdminState,
       "vRtrMplsFwdPlcyOperState": vRtrMplsFwdPlcyOperState,
       "vRtrMplsFwdPlcyBindingLabel": vRtrMplsFwdPlcyBindingLabel,
       "vRtrMplsFwdPlcyEndpointAddrType": vRtrMplsFwdPlcyEndpointAddrType,
       "vRtrMplsFwdPlcyEndpointAddr": vRtrMplsFwdPlcyEndpointAddr,
       "vRtrMplsFwdPlcyRevertTimer": vRtrMplsFwdPlcyRevertTimer,
       "vRtrMplsFwdPlcyPreference": vRtrMplsFwdPlcyPreference,
       "vRtrMplsFwdPlcyMetric": vRtrMplsFwdPlcyMetric,
       "vRtrMplsFwdPlcyTtmPreference": vRtrMplsFwdPlcyTtmPreference,
       "vRtrMplsFwdPlcyNHGrpTblLastChg": vRtrMplsFwdPlcyNHGrpTblLastChg,
       "vRtrMplsFwdPlcyNHGrpTable": vRtrMplsFwdPlcyNHGrpTable,
       "vRtrMplsFwdPlcyNHGrpEntry": vRtrMplsFwdPlcyNHGrpEntry,
       "vRtrMplsFwdPlcyNHGrpIdx": vRtrMplsFwdPlcyNHGrpIdx,
       "vRtrMplsFwdPlcyNHGrpRowStatus": vRtrMplsFwdPlcyNHGrpRowStatus,
       "vRtrMplsFwdPlcyNHGrpLastChanged": vRtrMplsFwdPlcyNHGrpLastChanged,
       "vRtrMplsFwdPlcyNHGrpAdminState": vRtrMplsFwdPlcyNHGrpAdminState,
       "vRtrMplsFwdPlcyNHGrpOperState": vRtrMplsFwdPlcyNHGrpOperState,
       "vRtrMplsFwdPlcyNHGrpResType": vRtrMplsFwdPlcyNHGrpResType,
       "vRtrMplsFwdPlcyNHGrpLoadBalWt": vRtrMplsFwdPlcyNHGrpLoadBalWt,
       "vRtrMplsFwdPlcyNhgNHTblLastChg": vRtrMplsFwdPlcyNhgNHTblLastChg,
       "vRtrMplsFwdPlcyNhgNHTable": vRtrMplsFwdPlcyNhgNHTable,
       "vRtrMplsFwdPlcyNhgNHEntry": vRtrMplsFwdPlcyNhgNHEntry,
       "vRtrMplsFwdPlcyNhgNHType": vRtrMplsFwdPlcyNhgNHType,
       "vRtrMplsFwdPlcyNhgNHRowStatus": vRtrMplsFwdPlcyNhgNHRowStatus,
       "vRtrMplsFwdPlcyNhgNHLastChanged": vRtrMplsFwdPlcyNhgNHLastChanged,
       "vRtrMplsFwdPlcyNhgNHOperState": vRtrMplsFwdPlcyNhgNHOperState,
       "vRtrMplsFwdPlcyNhgNHAddrType": vRtrMplsFwdPlcyNhgNHAddrType,
       "vRtrMplsFwdPlcyNhgNHAddr": vRtrMplsFwdPlcyNhgNHAddr,
       "vRtrMplsFwdPlcyGenTblLastChg": vRtrMplsFwdPlcyGenTblLastChg,
       "vRtrMplsFwdPlcyGenTable": vRtrMplsFwdPlcyGenTable,
       "vRtrMplsFwdPlcyGenEntry": vRtrMplsFwdPlcyGenEntry,
       "vRtrMplsFwdPlcyGenRowStatus": vRtrMplsFwdPlcyGenRowStatus,
       "vRtrMplsFwdPlcyGenLastChanged": vRtrMplsFwdPlcyGenLastChanged,
       "vRtrMplsFwdPlcyGenAdminState": vRtrMplsFwdPlcyGenAdminState,
       "vRtrMplsFwdPlcyGenOperState": vRtrMplsFwdPlcyGenOperState,
       "vRtrMplsFwdPlcyGenOperDownReason": vRtrMplsFwdPlcyGenOperDownReason,
       "vRtrMplsFwdPlcyGenReservedLblBlk": vRtrMplsFwdPlcyGenReservedLblBlk,
       "vRtrMplsFwdPlcyStatsTblLastChg": vRtrMplsFwdPlcyStatsTblLastChg,
       "vRtrMplsFwdPlcyStatsTable": vRtrMplsFwdPlcyStatsTable,
       "vRtrMplsFwdPlcyStatsEntry": vRtrMplsFwdPlcyStatsEntry,
       "vRtrMplsFwdPlcyStatsType": vRtrMplsFwdPlcyStatsType,
       "vRtrMplsFwdPlcyStatsRowStatus": vRtrMplsFwdPlcyStatsRowStatus,
       "vRtrMplsFwdPlcyStatsLastChanged": vRtrMplsFwdPlcyStatsLastChanged,
       "vRtrMplsFwdPlcyStatsAdminState": vRtrMplsFwdPlcyStatsAdminState,
       "vRtrMplsBindLblPathTable": vRtrMplsBindLblPathTable,
       "vRtrMplsBindLblPathEntry": vRtrMplsBindLblPathEntry,
       "vRtrMplsBindLbl": vRtrMplsBindLbl,
       "vRtrMplsBindLblPathId": vRtrMplsBindLblPathId,
       "vRtrMplsBindLblPathOwner": vRtrMplsBindLblPathOwner,
       "vRtrMplsBindLblPathName": vRtrMplsBindLblPathName,
       "vRtrMplsBindLblPathOperState": vRtrMplsBindLblPathOperState,
       "vRtrMplsBindLblPathLastOperChg": vRtrMplsBindLblPathLastOperChg,
       "vRtrMplsBindLblOperDownReason": vRtrMplsBindLblOperDownReason,
       "vRtrMplsBindLblPathNumNHGrpCnt": vRtrMplsBindLblPathNumNHGrpCnt,
       "vRtrMplsBindLblPathRetryCount": vRtrMplsBindLblPathRetryCount,
       "vRtrMplsBindLblPathRetryTimeRem": vRtrMplsBindLblPathRetryTimeRem,
       "vRtrMplsBindLblPathRevertTimer": vRtrMplsBindLblPathRevertTimer,
       "vRtrMplsBindLblPathIngStatsEnabl": vRtrMplsBindLblPathIngStatsEnabl,
       "vRtrMplsBindLblPathPref": vRtrMplsBindLblPathPref,
       "vRtrMplsBLPathIngStatOperState": vRtrMplsBLPathIngStatOperState,
       "vRtrMplsBindLblPathEgrStatsEnabl": vRtrMplsBindLblPathEgrStatsEnabl,
       "vRtrMplsBLPathEgrStatOperState": vRtrMplsBLPathEgrStatOperState,
       "vRtrMplsBindLblPathNhgTable": vRtrMplsBindLblPathNhgTable,
       "vRtrMplsBindLblPathNhgEntry": vRtrMplsBindLblPathNhgEntry,
       "vRtrMplsBindLblPathNhgIndex": vRtrMplsBindLblPathNhgIndex,
       "vRtrMplsBindLblPathNhgOperState": vRtrMplsBindLblPathNhgOperState,
       "vRtrMplsBindLblPathNHgResType": vRtrMplsBindLblPathNHgResType,
       "vRtrMplsBindLblPathNhgLoadBalWt": vRtrMplsBindLblPathNhgLoadBalWt,
       "vRtrMplsBindLblPathNhgFailovrCnt": vRtrMplsBindLblPathNhgFailovrCnt,
       "vRtrMplsBindLblPathNhgRevertCnt": vRtrMplsBindLblPathNhgRevertCnt,
       "vRtrMplsBindLblPathNhgRevTimeRem": vRtrMplsBindLblPathNhgRevTimeRem,
       "vRtrMplsBindLblPathNhgDownReason": vRtrMplsBindLblPathNhgDownReason,
       "vRtrMplsBindLblPathNhgWeights": vRtrMplsBindLblPathNhgWeights,
       "vRtrMplsBindLblPathNhgNHTable": vRtrMplsBindLblPathNhgNHTable,
       "vRtrMplsBindLblPathNhgNHEntry": vRtrMplsBindLblPathNhgNHEntry,
       "vRtrMplsBindLblPathNhgNHType": vRtrMplsBindLblPathNhgNHType,
       "vRtrMplsBindLblPathNhgNHAddrType": vRtrMplsBindLblPathNhgNHAddrType,
       "vRtrMplsBindLblPathNhgNHAddr": vRtrMplsBindLblPathNhgNHAddr,
       "vRtrMplsBindLblPathNhgNHResolved": vRtrMplsBindLblPathNhgNHResolved,
       "vRtrMplsBindLblPathNhgNHOutIf": vRtrMplsBindLblPathNhgNHOutIf,
       "vRtrMplsBindLblPathNhgNHDownCode": vRtrMplsBindLblPathNhgNHDownCode,
       "vRtrMplsBindLblPathNhgNHEgrOper": vRtrMplsBindLblPathNhgNHEgrOper,
       "vRtrMplsBindLblIngrStatsTable": vRtrMplsBindLblIngrStatsTable,
       "vRtrMplsBindLblIngrStatsEntry": vRtrMplsBindLblIngrStatsEntry,
       "vRtrMplsBindLblIngrAggPkts": vRtrMplsBindLblIngrAggPkts,
       "vRtrMplsBindLblIngrAggOctets": vRtrMplsBindLblIngrAggOctets,
       "vRtrMplsEndptPathTable": vRtrMplsEndptPathTable,
       "vRtrMplsEndptPathEntry": vRtrMplsEndptPathEntry,
       "vRtrMplsEndptAddrType": vRtrMplsEndptAddrType,
       "vRtrMplsEndptAddress": vRtrMplsEndptAddress,
       "vRtrMplsEndptPathId": vRtrMplsEndptPathId,
       "vRtrMplsEndptPathOwner": vRtrMplsEndptPathOwner,
       "vRtrMplsEndptPathName": vRtrMplsEndptPathName,
       "vRtrMplsEndptPathOperState": vRtrMplsEndptPathOperState,
       "vRtrMplsEndptPathLastOperChg": vRtrMplsEndptPathLastOperChg,
       "vRtrMplsEndptPathOperDownReason": vRtrMplsEndptPathOperDownReason,
       "vRtrMplsEndptPathNHGrpCnt": vRtrMplsEndptPathNHGrpCnt,
       "vRtrMplsEndptPathRetryCount": vRtrMplsEndptPathRetryCount,
       "vRtrMplsEndptPathRetryTimeRem": vRtrMplsEndptPathRetryTimeRem,
       "vRtrMplsEndptPathRevertTimer": vRtrMplsEndptPathRevertTimer,
       "vRtrMplsEndptPathPref": vRtrMplsEndptPathPref,
       "vRtrMplsEndptPathTTMPref": vRtrMplsEndptPathTTMPref,
       "vRtrMplsEndptPathMetric": vRtrMplsEndptPathMetric,
       "vRtrMplsEndptPathEgrStatsEnabl": vRtrMplsEndptPathEgrStatsEnabl,
       "vRtrMplsEndptPathEgrStatsOper": vRtrMplsEndptPathEgrStatsOper,
       "vRtrMplsEndptPathNhgTable": vRtrMplsEndptPathNhgTable,
       "vRtrMplsEndptPathNhgEntry": vRtrMplsEndptPathNhgEntry,
       "vRtrMplsEndptPathNhgIndex": vRtrMplsEndptPathNhgIndex,
       "vRtrMplsEndptPathNhgOperState": vRtrMplsEndptPathNhgOperState,
       "vRtrMplsEndptPathNhgResType": vRtrMplsEndptPathNhgResType,
       "vRtrMplsEndptPathNhgLoadBalWt": vRtrMplsEndptPathNhgLoadBalWt,
       "vRtrMplsEndptPathNhgFailovrCnt": vRtrMplsEndptPathNhgFailovrCnt,
       "vRtrMplsEndptPathNhgRevertCnt": vRtrMplsEndptPathNhgRevertCnt,
       "vRtrMplsEndptPathNhgRevTimeRem": vRtrMplsEndptPathNhgRevTimeRem,
       "vRtrMplsEndptPathNhgDownReason": vRtrMplsEndptPathNhgDownReason,
       "vRtrMplsEndptPathNhgWeights": vRtrMplsEndptPathNhgWeights,
       "vRtrMplsEndptPathNhgNHTable": vRtrMplsEndptPathNhgNHTable,
       "vRtrMplsEndptPathNhgNHEntry": vRtrMplsEndptPathNhgNHEntry,
       "vRtrMplsEndptPathNhgNHType": vRtrMplsEndptPathNhgNHType,
       "vRtrMplsEndptPathNhgNHAddrType": vRtrMplsEndptPathNhgNHAddrType,
       "vRtrMplsEndptPathNhgNHAddr": vRtrMplsEndptPathNhgNHAddr,
       "vRtrMplsEndptPathNhgNHResolved": vRtrMplsEndptPathNhgNHResolved,
       "vRtrMplsEndptPathNhgNHOutIf": vRtrMplsEndptPathNhgNHOutIf,
       "vRtrMplsEndptPathNhgNHDownCode": vRtrMplsEndptPathNhgNHDownCode,
       "vRtrMplsEndptPathNhgNHEgrOper": vRtrMplsEndptPathNhgNHEgrOper,
       "vRtrMplsFwdPlcyNhgNHPushLblTable": vRtrMplsFwdPlcyNhgNHPushLblTable,
       "vRtrMplsFwdPlcyNhgNHPushLblEntry": vRtrMplsFwdPlcyNhgNHPushLblEntry,
       "vRtrMplsFwdPlcyNhgNHPushLabel1": vRtrMplsFwdPlcyNhgNHPushLabel1,
       "vRtrMplsFwdPlcyNhgNHPushLabel2": vRtrMplsFwdPlcyNhgNHPushLabel2,
       "vRtrMplsFwdPlcyNhgNHPushLabel3": vRtrMplsFwdPlcyNhgNHPushLabel3,
       "vRtrMplsFwdPlcyNhgNHPushLabel4": vRtrMplsFwdPlcyNhgNHPushLabel4,
       "vRtrMplsFwdPlcyNhgNHPushLabel5": vRtrMplsFwdPlcyNhgNHPushLabel5,
       "vRtrMplsFwdPlcyNhgNHPushLabel6": vRtrMplsFwdPlcyNhgNHPushLabel6,
       "vRtrMplsFwdPlcyNhgNHPushLabel7": vRtrMplsFwdPlcyNhgNHPushLabel7,
       "vRtrMplsFwdPlcyNhgNHPushLabel8": vRtrMplsFwdPlcyNhgNHPushLabel8,
       "vRtrMplsFwdPlcyNhgNHPushLabel9": vRtrMplsFwdPlcyNhgNHPushLabel9,
       "vRtrMplsFwdPlcyNhgNHPushLabel10": vRtrMplsFwdPlcyNhgNHPushLabel10,
       "vRtrMplsBindLblPathNhgNHPLTable": vRtrMplsBindLblPathNhgNHPLTable,
       "vRtrMplsBindLblPathNhgNHPLEntry": vRtrMplsBindLblPathNhgNHPLEntry,
       "vRtrMplsBindLblPathNHgNHPLIndex": vRtrMplsBindLblPathNHgNHPLIndex,
       "vRtrMplsBindLblPathNHgNHPLabel": vRtrMplsBindLblPathNHgNHPLabel,
       "vRtrMplsEndptPathNhgNHPLlbTable": vRtrMplsEndptPathNhgNHPLlbTable,
       "vRtrMplsEndptPathNhgNHPLlbEntry": vRtrMplsEndptPathNhgNHPLlbEntry,
       "vRtrMplsEndptPathNhgNHPLblIndex": vRtrMplsEndptPathNhgNHPLblIndex,
       "vRtrMplsEndptPathNhgNHPLabel": vRtrMplsEndptPathNhgNHPLabel,
       "vRtrMplsPceInitGenTblLastChg": vRtrMplsPceInitGenTblLastChg,
       "vRtrMplsPceInitGenTable": vRtrMplsPceInitGenTable,
       "vRtrMplsPceInitGenEntry": vRtrMplsPceInitGenEntry,
       "vRtrMplsPceInitGenRowStatus": vRtrMplsPceInitGenRowStatus,
       "vRtrMplsPceInitGenSrte": vRtrMplsPceInitGenSrte,
       "vRtrMplsPceInitGenSrteAdminState": vRtrMplsPceInitGenSrteAdminState,
       "vRtrMplsPceInitGenSrteOperState": vRtrMplsPceInitGenSrteOperState,
       "vRtrMplsPceInitGenSrteOperDnRsn": vRtrMplsPceInitGenSrteOperDnRsn,
       "vRtrMplsBindLblNHEgrStatsTable": vRtrMplsBindLblNHEgrStatsTable,
       "vRtrMplsBindLblNHEgrStatsEntry": vRtrMplsBindLblNHEgrStatsEntry,
       "vRtrMplsBindLblEgrStatsAggPkts": vRtrMplsBindLblEgrStatsAggPkts,
       "vRtrMplsBindLblEgrStatsAggOctets": vRtrMplsBindLblEgrStatsAggOctets,
       "vRtrMplsEndptNHEgrStatsTable": vRtrMplsEndptNHEgrStatsTable,
       "vRtrMplsEndptNHEgrStatsEntry": vRtrMplsEndptNHEgrStatsEntry,
       "vRtrMplsEndptEgrStatsAggPkts": vRtrMplsEndptEgrStatsAggPkts,
       "vRtrMplsEndptEgrStatsAggOctets": vRtrMplsEndptEgrStatsAggOctets,
       "vRtrMplsLspPathEgressStatsTable": vRtrMplsLspPathEgressStatsTable,
       "vRtrMplsLspPathEgressStatsEntry": vRtrMplsLspPathEgressStatsEntry,
       "vRtrMplsLspPathEgrStatsOperState": vRtrMplsLspPathEgrStatsOperState,
       "vRtrMplsLspEgressStatsAggrPkts": vRtrMplsLspEgressStatsAggrPkts,
       "vRtrMplsLspEgressStatsAggrOctets": vRtrMplsLspEgressStatsAggrOctets,
       "vRtrMplsPathHopTableLastChg": vRtrMplsPathHopTableLastChg,
       "vRtrMplsPathHopTable": vRtrMplsPathHopTable,
       "vRtrMplsPathHopEntry": vRtrMplsPathHopEntry,
       "vRtrMplsPathIndex": vRtrMplsPathIndex,
       "vRtrMplsPathHopIndex": vRtrMplsPathHopIndex,
       "vRtrMplsPathHopRowStatus": vRtrMplsPathHopRowStatus,
       "vRtrMplsPathHopLastChange": vRtrMplsPathHopLastChange,
       "vRtrMplsPathHopAddrType": vRtrMplsPathHopAddrType,
       "vRtrMplsPathHopAddr": vRtrMplsPathHopAddr,
       "vRtrMplsPathHopStrictOrLoose": vRtrMplsPathHopStrictOrLoose,
       "vRtrMplsPathHopSidLabel": vRtrMplsPathHopSidLabel,
       "vRtrMplsLspTemplateExtTable": vRtrMplsLspTemplateExtTable,
       "vRtrMplsLspTemplateExtEntry": vRtrMplsLspTemplateExtEntry,
       "vRtrMplsLspTempExtFallbkPathComp": vRtrMplsLspTempExtFallbkPathComp,
       "vRtrMplsLspTempExtPceControl": vRtrMplsLspTempExtPceControl,
       "vRtrMplsLspTempExtOverrideTunElc": vRtrMplsLspTempExtOverrideTunElc,
       "vRtrMplsLspTempExtPrefTransFrr": vRtrMplsLspTempExtPrefTransFrr,
       "vRtrMplsLspTempExtReturnPathLbl": vRtrMplsLspTempExtReturnPathLbl,
       "vRtrMplsLspTempExtSoftPreemption": vRtrMplsLspTempExtSoftPreemption,
       "vRtrMplsLspTempPathProTblLastChg": vRtrMplsLspTempPathProTblLastChg,
       "vRtrMplsLspTempPathProfTable": vRtrMplsLspTempPathProfTable,
       "vRtrMplsLspTempPathProfEntry": vRtrMplsLspTempPathProfEntry,
       "vRtrMplsLspTempPathProfId": vRtrMplsLspTempPathProfId,
       "vRtrMplsLspTempPathProfRowStatus": vRtrMplsLspTempPathProfRowStatus,
       "vRtrMplsLspTempPathProfLastChg": vRtrMplsLspTempPathProfLastChg,
       "vRtrMplsLspTempPathProfGroupId": vRtrMplsLspTempPathProfGroupId,
       "tmnxMplsNotifyPrefix": tmnxMplsNotifyPrefix,
       "tmnxMplsNotifications": tmnxMplsNotifications,
       "vRtrMplsStateChange": vRtrMplsStateChange,
       "vRtrMplsIfStateChange": vRtrMplsIfStateChange,
       "vRtrMplsLspUp": vRtrMplsLspUp,
       "vRtrMplsLspDown": vRtrMplsLspDown,
       "vRtrMplsLspPathUp": vRtrMplsLspPathUp,
       "vRtrMplsLspPathDown": vRtrMplsLspPathDown,
       "vRtrMplsLspPathRerouted": vRtrMplsLspPathRerouted,
       "vRtrMplsLspPathResignaled": vRtrMplsLspPathResignaled,
       "vRtrMplsP2mpInstanceUp": vRtrMplsP2mpInstanceUp,
       "vRtrMplsP2mpInstanceDown": vRtrMplsP2mpInstanceDown,
       "vRtrMplsS2lSubLspUp": vRtrMplsS2lSubLspUp,
       "vRtrMplsS2lSubLspDown": vRtrMplsS2lSubLspDown,
       "vRtrMplsS2lSubLspRerouted": vRtrMplsS2lSubLspRerouted,
       "vRtrMplsS2lSubLspResignaled": vRtrMplsS2lSubLspResignaled,
       "vRtrMplsLspPathSoftPreempted": vRtrMplsLspPathSoftPreempted,
       "vRtrMplsLspPathLstFillReoptElig": vRtrMplsLspPathLstFillReoptElig,
       "vRtrMplsP2mpInstanceResignaled": vRtrMplsP2mpInstanceResignaled,
       "vRtrMplsResignalTimerExpired": vRtrMplsResignalTimerExpired,
       "vRtrMplsLspPathMbbStatusEvent": vRtrMplsLspPathMbbStatusEvent,
       "vRtrMplsLspSwitchStbyFailure": vRtrMplsLspSwitchStbyFailure,
       "vRtrMplsLspActivePathChanged": vRtrMplsLspActivePathChanged,
       "vRtrMplsXCBundleChange": vRtrMplsXCBundleChange,
       "vRtrMplsLblRangeModify": vRtrMplsLblRangeModify,
       "vRtrMplsNodeInIgpOverload": vRtrMplsNodeInIgpOverload,
       "vRtrMplsIPv6StateChange": vRtrMplsIPv6StateChange,
       "vRtrMplsIfIPv6StateChange": vRtrMplsIfIPv6StateChange,
       "vRtrMplsLspResourceExhaustion": vRtrMplsLspResourceExhaustion,
       "vRtrMplsLspManualSwitchFailure": vRtrMplsLspManualSwitchFailure,
       "vRtrMplsLspPathManualDegStateChg": vRtrMplsLspPathManualDegStateChg,
       "vRtrMplsS2lSubLspPreempted": vRtrMplsS2lSubLspPreempted}
)
