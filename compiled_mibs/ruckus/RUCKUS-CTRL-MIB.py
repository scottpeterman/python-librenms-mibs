# SNMP MIB module (RUCKUS-CTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ruckus\RUCKUS-CTRL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:39 2025
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(ruckusCTRLWLANModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusCTRLWLANModule")

(RuckusAdminStatus,
 RuckusAuthStatusType,
 RuckusAuthenticationType,
 RuckusChannelWidthType,
 RuckusCountryCode,
 RuckusMeshRoles,
 RuckusRadioMode,
 RuckusSSID,
 RuckusSystemClusterStatus,
 RuckusSystemNodeStatus,
 RuckusUUID,
 RuckusUUIDType,
 RuckusWLANAuthMethodType,
 RuckusWLANEncryptionType,
 RuckusWPACipherType,
 RuckusdB) = mibBuilder.importSymbols(
    "RUCKUS-TC-MIB",
    "RuckusAdminStatus",
    "RuckusAuthStatusType",
    "RuckusAuthenticationType",
    "RuckusChannelWidthType",
    "RuckusCountryCode",
    "RuckusMeshRoles",
    "RuckusRadioMode",
    "RuckusSSID",
    "RuckusSystemClusterStatus",
    "RuckusSystemNodeStatus",
    "RuckusUUID",
    "RuckusUUIDType",
    "RuckusWLANAuthMethodType",
    "RuckusWLANEncryptionType",
    "RuckusWPACipherType",
    "RuckusdB")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusCTRLWLANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusCTRLWLANMIB.setRevisions(
        ("2017-05-15 10:00",
         "2016-08-05 10:00",
         "2016-08-04 10:00",
         "2016-07-29 10:00",
         "2016-07-13 10:00",
         "2016-07-05 10:00",
         "2015-06-30 11:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RuckusEthPortStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )



class RuckusAPStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 0),
          ("connected", 1))
    )



class RuckusRebootStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("run-reboot", 1))
    )



class RuckusSystemClusterHAState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



class RuckusSystemClusterHARole(TextualConvention, Integer32):
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
        *(("active", 1),
          ("standby", 2),
          ("none", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RuckusCTRLWLANObjects_ObjectIdentity = ObjectIdentity
ruckusCTRLWLANObjects = _RuckusCTRLWLANObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1)
)
_RuckusCTRLInfo_ObjectIdentity = ObjectIdentity
ruckusCTRLInfo = _RuckusCTRLInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1)
)
_RuckusCTRLSystemNodeTable_Object = MibTable
ruckusCTRLSystemNodeTable = _RuckusCTRLSystemNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusCTRLSystemNodeTable.setStatus("current")
_RuckusCTRLSystemNodeEntry_Object = MibTableRow
ruckusCTRLSystemNodeEntry = _RuckusCTRLSystemNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 1, 1)
)
ruckusCTRLSystemNodeEntry.setIndexNames(
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlSystemNodeSerialNumber"),
)
if mibBuilder.loadTexts:
    ruckusCTRLSystemNodeEntry.setStatus("current")
_RuckusCtrlSystemNodeSerialNumber_Type = DisplayString
_RuckusCtrlSystemNodeSerialNumber_Object = MibTableColumn
ruckusCtrlSystemNodeSerialNumber = _RuckusCtrlSystemNodeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 1, 1, 1),
    _RuckusCtrlSystemNodeSerialNumber_Type()
)
ruckusCtrlSystemNodeSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSystemNodeSerialNumber.setStatus("current")
_RuckusCtrlSystemNodeName_Type = DisplayString
_RuckusCtrlSystemNodeName_Object = MibTableColumn
ruckusCtrlSystemNodeName = _RuckusCtrlSystemNodeName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 1, 1, 2),
    _RuckusCtrlSystemNodeName_Type()
)
ruckusCtrlSystemNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSystemNodeName.setStatus("current")
_RuckusCtrlSystemNodeModel_Type = DisplayString
_RuckusCtrlSystemNodeModel_Object = MibTableColumn
ruckusCtrlSystemNodeModel = _RuckusCtrlSystemNodeModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 1, 1, 3),
    _RuckusCtrlSystemNodeModel_Type()
)
ruckusCtrlSystemNodeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSystemNodeModel.setStatus("current")
_RuckusCtrlSystemNodeVersion_Type = DisplayString
_RuckusCtrlSystemNodeVersion_Object = MibTableColumn
ruckusCtrlSystemNodeVersion = _RuckusCtrlSystemNodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 1, 1, 9),
    _RuckusCtrlSystemNodeVersion_Type()
)
ruckusCtrlSystemNodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSystemNodeVersion.setStatus("current")
_RuckusCtrlSystemNodeNumApLicense_Type = Unsigned32
_RuckusCtrlSystemNodeNumApLicense_Object = MibTableColumn
ruckusCtrlSystemNodeNumApLicense = _RuckusCtrlSystemNodeNumApLicense_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 1, 1, 10),
    _RuckusCtrlSystemNodeNumApLicense_Type()
)
ruckusCtrlSystemNodeNumApLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSystemNodeNumApLicense.setStatus("current")
_RuckusCtrlSystemNodeMgmtIp_Type = IpAddress
_RuckusCtrlSystemNodeMgmtIp_Object = MibTableColumn
ruckusCtrlSystemNodeMgmtIp = _RuckusCtrlSystemNodeMgmtIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 1, 1, 11),
    _RuckusCtrlSystemNodeMgmtIp_Type()
)
ruckusCtrlSystemNodeMgmtIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSystemNodeMgmtIp.setStatus("current")
_RuckusCtrlSystemNodeMgmtIpv6_Type = Ipv6Address
_RuckusCtrlSystemNodeMgmtIpv6_Object = MibTableColumn
ruckusCtrlSystemNodeMgmtIpv6 = _RuckusCtrlSystemNodeMgmtIpv6_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 1, 1, 12),
    _RuckusCtrlSystemNodeMgmtIpv6_Type()
)
ruckusCtrlSystemNodeMgmtIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSystemNodeMgmtIpv6.setStatus("current")
_RuckusCtrlSystemNodeMgmtMac_Type = MacAddress
_RuckusCtrlSystemNodeMgmtMac_Object = MibTableColumn
ruckusCtrlSystemNodeMgmtMac = _RuckusCtrlSystemNodeMgmtMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 1, 1, 13),
    _RuckusCtrlSystemNodeMgmtMac_Type()
)
ruckusCtrlSystemNodeMgmtMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSystemNodeMgmtMac.setStatus("current")
_RuckusCtrlSystemNodeUptime_Type = TimeTicks
_RuckusCtrlSystemNodeUptime_Object = MibTableColumn
ruckusCtrlSystemNodeUptime = _RuckusCtrlSystemNodeUptime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 1, 1, 16),
    _RuckusCtrlSystemNodeUptime_Type()
)
ruckusCtrlSystemNodeUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSystemNodeUptime.setStatus("current")
_RuckusCtrlSystemNodeStatus_Type = RuckusSystemNodeStatus
_RuckusCtrlSystemNodeStatus_Object = MibTableColumn
ruckusCtrlSystemNodeStatus = _RuckusCtrlSystemNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 1, 1, 17),
    _RuckusCtrlSystemNodeStatus_Type()
)
ruckusCtrlSystemNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSystemNodeStatus.setStatus("current")
_RuckusCtrlSystemClusterStatus_Type = RuckusSystemClusterStatus
_RuckusCtrlSystemClusterStatus_Object = MibTableColumn
ruckusCtrlSystemClusterStatus = _RuckusCtrlSystemClusterStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 1, 1, 18),
    _RuckusCtrlSystemClusterStatus_Type()
)
ruckusCtrlSystemClusterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSystemClusterStatus.setStatus("current")
_RuckusCtrlSystemNodeNumApConnected_Type = Unsigned32
_RuckusCtrlSystemNodeNumApConnected_Object = MibTableColumn
ruckusCtrlSystemNodeNumApConnected = _RuckusCtrlSystemNodeNumApConnected_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 1, 1, 19),
    _RuckusCtrlSystemNodeNumApConnected_Type()
)
ruckusCtrlSystemNodeNumApConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSystemNodeNumApConnected.setStatus("current")
_RuckusCtrlSystemNodeClusterHAState_Type = RuckusSystemClusterHAState
_RuckusCtrlSystemNodeClusterHAState_Object = MibTableColumn
ruckusCtrlSystemNodeClusterHAState = _RuckusCtrlSystemNodeClusterHAState_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 1, 1, 26),
    _RuckusCtrlSystemNodeClusterHAState_Type()
)
ruckusCtrlSystemNodeClusterHAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSystemNodeClusterHAState.setStatus("current")
_RuckusCtrlSystemNodeClusterHARoles_Type = RuckusSystemClusterHARole
_RuckusCtrlSystemNodeClusterHARoles_Object = MibTableColumn
ruckusCtrlSystemNodeClusterHARoles = _RuckusCtrlSystemNodeClusterHARoles_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 1, 1, 27),
    _RuckusCtrlSystemNodeClusterHARoles_Type()
)
ruckusCtrlSystemNodeClusterHARoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSystemNodeClusterHARoles.setStatus("current")
_RuckusCTRLDomainTable_Object = MibTable
ruckusCTRLDomainTable = _RuckusCTRLDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruckusCTRLDomainTable.setStatus("current")
_RuckusCTRLDomainEntry_Object = MibTableRow
ruckusCTRLDomainEntry = _RuckusCTRLDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 2, 1)
)
ruckusCTRLDomainEntry.setIndexNames(
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlDomainId"),
)
if mibBuilder.loadTexts:
    ruckusCTRLDomainEntry.setStatus("current")
_RuckusCtrlDomainId_Type = RuckusUUID
_RuckusCtrlDomainId_Object = MibTableColumn
ruckusCtrlDomainId = _RuckusCtrlDomainId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 2, 1, 1),
    _RuckusCtrlDomainId_Type()
)
ruckusCtrlDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlDomainId.setStatus("current")
_RuckusCtrlDomainName_Type = DisplayString
_RuckusCtrlDomainName_Object = MibTableColumn
ruckusCtrlDomainName = _RuckusCtrlDomainName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 2, 1, 2),
    _RuckusCtrlDomainName_Type()
)
ruckusCtrlDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlDomainName.setStatus("current")
_RuckusCtrlDomainParentDomainId_Type = RuckusUUID
_RuckusCtrlDomainParentDomainId_Object = MibTableColumn
ruckusCtrlDomainParentDomainId = _RuckusCtrlDomainParentDomainId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 2, 1, 3),
    _RuckusCtrlDomainParentDomainId_Type()
)
ruckusCtrlDomainParentDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlDomainParentDomainId.setStatus("current")
_RuckusCtrlDomainNumSubdomains_Type = Integer32
_RuckusCtrlDomainNumSubdomains_Object = MibTableColumn
ruckusCtrlDomainNumSubdomains = _RuckusCtrlDomainNumSubdomains_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 2, 1, 8),
    _RuckusCtrlDomainNumSubdomains_Type()
)
ruckusCtrlDomainNumSubdomains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlDomainNumSubdomains.setStatus("current")
_RuckusCtrlDomainNumZones_Type = Integer32
_RuckusCtrlDomainNumZones_Object = MibTableColumn
ruckusCtrlDomainNumZones = _RuckusCtrlDomainNumZones_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 2, 1, 9),
    _RuckusCtrlDomainNumZones_Type()
)
ruckusCtrlDomainNumZones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlDomainNumZones.setStatus("current")
_RuckusCtrlDomainNumApConnected_Type = Integer32
_RuckusCtrlDomainNumApConnected_Object = MibTableColumn
ruckusCtrlDomainNumApConnected = _RuckusCtrlDomainNumApConnected_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 2, 1, 10),
    _RuckusCtrlDomainNumApConnected_Type()
)
ruckusCtrlDomainNumApConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlDomainNumApConnected.setStatus("current")
_RuckusCtrlDomainNumApDisconnected_Type = Integer32
_RuckusCtrlDomainNumApDisconnected_Object = MibTableColumn
ruckusCtrlDomainNumApDisconnected = _RuckusCtrlDomainNumApDisconnected_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 2, 1, 11),
    _RuckusCtrlDomainNumApDisconnected_Type()
)
ruckusCtrlDomainNumApDisconnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlDomainNumApDisconnected.setStatus("current")
_RuckusCTRLZoneTable_Object = MibTable
ruckusCTRLZoneTable = _RuckusCTRLZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ruckusCTRLZoneTable.setStatus("current")
_RuckusCTRLZoneEntry_Object = MibTableRow
ruckusCTRLZoneEntry = _RuckusCTRLZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 3, 1)
)
ruckusCTRLZoneEntry.setIndexNames(
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlZoneDomainId"),
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlZoneId"),
)
if mibBuilder.loadTexts:
    ruckusCTRLZoneEntry.setStatus("current")
_RuckusCtrlZoneDomainId_Type = RuckusUUID
_RuckusCtrlZoneDomainId_Object = MibTableColumn
ruckusCtrlZoneDomainId = _RuckusCtrlZoneDomainId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 3, 1, 1),
    _RuckusCtrlZoneDomainId_Type()
)
ruckusCtrlZoneDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlZoneDomainId.setStatus("current")
_RuckusCtrlZoneId_Type = RuckusUUID
_RuckusCtrlZoneId_Object = MibTableColumn
ruckusCtrlZoneId = _RuckusCtrlZoneId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 3, 1, 2),
    _RuckusCtrlZoneId_Type()
)
ruckusCtrlZoneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlZoneId.setStatus("current")
_RuckusCtrlZoneName_Type = DisplayString
_RuckusCtrlZoneName_Object = MibTableColumn
ruckusCtrlZoneName = _RuckusCtrlZoneName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 3, 1, 3),
    _RuckusCtrlZoneName_Type()
)
ruckusCtrlZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlZoneName.setStatus("current")
_RuckusCtrlZoneCountryCode_Type = RuckusCountryCode
_RuckusCtrlZoneCountryCode_Object = MibTableColumn
ruckusCtrlZoneCountryCode = _RuckusCtrlZoneCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 3, 1, 4),
    _RuckusCtrlZoneCountryCode_Type()
)
ruckusCtrlZoneCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlZoneCountryCode.setStatus("current")
_RuckusCtrlZoneNumApConnected_Type = Integer32
_RuckusCtrlZoneNumApConnected_Object = MibTableColumn
ruckusCtrlZoneNumApConnected = _RuckusCtrlZoneNumApConnected_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 3, 1, 9),
    _RuckusCtrlZoneNumApConnected_Type()
)
ruckusCtrlZoneNumApConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlZoneNumApConnected.setStatus("current")
_RuckusCtrlZoneNumApDisconnected_Type = Integer32
_RuckusCtrlZoneNumApDisconnected_Object = MibTableColumn
ruckusCtrlZoneNumApDisconnected = _RuckusCtrlZoneNumApDisconnected_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 3, 1, 10),
    _RuckusCtrlZoneNumApDisconnected_Type()
)
ruckusCtrlZoneNumApDisconnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlZoneNumApDisconnected.setStatus("current")
_RuckusCTRLApGroupTable_Object = MibTable
ruckusCTRLApGroupTable = _RuckusCTRLApGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ruckusCTRLApGroupTable.setStatus("current")
_RuckusCTRLApGroupEntry_Object = MibTableRow
ruckusCTRLApGroupEntry = _RuckusCTRLApGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 5, 1)
)
ruckusCTRLApGroupEntry.setIndexNames(
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlApGroupZoneId"),
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlApGroupId"),
)
if mibBuilder.loadTexts:
    ruckusCTRLApGroupEntry.setStatus("current")
_RuckusCtrlApGroupZoneId_Type = RuckusUUID
_RuckusCtrlApGroupZoneId_Object = MibTableColumn
ruckusCtrlApGroupZoneId = _RuckusCtrlApGroupZoneId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 5, 1, 1),
    _RuckusCtrlApGroupZoneId_Type()
)
ruckusCtrlApGroupZoneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApGroupZoneId.setStatus("current")
_RuckusCtrlApGroupId_Type = RuckusUUID
_RuckusCtrlApGroupId_Object = MibTableColumn
ruckusCtrlApGroupId = _RuckusCtrlApGroupId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 5, 1, 2),
    _RuckusCtrlApGroupId_Type()
)
ruckusCtrlApGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApGroupId.setStatus("current")


