# SNMP MIB module (ALCATEL-IND1-WCCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-WCCP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:14:30 2025
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

(softentIND1Wccp,
 wccpTraps) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Wccp",
    "wccpTraps")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1WCCPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class WccpServiceType(TextualConvention, Integer32):
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
        *(("standard", 1),
          ("dynamic", 2),
          ("unknown", 3))
    )



class WccpVersion(TextualConvention, Integer32):
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
        *(("version1", 1),
          ("version2", 2),
          ("unknown", 3))
    )



class WccpPasswordString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )



class WccpOperState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outOfService", 1),
          ("inService", 2))
    )



class WccpRestrictDisposition(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("block", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1WCCPMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1WCCPMIBObjects = _AlcatelIND1WCCPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1WCCPMIBObjects.setStatus("current")
_WccpFeature_ObjectIdentity = ObjectIdentity
wccpFeature = _WccpFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 1)
)
_WccpAdminEnabled_Type = TruthValue
_WccpAdminEnabled_Object = MibScalar
wccpAdminEnabled = _WccpAdminEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 1, 1),
    _WccpAdminEnabled_Type()
)
wccpAdminEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wccpAdminEnabled.setStatus("current")
_WccpServiceCount_Type = Counter32
_WccpServiceCount_Object = MibScalar
wccpServiceCount = _WccpServiceCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 1, 2),
    _WccpServiceCount_Type()
)
wccpServiceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServiceCount.setStatus("current")
_WccpServices_ObjectIdentity = ObjectIdentity
wccpServices = _WccpServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 2)
)
_WccpServiceTable_Object = MibTable
wccpServiceTable = _WccpServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wccpServiceTable.setStatus("current")
_WccpServiceTableEntry_Object = MibTableRow
wccpServiceTableEntry = _WccpServiceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 2, 1, 1)
)
wccpServiceTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpServiceId"),
)
if mibBuilder.loadTexts:
    wccpServiceTableEntry.setStatus("current")
_WccpServiceId_Type = Integer32
_WccpServiceId_Object = MibTableColumn
wccpServiceId = _WccpServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 2, 1, 1, 1),
    _WccpServiceId_Type()
)
wccpServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpServiceId.setStatus("current")
_WccpServiceAdminEnabled_Type = TruthValue
_WccpServiceAdminEnabled_Object = MibTableColumn
wccpServiceAdminEnabled = _WccpServiceAdminEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 2, 1, 1, 2),
    _WccpServiceAdminEnabled_Type()
)
wccpServiceAdminEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wccpServiceAdminEnabled.setStatus("current")
_WccpServicePassword_Type = WccpPasswordString
_WccpServicePassword_Object = MibTableColumn
wccpServicePassword = _WccpServicePassword_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 2, 1, 1, 3),
    _WccpServicePassword_Type()
)
wccpServicePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wccpServicePassword.setStatus("current")
_WccpServiceType_Type = WccpServiceType
_WccpServiceType_Object = MibTableColumn
wccpServiceType = _WccpServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 2, 1, 1, 4),
    _WccpServiceType_Type()
)
wccpServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServiceType.setStatus("current")
_WccpServiceVersion_Type = WccpVersion
_WccpServiceVersion_Object = MibTableColumn
wccpServiceVersion = _WccpServiceVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 2, 1, 1, 5),
    _WccpServiceVersion_Type()
)
wccpServiceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServiceVersion.setStatus("current")
_WccpServiceWebCacheCount_Type = Counter32
_WccpServiceWebCacheCount_Object = MibTableColumn
wccpServiceWebCacheCount = _WccpServiceWebCacheCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 2, 1, 1, 6),
    _WccpServiceWebCacheCount_Type()
)
wccpServiceWebCacheCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServiceWebCacheCount.setStatus("current")
_WccpServicePacketsRedir_Type = Counter32
_WccpServicePacketsRedir_Object = MibTableColumn
wccpServicePacketsRedir = _WccpServicePacketsRedir_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 2, 1, 1, 7),
    _WccpServicePacketsRedir_Type()
)
wccpServicePacketsRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServicePacketsRedir.setStatus("current")
_WccpServicePacketsLowRedir_Type = Counter32
_WccpServicePacketsLowRedir_Object = MibTableColumn
wccpServicePacketsLowRedir = _WccpServicePacketsLowRedir_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 2, 1, 1, 8),
    _WccpServicePacketsLowRedir_Type()
)
wccpServicePacketsLowRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServicePacketsLowRedir.setStatus("current")
_WccpServiceReceiveId_Type = Counter32
_WccpServiceReceiveId_Object = MibTableColumn
wccpServiceReceiveId = _WccpServiceReceiveId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 2, 1, 1, 9),
    _WccpServiceReceiveId_Type()
)
wccpServiceReceiveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServiceReceiveId.setStatus("current")
_WccpServiceChangeNumber_Type = Counter32
_WccpServiceChangeNumber_Object = MibTableColumn
wccpServiceChangeNumber = _WccpServiceChangeNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 2, 1, 1, 10),
    _WccpServiceChangeNumber_Type()
)
wccpServiceChangeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServiceChangeNumber.setStatus("current")
_WccpServiceRowStatus_Type = RowStatus
_WccpServiceRowStatus_Object = MibTableColumn
wccpServiceRowStatus = _WccpServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 2, 1, 1, 11),
    _WccpServiceRowStatus_Type()
)
wccpServiceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wccpServiceRowStatus.setStatus("current")
_WccpWebCaches_ObjectIdentity = ObjectIdentity
wccpWebCaches = _WccpWebCaches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 3)
)
_WccpWebCacheTable_Object = MibTable
wccpWebCacheTable = _WccpWebCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wccpWebCacheTable.setStatus("current")
_WccpWebCacheTableEntry_Object = MibTableRow
wccpWebCacheTableEntry = _WccpWebCacheTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 3, 1, 1)
)
wccpWebCacheTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpWebCacheServiceId"),
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpWebCacheIpAddress"),
)
if mibBuilder.loadTexts:
    wccpWebCacheTableEntry.setStatus("current")
