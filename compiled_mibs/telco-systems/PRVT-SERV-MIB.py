# SNMP MIB module (PRVT-SERV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-SERV-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:50 2025
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

(TNamedItem,
 TNamedItemOrEmpty,
 TNetworkPolicyIdOrNone,
 TSapEgressPolicyIdOrNone,
 TSapIngressPolicyIdOrNone,
 serviceAccessSwitch) = mibBuilder.importSymbols(
    "PRVT-QOS-MIB",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TNetworkPolicyIdOrNone",
    "TSapEgressPolicyIdOrNone",
    "TSapIngressPolicyIdOrNone",
    "serviceAccessSwitch")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

prvtServicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2)
)
if mibBuilder.loadTexts:
    prvtServicesMIB.setRevisions(
        ("2009-08-07 00:00",
         "2009-03-26 00:00",
         "2009-03-24 00:00",
         "2009-02-17 00:00",
         "2008-10-09 00:00",
         "2008-04-10 00:00",
         "2008-03-06 00:00",
         "2008-01-11 00:00",
         "2008-01-09 00:00",
         "2008-01-07 00:00",
         "2007-06-28 00:00",
         "2006-09-02 00:00",
         "2006-07-02 00:00",
         "2006-02-04 00:00",
         "2005-11-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ServiceAdminStatus(TextualConvention, Integer32):
    status = "current"
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



class ServiceOperStatus(TextualConvention, Integer32):
    status = "current"
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



class ServObjName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class ServObjDesc(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class ServType(TextualConvention, Integer32):
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
        *(("epipe", 1),
          ("p3pipe", 2),
          ("tls", 3),
          ("vprn", 4),
          ("ies", 5),
          ("mirror", 6),
          ("apipe", 7),
          ("fpipe", 8),
          ("vpws", 9),
          ("vpls-pe", 10),
          ("vpls-mtu", 11))
    )



class VpnId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



class SdpIdType(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 17407),
    )



class TMEncapVal(TextualConvention, Unsigned32):
    status = "current"


class TSapEgrQueueId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class TSapIngQueueId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )



# MIB Managed Objects in the order of their OIDs

_PrvtTMServObjs_ObjectIdentity = ObjectIdentity
prvtTMServObjs = _PrvtTMServObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1)
)
_PrvtTMCustObjs_ObjectIdentity = ObjectIdentity
prvtTMCustObjs = _PrvtTMCustObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1)
)
_CustNumEntries_Type = Integer32
_CustNumEntries_Object = MibScalar
custNumEntries = _CustNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 1),
    _CustNumEntries_Type()
)
custNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custNumEntries.setStatus("current")
_CustInfoTable_Object = MibTable
custInfoTable = _CustInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    custInfoTable.setStatus("current")
_CustInfoEntry_Object = MibTableRow
custInfoEntry = _CustInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 2, 1)
)
custInfoEntry.setIndexNames(
    (0, "PRVT-SERV-MIB", "custName"),
)
if mibBuilder.loadTexts:
    custInfoEntry.setStatus("current")


class _CustName_Type(ServObjName):
    """Custom type custName based on ServObjName"""
    defaultValue = OctetString("")


_CustName_Type.__name__ = "ServObjName"
_CustName_Object = MibTableColumn
custName = _CustName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 2, 1, 1),
    _CustName_Type()
)
custName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custName.setStatus("current")
_CustRowStatus_Type = RowStatus
_CustRowStatus_Object = MibTableColumn
custRowStatus = _CustRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 2, 1, 2),
    _CustRowStatus_Type()
)
custRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custRowStatus.setStatus("current")


class _CustContact_Type(ServObjDesc):
    """Custom type custContact based on ServObjDesc"""
    defaultValue = OctetString("")


_CustContact_Type.__name__ = "ServObjDesc"
_CustContact_Object = MibTableColumn
custContact = _CustContact_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 2, 1, 3),
    _CustContact_Type()
)
custContact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custContact.setStatus("current")


class _CustPhone_Type(ServObjDesc):
    """Custom type custPhone based on ServObjDesc"""
    defaultValue = OctetString("")


_CustPhone_Type.__name__ = "ServObjDesc"
_CustPhone_Object = MibTableColumn
custPhone = _CustPhone_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 2, 1, 4),
    _CustPhone_Type()
)
custPhone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custPhone.setStatus("current")
_CustLastMgmtChange_Type = TimeStamp
_CustLastMgmtChange_Object = MibTableColumn
custLastMgmtChange = _CustLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 2, 1, 5),
    _CustLastMgmtChange_Type()
)
custLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custLastMgmtChange.setStatus("current")
_CustMultiServiceSiteTable_Object = MibTable
custMultiServiceSiteTable = _CustMultiServiceSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    custMultiServiceSiteTable.setStatus("current")
_CustMultiServiceSiteEntry_Object = MibTableRow
custMultiServiceSiteEntry = _CustMultiServiceSiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 3, 1)
)
custMultiServiceSiteEntry.setIndexNames(
    (0, "PRVT-SERV-MIB", "custMultSvcSiteName"),
)
if mibBuilder.loadTexts:
    custMultiServiceSiteEntry.setStatus("current")


class _CustMultSvcSiteName_Type(DisplayString):
    """Custom type custMultSvcSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_CustMultSvcSiteName_Type.__name__ = "DisplayString"
_CustMultSvcSiteName_Object = MibTableColumn
custMultSvcSiteName = _CustMultSvcSiteName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 3, 1, 1),
    _CustMultSvcSiteName_Type()
)
custMultSvcSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMultSvcSiteName.setStatus("current")
_CustMultSvcSiteRowStatus_Type = RowStatus
_CustMultSvcSiteRowStatus_Object = MibTableColumn
custMultSvcSiteRowStatus = _CustMultSvcSiteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 3, 1, 2),
    _CustMultSvcSiteRowStatus_Type()
)
custMultSvcSiteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMultSvcSiteRowStatus.setStatus("current")


class _CustMultSvcSiteDescription_Type(ServObjDesc):
    """Custom type custMultSvcSiteDescription based on ServObjDesc"""
    defaultHexValue = ""


_CustMultSvcSiteDescription_Type.__name__ = "ServObjDesc"
_CustMultSvcSiteDescription_Object = MibTableColumn
custMultSvcSiteDescription = _CustMultSvcSiteDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 3, 1, 3),
    _CustMultSvcSiteDescription_Type()
)
custMultSvcSiteDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMultSvcSiteDescription.setStatus("current")


class _CustMultSvcSiteIngressSchedulerPolicy_Type(ServObjName):
    """Custom type custMultSvcSiteIngressSchedulerPolicy based on ServObjName"""
    defaultHexValue = ""


_CustMultSvcSiteIngressSchedulerPolicy_Type.__name__ = "ServObjName"
_CustMultSvcSiteIngressSchedulerPolicy_Object = MibTableColumn
custMultSvcSiteIngressSchedulerPolicy = _CustMultSvcSiteIngressSchedulerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 3, 1, 4),
    _CustMultSvcSiteIngressSchedulerPolicy_Type()
)
custMultSvcSiteIngressSchedulerPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMultSvcSiteIngressSchedulerPolicy.setStatus("current")


class _CustMultSvcSiteEgressSchedulerPolicy_Type(ServObjName):
    """Custom type custMultSvcSiteEgressSchedulerPolicy based on ServObjName"""
    defaultHexValue = ""


_CustMultSvcSiteEgressSchedulerPolicy_Type.__name__ = "ServObjName"
_CustMultSvcSiteEgressSchedulerPolicy_Object = MibTableColumn
custMultSvcSiteEgressSchedulerPolicy = _CustMultSvcSiteEgressSchedulerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 3, 1, 5),
    _CustMultSvcSiteEgressSchedulerPolicy_Type()
)
custMultSvcSiteEgressSchedulerPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMultSvcSiteEgressSchedulerPolicy.setStatus("current")
_CustMultSvcSiteLastMgmtChange_Type = TimeStamp
_CustMultSvcSiteLastMgmtChange_Object = MibTableColumn
custMultSvcSiteLastMgmtChange = _CustMultSvcSiteLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 3, 1, 6),
    _CustMultSvcSiteLastMgmtChange_Type()
)
custMultSvcSiteLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMultSvcSiteLastMgmtChange.setStatus("current")
_CustMultiSvcSiteIngQosSchedStatsTable_Object = MibTable
custMultiSvcSiteIngQosSchedStatsTable = _CustMultiSvcSiteIngQosSchedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    custMultiSvcSiteIngQosSchedStatsTable.setStatus("current")
_CustMultiSvcSiteIngQosSchedStatsEntry_Object = MibTableRow
custMultiSvcSiteIngQosSchedStatsEntry = _CustMultiSvcSiteIngQosSchedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 4, 1)
)
custMultiSvcSiteIngQosSchedStatsEntry.setIndexNames(
    (0, "PRVT-SERV-MIB", "custMultSvcSiteName"),
    (1, "PRVT-SERV-MIB", "custIngQosSchedName"),
)
if mibBuilder.loadTexts:
    custMultiSvcSiteIngQosSchedStatsEntry.setStatus("current")
_CustIngQosSchedName_Type = TNamedItem
_CustIngQosSchedName_Object = MibTableColumn
custIngQosSchedName = _CustIngQosSchedName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 4, 1, 1),
    _CustIngQosSchedName_Type()
)
custIngQosSchedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custIngQosSchedName.setStatus("current")
_CustIngQosSchedStatsForwardedPackets_Type = Counter32
_CustIngQosSchedStatsForwardedPackets_Object = MibTableColumn
custIngQosSchedStatsForwardedPackets = _CustIngQosSchedStatsForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 4, 1, 2),
    _CustIngQosSchedStatsForwardedPackets_Type()
)
custIngQosSchedStatsForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custIngQosSchedStatsForwardedPackets.setStatus("current")
_CustIngQosSchedStatsForwardedOctets_Type = Counter32
_CustIngQosSchedStatsForwardedOctets_Object = MibTableColumn
custIngQosSchedStatsForwardedOctets = _CustIngQosSchedStatsForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 4, 1, 3),
    _CustIngQosSchedStatsForwardedOctets_Type()
)
custIngQosSchedStatsForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custIngQosSchedStatsForwardedOctets.setStatus("current")
_CustMultiSvcSiteEgrQosSchedStatsTable_Object = MibTable
custMultiSvcSiteEgrQosSchedStatsTable = _CustMultiSvcSiteEgrQosSchedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    custMultiSvcSiteEgrQosSchedStatsTable.setStatus("current")
_CustMultiSvcSiteEgrQosSchedStatsEntry_Object = MibTableRow
custMultiSvcSiteEgrQosSchedStatsEntry = _CustMultiSvcSiteEgrQosSchedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 5, 1)
)
custMultiSvcSiteEgrQosSchedStatsEntry.setIndexNames(
    (0, "PRVT-SERV-MIB", "custMultSvcSiteName"),
    (1, "PRVT-SERV-MIB", "custEgrQosSchedName"),
)
if mibBuilder.loadTexts:
    custMultiSvcSiteEgrQosSchedStatsEntry.setStatus("current")
_CustEgrQosSchedName_Type = TNamedItem
_CustEgrQosSchedName_Object = MibTableColumn
custEgrQosSchedName = _CustEgrQosSchedName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 5, 1, 1),
    _CustEgrQosSchedName_Type()
)
custEgrQosSchedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custEgrQosSchedName.setStatus("current")
_CustEgrQosSchedStatsForwardedPackets_Type = Counter32
_CustEgrQosSchedStatsForwardedPackets_Object = MibTableColumn
custEgrQosSchedStatsForwardedPackets = _CustEgrQosSchedStatsForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 5, 1, 2),
    _CustEgrQosSchedStatsForwardedPackets_Type()
)
custEgrQosSchedStatsForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custEgrQosSchedStatsForwardedPackets.setStatus("current")
_CustEgrQosSchedStatsForwardedOctets_Type = Counter32
_CustEgrQosSchedStatsForwardedOctets_Object = MibTableColumn
custEgrQosSchedStatsForwardedOctets = _CustEgrQosSchedStatsForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 5, 1, 3),
    _CustEgrQosSchedStatsForwardedOctets_Type()
)
custEgrQosSchedStatsForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custEgrQosSchedStatsForwardedOctets.setStatus("current")
_CustIngQosPortIdSchedStatsTable_Object = MibTable
custIngQosPortIdSchedStatsTable = _CustIngQosPortIdSchedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    custIngQosPortIdSchedStatsTable.setStatus("current")
_CustIngQosPortIdSchedStatsEntry_Object = MibTableRow
custIngQosPortIdSchedStatsEntry = _CustIngQosPortIdSchedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 6, 1)
)
custIngQosPortIdSchedStatsEntry.setIndexNames(
    (0, "PRVT-SERV-MIB", "custMultSvcSiteName"),
    (0, "PRVT-SERV-MIB", "custIngQosPortIdSchedName"),
    (0, "PRVT-SERV-MIB", "custIngQosAssignmentPortId"),
)
if mibBuilder.loadTexts:
    custIngQosPortIdSchedStatsEntry.setStatus("current")
_CustIngQosPortIdSchedName_Type = TNamedItem
_CustIngQosPortIdSchedName_Object = MibTableColumn
custIngQosPortIdSchedName = _CustIngQosPortIdSchedName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 6, 1, 1),
    _CustIngQosPortIdSchedName_Type()
)
custIngQosPortIdSchedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custIngQosPortIdSchedName.setStatus("current")


class _CustIngQosAssignmentPortId_Type(Integer32):
    """Custom type custIngQosAssignmentPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CustIngQosAssignmentPortId_Type.__name__ = "Integer32"