class _RuckusCtrlApGroupName_Type(DisplayString):
    """Custom type ruckusCtrlApGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuckusCtrlApGroupName_Type.__name__ = "DisplayString"
_RuckusCtrlApGroupName_Object = MibTableColumn
ruckusCtrlApGroupName = _RuckusCtrlApGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 5, 1, 3),
    _RuckusCtrlApGroupName_Type()
)
ruckusCtrlApGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApGroupName.setStatus("current")
_RuckusCtrlApGroupNumApConnected_Type = Integer32
_RuckusCtrlApGroupNumApConnected_Object = MibTableColumn
ruckusCtrlApGroupNumApConnected = _RuckusCtrlApGroupNumApConnected_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 5, 1, 9),
    _RuckusCtrlApGroupNumApConnected_Type()
)
ruckusCtrlApGroupNumApConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApGroupNumApConnected.setStatus("current")
_RuckusCtrlApGroupNumApDisconnected_Type = Integer32
_RuckusCtrlApGroupNumApDisconnected_Object = MibTableColumn
ruckusCtrlApGroupNumApDisconnected = _RuckusCtrlApGroupNumApDisconnected_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 5, 1, 10),
    _RuckusCtrlApGroupNumApDisconnected_Type()
)
ruckusCtrlApGroupNumApDisconnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApGroupNumApDisconnected.setStatus("current")
_RuckusCTRLSummaryApTable_Object = MibTable
ruckusCTRLSummaryApTable = _RuckusCTRLSummaryApTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    ruckusCTRLSummaryApTable.setStatus("current")
_RuckusCTRLSummaryApEntry_Object = MibTableRow
ruckusCTRLSummaryApEntry = _RuckusCTRLSummaryApEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 8, 1)
)
ruckusCTRLSummaryApEntry.setIndexNames(
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlSummaryApIndexType"),
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlSummaryApIndexUUID"),
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlSummaryApMac"),
)
if mibBuilder.loadTexts:
    ruckusCTRLSummaryApEntry.setStatus("current")
_RuckusCtrlSummaryApIndexType_Type = RuckusUUIDType
_RuckusCtrlSummaryApIndexType_Object = MibTableColumn
ruckusCtrlSummaryApIndexType = _RuckusCtrlSummaryApIndexType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 8, 1, 1),
    _RuckusCtrlSummaryApIndexType_Type()
)
ruckusCtrlSummaryApIndexType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSummaryApIndexType.setStatus("current")
_RuckusCtrlSummaryApIndexUUID_Type = RuckusUUID
_RuckusCtrlSummaryApIndexUUID_Object = MibTableColumn
ruckusCtrlSummaryApIndexUUID = _RuckusCtrlSummaryApIndexUUID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 8, 1, 2),
    _RuckusCtrlSummaryApIndexUUID_Type()
)
ruckusCtrlSummaryApIndexUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSummaryApIndexUUID.setStatus("current")
_RuckusCtrlSummaryApDomainId_Type = RuckusUUID
_RuckusCtrlSummaryApDomainId_Object = MibTableColumn
ruckusCtrlSummaryApDomainId = _RuckusCtrlSummaryApDomainId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 8, 1, 3),
    _RuckusCtrlSummaryApDomainId_Type()
)
ruckusCtrlSummaryApDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSummaryApDomainId.setStatus("current")
_RuckusCtrlSummaryApZoneId_Type = RuckusUUID
_RuckusCtrlSummaryApZoneId_Object = MibTableColumn
ruckusCtrlSummaryApZoneId = _RuckusCtrlSummaryApZoneId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 8, 1, 4),
    _RuckusCtrlSummaryApZoneId_Type()
)
ruckusCtrlSummaryApZoneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSummaryApZoneId.setStatus("current")
_RuckusCtrlSummaryApApGroupId_Type = RuckusUUID
_RuckusCtrlSummaryApApGroupId_Object = MibTableColumn
ruckusCtrlSummaryApApGroupId = _RuckusCtrlSummaryApApGroupId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 8, 1, 5),
    _RuckusCtrlSummaryApApGroupId_Type()
)
ruckusCtrlSummaryApApGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSummaryApApGroupId.setStatus("current")
_RuckusCtrlSummaryApMac_Type = MacAddress
_RuckusCtrlSummaryApMac_Object = MibTableColumn
ruckusCtrlSummaryApMac = _RuckusCtrlSummaryApMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 8, 1, 6),
    _RuckusCtrlSummaryApMac_Type()
)
ruckusCtrlSummaryApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSummaryApMac.setStatus("current")
_RuckusCtrlSummaryApDomainName_Type = DisplayString
_RuckusCtrlSummaryApDomainName_Object = MibTableColumn
ruckusCtrlSummaryApDomainName = _RuckusCtrlSummaryApDomainName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 8, 1, 11),
    _RuckusCtrlSummaryApDomainName_Type()
)
ruckusCtrlSummaryApDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSummaryApDomainName.setStatus("current")
_RuckusCtrlSummaryApZoneName_Type = DisplayString
_RuckusCtrlSummaryApZoneName_Object = MibTableColumn
ruckusCtrlSummaryApZoneName = _RuckusCtrlSummaryApZoneName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 8, 1, 12),
    _RuckusCtrlSummaryApZoneName_Type()
)
ruckusCtrlSummaryApZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSummaryApZoneName.setStatus("current")
_RuckusCtrlSummaryApName_Type = DisplayString
_RuckusCtrlSummaryApName_Object = MibTableColumn
ruckusCtrlSummaryApName = _RuckusCtrlSummaryApName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 8, 1, 17),
    _RuckusCtrlSummaryApName_Type()
)
ruckusCtrlSummaryApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSummaryApName.setStatus("current")
_RuckusCtrlSummaryApLocation_Type = DisplayString
_RuckusCtrlSummaryApLocation_Object = MibTableColumn
ruckusCtrlSummaryApLocation = _RuckusCtrlSummaryApLocation_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 8, 1, 18),
    _RuckusCtrlSummaryApLocation_Type()
)
ruckusCtrlSummaryApLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlSummaryApLocation.setStatus("current")
_RuckusCTRLApClientTable_Object = MibTable
ruckusCTRLApClientTable = _RuckusCTRLApClientTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    ruckusCTRLApClientTable.setStatus("current")
_RuckusCTRLApClientEntry_Object = MibTableRow
ruckusCTRLApClientEntry = _RuckusCTRLApClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 9, 1)
)
ruckusCTRLApClientEntry.setIndexNames(
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlApClientApMac"),
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlApClientMac"),
)
if mibBuilder.loadTexts:
    ruckusCTRLApClientEntry.setStatus("current")
_RuckusCtrlApClientApMac_Type = MacAddress
_RuckusCtrlApClientApMac_Object = MibTableColumn
ruckusCtrlApClientApMac = _RuckusCtrlApClientApMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 9, 1, 1),
    _RuckusCtrlApClientApMac_Type()
)
ruckusCtrlApClientApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApClientApMac.setStatus("current")
_RuckusCtrlApClientMac_Type = MacAddress
_RuckusCtrlApClientMac_Object = MibTableColumn
ruckusCtrlApClientMac = _RuckusCtrlApClientMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 9, 1, 6),
    _RuckusCtrlApClientMac_Type()
)
ruckusCtrlApClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApClientMac.setStatus("current")
_RuckusCTRLApWiredClientTable_Object = MibTable
ruckusCTRLApWiredClientTable = _RuckusCTRLApWiredClientTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    ruckusCTRLApWiredClientTable.setStatus("current")
_RuckusCTRLApWiredClientEntry_Object = MibTableRow
ruckusCTRLApWiredClientEntry = _RuckusCTRLApWiredClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 11, 1)
)
ruckusCTRLApWiredClientEntry.setIndexNames(
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlApWiredClientApMac"),
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlApWiredClientMac"),
)
if mibBuilder.loadTexts:
    ruckusCTRLApWiredClientEntry.setStatus("current")
_RuckusCtrlApWiredClientApMac_Type = MacAddress
_RuckusCtrlApWiredClientApMac_Object = MibTableColumn
ruckusCtrlApWiredClientApMac = _RuckusCtrlApWiredClientApMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 11, 1, 1),
    _RuckusCtrlApWiredClientApMac_Type()
)
ruckusCtrlApWiredClientApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWiredClientApMac.setStatus("current")
_RuckusCtrlApWiredClientMac_Type = MacAddress
_RuckusCtrlApWiredClientMac_Object = MibTableColumn
ruckusCtrlApWiredClientMac = _RuckusCtrlApWiredClientMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 1, 11, 1, 6),
    _RuckusCtrlApWiredClientMac_Type()
)
ruckusCtrlApWiredClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWiredClientMac.setStatus("current")
_RuckusCTRLWLANInfo_ObjectIdentity = ObjectIdentity
ruckusCTRLWLANInfo = _RuckusCTRLWLANInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2)
)
_RuckusCTRLApTable_Object = MibTable
ruckusCTRLApTable = _RuckusCTRLApTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruckusCTRLApTable.setStatus("current")
_RuckusCTRLApEntry_Object = MibTableRow
ruckusCTRLApEntry = _RuckusCTRLApEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1)
)
ruckusCTRLApEntry.setIndexNames(
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlApMac"),
)
if mibBuilder.loadTexts:
    ruckusCTRLApEntry.setStatus("current")
_RuckusCtrlApMac_Type = MacAddress
_RuckusCtrlApMac_Object = MibTableColumn
ruckusCtrlApMac = _RuckusCtrlApMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 1),
    _RuckusCtrlApMac_Type()
)
ruckusCtrlApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApMac.setStatus("current")
_RuckusCtrlApDomainId_Type = RuckusUUID
_RuckusCtrlApDomainId_Object = MibTableColumn
ruckusCtrlApDomainId = _RuckusCtrlApDomainId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 2),
    _RuckusCtrlApDomainId_Type()
)
ruckusCtrlApDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApDomainId.setStatus("current")
_RuckusCtrlApDomainName_Type = DisplayString
_RuckusCtrlApDomainName_Object = MibTableColumn
ruckusCtrlApDomainName = _RuckusCtrlApDomainName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 3),
    _RuckusCtrlApDomainName_Type()
)
ruckusCtrlApDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApDomainName.setStatus("current")
_RuckusCtrlApZoneId_Type = RuckusUUID
_RuckusCtrlApZoneId_Object = MibTableColumn
ruckusCtrlApZoneId = _RuckusCtrlApZoneId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 4),
    _RuckusCtrlApZoneId_Type()
)
ruckusCtrlApZoneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApZoneId.setStatus("current")
_RuckusCtrlApZoneName_Type = DisplayString
_RuckusCtrlApZoneName_Object = MibTableColumn
ruckusCtrlApZoneName = _RuckusCtrlApZoneName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 5),
    _RuckusCtrlApZoneName_Type()
)
ruckusCtrlApZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApZoneName.setStatus("current")
_RuckusCtrlApApGroupId_Type = RuckusUUID
_RuckusCtrlApApGroupId_Object = MibTableColumn
ruckusCtrlApApGroupId = _RuckusCtrlApApGroupId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 6),
    _RuckusCtrlApApGroupId_Type()
)
ruckusCtrlApApGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApApGroupId.setStatus("current")
_RuckusCtrlApApGroupName_Type = DisplayString
_RuckusCtrlApApGroupName_Object = MibTableColumn
ruckusCtrlApApGroupName = _RuckusCtrlApApGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 7),
    _RuckusCtrlApApGroupName_Type()
)
ruckusCtrlApApGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApApGroupName.setStatus("current")
_RuckusCtrlApIp_Type = IpAddress
_RuckusCtrlApIp_Object = MibTableColumn
ruckusCtrlApIp = _RuckusCtrlApIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 12),
    _RuckusCtrlApIp_Type()
)
ruckusCtrlApIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApIp.setStatus("current")
_RuckusCtrlApIpv6_Type = Ipv6Address
_RuckusCtrlApIpv6_Object = MibTableColumn
ruckusCtrlApIpv6 = _RuckusCtrlApIpv6_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 13),
    _RuckusCtrlApIpv6_Type()
)
ruckusCtrlApIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApIpv6.setStatus("current")
_RuckusCtrlApNetmask_Type = IpAddress
_RuckusCtrlApNetmask_Object = MibTableColumn
ruckusCtrlApNetmask = _RuckusCtrlApNetmask_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 14),
    _RuckusCtrlApNetmask_Type()
)
ruckusCtrlApNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApNetmask.setStatus("current")
_RuckusCtrlApGateway_Type = IpAddress
_RuckusCtrlApGateway_Object = MibTableColumn
ruckusCtrlApGateway = _RuckusCtrlApGateway_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 15),
    _RuckusCtrlApGateway_Type()
)
ruckusCtrlApGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApGateway.setStatus("current")
_RuckusCtrlApIpDnsSvr1_Type = IpAddress
_RuckusCtrlApIpDnsSvr1_Object = MibTableColumn
ruckusCtrlApIpDnsSvr1 = _RuckusCtrlApIpDnsSvr1_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 16),
    _RuckusCtrlApIpDnsSvr1_Type()
)
ruckusCtrlApIpDnsSvr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApIpDnsSvr1.setStatus("current")
_RuckusCtrlApIpDnsSvr2_Type = IpAddress
_RuckusCtrlApIpDnsSvr2_Object = MibTableColumn
ruckusCtrlApIpDnsSvr2 = _RuckusCtrlApIpDnsSvr2_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 17),
    _RuckusCtrlApIpDnsSvr2_Type()
)
ruckusCtrlApIpDnsSvr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApIpDnsSvr2.setStatus("current")
_RuckusCtrlApIpv6DnsSvr1_Type = Ipv6Address
_RuckusCtrlApIpv6DnsSvr1_Object = MibTableColumn
ruckusCtrlApIpv6DnsSvr1 = _RuckusCtrlApIpv6DnsSvr1_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 22),
    _RuckusCtrlApIpv6DnsSvr1_Type()
)
ruckusCtrlApIpv6DnsSvr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApIpv6DnsSvr1.setStatus("current")
_RuckusCtrlApIpv6DnsSvr2_Type = Ipv6Address
_RuckusCtrlApIpv6DnsSvr2_Object = MibTableColumn
ruckusCtrlApIpv6DnsSvr2 = _RuckusCtrlApIpv6DnsSvr2_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 23),
    _RuckusCtrlApIpv6DnsSvr2_Type()
)
ruckusCtrlApIpv6DnsSvr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApIpv6DnsSvr2.setStatus("current")
_RuckusCtrlApName_Type = DisplayString
_RuckusCtrlApName_Object = MibTableColumn
ruckusCtrlApName = _RuckusCtrlApName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 28),
    _RuckusCtrlApName_Type()
)
ruckusCtrlApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApName.setStatus("current")
_RuckusCtrlApDescription_Type = DisplayString
_RuckusCtrlApDescription_Object = MibTableColumn
ruckusCtrlApDescription = _RuckusCtrlApDescription_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 29),
    _RuckusCtrlApDescription_Type()
)
ruckusCtrlApDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApDescription.setStatus("current")
_RuckusCtrlApStatus_Type = RuckusAPStatusType
_RuckusCtrlApStatus_Object = MibTableColumn
ruckusCtrlApStatus = _RuckusCtrlApStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 30),
    _RuckusCtrlApStatus_Type()
)
ruckusCtrlApStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApStatus.setStatus("current")
_RuckusCtrlApModel_Type = DisplayString
_RuckusCtrlApModel_Object = MibTableColumn
ruckusCtrlApModel = _RuckusCtrlApModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 31),
    _RuckusCtrlApModel_Type()
)
ruckusCtrlApModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApModel.setStatus("current")
_RuckusCtrlApSerialNumber_Type = DisplayString
_RuckusCtrlApSerialNumber_Object = MibTableColumn
ruckusCtrlApSerialNumber = _RuckusCtrlApSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 32),
    _RuckusCtrlApSerialNumber_Type()
)
ruckusCtrlApSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApSerialNumber.setStatus("current")
_RuckusCtrlApSwVersion_Type = DisplayString
_RuckusCtrlApSwVersion_Object = MibTableColumn
ruckusCtrlApSwVersion = _RuckusCtrlApSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 33),
    _RuckusCtrlApSwVersion_Type()
)
ruckusCtrlApSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApSwVersion.setStatus("current")
_RuckusCtrlApLocation_Type = DisplayString
_RuckusCtrlApLocation_Object = MibTableColumn
ruckusCtrlApLocation = _RuckusCtrlApLocation_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 34),
    _RuckusCtrlApLocation_Type()
)
ruckusCtrlApLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApLocation.setStatus("current")
_RuckusCtrlApGpsInfo_Type = DisplayString
_RuckusCtrlApGpsInfo_Object = MibTableColumn
ruckusCtrlApGpsInfo = _RuckusCtrlApGpsInfo_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 35),
    _RuckusCtrlApGpsInfo_Type()
)
ruckusCtrlApGpsInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApGpsInfo.setStatus("current")
_RuckusCtrlApTemperature_Type = Integer32
_RuckusCtrlApTemperature_Object = MibTableColumn
ruckusCtrlApTemperature = _RuckusCtrlApTemperature_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 36),
    _RuckusCtrlApTemperature_Type()
)
ruckusCtrlApTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApTemperature.setStatus("current")
_RuckusCtrlApUptime_Type = TimeTicks
_RuckusCtrlApUptime_Object = MibTableColumn
ruckusCtrlApUptime = _RuckusCtrlApUptime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 41),
    _RuckusCtrlApUptime_Type()
)
ruckusCtrlApUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApUptime.setStatus("current")
_RuckusCtrlApLastConfSyncTime_Type = DateAndTime
_RuckusCtrlApLastConfSyncTime_Object = MibTableColumn
ruckusCtrlApLastConfSyncTime = _RuckusCtrlApLastConfSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 45),
    _RuckusCtrlApLastConfSyncTime_Type()
)
ruckusCtrlApLastConfSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApLastConfSyncTime.setStatus("current")
_RuckusCtrlApCpuUtilization_Type = Integer32
_RuckusCtrlApCpuUtilization_Object = MibTableColumn
ruckusCtrlApCpuUtilization = _RuckusCtrlApCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 50),
    _RuckusCtrlApCpuUtilization_Type()
)
ruckusCtrlApCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApCpuUtilization.setStatus("current")
if mibBuilder.loadTexts:
    ruckusCtrlApCpuUtilization.setUnits("percentage")
_RuckusCtrlApTotalMemory_Type = Unsigned32
_RuckusCtrlApTotalMemory_Object = MibTableColumn
ruckusCtrlApTotalMemory = _RuckusCtrlApTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 51),
    _RuckusCtrlApTotalMemory_Type()
)
ruckusCtrlApTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApTotalMemory.setStatus("current")
if mibBuilder.loadTexts:
    ruckusCtrlApTotalMemory.setUnits("kb")
_RuckusCtrlApFreeMemory_Type = Unsigned32
_RuckusCtrlApFreeMemory_Object = MibTableColumn
ruckusCtrlApFreeMemory = _RuckusCtrlApFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 52),
    _RuckusCtrlApFreeMemory_Type()
)
ruckusCtrlApFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApFreeMemory.setStatus("current")
if mibBuilder.loadTexts:
    ruckusCtrlApFreeMemory.setUnits("kb")
_RuckusCtrlApFreeStorage_Type = Integer32
_RuckusCtrlApFreeStorage_Object = MibTableColumn
ruckusCtrlApFreeStorage = _RuckusCtrlApFreeStorage_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 53),
    _RuckusCtrlApFreeStorage_Type()
)
ruckusCtrlApFreeStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApFreeStorage.setStatus("current")
_RuckusCtrlApEtherPortStatus_Type = RuckusEthPortStatusType
_RuckusCtrlApEtherPortStatus_Object = MibTableColumn
ruckusCtrlApEtherPortStatus = _RuckusCtrlApEtherPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 54),
    _RuckusCtrlApEtherPortStatus_Type()
)
ruckusCtrlApEtherPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApEtherPortStatus.setStatus("current")
_RuckusCtrlApCableModemMac_Type = MacAddress
_RuckusCtrlApCableModemMac_Object = MibTableColumn
ruckusCtrlApCableModemMac = _RuckusCtrlApCableModemMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 56),
    _RuckusCtrlApCableModemMac_Type()
)
ruckusCtrlApCableModemMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApCableModemMac.setStatus("current")
_RuckusCtrlApCableModemSerialNumber_Type = DisplayString
_RuckusCtrlApCableModemSerialNumber_Object = MibTableColumn
ruckusCtrlApCableModemSerialNumber = _RuckusCtrlApCableModemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 57),
    _RuckusCtrlApCableModemSerialNumber_Type()
)
ruckusCtrlApCableModemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApCableModemSerialNumber.setStatus("current")
_RuckusCtrlApNumRadios_Type = Integer32
_RuckusCtrlApNumRadios_Object = MibTableColumn
ruckusCtrlApNumRadios = _RuckusCtrlApNumRadios_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 62),
    _RuckusCtrlApNumRadios_Type()
)
ruckusCtrlApNumRadios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApNumRadios.setStatus("current")
_RuckusCtrlApNumWlans_Type = Integer32
_RuckusCtrlApNumWlans_Object = MibTableColumn
ruckusCtrlApNumWlans = _RuckusCtrlApNumWlans_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 63),
    _RuckusCtrlApNumWlans_Type()
)
ruckusCtrlApNumWlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApNumWlans.setStatus("current")
_RuckusCtrlApNumAssocClients_Type = Integer32
_RuckusCtrlApNumAssocClients_Object = MibTableColumn
ruckusCtrlApNumAssocClients = _RuckusCtrlApNumAssocClients_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 65),
    _RuckusCtrlApNumAssocClients_Type()
)
ruckusCtrlApNumAssocClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApNumAssocClients.setStatus("current")
_RuckusCtrlApStatsRxBytes_Type = Counter64
_RuckusCtrlApStatsRxBytes_Object = MibTableColumn
ruckusCtrlApStatsRxBytes = _RuckusCtrlApStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 71),
    _RuckusCtrlApStatsRxBytes_Type()
)
ruckusCtrlApStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApStatsRxBytes.setStatus("current")
_RuckusCtrlApStatsTxBytes_Type = Counter64
_RuckusCtrlApStatsTxBytes_Object = MibTableColumn
ruckusCtrlApStatsTxBytes = _RuckusCtrlApStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 72),
    _RuckusCtrlApStatsTxBytes_Type()
)
ruckusCtrlApStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApStatsTxBytes.setStatus("current")
_RuckusCtrlApStatsRxDataBytes_Type = Counter64
_RuckusCtrlApStatsRxDataBytes_Object = MibTableColumn
ruckusCtrlApStatsRxDataBytes = _RuckusCtrlApStatsRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 73),
    _RuckusCtrlApStatsRxDataBytes_Type()
)
ruckusCtrlApStatsRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApStatsRxDataBytes.setStatus("current")
_RuckusCtrlApStatsTxDataBytes_Type = Counter64
_RuckusCtrlApStatsTxDataBytes_Object = MibTableColumn
ruckusCtrlApStatsTxDataBytes = _RuckusCtrlApStatsTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 74),
    _RuckusCtrlApStatsTxDataBytes_Type()
)
ruckusCtrlApStatsTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApStatsTxDataBytes.setStatus("current")
_RuckusCtrlApStatsRxPkts_Type = Counter64
_RuckusCtrlApStatsRxPkts_Object = MibTableColumn
ruckusCtrlApStatsRxPkts = _RuckusCtrlApStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 77),
    _RuckusCtrlApStatsRxPkts_Type()
)
ruckusCtrlApStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApStatsRxPkts.setStatus("current")
_RuckusCtrlApStatsTxPkts_Type = Counter64
_RuckusCtrlApStatsTxPkts_Object = MibTableColumn
ruckusCtrlApStatsTxPkts = _RuckusCtrlApStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 78),
    _RuckusCtrlApStatsTxPkts_Type()
)
ruckusCtrlApStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApStatsTxPkts.setStatus("current")
_RuckusCtrlApStatsRxDataPkts_Type = Counter64
_RuckusCtrlApStatsRxDataPkts_Object = MibTableColumn
ruckusCtrlApStatsRxDataPkts = _RuckusCtrlApStatsRxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 79),
    _RuckusCtrlApStatsRxDataPkts_Type()
)
ruckusCtrlApStatsRxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApStatsRxDataPkts.setStatus("current")
_RuckusCtrlApStatsTxDataPkts_Type = Counter64
_RuckusCtrlApStatsTxDataPkts_Object = MibTableColumn
ruckusCtrlApStatsTxDataPkts = _RuckusCtrlApStatsTxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 80),
    _RuckusCtrlApStatsTxDataPkts_Type()
)
ruckusCtrlApStatsTxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApStatsTxDataPkts.setStatus("current")
_RuckusCtrlApStatsRxErrorPkts_Type = Counter64
_RuckusCtrlApStatsRxErrorPkts_Object = MibTableColumn
ruckusCtrlApStatsRxErrorPkts = _RuckusCtrlApStatsRxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 81),
    _RuckusCtrlApStatsRxErrorPkts_Type()
)
ruckusCtrlApStatsRxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApStatsRxErrorPkts.setStatus("current")
_RuckusCtrlApStatsTxErrorPkts_Type = Counter64
_RuckusCtrlApStatsTxErrorPkts_Object = MibTableColumn
ruckusCtrlApStatsTxErrorPkts = _RuckusCtrlApStatsTxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 82),
    _RuckusCtrlApStatsTxErrorPkts_Type()
)
ruckusCtrlApStatsTxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApStatsTxErrorPkts.setStatus("current")
_RuckusCtrlApStatsRxDropPkts_Type = Counter64
_RuckusCtrlApStatsRxDropPkts_Object = MibTableColumn
ruckusCtrlApStatsRxDropPkts = _RuckusCtrlApStatsRxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 83),
    _RuckusCtrlApStatsRxDropPkts_Type()
)
ruckusCtrlApStatsRxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApStatsRxDropPkts.setStatus("current")
_RuckusCtrlApStatsTxDropPkts_Type = Counter64
_RuckusCtrlApStatsTxDropPkts_Object = MibTableColumn
ruckusCtrlApStatsTxDropPkts = _RuckusCtrlApStatsTxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 84),
    _RuckusCtrlApStatsTxDropPkts_Type()
)
ruckusCtrlApStatsTxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApStatsTxDropPkts.setStatus("current")
_RuckusCtrlApMeshRole_Type = RuckusMeshRoles
_RuckusCtrlApMeshRole_Object = MibTableColumn
ruckusCtrlApMeshRole = _RuckusCtrlApMeshRole_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 89),
    _RuckusCtrlApMeshRole_Type()
)
ruckusCtrlApMeshRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApMeshRole.setStatus("current")
_RuckusCtrlApNumMeshHops_Type = Integer32
_RuckusCtrlApNumMeshHops_Object = MibTableColumn
ruckusCtrlApNumMeshHops = _RuckusCtrlApNumMeshHops_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 90),
    _RuckusCtrlApNumMeshHops_Type()
)
ruckusCtrlApNumMeshHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApNumMeshHops.setStatus("current")
_RuckusCtrlApConnectScgCpIp_Type = IpAddress
_RuckusCtrlApConnectScgCpIp_Object = MibTableColumn
ruckusCtrlApConnectScgCpIp = _RuckusCtrlApConnectScgCpIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 95),
    _RuckusCtrlApConnectScgCpIp_Type()
)
ruckusCtrlApConnectScgCpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApConnectScgCpIp.setStatus("current")
_RuckusCtrlApConnectScgCpIpv6_Type = Ipv6Address
_RuckusCtrlApConnectScgCpIpv6_Object = MibTableColumn
ruckusCtrlApConnectScgCpIpv6 = _RuckusCtrlApConnectScgCpIpv6_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 96),
    _RuckusCtrlApConnectScgCpIpv6_Type()
)
ruckusCtrlApConnectScgCpIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApConnectScgCpIpv6.setStatus("current")
_RuckusCtrlApConnectScgDpIp_Type = IpAddress
_RuckusCtrlApConnectScgDpIp_Object = MibTableColumn
ruckusCtrlApConnectScgDpIp = _RuckusCtrlApConnectScgDpIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 97),
    _RuckusCtrlApConnectScgDpIp_Type()
)
ruckusCtrlApConnectScgDpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApConnectScgDpIp.setStatus("current")
_RuckusCtrlApConnectScgDpIpv6_Type = Ipv6Address
_RuckusCtrlApConnectScgDpIpv6_Object = MibTableColumn
ruckusCtrlApConnectScgDpIpv6 = _RuckusCtrlApConnectScgDpIpv6_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 98),
    _RuckusCtrlApConnectScgDpIpv6_Type()
)
ruckusCtrlApConnectScgDpIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApConnectScgDpIpv6.setStatus("current")
_RuckusCtrlApLanStatsRxBytes_Type = Counter64
_RuckusCtrlApLanStatsRxBytes_Object = MibTableColumn
ruckusCtrlApLanStatsRxBytes = _RuckusCtrlApLanStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 103),
    _RuckusCtrlApLanStatsRxBytes_Type()
)
ruckusCtrlApLanStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApLanStatsRxBytes.setStatus("current")
_RuckusCtrlApLanStatsTxBytes_Type = Counter64
_RuckusCtrlApLanStatsTxBytes_Object = MibTableColumn
ruckusCtrlApLanStatsTxBytes = _RuckusCtrlApLanStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 104),
    _RuckusCtrlApLanStatsTxBytes_Type()
)
ruckusCtrlApLanStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApLanStatsTxBytes.setStatus("current")
_RuckusCtrlApLanStatsRxPkts_Type = Counter64
_RuckusCtrlApLanStatsRxPkts_Object = MibTableColumn
ruckusCtrlApLanStatsRxPkts = _RuckusCtrlApLanStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 105),
    _RuckusCtrlApLanStatsRxPkts_Type()
)
ruckusCtrlApLanStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApLanStatsRxPkts.setStatus("current")
_RuckusCtrlApLanStatsTxPkts_Type = Counter64
_RuckusCtrlApLanStatsTxPkts_Object = MibTableColumn
ruckusCtrlApLanStatsTxPkts = _RuckusCtrlApLanStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 106),
    _RuckusCtrlApLanStatsTxPkts_Type()
)
ruckusCtrlApLanStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApLanStatsTxPkts.setStatus("current")
_RuckusCtrlApLanStatsRxErrorPkts_Type = Counter64
_RuckusCtrlApLanStatsRxErrorPkts_Object = MibTableColumn
ruckusCtrlApLanStatsRxErrorPkts = _RuckusCtrlApLanStatsRxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 107),
    _RuckusCtrlApLanStatsRxErrorPkts_Type()
)
ruckusCtrlApLanStatsRxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApLanStatsRxErrorPkts.setStatus("current")
_RuckusCtrlApLanStatsTxErrorPkts_Type = Counter64
_RuckusCtrlApLanStatsTxErrorPkts_Object = MibTableColumn
ruckusCtrlApLanStatsTxErrorPkts = _RuckusCtrlApLanStatsTxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 108),
    _RuckusCtrlApLanStatsTxErrorPkts_Type()
)
ruckusCtrlApLanStatsTxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApLanStatsTxErrorPkts.setStatus("current")
_RuckusCtrlApLanStatsRxDroppedPkts_Type = Counter64
_RuckusCtrlApLanStatsRxDroppedPkts_Object = MibTableColumn
ruckusCtrlApLanStatsRxDroppedPkts = _RuckusCtrlApLanStatsRxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 115),
    _RuckusCtrlApLanStatsRxDroppedPkts_Type()
)
ruckusCtrlApLanStatsRxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApLanStatsRxDroppedPkts.setStatus("current")
_RuckusCtrlApLanStatsTxDroppedPkts_Type = Counter64
_RuckusCtrlApLanStatsTxDroppedPkts_Object = MibTableColumn
ruckusCtrlApLanStatsTxDroppedPkts = _RuckusCtrlApLanStatsTxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 116),
    _RuckusCtrlApLanStatsTxDroppedPkts_Type()
)
ruckusCtrlApLanStatsTxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApLanStatsTxDroppedPkts.setStatus("current")
_RuckusCtrlAPIpsecRxBytes_Type = Counter64
_RuckusCtrlAPIpsecRxBytes_Object = MibTableColumn
ruckusCtrlAPIpsecRxBytes = _RuckusCtrlAPIpsecRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 123),
    _RuckusCtrlAPIpsecRxBytes_Type()
)
ruckusCtrlAPIpsecRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlAPIpsecRxBytes.setStatus("current")
_RuckusCtrlAPIpsecTxBytes_Type = Counter64
_RuckusCtrlAPIpsecTxBytes_Object = MibTableColumn
ruckusCtrlAPIpsecTxBytes = _RuckusCtrlAPIpsecTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 124),
    _RuckusCtrlAPIpsecTxBytes_Type()
)
ruckusCtrlAPIpsecTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlAPIpsecTxBytes.setStatus("current")
_RuckusCtrlAPIpsecRxPkts_Type = Counter64
_RuckusCtrlAPIpsecRxPkts_Object = MibTableColumn
ruckusCtrlAPIpsecRxPkts = _RuckusCtrlAPIpsecRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 125),
    _RuckusCtrlAPIpsecRxPkts_Type()
)
ruckusCtrlAPIpsecRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlAPIpsecRxPkts.setStatus("current")
_RuckusCtrlAPIpsecTxPkts_Type = Counter64
_RuckusCtrlAPIpsecTxPkts_Object = MibTableColumn
ruckusCtrlAPIpsecTxPkts = _RuckusCtrlAPIpsecTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 126),
    _RuckusCtrlAPIpsecTxPkts_Type()
)
ruckusCtrlAPIpsecTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlAPIpsecTxPkts.setStatus("current")
_RuckusCtrlAPIpsecRxDropPkts_Type = Counter64
_RuckusCtrlAPIpsecRxDropPkts_Object = MibTableColumn
ruckusCtrlAPIpsecRxDropPkts = _RuckusCtrlAPIpsecRxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 127),
    _RuckusCtrlAPIpsecRxDropPkts_Type()
)
ruckusCtrlAPIpsecRxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlAPIpsecRxDropPkts.setStatus("current")
_RuckusCtrlAPIpsecTxDropPkts_Type = Counter64
_RuckusCtrlAPIpsecTxDropPkts_Object = MibTableColumn
ruckusCtrlAPIpsecTxDropPkts = _RuckusCtrlAPIpsecTxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 128),
    _RuckusCtrlAPIpsecTxDropPkts_Type()
)
ruckusCtrlAPIpsecTxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlAPIpsecTxDropPkts.setStatus("current")
_RuckusCtrlAPIpsecSessionTime_Type = Unsigned32
_RuckusCtrlAPIpsecSessionTime_Object = MibTableColumn
ruckusCtrlAPIpsecSessionTime = _RuckusCtrlAPIpsecSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 129),
    _RuckusCtrlAPIpsecSessionTime_Type()
)
ruckusCtrlAPIpsecSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlAPIpsecSessionTime.setStatus("current")
_RuckusCtrlAPIpsecRxIdleTime_Type = Unsigned32
_RuckusCtrlAPIpsecRxIdleTime_Object = MibTableColumn
ruckusCtrlAPIpsecRxIdleTime = _RuckusCtrlAPIpsecRxIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 130),
    _RuckusCtrlAPIpsecRxIdleTime_Type()
)
ruckusCtrlAPIpsecRxIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlAPIpsecRxIdleTime.setStatus("current")
_RuckusCtrlAPIpsecTxIdleTime_Type = Unsigned32
_RuckusCtrlAPIpsecTxIdleTime_Object = MibTableColumn
ruckusCtrlAPIpsecTxIdleTime = _RuckusCtrlAPIpsecTxIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 1, 1, 131),
    _RuckusCtrlAPIpsecTxIdleTime_Type()
)
ruckusCtrlAPIpsecTxIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlAPIpsecTxIdleTime.setStatus("current")
_RuckusCTRLApRadioTable_Object = MibTable
ruckusCTRLApRadioTable = _RuckusCTRLApRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ruckusCTRLApRadioTable.setStatus("current")
_RuckusCTRLApRadioEntry_Object = MibTableRow
ruckusCTRLApRadioEntry = _RuckusCTRLApRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1)
)
ruckusCTRLApRadioEntry.setIndexNames(
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlApRadioApMac"),
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlApRadioIndex"),
)
if mibBuilder.loadTexts:
    ruckusCTRLApRadioEntry.setStatus("current")
_RuckusCtrlApRadioApMac_Type = MacAddress
_RuckusCtrlApRadioApMac_Object = MibTableColumn
ruckusCtrlApRadioApMac = _RuckusCtrlApRadioApMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 1),
    _RuckusCtrlApRadioApMac_Type()
)
ruckusCtrlApRadioApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioApMac.setStatus("current")


class _RuckusCtrlApRadioIndex_Type(Integer32):
    """Custom type ruckusCtrlApRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuckusCtrlApRadioIndex_Type.__name__ = "Integer32"