_WccpWebCacheServiceId_Type = Integer32
_WccpWebCacheServiceId_Object = MibTableColumn
wccpWebCacheServiceId = _WccpWebCacheServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 3, 1, 1, 1),
    _WccpWebCacheServiceId_Type()
)
wccpWebCacheServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpWebCacheServiceId.setStatus("current")
_WccpWebCacheIpAddress_Type = InetAddress
_WccpWebCacheIpAddress_Object = MibTableColumn
wccpWebCacheIpAddress = _WccpWebCacheIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 3, 1, 1, 2),
    _WccpWebCacheIpAddress_Type()
)
wccpWebCacheIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpWebCacheIpAddress.setStatus("current")
_WccpWebCacheIpAddressType_Type = InetAddressType
_WccpWebCacheIpAddressType_Object = MibTableColumn
wccpWebCacheIpAddressType = _WccpWebCacheIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 3, 1, 1, 3),
    _WccpWebCacheIpAddressType_Type()
)
wccpWebCacheIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpWebCacheIpAddressType.setStatus("current")
_WccpWebCacheReceiveId_Type = Counter32
_WccpWebCacheReceiveId_Object = MibTableColumn
wccpWebCacheReceiveId = _WccpWebCacheReceiveId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 3, 1, 1, 4),
    _WccpWebCacheReceiveId_Type()
)
wccpWebCacheReceiveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpWebCacheReceiveId.setStatus("current")
_WccpWebCacheChangeNum_Type = Counter32
_WccpWebCacheChangeNum_Object = MibTableColumn
wccpWebCacheChangeNum = _WccpWebCacheChangeNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 3, 1, 1, 5),
    _WccpWebCacheChangeNum_Type()
)
wccpWebCacheChangeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpWebCacheChangeNum.setStatus("current")
_WccpWebCacheNumberOfRouters_Type = Counter32
_WccpWebCacheNumberOfRouters_Object = MibTableColumn
wccpWebCacheNumberOfRouters = _WccpWebCacheNumberOfRouters_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 3, 1, 1, 6),
    _WccpWebCacheNumberOfRouters_Type()
)
wccpWebCacheNumberOfRouters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpWebCacheNumberOfRouters.setStatus("current")
_WccpWebCacheNumberOfWebCaches_Type = Counter32
_WccpWebCacheNumberOfWebCaches_Object = MibTableColumn
wccpWebCacheNumberOfWebCaches = _WccpWebCacheNumberOfWebCaches_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 3, 1, 1, 7),
    _WccpWebCacheNumberOfWebCaches_Type()
)
wccpWebCacheNumberOfWebCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpWebCacheNumberOfWebCaches.setStatus("current")
_WccpRestrictVlan_ObjectIdentity = ObjectIdentity
wccpRestrictVlan = _WccpRestrictVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 4)
)
_WccpRestrictVlanTable_Object = MibTable
wccpRestrictVlanTable = _WccpRestrictVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    wccpRestrictVlanTable.setStatus("current")
_WccpRestrictVlanTableEntry_Object = MibTableRow
wccpRestrictVlanTableEntry = _WccpRestrictVlanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 4, 1, 1)
)
wccpRestrictVlanTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpRestrictVlanServiceId"),
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpRestrictVlanVlanId"),
)
if mibBuilder.loadTexts:
    wccpRestrictVlanTableEntry.setStatus("current")