_CustIngQosAssignmentPortId_Object = MibTableColumn
custIngQosAssignmentPortId = _CustIngQosAssignmentPortId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 6, 1, 2),
    _CustIngQosAssignmentPortId_Type()
)
custIngQosAssignmentPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custIngQosAssignmentPortId.setStatus("current")
_CustIngQosPortSchedFwdPkts_Type = Counter32
_CustIngQosPortSchedFwdPkts_Object = MibTableColumn
custIngQosPortSchedFwdPkts = _CustIngQosPortSchedFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 6, 1, 3),
    _CustIngQosPortSchedFwdPkts_Type()
)
custIngQosPortSchedFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custIngQosPortSchedFwdPkts.setStatus("current")
_CustIngQosPortSchedFwdOctets_Type = Counter32
_CustIngQosPortSchedFwdOctets_Object = MibTableColumn
custIngQosPortSchedFwdOctets = _CustIngQosPortSchedFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 6, 1, 4),
    _CustIngQosPortSchedFwdOctets_Type()
)
custIngQosPortSchedFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custIngQosPortSchedFwdOctets.setStatus("current")
_CustEgrQosPortIdSchedStatsTable_Object = MibTable
custEgrQosPortIdSchedStatsTable = _CustEgrQosPortIdSchedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 7)
)
if mibBuilder.loadTexts:
    custEgrQosPortIdSchedStatsTable.setStatus("current")
_CustEgrQosPortIdSchedStatsEntry_Object = MibTableRow
custEgrQosPortIdSchedStatsEntry = _CustEgrQosPortIdSchedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 7, 1)
)
custEgrQosPortIdSchedStatsEntry.setIndexNames(
    (0, "PRVT-SERV-MIB", "custMultSvcSiteName"),
    (0, "PRVT-SERV-MIB", "custEgrQosPortIdSchedName"),
    (0, "PRVT-SERV-MIB", "custEgrQosAssignmentPortId"),
)
if mibBuilder.loadTexts:
    custEgrQosPortIdSchedStatsEntry.setStatus("current")
_CustEgrQosPortIdSchedName_Type = TNamedItem
_CustEgrQosPortIdSchedName_Object = MibTableColumn
custEgrQosPortIdSchedName = _CustEgrQosPortIdSchedName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 7, 1, 1),
    _CustEgrQosPortIdSchedName_Type()
)
custEgrQosPortIdSchedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custEgrQosPortIdSchedName.setStatus("current")


class _CustEgrQosAssignmentPortId_Type(Integer32):
    """Custom type custEgrQosAssignmentPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CustEgrQosAssignmentPortId_Type.__name__ = "Integer32"
_CustEgrQosAssignmentPortId_Object = MibTableColumn
custEgrQosAssignmentPortId = _CustEgrQosAssignmentPortId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 7, 1, 2),
    _CustEgrQosAssignmentPortId_Type()
)
custEgrQosAssignmentPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custEgrQosAssignmentPortId.setStatus("current")
_CustEgrQosPortSchedFwdPkts_Type = Counter32
_CustEgrQosPortSchedFwdPkts_Object = MibTableColumn
custEgrQosPortSchedFwdPkts = _CustEgrQosPortSchedFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 7, 1, 3),
    _CustEgrQosPortSchedFwdPkts_Type()
)
custEgrQosPortSchedFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custEgrQosPortSchedFwdPkts.setStatus("current")
_CustEgrQosPortSchedFwdOctets_Type = Counter32
_CustEgrQosPortSchedFwdOctets_Object = MibTableColumn
custEgrQosPortSchedFwdOctets = _CustEgrQosPortSchedFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 1, 7, 1, 4),
    _CustEgrQosPortSchedFwdOctets_Type()
)
custEgrQosPortSchedFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custEgrQosPortSchedFwdOctets.setStatus("current")
_PrvtTMSvcObjs_ObjectIdentity = ObjectIdentity
prvtTMSvcObjs = _PrvtTMSvcObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2)
)
_SvcNumEntries_Type = Integer32
_SvcNumEntries_Object = MibScalar
svcNumEntries = _SvcNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 1),
    _SvcNumEntries_Type()
)
svcNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcNumEntries.setStatus("current")
_SvcBaseInfoTable_Object = MibTable
svcBaseInfoTable = _SvcBaseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    svcBaseInfoTable.setStatus("current")
_SvcBaseInfoEntry_Object = MibTableRow
svcBaseInfoEntry = _SvcBaseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 2, 1)
)
svcBaseInfoEntry.setIndexNames(
    (0, "PRVT-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    svcBaseInfoEntry.setStatus("current")


class _SvcId_Type(Integer32):
    """Custom type svcId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SvcId_Type.__name__ = "Integer32"
_SvcId_Object = MibTableColumn
svcId = _SvcId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 2, 1, 1),
    _SvcId_Type()
)
svcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcId.setStatus("current")
_SvcVpnId_Type = VpnId
_SvcVpnId_Object = MibTableColumn
svcVpnId = _SvcVpnId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 2, 1, 2),
    _SvcVpnId_Type()
)
svcVpnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVpnId.setStatus("current")
_SvcRowStatus_Type = RowStatus
_SvcRowStatus_Object = MibTableColumn
svcRowStatus = _SvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 2, 1, 3),
    _SvcRowStatus_Type()
)
svcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcRowStatus.setStatus("current")
_SvcType_Type = ServType
_SvcType_Object = MibTableColumn
svcType = _SvcType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 2, 1, 4),
    _SvcType_Type()
)
svcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcType.setStatus("current")


class _SvcDescription_Type(ServObjDesc):
    """Custom type svcDescription based on ServObjDesc"""
    defaultValue = OctetString("")


_SvcDescription_Type.__name__ = "ServObjDesc"
_SvcDescription_Object = MibTableColumn
svcDescription = _SvcDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 2, 1, 5),
    _SvcDescription_Type()
)
svcDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcDescription.setStatus("current")


class _SvcMtu_Type(Integer32):
    """Custom type svcMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 9216),
    )


_SvcMtu_Type.__name__ = "Integer32"
_SvcMtu_Object = MibTableColumn
svcMtu = _SvcMtu_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 2, 1, 6),
    _SvcMtu_Type()
)
svcMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMtu.setStatus("current")


class _SvcAdminStatus_Type(ServiceAdminStatus):
    """Custom type svcAdminStatus based on ServiceAdminStatus"""
    defaultValue = 2


_SvcAdminStatus_Type.__name__ = "ServiceAdminStatus"
_SvcAdminStatus_Object = MibTableColumn
svcAdminStatus = _SvcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 2, 1, 7),
    _SvcAdminStatus_Type()
)
svcAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcAdminStatus.setStatus("current")
_SvcOperStatus_Type = ServiceOperStatus
_SvcOperStatus_Object = MibTableColumn
svcOperStatus = _SvcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 2, 1, 8),
    _SvcOperStatus_Type()
)
svcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcOperStatus.setStatus("current")
_SvcNumSaps_Type = Integer32
_SvcNumSaps_Object = MibTableColumn
svcNumSaps = _SvcNumSaps_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 2, 1, 9),
    _SvcNumSaps_Type()
)
svcNumSaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcNumSaps.setStatus("current")
_SvcNumSdps_Type = Integer32
_SvcNumSdps_Object = MibTableColumn
svcNumSdps = _SvcNumSdps_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 2, 1, 10),
    _SvcNumSdps_Type()
)
svcNumSdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcNumSdps.setStatus("current")
_SvcLastMgmtChange_Type = TimeStamp
_SvcLastMgmtChange_Object = MibTableColumn
svcLastMgmtChange = _SvcLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 2, 1, 11),
    _SvcLastMgmtChange_Type()
)
svcLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcLastMgmtChange.setStatus("current")
_SvcLastStatusChange_Type = TimeStamp
_SvcLastStatusChange_Object = MibTableColumn
svcLastStatusChange = _SvcLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 2, 1, 12),
    _SvcLastStatusChange_Type()
)
svcLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcLastStatusChange.setStatus("current")


class _SvcEnableSecureSaps_Type(TruthValue):
    """Custom type svcEnableSecureSaps based on TruthValue"""
    defaultValue = 2


_SvcEnableSecureSaps_Type.__name__ = "TruthValue"
_SvcEnableSecureSaps_Object = MibTableColumn
svcEnableSecureSaps = _SvcEnableSecureSaps_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 2, 1, 13),
    _SvcEnableSecureSaps_Type()
)
svcEnableSecureSaps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEnableSecureSaps.setStatus("current")


class _SvcCustName_Type(ServObjName):
    """Custom type svcCustName based on ServObjName"""
    defaultValue = OctetString("")


_SvcCustName_Type.__name__ = "ServObjName"
_SvcCustName_Object = MibTableColumn
svcCustName = _SvcCustName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 2, 1, 14),
    _SvcCustName_Type()
)
svcCustName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcCustName.setStatus("current")
_SvcRevertTimer_Type = Unsigned32
_SvcRevertTimer_Object = MibTableColumn
svcRevertTimer = _SvcRevertTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 2, 1, 15),
    _SvcRevertTimer_Type()
)
svcRevertTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcRevertTimer.setStatus("current")
_PrvtTMServVPLSGlobals_ObjectIdentity = ObjectIdentity
prvtTMServVPLSGlobals = _PrvtTMServVPLSGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 3)
)


class _SvcVplsMode_Type(Integer32):
    """Custom type svcVplsMode based on Integer32"""
    defaultValue = 2

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
        *(("disable", 0),
          ("qualified", 1),
          ("unqualified", 2),
          ("enable", 3))
    )


_SvcVplsMode_Type.__name__ = "Integer32"
_SvcVplsMode_Object = MibScalar
svcVplsMode = _SvcVplsMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 3, 1),
    _SvcVplsMode_Type()
)
svcVplsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcVplsMode.setStatus("current")
_SvcVPLSUplinkTable_Object = MibTable
svcVPLSUplinkTable = _SvcVPLSUplinkTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    svcVPLSUplinkTable.setStatus("current")
_SvcVPLSUplinkEntry_Object = MibTableRow
svcVPLSUplinkEntry = _SvcVPLSUplinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 3, 2, 1)
)
svcVPLSUplinkEntry.setIndexNames(
    (0, "PRVT-SERV-MIB", "svcVPLSUplinkPortID"),
)
if mibBuilder.loadTexts:
    svcVPLSUplinkEntry.setStatus("current")


class _SvcVPLSUplinkPortID_Type(Integer32):
    """Custom type svcVPLSUplinkPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SvcVPLSUplinkPortID_Type.__name__ = "Integer32"