_RuckusCtrlApRadioIndex_Object = MibTableColumn
ruckusCtrlApRadioIndex = _RuckusCtrlApRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 2),
    _RuckusCtrlApRadioIndex_Type()
)
ruckusCtrlApRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioIndex.setStatus("current")
_RuckusCtrlApRadioNumWlans_Type = Unsigned32
_RuckusCtrlApRadioNumWlans_Object = MibTableColumn
ruckusCtrlApRadioNumWlans = _RuckusCtrlApRadioNumWlans_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 7),
    _RuckusCtrlApRadioNumWlans_Type()
)
ruckusCtrlApRadioNumWlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioNumWlans.setStatus("current")
_RuckusCtrlApRadioType_Type = RuckusRadioMode
_RuckusCtrlApRadioType_Object = MibTableColumn
ruckusCtrlApRadioType = _RuckusCtrlApRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 8),
    _RuckusCtrlApRadioType_Type()
)
ruckusCtrlApRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioType.setStatus("current")
_RuckusCtrlApRadioChannelWidth_Type = RuckusChannelWidthType
_RuckusCtrlApRadioChannelWidth_Object = MibTableColumn
ruckusCtrlApRadioChannelWidth = _RuckusCtrlApRadioChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 9),
    _RuckusCtrlApRadioChannelWidth_Type()
)
ruckusCtrlApRadioChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioChannelWidth.setStatus("current")
_RuckusCtrlApRadioChannel_Type = Unsigned32
_RuckusCtrlApRadioChannel_Object = MibTableColumn
ruckusCtrlApRadioChannel = _RuckusCtrlApRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 10),
    _RuckusCtrlApRadioChannel_Type()
)
ruckusCtrlApRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioChannel.setStatus("current")
_RuckusCtrlApRadioTxPower_Type = DisplayString
_RuckusCtrlApRadioTxPower_Object = MibTableColumn
ruckusCtrlApRadioTxPower = _RuckusCtrlApRadioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 11),
    _RuckusCtrlApRadioTxPower_Type()
)
ruckusCtrlApRadioTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioTxPower.setStatus("current")