_WccpRestrictVlanServiceId_Type = Integer32
_WccpRestrictVlanServiceId_Object = MibTableColumn
wccpRestrictVlanServiceId = _WccpRestrictVlanServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 4, 1, 1, 1),
    _WccpRestrictVlanServiceId_Type()
)
wccpRestrictVlanServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpRestrictVlanServiceId.setStatus("current")
_WccpRestrictVlanVlanId_Type = Integer32
_WccpRestrictVlanVlanId_Object = MibTableColumn
wccpRestrictVlanVlanId = _WccpRestrictVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 4, 1, 1, 2),
    _WccpRestrictVlanVlanId_Type()
)
wccpRestrictVlanVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpRestrictVlanVlanId.setStatus("current")
_WccpRestrictVlanDisposition_Type = WccpRestrictDisposition
_WccpRestrictVlanDisposition_Object = MibTableColumn
wccpRestrictVlanDisposition = _WccpRestrictVlanDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 4, 1, 1, 3),
    _WccpRestrictVlanDisposition_Type()
)
wccpRestrictVlanDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wccpRestrictVlanDisposition.setStatus("current")
_WccpRestrictVlanRowStatus_Type = RowStatus
_WccpRestrictVlanRowStatus_Object = MibTableColumn
wccpRestrictVlanRowStatus = _WccpRestrictVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 4, 1, 1, 4),
    _WccpRestrictVlanRowStatus_Type()
)
wccpRestrictVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wccpRestrictVlanRowStatus.setStatus("current")
_WccpRestrictWebCache_ObjectIdentity = ObjectIdentity
wccpRestrictWebCache = _WccpRestrictWebCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 5)
)
_WccpRestrictWebCacheTable_Object = MibTable
wccpRestrictWebCacheTable = _WccpRestrictWebCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    wccpRestrictWebCacheTable.setStatus("current")
_WccpRestrictWebCacheTableEntry_Object = MibTableRow
wccpRestrictWebCacheTableEntry = _WccpRestrictWebCacheTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 5, 1, 1)
)
wccpRestrictWebCacheTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpRestrictWebCacheServiceId"),
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpRestrictWebCacheIpAddress"),
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpRestrictWebCacheIpMask"),
)
if mibBuilder.loadTexts:
    wccpRestrictWebCacheTableEntry.setStatus("current")