_SvcVPLSUplinkPortID_Object = MibTableColumn
svcVPLSUplinkPortID = _SvcVPLSUplinkPortID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 3, 2, 1, 1),
    _SvcVPLSUplinkPortID_Type()
)
svcVPLSUplinkPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcVPLSUplinkPortID.setStatus("current")


class _SvcVPLSUplinkIfIndex_Type(Integer32):
    """Custom type svcVPLSUplinkIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SvcVPLSUplinkIfIndex_Type.__name__ = "Integer32"
_SvcVPLSUplinkIfIndex_Object = MibTableColumn
svcVPLSUplinkIfIndex = _SvcVPLSUplinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 3, 2, 1, 2),
    _SvcVPLSUplinkIfIndex_Type()
)
svcVPLSUplinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcVPLSUplinkIfIndex.setStatus("current")
_SvcVPLSUplinkNetworkPolicy_Type = TNetworkPolicyIdOrNone
_SvcVPLSUplinkNetworkPolicy_Object = MibTableColumn
svcVPLSUplinkNetworkPolicy = _SvcVPLSUplinkNetworkPolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 3, 2, 1, 3),
    _SvcVPLSUplinkNetworkPolicy_Type()
)
svcVPLSUplinkNetworkPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcVPLSUplinkNetworkPolicy.setStatus("current")
_SvcVPLSUplinkNetworkQueueEgressPolicy_Type = TNamedItemOrEmpty
_SvcVPLSUplinkNetworkQueueEgressPolicy_Object = MibTableColumn
svcVPLSUplinkNetworkQueueEgressPolicy = _SvcVPLSUplinkNetworkQueueEgressPolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 3, 2, 1, 4),
    _SvcVPLSUplinkNetworkQueueEgressPolicy_Type()
)
svcVPLSUplinkNetworkQueueEgressPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcVPLSUplinkNetworkQueueEgressPolicy.setStatus("current")


class _SvcVPLSUplinkShaperProfile_Type(Integer32):
    """Custom type svcVPLSUplinkShaperProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SvcVPLSUplinkShaperProfile_Type.__name__ = "Integer32"
_SvcVPLSUplinkShaperProfile_Object = MibTableColumn
svcVPLSUplinkShaperProfile = _SvcVPLSUplinkShaperProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 2, 3, 2, 1, 5),
    _SvcVPLSUplinkShaperProfile_Type()
)
svcVPLSUplinkShaperProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcVPLSUplinkShaperProfile.setStatus("current")
_PrvtTMSapObjs_ObjectIdentity = ObjectIdentity
prvtTMSapObjs = _PrvtTMSapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3)
)
_SapNumEntries_Type = Integer32
_SapNumEntries_Object = MibScalar
sapNumEntries = _SapNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 1),
    _SapNumEntries_Type()
)
sapNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapNumEntries.setStatus("current")
_SapBaseInfoTable_Object = MibTable
sapBaseInfoTable = _SapBaseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sapBaseInfoTable.setStatus("current")
_SapBaseInfoEntry_Object = MibTableRow
sapBaseInfoEntry = _SapBaseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 2, 1)
)
sapBaseInfoEntry.setIndexNames(
    (0, "PRVT-SERV-MIB", "svcId"),
    (0, "PRVT-SERV-MIB", "sapPortId"),
    (0, "PRVT-SERV-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapBaseInfoEntry.setStatus("current")


class _SapPortId_Type(Integer32):
    """Custom type sapPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SapPortId_Type.__name__ = "Integer32"
_SapPortId_Object = MibTableColumn
sapPortId = _SapPortId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 2, 1, 1),
    _SapPortId_Type()
)
sapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapPortId.setStatus("current")
_SapEncapValue_Type = TMEncapVal
_SapEncapValue_Object = MibTableColumn
sapEncapValue = _SapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 2, 1, 2),
    _SapEncapValue_Type()
)
sapEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEncapValue.setStatus("current")
_SapRowStatus_Type = RowStatus
_SapRowStatus_Object = MibTableColumn
sapRowStatus = _SapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 2, 1, 3),
    _SapRowStatus_Type()
)
sapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapRowStatus.setStatus("current")
_SapType_Type = ServType
_SapType_Object = MibTableColumn
sapType = _SapType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 2, 1, 4),
    _SapType_Type()
)
sapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapType.setStatus("current")


class _SapDescription_Type(ServObjDesc):
    """Custom type sapDescription based on ServObjDesc"""
    defaultValue = OctetString("")


_SapDescription_Type.__name__ = "ServObjDesc"
_SapDescription_Object = MibTableColumn
sapDescription = _SapDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 2, 1, 5),
    _SapDescription_Type()
)
sapDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapDescription.setStatus("current")


class _SapAdminStatus_Type(ServiceAdminStatus):
    """Custom type sapAdminStatus based on ServiceAdminStatus"""
    defaultValue = 1


_SapAdminStatus_Type.__name__ = "ServiceAdminStatus"
_SapAdminStatus_Object = MibTableColumn
sapAdminStatus = _SapAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 2, 1, 6),
    _SapAdminStatus_Type()
)
sapAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAdminStatus.setStatus("current")


class _SapOperStatus_Type(Integer32):
    """Custom type sapOperStatus based on Integer32"""
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
          ("down", 2),
          ("ingressQosMismatch", 3),
          ("egressQosMismatch", 4),
          ("svcAdminDown", 5),
          ("portMtuTooSmall", 6))
    )


_SapOperStatus_Type.__name__ = "Integer32"
_SapOperStatus_Object = MibTableColumn
sapOperStatus = _SapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 2, 1, 7),
    _SapOperStatus_Type()
)
sapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapOperStatus.setStatus("current")
_SapLastMgmtChange_Type = TimeStamp
_SapLastMgmtChange_Object = MibTableColumn
sapLastMgmtChange = _SapLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 2, 1, 8),
    _SapLastMgmtChange_Type()
)
sapLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapLastMgmtChange.setStatus("current")


class _SapOperFlags_Type(Bits):
    """Custom type sapOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("sapAdminDown", 0),
          ("svcAdminDown", 1),
          ("portOperDown", 2))
    )

_SapOperFlags_Type.__name__ = "Bits"
_SapOperFlags_Object = MibTableColumn
sapOperFlags = _SapOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 2, 1, 9),
    _SapOperFlags_Type()
)
sapOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapOperFlags.setStatus("current")


class _SapCustMultSvcSiteName_Type(DisplayString):
    """Custom type sapCustMultSvcSiteName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_SapCustMultSvcSiteName_Type.__name__ = "DisplayString"
_SapCustMultSvcSiteName_Object = MibTableColumn
sapCustMultSvcSiteName = _SapCustMultSvcSiteName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 2, 1, 11),
    _SapCustMultSvcSiteName_Type()
)
sapCustMultSvcSiteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCustMultSvcSiteName.setStatus("current")


class _SapIngressQosPolicyId_Type(TSapIngressPolicyIdOrNone):
    """Custom type sapIngressQosPolicyId based on TSapIngressPolicyIdOrNone"""
    defaultValue = 0


_SapIngressQosPolicyId_Type.__name__ = "TSapIngressPolicyIdOrNone"
_SapIngressQosPolicyId_Object = MibTableColumn
sapIngressQosPolicyId = _SapIngressQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 2, 1, 12),
    _SapIngressQosPolicyId_Type()
)
sapIngressQosPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIngressQosPolicyId.setStatus("current")


class _SapEgressQosPolicyId_Type(TSapEgressPolicyIdOrNone):
    """Custom type sapEgressQosPolicyId based on TSapEgressPolicyIdOrNone"""
    defaultValue = 0


_SapEgressQosPolicyId_Type.__name__ = "TSapEgressPolicyIdOrNone"
_SapEgressQosPolicyId_Object = MibTableColumn
sapEgressQosPolicyId = _SapEgressQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 2, 1, 13),
    _SapEgressQosPolicyId_Type()
)
sapEgressQosPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapEgressQosPolicyId.setStatus("current")


class _SapIngressQosSchedulerPolicy_Type(TNamedItemOrEmpty):
    """Custom type sapIngressQosSchedulerPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SapIngressQosSchedulerPolicy_Type.__name__ = "TNamedItemOrEmpty"
_SapIngressQosSchedulerPolicy_Object = MibTableColumn
sapIngressQosSchedulerPolicy = _SapIngressQosSchedulerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 2, 1, 14),
    _SapIngressQosSchedulerPolicy_Type()
)
sapIngressQosSchedulerPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIngressQosSchedulerPolicy.setStatus("current")