class _RuckusCtrlApRadioBeaconPeriod_Type(Integer32):
    """Custom type ruckusCtrlApRadioBeaconPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_RuckusCtrlApRadioBeaconPeriod_Type.__name__ = "Integer32"
_RuckusCtrlApRadioBeaconPeriod_Object = MibTableColumn
ruckusCtrlApRadioBeaconPeriod = _RuckusCtrlApRadioBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 16),
    _RuckusCtrlApRadioBeaconPeriod_Type()
)
ruckusCtrlApRadioBeaconPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioBeaconPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioBeaconPeriod.setUnits("milliseconds")
_RuckusCtrlApRadioPowerMgmtEnable_Type = Integer32
_RuckusCtrlApRadioPowerMgmtEnable_Object = MibTableColumn
ruckusCtrlApRadioPowerMgmtEnable = _RuckusCtrlApRadioPowerMgmtEnable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 23),
    _RuckusCtrlApRadioPowerMgmtEnable_Type()
)
ruckusCtrlApRadioPowerMgmtEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioPowerMgmtEnable.setStatus("current")
_RuckusCtrlApRadioMeshEnable_Type = Integer32
_RuckusCtrlApRadioMeshEnable_Object = MibTableColumn
ruckusCtrlApRadioMeshEnable = _RuckusCtrlApRadioMeshEnable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 24),
    _RuckusCtrlApRadioMeshEnable_Type()
)
ruckusCtrlApRadioMeshEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioMeshEnable.setStatus("current")
_RuckusCtrlApRadioStatsRxAirtime_Type = Unsigned32
_RuckusCtrlApRadioStatsRxAirtime_Object = MibTableColumn
ruckusCtrlApRadioStatsRxAirtime = _RuckusCtrlApRadioStatsRxAirtime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 29),
    _RuckusCtrlApRadioStatsRxAirtime_Type()
)
ruckusCtrlApRadioStatsRxAirtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsRxAirtime.setStatus("current")
_RuckusCtrlApRadioStatsTxAirtime_Type = Unsigned32
_RuckusCtrlApRadioStatsTxAirtime_Object = MibTableColumn
ruckusCtrlApRadioStatsTxAirtime = _RuckusCtrlApRadioStatsTxAirtime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 30),
    _RuckusCtrlApRadioStatsTxAirtime_Type()
)
ruckusCtrlApRadioStatsTxAirtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsTxAirtime.setStatus("current")
_RuckusCtrlApRadioStatsBusyAirtime_Type = Unsigned32
_RuckusCtrlApRadioStatsBusyAirtime_Object = MibTableColumn
ruckusCtrlApRadioStatsBusyAirtime = _RuckusCtrlApRadioStatsBusyAirtime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 31),
    _RuckusCtrlApRadioStatsBusyAirtime_Type()
)
ruckusCtrlApRadioStatsBusyAirtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsBusyAirtime.setStatus("current")
_RuckusCtrlApRadioStatsTotalAirtime_Type = Unsigned32
_RuckusCtrlApRadioStatsTotalAirtime_Object = MibTableColumn
ruckusCtrlApRadioStatsTotalAirtime = _RuckusCtrlApRadioStatsTotalAirtime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 32),
    _RuckusCtrlApRadioStatsTotalAirtime_Type()
)
ruckusCtrlApRadioStatsTotalAirtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsTotalAirtime.setStatus("current")
_RuckusCtrlApRadioAntennaGain_Type = Unsigned32
_RuckusCtrlApRadioAntennaGain_Object = MibTableColumn
ruckusCtrlApRadioAntennaGain = _RuckusCtrlApRadioAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 38),
    _RuckusCtrlApRadioAntennaGain_Type()
)
ruckusCtrlApRadioAntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioAntennaGain.setStatus("current")
_RuckusCtrlApRadioStatsSnr_Type = Unsigned32
_RuckusCtrlApRadioStatsSnr_Object = MibTableColumn
ruckusCtrlApRadioStatsSnr = _RuckusCtrlApRadioStatsSnr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 39),
    _RuckusCtrlApRadioStatsSnr_Type()
)
ruckusCtrlApRadioStatsSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsSnr.setStatus("current")
_RuckusCtrlApRadioStatsNoiseFloor_Type = Integer32
_RuckusCtrlApRadioStatsNoiseFloor_Object = MibTableColumn
ruckusCtrlApRadioStatsNoiseFloor = _RuckusCtrlApRadioStatsNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 40),
    _RuckusCtrlApRadioStatsNoiseFloor_Type()
)
ruckusCtrlApRadioStatsNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsNoiseFloor.setStatus("current")
_RuckusCtrlApRadioStatsNumAssocClients_Type = Unsigned32
_RuckusCtrlApRadioStatsNumAssocClients_Object = MibTableColumn
ruckusCtrlApRadioStatsNumAssocClients = _RuckusCtrlApRadioStatsNumAssocClients_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 41),
    _RuckusCtrlApRadioStatsNumAssocClients_Type()
)
ruckusCtrlApRadioStatsNumAssocClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsNumAssocClients.setStatus("current")
_RuckusCtrlApRadioStatsNumAuthClients_Type = Unsigned32
_RuckusCtrlApRadioStatsNumAuthClients_Object = MibTableColumn
ruckusCtrlApRadioStatsNumAuthClients = _RuckusCtrlApRadioStatsNumAuthClients_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 42),
    _RuckusCtrlApRadioStatsNumAuthClients_Type()
)
ruckusCtrlApRadioStatsNumAuthClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsNumAuthClients.setStatus("current")
_RuckusCtrlApRadioStatsNumMaxClients_Type = Unsigned32
_RuckusCtrlApRadioStatsNumMaxClients_Object = MibTableColumn
ruckusCtrlApRadioStatsNumMaxClients = _RuckusCtrlApRadioStatsNumMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 43),
    _RuckusCtrlApRadioStatsNumMaxClients_Type()
)
ruckusCtrlApRadioStatsNumMaxClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsNumMaxClients.setStatus("current")
_RuckusCtrlApRadioStatsPhyError_Type = Unsigned32
_RuckusCtrlApRadioStatsPhyError_Object = MibTableColumn
ruckusCtrlApRadioStatsPhyError = _RuckusCtrlApRadioStatsPhyError_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 49),
    _RuckusCtrlApRadioStatsPhyError_Type()
)
ruckusCtrlApRadioStatsPhyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsPhyError.setStatus("current")
_RuckusCtrlApRadioStatsRxWepFail_Type = Counter32
_RuckusCtrlApRadioStatsRxWepFail_Object = MibTableColumn
ruckusCtrlApRadioStatsRxWepFail = _RuckusCtrlApRadioStatsRxWepFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 50),
    _RuckusCtrlApRadioStatsRxWepFail_Type()
)
ruckusCtrlApRadioStatsRxWepFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsRxWepFail.setStatus("current")
_RuckusCtrlApRadioStatsRxDecryptCrcError_Type = Counter32
_RuckusCtrlApRadioStatsRxDecryptCrcError_Object = MibTableColumn
ruckusCtrlApRadioStatsRxDecryptCrcError = _RuckusCtrlApRadioStatsRxDecryptCrcError_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 51),
    _RuckusCtrlApRadioStatsRxDecryptCrcError_Type()
)
ruckusCtrlApRadioStatsRxDecryptCrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsRxDecryptCrcError.setStatus("current")
_RuckusCtrlApRadioStatsRxMicError_Type = Counter32
_RuckusCtrlApRadioStatsRxMicError_Object = MibTableColumn
ruckusCtrlApRadioStatsRxMicError = _RuckusCtrlApRadioStatsRxMicError_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 52),
    _RuckusCtrlApRadioStatsRxMicError_Type()
)
ruckusCtrlApRadioStatsRxMicError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsRxMicError.setStatus("current")
_RuckusCtrlApRadioStatsRxBytes_Type = Counter64
_RuckusCtrlApRadioStatsRxBytes_Object = MibTableColumn
ruckusCtrlApRadioStatsRxBytes = _RuckusCtrlApRadioStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 57),
    _RuckusCtrlApRadioStatsRxBytes_Type()
)
ruckusCtrlApRadioStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsRxBytes.setStatus("current")
_RuckusCtrlApRadioStatsTxBytes_Type = Counter64
_RuckusCtrlApRadioStatsTxBytes_Object = MibTableColumn
ruckusCtrlApRadioStatsTxBytes = _RuckusCtrlApRadioStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 58),
    _RuckusCtrlApRadioStatsTxBytes_Type()
)
ruckusCtrlApRadioStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsTxBytes.setStatus("current")
_RuckusCtrlApRadioStatsRxPkts_Type = Counter64
_RuckusCtrlApRadioStatsRxPkts_Object = MibTableColumn
ruckusCtrlApRadioStatsRxPkts = _RuckusCtrlApRadioStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 59),
    _RuckusCtrlApRadioStatsRxPkts_Type()
)
ruckusCtrlApRadioStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsRxPkts.setStatus("current")
_RuckusCtrlApRadioStatsTxPkts_Type = Counter64
_RuckusCtrlApRadioStatsTxPkts_Object = MibTableColumn
ruckusCtrlApRadioStatsTxPkts = _RuckusCtrlApRadioStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 60),
    _RuckusCtrlApRadioStatsTxPkts_Type()
)
ruckusCtrlApRadioStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsTxPkts.setStatus("current")
_RuckusCtrlApRadioStatsRxMcastPkts_Type = Counter64
_RuckusCtrlApRadioStatsRxMcastPkts_Object = MibTableColumn
ruckusCtrlApRadioStatsRxMcastPkts = _RuckusCtrlApRadioStatsRxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 65),
    _RuckusCtrlApRadioStatsRxMcastPkts_Type()
)
ruckusCtrlApRadioStatsRxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsRxMcastPkts.setStatus("current")
_RuckusCtrlApRadioStatsTxMcastPkts_Type = Counter64
_RuckusCtrlApRadioStatsTxMcastPkts_Object = MibTableColumn
ruckusCtrlApRadioStatsTxMcastPkts = _RuckusCtrlApRadioStatsTxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 66),
    _RuckusCtrlApRadioStatsTxMcastPkts_Type()
)
ruckusCtrlApRadioStatsTxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsTxMcastPkts.setStatus("current")
_RuckusCtrlApRadioStatsRxErrorPkts_Type = Counter64
_RuckusCtrlApRadioStatsRxErrorPkts_Object = MibTableColumn
ruckusCtrlApRadioStatsRxErrorPkts = _RuckusCtrlApRadioStatsRxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 67),
    _RuckusCtrlApRadioStatsRxErrorPkts_Type()
)
ruckusCtrlApRadioStatsRxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsRxErrorPkts.setStatus("current")
_RuckusCtrlApRadioStatsTxErrorPkts_Type = Counter64
_RuckusCtrlApRadioStatsTxErrorPkts_Object = MibTableColumn
ruckusCtrlApRadioStatsTxErrorPkts = _RuckusCtrlApRadioStatsTxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 68),
    _RuckusCtrlApRadioStatsTxErrorPkts_Type()
)
ruckusCtrlApRadioStatsTxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsTxErrorPkts.setStatus("current")
_RuckusCtrlApRadioStatsRxPktErrorRate_Type = Unsigned32
_RuckusCtrlApRadioStatsRxPktErrorRate_Object = MibTableColumn
ruckusCtrlApRadioStatsRxPktErrorRate = _RuckusCtrlApRadioStatsRxPktErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 69),
    _RuckusCtrlApRadioStatsRxPktErrorRate_Type()
)
ruckusCtrlApRadioStatsRxPktErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsRxPktErrorRate.setStatus("current")
_RuckusCtrlApRadioStatsTxPktErrorRate_Type = Unsigned32
_RuckusCtrlApRadioStatsTxPktErrorRate_Object = MibTableColumn
ruckusCtrlApRadioStatsTxPktErrorRate = _RuckusCtrlApRadioStatsTxPktErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 70),
    _RuckusCtrlApRadioStatsTxPktErrorRate_Type()
)
ruckusCtrlApRadioStatsTxPktErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsTxPktErrorRate.setStatus("current")
_RuckusCtrlApRadioStatsTxPktRetryRate_Type = Unsigned32
_RuckusCtrlApRadioStatsTxPktRetryRate_Object = MibTableColumn
ruckusCtrlApRadioStatsTxPktRetryRate = _RuckusCtrlApRadioStatsTxPktRetryRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 71),
    _RuckusCtrlApRadioStatsTxPktRetryRate_Type()
)
ruckusCtrlApRadioStatsTxPktRetryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsTxPktRetryRate.setStatus("current")
_RuckusCtrlApRadioStatsTxRetryPkts_Type = Counter64
_RuckusCtrlApRadioStatsTxRetryPkts_Object = MibTableColumn
ruckusCtrlApRadioStatsTxRetryPkts = _RuckusCtrlApRadioStatsTxRetryPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 73),
    _RuckusCtrlApRadioStatsTxRetryPkts_Type()
)
ruckusCtrlApRadioStatsTxRetryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsTxRetryPkts.setStatus("current")
_RuckusCtrlApRadioStatsRxDropPkts_Type = Counter64
_RuckusCtrlApRadioStatsRxDropPkts_Object = MibTableColumn
ruckusCtrlApRadioStatsRxDropPkts = _RuckusCtrlApRadioStatsRxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 76),
    _RuckusCtrlApRadioStatsRxDropPkts_Type()
)
ruckusCtrlApRadioStatsRxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsRxDropPkts.setStatus("current")
_RuckusCtrlApRadioStatsTxDropPkts_Type = Counter64
_RuckusCtrlApRadioStatsTxDropPkts_Object = MibTableColumn
ruckusCtrlApRadioStatsTxDropPkts = _RuckusCtrlApRadioStatsTxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 77),
    _RuckusCtrlApRadioStatsTxDropPkts_Type()
)
ruckusCtrlApRadioStatsTxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsTxDropPkts.setStatus("current")
_RuckusCtrlApRadioStatsNumAuthReqs_Type = Counter32
_RuckusCtrlApRadioStatsNumAuthReqs_Object = MibTableColumn
ruckusCtrlApRadioStatsNumAuthReqs = _RuckusCtrlApRadioStatsNumAuthReqs_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 82),
    _RuckusCtrlApRadioStatsNumAuthReqs_Type()
)
ruckusCtrlApRadioStatsNumAuthReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsNumAuthReqs.setStatus("current")
_RuckusCtrlApRadioStatsNumAuthResps_Type = Counter32
_RuckusCtrlApRadioStatsNumAuthResps_Object = MibTableColumn
ruckusCtrlApRadioStatsNumAuthResps = _RuckusCtrlApRadioStatsNumAuthResps_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 83),
    _RuckusCtrlApRadioStatsNumAuthResps_Type()
)
ruckusCtrlApRadioStatsNumAuthResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsNumAuthResps.setStatus("current")
_RuckusCtrlApRadioStatsNumAuthSuccess_Type = Counter32
_RuckusCtrlApRadioStatsNumAuthSuccess_Object = MibTableColumn
ruckusCtrlApRadioStatsNumAuthSuccess = _RuckusCtrlApRadioStatsNumAuthSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 84),
    _RuckusCtrlApRadioStatsNumAuthSuccess_Type()
)
ruckusCtrlApRadioStatsNumAuthSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsNumAuthSuccess.setStatus("current")
_RuckusCtrlApRadioStatsNumAuthFail_Type = Counter32
_RuckusCtrlApRadioStatsNumAuthFail_Object = MibTableColumn
ruckusCtrlApRadioStatsNumAuthFail = _RuckusCtrlApRadioStatsNumAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 85),
    _RuckusCtrlApRadioStatsNumAuthFail_Type()
)
ruckusCtrlApRadioStatsNumAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsNumAuthFail.setStatus("current")
_RuckusCtrlApRadioStatsAuthFailRate_Type = Counter32
_RuckusCtrlApRadioStatsAuthFailRate_Object = MibTableColumn
ruckusCtrlApRadioStatsAuthFailRate = _RuckusCtrlApRadioStatsAuthFailRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 86),
    _RuckusCtrlApRadioStatsAuthFailRate_Type()
)
ruckusCtrlApRadioStatsAuthFailRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsAuthFailRate.setStatus("current")
_RuckusCtrlApRadioStatsNumAssocReq_Type = Counter32
_RuckusCtrlApRadioStatsNumAssocReq_Object = MibTableColumn
ruckusCtrlApRadioStatsNumAssocReq = _RuckusCtrlApRadioStatsNumAssocReq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 87),
    _RuckusCtrlApRadioStatsNumAssocReq_Type()
)
ruckusCtrlApRadioStatsNumAssocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsNumAssocReq.setStatus("current")
_RuckusCtrlApRadioStatsNumAssocResp_Type = Counter32
_RuckusCtrlApRadioStatsNumAssocResp_Object = MibTableColumn
ruckusCtrlApRadioStatsNumAssocResp = _RuckusCtrlApRadioStatsNumAssocResp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 88),
    _RuckusCtrlApRadioStatsNumAssocResp_Type()
)
ruckusCtrlApRadioStatsNumAssocResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsNumAssocResp.setStatus("current")
_RuckusCtrlApRadioStatsNumReassocReq_Type = Counter32
_RuckusCtrlApRadioStatsNumReassocReq_Object = MibTableColumn
ruckusCtrlApRadioStatsNumReassocReq = _RuckusCtrlApRadioStatsNumReassocReq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 89),
    _RuckusCtrlApRadioStatsNumReassocReq_Type()
)
ruckusCtrlApRadioStatsNumReassocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsNumReassocReq.setStatus("current")
_RuckusCtrlApRadioStatsNumReassocResp_Type = Counter32
_RuckusCtrlApRadioStatsNumReassocResp_Object = MibTableColumn
ruckusCtrlApRadioStatsNumReassocResp = _RuckusCtrlApRadioStatsNumReassocResp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 90),
    _RuckusCtrlApRadioStatsNumReassocResp_Type()
)
ruckusCtrlApRadioStatsNumReassocResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsNumReassocResp.setStatus("current")
_RuckusCtrlApRadioStatsNumAssocSuccess_Type = Counter32
_RuckusCtrlApRadioStatsNumAssocSuccess_Object = MibTableColumn
ruckusCtrlApRadioStatsNumAssocSuccess = _RuckusCtrlApRadioStatsNumAssocSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 91),
    _RuckusCtrlApRadioStatsNumAssocSuccess_Type()
)
ruckusCtrlApRadioStatsNumAssocSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsNumAssocSuccess.setStatus("current")
_RuckusCtrlApRadioStatsNumAssocFail_Type = Counter32
_RuckusCtrlApRadioStatsNumAssocFail_Object = MibTableColumn
ruckusCtrlApRadioStatsNumAssocFail = _RuckusCtrlApRadioStatsNumAssocFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 92),
    _RuckusCtrlApRadioStatsNumAssocFail_Type()
)
ruckusCtrlApRadioStatsNumAssocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsNumAssocFail.setStatus("current")
_RuckusCtrlApRadioStatsAssocSuccessRate_Type = Unsigned32
_RuckusCtrlApRadioStatsAssocSuccessRate_Object = MibTableColumn
ruckusCtrlApRadioStatsAssocSuccessRate = _RuckusCtrlApRadioStatsAssocSuccessRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 94),
    _RuckusCtrlApRadioStatsAssocSuccessRate_Type()
)
ruckusCtrlApRadioStatsAssocSuccessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsAssocSuccessRate.setStatus("current")
_RuckusCtrlApRadioStatsAssocFailRate_Type = Unsigned32
_RuckusCtrlApRadioStatsAssocFailRate_Object = MibTableColumn
ruckusCtrlApRadioStatsAssocFailRate = _RuckusCtrlApRadioStatsAssocFailRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 3, 1, 95),
    _RuckusCtrlApRadioStatsAssocFailRate_Type()
)
ruckusCtrlApRadioStatsAssocFailRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApRadioStatsAssocFailRate.setStatus("current")
_RuckusCTRLApWlanTable_Object = MibTable
ruckusCTRLApWlanTable = _RuckusCTRLApWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ruckusCTRLApWlanTable.setStatus("current")
_RuckusCTRLApWlanEntry_Object = MibTableRow
ruckusCTRLApWlanEntry = _RuckusCTRLApWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1)
)
ruckusCTRLApWlanEntry.setIndexNames(
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlApWlanApMac"),
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlApWlanRadioIndex"),
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlApWlanBssid"),
)
if mibBuilder.loadTexts:
    ruckusCTRLApWlanEntry.setStatus("current")
_RuckusCtrlApWlanApMac_Type = MacAddress
_RuckusCtrlApWlanApMac_Object = MibTableColumn
ruckusCtrlApWlanApMac = _RuckusCtrlApWlanApMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 1),
    _RuckusCtrlApWlanApMac_Type()
)
ruckusCtrlApWlanApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanApMac.setStatus("current")


class _RuckusCtrlApWlanRadioIndex_Type(Integer32):
    """Custom type ruckusCtrlApWlanRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_RuckusCtrlApWlanRadioIndex_Type.__name__ = "Integer32"