_WccpRestrictWebCacheServiceId_Type = Integer32
_WccpRestrictWebCacheServiceId_Object = MibTableColumn
wccpRestrictWebCacheServiceId = _WccpRestrictWebCacheServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 5, 1, 1, 1),
    _WccpRestrictWebCacheServiceId_Type()
)
wccpRestrictWebCacheServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpRestrictWebCacheServiceId.setStatus("current")
_WccpRestrictWebCacheIpAddress_Type = InetAddress
_WccpRestrictWebCacheIpAddress_Object = MibTableColumn
wccpRestrictWebCacheIpAddress = _WccpRestrictWebCacheIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 5, 1, 1, 2),
    _WccpRestrictWebCacheIpAddress_Type()
)
wccpRestrictWebCacheIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpRestrictWebCacheIpAddress.setStatus("current")
_WccpRestrictWebCacheIpAddressType_Type = InetAddressType
_WccpRestrictWebCacheIpAddressType_Object = MibTableColumn
wccpRestrictWebCacheIpAddressType = _WccpRestrictWebCacheIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 5, 1, 1, 3),
    _WccpRestrictWebCacheIpAddressType_Type()
)
wccpRestrictWebCacheIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpRestrictWebCacheIpAddressType.setStatus("current")
_WccpRestrictWebCacheIpMask_Type = InetAddress
_WccpRestrictWebCacheIpMask_Object = MibTableColumn
wccpRestrictWebCacheIpMask = _WccpRestrictWebCacheIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 5, 1, 1, 4),
    _WccpRestrictWebCacheIpMask_Type()
)
wccpRestrictWebCacheIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpRestrictWebCacheIpMask.setStatus("current")
_WccpRestrictWebCacheIpMaskAddressType_Type = InetAddressType
_WccpRestrictWebCacheIpMaskAddressType_Object = MibTableColumn
wccpRestrictWebCacheIpMaskAddressType = _WccpRestrictWebCacheIpMaskAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 5, 1, 1, 5),
    _WccpRestrictWebCacheIpMaskAddressType_Type()
)
wccpRestrictWebCacheIpMaskAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpRestrictWebCacheIpMaskAddressType.setStatus("current")
_WccpRestrictWebCacheDisposition_Type = WccpRestrictDisposition
_WccpRestrictWebCacheDisposition_Object = MibTableColumn
wccpRestrictWebCacheDisposition = _WccpRestrictWebCacheDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 5, 1, 1, 6),
    _WccpRestrictWebCacheDisposition_Type()
)
wccpRestrictWebCacheDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wccpRestrictWebCacheDisposition.setStatus("current")
_WccpRestrictWebCacheRowStatus_Type = RowStatus
_WccpRestrictWebCacheRowStatus_Object = MibTableColumn
wccpRestrictWebCacheRowStatus = _WccpRestrictWebCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 1, 5, 1, 1, 7),
    _WccpRestrictWebCacheRowStatus_Type()
)
wccpRestrictWebCacheRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wccpRestrictWebCacheRowStatus.setStatus("current")
_AlcatelIND1WCCPMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1WCCPMIBConformance = _AlcatelIND1WCCPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1WCCPMIBConformance.setStatus("current")
_AlcatelIND1WCCPMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1WCCPMIBGroups = _AlcatelIND1WCCPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1WCCPMIBGroups.setStatus("current")
_AlcatelIND1WCCPMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1WCCPMIBCompliances = _AlcatelIND1WCCPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1WCCPMIBCompliances.setStatus("current")
_WccpTrapsDesc_ObjectIdentity = ObjectIdentity
wccpTrapsDesc = _WccpTrapsDesc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 18, 1)
)
_WccpTrapsObj_ObjectIdentity = ObjectIdentity
wccpTrapsObj = _WccpTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 18, 2)
)
_WccpTrapInfoServiceId_Type = Integer32
_WccpTrapInfoServiceId_Object = MibScalar
wccpTrapInfoServiceId = _WccpTrapInfoServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 18, 2, 1),
    _WccpTrapInfoServiceId_Type()
)
wccpTrapInfoServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpTrapInfoServiceId.setStatus("current")
_WccpTrapInfoOperStatus_Type = WccpOperState
_WccpTrapInfoOperStatus_Object = MibScalar
wccpTrapInfoOperStatus = _WccpTrapInfoOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 18, 2, 2),
    _WccpTrapInfoOperStatus_Type()
)
wccpTrapInfoOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpTrapInfoOperStatus.setStatus("current")
_WccpTrapInfoWebCacheIpAddr_Type = IpAddress
_WccpTrapInfoWebCacheIpAddr_Object = MibScalar
wccpTrapInfoWebCacheIpAddr = _WccpTrapInfoWebCacheIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 18, 2, 3),
    _WccpTrapInfoWebCacheIpAddr_Type()
)
wccpTrapInfoWebCacheIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpTrapInfoWebCacheIpAddr.setStatus("current")