class _SapEgressQosSchedulerPolicy_Type(TNamedItemOrEmpty):
    """Custom type sapEgressQosSchedulerPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SapEgressQosSchedulerPolicy_Type.__name__ = "TNamedItemOrEmpty"
_SapEgressQosSchedulerPolicy_Object = MibTableColumn
sapEgressQosSchedulerPolicy = _SapEgressQosSchedulerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 2, 1, 15),
    _SapEgressQosSchedulerPolicy_Type()
)
sapEgressQosSchedulerPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapEgressQosSchedulerPolicy.setStatus("current")


class _SapLearnMode_Type(Integer32):
    """Custom type sapLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qualified", 1),
          ("unqualified", 2))
    )


_SapLearnMode_Type.__name__ = "Integer32"
_SapLearnMode_Object = MibTableColumn
sapLearnMode = _SapLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 2, 1, 16),
    _SapLearnMode_Type()
)
sapLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapLearnMode.setStatus("current")
_SapIngQosQueueStatsTable_Object = MibTable
sapIngQosQueueStatsTable = _SapIngQosQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    sapIngQosQueueStatsTable.setStatus("current")
_SapIngQosQueueStatsEntry_Object = MibTableRow
sapIngQosQueueStatsEntry = _SapIngQosQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 3, 1)
)
sapIngQosQueueStatsEntry.setIndexNames(
    (0, "PRVT-SERV-MIB", "svcId"),
    (0, "PRVT-SERV-MIB", "sapPortId"),
    (0, "PRVT-SERV-MIB", "sapEncapValue"),
    (0, "PRVT-SERV-MIB", "sapIngQosQueueId"),
)
if mibBuilder.loadTexts:
    sapIngQosQueueStatsEntry.setStatus("current")
_SapIngQosQueueId_Type = TSapIngQueueId
_SapIngQosQueueId_Object = MibTableColumn
sapIngQosQueueId = _SapIngQosQueueId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 3, 1, 1),
    _SapIngQosQueueId_Type()
)
sapIngQosQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueId.setStatus("current")
_SapIngQosQueueStatsOfferedHiPrioPackets_Type = Counter32
_SapIngQosQueueStatsOfferedHiPrioPackets_Object = MibTableColumn
sapIngQosQueueStatsOfferedHiPrioPackets = _SapIngQosQueueStatsOfferedHiPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 3, 1, 2),
    _SapIngQosQueueStatsOfferedHiPrioPackets_Type()
)
sapIngQosQueueStatsOfferedHiPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsOfferedHiPrioPackets.setStatus("current")
_SapIngQosQueueStatsOfferedLoPrioPackets_Type = Counter32
_SapIngQosQueueStatsOfferedLoPrioPackets_Object = MibTableColumn
sapIngQosQueueStatsOfferedLoPrioPackets = _SapIngQosQueueStatsOfferedLoPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 3, 1, 3),
    _SapIngQosQueueStatsOfferedLoPrioPackets_Type()
)
sapIngQosQueueStatsOfferedLoPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsOfferedLoPrioPackets.setStatus("current")
_SapIngQosQueueStatsOfferedHiPrioOctets_Type = Counter32
_SapIngQosQueueStatsOfferedHiPrioOctets_Object = MibTableColumn
sapIngQosQueueStatsOfferedHiPrioOctets = _SapIngQosQueueStatsOfferedHiPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 3, 1, 4),
    _SapIngQosQueueStatsOfferedHiPrioOctets_Type()
)
sapIngQosQueueStatsOfferedHiPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsOfferedHiPrioOctets.setStatus("current")
_SapIngQosQueueStatsOfferedLoPrioOctets_Type = Counter32
_SapIngQosQueueStatsOfferedLoPrioOctets_Object = MibTableColumn
sapIngQosQueueStatsOfferedLoPrioOctets = _SapIngQosQueueStatsOfferedLoPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 3, 1, 5),
    _SapIngQosQueueStatsOfferedLoPrioOctets_Type()
)
sapIngQosQueueStatsOfferedLoPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsOfferedLoPrioOctets.setStatus("current")
_SapIngQosQueueStatsForwardedInProfPackets_Type = Counter32
_SapIngQosQueueStatsForwardedInProfPackets_Object = MibTableColumn
sapIngQosQueueStatsForwardedInProfPackets = _SapIngQosQueueStatsForwardedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 3, 1, 6),
    _SapIngQosQueueStatsForwardedInProfPackets_Type()
)
sapIngQosQueueStatsForwardedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsForwardedInProfPackets.setStatus("current")
_SapIngQosQueueStatsForwardedOutProfPackets_Type = Counter32
_SapIngQosQueueStatsForwardedOutProfPackets_Object = MibTableColumn
sapIngQosQueueStatsForwardedOutProfPackets = _SapIngQosQueueStatsForwardedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 3, 1, 7),
    _SapIngQosQueueStatsForwardedOutProfPackets_Type()
)
sapIngQosQueueStatsForwardedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsForwardedOutProfPackets.setStatus("current")
_SapIngQosQueueStatsForwardedInProfOctets_Type = Counter32
_SapIngQosQueueStatsForwardedInProfOctets_Object = MibTableColumn
sapIngQosQueueStatsForwardedInProfOctets = _SapIngQosQueueStatsForwardedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 3, 1, 8),
    _SapIngQosQueueStatsForwardedInProfOctets_Type()
)
sapIngQosQueueStatsForwardedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsForwardedInProfOctets.setStatus("current")
_SapIngQosQueueStatsForwardedOutProfOctets_Type = Counter32
_SapIngQosQueueStatsForwardedOutProfOctets_Object = MibTableColumn
sapIngQosQueueStatsForwardedOutProfOctets = _SapIngQosQueueStatsForwardedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 3, 1, 9),
    _SapIngQosQueueStatsForwardedOutProfOctets_Type()
)
sapIngQosQueueStatsForwardedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsForwardedOutProfOctets.setStatus("current")
_SapIngQosQueueStatsDroppedOctets_Type = Counter32
_SapIngQosQueueStatsDroppedOctets_Object = MibTableColumn
sapIngQosQueueStatsDroppedOctets = _SapIngQosQueueStatsDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 3, 1, 10),
    _SapIngQosQueueStatsDroppedOctets_Type()
)
sapIngQosQueueStatsDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsDroppedOctets.setStatus("current")
_SapIngQosQueueStatsDroppedPackets_Type = Counter32
_SapIngQosQueueStatsDroppedPackets_Object = MibTableColumn
sapIngQosQueueStatsDroppedPackets = _SapIngQosQueueStatsDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 3, 1, 11),
    _SapIngQosQueueStatsDroppedPackets_Type()
)
sapIngQosQueueStatsDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsDroppedPackets.setStatus("current")
_SapIngQosCustName_Type = ServObjName
_SapIngQosCustName_Object = MibTableColumn
sapIngQosCustName = _SapIngQosCustName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 3, 1, 12),
    _SapIngQosCustName_Type()
)
sapIngQosCustName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosCustName.setStatus("current")
_SapEgrQosQueueStatsTable_Object = MibTable
sapEgrQosQueueStatsTable = _SapEgrQosQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsTable.setStatus("current")
_SapEgrQosQueueStatsEntry_Object = MibTableRow
sapEgrQosQueueStatsEntry = _SapEgrQosQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 4, 1)
)
sapEgrQosQueueStatsEntry.setIndexNames(
    (0, "PRVT-SERV-MIB", "svcId"),
    (0, "PRVT-SERV-MIB", "sapPortId"),
    (0, "PRVT-SERV-MIB", "sapEncapValue"),
    (0, "PRVT-SERV-MIB", "sapEgrQosQueueId"),
)
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsEntry.setStatus("current")
_SapEgrQosQueueId_Type = TSapEgrQueueId
_SapEgrQosQueueId_Object = MibTableColumn
sapEgrQosQueueId = _SapEgrQosQueueId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 4, 1, 1),
    _SapEgrQosQueueId_Type()
)
sapEgrQosQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueId.setStatus("current")
_SapEgrQosQueueStatsForwardedInProfPackets_Type = Counter32
_SapEgrQosQueueStatsForwardedInProfPackets_Object = MibTableColumn
sapEgrQosQueueStatsForwardedInProfPackets = _SapEgrQosQueueStatsForwardedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 4, 1, 2),
    _SapEgrQosQueueStatsForwardedInProfPackets_Type()
)
sapEgrQosQueueStatsForwardedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsForwardedInProfPackets.setStatus("current")
_SapEgrQosQueueStatsForwardedOutProfPackets_Type = Counter32
_SapEgrQosQueueStatsForwardedOutProfPackets_Object = MibTableColumn
sapEgrQosQueueStatsForwardedOutProfPackets = _SapEgrQosQueueStatsForwardedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 4, 1, 3),
    _SapEgrQosQueueStatsForwardedOutProfPackets_Type()
)
sapEgrQosQueueStatsForwardedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsForwardedOutProfPackets.setStatus("current")
_SapEgrQosQueueStatsForwardedInProfOctets_Type = Counter32
_SapEgrQosQueueStatsForwardedInProfOctets_Object = MibTableColumn
sapEgrQosQueueStatsForwardedInProfOctets = _SapEgrQosQueueStatsForwardedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 4, 1, 4),
    _SapEgrQosQueueStatsForwardedInProfOctets_Type()
)
sapEgrQosQueueStatsForwardedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsForwardedInProfOctets.setStatus("current")
_SapEgrQosQueueStatsForwardedOutProfOctets_Type = Counter32
_SapEgrQosQueueStatsForwardedOutProfOctets_Object = MibTableColumn
sapEgrQosQueueStatsForwardedOutProfOctets = _SapEgrQosQueueStatsForwardedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 4, 1, 5),
    _SapEgrQosQueueStatsForwardedOutProfOctets_Type()
)
sapEgrQosQueueStatsForwardedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsForwardedOutProfOctets.setStatus("current")
_SapEgrQosQueueStatsDroppedOctets_Type = Counter32
_SapEgrQosQueueStatsDroppedOctets_Object = MibTableColumn
sapEgrQosQueueStatsDroppedOctets = _SapEgrQosQueueStatsDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 4, 1, 6),
    _SapEgrQosQueueStatsDroppedOctets_Type()
)
sapEgrQosQueueStatsDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsDroppedOctets.setStatus("current")
_SapEgrQosQueueStatsDroppedPackets_Type = Counter32
_SapEgrQosQueueStatsDroppedPackets_Object = MibTableColumn
sapEgrQosQueueStatsDroppedPackets = _SapEgrQosQueueStatsDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 4, 1, 7),
    _SapEgrQosQueueStatsDroppedPackets_Type()
)
sapEgrQosQueueStatsDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsDroppedPackets.setStatus("current")
_SapEgrQosCustName_Type = ServObjName
_SapEgrQosCustName_Object = MibTableColumn
sapEgrQosCustName = _SapEgrQosCustName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 4, 1, 8),
    _SapEgrQosCustName_Type()
)
sapEgrQosCustName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosCustName.setStatus("current")
_SapIngQosSchedStatsTable_Object = MibTable
sapIngQosSchedStatsTable = _SapIngQosSchedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 5)
)
if mibBuilder.loadTexts:
    sapIngQosSchedStatsTable.setStatus("current")