_RuckusCtrlApWlanRadioIndex_Object = MibTableColumn
ruckusCtrlApWlanRadioIndex = _RuckusCtrlApWlanRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 2),
    _RuckusCtrlApWlanRadioIndex_Type()
)
ruckusCtrlApWlanRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanRadioIndex.setStatus("current")
_RuckusCtrlApWlanBssid_Type = MacAddress
_RuckusCtrlApWlanBssid_Object = MibTableColumn
ruckusCtrlApWlanBssid = _RuckusCtrlApWlanBssid_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 3),
    _RuckusCtrlApWlanBssid_Type()
)
ruckusCtrlApWlanBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanBssid.setStatus("current")
_RuckusCtrlApWlanAuthMethod_Type = RuckusWLANAuthMethodType
_RuckusCtrlApWlanAuthMethod_Object = MibTableColumn
ruckusCtrlApWlanAuthMethod = _RuckusCtrlApWlanAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 8),
    _RuckusCtrlApWlanAuthMethod_Type()
)
ruckusCtrlApWlanAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanAuthMethod.setStatus("current")
_RuckusCtrlApWlanEncryptMethod_Type = RuckusWLANEncryptionType
_RuckusCtrlApWlanEncryptMethod_Object = MibTableColumn
ruckusCtrlApWlanEncryptMethod = _RuckusCtrlApWlanEncryptMethod_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 9),
    _RuckusCtrlApWlanEncryptMethod_Type()
)
ruckusCtrlApWlanEncryptMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanEncryptMethod.setStatus("current")


class _RuckusCtrlApWlanId_Type(Unsigned32):
    """Custom type ruckusCtrlApWlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_RuckusCtrlApWlanId_Type.__name__ = "Unsigned32"
_RuckusCtrlApWlanId_Object = MibTableColumn
ruckusCtrlApWlanId = _RuckusCtrlApWlanId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 10),
    _RuckusCtrlApWlanId_Type()
)
ruckusCtrlApWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanId.setStatus("current")
_RuckusCtrlApWlanName_Type = DisplayString
_RuckusCtrlApWlanName_Object = MibTableColumn
ruckusCtrlApWlanName = _RuckusCtrlApWlanName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 11),
    _RuckusCtrlApWlanName_Type()
)
ruckusCtrlApWlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanName.setStatus("current")
_RuckusCtrlApWlanRadioChannel_Type = Integer32
_RuckusCtrlApWlanRadioChannel_Object = MibTableColumn
ruckusCtrlApWlanRadioChannel = _RuckusCtrlApWlanRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 12),
    _RuckusCtrlApWlanRadioChannel_Type()
)
ruckusCtrlApWlanRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanRadioChannel.setStatus("current")
_RuckusCtrlApWlanSsid_Type = RuckusSSID
_RuckusCtrlApWlanSsid_Object = MibTableColumn
ruckusCtrlApWlanSsid = _RuckusCtrlApWlanSsid_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 13),
    _RuckusCtrlApWlanSsid_Type()
)
ruckusCtrlApWlanSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanSsid.setStatus("current")


class _RuckusCtrlApWlanVlanId_Type(Integer32):
    """Custom type ruckusCtrlApWlanVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuckusCtrlApWlanVlanId_Type.__name__ = "Integer32"
_RuckusCtrlApWlanVlanId_Object = MibTableColumn
ruckusCtrlApWlanVlanId = _RuckusCtrlApWlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 14),
    _RuckusCtrlApWlanVlanId_Type()
)
ruckusCtrlApWlanVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanVlanId.setStatus("current")