class _WccpTrapInfoEntityGroup_Type(Integer32):
    """Custom type wccpTrapInfoEntityGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wccp", 1),
          ("service", 2),
          ("webcache", 3))
    )


_WccpTrapInfoEntityGroup_Type.__name__ = "Integer32"
_WccpTrapInfoEntityGroup_Object = MibScalar
wccpTrapInfoEntityGroup = _WccpTrapInfoEntityGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 18, 2, 4),
    _WccpTrapInfoEntityGroup_Type()
)
wccpTrapInfoEntityGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpTrapInfoEntityGroup.setStatus("current")

# Managed Objects groups

wccpFeatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 2, 1, 1)
)
wccpFeatureGroup.setObjects(
      *(("ALCATEL-IND1-WCCP-MIB", "wccpAdminEnabled"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServiceCount"))
)
if mibBuilder.loadTexts:
    wccpFeatureGroup.setStatus("current")

wccpServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 2, 1, 2)
)
wccpServiceGroup.setObjects(
      *(("ALCATEL-IND1-WCCP-MIB", "wccpServiceAdminEnabled"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServicePassword"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServiceType"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServiceVersion"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServiceWebCacheCount"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServicePacketsRedir"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServicePacketsLowRedir"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServiceReceiveId"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServiceChangeNumber"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServiceRowStatus"))
)
if mibBuilder.loadTexts:
    wccpServiceGroup.setStatus("current")

wccpWebCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 2, 1, 3)
)
wccpWebCacheGroup.setObjects(
      *(("ALCATEL-IND1-WCCP-MIB", "wccpWebCacheReceiveId"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpWebCacheChangeNum"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpWebCacheNumberOfRouters"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpWebCacheNumberOfWebCaches"))
)
if mibBuilder.loadTexts:
    wccpWebCacheGroup.setStatus("current")

wccpRestrictVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 2, 1, 4)
)
wccpRestrictVlanGroup.setObjects(
      *(("ALCATEL-IND1-WCCP-MIB", "wccpRestrictVlanDisposition"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpRestrictVlanRowStatus"))
)
if mibBuilder.loadTexts:
    wccpRestrictVlanGroup.setStatus("current")

wccpRestrictWebCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 2, 1, 5)
)
wccpRestrictWebCacheGroup.setObjects(
      *(("ALCATEL-IND1-WCCP-MIB", "wccpRestrictWebCacheDisposition"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpRestrictWebCacheRowStatus"))
)
if mibBuilder.loadTexts:
    wccpRestrictWebCacheGroup.setStatus("current")


# Notification objects

wccpTrapOperStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 18, 1, 0, 3)
)
wccpTrapOperStatus.setObjects(
      *(("ALCATEL-IND1-WCCP-MIB", "wccpTrapInfoEntityGroup"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpTrapInfoOperStatus"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpTrapInfoServiceId"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpTrapInfoWebCacheIpAddr"))
)
if mibBuilder.loadTexts:
    wccpTrapOperStatus.setStatus(
        "current"
    )


# Notifications groups

wccpTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 2, 1, 6)
)
wccpTrapsGroup.setObjects(
    ("ALCATEL-IND1-WCCP-MIB", "wccpTrapOperStatus")
)
if mibBuilder.loadTexts:
    wccpTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1WCCPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 38, 1, 2, 2, 1)
)
alcatelIND1WCCPMIBCompliance.setObjects(
      *(("ALCATEL-IND1-WCCP-MIB", "wccpFeatureGroup"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServiceGroup"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpWebCacheGroup"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpRestrictVlanGroup"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpRestrictWebCacheGroup"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpTrapsGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1WCCPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-WCCP-MIB",
    **{"WccpServiceType": WccpServiceType,
       "WccpVersion": WccpVersion,
       "WccpPasswordString": WccpPasswordString,
       "WccpOperState": WccpOperState,
       "WccpRestrictDisposition": WccpRestrictDisposition,
       "alcatelIND1WCCPMIB": alcatelIND1WCCPMIB,
       "alcatelIND1WCCPMIBObjects": alcatelIND1WCCPMIBObjects,
       "wccpFeature": wccpFeature,
       "wccpAdminEnabled": wccpAdminEnabled,
       "wccpServiceCount": wccpServiceCount,
       "wccpServices": wccpServices,
       "wccpServiceTable": wccpServiceTable,
       "wccpServiceTableEntry": wccpServiceTableEntry,
       "wccpServiceId": wccpServiceId,
       "wccpServiceAdminEnabled": wccpServiceAdminEnabled,
       "wccpServicePassword": wccpServicePassword,
       "wccpServiceType": wccpServiceType,
       "wccpServiceVersion": wccpServiceVersion,
       "wccpServiceWebCacheCount": wccpServiceWebCacheCount,
       "wccpServicePacketsRedir": wccpServicePacketsRedir,
       "wccpServicePacketsLowRedir": wccpServicePacketsLowRedir,
       "wccpServiceReceiveId": wccpServiceReceiveId,
       "wccpServiceChangeNumber": wccpServiceChangeNumber,
       "wccpServiceRowStatus": wccpServiceRowStatus,
       "wccpWebCaches": wccpWebCaches,
       "wccpWebCacheTable": wccpWebCacheTable,
       "wccpWebCacheTableEntry": wccpWebCacheTableEntry,
       "wccpWebCacheServiceId": wccpWebCacheServiceId,
       "wccpWebCacheIpAddress": wccpWebCacheIpAddress,
       "wccpWebCacheIpAddressType": wccpWebCacheIpAddressType,
       "wccpWebCacheReceiveId": wccpWebCacheReceiveId,
       "wccpWebCacheChangeNum": wccpWebCacheChangeNum,
       "wccpWebCacheNumberOfRouters": wccpWebCacheNumberOfRouters,
       "wccpWebCacheNumberOfWebCaches": wccpWebCacheNumberOfWebCaches,
       "wccpRestrictVlan": wccpRestrictVlan,
       "wccpRestrictVlanTable": wccpRestrictVlanTable,
       "wccpRestrictVlanTableEntry": wccpRestrictVlanTableEntry,
       "wccpRestrictVlanServiceId": wccpRestrictVlanServiceId,
       "wccpRestrictVlanVlanId": wccpRestrictVlanVlanId,
       "wccpRestrictVlanDisposition": wccpRestrictVlanDisposition,
       "wccpRestrictVlanRowStatus": wccpRestrictVlanRowStatus,
       "wccpRestrictWebCache": wccpRestrictWebCache,
       "wccpRestrictWebCacheTable": wccpRestrictWebCacheTable,
       "wccpRestrictWebCacheTableEntry": wccpRestrictWebCacheTableEntry,
       "wccpRestrictWebCacheServiceId": wccpRestrictWebCacheServiceId,
       "wccpRestrictWebCacheIpAddress": wccpRestrictWebCacheIpAddress,
       "wccpRestrictWebCacheIpAddressType": wccpRestrictWebCacheIpAddressType,
       "wccpRestrictWebCacheIpMask": wccpRestrictWebCacheIpMask,
       "wccpRestrictWebCacheIpMaskAddressType": wccpRestrictWebCacheIpMaskAddressType,
       "wccpRestrictWebCacheDisposition": wccpRestrictWebCacheDisposition,
       "wccpRestrictWebCacheRowStatus": wccpRestrictWebCacheRowStatus,
       "alcatelIND1WCCPMIBConformance": alcatelIND1WCCPMIBConformance,
       "alcatelIND1WCCPMIBGroups": alcatelIND1WCCPMIBGroups,
       "wccpFeatureGroup": wccpFeatureGroup,
       "wccpServiceGroup": wccpServiceGroup,
       "wccpWebCacheGroup": wccpWebCacheGroup,
       "wccpRestrictVlanGroup": wccpRestrictVlanGroup,
       "wccpRestrictWebCacheGroup": wccpRestrictWebCacheGroup,
       "wccpTrapsGroup": wccpTrapsGroup,
       "alcatelIND1WCCPMIBCompliances": alcatelIND1WCCPMIBCompliances,
       "alcatelIND1WCCPMIBCompliance": alcatelIND1WCCPMIBCompliance,
       "wccpTrapsDesc": wccpTrapsDesc,
       "wccpTrapOperStatus": wccpTrapOperStatus,
       "wccpTrapsObj": wccpTrapsObj,
       "wccpTrapInfoServiceId": wccpTrapInfoServiceId,
       "wccpTrapInfoOperStatus": wccpTrapInfoOperStatus,
       "wccpTrapInfoWebCacheIpAddr": wccpTrapInfoWebCacheIpAddr,
       "wccpTrapInfoEntityGroup": wccpTrapInfoEntityGroup}
)