_SapIngQosSchedStatsEntry_Object = MibTableRow
sapIngQosSchedStatsEntry = _SapIngQosSchedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 5, 1)
)
sapIngQosSchedStatsEntry.setIndexNames(
    (0, "PRVT-SERV-MIB", "svcId"),
    (0, "PRVT-SERV-MIB", "sapPortId"),
    (0, "PRVT-SERV-MIB", "sapEncapValue"),
    (1, "PRVT-SERV-MIB", "sapIngQosSchedName"),
)
if mibBuilder.loadTexts:
    sapIngQosSchedStatsEntry.setStatus("current")
_SapIngQosSchedName_Type = TNamedItem
_SapIngQosSchedName_Object = MibTableColumn
sapIngQosSchedName = _SapIngQosSchedName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 5, 1, 1),
    _SapIngQosSchedName_Type()
)
sapIngQosSchedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapIngQosSchedName.setStatus("current")
_SapIngQosSchedStatsForwardedPackets_Type = Counter32
_SapIngQosSchedStatsForwardedPackets_Object = MibTableColumn
sapIngQosSchedStatsForwardedPackets = _SapIngQosSchedStatsForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 5, 1, 2),
    _SapIngQosSchedStatsForwardedPackets_Type()
)
sapIngQosSchedStatsForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosSchedStatsForwardedPackets.setStatus("current")
_SapIngQosSchedStatsForwardedOctets_Type = Counter32
_SapIngQosSchedStatsForwardedOctets_Object = MibTableColumn
sapIngQosSchedStatsForwardedOctets = _SapIngQosSchedStatsForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 5, 1, 3),
    _SapIngQosSchedStatsForwardedOctets_Type()
)
sapIngQosSchedStatsForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosSchedStatsForwardedOctets.setStatus("current")
_SapIngQosSchedCustName_Type = ServObjName
_SapIngQosSchedCustName_Object = MibTableColumn
sapIngQosSchedCustName = _SapIngQosSchedCustName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 5, 1, 4),
    _SapIngQosSchedCustName_Type()
)
sapIngQosSchedCustName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosSchedCustName.setStatus("current")
_SapEgrQosSchedStatsTable_Object = MibTable
sapEgrQosSchedStatsTable = _SapEgrQosSchedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 6)
)
if mibBuilder.loadTexts:
    sapEgrQosSchedStatsTable.setStatus("current")
_SapEgrQosSchedStatsEntry_Object = MibTableRow
sapEgrQosSchedStatsEntry = _SapEgrQosSchedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 6, 1)
)
sapEgrQosSchedStatsEntry.setIndexNames(
    (0, "PRVT-SERV-MIB", "svcId"),
    (0, "PRVT-SERV-MIB", "sapPortId"),
    (0, "PRVT-SERV-MIB", "sapEncapValue"),
    (1, "PRVT-SERV-MIB", "sapEgrQosSchedName"),
)
if mibBuilder.loadTexts:
    sapEgrQosSchedStatsEntry.setStatus("current")
_SapEgrQosSchedName_Type = TNamedItem
_SapEgrQosSchedName_Object = MibTableColumn
sapEgrQosSchedName = _SapEgrQosSchedName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 6, 1, 1),
    _SapEgrQosSchedName_Type()
)
sapEgrQosSchedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapEgrQosSchedName.setStatus("current")
_SapEgrQosSchedStatsForwardedPackets_Type = Counter32
_SapEgrQosSchedStatsForwardedPackets_Object = MibTableColumn
sapEgrQosSchedStatsForwardedPackets = _SapEgrQosSchedStatsForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 6, 1, 2),
    _SapEgrQosSchedStatsForwardedPackets_Type()
)
sapEgrQosSchedStatsForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosSchedStatsForwardedPackets.setStatus("current")
_SapEgrQosSchedStatsForwardedOctets_Type = Counter32
_SapEgrQosSchedStatsForwardedOctets_Object = MibTableColumn
sapEgrQosSchedStatsForwardedOctets = _SapEgrQosSchedStatsForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 6, 1, 3),
    _SapEgrQosSchedStatsForwardedOctets_Type()
)
sapEgrQosSchedStatsForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosSchedStatsForwardedOctets.setStatus("current")
_SapEgrQosSchedCustName_Type = ServObjName
_SapEgrQosSchedCustName_Object = MibTableColumn
sapEgrQosSchedCustName = _SapEgrQosSchedCustName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 3, 6, 1, 4),
    _SapEgrQosSchedCustName_Type()
)
sapEgrQosSchedCustName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosSchedCustName.setStatus("current")
_PrvtTMSdpObjs_ObjectIdentity = ObjectIdentity
prvtTMSdpObjs = _PrvtTMSdpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4)
)
_SdpNumEntries_Type = Integer32
_SdpNumEntries_Object = MibScalar
sdpNumEntries = _SdpNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 1),
    _SdpNumEntries_Type()
)
sdpNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpNumEntries.setStatus("current")
_SdpNextFreeId_Type = SdpIdType
_SdpNextFreeId_Object = MibScalar
sdpNextFreeId = _SdpNextFreeId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 2),
    _SdpNextFreeId_Type()
)
sdpNextFreeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpNextFreeId.setStatus("current")
_SdpInfoTable_Object = MibTable
sdpInfoTable = _SdpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    sdpInfoTable.setStatus("current")
_SdpInfoEntry_Object = MibTableRow
sdpInfoEntry = _SdpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1)
)
sdpInfoEntry.setIndexNames(
    (0, "PRVT-SERV-MIB", "svcId"),
    (0, "PRVT-SERV-MIB", "sdpId"),
)
if mibBuilder.loadTexts:
    sdpInfoEntry.setStatus("current")
_SdpId_Type = SdpIdType
_SdpId_Object = MibTableColumn
sdpId = _SdpId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 1),
    _SdpId_Type()
)
sdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpId.setStatus("current")
_SdpRowStatus_Type = RowStatus
_SdpRowStatus_Object = MibTableColumn
sdpRowStatus = _SdpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 2),
    _SdpRowStatus_Type()
)
sdpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpRowStatus.setStatus("current")


class _SdpDelivery_Type(Integer32):
    """Custom type sdpDelivery based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("mpls", 2))
    )


_SdpDelivery_Type.__name__ = "Integer32"
_SdpDelivery_Object = MibTableColumn
sdpDelivery = _SdpDelivery_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 3),
    _SdpDelivery_Type()
)
sdpDelivery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpDelivery.setStatus("current")
_SdpFarEndIpAddress_Type = IpAddress
_SdpFarEndIpAddress_Object = MibTableColumn
sdpFarEndIpAddress = _SdpFarEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 4),
    _SdpFarEndIpAddress_Type()
)
sdpFarEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpFarEndIpAddress.setStatus("current")


class _SdpDescription_Type(ServObjDesc):
    """Custom type sdpDescription based on ServObjDesc"""
    defaultValue = OctetString("")


_SdpDescription_Type.__name__ = "ServObjDesc"
_SdpDescription_Object = MibTableColumn
sdpDescription = _SdpDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 5),
    _SdpDescription_Type()
)
sdpDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpDescription.setStatus("current")


class _SdpLabelSignaling_Type(Integer32):
    """Custom type sdpLabelSignaling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tldp", 2))
    )


_SdpLabelSignaling_Type.__name__ = "Integer32"
_SdpLabelSignaling_Object = MibTableColumn
sdpLabelSignaling = _SdpLabelSignaling_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 6),
    _SdpLabelSignaling_Type()
)
sdpLabelSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpLabelSignaling.setStatus("current")


class _SdpAdminStatus_Type(ServiceAdminStatus):
    """Custom type sdpAdminStatus based on ServiceAdminStatus"""
    defaultValue = 2


_SdpAdminStatus_Type.__name__ = "ServiceAdminStatus"
_SdpAdminStatus_Object = MibTableColumn
sdpAdminStatus = _SdpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 7),
    _SdpAdminStatus_Type()
)
sdpAdminStatus.setMaxAccess("read-write")
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
          ("down", 2),
          ("goingUp", 3),
          ("tunnelDown", 4),
          ("transportSelected", 5),
          ("supressed", 6))
    )


_SdpOperStatus_Type.__name__ = "Integer32"
_SdpOperStatus_Object = MibTableColumn
sdpOperStatus = _SdpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 8),
    _SdpOperStatus_Type()
)
sdpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpOperStatus.setStatus("current")
_SdpLastMgmtChange_Type = TimeStamp
_SdpLastMgmtChange_Object = MibTableColumn
sdpLastMgmtChange = _SdpLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 9),
    _SdpLastMgmtChange_Type()
)
sdpLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpLastMgmtChange.setStatus("current")


class _SdpLdpEnabled_Type(TruthValue):
    """Custom type sdpLdpEnabled based on TruthValue"""
    defaultValue = 2


_SdpLdpEnabled_Type.__name__ = "TruthValue"
_SdpLdpEnabled_Object = MibTableColumn
sdpLdpEnabled = _SdpLdpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 10),
    _SdpLdpEnabled_Type()
)
sdpLdpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpLdpEnabled.setStatus("current")


class _SdpOperFlags_Type(Bits):
    """Custom type sdpOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("sdpAdminDown", 0),
          ("signalingSessionDown", 1),
          ("transportTunnelDown", 2),
          ("invalidEgressInterface", 3),
          ("noSystemIpAddress", 4))
    )

_SdpOperFlags_Type.__name__ = "Bits"
_SdpOperFlags_Object = MibTableColumn
sdpOperFlags = _SdpOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 11),
    _SdpOperFlags_Type()
)
sdpOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpOperFlags.setStatus("current")
_SdpLastStatusChange_Type = TimeStamp
_SdpLastStatusChange_Object = MibTableColumn
sdpLastStatusChange = _SdpLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 12),
    _SdpLastStatusChange_Type()
)
sdpLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpLastStatusChange.setStatus("current")


class _SdpAdminIngressLabel_Type(Unsigned32):
    """Custom type sdpAdminIngressLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2048, 18431),
    )


_SdpAdminIngressLabel_Type.__name__ = "Unsigned32"
_SdpAdminIngressLabel_Object = MibTableColumn
sdpAdminIngressLabel = _SdpAdminIngressLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 13),
    _SdpAdminIngressLabel_Type()
)
sdpAdminIngressLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpAdminIngressLabel.setStatus("current")