class _RuckusCtrlApWlanRtsThreshold_Type(Integer32):
    """Custom type ruckusCtrlApWlanRtsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_RuckusCtrlApWlanRtsThreshold_Type.__name__ = "Integer32"
_RuckusCtrlApWlanRtsThreshold_Object = MibTableColumn
ruckusCtrlApWlanRtsThreshold = _RuckusCtrlApWlanRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 15),
    _RuckusCtrlApWlanRtsThreshold_Type()
)
ruckusCtrlApWlanRtsThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanRtsThreshold.setStatus("current")
_RuckusCtrlApWlanDownRateLimit_Type = Integer32
_RuckusCtrlApWlanDownRateLimit_Object = MibTableColumn
ruckusCtrlApWlanDownRateLimit = _RuckusCtrlApWlanDownRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 19),
    _RuckusCtrlApWlanDownRateLimit_Type()
)
ruckusCtrlApWlanDownRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanDownRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanDownRateLimit.setUnits("kbps")
_RuckusCtrlApWlanUpRateLimit_Type = Integer32
_RuckusCtrlApWlanUpRateLimit_Object = MibTableColumn
ruckusCtrlApWlanUpRateLimit = _RuckusCtrlApWlanUpRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 20),
    _RuckusCtrlApWlanUpRateLimit_Type()
)
ruckusCtrlApWlanUpRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanUpRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanUpRateLimit.setUnits("kbps")
_RuckusCtrlApWlanIsBcastDisable_Type = TruthValue
_RuckusCtrlApWlanIsBcastDisable_Object = MibTableColumn
ruckusCtrlApWlanIsBcastDisable = _RuckusCtrlApWlanIsBcastDisable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 25),
    _RuckusCtrlApWlanIsBcastDisable_Type()
)
ruckusCtrlApWlanIsBcastDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanIsBcastDisable.setStatus("current")
_RuckusCtrlApWlanIsGuest_Type = TruthValue
_RuckusCtrlApWlanIsGuest_Object = MibTableColumn
ruckusCtrlApWlanIsGuest = _RuckusCtrlApWlanIsGuest_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 26),
    _RuckusCtrlApWlanIsGuest_Type()
)
ruckusCtrlApWlanIsGuest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanIsGuest.setStatus("current")
_RuckusCtrlApWlanIsTunnel_Type = TruthValue
_RuckusCtrlApWlanIsTunnel_Object = MibTableColumn
ruckusCtrlApWlanIsTunnel = _RuckusCtrlApWlanIsTunnel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 27),
    _RuckusCtrlApWlanIsTunnel_Type()
)
ruckusCtrlApWlanIsTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanIsTunnel.setStatus("current")
_RuckusCtrlApWlanStatsNumAssocClients_Type = Unsigned32
_RuckusCtrlApWlanStatsNumAssocClients_Object = MibTableColumn
ruckusCtrlApWlanStatsNumAssocClients = _RuckusCtrlApWlanStatsNumAssocClients_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 32),
    _RuckusCtrlApWlanStatsNumAssocClients_Type()
)
ruckusCtrlApWlanStatsNumAssocClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsNumAssocClients.setStatus("current")
_RuckusCtrlApWlanStatsRxPkts_Type = Counter64
_RuckusCtrlApWlanStatsRxPkts_Object = MibTableColumn
ruckusCtrlApWlanStatsRxPkts = _RuckusCtrlApWlanStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 37),
    _RuckusCtrlApWlanStatsRxPkts_Type()
)
ruckusCtrlApWlanStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsRxPkts.setStatus("current")
_RuckusCtrlApWlanStatsTxPkts_Type = Counter64
_RuckusCtrlApWlanStatsTxPkts_Object = MibTableColumn
ruckusCtrlApWlanStatsTxPkts = _RuckusCtrlApWlanStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 38),
    _RuckusCtrlApWlanStatsTxPkts_Type()
)
ruckusCtrlApWlanStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsTxPkts.setStatus("current")
_RuckusCtrlApWlanStatsRxBytes_Type = Counter64
_RuckusCtrlApWlanStatsRxBytes_Object = MibTableColumn
ruckusCtrlApWlanStatsRxBytes = _RuckusCtrlApWlanStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 39),
    _RuckusCtrlApWlanStatsRxBytes_Type()
)
ruckusCtrlApWlanStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsRxBytes.setStatus("current")
_RuckusCtrlApWlanStatsTxBytes_Type = Counter64
_RuckusCtrlApWlanStatsTxBytes_Object = MibTableColumn
ruckusCtrlApWlanStatsTxBytes = _RuckusCtrlApWlanStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 40),
    _RuckusCtrlApWlanStatsTxBytes_Type()
)
ruckusCtrlApWlanStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsTxBytes.setStatus("current")
_RuckusCtrlApWlanStatsRxDataBytes_Type = Counter64
_RuckusCtrlApWlanStatsRxDataBytes_Object = MibTableColumn
ruckusCtrlApWlanStatsRxDataBytes = _RuckusCtrlApWlanStatsRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 47),
    _RuckusCtrlApWlanStatsRxDataBytes_Type()
)
ruckusCtrlApWlanStatsRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsRxDataBytes.setStatus("current")
_RuckusCtrlApWlanStatsTxDataBytes_Type = Counter64
_RuckusCtrlApWlanStatsTxDataBytes_Object = MibTableColumn
ruckusCtrlApWlanStatsTxDataBytes = _RuckusCtrlApWlanStatsTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 48),
    _RuckusCtrlApWlanStatsTxDataBytes_Type()
)
ruckusCtrlApWlanStatsTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsTxDataBytes.setStatus("current")
_RuckusCtrlApWlanStatsRxDataPkts_Type = Counter64
_RuckusCtrlApWlanStatsRxDataPkts_Object = MibTableColumn
ruckusCtrlApWlanStatsRxDataPkts = _RuckusCtrlApWlanStatsRxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 49),
    _RuckusCtrlApWlanStatsRxDataPkts_Type()
)
ruckusCtrlApWlanStatsRxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsRxDataPkts.setStatus("current")
_RuckusCtrlApWlanStatsTxDataPkts_Type = Counter64
_RuckusCtrlApWlanStatsTxDataPkts_Object = MibTableColumn
ruckusCtrlApWlanStatsTxDataPkts = _RuckusCtrlApWlanStatsTxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 50),
    _RuckusCtrlApWlanStatsTxDataPkts_Type()
)
ruckusCtrlApWlanStatsTxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsTxDataPkts.setStatus("current")
_RuckusCtrlApWlanStatsRxBcastDataPkts_Type = Counter64
_RuckusCtrlApWlanStatsRxBcastDataPkts_Object = MibTableColumn
ruckusCtrlApWlanStatsRxBcastDataPkts = _RuckusCtrlApWlanStatsRxBcastDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 55),
    _RuckusCtrlApWlanStatsRxBcastDataPkts_Type()
)
ruckusCtrlApWlanStatsRxBcastDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsRxBcastDataPkts.setStatus("current")
_RuckusCtrlApWlanStatsTxBcastDataPkts_Type = Counter64
_RuckusCtrlApWlanStatsTxBcastDataPkts_Object = MibTableColumn
ruckusCtrlApWlanStatsTxBcastDataPkts = _RuckusCtrlApWlanStatsTxBcastDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 56),
    _RuckusCtrlApWlanStatsTxBcastDataPkts_Type()
)
ruckusCtrlApWlanStatsTxBcastDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsTxBcastDataPkts.setStatus("current")
_RuckusCtrlApWlanStatsRxMcastDataPkts_Type = Counter64
_RuckusCtrlApWlanStatsRxMcastDataPkts_Object = MibTableColumn
ruckusCtrlApWlanStatsRxMcastDataPkts = _RuckusCtrlApWlanStatsRxMcastDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 57),
    _RuckusCtrlApWlanStatsRxMcastDataPkts_Type()
)
ruckusCtrlApWlanStatsRxMcastDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsRxMcastDataPkts.setStatus("current")
_RuckusCtrlApWlanStatsTxMcastDataPkts_Type = Counter64
_RuckusCtrlApWlanStatsTxMcastDataPkts_Object = MibTableColumn
ruckusCtrlApWlanStatsTxMcastDataPkts = _RuckusCtrlApWlanStatsTxMcastDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 58),
    _RuckusCtrlApWlanStatsTxMcastDataPkts_Type()
)
ruckusCtrlApWlanStatsTxMcastDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsTxMcastDataPkts.setStatus("current")
_RuckusCtrlApWlanStatsNumAssocReq_Type = Counter32
_RuckusCtrlApWlanStatsNumAssocReq_Object = MibTableColumn
ruckusCtrlApWlanStatsNumAssocReq = _RuckusCtrlApWlanStatsNumAssocReq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 78),
    _RuckusCtrlApWlanStatsNumAssocReq_Type()
)
ruckusCtrlApWlanStatsNumAssocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsNumAssocReq.setStatus("current")
_RuckusCtrlApWlanStatsNumAssocResp_Type = Counter32
_RuckusCtrlApWlanStatsNumAssocResp_Object = MibTableColumn
ruckusCtrlApWlanStatsNumAssocResp = _RuckusCtrlApWlanStatsNumAssocResp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 79),
    _RuckusCtrlApWlanStatsNumAssocResp_Type()
)
ruckusCtrlApWlanStatsNumAssocResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsNumAssocResp.setStatus("current")
_RuckusCtrlApWlanStatsNumReassocReq_Type = Counter32
_RuckusCtrlApWlanStatsNumReassocReq_Object = MibTableColumn
ruckusCtrlApWlanStatsNumReassocReq = _RuckusCtrlApWlanStatsNumReassocReq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 80),
    _RuckusCtrlApWlanStatsNumReassocReq_Type()
)
ruckusCtrlApWlanStatsNumReassocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsNumReassocReq.setStatus("current")
_RuckusCtrlApWlanStatsNumReassocResp_Type = Counter32
_RuckusCtrlApWlanStatsNumReassocResp_Object = MibTableColumn
ruckusCtrlApWlanStatsNumReassocResp = _RuckusCtrlApWlanStatsNumReassocResp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 81),
    _RuckusCtrlApWlanStatsNumReassocResp_Type()
)
ruckusCtrlApWlanStatsNumReassocResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsNumReassocResp.setStatus("current")
_RuckusCtrlApWlanStatsNumAuthReq_Type = Counter32
_RuckusCtrlApWlanStatsNumAuthReq_Object = MibTableColumn
ruckusCtrlApWlanStatsNumAuthReq = _RuckusCtrlApWlanStatsNumAuthReq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 89),
    _RuckusCtrlApWlanStatsNumAuthReq_Type()
)
ruckusCtrlApWlanStatsNumAuthReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsNumAuthReq.setStatus("current")
_RuckusCtrlApWlanStatsNumAuthResp_Type = Counter32
_RuckusCtrlApWlanStatsNumAuthResp_Object = MibTableColumn
ruckusCtrlApWlanStatsNumAuthResp = _RuckusCtrlApWlanStatsNumAuthResp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 90),
    _RuckusCtrlApWlanStatsNumAuthResp_Type()
)
ruckusCtrlApWlanStatsNumAuthResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsNumAuthResp.setStatus("current")
_RuckusCtrlApWlanStatsNumAuthSuccess_Type = Counter32
_RuckusCtrlApWlanStatsNumAuthSuccess_Object = MibTableColumn
ruckusCtrlApWlanStatsNumAuthSuccess = _RuckusCtrlApWlanStatsNumAuthSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 91),
    _RuckusCtrlApWlanStatsNumAuthSuccess_Type()
)
ruckusCtrlApWlanStatsNumAuthSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsNumAuthSuccess.setStatus("current")
_RuckusCtrlApWlanStatsNumAuthFail_Type = Counter32
_RuckusCtrlApWlanStatsNumAuthFail_Object = MibTableColumn
ruckusCtrlApWlanStatsNumAuthFail = _RuckusCtrlApWlanStatsNumAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 92),
    _RuckusCtrlApWlanStatsNumAuthFail_Type()
)
ruckusCtrlApWlanStatsNumAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsNumAuthFail.setStatus("current")
_RuckusCtrlApWlanStatsAuthFailRate_Type = Unsigned32
_RuckusCtrlApWlanStatsAuthFailRate_Object = MibTableColumn
ruckusCtrlApWlanStatsAuthFailRate = _RuckusCtrlApWlanStatsAuthFailRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 93),
    _RuckusCtrlApWlanStatsAuthFailRate_Type()
)
ruckusCtrlApWlanStatsAuthFailRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsAuthFailRate.setStatus("current")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsAuthFailRate.setUnits("percentage")
_RuckusCtrlApWlanStatsNumAssocFail_Type = Counter32
_RuckusCtrlApWlanStatsNumAssocFail_Object = MibTableColumn
ruckusCtrlApWlanStatsNumAssocFail = _RuckusCtrlApWlanStatsNumAssocFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 5, 1, 98),
    _RuckusCtrlApWlanStatsNumAssocFail_Type()
)
ruckusCtrlApWlanStatsNumAssocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlApWlanStatsNumAssocFail.setStatus("current")
_RuckusCTRLClientTable_Object = MibTable
ruckusCTRLClientTable = _RuckusCTRLClientTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    ruckusCTRLClientTable.setStatus("current")
_RuckusCTRLClientEntry_Object = MibTableRow
ruckusCTRLClientEntry = _RuckusCTRLClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1)
)
ruckusCTRLClientEntry.setIndexNames(
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlClientMac"),
)
if mibBuilder.loadTexts:
    ruckusCTRLClientEntry.setStatus("current")
_RuckusCtrlClientMac_Type = MacAddress
_RuckusCtrlClientMac_Object = MibTableColumn
ruckusCtrlClientMac = _RuckusCtrlClientMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 1),
    _RuckusCtrlClientMac_Type()
)
ruckusCtrlClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientMac.setStatus("current")
_RuckusCtrlClientIp_Type = IpAddress
_RuckusCtrlClientIp_Object = MibTableColumn
ruckusCtrlClientIp = _RuckusCtrlClientIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 6),
    _RuckusCtrlClientIp_Type()
)
ruckusCtrlClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientIp.setStatus("current")
_RuckusCtrlClientIpv6_Type = Ipv6Address
_RuckusCtrlClientIpv6_Object = MibTableColumn
ruckusCtrlClientIpv6 = _RuckusCtrlClientIpv6_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 7),
    _RuckusCtrlClientIpv6_Type()
)
ruckusCtrlClientIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientIpv6.setStatus("current")
_RuckusCtrlClientApMac_Type = MacAddress
_RuckusCtrlClientApMac_Object = MibTableColumn
ruckusCtrlClientApMac = _RuckusCtrlClientApMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 8),
    _RuckusCtrlClientApMac_Type()
)
ruckusCtrlClientApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientApMac.setStatus("current")
_RuckusCtrlClientWlanBssid_Type = MacAddress
_RuckusCtrlClientWlanBssid_Object = MibTableColumn
ruckusCtrlClientWlanBssid = _RuckusCtrlClientWlanBssid_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 9),
    _RuckusCtrlClientWlanBssid_Type()
)
ruckusCtrlClientWlanBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientWlanBssid.setStatus("current")
_RuckusCtrlClientSsid_Type = RuckusSSID
_RuckusCtrlClientSsid_Object = MibTableColumn
ruckusCtrlClientSsid = _RuckusCtrlClientSsid_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 10),
    _RuckusCtrlClientSsid_Type()
)
ruckusCtrlClientSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientSsid.setStatus("current")
_RuckusCtrlClientRadioIndex_Type = Integer32
_RuckusCtrlClientRadioIndex_Object = MibTableColumn
ruckusCtrlClientRadioIndex = _RuckusCtrlClientRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 12),
    _RuckusCtrlClientRadioIndex_Type()
)
ruckusCtrlClientRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientRadioIndex.setStatus("current")
_RuckusCtrlClientRadioType_Type = RuckusRadioMode
_RuckusCtrlClientRadioType_Object = MibTableColumn
ruckusCtrlClientRadioType = _RuckusCtrlClientRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 13),
    _RuckusCtrlClientRadioType_Type()
)
ruckusCtrlClientRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientRadioType.setStatus("current")
_RuckusCtrlClientRadioChannel_Type = Integer32
_RuckusCtrlClientRadioChannel_Object = MibTableColumn
ruckusCtrlClientRadioChannel = _RuckusCtrlClientRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 14),
    _RuckusCtrlClientRadioChannel_Type()
)
ruckusCtrlClientRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientRadioChannel.setStatus("current")
_RuckusCtrlClientUsername_Type = DisplayString
_RuckusCtrlClientUsername_Object = MibTableColumn
ruckusCtrlClientUsername = _RuckusCtrlClientUsername_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 15),
    _RuckusCtrlClientUsername_Type()
)
ruckusCtrlClientUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientUsername.setStatus("current")
_RuckusCtrlClientVlanId_Type = Integer32
_RuckusCtrlClientVlanId_Object = MibTableColumn
ruckusCtrlClientVlanId = _RuckusCtrlClientVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 18),
    _RuckusCtrlClientVlanId_Type()
)
ruckusCtrlClientVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientVlanId.setStatus("current")
_RuckusCtrlClientOsType_Type = DisplayString
_RuckusCtrlClientOsType_Object = MibTableColumn
ruckusCtrlClientOsType = _RuckusCtrlClientOsType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 19),
    _RuckusCtrlClientOsType_Type()
)
ruckusCtrlClientOsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientOsType.setStatus("current")
_RuckusCtrlClientStatus_Type = RuckusAuthStatusType
_RuckusCtrlClientStatus_Object = MibTableColumn
ruckusCtrlClientStatus = _RuckusCtrlClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 20),
    _RuckusCtrlClientStatus_Type()
)
ruckusCtrlClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientStatus.setStatus("current")
_RuckusCtrlClientAuthMode_Type = DisplayString
_RuckusCtrlClientAuthMode_Object = MibTableColumn
ruckusCtrlClientAuthMode = _RuckusCtrlClientAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 29),
    _RuckusCtrlClientAuthMode_Type()
)
ruckusCtrlClientAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientAuthMode.setStatus("current")
_RuckusCtrlClientStatsRssi_Type = Integer32
_RuckusCtrlClientStatsRssi_Object = MibTableColumn
ruckusCtrlClientStatsRssi = _RuckusCtrlClientStatsRssi_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 41),
    _RuckusCtrlClientStatsRssi_Type()
)
ruckusCtrlClientStatsRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientStatsRssi.setStatus("current")
_RuckusCtrlClientStatsSnr_Type = RuckusdB
_RuckusCtrlClientStatsSnr_Object = MibTableColumn
ruckusCtrlClientStatsSnr = _RuckusCtrlClientStatsSnr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 42),
    _RuckusCtrlClientStatsSnr_Type()
)
ruckusCtrlClientStatsSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientStatsSnr.setStatus("current")
_RuckusCtrlClientStatsNoiseFloor_Type = RuckusdB
_RuckusCtrlClientStatsNoiseFloor_Object = MibTableColumn
ruckusCtrlClientStatsNoiseFloor = _RuckusCtrlClientStatsNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 43),
    _RuckusCtrlClientStatsNoiseFloor_Type()
)
ruckusCtrlClientStatsNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientStatsNoiseFloor.setStatus("current")
_RuckusCtrlClientStatsThroughput_Type = Unsigned32
_RuckusCtrlClientStatsThroughput_Object = MibTableColumn
ruckusCtrlClientStatsThroughput = _RuckusCtrlClientStatsThroughput_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 44),
    _RuckusCtrlClientStatsThroughput_Type()
)
ruckusCtrlClientStatsThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientStatsThroughput.setStatus("current")
if mibBuilder.loadTexts:
    ruckusCtrlClientStatsThroughput.setUnits("kbps")
_RuckusCtrlClientStatsRxDataBytes_Type = Counter64
_RuckusCtrlClientStatsRxDataBytes_Object = MibTableColumn
ruckusCtrlClientStatsRxDataBytes = _RuckusCtrlClientStatsRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 49),
    _RuckusCtrlClientStatsRxDataBytes_Type()
)
ruckusCtrlClientStatsRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientStatsRxDataBytes.setStatus("current")
_RuckusCtrlClientStatsTxDataBytes_Type = Counter64
_RuckusCtrlClientStatsTxDataBytes_Object = MibTableColumn
ruckusCtrlClientStatsTxDataBytes = _RuckusCtrlClientStatsTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 50),
    _RuckusCtrlClientStatsTxDataBytes_Type()
)
ruckusCtrlClientStatsTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientStatsTxDataBytes.setStatus("current")
_RuckusCtrlClientStatsRxDataPkts_Type = Counter64
_RuckusCtrlClientStatsRxDataPkts_Object = MibTableColumn
ruckusCtrlClientStatsRxDataPkts = _RuckusCtrlClientStatsRxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 51),
    _RuckusCtrlClientStatsRxDataPkts_Type()
)
ruckusCtrlClientStatsRxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientStatsRxDataPkts.setStatus("current")
_RuckusCtrlClientStatsTxDataPkts_Type = Counter64
_RuckusCtrlClientStatsTxDataPkts_Object = MibTableColumn
ruckusCtrlClientStatsTxDataPkts = _RuckusCtrlClientStatsTxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 52),
    _RuckusCtrlClientStatsTxDataPkts_Type()
)
ruckusCtrlClientStatsTxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientStatsTxDataPkts.setStatus("current")
_RuckusCtrlClientStatsTxAvgByteRate_Type = Unsigned32
_RuckusCtrlClientStatsTxAvgByteRate_Object = MibTableColumn
ruckusCtrlClientStatsTxAvgByteRate = _RuckusCtrlClientStatsTxAvgByteRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 56),
    _RuckusCtrlClientStatsTxAvgByteRate_Type()
)
ruckusCtrlClientStatsTxAvgByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientStatsTxAvgByteRate.setStatus("current")
if mibBuilder.loadTexts:
    ruckusCtrlClientStatsTxAvgByteRate.setUnits("kbps")
_RuckusCtrlClientStatsTxRetry_Type = Counter32
_RuckusCtrlClientStatsTxRetry_Object = MibTableColumn
ruckusCtrlClientStatsTxRetry = _RuckusCtrlClientStatsTxRetry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 57),
    _RuckusCtrlClientStatsTxRetry_Type()
)
ruckusCtrlClientStatsTxRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientStatsTxRetry.setStatus("current")
_RuckusCtrlClientStatsRxError_Type = Counter32
_RuckusCtrlClientStatsRxError_Object = MibTableColumn
ruckusCtrlClientStatsRxError = _RuckusCtrlClientStatsRxError_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 58),
    _RuckusCtrlClientStatsRxError_Type()
)
ruckusCtrlClientStatsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientStatsRxError.setStatus("current")
_RuckusCtrlClientStatsTxError_Type = Counter32
_RuckusCtrlClientStatsTxError_Object = MibTableColumn
ruckusCtrlClientStatsTxError = _RuckusCtrlClientStatsTxError_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 59),
    _RuckusCtrlClientStatsTxError_Type()
)
ruckusCtrlClientStatsTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientStatsTxError.setStatus("current")
_RuckusCtrlClientStatsTxRetryBytes_Type = Counter32
_RuckusCtrlClientStatsTxRetryBytes_Object = MibTableColumn
ruckusCtrlClientStatsTxRetryBytes = _RuckusCtrlClientStatsTxRetryBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 61),
    _RuckusCtrlClientStatsTxRetryBytes_Type()
)
ruckusCtrlClientStatsTxRetryBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientStatsTxRetryBytes.setStatus("current")
_RuckusCtrlClientStatsTxDropPkts_Type = Counter64
_RuckusCtrlClientStatsTxDropPkts_Object = MibTableColumn
ruckusCtrlClientStatsTxDropPkts = _RuckusCtrlClientStatsTxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 8, 1, 63),
    _RuckusCtrlClientStatsTxDropPkts_Type()
)
ruckusCtrlClientStatsTxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlClientStatsTxDropPkts.setStatus("current")
_RuckusCTRLWiredClientTable_Object = MibTable
ruckusCTRLWiredClientTable = _RuckusCTRLWiredClientTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15)
)
if mibBuilder.loadTexts:
    ruckusCTRLWiredClientTable.setStatus("current")
_RuckusCTRLWiredClientEntry_Object = MibTableRow
ruckusCTRLWiredClientEntry = _RuckusCTRLWiredClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1)
)
ruckusCTRLWiredClientEntry.setIndexNames(
    (0, "RUCKUS-CTRL-MIB", "ruckusCtrlWiredClientApMac"),
)
if mibBuilder.loadTexts:
    ruckusCTRLWiredClientEntry.setStatus("current")
_RuckusCtrlWiredClientMac_Type = MacAddress
_RuckusCtrlWiredClientMac_Object = MibTableColumn
ruckusCtrlWiredClientMac = _RuckusCtrlWiredClientMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 1),
    _RuckusCtrlWiredClientMac_Type()
)
ruckusCtrlWiredClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientMac.setStatus("current")
_RuckusCtrlWiredClientUserName_Type = DisplayString
_RuckusCtrlWiredClientUserName_Object = MibTableColumn
ruckusCtrlWiredClientUserName = _RuckusCtrlWiredClientUserName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 3),
    _RuckusCtrlWiredClientUserName_Type()
)
ruckusCtrlWiredClientUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientUserName.setStatus("current")
_RuckusCtrlWiredClientLanPort_Type = Integer32
_RuckusCtrlWiredClientLanPort_Object = MibTableColumn
ruckusCtrlWiredClientLanPort = _RuckusCtrlWiredClientLanPort_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 4),
    _RuckusCtrlWiredClientLanPort_Type()
)
ruckusCtrlWiredClientLanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientLanPort.setStatus("current")
_RuckusCtrlWiredClientVlanId_Type = Integer32
_RuckusCtrlWiredClientVlanId_Object = MibTableColumn
ruckusCtrlWiredClientVlanId = _RuckusCtrlWiredClientVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 5),
    _RuckusCtrlWiredClientVlanId_Type()
)
ruckusCtrlWiredClientVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientVlanId.setStatus("current")
_RuckusCtrlWiredClientIp_Type = IpAddress
_RuckusCtrlWiredClientIp_Object = MibTableColumn
ruckusCtrlWiredClientIp = _RuckusCtrlWiredClientIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 6),
    _RuckusCtrlWiredClientIp_Type()
)
ruckusCtrlWiredClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientIp.setStatus("current")
_RuckusCtrlWiredClientIpv6_Type = Ipv6Address
_RuckusCtrlWiredClientIpv6_Object = MibTableColumn
ruckusCtrlWiredClientIpv6 = _RuckusCtrlWiredClientIpv6_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 7),
    _RuckusCtrlWiredClientIpv6_Type()
)
ruckusCtrlWiredClientIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientIpv6.setStatus("current")
_RuckusCtrlWiredClientApMac_Type = MacAddress
_RuckusCtrlWiredClientApMac_Object = MibTableColumn
ruckusCtrlWiredClientApMac = _RuckusCtrlWiredClientApMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 8),
    _RuckusCtrlWiredClientApMac_Type()
)
ruckusCtrlWiredClientApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientApMac.setStatus("current")
_RuckusCtrlWiredClientAuthStatus_Type = RuckusAuthStatusType
_RuckusCtrlWiredClientAuthStatus_Object = MibTableColumn
ruckusCtrlWiredClientAuthStatus = _RuckusCtrlWiredClientAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 10),
    _RuckusCtrlWiredClientAuthStatus_Type()
)
ruckusCtrlWiredClientAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientAuthStatus.setStatus("current")
_RuckusCtrlWiredClientRxFrames_Type = Counter64
_RuckusCtrlWiredClientRxFrames_Object = MibTableColumn
ruckusCtrlWiredClientRxFrames = _RuckusCtrlWiredClientRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 15),
    _RuckusCtrlWiredClientRxFrames_Type()
)
ruckusCtrlWiredClientRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientRxFrames.setStatus("current")
_RuckusCtrlWiredClientTxFrames_Type = Counter64
_RuckusCtrlWiredClientTxFrames_Object = MibTableColumn
ruckusCtrlWiredClientTxFrames = _RuckusCtrlWiredClientTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 16),
    _RuckusCtrlWiredClientTxFrames_Type()
)
ruckusCtrlWiredClientTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientTxFrames.setStatus("current")
_RuckusCtrlWiredClientRxBytes_Type = Counter64
_RuckusCtrlWiredClientRxBytes_Object = MibTableColumn
ruckusCtrlWiredClientRxBytes = _RuckusCtrlWiredClientRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 17),
    _RuckusCtrlWiredClientRxBytes_Type()
)
ruckusCtrlWiredClientRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientRxBytes.setStatus("current")
_RuckusCtrlWiredClientTxBytes_Type = Counter64
_RuckusCtrlWiredClientTxBytes_Object = MibTableColumn
ruckusCtrlWiredClientTxBytes = _RuckusCtrlWiredClientTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 18),
    _RuckusCtrlWiredClientTxBytes_Type()
)
ruckusCtrlWiredClientTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientTxBytes.setStatus("current")
_RuckusCtrlWiredClientRxUcastPkts_Type = Counter64
_RuckusCtrlWiredClientRxUcastPkts_Object = MibTableColumn
ruckusCtrlWiredClientRxUcastPkts = _RuckusCtrlWiredClientRxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 23),
    _RuckusCtrlWiredClientRxUcastPkts_Type()
)
ruckusCtrlWiredClientRxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientRxUcastPkts.setStatus("current")
_RuckusCtrlWiredClientTxUcastPkts_Type = Counter64
_RuckusCtrlWiredClientTxUcastPkts_Object = MibTableColumn
ruckusCtrlWiredClientTxUcastPkts = _RuckusCtrlWiredClientTxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 24),
    _RuckusCtrlWiredClientTxUcastPkts_Type()
)
ruckusCtrlWiredClientTxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientTxUcastPkts.setStatus("current")
_RuckusCtrlWiredClientRxMcastPkts_Type = Counter64
_RuckusCtrlWiredClientRxMcastPkts_Object = MibTableColumn
ruckusCtrlWiredClientRxMcastPkts = _RuckusCtrlWiredClientRxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 25),
    _RuckusCtrlWiredClientRxMcastPkts_Type()
)
ruckusCtrlWiredClientRxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientRxMcastPkts.setStatus("current")
_RuckusCtrlWiredClientTxMcastPkts_Type = Counter64
_RuckusCtrlWiredClientTxMcastPkts_Object = MibTableColumn
ruckusCtrlWiredClientTxMcastPkts = _RuckusCtrlWiredClientTxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 26),
    _RuckusCtrlWiredClientTxMcastPkts_Type()
)
ruckusCtrlWiredClientTxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientTxMcastPkts.setStatus("current")
_RuckusCtrlWiredClientRxMcastLegacyPkts_Type = Counter64
_RuckusCtrlWiredClientRxMcastLegacyPkts_Object = MibTableColumn
ruckusCtrlWiredClientRxMcastLegacyPkts = _RuckusCtrlWiredClientRxMcastLegacyPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 27),
    _RuckusCtrlWiredClientRxMcastLegacyPkts_Type()
)
ruckusCtrlWiredClientRxMcastLegacyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientRxMcastLegacyPkts.setStatus("current")
_RuckusCtrlWiredClientRxBcastPkts_Type = Counter64
_RuckusCtrlWiredClientRxBcastPkts_Object = MibTableColumn
ruckusCtrlWiredClientRxBcastPkts = _RuckusCtrlWiredClientRxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 28),
    _RuckusCtrlWiredClientRxBcastPkts_Type()
)
ruckusCtrlWiredClientRxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientRxBcastPkts.setStatus("current")
_RuckusCtrlWiredClientTxBcastPkts_Type = Counter64
_RuckusCtrlWiredClientTxBcastPkts_Object = MibTableColumn
ruckusCtrlWiredClientTxBcastPkts = _RuckusCtrlWiredClientTxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 29),
    _RuckusCtrlWiredClientTxBcastPkts_Type()
)
ruckusCtrlWiredClientTxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientTxBcastPkts.setStatus("current")
_RuckusCtrlWiredClientRxDroppedPkts_Type = Counter64
_RuckusCtrlWiredClientRxDroppedPkts_Object = MibTableColumn
ruckusCtrlWiredClientRxDroppedPkts = _RuckusCtrlWiredClientRxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 34),
    _RuckusCtrlWiredClientRxDroppedPkts_Type()
)
ruckusCtrlWiredClientRxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientRxDroppedPkts.setStatus("current")
_RuckusCtrlWiredClientTxDroppedPkts_Type = Counter64
_RuckusCtrlWiredClientTxDroppedPkts_Object = MibTableColumn
ruckusCtrlWiredClientTxDroppedPkts = _RuckusCtrlWiredClientTxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 35),
    _RuckusCtrlWiredClientTxDroppedPkts_Type()
)
ruckusCtrlWiredClientTxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientTxDroppedPkts.setStatus("current")
_RuckusCtrlWiredClientRxEapolPkts_Type = Counter64
_RuckusCtrlWiredClientRxEapolPkts_Object = MibTableColumn
ruckusCtrlWiredClientRxEapolPkts = _RuckusCtrlWiredClientRxEapolPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 36),
    _RuckusCtrlWiredClientRxEapolPkts_Type()
)
ruckusCtrlWiredClientRxEapolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientRxEapolPkts.setStatus("current")
_RuckusCtrlWiredClientTxEapolPkts_Type = Counter64
_RuckusCtrlWiredClientTxEapolPkts_Object = MibTableColumn
ruckusCtrlWiredClientTxEapolPkts = _RuckusCtrlWiredClientTxEapolPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 1, 2, 15, 1, 37),
    _RuckusCtrlWiredClientTxEapolPkts_Type()
)
ruckusCtrlWiredClientTxEapolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCtrlWiredClientTxEapolPkts.setStatus("current")
_RuckusCTRLSystemObjects_ObjectIdentity = ObjectIdentity
ruckusCTRLSystemObjects = _RuckusCTRLSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 3)
)
_RuckusCTRLSysCommands_ObjectIdentity = ObjectIdentity
ruckusCTRLSysCommands = _RuckusCTRLSysCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 3, 1)
)
_RuckusCTRLSysCmdReboot_Type = RuckusRebootStatusType
_RuckusCTRLSysCmdReboot_Object = MibScalar
ruckusCTRLSysCmdReboot = _RuckusCTRLSysCmdReboot_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1, 1, 3, 1, 1),
    _RuckusCTRLSysCmdReboot_Type()
)
ruckusCTRLSysCmdReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusCTRLSysCmdReboot.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-CTRL-MIB",
    **{"RuckusEthPortStatusType": RuckusEthPortStatusType,
       "RuckusAPStatusType": RuckusAPStatusType,
       "RuckusRebootStatusType": RuckusRebootStatusType,
       "RuckusSystemClusterHAState": RuckusSystemClusterHAState,
       "RuckusSystemClusterHARole": RuckusSystemClusterHARole,
       "ruckusCTRLWLANMIB": ruckusCTRLWLANMIB,
       "ruckusCTRLWLANObjects": ruckusCTRLWLANObjects,
       "ruckusCTRLInfo": ruckusCTRLInfo,
       "ruckusCTRLSystemNodeTable": ruckusCTRLSystemNodeTable,
       "ruckusCTRLSystemNodeEntry": ruckusCTRLSystemNodeEntry,
       "ruckusCtrlSystemNodeSerialNumber": ruckusCtrlSystemNodeSerialNumber,
       "ruckusCtrlSystemNodeName": ruckusCtrlSystemNodeName,
       "ruckusCtrlSystemNodeModel": ruckusCtrlSystemNodeModel,
       "ruckusCtrlSystemNodeVersion": ruckusCtrlSystemNodeVersion,
       "ruckusCtrlSystemNodeNumApLicense": ruckusCtrlSystemNodeNumApLicense,
       "ruckusCtrlSystemNodeMgmtIp": ruckusCtrlSystemNodeMgmtIp,
       "ruckusCtrlSystemNodeMgmtIpv6": ruckusCtrlSystemNodeMgmtIpv6,
       "ruckusCtrlSystemNodeMgmtMac": ruckusCtrlSystemNodeMgmtMac,
       "ruckusCtrlSystemNodeUptime": ruckusCtrlSystemNodeUptime,
       "ruckusCtrlSystemNodeStatus": ruckusCtrlSystemNodeStatus,
       "ruckusCtrlSystemClusterStatus": ruckusCtrlSystemClusterStatus,
       "ruckusCtrlSystemNodeNumApConnected": ruckusCtrlSystemNodeNumApConnected,
       "ruckusCtrlSystemNodeClusterHAState": ruckusCtrlSystemNodeClusterHAState,
       "ruckusCtrlSystemNodeClusterHARoles": ruckusCtrlSystemNodeClusterHARoles,
       "ruckusCTRLDomainTable": ruckusCTRLDomainTable,
       "ruckusCTRLDomainEntry": ruckusCTRLDomainEntry,
       "ruckusCtrlDomainId": ruckusCtrlDomainId,
       "ruckusCtrlDomainName": ruckusCtrlDomainName,
       "ruckusCtrlDomainParentDomainId": ruckusCtrlDomainParentDomainId,
       "ruckusCtrlDomainNumSubdomains": ruckusCtrlDomainNumSubdomains,
       "ruckusCtrlDomainNumZones": ruckusCtrlDomainNumZones,
       "ruckusCtrlDomainNumApConnected": ruckusCtrlDomainNumApConnected,
       "ruckusCtrlDomainNumApDisconnected": ruckusCtrlDomainNumApDisconnected,
       "ruckusCTRLZoneTable": ruckusCTRLZoneTable,
       "ruckusCTRLZoneEntry": ruckusCTRLZoneEntry,
       "ruckusCtrlZoneDomainId": ruckusCtrlZoneDomainId,
       "ruckusCtrlZoneId": ruckusCtrlZoneId,
       "ruckusCtrlZoneName": ruckusCtrlZoneName,
       "ruckusCtrlZoneCountryCode": ruckusCtrlZoneCountryCode,
       "ruckusCtrlZoneNumApConnected": ruckusCtrlZoneNumApConnected,
       "ruckusCtrlZoneNumApDisconnected": ruckusCtrlZoneNumApDisconnected,
       "ruckusCTRLApGroupTable": ruckusCTRLApGroupTable,
       "ruckusCTRLApGroupEntry": ruckusCTRLApGroupEntry,
       "ruckusCtrlApGroupZoneId": ruckusCtrlApGroupZoneId,
       "ruckusCtrlApGroupId": ruckusCtrlApGroupId,
       "ruckusCtrlApGroupName": ruckusCtrlApGroupName,
       "ruckusCtrlApGroupNumApConnected": ruckusCtrlApGroupNumApConnected,
       "ruckusCtrlApGroupNumApDisconnected": ruckusCtrlApGroupNumApDisconnected,
       "ruckusCTRLSummaryApTable": ruckusCTRLSummaryApTable,
       "ruckusCTRLSummaryApEntry": ruckusCTRLSummaryApEntry,
       "ruckusCtrlSummaryApIndexType": ruckusCtrlSummaryApIndexType,
       "ruckusCtrlSummaryApIndexUUID": ruckusCtrlSummaryApIndexUUID,
       "ruckusCtrlSummaryApDomainId": ruckusCtrlSummaryApDomainId,
       "ruckusCtrlSummaryApZoneId": ruckusCtrlSummaryApZoneId,
       "ruckusCtrlSummaryApApGroupId": ruckusCtrlSummaryApApGroupId,
       "ruckusCtrlSummaryApMac": ruckusCtrlSummaryApMac,
       "ruckusCtrlSummaryApDomainName": ruckusCtrlSummaryApDomainName,
       "ruckusCtrlSummaryApZoneName": ruckusCtrlSummaryApZoneName,
       "ruckusCtrlSummaryApName": ruckusCtrlSummaryApName,
       "ruckusCtrlSummaryApLocation": ruckusCtrlSummaryApLocation,
       "ruckusCTRLApClientTable": ruckusCTRLApClientTable,
       "ruckusCTRLApClientEntry": ruckusCTRLApClientEntry,
       "ruckusCtrlApClientApMac": ruckusCtrlApClientApMac,
       "ruckusCtrlApClientMac": ruckusCtrlApClientMac,
       "ruckusCTRLApWiredClientTable": ruckusCTRLApWiredClientTable,
       "ruckusCTRLApWiredClientEntry": ruckusCTRLApWiredClientEntry,
       "ruckusCtrlApWiredClientApMac": ruckusCtrlApWiredClientApMac,
       "ruckusCtrlApWiredClientMac": ruckusCtrlApWiredClientMac,
       "ruckusCTRLWLANInfo": ruckusCTRLWLANInfo,
       "ruckusCTRLApTable": ruckusCTRLApTable,
       "ruckusCTRLApEntry": ruckusCTRLApEntry,
       "ruckusCtrlApMac": ruckusCtrlApMac,
       "ruckusCtrlApDomainId": ruckusCtrlApDomainId,
       "ruckusCtrlApDomainName": ruckusCtrlApDomainName,
       "ruckusCtrlApZoneId": ruckusCtrlApZoneId,
       "ruckusCtrlApZoneName": ruckusCtrlApZoneName,
       "ruckusCtrlApApGroupId": ruckusCtrlApApGroupId,
       "ruckusCtrlApApGroupName": ruckusCtrlApApGroupName,
       "ruckusCtrlApIp": ruckusCtrlApIp,
       "ruckusCtrlApIpv6": ruckusCtrlApIpv6,
       "ruckusCtrlApNetmask": ruckusCtrlApNetmask,
       "ruckusCtrlApGateway": ruckusCtrlApGateway,
       "ruckusCtrlApIpDnsSvr1": ruckusCtrlApIpDnsSvr1,
       "ruckusCtrlApIpDnsSvr2": ruckusCtrlApIpDnsSvr2,
       "ruckusCtrlApIpv6DnsSvr1": ruckusCtrlApIpv6DnsSvr1,
       "ruckusCtrlApIpv6DnsSvr2": ruckusCtrlApIpv6DnsSvr2,
       "ruckusCtrlApName": ruckusCtrlApName,
       "ruckusCtrlApDescription": ruckusCtrlApDescription,
       "ruckusCtrlApStatus": ruckusCtrlApStatus,
       "ruckusCtrlApModel": ruckusCtrlApModel,
       "ruckusCtrlApSerialNumber": ruckusCtrlApSerialNumber,
       "ruckusCtrlApSwVersion": ruckusCtrlApSwVersion,
       "ruckusCtrlApLocation": ruckusCtrlApLocation,
       "ruckusCtrlApGpsInfo": ruckusCtrlApGpsInfo,
       "ruckusCtrlApTemperature": ruckusCtrlApTemperature,
       "ruckusCtrlApUptime": ruckusCtrlApUptime,
       "ruckusCtrlApLastConfSyncTime": ruckusCtrlApLastConfSyncTime,
       "ruckusCtrlApCpuUtilization": ruckusCtrlApCpuUtilization,
       "ruckusCtrlApTotalMemory": ruckusCtrlApTotalMemory,
       "ruckusCtrlApFreeMemory": ruckusCtrlApFreeMemory,
       "ruckusCtrlApFreeStorage": ruckusCtrlApFreeStorage,
       "ruckusCtrlApEtherPortStatus": ruckusCtrlApEtherPortStatus,
       "ruckusCtrlApCableModemMac": ruckusCtrlApCableModemMac,
       "ruckusCtrlApCableModemSerialNumber": ruckusCtrlApCableModemSerialNumber,
       "ruckusCtrlApNumRadios": ruckusCtrlApNumRadios,
       "ruckusCtrlApNumWlans": ruckusCtrlApNumWlans,
       "ruckusCtrlApNumAssocClients": ruckusCtrlApNumAssocClients,
       "ruckusCtrlApStatsRxBytes": ruckusCtrlApStatsRxBytes,
       "ruckusCtrlApStatsTxBytes": ruckusCtrlApStatsTxBytes,
       "ruckusCtrlApStatsRxDataBytes": ruckusCtrlApStatsRxDataBytes,
       "ruckusCtrlApStatsTxDataBytes": ruckusCtrlApStatsTxDataBytes,
       "ruckusCtrlApStatsRxPkts": ruckusCtrlApStatsRxPkts,
       "ruckusCtrlApStatsTxPkts": ruckusCtrlApStatsTxPkts,
       "ruckusCtrlApStatsRxDataPkts": ruckusCtrlApStatsRxDataPkts,
       "ruckusCtrlApStatsTxDataPkts": ruckusCtrlApStatsTxDataPkts,
       "ruckusCtrlApStatsRxErrorPkts": ruckusCtrlApStatsRxErrorPkts,
       "ruckusCtrlApStatsTxErrorPkts": ruckusCtrlApStatsTxErrorPkts,
       "ruckusCtrlApStatsRxDropPkts": ruckusCtrlApStatsRxDropPkts,
       "ruckusCtrlApStatsTxDropPkts": ruckusCtrlApStatsTxDropPkts,
       "ruckusCtrlApMeshRole": ruckusCtrlApMeshRole,
       "ruckusCtrlApNumMeshHops": ruckusCtrlApNumMeshHops,
       "ruckusCtrlApConnectScgCpIp": ruckusCtrlApConnectScgCpIp,
       "ruckusCtrlApConnectScgCpIpv6": ruckusCtrlApConnectScgCpIpv6,
       "ruckusCtrlApConnectScgDpIp": ruckusCtrlApConnectScgDpIp,
       "ruckusCtrlApConnectScgDpIpv6": ruckusCtrlApConnectScgDpIpv6,
       "ruckusCtrlApLanStatsRxBytes": ruckusCtrlApLanStatsRxBytes,
       "ruckusCtrlApLanStatsTxBytes": ruckusCtrlApLanStatsTxBytes,
       "ruckusCtrlApLanStatsRxPkts": ruckusCtrlApLanStatsRxPkts,
       "ruckusCtrlApLanStatsTxPkts": ruckusCtrlApLanStatsTxPkts,
       "ruckusCtrlApLanStatsRxErrorPkts": ruckusCtrlApLanStatsRxErrorPkts,
       "ruckusCtrlApLanStatsTxErrorPkts": ruckusCtrlApLanStatsTxErrorPkts,
       "ruckusCtrlApLanStatsRxDroppedPkts": ruckusCtrlApLanStatsRxDroppedPkts,
       "ruckusCtrlApLanStatsTxDroppedPkts": ruckusCtrlApLanStatsTxDroppedPkts,
       "ruckusCtrlAPIpsecRxBytes": ruckusCtrlAPIpsecRxBytes,
       "ruckusCtrlAPIpsecTxBytes": ruckusCtrlAPIpsecTxBytes,
       "ruckusCtrlAPIpsecRxPkts": ruckusCtrlAPIpsecRxPkts,
       "ruckusCtrlAPIpsecTxPkts": ruckusCtrlAPIpsecTxPkts,
       "ruckusCtrlAPIpsecRxDropPkts": ruckusCtrlAPIpsecRxDropPkts,
       "ruckusCtrlAPIpsecTxDropPkts": ruckusCtrlAPIpsecTxDropPkts,
       "ruckusCtrlAPIpsecSessionTime": ruckusCtrlAPIpsecSessionTime,
       "ruckusCtrlAPIpsecRxIdleTime": ruckusCtrlAPIpsecRxIdleTime,
       "ruckusCtrlAPIpsecTxIdleTime": ruckusCtrlAPIpsecTxIdleTime,
       "ruckusCTRLApRadioTable": ruckusCTRLApRadioTable,
       "ruckusCTRLApRadioEntry": ruckusCTRLApRadioEntry,
       "ruckusCtrlApRadioApMac": ruckusCtrlApRadioApMac,
       "ruckusCtrlApRadioIndex": ruckusCtrlApRadioIndex,
       "ruckusCtrlApRadioNumWlans": ruckusCtrlApRadioNumWlans,
       "ruckusCtrlApRadioType": ruckusCtrlApRadioType,
       "ruckusCtrlApRadioChannelWidth": ruckusCtrlApRadioChannelWidth,
       "ruckusCtrlApRadioChannel": ruckusCtrlApRadioChannel,
       "ruckusCtrlApRadioTxPower": ruckusCtrlApRadioTxPower,
       "ruckusCtrlApRadioBeaconPeriod": ruckusCtrlApRadioBeaconPeriod,
       "ruckusCtrlApRadioPowerMgmtEnable": ruckusCtrlApRadioPowerMgmtEnable,
       "ruckusCtrlApRadioMeshEnable": ruckusCtrlApRadioMeshEnable,
       "ruckusCtrlApRadioStatsRxAirtime": ruckusCtrlApRadioStatsRxAirtime,
       "ruckusCtrlApRadioStatsTxAirtime": ruckusCtrlApRadioStatsTxAirtime,
       "ruckusCtrlApRadioStatsBusyAirtime": ruckusCtrlApRadioStatsBusyAirtime,
       "ruckusCtrlApRadioStatsTotalAirtime": ruckusCtrlApRadioStatsTotalAirtime,
       "ruckusCtrlApRadioAntennaGain": ruckusCtrlApRadioAntennaGain,
       "ruckusCtrlApRadioStatsSnr": ruckusCtrlApRadioStatsSnr,
       "ruckusCtrlApRadioStatsNoiseFloor": ruckusCtrlApRadioStatsNoiseFloor,
       "ruckusCtrlApRadioStatsNumAssocClients": ruckusCtrlApRadioStatsNumAssocClients,
       "ruckusCtrlApRadioStatsNumAuthClients": ruckusCtrlApRadioStatsNumAuthClients,
       "ruckusCtrlApRadioStatsNumMaxClients": ruckusCtrlApRadioStatsNumMaxClients,
       "ruckusCtrlApRadioStatsPhyError": ruckusCtrlApRadioStatsPhyError,
       "ruckusCtrlApRadioStatsRxWepFail": ruckusCtrlApRadioStatsRxWepFail,
       "ruckusCtrlApRadioStatsRxDecryptCrcError": ruckusCtrlApRadioStatsRxDecryptCrcError,
       "ruckusCtrlApRadioStatsRxMicError": ruckusCtrlApRadioStatsRxMicError,
       "ruckusCtrlApRadioStatsRxBytes": ruckusCtrlApRadioStatsRxBytes,
       "ruckusCtrlApRadioStatsTxBytes": ruckusCtrlApRadioStatsTxBytes,
       "ruckusCtrlApRadioStatsRxPkts": ruckusCtrlApRadioStatsRxPkts,
       "ruckusCtrlApRadioStatsTxPkts": ruckusCtrlApRadioStatsTxPkts,
       "ruckusCtrlApRadioStatsRxMcastPkts": ruckusCtrlApRadioStatsRxMcastPkts,
       "ruckusCtrlApRadioStatsTxMcastPkts": ruckusCtrlApRadioStatsTxMcastPkts,
       "ruckusCtrlApRadioStatsRxErrorPkts": ruckusCtrlApRadioStatsRxErrorPkts,
       "ruckusCtrlApRadioStatsTxErrorPkts": ruckusCtrlApRadioStatsTxErrorPkts,
       "ruckusCtrlApRadioStatsRxPktErrorRate": ruckusCtrlApRadioStatsRxPktErrorRate,
       "ruckusCtrlApRadioStatsTxPktErrorRate": ruckusCtrlApRadioStatsTxPktErrorRate,
       "ruckusCtrlApRadioStatsTxPktRetryRate": ruckusCtrlApRadioStatsTxPktRetryRate,
       "ruckusCtrlApRadioStatsTxRetryPkts": ruckusCtrlApRadioStatsTxRetryPkts,
       "ruckusCtrlApRadioStatsRxDropPkts": ruckusCtrlApRadioStatsRxDropPkts,
       "ruckusCtrlApRadioStatsTxDropPkts": ruckusCtrlApRadioStatsTxDropPkts,
       "ruckusCtrlApRadioStatsNumAuthReqs": ruckusCtrlApRadioStatsNumAuthReqs,
       "ruckusCtrlApRadioStatsNumAuthResps": ruckusCtrlApRadioStatsNumAuthResps,
       "ruckusCtrlApRadioStatsNumAuthSuccess": ruckusCtrlApRadioStatsNumAuthSuccess,
       "ruckusCtrlApRadioStatsNumAuthFail": ruckusCtrlApRadioStatsNumAuthFail,
       "ruckusCtrlApRadioStatsAuthFailRate": ruckusCtrlApRadioStatsAuthFailRate,
       "ruckusCtrlApRadioStatsNumAssocReq": ruckusCtrlApRadioStatsNumAssocReq,
       "ruckusCtrlApRadioStatsNumAssocResp": ruckusCtrlApRadioStatsNumAssocResp,
       "ruckusCtrlApRadioStatsNumReassocReq": ruckusCtrlApRadioStatsNumReassocReq,
       "ruckusCtrlApRadioStatsNumReassocResp": ruckusCtrlApRadioStatsNumReassocResp,
       "ruckusCtrlApRadioStatsNumAssocSuccess": ruckusCtrlApRadioStatsNumAssocSuccess,
       "ruckusCtrlApRadioStatsNumAssocFail": ruckusCtrlApRadioStatsNumAssocFail,
       "ruckusCtrlApRadioStatsAssocSuccessRate": ruckusCtrlApRadioStatsAssocSuccessRate,
       "ruckusCtrlApRadioStatsAssocFailRate": ruckusCtrlApRadioStatsAssocFailRate,
       "ruckusCTRLApWlanTable": ruckusCTRLApWlanTable,
       "ruckusCTRLApWlanEntry": ruckusCTRLApWlanEntry,
       "ruckusCtrlApWlanApMac": ruckusCtrlApWlanApMac,
       "ruckusCtrlApWlanRadioIndex": ruckusCtrlApWlanRadioIndex,
       "ruckusCtrlApWlanBssid": ruckusCtrlApWlanBssid,
       "ruckusCtrlApWlanAuthMethod": ruckusCtrlApWlanAuthMethod,
       "ruckusCtrlApWlanEncryptMethod": ruckusCtrlApWlanEncryptMethod,
       "ruckusCtrlApWlanId": ruckusCtrlApWlanId,
       "ruckusCtrlApWlanName": ruckusCtrlApWlanName,
       "ruckusCtrlApWlanRadioChannel": ruckusCtrlApWlanRadioChannel,
       "ruckusCtrlApWlanSsid": ruckusCtrlApWlanSsid,
       "ruckusCtrlApWlanVlanId": ruckusCtrlApWlanVlanId,
       "ruckusCtrlApWlanRtsThreshold": ruckusCtrlApWlanRtsThreshold,
       "ruckusCtrlApWlanDownRateLimit": ruckusCtrlApWlanDownRateLimit,
       "ruckusCtrlApWlanUpRateLimit": ruckusCtrlApWlanUpRateLimit,
       "ruckusCtrlApWlanIsBcastDisable": ruckusCtrlApWlanIsBcastDisable,
       "ruckusCtrlApWlanIsGuest": ruckusCtrlApWlanIsGuest,
       "ruckusCtrlApWlanIsTunnel": ruckusCtrlApWlanIsTunnel,
       "ruckusCtrlApWlanStatsNumAssocClients": ruckusCtrlApWlanStatsNumAssocClients,
       "ruckusCtrlApWlanStatsRxPkts": ruckusCtrlApWlanStatsRxPkts,
       "ruckusCtrlApWlanStatsTxPkts": ruckusCtrlApWlanStatsTxPkts,
       "ruckusCtrlApWlanStatsRxBytes": ruckusCtrlApWlanStatsRxBytes,
       "ruckusCtrlApWlanStatsTxBytes": ruckusCtrlApWlanStatsTxBytes,
       "ruckusCtrlApWlanStatsRxDataBytes": ruckusCtrlApWlanStatsRxDataBytes,
       "ruckusCtrlApWlanStatsTxDataBytes": ruckusCtrlApWlanStatsTxDataBytes,
       "ruckusCtrlApWlanStatsRxDataPkts": ruckusCtrlApWlanStatsRxDataPkts,
       "ruckusCtrlApWlanStatsTxDataPkts": ruckusCtrlApWlanStatsTxDataPkts,
       "ruckusCtrlApWlanStatsRxBcastDataPkts": ruckusCtrlApWlanStatsRxBcastDataPkts,
       "ruckusCtrlApWlanStatsTxBcastDataPkts": ruckusCtrlApWlanStatsTxBcastDataPkts,
       "ruckusCtrlApWlanStatsRxMcastDataPkts": ruckusCtrlApWlanStatsRxMcastDataPkts,
       "ruckusCtrlApWlanStatsTxMcastDataPkts": ruckusCtrlApWlanStatsTxMcastDataPkts,
       "ruckusCtrlApWlanStatsNumAssocReq": ruckusCtrlApWlanStatsNumAssocReq,
       "ruckusCtrlApWlanStatsNumAssocResp": ruckusCtrlApWlanStatsNumAssocResp,
       "ruckusCtrlApWlanStatsNumReassocReq": ruckusCtrlApWlanStatsNumReassocReq,
       "ruckusCtrlApWlanStatsNumReassocResp": ruckusCtrlApWlanStatsNumReassocResp,
       "ruckusCtrlApWlanStatsNumAuthReq": ruckusCtrlApWlanStatsNumAuthReq,
       "ruckusCtrlApWlanStatsNumAuthResp": ruckusCtrlApWlanStatsNumAuthResp,
       "ruckusCtrlApWlanStatsNumAuthSuccess": ruckusCtrlApWlanStatsNumAuthSuccess,
       "ruckusCtrlApWlanStatsNumAuthFail": ruckusCtrlApWlanStatsNumAuthFail,
       "ruckusCtrlApWlanStatsAuthFailRate": ruckusCtrlApWlanStatsAuthFailRate,
       "ruckusCtrlApWlanStatsNumAssocFail": ruckusCtrlApWlanStatsNumAssocFail,
       "ruckusCTRLClientTable": ruckusCTRLClientTable,
       "ruckusCTRLClientEntry": ruckusCTRLClientEntry,
       "ruckusCtrlClientMac": ruckusCtrlClientMac,
       "ruckusCtrlClientIp": ruckusCtrlClientIp,
       "ruckusCtrlClientIpv6": ruckusCtrlClientIpv6,
       "ruckusCtrlClientApMac": ruckusCtrlClientApMac,
       "ruckusCtrlClientWlanBssid": ruckusCtrlClientWlanBssid,
       "ruckusCtrlClientSsid": ruckusCtrlClientSsid,
       "ruckusCtrlClientRadioIndex": ruckusCtrlClientRadioIndex,
       "ruckusCtrlClientRadioType": ruckusCtrlClientRadioType,
       "ruckusCtrlClientRadioChannel": ruckusCtrlClientRadioChannel,
       "ruckusCtrlClientUsername": ruckusCtrlClientUsername,
       "ruckusCtrlClientVlanId": ruckusCtrlClientVlanId,
       "ruckusCtrlClientOsType": ruckusCtrlClientOsType,
       "ruckusCtrlClientStatus": ruckusCtrlClientStatus,
       "ruckusCtrlClientAuthMode": ruckusCtrlClientAuthMode,
       "ruckusCtrlClientStatsRssi": ruckusCtrlClientStatsRssi,
       "ruckusCtrlClientStatsSnr": ruckusCtrlClientStatsSnr,
       "ruckusCtrlClientStatsNoiseFloor": ruckusCtrlClientStatsNoiseFloor,
       "ruckusCtrlClientStatsThroughput": ruckusCtrlClientStatsThroughput,
       "ruckusCtrlClientStatsRxDataBytes": ruckusCtrlClientStatsRxDataBytes,
       "ruckusCtrlClientStatsTxDataBytes": ruckusCtrlClientStatsTxDataBytes,
       "ruckusCtrlClientStatsRxDataPkts": ruckusCtrlClientStatsRxDataPkts,
       "ruckusCtrlClientStatsTxDataPkts": ruckusCtrlClientStatsTxDataPkts,
       "ruckusCtrlClientStatsTxAvgByteRate": ruckusCtrlClientStatsTxAvgByteRate,
       "ruckusCtrlClientStatsTxRetry": ruckusCtrlClientStatsTxRetry,
       "ruckusCtrlClientStatsRxError": ruckusCtrlClientStatsRxError,
       "ruckusCtrlClientStatsTxError": ruckusCtrlClientStatsTxError,
       "ruckusCtrlClientStatsTxRetryBytes": ruckusCtrlClientStatsTxRetryBytes,
       "ruckusCtrlClientStatsTxDropPkts": ruckusCtrlClientStatsTxDropPkts,
       "ruckusCTRLWiredClientTable": ruckusCTRLWiredClientTable,
       "ruckusCTRLWiredClientEntry": ruckusCTRLWiredClientEntry,
       "ruckusCtrlWiredClientMac": ruckusCtrlWiredClientMac,
       "ruckusCtrlWiredClientUserName": ruckusCtrlWiredClientUserName,
       "ruckusCtrlWiredClientLanPort": ruckusCtrlWiredClientLanPort,
       "ruckusCtrlWiredClientVlanId": ruckusCtrlWiredClientVlanId,
       "ruckusCtrlWiredClientIp": ruckusCtrlWiredClientIp,
       "ruckusCtrlWiredClientIpv6": ruckusCtrlWiredClientIpv6,
       "ruckusCtrlWiredClientApMac": ruckusCtrlWiredClientApMac,
       "ruckusCtrlWiredClientAuthStatus": ruckusCtrlWiredClientAuthStatus,
       "ruckusCtrlWiredClientRxFrames": ruckusCtrlWiredClientRxFrames,
       "ruckusCtrlWiredClientTxFrames": ruckusCtrlWiredClientTxFrames,
       "ruckusCtrlWiredClientRxBytes": ruckusCtrlWiredClientRxBytes,
       "ruckusCtrlWiredClientTxBytes": ruckusCtrlWiredClientTxBytes,
       "ruckusCtrlWiredClientRxUcastPkts": ruckusCtrlWiredClientRxUcastPkts,
       "ruckusCtrlWiredClientTxUcastPkts": ruckusCtrlWiredClientTxUcastPkts,
       "ruckusCtrlWiredClientRxMcastPkts": ruckusCtrlWiredClientRxMcastPkts,
       "ruckusCtrlWiredClientTxMcastPkts": ruckusCtrlWiredClientTxMcastPkts,
       "ruckusCtrlWiredClientRxMcastLegacyPkts": ruckusCtrlWiredClientRxMcastLegacyPkts,
       "ruckusCtrlWiredClientRxBcastPkts": ruckusCtrlWiredClientRxBcastPkts,
       "ruckusCtrlWiredClientTxBcastPkts": ruckusCtrlWiredClientTxBcastPkts,
       "ruckusCtrlWiredClientRxDroppedPkts": ruckusCtrlWiredClientRxDroppedPkts,
       "ruckusCtrlWiredClientTxDroppedPkts": ruckusCtrlWiredClientTxDroppedPkts,
       "ruckusCtrlWiredClientRxEapolPkts": ruckusCtrlWiredClientRxEapolPkts,
       "ruckusCtrlWiredClientTxEapolPkts": ruckusCtrlWiredClientTxEapolPkts,
       "ruckusCTRLSystemObjects": ruckusCTRLSystemObjects,
       "ruckusCTRLSysCommands": ruckusCTRLSysCommands,
       "ruckusCTRLSysCmdReboot": ruckusCTRLSysCmdReboot}
)