class _SdpAdminEgressLabel_Type(Unsigned32):
    """Custom type sdpAdminEgressLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1048575),
    )


_SdpAdminEgressLabel_Type.__name__ = "Unsigned32"
_SdpAdminEgressLabel_Object = MibTableColumn
sdpAdminEgressLabel = _SdpAdminEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 14),
    _SdpAdminEgressLabel_Type()
)
sdpAdminEgressLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpAdminEgressLabel.setStatus("current")


class _SdpAdminIsBackup_Type(TruthValue):
    """Custom type sdpAdminIsBackup based on TruthValue"""
    defaultValue = 2


_SdpAdminIsBackup_Type.__name__ = "TruthValue"
_SdpAdminIsBackup_Object = MibTableColumn
sdpAdminIsBackup = _SdpAdminIsBackup_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 15),
    _SdpAdminIsBackup_Type()
)
sdpAdminIsBackup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpAdminIsBackup.setStatus("current")


class _SdpOperIsBackup_Type(TruthValue):
    """Custom type sdpOperIsBackup based on TruthValue"""
    defaultValue = 2


_SdpOperIsBackup_Type.__name__ = "TruthValue"
_SdpOperIsBackup_Object = MibTableColumn
sdpOperIsBackup = _SdpOperIsBackup_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 16),
    _SdpOperIsBackup_Type()
)
sdpOperIsBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpOperIsBackup.setStatus("current")


class _SdpOutInterface_Type(Integer32):
    """Custom type sdpOutInterface based on Integer32"""
    defaultValue = 0


_SdpOutInterface_Type.__name__ = "Integer32"
_SdpOutInterface_Object = MibTableColumn
sdpOutInterface = _SdpOutInterface_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 17),
    _SdpOutInterface_Type()
)
sdpOutInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpOutInterface.setStatus("current")


class _SdpGroupIdentifier_Type(Unsigned32):
    """Custom type sdpGroupIdentifier based on Unsigned32"""
    defaultValue = 0


_SdpGroupIdentifier_Type.__name__ = "Unsigned32"
_SdpGroupIdentifier_Object = MibTableColumn
sdpGroupIdentifier = _SdpGroupIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 18),
    _SdpGroupIdentifier_Type()
)
sdpGroupIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpGroupIdentifier.setStatus("current")


class _SdpTransportTunnelName_Type(DisplayString):
    """Custom type sdpTransportTunnelName based on DisplayString"""
    defaultValue = OctetString("")


_SdpTransportTunnelName_Type.__name__ = "DisplayString"
_SdpTransportTunnelName_Object = MibTableColumn
sdpTransportTunnelName = _SdpTransportTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 19),
    _SdpTransportTunnelName_Type()
)
sdpTransportTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpTransportTunnelName.setStatus("current")


class _SdpVCType_Type(Integer32):
    """Custom type sdpVCType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-vlan", 4),
          ("ethernet", 5))
    )


_SdpVCType_Type.__name__ = "Integer32"
_SdpVCType_Object = MibTableColumn
sdpVCType = _SdpVCType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 20),
    _SdpVCType_Type()
)
sdpVCType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpVCType.setStatus("current")


class _SdpType_Type(Integer32):
    """Custom type sdpType based on Integer32"""
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
        *(("invalidType", 0),
          ("generic", 1),
          ("spoke", 2),
          ("mesh", 3),
          ("hub", 4))
    )


_SdpType_Type.__name__ = "Integer32"
_SdpType_Object = MibTableColumn
sdpType = _SdpType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 21),
    _SdpType_Type()
)
sdpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpType.setStatus("current")


class _SdpMtu_Type(Integer32):
    """Custom type sdpMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 9216),
    )


_SdpMtu_Type.__name__ = "Integer32"
_SdpMtu_Object = MibTableColumn
sdpMtu = _SdpMtu_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 22),
    _SdpMtu_Type()
)
sdpMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpMtu.setStatus("current")
_SdpBindVlanTag_Type = Unsigned32
_SdpBindVlanTag_Object = MibTableColumn
sdpBindVlanTag = _SdpBindVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 23),
    _SdpBindVlanTag_Type()
)
sdpBindVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindVlanTag.setStatus("current")
_SdpIsPwStatusSignalingEnable_Type = TruthValue
_SdpIsPwStatusSignalingEnable_Object = MibTableColumn
sdpIsPwStatusSignalingEnable = _SdpIsPwStatusSignalingEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 24),
    _SdpIsPwStatusSignalingEnable_Type()
)
sdpIsPwStatusSignalingEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpIsPwStatusSignalingEnable.setStatus("current")


class _SdpEpsAdminIsPrimary_Type(TruthValue):
    """Custom type sdpEpsAdminIsPrimary based on TruthValue"""
    defaultValue = 2


_SdpEpsAdminIsPrimary_Type.__name__ = "TruthValue"
_SdpEpsAdminIsPrimary_Object = MibTableColumn
sdpEpsAdminIsPrimary = _SdpEpsAdminIsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 25),
    _SdpEpsAdminIsPrimary_Type()
)
sdpEpsAdminIsPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpEpsAdminIsPrimary.setStatus("current")


class _SdpEpsAdminIsSecondary_Type(TruthValue):
    """Custom type sdpEpsAdminIsSecondary based on TruthValue"""
    defaultValue = 2


_SdpEpsAdminIsSecondary_Type.__name__ = "TruthValue"
_SdpEpsAdminIsSecondary_Object = MibTableColumn
sdpEpsAdminIsSecondary = _SdpEpsAdminIsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 1, 4, 3, 1, 26),
    _SdpEpsAdminIsSecondary_Type()
)
sdpEpsAdminIsSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpEpsAdminIsSecondary.setStatus("current")
_PrvtServNotifications_ObjectIdentity = ObjectIdentity
prvtServNotifications = _PrvtServNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2)
)
_PrvtCustNotif_ObjectIdentity = ObjectIdentity
prvtCustNotif = _PrvtCustNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 1)
)
_PrvtCustTraps_ObjectIdentity = ObjectIdentity
prvtCustTraps = _PrvtCustTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 1, 0)
)
_PrvtSvcNotif_ObjectIdentity = ObjectIdentity
prvtSvcNotif = _PrvtSvcNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 2)
)
_PrvtSvcTraps_ObjectIdentity = ObjectIdentity
prvtSvcTraps = _PrvtSvcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 2, 0)
)
_PrvtSapNotif_ObjectIdentity = ObjectIdentity
prvtSapNotif = _PrvtSapNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 3)
)
_PrvtSapTraps_ObjectIdentity = ObjectIdentity
prvtSapTraps = _PrvtSapTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 3, 0)
)
_PrvtSdpNotif_ObjectIdentity = ObjectIdentity
prvtSdpNotif = _PrvtSdpNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 4)
)
_PrvtSdpTraps_ObjectIdentity = ObjectIdentity
prvtSdpTraps = _PrvtSdpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 4, 0)
)
_PrvtTMServConformance_ObjectIdentity = ObjectIdentity
prvtTMServConformance = _PrvtTMServConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3)
)
_PrvtTMCustConformance_ObjectIdentity = ObjectIdentity
prvtTMCustConformance = _PrvtTMCustConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 1)
)
_PrvtTMCustCompliances_ObjectIdentity = ObjectIdentity
prvtTMCustCompliances = _PrvtTMCustCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 1, 1)
)
_PrvtTMCustGroups_ObjectIdentity = ObjectIdentity
prvtTMCustGroups = _PrvtTMCustGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 1, 2)
)
_PrvtTMSvcConformance_ObjectIdentity = ObjectIdentity
prvtTMSvcConformance = _PrvtTMSvcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 2)
)
_PrvtTMSvcCompliances_ObjectIdentity = ObjectIdentity
prvtTMSvcCompliances = _PrvtTMSvcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 2, 1)
)
_PrvtTMSvcGroups_ObjectIdentity = ObjectIdentity
prvtTMSvcGroups = _PrvtTMSvcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 2, 2)
)
_PrvtTMSapConformance_ObjectIdentity = ObjectIdentity
prvtTMSapConformance = _PrvtTMSapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 3)
)
_PrvtTMSapCompliances_ObjectIdentity = ObjectIdentity
prvtTMSapCompliances = _PrvtTMSapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 3, 1)
)
_PrvtTMSapGroups_ObjectIdentity = ObjectIdentity
prvtTMSapGroups = _PrvtTMSapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 3, 2)
)
_PrvtTMSdpConformance_ObjectIdentity = ObjectIdentity
prvtTMSdpConformance = _PrvtTMSdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 4)
)
_PrvtTMSdpCompliances_ObjectIdentity = ObjectIdentity
prvtTMSdpCompliances = _PrvtTMSdpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 4, 1)
)
_PrvtTMSdpGroups_ObjectIdentity = ObjectIdentity
prvtTMSdpGroups = _PrvtTMSdpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 4, 2)
)
_PrvtTMTstpConformance_ObjectIdentity = ObjectIdentity
prvtTMTstpConformance = _PrvtTMTstpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 5)
)

# Managed Objects groups

prvtTMCustGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 1, 2, 1)
)
prvtTMCustGlobalGroup.setObjects(
      *(("PRVT-SERV-MIB", "custNumEntries"),
        ("PRVT-SERV-MIB", "custName"),
        ("PRVT-SERV-MIB", "custRowStatus"),
        ("PRVT-SERV-MIB", "custContact"),
        ("PRVT-SERV-MIB", "custPhone"),
        ("PRVT-SERV-MIB", "custLastMgmtChange"))
)
if mibBuilder.loadTexts:
    prvtTMCustGlobalGroup.setStatus("current")

prvtTMSvcGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 2, 2, 1)
)
prvtTMSvcGlobalGroup.setObjects(
      *(("PRVT-SERV-MIB", "svcNumEntries"),
        ("PRVT-SERV-MIB", "svcId"),
        ("PRVT-SERV-MIB", "svcRowStatus"),
        ("PRVT-SERV-MIB", "svcType"),
        ("PRVT-SERV-MIB", "svcDescription"),
        ("PRVT-SERV-MIB", "svcAdminStatus"),
        ("PRVT-SERV-MIB", "svcOperStatus"),
        ("PRVT-SERV-MIB", "svcNumSaps"),
        ("PRVT-SERV-MIB", "svcNumSdps"),
        ("PRVT-SERV-MIB", "svcLastMgmtChange"),
        ("PRVT-SERV-MIB", "svcVpnId"))
)
if mibBuilder.loadTexts:
    prvtTMSvcGlobalGroup.setStatus("current")

prvtTMSapGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 3, 2, 1)
)
prvtTMSapGlobalGroup.setObjects(
      *(("PRVT-SERV-MIB", "sapNumEntries"),
        ("PRVT-SERV-MIB", "sapPortId"),
        ("PRVT-SERV-MIB", "sapEncapValue"),
        ("PRVT-SERV-MIB", "sapRowStatus"),
        ("PRVT-SERV-MIB", "sapType"),
        ("PRVT-SERV-MIB", "sapDescription"),
        ("PRVT-SERV-MIB", "sapAdminStatus"),
        ("PRVT-SERV-MIB", "sapOperStatus"),
        ("PRVT-SERV-MIB", "sapIngressQosPolicyId"),
        ("PRVT-SERV-MIB", "sapEgressQosPolicyId"),
        ("PRVT-SERV-MIB", "sapLastMgmtChange"))
)
if mibBuilder.loadTexts:
    prvtTMSapGlobalGroup.setStatus("current")

prvtTMSdpGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 4, 2, 1)
)
prvtTMSdpGlobalGroup.setObjects(
      *(("PRVT-SERV-MIB", "sdpNumEntries"),
        ("PRVT-SERV-MIB", "sdpId"),
        ("PRVT-SERV-MIB", "sdpNextFreeId"),
        ("PRVT-SERV-MIB", "sdpRowStatus"),
        ("PRVT-SERV-MIB", "sdpDelivery"),
        ("PRVT-SERV-MIB", "sdpFarEndIpAddress"),
        ("PRVT-SERV-MIB", "sdpDescription"),
        ("PRVT-SERV-MIB", "sdpLabelSignaling"),
        ("PRVT-SERV-MIB", "sdpAdminStatus"),
        ("PRVT-SERV-MIB", "sdpOperStatus"),
        ("PRVT-SERV-MIB", "sdpLastMgmtChange"),
        ("PRVT-SERV-MIB", "sdpLdpEnabled"))
)
if mibBuilder.loadTexts:
    prvtTMSdpGlobalGroup.setStatus("current")


# Notification objects

prvtCustCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 1, 0, 1)
)
prvtCustCreated.setObjects(
    ("PRVT-SERV-MIB", "custName")
)
if mibBuilder.loadTexts:
    prvtCustCreated.setStatus(
        "current"
    )

prvtCustDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 1, 0, 2)
)
prvtCustDeleted.setObjects(
    ("PRVT-SERV-MIB", "custName")
)
if mibBuilder.loadTexts:
    prvtCustDeleted.setStatus(
        "current"
    )

prvtSvcCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 2, 0, 1)
)
prvtSvcCreated.setObjects(
    ("PRVT-SERV-MIB", "svcId")
)
if mibBuilder.loadTexts:
    prvtSvcCreated.setStatus(
        "current"
    )

prvtSvcDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 2, 0, 2)
)
prvtSvcDeleted.setObjects(
    ("PRVT-SERV-MIB", "svcId")
)
if mibBuilder.loadTexts:
    prvtSvcDeleted.setStatus(
        "current"
    )

prvtSvcStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 2, 0, 3)
)
prvtSvcStatusChanged.setObjects(
      *(("PRVT-SERV-MIB", "svcId"),
        ("PRVT-SERV-MIB", "svcVpnId"),
        ("PRVT-SERV-MIB", "svcAdminStatus"),
        ("PRVT-SERV-MIB", "svcOperStatus"))
)
if mibBuilder.loadTexts:
    prvtSvcStatusChanged.setStatus(
        "current"
    )

prvtSapCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 3, 0, 1)
)
prvtSapCreated.setObjects(
      *(("PRVT-SERV-MIB", "svcId"),
        ("PRVT-SERV-MIB", "sapPortId"),
        ("PRVT-SERV-MIB", "sapEncapValue"))
)
if mibBuilder.loadTexts:
    prvtSapCreated.setStatus(
        "current"
    )

prvtSapDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 3, 0, 2)
)
prvtSapDeleted.setObjects(
      *(("PRVT-SERV-MIB", "svcId"),
        ("PRVT-SERV-MIB", "sapPortId"),
        ("PRVT-SERV-MIB", "sapEncapValue"))
)
if mibBuilder.loadTexts:
    prvtSapDeleted.setStatus(
        "current"
    )

prvtSapStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 3, 0, 3)
)
prvtSapStatusChanged.setObjects(
      *(("PRVT-SERV-MIB", "svcId"),
        ("PRVT-SERV-MIB", "sapPortId"),
        ("PRVT-SERV-MIB", "sapEncapValue"),
        ("PRVT-SERV-MIB", "sapAdminStatus"),
        ("PRVT-SERV-MIB", "sapOperStatus"))
)
if mibBuilder.loadTexts:
    prvtSapStatusChanged.setStatus(
        "current"
    )

prvtSdpCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 4, 0, 1)
)
prvtSdpCreated.setObjects(
      *(("PRVT-SERV-MIB", "svcId"),
        ("PRVT-SERV-MIB", "sdpId"))
)
if mibBuilder.loadTexts:
    prvtSdpCreated.setStatus(
        "current"
    )

prvtSdpDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 4, 0, 2)
)
prvtSdpDeleted.setObjects(
      *(("PRVT-SERV-MIB", "svcId"),
        ("PRVT-SERV-MIB", "sdpId"))
)
if mibBuilder.loadTexts:
    prvtSdpDeleted.setStatus(
        "current"
    )

prvtSdpStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 2, 4, 0, 3)
)
prvtSdpStatusChanged.setObjects(
      *(("PRVT-SERV-MIB", "svcId"),
        ("PRVT-SERV-MIB", "sdpId"),
        ("PRVT-SERV-MIB", "sdpAdminStatus"),
        ("PRVT-SERV-MIB", "sdpOperStatus"))
)
if mibBuilder.loadTexts:
    prvtSdpStatusChanged.setStatus(
        "current"
    )


# Notifications groups

prvtTMSvcNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 2, 2, 2)
)
prvtTMSvcNotificationGroup.setObjects(
      *(("PRVT-SERV-MIB", "prvtSvcCreated"),
        ("PRVT-SERV-MIB", "prvtSvcDeleted"))
)
if mibBuilder.loadTexts:
    prvtTMSvcNotificationGroup.setStatus(
        "current"
    )

prvtTMSapNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 3, 2, 2)
)
prvtTMSapNotificationGroup.setObjects(
      *(("PRVT-SERV-MIB", "prvtSapStatusChanged"),
        ("PRVT-SERV-MIB", "prvtSapCreated"),
        ("PRVT-SERV-MIB", "prvtSapDeleted"))
)
if mibBuilder.loadTexts:
    prvtTMSapNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

prvtTMCustCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 1, 1, 1)
)
prvtTMCustCompliance.setObjects(
    ("PRVT-SERV-MIB", "prvtTMCustGlobalGroup")
)
if mibBuilder.loadTexts:
    prvtTMCustCompliance.setStatus(
        "current"
    )

prvtTMSvcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 2, 1, 1)
)
prvtTMSvcCompliance.setObjects(
      *(("PRVT-SERV-MIB", "prvtTMSvcGlobalGroup"),
        ("PRVT-SERV-MIB", "prvtTMSvcNotificationGroup"))
)
if mibBuilder.loadTexts:
    prvtTMSvcCompliance.setStatus(
        "current"
    )

prvtTMSapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 3, 1, 1)
)
prvtTMSapCompliance.setObjects(
      *(("PRVT-SERV-MIB", "prvtTMSapGlobalGroup"),
        ("PRVT-SERV-MIB", "prvtTMSapNotificationGroup"))
)
if mibBuilder.loadTexts:
    prvtTMSapCompliance.setStatus(
        "current"
    )

prvtTMSdpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 2, 3, 4, 1, 1)
)
prvtTMSdpCompliance.setObjects(
    ("PRVT-SERV-MIB", "prvtTMSdpGlobalGroup")
)
if mibBuilder.loadTexts:
    prvtTMSdpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-SERV-MIB",
    **{"ServiceAdminStatus": ServiceAdminStatus,
       "ServiceOperStatus": ServiceOperStatus,
       "ServObjName": ServObjName,
       "ServObjDesc": ServObjDesc,
       "ServType": ServType,
       "VpnId": VpnId,
       "SdpIdType": SdpIdType,
       "TMEncapVal": TMEncapVal,
       "TSapEgrQueueId": TSapEgrQueueId,
       "TSapIngQueueId": TSapIngQueueId,
       "prvtServicesMIB": prvtServicesMIB,
       "prvtTMServObjs": prvtTMServObjs,
       "prvtTMCustObjs": prvtTMCustObjs,
       "custNumEntries": custNumEntries,
       "custInfoTable": custInfoTable,
       "custInfoEntry": custInfoEntry,
       "custName": custName,
       "custRowStatus": custRowStatus,
       "custContact": custContact,
       "custPhone": custPhone,
       "custLastMgmtChange": custLastMgmtChange,
       "custMultiServiceSiteTable": custMultiServiceSiteTable,
       "custMultiServiceSiteEntry": custMultiServiceSiteEntry,
       "custMultSvcSiteName": custMultSvcSiteName,
       "custMultSvcSiteRowStatus": custMultSvcSiteRowStatus,
       "custMultSvcSiteDescription": custMultSvcSiteDescription,
       "custMultSvcSiteIngressSchedulerPolicy": custMultSvcSiteIngressSchedulerPolicy,
       "custMultSvcSiteEgressSchedulerPolicy": custMultSvcSiteEgressSchedulerPolicy,
       "custMultSvcSiteLastMgmtChange": custMultSvcSiteLastMgmtChange,
       "custMultiSvcSiteIngQosSchedStatsTable": custMultiSvcSiteIngQosSchedStatsTable,
       "custMultiSvcSiteIngQosSchedStatsEntry": custMultiSvcSiteIngQosSchedStatsEntry,
       "custIngQosSchedName": custIngQosSchedName,
       "custIngQosSchedStatsForwardedPackets": custIngQosSchedStatsForwardedPackets,
       "custIngQosSchedStatsForwardedOctets": custIngQosSchedStatsForwardedOctets,
       "custMultiSvcSiteEgrQosSchedStatsTable": custMultiSvcSiteEgrQosSchedStatsTable,
       "custMultiSvcSiteEgrQosSchedStatsEntry": custMultiSvcSiteEgrQosSchedStatsEntry,
       "custEgrQosSchedName": custEgrQosSchedName,
       "custEgrQosSchedStatsForwardedPackets": custEgrQosSchedStatsForwardedPackets,
       "custEgrQosSchedStatsForwardedOctets": custEgrQosSchedStatsForwardedOctets,
       "custIngQosPortIdSchedStatsTable": custIngQosPortIdSchedStatsTable,
       "custIngQosPortIdSchedStatsEntry": custIngQosPortIdSchedStatsEntry,
       "custIngQosPortIdSchedName": custIngQosPortIdSchedName,
       "custIngQosAssignmentPortId": custIngQosAssignmentPortId,
       "custIngQosPortSchedFwdPkts": custIngQosPortSchedFwdPkts,
       "custIngQosPortSchedFwdOctets": custIngQosPortSchedFwdOctets,
       "custEgrQosPortIdSchedStatsTable": custEgrQosPortIdSchedStatsTable,
       "custEgrQosPortIdSchedStatsEntry": custEgrQosPortIdSchedStatsEntry,
       "custEgrQosPortIdSchedName": custEgrQosPortIdSchedName,
       "custEgrQosAssignmentPortId": custEgrQosAssignmentPortId,
       "custEgrQosPortSchedFwdPkts": custEgrQosPortSchedFwdPkts,
       "custEgrQosPortSchedFwdOctets": custEgrQosPortSchedFwdOctets,
       "prvtTMSvcObjs": prvtTMSvcObjs,
       "svcNumEntries": svcNumEntries,
       "svcBaseInfoTable": svcBaseInfoTable,
       "svcBaseInfoEntry": svcBaseInfoEntry,
       "svcId": svcId,
       "svcVpnId": svcVpnId,
       "svcRowStatus": svcRowStatus,
       "svcType": svcType,
       "svcDescription": svcDescription,
       "svcMtu": svcMtu,
       "svcAdminStatus": svcAdminStatus,
       "svcOperStatus": svcOperStatus,
       "svcNumSaps": svcNumSaps,
       "svcNumSdps": svcNumSdps,
       "svcLastMgmtChange": svcLastMgmtChange,
       "svcLastStatusChange": svcLastStatusChange,
       "svcEnableSecureSaps": svcEnableSecureSaps,
       "svcCustName": svcCustName,
       "svcRevertTimer": svcRevertTimer,
       "prvtTMServVPLSGlobals": prvtTMServVPLSGlobals,
       "svcVplsMode": svcVplsMode,
       "svcVPLSUplinkTable": svcVPLSUplinkTable,
       "svcVPLSUplinkEntry": svcVPLSUplinkEntry,
       "svcVPLSUplinkPortID": svcVPLSUplinkPortID,
       "svcVPLSUplinkIfIndex": svcVPLSUplinkIfIndex,
       "svcVPLSUplinkNetworkPolicy": svcVPLSUplinkNetworkPolicy,
       "svcVPLSUplinkNetworkQueueEgressPolicy": svcVPLSUplinkNetworkQueueEgressPolicy,
       "svcVPLSUplinkShaperProfile": svcVPLSUplinkShaperProfile,
       "prvtTMSapObjs": prvtTMSapObjs,
       "sapNumEntries": sapNumEntries,
       "sapBaseInfoTable": sapBaseInfoTable,
       "sapBaseInfoEntry": sapBaseInfoEntry,
       "sapPortId": sapPortId,
       "sapEncapValue": sapEncapValue,
       "sapRowStatus": sapRowStatus,
       "sapType": sapType,
       "sapDescription": sapDescription,
       "sapAdminStatus": sapAdminStatus,
       "sapOperStatus": sapOperStatus,
       "sapLastMgmtChange": sapLastMgmtChange,
       "sapOperFlags": sapOperFlags,
       "sapCustMultSvcSiteName": sapCustMultSvcSiteName,
       "sapIngressQosPolicyId": sapIngressQosPolicyId,
       "sapEgressQosPolicyId": sapEgressQosPolicyId,
       "sapIngressQosSchedulerPolicy": sapIngressQosSchedulerPolicy,
       "sapEgressQosSchedulerPolicy": sapEgressQosSchedulerPolicy,
       "sapLearnMode": sapLearnMode,
       "sapIngQosQueueStatsTable": sapIngQosQueueStatsTable,
       "sapIngQosQueueStatsEntry": sapIngQosQueueStatsEntry,
       "sapIngQosQueueId": sapIngQosQueueId,
       "sapIngQosQueueStatsOfferedHiPrioPackets": sapIngQosQueueStatsOfferedHiPrioPackets,
       "sapIngQosQueueStatsOfferedLoPrioPackets": sapIngQosQueueStatsOfferedLoPrioPackets,
       "sapIngQosQueueStatsOfferedHiPrioOctets": sapIngQosQueueStatsOfferedHiPrioOctets,
       "sapIngQosQueueStatsOfferedLoPrioOctets": sapIngQosQueueStatsOfferedLoPrioOctets,
       "sapIngQosQueueStatsForwardedInProfPackets": sapIngQosQueueStatsForwardedInProfPackets,
       "sapIngQosQueueStatsForwardedOutProfPackets": sapIngQosQueueStatsForwardedOutProfPackets,
       "sapIngQosQueueStatsForwardedInProfOctets": sapIngQosQueueStatsForwardedInProfOctets,
       "sapIngQosQueueStatsForwardedOutProfOctets": sapIngQosQueueStatsForwardedOutProfOctets,
       "sapIngQosQueueStatsDroppedOctets": sapIngQosQueueStatsDroppedOctets,
       "sapIngQosQueueStatsDroppedPackets": sapIngQosQueueStatsDroppedPackets,
       "sapIngQosCustName": sapIngQosCustName,
       "sapEgrQosQueueStatsTable": sapEgrQosQueueStatsTable,
       "sapEgrQosQueueStatsEntry": sapEgrQosQueueStatsEntry,
       "sapEgrQosQueueId": sapEgrQosQueueId,
       "sapEgrQosQueueStatsForwardedInProfPackets": sapEgrQosQueueStatsForwardedInProfPackets,
       "sapEgrQosQueueStatsForwardedOutProfPackets": sapEgrQosQueueStatsForwardedOutProfPackets,
       "sapEgrQosQueueStatsForwardedInProfOctets": sapEgrQosQueueStatsForwardedInProfOctets,
       "sapEgrQosQueueStatsForwardedOutProfOctets": sapEgrQosQueueStatsForwardedOutProfOctets,
       "sapEgrQosQueueStatsDroppedOctets": sapEgrQosQueueStatsDroppedOctets,
       "sapEgrQosQueueStatsDroppedPackets": sapEgrQosQueueStatsDroppedPackets,
       "sapEgrQosCustName": sapEgrQosCustName,
       "sapIngQosSchedStatsTable": sapIngQosSchedStatsTable,
       "sapIngQosSchedStatsEntry": sapIngQosSchedStatsEntry,
       "sapIngQosSchedName": sapIngQosSchedName,
       "sapIngQosSchedStatsForwardedPackets": sapIngQosSchedStatsForwardedPackets,
       "sapIngQosSchedStatsForwardedOctets": sapIngQosSchedStatsForwardedOctets,
       "sapIngQosSchedCustName": sapIngQosSchedCustName,
       "sapEgrQosSchedStatsTable": sapEgrQosSchedStatsTable,
       "sapEgrQosSchedStatsEntry": sapEgrQosSchedStatsEntry,
       "sapEgrQosSchedName": sapEgrQosSchedName,
       "sapEgrQosSchedStatsForwardedPackets": sapEgrQosSchedStatsForwardedPackets,
       "sapEgrQosSchedStatsForwardedOctets": sapEgrQosSchedStatsForwardedOctets,
       "sapEgrQosSchedCustName": sapEgrQosSchedCustName,
       "prvtTMSdpObjs": prvtTMSdpObjs,
       "sdpNumEntries": sdpNumEntries,
       "sdpNextFreeId": sdpNextFreeId,
       "sdpInfoTable": sdpInfoTable,
       "sdpInfoEntry": sdpInfoEntry,
       "sdpId": sdpId,
       "sdpRowStatus": sdpRowStatus,
       "sdpDelivery": sdpDelivery,
       "sdpFarEndIpAddress": sdpFarEndIpAddress,
       "sdpDescription": sdpDescription,
       "sdpLabelSignaling": sdpLabelSignaling,
       "sdpAdminStatus": sdpAdminStatus,
       "sdpOperStatus": sdpOperStatus,
       "sdpLastMgmtChange": sdpLastMgmtChange,
       "sdpLdpEnabled": sdpLdpEnabled,
       "sdpOperFlags": sdpOperFlags,
       "sdpLastStatusChange": sdpLastStatusChange,
       "sdpAdminIngressLabel": sdpAdminIngressLabel,
       "sdpAdminEgressLabel": sdpAdminEgressLabel,
       "sdpAdminIsBackup": sdpAdminIsBackup,
       "sdpOperIsBackup": sdpOperIsBackup,
       "sdpOutInterface": sdpOutInterface,
       "sdpGroupIdentifier": sdpGroupIdentifier,
       "sdpTransportTunnelName": sdpTransportTunnelName,
       "sdpVCType": sdpVCType,
       "sdpType": sdpType,
       "sdpMtu": sdpMtu,
       "sdpBindVlanTag": sdpBindVlanTag,
       "sdpIsPwStatusSignalingEnable": sdpIsPwStatusSignalingEnable,
       "sdpEpsAdminIsPrimary": sdpEpsAdminIsPrimary,
       "sdpEpsAdminIsSecondary": sdpEpsAdminIsSecondary,
       "prvtServNotifications": prvtServNotifications,
       "prvtCustNotif": prvtCustNotif,
       "prvtCustTraps": prvtCustTraps,
       "prvtCustCreated": prvtCustCreated,
       "prvtCustDeleted": prvtCustDeleted,
       "prvtSvcNotif": prvtSvcNotif,
       "prvtSvcTraps": prvtSvcTraps,
       "prvtSvcCreated": prvtSvcCreated,
       "prvtSvcDeleted": prvtSvcDeleted,
       "prvtSvcStatusChanged": prvtSvcStatusChanged,
       "prvtSapNotif": prvtSapNotif,
       "prvtSapTraps": prvtSapTraps,
       "prvtSapCreated": prvtSapCreated,
       "prvtSapDeleted": prvtSapDeleted,
       "prvtSapStatusChanged": prvtSapStatusChanged,
       "prvtSdpNotif": prvtSdpNotif,
       "prvtSdpTraps": prvtSdpTraps,
       "prvtSdpCreated": prvtSdpCreated,
       "prvtSdpDeleted": prvtSdpDeleted,
       "prvtSdpStatusChanged": prvtSdpStatusChanged,
       "prvtTMServConformance": prvtTMServConformance,
       "prvtTMCustConformance": prvtTMCustConformance,
       "prvtTMCustCompliances": prvtTMCustCompliances,
       "prvtTMCustCompliance": prvtTMCustCompliance,
       "prvtTMCustGroups": prvtTMCustGroups,
       "prvtTMCustGlobalGroup": prvtTMCustGlobalGroup,
       "prvtTMSvcConformance": prvtTMSvcConformance,
       "prvtTMSvcCompliances": prvtTMSvcCompliances,
       "prvtTMSvcCompliance": prvtTMSvcCompliance,
       "prvtTMSvcGroups": prvtTMSvcGroups,
       "prvtTMSvcGlobalGroup": prvtTMSvcGlobalGroup,
       "prvtTMSvcNotificationGroup": prvtTMSvcNotificationGroup,
       "prvtTMSapConformance": prvtTMSapConformance,
       "prvtTMSapCompliances": prvtTMSapCompliances,
       "prvtTMSapCompliance": prvtTMSapCompliance,
       "prvtTMSapGroups": prvtTMSapGroups,
       "prvtTMSapGlobalGroup": prvtTMSapGlobalGroup,
       "prvtTMSapNotificationGroup": prvtTMSapNotificationGroup,
       "prvtTMSdpConformance": prvtTMSdpConformance,
       "prvtTMSdpCompliances": prvtTMSdpCompliances,
       "prvtTMSdpCompliance": prvtTMSdpCompliance,
       "prvtTMSdpGroups": prvtTMSdpGroups,
       "prvtTMSdpGlobalGroup": prvtTMSdpGlobalGroup,
       "prvtTMTstpConformance": prvtTMTstpConformance}
)
