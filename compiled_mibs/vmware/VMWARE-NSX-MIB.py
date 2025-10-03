# SNMP MIB module (VMWARE-NSX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vmware\VMWARE-NSX-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:24 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(vmwNSXsys,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwNSXsys")


# MODULE-IDENTITY

vmwNSXsysMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1)
)
if mibBuilder.loadTexts:
    vmwNSXsysMIB.setRevisions(
        ("2022-02-14 00:00",
         "2021-08-06 00:00",
         "2021-04-22 00:00",
         "2021-03-25 00:00",
         "2021-01-30 00:00",
         "2020-10-30 00:00",
         "2020-09-22 00:00",
         "2020-06-29 00:00",
         "2020-03-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VmwNsxTDataCenterFeatureIdType(TextualConvention, Integer32):
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
              9,
              10,
              11,
              12,
              13,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              24,
              28,
              30,
              31,
              32,
              33,
              35,
              36,
              38,
              39,
              40,
              41,
              42,
              43,
              45,
              46)
        )
    )
    namedValues = NamedValues(
        *(("managerHealth", 1),
          ("edgeHealth", 2),
          ("certificates", 3),
          ("passwordManagement", 4),
          ("licenses", 5),
          ("intelligenceHealth", 6),
          ("infrastructureCommunication", 7),
          ("intelligenceCommunication", 9),
          ("cniHealth", 10),
          ("ncpHealth", 11),
          ("nodeAgentsHealth", 12),
          ("endpointProtection", 13),
          ("vpn", 15),
          ("alarmManagement", 16),
          ("loadBalancer", 17),
          ("transportNodeHealth", 18),
          ("infrastructureService", 19),
          ("dhcp", 20),
          ("highAvailability", 21),
          ("capacity", 22),
          ("auditLogHealth", 24),
          ("routing", 28),
          ("dns", 30),
          ("distributedFirewall", 31),
          ("federation", 32),
          ("distributedIdsIps", 33),
          ("communication", 35),
          ("identityFirewall", 36),
          ("ipam", 38),
          ("gatewayFirewall", 39),
          ("clustering", 40),
          ("nsxApplicationPlatformCommunication", 41),
          ("mtuCheck", 42),
          ("nsxApplicationPlatformHealth", 43),
          ("edge", 45),
          ("nat", 46))
    )



class VmwNsxTDataCenterEventTypeType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterSeverityType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("informational", 6),
          ("debug", 7))
    )



class VmwNsxTDataCenterNodeIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterNodeTypeType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("manager", 0),
          ("edge", 1),
          ("esx", 2),
          ("kvm", 3),
          ("publiccloudgateway", 4),
          ("intelligence", 5),
          ("autonomousedge", 6),
          ("globalmanager", 7))
    )



class VmwNsxTDataCenterEntityIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterSystemResourceUsageType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterDiskPartitionNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterLicenseEditionTypeType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterApplianceAddressType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterCurrentGatewayStateType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterCurrentServiceStateType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterDatapathResourceUsageType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterDHCPPoolUsageType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterEdgeServiceNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterFailureReasonType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterPreviousGatewayStateType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterPreviousServiceStateType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterSystemUsageThresholdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterUsernameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterDHCPServerIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterServiceNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterIntelligenceNodeIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterHostnameOrIPAddressWithPortType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterEventIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterActiveGlobalManagerType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterActiveGlobalManagersType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterSessionDownReasonType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterManagerNodeNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterTransportNodeAddressType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterTransportNodeNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterCentralControlPlaneIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterTunnelDownReasonType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterHeapTypeType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterMempoolNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterPasswordExpirationDaysType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterBGPNeighborIPType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterLDAPServerType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterPeerAddressType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterMaxIDSEventsAllowedType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterStaticAddressType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterDuplicateIPAddressType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterCapacityDisplayNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterCapacityUsageCountType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterEdgeNICNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterRxRingBufferOverflowPercentageType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterTxRingBufferOverflowPercentageType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterSrIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterIDSEventsCountType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterRemoteSiteNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterBGPSourceIPType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterRemoteSiteIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterSiteIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterSiteNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterLrIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterRxMissesType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterRxProcessedType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterTxMissesType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterTxProcessedType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterLrportIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterServiceIPType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterRemoteManagerNodeIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterDirectoryDomainType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterTimeoutInMinutesType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterMaxCapacityThresholdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterMinCapacityThresholdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterMaxSupportedCapacityCountType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterLatencySourceType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterLatencyThresholdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterLatencyValueType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterApplianceFQDNType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterRemoteApplianceAddressType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterManagerNodeIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterDisplayedLicenseKeyType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterEdgeThreadNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterIntentPathType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterFirewallHalfopenFlowUsageType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterFirewallICMPFlowUsageType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterServiceDownReasonType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterFirewallUDPFlowUsageType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterFirewallIPFlowUsageType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterDNSIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterDNSUpstreamIPType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterCABundleAgeThresholdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterAPICollectionPathType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterEdgeNodeSettingMismatchReasonType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterEdgeVMvSphereSettingsMismatchReasonType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterFirewallSNATPortsUsageType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterEdgevSphereLocationMismatchReasonType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterEdgeNodeAndvSphereSettingsMismatchReasonType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterSNATIPAddressType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterNappClusterIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterNappMessagingLAGThresholdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterNappNodeIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterNappServiceNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterFlowIdentifierType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterSyncIssueReasonType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterQueueNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterQueueSizeType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterQueueSizeThresholdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterGroupTypeType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterManagerNodeIDSType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterServiceRouterIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterTransportNodeIdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterFromGMPathType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterToGMPathType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterNICThroughputType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterNICThroughputThresholdType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterEdgeCryptoDrvNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VmwNsxTDataCenterNappNodeNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_VmwNsxTDataCenterNotifications_ObjectIdentity = ObjectIdentity
vmwNsxTDataCenterNotifications = _VmwNsxTDataCenterNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotifications.setStatus("current")
_VmwNsxTManagerHealthFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTManagerHealthFeaturePrefix = _VmwNsxTManagerHealthFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1)
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthFeaturePrefix.setStatus("current")
_VmwNsxTManagerHealthFeature_ObjectIdentity = ObjectIdentity
vmwNsxTManagerHealthFeature = _VmwNsxTManagerHealthFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthFeature.setStatus("current")
_VmwNsxTEdgeHealthFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTEdgeHealthFeaturePrefix = _VmwNsxTEdgeHealthFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2)
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthFeaturePrefix.setStatus("current")
_VmwNsxTEdgeHealthFeature_ObjectIdentity = ObjectIdentity
vmwNsxTEdgeHealthFeature = _VmwNsxTEdgeHealthFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthFeature.setStatus("current")
_VmwNsxTCertificatesFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTCertificatesFeaturePrefix = _VmwNsxTCertificatesFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3)
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesFeaturePrefix.setStatus("current")
_VmwNsxTCertificatesFeature_ObjectIdentity = ObjectIdentity
vmwNsxTCertificatesFeature = _VmwNsxTCertificatesFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesFeature.setStatus("current")
_VmwNsxTPasswordManagementFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTPasswordManagementFeaturePrefix = _VmwNsxTPasswordManagementFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 4)
)
if mibBuilder.loadTexts:
    vmwNsxTPasswordManagementFeaturePrefix.setStatus("current")
_VmwNsxTPasswordManagementFeature_ObjectIdentity = ObjectIdentity
vmwNsxTPasswordManagementFeature = _VmwNsxTPasswordManagementFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 4, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTPasswordManagementFeature.setStatus("current")
_VmwNsxTLicensesFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTLicensesFeaturePrefix = _VmwNsxTLicensesFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 5)
)
if mibBuilder.loadTexts:
    vmwNsxTLicensesFeaturePrefix.setStatus("current")
_VmwNsxTLicensesFeature_ObjectIdentity = ObjectIdentity
vmwNsxTLicensesFeature = _VmwNsxTLicensesFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 5, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTLicensesFeature.setStatus("current")
_VmwNsxTIntelligenceHealthFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTIntelligenceHealthFeaturePrefix = _VmwNsxTIntelligenceHealthFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6)
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthFeaturePrefix.setStatus("current")
_VmwNsxTIntelligenceHealthFeature_ObjectIdentity = ObjectIdentity
vmwNsxTIntelligenceHealthFeature = _VmwNsxTIntelligenceHealthFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthFeature.setStatus("current")
_VmwNsxTInfrastructureCommunicationFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTInfrastructureCommunicationFeaturePrefix = _VmwNsxTInfrastructureCommunicationFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 7)
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureCommunicationFeaturePrefix.setStatus("current")
_VmwNsxTInfrastructureCommunicationFeature_ObjectIdentity = ObjectIdentity
vmwNsxTInfrastructureCommunicationFeature = _VmwNsxTInfrastructureCommunicationFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 7, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureCommunicationFeature.setStatus("current")
_VmwNsxTIntelligenceCommunicationFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTIntelligenceCommunicationFeaturePrefix = _VmwNsxTIntelligenceCommunicationFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 9)
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceCommunicationFeaturePrefix.setStatus("current")
_VmwNsxTIntelligenceCommunicationFeature_ObjectIdentity = ObjectIdentity
vmwNsxTIntelligenceCommunicationFeature = _VmwNsxTIntelligenceCommunicationFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 9, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceCommunicationFeature.setStatus("current")
_VmwNsxTCniHealthFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTCniHealthFeaturePrefix = _VmwNsxTCniHealthFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 10)
)
if mibBuilder.loadTexts:
    vmwNsxTCniHealthFeaturePrefix.setStatus("current")
_VmwNsxTCniHealthFeature_ObjectIdentity = ObjectIdentity
vmwNsxTCniHealthFeature = _VmwNsxTCniHealthFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 10, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTCniHealthFeature.setStatus("current")
_VmwNsxTNCPHealthFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTNCPHealthFeaturePrefix = _VmwNsxTNCPHealthFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 11)
)
if mibBuilder.loadTexts:
    vmwNsxTNCPHealthFeaturePrefix.setStatus("current")
_VmwNsxTNCPHealthFeature_ObjectIdentity = ObjectIdentity
vmwNsxTNCPHealthFeature = _VmwNsxTNCPHealthFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 11, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTNCPHealthFeature.setStatus("current")
_VmwNsxTNodeAgentsHealthFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTNodeAgentsHealthFeaturePrefix = _VmwNsxTNodeAgentsHealthFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 12)
)
if mibBuilder.loadTexts:
    vmwNsxTNodeAgentsHealthFeaturePrefix.setStatus("current")
_VmwNsxTNodeAgentsHealthFeature_ObjectIdentity = ObjectIdentity
vmwNsxTNodeAgentsHealthFeature = _VmwNsxTNodeAgentsHealthFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 12, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTNodeAgentsHealthFeature.setStatus("current")
_VmwNsxTEndpointProtectionFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTEndpointProtectionFeaturePrefix = _VmwNsxTEndpointProtectionFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 13)
)
if mibBuilder.loadTexts:
    vmwNsxTEndpointProtectionFeaturePrefix.setStatus("current")
_VmwNsxTEndpointProtectionFeature_ObjectIdentity = ObjectIdentity
vmwNsxTEndpointProtectionFeature = _VmwNsxTEndpointProtectionFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 13, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTEndpointProtectionFeature.setStatus("current")
_VmwNsxTVPNFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTVPNFeaturePrefix = _VmwNsxTVPNFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15)
)
if mibBuilder.loadTexts:
    vmwNsxTVPNFeaturePrefix.setStatus("current")
_VmwNsxTVPNFeature_ObjectIdentity = ObjectIdentity
vmwNsxTVPNFeature = _VmwNsxTVPNFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTVPNFeature.setStatus("current")
_VmwNsxTAlarmManagementFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTAlarmManagementFeaturePrefix = _VmwNsxTAlarmManagementFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 16)
)
if mibBuilder.loadTexts:
    vmwNsxTAlarmManagementFeaturePrefix.setStatus("current")
_VmwNsxTAlarmManagementFeature_ObjectIdentity = ObjectIdentity
vmwNsxTAlarmManagementFeature = _VmwNsxTAlarmManagementFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 16, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTAlarmManagementFeature.setStatus("current")
_VmwNsxTLoadBalancerFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTLoadBalancerFeaturePrefix = _VmwNsxTLoadBalancerFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17)
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerFeaturePrefix.setStatus("current")
_VmwNsxTLoadBalancerFeature_ObjectIdentity = ObjectIdentity
vmwNsxTLoadBalancerFeature = _VmwNsxTLoadBalancerFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerFeature.setStatus("current")
_VmwNsxTTransportNodeHealthFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTTransportNodeHealthFeaturePrefix = _VmwNsxTTransportNodeHealthFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 18)
)
if mibBuilder.loadTexts:
    vmwNsxTTransportNodeHealthFeaturePrefix.setStatus("current")
_VmwNsxTTransportNodeHealthFeature_ObjectIdentity = ObjectIdentity
vmwNsxTTransportNodeHealthFeature = _VmwNsxTTransportNodeHealthFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 18, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTTransportNodeHealthFeature.setStatus("current")
_VmwNsxTInfrastructureServiceFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTInfrastructureServiceFeaturePrefix = _VmwNsxTInfrastructureServiceFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 19)
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureServiceFeaturePrefix.setStatus("current")
_VmwNsxTInfrastructureServiceFeature_ObjectIdentity = ObjectIdentity
vmwNsxTInfrastructureServiceFeature = _VmwNsxTInfrastructureServiceFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 19, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureServiceFeature.setStatus("current")
_VmwNsxTDHCPFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTDHCPFeaturePrefix = _VmwNsxTDHCPFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 20)
)
if mibBuilder.loadTexts:
    vmwNsxTDHCPFeaturePrefix.setStatus("current")
_VmwNsxTDHCPFeature_ObjectIdentity = ObjectIdentity
vmwNsxTDHCPFeature = _VmwNsxTDHCPFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 20, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTDHCPFeature.setStatus("current")
_VmwNsxTHighAvailabilityFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTHighAvailabilityFeaturePrefix = _VmwNsxTHighAvailabilityFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 21)
)
if mibBuilder.loadTexts:
    vmwNsxTHighAvailabilityFeaturePrefix.setStatus("current")
_VmwNsxTHighAvailabilityFeature_ObjectIdentity = ObjectIdentity
vmwNsxTHighAvailabilityFeature = _VmwNsxTHighAvailabilityFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 21, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTHighAvailabilityFeature.setStatus("current")
_VmwNsxTCapacityFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTCapacityFeaturePrefix = _VmwNsxTCapacityFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 22)
)
if mibBuilder.loadTexts:
    vmwNsxTCapacityFeaturePrefix.setStatus("current")
_VmwNsxTCapacityFeature_ObjectIdentity = ObjectIdentity
vmwNsxTCapacityFeature = _VmwNsxTCapacityFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 22, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTCapacityFeature.setStatus("current")
_VmwNsxTAuditLogHealthFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTAuditLogHealthFeaturePrefix = _VmwNsxTAuditLogHealthFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 24)
)
if mibBuilder.loadTexts:
    vmwNsxTAuditLogHealthFeaturePrefix.setStatus("current")
_VmwNsxTAuditLogHealthFeature_ObjectIdentity = ObjectIdentity
vmwNsxTAuditLogHealthFeature = _VmwNsxTAuditLogHealthFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 24, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTAuditLogHealthFeature.setStatus("current")
_VmwNsxTRoutingFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTRoutingFeaturePrefix = _VmwNsxTRoutingFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28)
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingFeaturePrefix.setStatus("current")
_VmwNsxTRoutingFeature_ObjectIdentity = ObjectIdentity
vmwNsxTRoutingFeature = _VmwNsxTRoutingFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingFeature.setStatus("current")
_VmwNsxTDNSFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTDNSFeaturePrefix = _VmwNsxTDNSFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 30)
)
if mibBuilder.loadTexts:
    vmwNsxTDNSFeaturePrefix.setStatus("current")
_VmwNsxTDNSFeature_ObjectIdentity = ObjectIdentity
vmwNsxTDNSFeature = _VmwNsxTDNSFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 30, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTDNSFeature.setStatus("current")
_VmwNsxTDistributedFirewallFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTDistributedFirewallFeaturePrefix = _VmwNsxTDistributedFirewallFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 31)
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedFirewallFeaturePrefix.setStatus("current")
_VmwNsxTDistributedFirewallFeature_ObjectIdentity = ObjectIdentity
vmwNsxTDistributedFirewallFeature = _VmwNsxTDistributedFirewallFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 31, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedFirewallFeature.setStatus("current")
_VmwNsxTFederationFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTFederationFeaturePrefix = _VmwNsxTFederationFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32)
)
if mibBuilder.loadTexts:
    vmwNsxTFederationFeaturePrefix.setStatus("current")
_VmwNsxTFederationFeature_ObjectIdentity = ObjectIdentity
vmwNsxTFederationFeature = _VmwNsxTFederationFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTFederationFeature.setStatus("current")
_VmwNsxTDistributedIDSIPSFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTDistributedIDSIPSFeaturePrefix = _VmwNsxTDistributedIDSIPSFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33)
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSFeaturePrefix.setStatus("current")
_VmwNsxTDistributedIDSIPSFeature_ObjectIdentity = ObjectIdentity
vmwNsxTDistributedIDSIPSFeature = _VmwNsxTDistributedIDSIPSFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSFeature.setStatus("current")
_VmwNsxTCommunicationFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTCommunicationFeaturePrefix = _VmwNsxTCommunicationFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35)
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationFeaturePrefix.setStatus("current")
_VmwNsxTCommunicationFeature_ObjectIdentity = ObjectIdentity
vmwNsxTCommunicationFeature = _VmwNsxTCommunicationFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationFeature.setStatus("current")
_VmwNsxTIdentityFirewallFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTIdentityFirewallFeaturePrefix = _VmwNsxTIdentityFirewallFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 36)
)
if mibBuilder.loadTexts:
    vmwNsxTIdentityFirewallFeaturePrefix.setStatus("current")
_VmwNsxTIdentityFirewallFeature_ObjectIdentity = ObjectIdentity
vmwNsxTIdentityFirewallFeature = _VmwNsxTIdentityFirewallFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 36, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTIdentityFirewallFeature.setStatus("current")
_VmwNsxTIPAMFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTIPAMFeaturePrefix = _VmwNsxTIPAMFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 38)
)
if mibBuilder.loadTexts:
    vmwNsxTIPAMFeaturePrefix.setStatus("current")
_VmwNsxTIPAMFeature_ObjectIdentity = ObjectIdentity
vmwNsxTIPAMFeature = _VmwNsxTIPAMFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 38, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTIPAMFeature.setStatus("current")
_VmwNsxTGatewayFirewallFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTGatewayFirewallFeaturePrefix = _VmwNsxTGatewayFirewallFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 39)
)
if mibBuilder.loadTexts:
    vmwNsxTGatewayFirewallFeaturePrefix.setStatus("current")
_VmwNsxTGatewayFirewallFeature_ObjectIdentity = ObjectIdentity
vmwNsxTGatewayFirewallFeature = _VmwNsxTGatewayFirewallFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 39, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTGatewayFirewallFeature.setStatus("current")
_VmwNsxTClusteringFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTClusteringFeaturePrefix = _VmwNsxTClusteringFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 40)
)
if mibBuilder.loadTexts:
    vmwNsxTClusteringFeaturePrefix.setStatus("current")
_VmwNsxTClusteringFeature_ObjectIdentity = ObjectIdentity
vmwNsxTClusteringFeature = _VmwNsxTClusteringFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 40, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTClusteringFeature.setStatus("current")
_VmwNsxTNSXApplicationPlatformCommunicationFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTNSXApplicationPlatformCommunicationFeaturePrefix = _VmwNsxTNSXApplicationPlatformCommunicationFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 41)
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformCommunicationFeaturePrefix.setStatus("current")
_VmwNsxTNSXApplicationPlatformCommunicationFeature_ObjectIdentity = ObjectIdentity
vmwNsxTNSXApplicationPlatformCommunicationFeature = _VmwNsxTNSXApplicationPlatformCommunicationFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 41, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformCommunicationFeature.setStatus("current")
_VmwNsxTMTUCheckFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTMTUCheckFeaturePrefix = _VmwNsxTMTUCheckFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 42)
)
if mibBuilder.loadTexts:
    vmwNsxTMTUCheckFeaturePrefix.setStatus("current")
_VmwNsxTMTUCheckFeature_ObjectIdentity = ObjectIdentity
vmwNsxTMTUCheckFeature = _VmwNsxTMTUCheckFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 42, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTMTUCheckFeature.setStatus("current")
_VmwNsxTNSXApplicationPlatformHealthFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTNSXApplicationPlatformHealthFeaturePrefix = _VmwNsxTNSXApplicationPlatformHealthFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43)
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthFeaturePrefix.setStatus("current")
_VmwNsxTNSXApplicationPlatformHealthFeature_ObjectIdentity = ObjectIdentity
vmwNsxTNSXApplicationPlatformHealthFeature = _VmwNsxTNSXApplicationPlatformHealthFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthFeature.setStatus("current")
_VmwNsxTEdgeFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTEdgeFeaturePrefix = _VmwNsxTEdgeFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 45)
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeFeaturePrefix.setStatus("current")
_VmwNsxTEdgeFeature_ObjectIdentity = ObjectIdentity
vmwNsxTEdgeFeature = _VmwNsxTEdgeFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 45, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeFeature.setStatus("current")
_VmwNsxTNATFeaturePrefix_ObjectIdentity = ObjectIdentity
vmwNsxTNATFeaturePrefix = _VmwNsxTNATFeaturePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 46)
)
if mibBuilder.loadTexts:
    vmwNsxTNATFeaturePrefix.setStatus("current")
_VmwNsxTNATFeature_ObjectIdentity = ObjectIdentity
vmwNsxTNATFeature = _VmwNsxTNATFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 46, 0)
)
if mibBuilder.loadTexts:
    vmwNsxTNATFeature.setStatus("current")
_VmwNsxTDataCenterData_ObjectIdentity = ObjectIdentity
vmwNsxTDataCenterData = _VmwNsxTDataCenterData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1)
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterData.setStatus("current")
_VmwNsxTDataCenterTimestamp_Type = DateAndTime
_VmwNsxTDataCenterTimestamp_Object = MibScalar
vmwNsxTDataCenterTimestamp = _VmwNsxTDataCenterTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 1),
    _VmwNsxTDataCenterTimestamp_Type()
)
vmwNsxTDataCenterTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterTimestamp.setStatus("current")
_VmwNsxTDataCenterFeatureName_Type = VmwNsxTDataCenterFeatureIdType
_VmwNsxTDataCenterFeatureName_Object = MibScalar
vmwNsxTDataCenterFeatureName = _VmwNsxTDataCenterFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 2),
    _VmwNsxTDataCenterFeatureName_Type()
)
vmwNsxTDataCenterFeatureName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterFeatureName.setStatus("current")
_VmwNsxTDataCenterEventType_Type = VmwNsxTDataCenterEventTypeType
_VmwNsxTDataCenterEventType_Object = MibScalar
vmwNsxTDataCenterEventType = _VmwNsxTDataCenterEventType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 3),
    _VmwNsxTDataCenterEventType_Type()
)
vmwNsxTDataCenterEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEventType.setStatus("current")
_VmwNsxTDataCenterEventSeverity_Type = VmwNsxTDataCenterSeverityType
_VmwNsxTDataCenterEventSeverity_Object = MibScalar
vmwNsxTDataCenterEventSeverity = _VmwNsxTDataCenterEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 4),
    _VmwNsxTDataCenterEventSeverity_Type()
)
vmwNsxTDataCenterEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEventSeverity.setStatus("current")
_VmwNsxTDataCenterNodeId_Type = VmwNsxTDataCenterNodeIdType
_VmwNsxTDataCenterNodeId_Object = MibScalar
vmwNsxTDataCenterNodeId = _VmwNsxTDataCenterNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 5),
    _VmwNsxTDataCenterNodeId_Type()
)
vmwNsxTDataCenterNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNodeId.setStatus("current")
_VmwNsxTDataCenterNodeType_Type = VmwNsxTDataCenterNodeTypeType
_VmwNsxTDataCenterNodeType_Object = MibScalar
vmwNsxTDataCenterNodeType = _VmwNsxTDataCenterNodeType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 6),
    _VmwNsxTDataCenterNodeType_Type()
)
vmwNsxTDataCenterNodeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNodeType.setStatus("current")
_VmwNsxTDataCenterEntityId_Type = VmwNsxTDataCenterEntityIdType
_VmwNsxTDataCenterEntityId_Object = MibScalar
vmwNsxTDataCenterEntityId = _VmwNsxTDataCenterEntityId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 21),
    _VmwNsxTDataCenterEntityId_Type()
)
vmwNsxTDataCenterEntityId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEntityId.setStatus("current")
_VmwNsxTDataCenterSystemResourceUsage_Type = VmwNsxTDataCenterSystemResourceUsageType
_VmwNsxTDataCenterSystemResourceUsage_Object = MibScalar
vmwNsxTDataCenterSystemResourceUsage = _VmwNsxTDataCenterSystemResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 22),
    _VmwNsxTDataCenterSystemResourceUsage_Type()
)
vmwNsxTDataCenterSystemResourceUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterSystemResourceUsage.setStatus("current")
_VmwNsxTDataCenterDiskPartitionName_Type = VmwNsxTDataCenterDiskPartitionNameType
_VmwNsxTDataCenterDiskPartitionName_Object = MibScalar
vmwNsxTDataCenterDiskPartitionName = _VmwNsxTDataCenterDiskPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 23),
    _VmwNsxTDataCenterDiskPartitionName_Type()
)
vmwNsxTDataCenterDiskPartitionName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterDiskPartitionName.setStatus("current")
_VmwNsxTDataCenterLicenseEditionType_Type = VmwNsxTDataCenterLicenseEditionTypeType
_VmwNsxTDataCenterLicenseEditionType_Object = MibScalar
vmwNsxTDataCenterLicenseEditionType = _VmwNsxTDataCenterLicenseEditionType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 24),
    _VmwNsxTDataCenterLicenseEditionType_Type()
)
vmwNsxTDataCenterLicenseEditionType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterLicenseEditionType.setStatus("current")
_VmwNsxTDataCenterApplianceAddress_Type = VmwNsxTDataCenterApplianceAddressType
_VmwNsxTDataCenterApplianceAddress_Object = MibScalar
vmwNsxTDataCenterApplianceAddress = _VmwNsxTDataCenterApplianceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 25),
    _VmwNsxTDataCenterApplianceAddress_Type()
)
vmwNsxTDataCenterApplianceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterApplianceAddress.setStatus("current")
_VmwNsxTDataCenterCurrentGatewayState_Type = VmwNsxTDataCenterCurrentGatewayStateType
_VmwNsxTDataCenterCurrentGatewayState_Object = MibScalar
vmwNsxTDataCenterCurrentGatewayState = _VmwNsxTDataCenterCurrentGatewayState_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 26),
    _VmwNsxTDataCenterCurrentGatewayState_Type()
)
vmwNsxTDataCenterCurrentGatewayState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterCurrentGatewayState.setStatus("current")
_VmwNsxTDataCenterCurrentServiceState_Type = VmwNsxTDataCenterCurrentServiceStateType
_VmwNsxTDataCenterCurrentServiceState_Object = MibScalar
vmwNsxTDataCenterCurrentServiceState = _VmwNsxTDataCenterCurrentServiceState_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 27),
    _VmwNsxTDataCenterCurrentServiceState_Type()
)
vmwNsxTDataCenterCurrentServiceState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterCurrentServiceState.setStatus("current")
_VmwNsxTDataCenterDatapathResourceUsage_Type = VmwNsxTDataCenterDatapathResourceUsageType
_VmwNsxTDataCenterDatapathResourceUsage_Object = MibScalar
vmwNsxTDataCenterDatapathResourceUsage = _VmwNsxTDataCenterDatapathResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 28),
    _VmwNsxTDataCenterDatapathResourceUsage_Type()
)
vmwNsxTDataCenterDatapathResourceUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterDatapathResourceUsage.setStatus("current")
_VmwNsxTDataCenterDHCPPoolUsage_Type = VmwNsxTDataCenterDHCPPoolUsageType
_VmwNsxTDataCenterDHCPPoolUsage_Object = MibScalar
vmwNsxTDataCenterDHCPPoolUsage = _VmwNsxTDataCenterDHCPPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 29),
    _VmwNsxTDataCenterDHCPPoolUsage_Type()
)
vmwNsxTDataCenterDHCPPoolUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterDHCPPoolUsage.setStatus("current")
_VmwNsxTDataCenterEdgeServiceName_Type = VmwNsxTDataCenterEdgeServiceNameType
_VmwNsxTDataCenterEdgeServiceName_Object = MibScalar
vmwNsxTDataCenterEdgeServiceName = _VmwNsxTDataCenterEdgeServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 30),
    _VmwNsxTDataCenterEdgeServiceName_Type()
)
vmwNsxTDataCenterEdgeServiceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEdgeServiceName.setStatus("current")
_VmwNsxTDataCenterFailureReason_Type = VmwNsxTDataCenterFailureReasonType
_VmwNsxTDataCenterFailureReason_Object = MibScalar
vmwNsxTDataCenterFailureReason = _VmwNsxTDataCenterFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 31),
    _VmwNsxTDataCenterFailureReason_Type()
)
vmwNsxTDataCenterFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterFailureReason.setStatus("current")
_VmwNsxTDataCenterPreviousGatewayState_Type = VmwNsxTDataCenterPreviousGatewayStateType
_VmwNsxTDataCenterPreviousGatewayState_Object = MibScalar
vmwNsxTDataCenterPreviousGatewayState = _VmwNsxTDataCenterPreviousGatewayState_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 32),
    _VmwNsxTDataCenterPreviousGatewayState_Type()
)
vmwNsxTDataCenterPreviousGatewayState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterPreviousGatewayState.setStatus("current")
_VmwNsxTDataCenterPreviousServiceState_Type = VmwNsxTDataCenterPreviousServiceStateType
_VmwNsxTDataCenterPreviousServiceState_Object = MibScalar
vmwNsxTDataCenterPreviousServiceState = _VmwNsxTDataCenterPreviousServiceState_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 33),
    _VmwNsxTDataCenterPreviousServiceState_Type()
)
vmwNsxTDataCenterPreviousServiceState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterPreviousServiceState.setStatus("current")
_VmwNsxTDataCenterSystemUsageThreshold_Type = VmwNsxTDataCenterSystemUsageThresholdType
_VmwNsxTDataCenterSystemUsageThreshold_Object = MibScalar
vmwNsxTDataCenterSystemUsageThreshold = _VmwNsxTDataCenterSystemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 34),
    _VmwNsxTDataCenterSystemUsageThreshold_Type()
)
vmwNsxTDataCenterSystemUsageThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterSystemUsageThreshold.setStatus("current")
_VmwNsxTDataCenterUsername_Type = VmwNsxTDataCenterUsernameType
_VmwNsxTDataCenterUsername_Object = MibScalar
vmwNsxTDataCenterUsername = _VmwNsxTDataCenterUsername_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 35),
    _VmwNsxTDataCenterUsername_Type()
)
vmwNsxTDataCenterUsername.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterUsername.setStatus("current")
_VmwNsxTDataCenterDHCPServerId_Type = VmwNsxTDataCenterDHCPServerIdType
_VmwNsxTDataCenterDHCPServerId_Object = MibScalar
vmwNsxTDataCenterDHCPServerId = _VmwNsxTDataCenterDHCPServerId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 36),
    _VmwNsxTDataCenterDHCPServerId_Type()
)
vmwNsxTDataCenterDHCPServerId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterDHCPServerId.setStatus("current")
_VmwNsxTDataCenterServiceName_Type = VmwNsxTDataCenterServiceNameType
_VmwNsxTDataCenterServiceName_Object = MibScalar
vmwNsxTDataCenterServiceName = _VmwNsxTDataCenterServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 37),
    _VmwNsxTDataCenterServiceName_Type()
)
vmwNsxTDataCenterServiceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterServiceName.setStatus("current")
_VmwNsxTDataCenterIntelligenceNodeId_Type = VmwNsxTDataCenterIntelligenceNodeIdType
_VmwNsxTDataCenterIntelligenceNodeId_Object = MibScalar
vmwNsxTDataCenterIntelligenceNodeId = _VmwNsxTDataCenterIntelligenceNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 38),
    _VmwNsxTDataCenterIntelligenceNodeId_Type()
)
vmwNsxTDataCenterIntelligenceNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterIntelligenceNodeId.setStatus("current")
_VmwNsxTDataCenterHostnameOrIPAddressWithPort_Type = VmwNsxTDataCenterHostnameOrIPAddressWithPortType
_VmwNsxTDataCenterHostnameOrIPAddressWithPort_Object = MibScalar
vmwNsxTDataCenterHostnameOrIPAddressWithPort = _VmwNsxTDataCenterHostnameOrIPAddressWithPort_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 39),
    _VmwNsxTDataCenterHostnameOrIPAddressWithPort_Type()
)
vmwNsxTDataCenterHostnameOrIPAddressWithPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterHostnameOrIPAddressWithPort.setStatus("current")
_VmwNsxTDataCenterEventId_Type = VmwNsxTDataCenterEventIdType
_VmwNsxTDataCenterEventId_Object = MibScalar
vmwNsxTDataCenterEventId = _VmwNsxTDataCenterEventId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 40),
    _VmwNsxTDataCenterEventId_Type()
)
vmwNsxTDataCenterEventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEventId.setStatus("current")
_VmwNsxTDataCenterActiveGlobalManager_Type = VmwNsxTDataCenterActiveGlobalManagerType
_VmwNsxTDataCenterActiveGlobalManager_Object = MibScalar
vmwNsxTDataCenterActiveGlobalManager = _VmwNsxTDataCenterActiveGlobalManager_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 41),
    _VmwNsxTDataCenterActiveGlobalManager_Type()
)
vmwNsxTDataCenterActiveGlobalManager.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterActiveGlobalManager.setStatus("current")
_VmwNsxTDataCenterActiveGlobalManagers_Type = VmwNsxTDataCenterActiveGlobalManagersType
_VmwNsxTDataCenterActiveGlobalManagers_Object = MibScalar
vmwNsxTDataCenterActiveGlobalManagers = _VmwNsxTDataCenterActiveGlobalManagers_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 42),
    _VmwNsxTDataCenterActiveGlobalManagers_Type()
)
vmwNsxTDataCenterActiveGlobalManagers.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterActiveGlobalManagers.setStatus("current")
_VmwNsxTDataCenterSessionDownReason_Type = VmwNsxTDataCenterSessionDownReasonType
_VmwNsxTDataCenterSessionDownReason_Object = MibScalar
vmwNsxTDataCenterSessionDownReason = _VmwNsxTDataCenterSessionDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 43),
    _VmwNsxTDataCenterSessionDownReason_Type()
)
vmwNsxTDataCenterSessionDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterSessionDownReason.setStatus("current")
_VmwNsxTDataCenterManagerNodeName_Type = VmwNsxTDataCenterManagerNodeNameType
_VmwNsxTDataCenterManagerNodeName_Object = MibScalar
vmwNsxTDataCenterManagerNodeName = _VmwNsxTDataCenterManagerNodeName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 44),
    _VmwNsxTDataCenterManagerNodeName_Type()
)
vmwNsxTDataCenterManagerNodeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterManagerNodeName.setStatus("current")
_VmwNsxTDataCenterTransportNodeAddress_Type = VmwNsxTDataCenterTransportNodeAddressType
_VmwNsxTDataCenterTransportNodeAddress_Object = MibScalar
vmwNsxTDataCenterTransportNodeAddress = _VmwNsxTDataCenterTransportNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 45),
    _VmwNsxTDataCenterTransportNodeAddress_Type()
)
vmwNsxTDataCenterTransportNodeAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterTransportNodeAddress.setStatus("current")
_VmwNsxTDataCenterTransportNodeName_Type = VmwNsxTDataCenterTransportNodeNameType
_VmwNsxTDataCenterTransportNodeName_Object = MibScalar
vmwNsxTDataCenterTransportNodeName = _VmwNsxTDataCenterTransportNodeName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 46),
    _VmwNsxTDataCenterTransportNodeName_Type()
)
vmwNsxTDataCenterTransportNodeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterTransportNodeName.setStatus("current")
_VmwNsxTDataCenterCentralControlPlaneId_Type = VmwNsxTDataCenterCentralControlPlaneIdType
_VmwNsxTDataCenterCentralControlPlaneId_Object = MibScalar
vmwNsxTDataCenterCentralControlPlaneId = _VmwNsxTDataCenterCentralControlPlaneId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 47),
    _VmwNsxTDataCenterCentralControlPlaneId_Type()
)
vmwNsxTDataCenterCentralControlPlaneId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterCentralControlPlaneId.setStatus("current")
_VmwNsxTDataCenterTunnelDownReason_Type = VmwNsxTDataCenterTunnelDownReasonType
_VmwNsxTDataCenterTunnelDownReason_Object = MibScalar
vmwNsxTDataCenterTunnelDownReason = _VmwNsxTDataCenterTunnelDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 48),
    _VmwNsxTDataCenterTunnelDownReason_Type()
)
vmwNsxTDataCenterTunnelDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterTunnelDownReason.setStatus("current")
_VmwNsxTDataCenterHeapType_Type = VmwNsxTDataCenterHeapTypeType
_VmwNsxTDataCenterHeapType_Object = MibScalar
vmwNsxTDataCenterHeapType = _VmwNsxTDataCenterHeapType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 49),
    _VmwNsxTDataCenterHeapType_Type()
)
vmwNsxTDataCenterHeapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterHeapType.setStatus("current")
_VmwNsxTDataCenterMempoolName_Type = VmwNsxTDataCenterMempoolNameType
_VmwNsxTDataCenterMempoolName_Object = MibScalar
vmwNsxTDataCenterMempoolName = _VmwNsxTDataCenterMempoolName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 50),
    _VmwNsxTDataCenterMempoolName_Type()
)
vmwNsxTDataCenterMempoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterMempoolName.setStatus("current")
_VmwNsxTDataCenterPasswordExpirationDays_Type = VmwNsxTDataCenterPasswordExpirationDaysType
_VmwNsxTDataCenterPasswordExpirationDays_Object = MibScalar
vmwNsxTDataCenterPasswordExpirationDays = _VmwNsxTDataCenterPasswordExpirationDays_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 51),
    _VmwNsxTDataCenterPasswordExpirationDays_Type()
)
vmwNsxTDataCenterPasswordExpirationDays.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterPasswordExpirationDays.setStatus("current")
_VmwNsxTDataCenterBGPNeighborIP_Type = VmwNsxTDataCenterBGPNeighborIPType
_VmwNsxTDataCenterBGPNeighborIP_Object = MibScalar
vmwNsxTDataCenterBGPNeighborIP = _VmwNsxTDataCenterBGPNeighborIP_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 52),
    _VmwNsxTDataCenterBGPNeighborIP_Type()
)
vmwNsxTDataCenterBGPNeighborIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBGPNeighborIP.setStatus("current")
_VmwNsxTDataCenterLDAPServer_Type = VmwNsxTDataCenterLDAPServerType
_VmwNsxTDataCenterLDAPServer_Object = MibScalar
vmwNsxTDataCenterLDAPServer = _VmwNsxTDataCenterLDAPServer_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 53),
    _VmwNsxTDataCenterLDAPServer_Type()
)
vmwNsxTDataCenterLDAPServer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterLDAPServer.setStatus("current")
_VmwNsxTDataCenterPeerAddress_Type = VmwNsxTDataCenterPeerAddressType
_VmwNsxTDataCenterPeerAddress_Object = MibScalar
vmwNsxTDataCenterPeerAddress = _VmwNsxTDataCenterPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 54),
    _VmwNsxTDataCenterPeerAddress_Type()
)
vmwNsxTDataCenterPeerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterPeerAddress.setStatus("current")
_VmwNsxTDataCenterMaxIDSEventsAllowed_Type = VmwNsxTDataCenterMaxIDSEventsAllowedType
_VmwNsxTDataCenterMaxIDSEventsAllowed_Object = MibScalar
vmwNsxTDataCenterMaxIDSEventsAllowed = _VmwNsxTDataCenterMaxIDSEventsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 55),
    _VmwNsxTDataCenterMaxIDSEventsAllowed_Type()
)
vmwNsxTDataCenterMaxIDSEventsAllowed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterMaxIDSEventsAllowed.setStatus("current")
_VmwNsxTDataCenterStaticAddress_Type = VmwNsxTDataCenterStaticAddressType
_VmwNsxTDataCenterStaticAddress_Object = MibScalar
vmwNsxTDataCenterStaticAddress = _VmwNsxTDataCenterStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 56),
    _VmwNsxTDataCenterStaticAddress_Type()
)
vmwNsxTDataCenterStaticAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterStaticAddress.setStatus("current")
_VmwNsxTDataCenterDuplicateIPAddress_Type = VmwNsxTDataCenterDuplicateIPAddressType
_VmwNsxTDataCenterDuplicateIPAddress_Object = MibScalar
vmwNsxTDataCenterDuplicateIPAddress = _VmwNsxTDataCenterDuplicateIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 57),
    _VmwNsxTDataCenterDuplicateIPAddress_Type()
)
vmwNsxTDataCenterDuplicateIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterDuplicateIPAddress.setStatus("current")
_VmwNsxTDataCenterCapacityDisplayName_Type = VmwNsxTDataCenterCapacityDisplayNameType
_VmwNsxTDataCenterCapacityDisplayName_Object = MibScalar
vmwNsxTDataCenterCapacityDisplayName = _VmwNsxTDataCenterCapacityDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 58),
    _VmwNsxTDataCenterCapacityDisplayName_Type()
)
vmwNsxTDataCenterCapacityDisplayName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterCapacityDisplayName.setStatus("current")
_VmwNsxTDataCenterCapacityUsageCount_Type = VmwNsxTDataCenterCapacityUsageCountType
_VmwNsxTDataCenterCapacityUsageCount_Object = MibScalar
vmwNsxTDataCenterCapacityUsageCount = _VmwNsxTDataCenterCapacityUsageCount_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 59),
    _VmwNsxTDataCenterCapacityUsageCount_Type()
)
vmwNsxTDataCenterCapacityUsageCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterCapacityUsageCount.setStatus("current")
_VmwNsxTDataCenterEdgeNICName_Type = VmwNsxTDataCenterEdgeNICNameType
_VmwNsxTDataCenterEdgeNICName_Object = MibScalar
vmwNsxTDataCenterEdgeNICName = _VmwNsxTDataCenterEdgeNICName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 60),
    _VmwNsxTDataCenterEdgeNICName_Type()
)
vmwNsxTDataCenterEdgeNICName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEdgeNICName.setStatus("current")
_VmwNsxTDataCenterRxRingBufferOverflowPercentage_Type = VmwNsxTDataCenterRxRingBufferOverflowPercentageType
_VmwNsxTDataCenterRxRingBufferOverflowPercentage_Object = MibScalar
vmwNsxTDataCenterRxRingBufferOverflowPercentage = _VmwNsxTDataCenterRxRingBufferOverflowPercentage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 61),
    _VmwNsxTDataCenterRxRingBufferOverflowPercentage_Type()
)
vmwNsxTDataCenterRxRingBufferOverflowPercentage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterRxRingBufferOverflowPercentage.setStatus("current")
_VmwNsxTDataCenterTxRingBufferOverflowPercentage_Type = VmwNsxTDataCenterTxRingBufferOverflowPercentageType
_VmwNsxTDataCenterTxRingBufferOverflowPercentage_Object = MibScalar
vmwNsxTDataCenterTxRingBufferOverflowPercentage = _VmwNsxTDataCenterTxRingBufferOverflowPercentage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 62),
    _VmwNsxTDataCenterTxRingBufferOverflowPercentage_Type()
)
vmwNsxTDataCenterTxRingBufferOverflowPercentage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterTxRingBufferOverflowPercentage.setStatus("current")
_VmwNsxTDataCenterSrId_Type = VmwNsxTDataCenterSrIdType
_VmwNsxTDataCenterSrId_Object = MibScalar
vmwNsxTDataCenterSrId = _VmwNsxTDataCenterSrId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 63),
    _VmwNsxTDataCenterSrId_Type()
)
vmwNsxTDataCenterSrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterSrId.setStatus("current")
_VmwNsxTDataCenterIDSEventsCount_Type = VmwNsxTDataCenterIDSEventsCountType
_VmwNsxTDataCenterIDSEventsCount_Object = MibScalar
vmwNsxTDataCenterIDSEventsCount = _VmwNsxTDataCenterIDSEventsCount_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 64),
    _VmwNsxTDataCenterIDSEventsCount_Type()
)
vmwNsxTDataCenterIDSEventsCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterIDSEventsCount.setStatus("current")
_VmwNsxTDataCenterRemoteSiteName_Type = VmwNsxTDataCenterRemoteSiteNameType
_VmwNsxTDataCenterRemoteSiteName_Object = MibScalar
vmwNsxTDataCenterRemoteSiteName = _VmwNsxTDataCenterRemoteSiteName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 65),
    _VmwNsxTDataCenterRemoteSiteName_Type()
)
vmwNsxTDataCenterRemoteSiteName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterRemoteSiteName.setStatus("current")
_VmwNsxTDataCenterBGPSourceIP_Type = VmwNsxTDataCenterBGPSourceIPType
_VmwNsxTDataCenterBGPSourceIP_Object = MibScalar
vmwNsxTDataCenterBGPSourceIP = _VmwNsxTDataCenterBGPSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 66),
    _VmwNsxTDataCenterBGPSourceIP_Type()
)
vmwNsxTDataCenterBGPSourceIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBGPSourceIP.setStatus("current")
_VmwNsxTDataCenterRemoteSiteId_Type = VmwNsxTDataCenterRemoteSiteIdType
_VmwNsxTDataCenterRemoteSiteId_Object = MibScalar
vmwNsxTDataCenterRemoteSiteId = _VmwNsxTDataCenterRemoteSiteId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 67),
    _VmwNsxTDataCenterRemoteSiteId_Type()
)
vmwNsxTDataCenterRemoteSiteId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterRemoteSiteId.setStatus("current")
_VmwNsxTDataCenterSiteId_Type = VmwNsxTDataCenterSiteIdType
_VmwNsxTDataCenterSiteId_Object = MibScalar
vmwNsxTDataCenterSiteId = _VmwNsxTDataCenterSiteId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 68),
    _VmwNsxTDataCenterSiteId_Type()
)
vmwNsxTDataCenterSiteId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterSiteId.setStatus("current")
_VmwNsxTDataCenterSiteName_Type = VmwNsxTDataCenterSiteNameType
_VmwNsxTDataCenterSiteName_Object = MibScalar
vmwNsxTDataCenterSiteName = _VmwNsxTDataCenterSiteName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 69),
    _VmwNsxTDataCenterSiteName_Type()
)
vmwNsxTDataCenterSiteName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterSiteName.setStatus("current")
_VmwNsxTDataCenterLrId_Type = VmwNsxTDataCenterLrIdType
_VmwNsxTDataCenterLrId_Object = MibScalar
vmwNsxTDataCenterLrId = _VmwNsxTDataCenterLrId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 70),
    _VmwNsxTDataCenterLrId_Type()
)
vmwNsxTDataCenterLrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterLrId.setStatus("current")
_VmwNsxTDataCenterRxMisses_Type = VmwNsxTDataCenterRxMissesType
_VmwNsxTDataCenterRxMisses_Object = MibScalar
vmwNsxTDataCenterRxMisses = _VmwNsxTDataCenterRxMisses_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 71),
    _VmwNsxTDataCenterRxMisses_Type()
)
vmwNsxTDataCenterRxMisses.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterRxMisses.setStatus("current")
_VmwNsxTDataCenterRxProcessed_Type = VmwNsxTDataCenterRxProcessedType
_VmwNsxTDataCenterRxProcessed_Object = MibScalar
vmwNsxTDataCenterRxProcessed = _VmwNsxTDataCenterRxProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 72),
    _VmwNsxTDataCenterRxProcessed_Type()
)
vmwNsxTDataCenterRxProcessed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterRxProcessed.setStatus("current")
_VmwNsxTDataCenterTxMisses_Type = VmwNsxTDataCenterTxMissesType
_VmwNsxTDataCenterTxMisses_Object = MibScalar
vmwNsxTDataCenterTxMisses = _VmwNsxTDataCenterTxMisses_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 73),
    _VmwNsxTDataCenterTxMisses_Type()
)
vmwNsxTDataCenterTxMisses.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterTxMisses.setStatus("current")
_VmwNsxTDataCenterTxProcessed_Type = VmwNsxTDataCenterTxProcessedType
_VmwNsxTDataCenterTxProcessed_Object = MibScalar
vmwNsxTDataCenterTxProcessed = _VmwNsxTDataCenterTxProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 74),
    _VmwNsxTDataCenterTxProcessed_Type()
)
vmwNsxTDataCenterTxProcessed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterTxProcessed.setStatus("current")
_VmwNsxTDataCenterLrportId_Type = VmwNsxTDataCenterLrportIdType
_VmwNsxTDataCenterLrportId_Object = MibScalar
vmwNsxTDataCenterLrportId = _VmwNsxTDataCenterLrportId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 75),
    _VmwNsxTDataCenterLrportId_Type()
)
vmwNsxTDataCenterLrportId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterLrportId.setStatus("current")
_VmwNsxTDataCenterServiceIP_Type = VmwNsxTDataCenterServiceIPType
_VmwNsxTDataCenterServiceIP_Object = MibScalar
vmwNsxTDataCenterServiceIP = _VmwNsxTDataCenterServiceIP_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 77),
    _VmwNsxTDataCenterServiceIP_Type()
)
vmwNsxTDataCenterServiceIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterServiceIP.setStatus("current")
_VmwNsxTDataCenterRemoteManagerNodeId_Type = VmwNsxTDataCenterRemoteManagerNodeIdType
_VmwNsxTDataCenterRemoteManagerNodeId_Object = MibScalar
vmwNsxTDataCenterRemoteManagerNodeId = _VmwNsxTDataCenterRemoteManagerNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 80),
    _VmwNsxTDataCenterRemoteManagerNodeId_Type()
)
vmwNsxTDataCenterRemoteManagerNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterRemoteManagerNodeId.setStatus("current")
_VmwNsxTDataCenterDirectoryDomain_Type = VmwNsxTDataCenterDirectoryDomainType
_VmwNsxTDataCenterDirectoryDomain_Object = MibScalar
vmwNsxTDataCenterDirectoryDomain = _VmwNsxTDataCenterDirectoryDomain_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 81),
    _VmwNsxTDataCenterDirectoryDomain_Type()
)
vmwNsxTDataCenterDirectoryDomain.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterDirectoryDomain.setStatus("current")
_VmwNsxTDataCenterTimeoutInMinutes_Type = VmwNsxTDataCenterTimeoutInMinutesType
_VmwNsxTDataCenterTimeoutInMinutes_Object = MibScalar
vmwNsxTDataCenterTimeoutInMinutes = _VmwNsxTDataCenterTimeoutInMinutes_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 82),
    _VmwNsxTDataCenterTimeoutInMinutes_Type()
)
vmwNsxTDataCenterTimeoutInMinutes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterTimeoutInMinutes.setStatus("current")
_VmwNsxTDataCenterMaxCapacityThreshold_Type = VmwNsxTDataCenterMaxCapacityThresholdType
_VmwNsxTDataCenterMaxCapacityThreshold_Object = MibScalar
vmwNsxTDataCenterMaxCapacityThreshold = _VmwNsxTDataCenterMaxCapacityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 83),
    _VmwNsxTDataCenterMaxCapacityThreshold_Type()
)
vmwNsxTDataCenterMaxCapacityThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterMaxCapacityThreshold.setStatus("current")
_VmwNsxTDataCenterMinCapacityThreshold_Type = VmwNsxTDataCenterMinCapacityThresholdType
_VmwNsxTDataCenterMinCapacityThreshold_Object = MibScalar
vmwNsxTDataCenterMinCapacityThreshold = _VmwNsxTDataCenterMinCapacityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 84),
    _VmwNsxTDataCenterMinCapacityThreshold_Type()
)
vmwNsxTDataCenterMinCapacityThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterMinCapacityThreshold.setStatus("current")
_VmwNsxTDataCenterMaxSupportedCapacityCount_Type = VmwNsxTDataCenterMaxSupportedCapacityCountType
_VmwNsxTDataCenterMaxSupportedCapacityCount_Object = MibScalar
vmwNsxTDataCenterMaxSupportedCapacityCount = _VmwNsxTDataCenterMaxSupportedCapacityCount_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 85),
    _VmwNsxTDataCenterMaxSupportedCapacityCount_Type()
)
vmwNsxTDataCenterMaxSupportedCapacityCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterMaxSupportedCapacityCount.setStatus("current")
_VmwNsxTDataCenterLatencySource_Type = VmwNsxTDataCenterLatencySourceType
_VmwNsxTDataCenterLatencySource_Object = MibScalar
vmwNsxTDataCenterLatencySource = _VmwNsxTDataCenterLatencySource_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 86),
    _VmwNsxTDataCenterLatencySource_Type()
)
vmwNsxTDataCenterLatencySource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterLatencySource.setStatus("current")
_VmwNsxTDataCenterLatencyThreshold_Type = VmwNsxTDataCenterLatencyThresholdType
_VmwNsxTDataCenterLatencyThreshold_Object = MibScalar
vmwNsxTDataCenterLatencyThreshold = _VmwNsxTDataCenterLatencyThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 87),
    _VmwNsxTDataCenterLatencyThreshold_Type()
)
vmwNsxTDataCenterLatencyThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterLatencyThreshold.setStatus("current")
_VmwNsxTDataCenterLatencyValue_Type = VmwNsxTDataCenterLatencyValueType
_VmwNsxTDataCenterLatencyValue_Object = MibScalar
vmwNsxTDataCenterLatencyValue = _VmwNsxTDataCenterLatencyValue_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 88),
    _VmwNsxTDataCenterLatencyValue_Type()
)
vmwNsxTDataCenterLatencyValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterLatencyValue.setStatus("current")
_VmwNsxTDataCenterApplianceFQDN_Type = VmwNsxTDataCenterApplianceFQDNType
_VmwNsxTDataCenterApplianceFQDN_Object = MibScalar
vmwNsxTDataCenterApplianceFQDN = _VmwNsxTDataCenterApplianceFQDN_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 89),
    _VmwNsxTDataCenterApplianceFQDN_Type()
)
vmwNsxTDataCenterApplianceFQDN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterApplianceFQDN.setStatus("current")
_VmwNsxTDataCenterRemoteApplianceAddress_Type = VmwNsxTDataCenterRemoteApplianceAddressType
_VmwNsxTDataCenterRemoteApplianceAddress_Object = MibScalar
vmwNsxTDataCenterRemoteApplianceAddress = _VmwNsxTDataCenterRemoteApplianceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 90),
    _VmwNsxTDataCenterRemoteApplianceAddress_Type()
)
vmwNsxTDataCenterRemoteApplianceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterRemoteApplianceAddress.setStatus("current")
_VmwNsxTDataCenterManagerNodeId_Type = VmwNsxTDataCenterManagerNodeIdType
_VmwNsxTDataCenterManagerNodeId_Object = MibScalar
vmwNsxTDataCenterManagerNodeId = _VmwNsxTDataCenterManagerNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 91),
    _VmwNsxTDataCenterManagerNodeId_Type()
)
vmwNsxTDataCenterManagerNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterManagerNodeId.setStatus("current")
_VmwNsxTDataCenterDisplayedLicenseKey_Type = VmwNsxTDataCenterDisplayedLicenseKeyType
_VmwNsxTDataCenterDisplayedLicenseKey_Object = MibScalar
vmwNsxTDataCenterDisplayedLicenseKey = _VmwNsxTDataCenterDisplayedLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 92),
    _VmwNsxTDataCenterDisplayedLicenseKey_Type()
)
vmwNsxTDataCenterDisplayedLicenseKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterDisplayedLicenseKey.setStatus("current")
_VmwNsxTDataCenterEdgeThreadName_Type = VmwNsxTDataCenterEdgeThreadNameType
_VmwNsxTDataCenterEdgeThreadName_Object = MibScalar
vmwNsxTDataCenterEdgeThreadName = _VmwNsxTDataCenterEdgeThreadName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 93),
    _VmwNsxTDataCenterEdgeThreadName_Type()
)
vmwNsxTDataCenterEdgeThreadName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEdgeThreadName.setStatus("current")
_VmwNsxTDataCenterIntentPath_Type = VmwNsxTDataCenterIntentPathType
_VmwNsxTDataCenterIntentPath_Object = MibScalar
vmwNsxTDataCenterIntentPath = _VmwNsxTDataCenterIntentPath_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 94),
    _VmwNsxTDataCenterIntentPath_Type()
)
vmwNsxTDataCenterIntentPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterIntentPath.setStatus("current")
_VmwNsxTDataCenterFirewallHalfopenFlowUsage_Type = VmwNsxTDataCenterFirewallHalfopenFlowUsageType
_VmwNsxTDataCenterFirewallHalfopenFlowUsage_Object = MibScalar
vmwNsxTDataCenterFirewallHalfopenFlowUsage = _VmwNsxTDataCenterFirewallHalfopenFlowUsage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 95),
    _VmwNsxTDataCenterFirewallHalfopenFlowUsage_Type()
)
vmwNsxTDataCenterFirewallHalfopenFlowUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterFirewallHalfopenFlowUsage.setStatus("current")
_VmwNsxTDataCenterFirewallICMPFlowUsage_Type = VmwNsxTDataCenterFirewallICMPFlowUsageType
_VmwNsxTDataCenterFirewallICMPFlowUsage_Object = MibScalar
vmwNsxTDataCenterFirewallICMPFlowUsage = _VmwNsxTDataCenterFirewallICMPFlowUsage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 96),
    _VmwNsxTDataCenterFirewallICMPFlowUsage_Type()
)
vmwNsxTDataCenterFirewallICMPFlowUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterFirewallICMPFlowUsage.setStatus("current")
_VmwNsxTDataCenterServiceDownReason_Type = VmwNsxTDataCenterServiceDownReasonType
_VmwNsxTDataCenterServiceDownReason_Object = MibScalar
vmwNsxTDataCenterServiceDownReason = _VmwNsxTDataCenterServiceDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 97),
    _VmwNsxTDataCenterServiceDownReason_Type()
)
vmwNsxTDataCenterServiceDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterServiceDownReason.setStatus("current")
_VmwNsxTDataCenterFirewallUDPFlowUsage_Type = VmwNsxTDataCenterFirewallUDPFlowUsageType
_VmwNsxTDataCenterFirewallUDPFlowUsage_Object = MibScalar
vmwNsxTDataCenterFirewallUDPFlowUsage = _VmwNsxTDataCenterFirewallUDPFlowUsage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 98),
    _VmwNsxTDataCenterFirewallUDPFlowUsage_Type()
)
vmwNsxTDataCenterFirewallUDPFlowUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterFirewallUDPFlowUsage.setStatus("current")
_VmwNsxTDataCenterFirewallIPFlowUsage_Type = VmwNsxTDataCenterFirewallIPFlowUsageType
_VmwNsxTDataCenterFirewallIPFlowUsage_Object = MibScalar
vmwNsxTDataCenterFirewallIPFlowUsage = _VmwNsxTDataCenterFirewallIPFlowUsage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 99),
    _VmwNsxTDataCenterFirewallIPFlowUsage_Type()
)
vmwNsxTDataCenterFirewallIPFlowUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterFirewallIPFlowUsage.setStatus("current")
_VmwNsxTDataCenterDNSId_Type = VmwNsxTDataCenterDNSIdType
_VmwNsxTDataCenterDNSId_Object = MibScalar
vmwNsxTDataCenterDNSId = _VmwNsxTDataCenterDNSId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 100),
    _VmwNsxTDataCenterDNSId_Type()
)
vmwNsxTDataCenterDNSId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterDNSId.setStatus("current")
_VmwNsxTDataCenterDNSUpstreamIP_Type = VmwNsxTDataCenterDNSUpstreamIPType
_VmwNsxTDataCenterDNSUpstreamIP_Object = MibScalar
vmwNsxTDataCenterDNSUpstreamIP = _VmwNsxTDataCenterDNSUpstreamIP_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 101),
    _VmwNsxTDataCenterDNSUpstreamIP_Type()
)
vmwNsxTDataCenterDNSUpstreamIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterDNSUpstreamIP.setStatus("current")
_VmwNsxTDataCenterCABundleAgeThreshold_Type = VmwNsxTDataCenterCABundleAgeThresholdType
_VmwNsxTDataCenterCABundleAgeThreshold_Object = MibScalar
vmwNsxTDataCenterCABundleAgeThreshold = _VmwNsxTDataCenterCABundleAgeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 121),
    _VmwNsxTDataCenterCABundleAgeThreshold_Type()
)
vmwNsxTDataCenterCABundleAgeThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterCABundleAgeThreshold.setStatus("current")
_VmwNsxTDataCenterAPICollectionPath_Type = VmwNsxTDataCenterAPICollectionPathType
_VmwNsxTDataCenterAPICollectionPath_Object = MibScalar
vmwNsxTDataCenterAPICollectionPath = _VmwNsxTDataCenterAPICollectionPath_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 122),
    _VmwNsxTDataCenterAPICollectionPath_Type()
)
vmwNsxTDataCenterAPICollectionPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterAPICollectionPath.setStatus("current")
_VmwNsxTDataCenterEdgeNodeSettingMismatchReason_Type = VmwNsxTDataCenterEdgeNodeSettingMismatchReasonType
_VmwNsxTDataCenterEdgeNodeSettingMismatchReason_Object = MibScalar
vmwNsxTDataCenterEdgeNodeSettingMismatchReason = _VmwNsxTDataCenterEdgeNodeSettingMismatchReason_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 123),
    _VmwNsxTDataCenterEdgeNodeSettingMismatchReason_Type()
)
vmwNsxTDataCenterEdgeNodeSettingMismatchReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEdgeNodeSettingMismatchReason.setStatus("current")
_VmwNsxTDataCenterEdgeVMvSphereSettingsMismatchReason_Type = VmwNsxTDataCenterEdgeVMvSphereSettingsMismatchReasonType
_VmwNsxTDataCenterEdgeVMvSphereSettingsMismatchReason_Object = MibScalar
vmwNsxTDataCenterEdgeVMvSphereSettingsMismatchReason = _VmwNsxTDataCenterEdgeVMvSphereSettingsMismatchReason_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 124),
    _VmwNsxTDataCenterEdgeVMvSphereSettingsMismatchReason_Type()
)
vmwNsxTDataCenterEdgeVMvSphereSettingsMismatchReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEdgeVMvSphereSettingsMismatchReason.setStatus("current")
_VmwNsxTDataCenterFirewallSNATPortsUsage_Type = VmwNsxTDataCenterFirewallSNATPortsUsageType
_VmwNsxTDataCenterFirewallSNATPortsUsage_Object = MibScalar
vmwNsxTDataCenterFirewallSNATPortsUsage = _VmwNsxTDataCenterFirewallSNATPortsUsage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 125),
    _VmwNsxTDataCenterFirewallSNATPortsUsage_Type()
)
vmwNsxTDataCenterFirewallSNATPortsUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterFirewallSNATPortsUsage.setStatus("current")
_VmwNsxTDataCenterEdgevSphereLocationMismatchReason_Type = VmwNsxTDataCenterEdgevSphereLocationMismatchReasonType
_VmwNsxTDataCenterEdgevSphereLocationMismatchReason_Object = MibScalar
vmwNsxTDataCenterEdgevSphereLocationMismatchReason = _VmwNsxTDataCenterEdgevSphereLocationMismatchReason_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 126),
    _VmwNsxTDataCenterEdgevSphereLocationMismatchReason_Type()
)
vmwNsxTDataCenterEdgevSphereLocationMismatchReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEdgevSphereLocationMismatchReason.setStatus("current")
_VmwNsxTDataCenterEdgeNodeAndvSphereSettingsMismatchReason_Type = VmwNsxTDataCenterEdgeNodeAndvSphereSettingsMismatchReasonType
_VmwNsxTDataCenterEdgeNodeAndvSphereSettingsMismatchReason_Object = MibScalar
vmwNsxTDataCenterEdgeNodeAndvSphereSettingsMismatchReason = _VmwNsxTDataCenterEdgeNodeAndvSphereSettingsMismatchReason_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 127),
    _VmwNsxTDataCenterEdgeNodeAndvSphereSettingsMismatchReason_Type()
)
vmwNsxTDataCenterEdgeNodeAndvSphereSettingsMismatchReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEdgeNodeAndvSphereSettingsMismatchReason.setStatus("current")
_VmwNsxTDataCenterSNATIPAddress_Type = VmwNsxTDataCenterSNATIPAddressType
_VmwNsxTDataCenterSNATIPAddress_Object = MibScalar
vmwNsxTDataCenterSNATIPAddress = _VmwNsxTDataCenterSNATIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 128),
    _VmwNsxTDataCenterSNATIPAddress_Type()
)
vmwNsxTDataCenterSNATIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterSNATIPAddress.setStatus("current")
_VmwNsxTDataCenterNappClusterId_Type = VmwNsxTDataCenterNappClusterIdType
_VmwNsxTDataCenterNappClusterId_Object = MibScalar
vmwNsxTDataCenterNappClusterId = _VmwNsxTDataCenterNappClusterId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 129),
    _VmwNsxTDataCenterNappClusterId_Type()
)
vmwNsxTDataCenterNappClusterId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNappClusterId.setStatus("current")
_VmwNsxTDataCenterNappMessagingLAGThreshold_Type = VmwNsxTDataCenterNappMessagingLAGThresholdType
_VmwNsxTDataCenterNappMessagingLAGThreshold_Object = MibScalar
vmwNsxTDataCenterNappMessagingLAGThreshold = _VmwNsxTDataCenterNappMessagingLAGThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 130),
    _VmwNsxTDataCenterNappMessagingLAGThreshold_Type()
)
vmwNsxTDataCenterNappMessagingLAGThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNappMessagingLAGThreshold.setStatus("current")
_VmwNsxTDataCenterNappNodeId_Type = VmwNsxTDataCenterNappNodeIdType
_VmwNsxTDataCenterNappNodeId_Object = MibScalar
vmwNsxTDataCenterNappNodeId = _VmwNsxTDataCenterNappNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 131),
    _VmwNsxTDataCenterNappNodeId_Type()
)
vmwNsxTDataCenterNappNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNappNodeId.setStatus("current")
_VmwNsxTDataCenterNappServiceName_Type = VmwNsxTDataCenterNappServiceNameType
_VmwNsxTDataCenterNappServiceName_Object = MibScalar
vmwNsxTDataCenterNappServiceName = _VmwNsxTDataCenterNappServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 132),
    _VmwNsxTDataCenterNappServiceName_Type()
)
vmwNsxTDataCenterNappServiceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNappServiceName.setStatus("current")
_VmwNsxTDataCenterFlowIdentifier_Type = VmwNsxTDataCenterFlowIdentifierType
_VmwNsxTDataCenterFlowIdentifier_Object = MibScalar
vmwNsxTDataCenterFlowIdentifier = _VmwNsxTDataCenterFlowIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 133),
    _VmwNsxTDataCenterFlowIdentifier_Type()
)
vmwNsxTDataCenterFlowIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterFlowIdentifier.setStatus("current")
_VmwNsxTDataCenterSyncIssueReason_Type = VmwNsxTDataCenterSyncIssueReasonType
_VmwNsxTDataCenterSyncIssueReason_Object = MibScalar
vmwNsxTDataCenterSyncIssueReason = _VmwNsxTDataCenterSyncIssueReason_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 134),
    _VmwNsxTDataCenterSyncIssueReason_Type()
)
vmwNsxTDataCenterSyncIssueReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterSyncIssueReason.setStatus("current")
_VmwNsxTDataCenterQueueName_Type = VmwNsxTDataCenterQueueNameType
_VmwNsxTDataCenterQueueName_Object = MibScalar
vmwNsxTDataCenterQueueName = _VmwNsxTDataCenterQueueName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 135),
    _VmwNsxTDataCenterQueueName_Type()
)
vmwNsxTDataCenterQueueName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterQueueName.setStatus("current")
_VmwNsxTDataCenterQueueSize_Type = VmwNsxTDataCenterQueueSizeType
_VmwNsxTDataCenterQueueSize_Object = MibScalar
vmwNsxTDataCenterQueueSize = _VmwNsxTDataCenterQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 136),
    _VmwNsxTDataCenterQueueSize_Type()
)
vmwNsxTDataCenterQueueSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterQueueSize.setStatus("current")
_VmwNsxTDataCenterQueueSizeThreshold_Type = VmwNsxTDataCenterQueueSizeThresholdType
_VmwNsxTDataCenterQueueSizeThreshold_Object = MibScalar
vmwNsxTDataCenterQueueSizeThreshold = _VmwNsxTDataCenterQueueSizeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 137),
    _VmwNsxTDataCenterQueueSizeThreshold_Type()
)
vmwNsxTDataCenterQueueSizeThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterQueueSizeThreshold.setStatus("current")
_VmwNsxTDataCenterGroupType_Type = VmwNsxTDataCenterGroupTypeType
_VmwNsxTDataCenterGroupType_Object = MibScalar
vmwNsxTDataCenterGroupType = _VmwNsxTDataCenterGroupType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 138),
    _VmwNsxTDataCenterGroupType_Type()
)
vmwNsxTDataCenterGroupType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterGroupType.setStatus("current")
_VmwNsxTDataCenterManagerNodeIDS_Type = VmwNsxTDataCenterManagerNodeIDSType
_VmwNsxTDataCenterManagerNodeIDS_Object = MibScalar
vmwNsxTDataCenterManagerNodeIDS = _VmwNsxTDataCenterManagerNodeIDS_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 139),
    _VmwNsxTDataCenterManagerNodeIDS_Type()
)
vmwNsxTDataCenterManagerNodeIDS.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterManagerNodeIDS.setStatus("current")
_VmwNsxTDataCenterServiceRouterId_Type = VmwNsxTDataCenterServiceRouterIdType
_VmwNsxTDataCenterServiceRouterId_Object = MibScalar
vmwNsxTDataCenterServiceRouterId = _VmwNsxTDataCenterServiceRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 140),
    _VmwNsxTDataCenterServiceRouterId_Type()
)
vmwNsxTDataCenterServiceRouterId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterServiceRouterId.setStatus("current")
_VmwNsxTDataCenterTransportNodeId_Type = VmwNsxTDataCenterTransportNodeIdType
_VmwNsxTDataCenterTransportNodeId_Object = MibScalar
vmwNsxTDataCenterTransportNodeId = _VmwNsxTDataCenterTransportNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 141),
    _VmwNsxTDataCenterTransportNodeId_Type()
)
vmwNsxTDataCenterTransportNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterTransportNodeId.setStatus("current")
_VmwNsxTDataCenterFromGMPath_Type = VmwNsxTDataCenterFromGMPathType
_VmwNsxTDataCenterFromGMPath_Object = MibScalar
vmwNsxTDataCenterFromGMPath = _VmwNsxTDataCenterFromGMPath_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 142),
    _VmwNsxTDataCenterFromGMPath_Type()
)
vmwNsxTDataCenterFromGMPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterFromGMPath.setStatus("current")
_VmwNsxTDataCenterToGMPath_Type = VmwNsxTDataCenterToGMPathType
_VmwNsxTDataCenterToGMPath_Object = MibScalar
vmwNsxTDataCenterToGMPath = _VmwNsxTDataCenterToGMPath_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 143),
    _VmwNsxTDataCenterToGMPath_Type()
)
vmwNsxTDataCenterToGMPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterToGMPath.setStatus("current")
_VmwNsxTDataCenterNICThroughput_Type = VmwNsxTDataCenterNICThroughputType
_VmwNsxTDataCenterNICThroughput_Object = MibScalar
vmwNsxTDataCenterNICThroughput = _VmwNsxTDataCenterNICThroughput_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 144),
    _VmwNsxTDataCenterNICThroughput_Type()
)
vmwNsxTDataCenterNICThroughput.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNICThroughput.setStatus("current")
_VmwNsxTDataCenterNICThroughputThreshold_Type = VmwNsxTDataCenterNICThroughputThresholdType
_VmwNsxTDataCenterNICThroughputThreshold_Object = MibScalar
vmwNsxTDataCenterNICThroughputThreshold = _VmwNsxTDataCenterNICThroughputThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 145),
    _VmwNsxTDataCenterNICThroughputThreshold_Type()
)
vmwNsxTDataCenterNICThroughputThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNICThroughputThreshold.setStatus("current")
_VmwNsxTDataCenterEdgeCryptoDrvName_Type = VmwNsxTDataCenterEdgeCryptoDrvNameType
_VmwNsxTDataCenterEdgeCryptoDrvName_Object = MibScalar
vmwNsxTDataCenterEdgeCryptoDrvName = _VmwNsxTDataCenterEdgeCryptoDrvName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 146),
    _VmwNsxTDataCenterEdgeCryptoDrvName_Type()
)
vmwNsxTDataCenterEdgeCryptoDrvName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterEdgeCryptoDrvName.setStatus("current")
_VmwNsxTDataCenterNappNodeName_Type = VmwNsxTDataCenterNappNodeNameType
_VmwNsxTDataCenterNappNodeName_Object = MibScalar
vmwNsxTDataCenterNappNodeName = _VmwNsxTDataCenterNappNodeName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 1, 147),
    _VmwNsxTDataCenterNappNodeName_Type()
)
vmwNsxTDataCenterNappNodeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNappNodeName.setStatus("current")
_VmwNsxTDataCenterConformance_ObjectIdentity = ObjectIdentity
vmwNsxTDataCenterConformance = _VmwNsxTDataCenterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2)
)
_VmwNsxTDataCenterCompliances_ObjectIdentity = ObjectIdentity
vmwNsxTDataCenterCompliances = _VmwNsxTDataCenterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 1)
)
_VmwNsxTDataCenterSMIBGroups_ObjectIdentity = ObjectIdentity
vmwNsxTDataCenterSMIBGroups = _VmwNsxTDataCenterSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2)
)

# Managed Objects groups

vmwNsxTDataCenterNotificationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 1)
)
vmwNsxTDataCenterNotificationInfoGroup.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterBGPNeighborIP"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCurrentGatewayState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCurrentServiceState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDHCPPoolUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDHCPServerId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDatapathResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDuplicateIPAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNICName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeServiceName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFailureReason"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterHeapType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLicenseEditionType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMempoolName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPasswordExpirationDays"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPeerAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPreviousGatewayState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPreviousServiceState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRxRingBufferOverflowPercentage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSessionDownReason"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSrId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterStaticAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTunnelDownReason"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTxRingBufferOverflowPercentage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterUsername"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationInfoGroup.setStatus("current")

vmwNsxTDataCenterNotificationInfoGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 3)
)
vmwNsxTDataCenterNotificationInfoGroup2.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterBGPSourceIP"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationInfoGroup2.setStatus("current")

vmwNsxTDataCenterNotificationInfoGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 5)
)
vmwNsxTDataCenterNotificationInfoGroup3.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRxMisses"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRxProcessed"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTxMisses"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTxProcessed"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationInfoGroup3.setStatus("current")

vmwNsxTDataCenterNotificationInfoGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 7)
)
vmwNsxTDataCenterNotificationInfoGroup4.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterActiveGlobalManager"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterActiveGlobalManagers"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceFQDN"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityDisplayName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityUsageCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCentralControlPlaneId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDirectoryDomain"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDisplayedLicenseKey"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeThreadName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterHostnameOrIPAddressWithPort"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIDSEventsCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLDAPServer"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLatencySource"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLatencyThreshold"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLatencyValue"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMaxCapacityThreshold"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMaxIDSEventsAllowed"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMaxSupportedCapacityCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMinCapacityThreshold"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteApplianceAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteManagerNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimeoutInMinutes"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationInfoGroup4.setStatus("current")

vmwNsxTDataCenterNotificationInfoGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 11)
)
vmwNsxTDataCenterNotificationInfoGroup6.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrportId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceIP"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationInfoGroup6.setStatus("current")

vmwNsxTDataCenterNotificationInfoGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 13)
)
vmwNsxTDataCenterNotificationInfoGroup7.setObjects(
    ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntentPath")
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationInfoGroup7.setStatus("current")

vmwNsxTDataCenterNotificationInfoGroup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 15)
)
vmwNsxTDataCenterNotificationInfoGroup8.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterDNSId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDNSUpstreamIP"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFirewallHalfopenFlowUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFirewallICMPFlowUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFirewallIPFlowUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFirewallUDPFlowUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationInfoGroup8.setStatus("current")

vmwNsxTDataCenterNotificationInfoGroup9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 17)
)
vmwNsxTDataCenterNotificationInfoGroup9.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterAPICollectionPath"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCABundleAgeThreshold"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeCryptoDrvName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNodeSettingMismatchReason"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNodeAndvSphereSettingsMismatchReason"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeVMvSphereSettingsMismatchReason"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgevSphereLocationMismatchReason"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFirewallSNATPortsUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFlowIdentifier"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFromGMPath"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterGroupType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeIDS"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNICThroughput"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNICThroughputThreshold"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappMessagingLAGThreshold"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappServiceName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterQueueName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterQueueSize"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterQueueSizeThreshold"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSNATIPAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceDownReason"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceRouterId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSyncIssueReason"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterToGMPath"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationInfoGroup9.setStatus("current")


# Notification objects

vmwNsxTManagerHealthManagerCPUUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 1)
)
vmwNsxTManagerHealthManagerCPUUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerCPUUsageHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerCPUUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 2)
)
vmwNsxTManagerHealthManagerCPUUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerCPUUsageHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerCPUUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 3)
)
vmwNsxTManagerHealthManagerCPUUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerCPUUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerCPUUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 4)
)
vmwNsxTManagerHealthManagerCPUUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerCPUUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 5)
)
vmwNsxTManagerHealthManagerMemoryUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerMemoryUsageHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerMemoryUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 6)
)
vmwNsxTManagerHealthManagerMemoryUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerMemoryUsageHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerMemoryUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 7)
)
vmwNsxTManagerHealthManagerMemoryUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerMemoryUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerMemoryUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 8)
)
vmwNsxTManagerHealthManagerMemoryUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerMemoryUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 9)
)
vmwNsxTManagerHealthManagerDiskUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerDiskUsageHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerDiskUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 10)
)
vmwNsxTManagerHealthManagerDiskUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerDiskUsageHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerDiskUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 11)
)
vmwNsxTManagerHealthManagerDiskUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerDiskUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerDiskUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 12)
)
vmwNsxTManagerHealthManagerDiskUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerDiskUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerConfigDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 13)
)
vmwNsxTManagerHealthManagerConfigDiskUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerConfigDiskUsageHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerConfigDiskUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 14)
)
vmwNsxTManagerHealthManagerConfigDiskUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerConfigDiskUsageHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerConfigDiskUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 15)
)
vmwNsxTManagerHealthManagerConfigDiskUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerConfigDiskUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthManagerConfigDiskUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 16)
)
vmwNsxTManagerHealthManagerConfigDiskUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthManagerConfigDiskUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthDuplicateIPAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 17)
)
vmwNsxTManagerHealthDuplicateIPAddress.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDuplicateIPAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthDuplicateIPAddress.setStatus(
        "current"
    )

vmwNsxTManagerHealthDuplicateIPAddressClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 18)
)
vmwNsxTManagerHealthDuplicateIPAddressClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDuplicateIPAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthDuplicateIPAddressClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthOperationsDbDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 19)
)
vmwNsxTManagerHealthOperationsDbDiskUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthOperationsDbDiskUsageHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthOperationsDbDiskUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 20)
)
vmwNsxTManagerHealthOperationsDbDiskUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthOperationsDbDiskUsageHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthOperationsDbDiskUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 21)
)
vmwNsxTManagerHealthOperationsDbDiskUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthOperationsDbDiskUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTManagerHealthOperationsDbDiskUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 22)
)
vmwNsxTManagerHealthOperationsDbDiskUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthOperationsDbDiskUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTManagerHealthStorageError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 23)
)
vmwNsxTManagerHealthStorageError.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthStorageError.setStatus(
        "current"
    )

vmwNsxTManagerHealthStorageErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 1, 0, 24)
)
vmwNsxTManagerHealthStorageErrorClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"))
)
if mibBuilder.loadTexts:
    vmwNsxTManagerHealthStorageErrorClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeCPUUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 1)
)
vmwNsxTEdgeHealthEdgeCPUUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeCPUUsageHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeCPUUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 2)
)
vmwNsxTEdgeHealthEdgeCPUUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeCPUUsageHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeCPUUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 3)
)
vmwNsxTEdgeHealthEdgeCPUUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeCPUUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeCPUUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 4)
)
vmwNsxTEdgeHealthEdgeCPUUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeCPUUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 5)
)
vmwNsxTEdgeHealthEdgeMemoryUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeMemoryUsageHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeMemoryUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 6)
)
vmwNsxTEdgeHealthEdgeMemoryUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeMemoryUsageHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeMemoryUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 7)
)
vmwNsxTEdgeHealthEdgeMemoryUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeMemoryUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeMemoryUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 8)
)
vmwNsxTEdgeHealthEdgeMemoryUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeMemoryUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 9)
)
vmwNsxTEdgeHealthEdgeDiskUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDiskUsageHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDiskUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 10)
)
vmwNsxTEdgeHealthEdgeDiskUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDiskUsageHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDiskUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 11)
)
vmwNsxTEdgeHealthEdgeDiskUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDiskUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDiskUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 12)
)
vmwNsxTEdgeHealthEdgeDiskUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDiskUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathCPUHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 17)
)
vmwNsxTEdgeHealthEdgeDatapathCPUHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDatapathResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathCPUHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathCPUHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 18)
)
vmwNsxTEdgeHealthEdgeDatapathCPUHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathCPUHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathCPUVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 19)
)
vmwNsxTEdgeHealthEdgeDatapathCPUVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDatapathResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathCPUVeryHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathCPUVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 20)
)
vmwNsxTEdgeHealthEdgeDatapathCPUVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathCPUVeryHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathConfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 21)
)
vmwNsxTEdgeHealthEdgeDatapathConfigurationFailure.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathConfigurationFailure.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathConfigurationFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 22)
)
vmwNsxTEdgeHealthEdgeDatapathConfigurationFailureClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathConfigurationFailureClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathCryptodrvDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 23)
)
vmwNsxTEdgeHealthEdgeDatapathCryptodrvDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeCryptoDrvName"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathCryptodrvDown.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathCryptodrvDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 24)
)
vmwNsxTEdgeHealthEdgeDatapathCryptodrvDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeCryptoDrvName"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathCryptodrvDownClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathMempoolHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 25)
)
vmwNsxTEdgeHealthEdgeDatapathMempoolHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMempoolName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathMempoolHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathMempoolHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 26)
)
vmwNsxTEdgeHealthEdgeDatapathMempoolHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMempoolName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathMempoolHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 27)
)
vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDatapathResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 28)
)
vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeNICLinkStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 29)
)
vmwNsxTEdgeHealthEdgeNICLinkStatusDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNICName"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeNICLinkStatusDown.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeNICLinkStatusDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 30)
)
vmwNsxTEdgeHealthEdgeNICLinkStatusDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNICName"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeNICLinkStatusDownClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeNICOutOfReceiveBuffer = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 31)
)
vmwNsxTEdgeHealthEdgeNICOutOfReceiveBuffer.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNICName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRxRingBufferOverflowPercentage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRxMisses"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRxProcessed"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeNICOutOfReceiveBuffer.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeNICOutOfReceiveBufferClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 32)
)
vmwNsxTEdgeHealthEdgeNICOutOfReceiveBufferClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNICName"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeNICOutOfReceiveBufferClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeNICOutOfTransmitBuffer = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 33)
)
vmwNsxTEdgeHealthEdgeNICOutOfTransmitBuffer.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNICName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTxRingBufferOverflowPercentage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTxMisses"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTxProcessed"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeNICOutOfTransmitBuffer.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeNICOutOfTransmitBufferClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 34)
)
vmwNsxTEdgeHealthEdgeNICOutOfTransmitBufferClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNICName"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeNICOutOfTransmitBufferClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthStorageError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 37)
)
vmwNsxTEdgeHealthStorageError.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthStorageError.setStatus(
        "current"
    )

vmwNsxTEdgeHealthStorageErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 38)
)
vmwNsxTEdgeHealthStorageErrorClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthStorageErrorClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthDatapathThreadDeadlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 45)
)
vmwNsxTEdgeHealthDatapathThreadDeadlocked.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeThreadName"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthDatapathThreadDeadlocked.setStatus(
        "current"
    )

vmwNsxTEdgeHealthDatapathThreadDeadlockedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 46)
)
vmwNsxTEdgeHealthDatapathThreadDeadlockedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeThreadName"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthDatapathThreadDeadlockedClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathNICThroughputHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 49)
)
vmwNsxTEdgeHealthEdgeDatapathNICThroughputHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNICName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNICThroughput"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNICThroughputThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathNICThroughputHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathNICThroughputHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 50)
)
vmwNsxTEdgeHealthEdgeDatapathNICThroughputHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNICName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNICThroughput"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNICThroughputThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathNICThroughputHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathNICThroughputVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 51)
)
vmwNsxTEdgeHealthEdgeDatapathNICThroughputVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNICName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNICThroughput"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNICThroughputThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathNICThroughputVeryHigh.setStatus(
        "current"
    )

vmwNsxTEdgeHealthEdgeDatapathNICThroughputVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 52)
)
vmwNsxTEdgeHealthEdgeDatapathNICThroughputVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNICName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNICThroughput"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNICThroughputThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthEdgeDatapathNICThroughputVeryHighClear.setStatus(
        "current"
    )

vmwNsxTEdgeHealthFailureDomainDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 53)
)
vmwNsxTEdgeHealthFailureDomainDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthFailureDomainDown.setStatus(
        "current"
    )

vmwNsxTEdgeHealthFailureDomainDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 2, 0, 54)
)
vmwNsxTEdgeHealthFailureDomainDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeHealthFailureDomainDownClear.setStatus(
        "current"
    )

vmwNsxTCertificatesCertificateExpirationApproaching = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3, 0, 1)
)
vmwNsxTCertificatesCertificateExpirationApproaching.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterAPICollectionPath"))
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesCertificateExpirationApproaching.setStatus(
        "current"
    )

vmwNsxTCertificatesCertificateExpirationApproachingClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3, 0, 2)
)
vmwNsxTCertificatesCertificateExpirationApproachingClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesCertificateExpirationApproachingClear.setStatus(
        "current"
    )

vmwNsxTCertificatesCertificateExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3, 0, 3)
)
vmwNsxTCertificatesCertificateExpired.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterAPICollectionPath"))
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesCertificateExpired.setStatus(
        "current"
    )

vmwNsxTCertificatesCertificateExpiredClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3, 0, 4)
)
vmwNsxTCertificatesCertificateExpiredClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesCertificateExpiredClear.setStatus(
        "current"
    )

vmwNsxTCertificatesCertificateIsAboutToExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3, 0, 5)
)
vmwNsxTCertificatesCertificateIsAboutToExpire.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterAPICollectionPath"))
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesCertificateIsAboutToExpire.setStatus(
        "current"
    )

vmwNsxTCertificatesCertificateIsAboutToExpireClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3, 0, 6)
)
vmwNsxTCertificatesCertificateIsAboutToExpireClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesCertificateIsAboutToExpireClear.setStatus(
        "current"
    )

vmwNsxTCertificatesCABundleUpdateRecommended = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3, 0, 7)
)
vmwNsxTCertificatesCABundleUpdateRecommended.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCABundleAgeThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesCABundleUpdateRecommended.setStatus(
        "current"
    )

vmwNsxTCertificatesCABundleUpdateRecommendedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3, 0, 8)
)
vmwNsxTCertificatesCABundleUpdateRecommendedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesCABundleUpdateRecommendedClear.setStatus(
        "current"
    )

vmwNsxTCertificatesCABundleUpdateSuggested = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3, 0, 9)
)
vmwNsxTCertificatesCABundleUpdateSuggested.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCABundleAgeThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesCABundleUpdateSuggested.setStatus(
        "current"
    )

vmwNsxTCertificatesCABundleUpdateSuggestedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 3, 0, 10)
)
vmwNsxTCertificatesCABundleUpdateSuggestedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCertificatesCABundleUpdateSuggestedClear.setStatus(
        "current"
    )

vmwNsxTPasswordManagementPasswordExpirationApproaching = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 4, 0, 1)
)
vmwNsxTPasswordManagementPasswordExpirationApproaching.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterUsername"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPasswordExpirationDays"))
)
if mibBuilder.loadTexts:
    vmwNsxTPasswordManagementPasswordExpirationApproaching.setStatus(
        "current"
    )

vmwNsxTPasswordManagementPasswordExpirationApproachingClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 4, 0, 2)
)
vmwNsxTPasswordManagementPasswordExpirationApproachingClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterUsername"))
)
if mibBuilder.loadTexts:
    vmwNsxTPasswordManagementPasswordExpirationApproachingClear.setStatus(
        "current"
    )

vmwNsxTPasswordManagementPasswordExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 4, 0, 3)
)
vmwNsxTPasswordManagementPasswordExpired.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterUsername"))
)
if mibBuilder.loadTexts:
    vmwNsxTPasswordManagementPasswordExpired.setStatus(
        "current"
    )

vmwNsxTPasswordManagementPasswordExpiredClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 4, 0, 4)
)
vmwNsxTPasswordManagementPasswordExpiredClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterUsername"))
)
if mibBuilder.loadTexts:
    vmwNsxTPasswordManagementPasswordExpiredClear.setStatus(
        "current"
    )

vmwNsxTPasswordManagementPasswordIsAboutToExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 4, 0, 5)
)
vmwNsxTPasswordManagementPasswordIsAboutToExpire.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterUsername"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPasswordExpirationDays"))
)
if mibBuilder.loadTexts:
    vmwNsxTPasswordManagementPasswordIsAboutToExpire.setStatus(
        "current"
    )

vmwNsxTPasswordManagementPasswordIsAboutToExpireClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 4, 0, 6)
)
vmwNsxTPasswordManagementPasswordIsAboutToExpireClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterUsername"))
)
if mibBuilder.loadTexts:
    vmwNsxTPasswordManagementPasswordIsAboutToExpireClear.setStatus(
        "current"
    )

vmwNsxTLicensesLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 5, 0, 1)
)
vmwNsxTLicensesLicenseExpired.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLicenseEditionType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDisplayedLicenseKey"))
)
if mibBuilder.loadTexts:
    vmwNsxTLicensesLicenseExpired.setStatus(
        "current"
    )

vmwNsxTLicensesLicenseExpiredClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 5, 0, 2)
)
vmwNsxTLicensesLicenseExpiredClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLicenseEditionType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDisplayedLicenseKey"))
)
if mibBuilder.loadTexts:
    vmwNsxTLicensesLicenseExpiredClear.setStatus(
        "current"
    )

vmwNsxTLicensesLicenseIsAboutToExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 5, 0, 3)
)
vmwNsxTLicensesLicenseIsAboutToExpire.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLicenseEditionType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDisplayedLicenseKey"))
)
if mibBuilder.loadTexts:
    vmwNsxTLicensesLicenseIsAboutToExpire.setStatus(
        "current"
    )

vmwNsxTLicensesLicenseIsAboutToExpireClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 5, 0, 4)
)
vmwNsxTLicensesLicenseIsAboutToExpireClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLicenseEditionType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDisplayedLicenseKey"))
)
if mibBuilder.loadTexts:
    vmwNsxTLicensesLicenseIsAboutToExpireClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthCPUUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 41)
)
vmwNsxTIntelligenceHealthCPUUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthCPUUsageHigh.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthCPUUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 42)
)
vmwNsxTIntelligenceHealthCPUUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthCPUUsageHighClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthCPUUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 43)
)
vmwNsxTIntelligenceHealthCPUUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthCPUUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthCPUUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 44)
)
vmwNsxTIntelligenceHealthCPUUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthCPUUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthDataDiskPartitionUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 45)
)
vmwNsxTIntelligenceHealthDataDiskPartitionUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthDataDiskPartitionUsageHigh.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthDataDiskPartitionUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 46)
)
vmwNsxTIntelligenceHealthDataDiskPartitionUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthDataDiskPartitionUsageHighClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 47)
)
vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 48)
)
vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 49)
)
vmwNsxTIntelligenceHealthDiskUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthDiskUsageHigh.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthDiskUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 50)
)
vmwNsxTIntelligenceHealthDiskUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthDiskUsageHighClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthDiskUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 51)
)
vmwNsxTIntelligenceHealthDiskUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthDiskUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthDiskUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 52)
)
vmwNsxTIntelligenceHealthDiskUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthDiskUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 53)
)
vmwNsxTIntelligenceHealthMemoryUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthMemoryUsageHigh.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthMemoryUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 54)
)
vmwNsxTIntelligenceHealthMemoryUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthMemoryUsageHighClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthMemoryUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 55)
)
vmwNsxTIntelligenceHealthMemoryUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthMemoryUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthMemoryUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 56)
)
vmwNsxTIntelligenceHealthMemoryUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthMemoryUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthNodeStatusDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 57)
)
vmwNsxTIntelligenceHealthNodeStatusDegraded.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthNodeStatusDegraded.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthNodeStatusDegradedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 58)
)
vmwNsxTIntelligenceHealthNodeStatusDegradedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthNodeStatusDegradedClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthStorageLatencyHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 63)
)
vmwNsxTIntelligenceHealthStorageLatencyHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthStorageLatencyHigh.setStatus(
        "current"
    )

vmwNsxTIntelligenceHealthStorageLatencyHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 6, 0, 64)
)
vmwNsxTIntelligenceHealthStorageLatencyHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDiskPartitionName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntelligenceNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceHealthStorageLatencyHighClear.setStatus(
        "current"
    )

vmwNsxTInfrastructureCommunicationEdgeTunnelsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 7, 0, 17)
)
vmwNsxTInfrastructureCommunicationEdgeTunnelsDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureCommunicationEdgeTunnelsDown.setStatus(
        "current"
    )

vmwNsxTInfrastructureCommunicationEdgeTunnelsDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 7, 0, 18)
)
vmwNsxTInfrastructureCommunicationEdgeTunnelsDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureCommunicationEdgeTunnelsDownClear.setStatus(
        "current"
    )

vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 9, 0, 7)
)
vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnected.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnected.setStatus(
        "current"
    )

vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnectedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 9, 0, 8)
)
vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnectedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnectedClear.setStatus(
        "current"
    )

vmwNsxTCniHealthHyperbusManagerConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 10, 0, 3)
)
vmwNsxTCniHealthHyperbusManagerConnectionDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCniHealthHyperbusManagerConnectionDown.setStatus(
        "current"
    )

vmwNsxTCniHealthHyperbusManagerConnectionDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 10, 0, 4)
)
vmwNsxTCniHealthHyperbusManagerConnectionDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCniHealthHyperbusManagerConnectionDownClear.setStatus(
        "current"
    )

vmwNsxTNCPHealthNCPPluginDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 11, 0, 3)
)
vmwNsxTNCPHealthNCPPluginDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTNCPHealthNCPPluginDown.setStatus(
        "current"
    )

vmwNsxTNCPHealthNCPPluginDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 11, 0, 4)
)
vmwNsxTNCPHealthNCPPluginDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTNCPHealthNCPPluginDownClear.setStatus(
        "current"
    )

vmwNsxTNodeAgentsHealthNodeAgentsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 12, 0, 3)
)
vmwNsxTNodeAgentsHealthNodeAgentsDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTNodeAgentsHealthNodeAgentsDown.setStatus(
        "current"
    )

vmwNsxTNodeAgentsHealthNodeAgentsDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 12, 0, 4)
)
vmwNsxTNodeAgentsHealthNodeAgentsDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTNodeAgentsHealthNodeAgentsDownClear.setStatus(
        "current"
    )

vmwNsxTEndpointProtectionEAMStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 13, 0, 1)
)
vmwNsxTEndpointProtectionEAMStatusDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEndpointProtectionEAMStatusDown.setStatus(
        "current"
    )

vmwNsxTEndpointProtectionEAMStatusDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 13, 0, 2)
)
vmwNsxTEndpointProtectionEAMStatusDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEndpointProtectionEAMStatusDownClear.setStatus(
        "current"
    )

vmwNsxTEndpointProtectionPartnerChannelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 13, 0, 3)
)
vmwNsxTEndpointProtectionPartnerChannelDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEndpointProtectionPartnerChannelDown.setStatus(
        "current"
    )

vmwNsxTEndpointProtectionPartnerChannelDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 13, 0, 4)
)
vmwNsxTEndpointProtectionPartnerChannelDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEndpointProtectionPartnerChannelDownClear.setStatus(
        "current"
    )

vmwNsxTVPNIPsecPolicyBasedSessionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 7)
)
vmwNsxTVPNIPsecPolicyBasedSessionDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSessionDownReason"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNIPsecPolicyBasedSessionDown.setStatus(
        "current"
    )

vmwNsxTVPNIPsecPolicyBasedSessionDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 8)
)
vmwNsxTVPNIPsecPolicyBasedSessionDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNIPsecPolicyBasedSessionDownClear.setStatus(
        "current"
    )

vmwNsxTVPNIPsecPolicyBasedTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 9)
)
vmwNsxTVPNIPsecPolicyBasedTunnelDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNIPsecPolicyBasedTunnelDown.setStatus(
        "current"
    )

vmwNsxTVPNIPsecPolicyBasedTunnelDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 10)
)
vmwNsxTVPNIPsecPolicyBasedTunnelDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNIPsecPolicyBasedTunnelDownClear.setStatus(
        "current"
    )

vmwNsxTVPNIPsecRouteBasedSessionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 11)
)
vmwNsxTVPNIPsecRouteBasedSessionDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSessionDownReason"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNIPsecRouteBasedSessionDown.setStatus(
        "current"
    )

vmwNsxTVPNIPsecRouteBasedSessionDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 12)
)
vmwNsxTVPNIPsecRouteBasedSessionDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNIPsecRouteBasedSessionDownClear.setStatus(
        "current"
    )

vmwNsxTVPNIPsecRouteBasedTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 13)
)
vmwNsxTVPNIPsecRouteBasedTunnelDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTunnelDownReason"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNIPsecRouteBasedTunnelDown.setStatus(
        "current"
    )

vmwNsxTVPNIPsecRouteBasedTunnelDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 14)
)
vmwNsxTVPNIPsecRouteBasedTunnelDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNIPsecRouteBasedTunnelDownClear.setStatus(
        "current"
    )

vmwNsxTVPNL2VpnSessionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 15)
)
vmwNsxTVPNL2VpnSessionDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNL2VpnSessionDown.setStatus(
        "current"
    )

vmwNsxTVPNL2VpnSessionDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 16)
)
vmwNsxTVPNL2VpnSessionDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNL2VpnSessionDownClear.setStatus(
        "current"
    )

vmwNsxTVPNIPsecServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 17)
)
vmwNsxTVPNIPsecServiceDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceDownReason"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNIPsecServiceDown.setStatus(
        "current"
    )

vmwNsxTVPNIPsecServiceDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 15, 0, 18)
)
vmwNsxTVPNIPsecServiceDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTVPNIPsecServiceDownClear.setStatus(
        "current"
    )

vmwNsxTAlarmManagementAlarmServiceOverloaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 16, 0, 1)
)
vmwNsxTAlarmManagementAlarmServiceOverloaded.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTAlarmManagementAlarmServiceOverloaded.setStatus(
        "current"
    )

vmwNsxTAlarmManagementAlarmServiceOverloadedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 16, 0, 2)
)
vmwNsxTAlarmManagementAlarmServiceOverloadedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTAlarmManagementAlarmServiceOverloadedClear.setStatus(
        "current"
    )

vmwNsxTAlarmManagementHeavyVolumeOfAlarms = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 16, 0, 3)
)
vmwNsxTAlarmManagementHeavyVolumeOfAlarms.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventId"))
)
if mibBuilder.loadTexts:
    vmwNsxTAlarmManagementHeavyVolumeOfAlarms.setStatus(
        "current"
    )

vmwNsxTAlarmManagementHeavyVolumeOfAlarmsClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 16, 0, 4)
)
vmwNsxTAlarmManagementHeavyVolumeOfAlarmsClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventId"))
)
if mibBuilder.loadTexts:
    vmwNsxTAlarmManagementHeavyVolumeOfAlarmsClear.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBCPUVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 1)
)
vmwNsxTLoadBalancerLBCPUVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBCPUVeryHigh.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBCPUVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 2)
)
vmwNsxTLoadBalancerLBCPUVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBCPUVeryHighClear.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBEdgeCapacityInUseHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 3)
)
vmwNsxTLoadBalancerLBEdgeCapacityInUseHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBEdgeCapacityInUseHigh.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBEdgeCapacityInUseHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 4)
)
vmwNsxTLoadBalancerLBEdgeCapacityInUseHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBEdgeCapacityInUseHighClear.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 5)
)
vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHigh.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 6)
)
vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHighClear.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 7)
)
vmwNsxTLoadBalancerLBStatusDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBStatusDown.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBStatusDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 8)
)
vmwNsxTLoadBalancerLBStatusDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBStatusDownClear.setStatus(
        "current"
    )

vmwNsxTLoadBalancerPoolStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 9)
)
vmwNsxTLoadBalancerPoolStatusDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerPoolStatusDown.setStatus(
        "current"
    )

vmwNsxTLoadBalancerPoolStatusDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 10)
)
vmwNsxTLoadBalancerPoolStatusDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerPoolStatusDownClear.setStatus(
        "current"
    )

vmwNsxTLoadBalancerVirtualServerStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 11)
)
vmwNsxTLoadBalancerVirtualServerStatusDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerVirtualServerStatusDown.setStatus(
        "current"
    )

vmwNsxTLoadBalancerVirtualServerStatusDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 12)
)
vmwNsxTLoadBalancerVirtualServerStatusDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerVirtualServerStatusDownClear.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBStatusDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 15)
)
vmwNsxTLoadBalancerLBStatusDegraded.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBStatusDegraded.setStatus(
        "current"
    )

vmwNsxTLoadBalancerLBStatusDegradedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 16)
)
vmwNsxTLoadBalancerLBStatusDegradedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerLBStatusDegradedClear.setStatus(
        "current"
    )

vmwNsxTLoadBalancerDLBStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 17)
)
vmwNsxTLoadBalancerDLBStatusDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerDLBStatusDown.setStatus(
        "current"
    )

vmwNsxTLoadBalancerDLBStatusDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 18)
)
vmwNsxTLoadBalancerDLBStatusDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerDLBStatusDownClear.setStatus(
        "current"
    )

vmwNsxTLoadBalancerConfigurationNotRealizedDueToLowMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 19)
)
vmwNsxTLoadBalancerConfigurationNotRealizedDueToLowMemory.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerConfigurationNotRealizedDueToLowMemory.setStatus(
        "current"
    )

vmwNsxTLoadBalancerConfigurationNotRealizedDueToLowMemoryClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 17, 0, 20)
)
vmwNsxTLoadBalancerConfigurationNotRealizedDueToLowMemoryClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeId"))
)
if mibBuilder.loadTexts:
    vmwNsxTLoadBalancerConfigurationNotRealizedDueToLowMemoryClear.setStatus(
        "current"
    )

vmwNsxTTransportNodeHealthNVDSUplinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 18, 0, 3)
)
vmwNsxTTransportNodeHealthNVDSUplinkDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTTransportNodeHealthNVDSUplinkDown.setStatus(
        "current"
    )

vmwNsxTTransportNodeHealthNVDSUplinkDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 18, 0, 4)
)
vmwNsxTTransportNodeHealthNVDSUplinkDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTTransportNodeHealthNVDSUplinkDownClear.setStatus(
        "current"
    )

vmwNsxTTransportNodeHealthLAGMemberDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 18, 0, 5)
)
vmwNsxTTransportNodeHealthLAGMemberDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTTransportNodeHealthLAGMemberDown.setStatus(
        "current"
    )

vmwNsxTTransportNodeHealthLAGMemberDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 18, 0, 6)
)
vmwNsxTTransportNodeHealthLAGMemberDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTTransportNodeHealthLAGMemberDownClear.setStatus(
        "current"
    )

vmwNsxTTransportNodeHealthTransportNodeUplinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 18, 0, 7)
)
vmwNsxTTransportNodeHealthTransportNodeUplinkDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTTransportNodeHealthTransportNodeUplinkDown.setStatus(
        "current"
    )

vmwNsxTTransportNodeHealthTransportNodeUplinkDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 18, 0, 8)
)
vmwNsxTTransportNodeHealthTransportNodeUplinkDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTTransportNodeHealthTransportNodeUplinkDownClear.setStatus(
        "current"
    )

vmwNsxTInfrastructureServiceEdgeServiceStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 19, 0, 1)
)
vmwNsxTInfrastructureServiceEdgeServiceStatusChanged.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeServiceName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPreviousServiceState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCurrentServiceState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceDownReason"))
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureServiceEdgeServiceStatusChanged.setStatus(
        "current"
    )

vmwNsxTInfrastructureServiceEdgeServiceStatusChangedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 19, 0, 2)
)
vmwNsxTInfrastructureServiceEdgeServiceStatusChangedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeServiceName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPreviousServiceState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCurrentServiceState"))
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureServiceEdgeServiceStatusChangedClear.setStatus(
        "current"
    )

vmwNsxTInfrastructureServiceEdgeServiceStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 19, 0, 3)
)
vmwNsxTInfrastructureServiceEdgeServiceStatusDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeServiceName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceDownReason"))
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureServiceEdgeServiceStatusDown.setStatus(
        "current"
    )

vmwNsxTInfrastructureServiceEdgeServiceStatusDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 19, 0, 4)
)
vmwNsxTInfrastructureServiceEdgeServiceStatusDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeServiceName"))
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureServiceEdgeServiceStatusDownClear.setStatus(
        "current"
    )

vmwNsxTInfrastructureServiceServiceStatusUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 19, 0, 7)
)
vmwNsxTInfrastructureServiceServiceStatusUnknown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceName"))
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureServiceServiceStatusUnknown.setStatus(
        "current"
    )

vmwNsxTInfrastructureServiceServiceStatusUnknownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 19, 0, 8)
)
vmwNsxTInfrastructureServiceServiceStatusUnknownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceName"))
)
if mibBuilder.loadTexts:
    vmwNsxTInfrastructureServiceServiceStatusUnknownClear.setStatus(
        "current"
    )

vmwNsxTDHCPPoolLeaseAllocationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 20, 0, 1)
)
vmwNsxTDHCPPoolLeaseAllocationFailed.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDHCPServerId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDHCPPoolLeaseAllocationFailed.setStatus(
        "current"
    )

vmwNsxTDHCPPoolLeaseAllocationFailedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 20, 0, 2)
)
vmwNsxTDHCPPoolLeaseAllocationFailedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDHCPServerId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDHCPPoolLeaseAllocationFailedClear.setStatus(
        "current"
    )

vmwNsxTDHCPPoolOverloaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 20, 0, 3)
)
vmwNsxTDHCPPoolOverloaded.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDHCPServerId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDHCPPoolUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDHCPPoolOverloaded.setStatus(
        "current"
    )

vmwNsxTDHCPPoolOverloadedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 20, 0, 4)
)
vmwNsxTDHCPPoolOverloadedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDHCPServerId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDHCPPoolOverloadedClear.setStatus(
        "current"
    )

vmwNsxTHighAvailabilityTier0GatewayFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 21, 0, 9)
)
vmwNsxTHighAvailabilityTier0GatewayFailover.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPreviousGatewayState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCurrentGatewayState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceRouterId"))
)
if mibBuilder.loadTexts:
    vmwNsxTHighAvailabilityTier0GatewayFailover.setStatus(
        "current"
    )

vmwNsxTHighAvailabilityTier0GatewayFailoverClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 21, 0, 10)
)
vmwNsxTHighAvailabilityTier0GatewayFailoverClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTHighAvailabilityTier0GatewayFailoverClear.setStatus(
        "current"
    )

vmwNsxTHighAvailabilityTier1GatewayFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 21, 0, 11)
)
vmwNsxTHighAvailabilityTier1GatewayFailover.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPreviousGatewayState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCurrentGatewayState"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceRouterId"))
)
if mibBuilder.loadTexts:
    vmwNsxTHighAvailabilityTier1GatewayFailover.setStatus(
        "current"
    )

vmwNsxTHighAvailabilityTier1GatewayFailoverClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 21, 0, 12)
)
vmwNsxTHighAvailabilityTier1GatewayFailoverClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTHighAvailabilityTier1GatewayFailoverClear.setStatus(
        "current"
    )

vmwNsxTCapacityMaximumCapacity = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 22, 0, 1)
)
vmwNsxTCapacityMaximumCapacity.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityDisplayName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityUsageCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMaxSupportedCapacityCount"))
)
if mibBuilder.loadTexts:
    vmwNsxTCapacityMaximumCapacity.setStatus(
        "current"
    )

vmwNsxTCapacityMaximumCapacityClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 22, 0, 2)
)
vmwNsxTCapacityMaximumCapacityClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityDisplayName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityUsageCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMaxSupportedCapacityCount"))
)
if mibBuilder.loadTexts:
    vmwNsxTCapacityMaximumCapacityClear.setStatus(
        "current"
    )

vmwNsxTCapacityMaximumCapacityThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 22, 0, 3)
)
vmwNsxTCapacityMaximumCapacityThreshold.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityDisplayName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityUsageCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMaxCapacityThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTCapacityMaximumCapacityThreshold.setStatus(
        "current"
    )

vmwNsxTCapacityMaximumCapacityThresholdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 22, 0, 4)
)
vmwNsxTCapacityMaximumCapacityThresholdClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityDisplayName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityUsageCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMaxCapacityThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTCapacityMaximumCapacityThresholdClear.setStatus(
        "current"
    )

vmwNsxTCapacityMinimumCapacityThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 22, 0, 5)
)
vmwNsxTCapacityMinimumCapacityThreshold.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityDisplayName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityUsageCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMinCapacityThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTCapacityMinimumCapacityThreshold.setStatus(
        "current"
    )

vmwNsxTCapacityMinimumCapacityThresholdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 22, 0, 6)
)
vmwNsxTCapacityMinimumCapacityThresholdClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityDisplayName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCapacityUsageCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMinCapacityThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTCapacityMinimumCapacityThresholdClear.setStatus(
        "current"
    )

vmwNsxTAuditLogHealthAuditLogFileUpdateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 24, 0, 1)
)
vmwNsxTAuditLogHealthAuditLogFileUpdateError.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTAuditLogHealthAuditLogFileUpdateError.setStatus(
        "current"
    )

vmwNsxTAuditLogHealthAuditLogFileUpdateErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 24, 0, 2)
)
vmwNsxTAuditLogHealthAuditLogFileUpdateErrorClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTAuditLogHealthAuditLogFileUpdateErrorClear.setStatus(
        "current"
    )

vmwNsxTAuditLogHealthRemoteLoggingServerError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 24, 0, 3)
)
vmwNsxTAuditLogHealthRemoteLoggingServerError.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterHostnameOrIPAddressWithPort"))
)
if mibBuilder.loadTexts:
    vmwNsxTAuditLogHealthRemoteLoggingServerError.setStatus(
        "current"
    )

vmwNsxTAuditLogHealthRemoteLoggingServerErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 24, 0, 4)
)
vmwNsxTAuditLogHealthRemoteLoggingServerErrorClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterHostnameOrIPAddressWithPort"))
)
if mibBuilder.loadTexts:
    vmwNsxTAuditLogHealthRemoteLoggingServerErrorClear.setStatus(
        "current"
    )

vmwNsxTRoutingBGPDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 1)
)
vmwNsxTRoutingBGPDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterBGPNeighborIP"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFailureReason"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSrId"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingBGPDown.setStatus(
        "current"
    )

vmwNsxTRoutingBGPDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 2)
)
vmwNsxTRoutingBGPDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterBGPNeighborIP"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingBGPDownClear.setStatus(
        "current"
    )

vmwNsxTRoutingStaticRoutingRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 5)
)
vmwNsxTRoutingStaticRoutingRemoved.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterStaticAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSrId"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingStaticRoutingRemoved.setStatus(
        "current"
    )

vmwNsxTRoutingStaticRoutingRemovedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 6)
)
vmwNsxTRoutingStaticRoutingRemovedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterStaticAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingStaticRoutingRemovedClear.setStatus(
        "current"
    )

vmwNsxTRoutingBFDDownOnExternalInterface = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 7)
)
vmwNsxTRoutingBFDDownOnExternalInterface.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPeerAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSrId"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingBFDDownOnExternalInterface.setStatus(
        "current"
    )

vmwNsxTRoutingBFDDownOnExternalInterfaceClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 8)
)
vmwNsxTRoutingBFDDownOnExternalInterfaceClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPeerAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingBFDDownOnExternalInterfaceClear.setStatus(
        "current"
    )

vmwNsxTRoutingRoutingDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 9)
)
vmwNsxTRoutingRoutingDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingRoutingDown.setStatus(
        "current"
    )

vmwNsxTRoutingRoutingDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 10)
)
vmwNsxTRoutingRoutingDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingRoutingDownClear.setStatus(
        "current"
    )

vmwNsxTRoutingOSPFNeighborWentDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 11)
)
vmwNsxTRoutingOSPFNeighborWentDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPeerAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingOSPFNeighborWentDown.setStatus(
        "current"
    )

vmwNsxTRoutingOSPFNeighborWentDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 12)
)
vmwNsxTRoutingOSPFNeighborWentDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterPeerAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingOSPFNeighborWentDownClear.setStatus(
        "current"
    )

vmwNsxTRoutingProxyARPNotConfiguredForServiceIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 13)
)
vmwNsxTRoutingProxyARPNotConfiguredForServiceIP.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterServiceIP"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrportId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrId"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingProxyARPNotConfiguredForServiceIP.setStatus(
        "current"
    )

vmwNsxTRoutingProxyARPNotConfiguredForServiceIPClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 28, 0, 14)
)
vmwNsxTRoutingProxyARPNotConfiguredForServiceIPClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrportId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLrId"))
)
if mibBuilder.loadTexts:
    vmwNsxTRoutingProxyARPNotConfiguredForServiceIPClear.setStatus(
        "current"
    )

vmwNsxTDNSForwarderDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 30, 0, 1)
)
vmwNsxTDNSForwarderDisabled.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDNSForwarderDisabled.setStatus(
        "current"
    )

vmwNsxTDNSForwarderDisabledClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 30, 0, 2)
)
vmwNsxTDNSForwarderDisabledClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDNSForwarderDisabledClear.setStatus(
        "current"
    )

vmwNsxTDNSForwarderDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 30, 0, 3)
)
vmwNsxTDNSForwarderDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDNSForwarderDown.setStatus(
        "current"
    )

vmwNsxTDNSForwarderDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 30, 0, 4)
)
vmwNsxTDNSForwarderDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDNSForwarderDownClear.setStatus(
        "current"
    )

vmwNsxTDNSForwarderUpstreamServerTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 30, 0, 5)
)
vmwNsxTDNSForwarderUpstreamServerTimeout.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntentPath"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDNSId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDNSUpstreamIP"))
)
if mibBuilder.loadTexts:
    vmwNsxTDNSForwarderUpstreamServerTimeout.setStatus(
        "current"
    )

vmwNsxTDNSForwarderUpstreamServerTimeoutClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 30, 0, 6)
)
vmwNsxTDNSForwarderUpstreamServerTimeoutClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntentPath"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDNSId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDNSUpstreamIP"))
)
if mibBuilder.loadTexts:
    vmwNsxTDNSForwarderUpstreamServerTimeoutClear.setStatus(
        "current"
    )

vmwNsxTDistributedFirewallDFWCPUUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 31, 0, 1)
)
vmwNsxTDistributedFirewallDFWCPUUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedFirewallDFWCPUUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTDistributedFirewallDFWCPUUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 31, 0, 2)
)
vmwNsxTDistributedFirewallDFWCPUUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedFirewallDFWCPUUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTDistributedFirewallDFWMemoryUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 31, 0, 3)
)
vmwNsxTDistributedFirewallDFWMemoryUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterHeapType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedFirewallDFWMemoryUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTDistributedFirewallDFWMemoryUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 31, 0, 4)
)
vmwNsxTDistributedFirewallDFWMemoryUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterHeapType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedFirewallDFWMemoryUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTDistributedFirewallDFWSessionCountHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 31, 0, 5)
)
vmwNsxTDistributedFirewallDFWSessionCountHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedFirewallDFWSessionCountHigh.setStatus(
        "current"
    )

vmwNsxTDistributedFirewallDFWSessionCountHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 31, 0, 6)
)
vmwNsxTDistributedFirewallDFWSessionCountHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedFirewallDFWSessionCountHighClear.setStatus(
        "current"
    )

vmwNsxTDistributedFirewallDFWVmotionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 31, 0, 7)
)
vmwNsxTDistributedFirewallDFWVmotionFailure.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeName"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedFirewallDFWVmotionFailure.setStatus(
        "current"
    )

vmwNsxTDistributedFirewallDFWVmotionFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 31, 0, 8)
)
vmwNsxTDistributedFirewallDFWVmotionFailureClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeName"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedFirewallDFWVmotionFailureClear.setStatus(
        "current"
    )

vmwNsxTFederationRtepBGPDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 1)
)
vmwNsxTFederationRtepBGPDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterBGPSourceIP"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterBGPNeighborIP"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFailureReason"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationRtepBGPDown.setStatus(
        "current"
    )

vmwNsxTFederationRtepBGPDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 2)
)
vmwNsxTFederationRtepBGPDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterBGPSourceIP"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterBGPNeighborIP"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationRtepBGPDownClear.setStatus(
        "current"
    )

vmwNsxTFederationLmToLmSynchronizationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 3)
)
vmwNsxTFederationLmToLmSynchronizationError.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationLmToLmSynchronizationError.setStatus(
        "current"
    )

vmwNsxTFederationLmToLmSynchronizationErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 4)
)
vmwNsxTFederationLmToLmSynchronizationErrorClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationLmToLmSynchronizationErrorClear.setStatus(
        "current"
    )

vmwNsxTFederationLmToLmSynchronizationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 5)
)
vmwNsxTFederationLmToLmSynchronizationWarning.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationLmToLmSynchronizationWarning.setStatus(
        "current"
    )

vmwNsxTFederationLmToLmSynchronizationWarningClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 6)
)
vmwNsxTFederationLmToLmSynchronizationWarningClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationLmToLmSynchronizationWarningClear.setStatus(
        "current"
    )

vmwNsxTFederationRtepConnectivityLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 7)
)
vmwNsxTFederationRtepConnectivityLost.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationRtepConnectivityLost.setStatus(
        "current"
    )

vmwNsxTFederationRtepConnectivityLostClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 8)
)
vmwNsxTFederationRtepConnectivityLostClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationRtepConnectivityLostClear.setStatus(
        "current"
    )

vmwNsxTFederationGMToGMSplitBrain = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 9)
)
vmwNsxTFederationGMToGMSplitBrain.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterActiveGlobalManagers"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationGMToGMSplitBrain.setStatus(
        "current"
    )

vmwNsxTFederationGMToGMSplitBrainClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 10)
)
vmwNsxTFederationGMToGMSplitBrainClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterActiveGlobalManager"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationGMToGMSplitBrainClear.setStatus(
        "current"
    )

vmwNsxTFederationGMToGMLatencyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 17)
)
vmwNsxTFederationGMToGMLatencyWarning.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFromGMPath"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterToGMPath"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationGMToGMLatencyWarning.setStatus(
        "current"
    )

vmwNsxTFederationGMToGMLatencyWarningClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 18)
)
vmwNsxTFederationGMToGMLatencyWarningClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFromGMPath"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterToGMPath"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationGMToGMLatencyWarningClear.setStatus(
        "current"
    )

vmwNsxTFederationGMToGMSynchronizationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 19)
)
vmwNsxTFederationGMToGMSynchronizationError.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFromGMPath"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterToGMPath"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationGMToGMSynchronizationError.setStatus(
        "current"
    )

vmwNsxTFederationGMToGMSynchronizationErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 20)
)
vmwNsxTFederationGMToGMSynchronizationErrorClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFromGMPath"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterToGMPath"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationGMToGMSynchronizationErrorClear.setStatus(
        "current"
    )

vmwNsxTFederationGMToGMSynchronizationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 21)
)
vmwNsxTFederationGMToGMSynchronizationWarning.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFromGMPath"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterToGMPath"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationGMToGMSynchronizationWarning.setStatus(
        "current"
    )

vmwNsxTFederationGMToGMSynchronizationWarningClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 22)
)
vmwNsxTFederationGMToGMSynchronizationWarningClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFromGMPath"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterToGMPath"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationGMToGMSynchronizationWarningClear.setStatus(
        "current"
    )

vmwNsxTFederationGMToLMSynchronizationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 23)
)
vmwNsxTFederationGMToLMSynchronizationError.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFlowIdentifier"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSyncIssueReason"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationGMToLMSynchronizationError.setStatus(
        "current"
    )

vmwNsxTFederationGMToLMSynchronizationErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 24)
)
vmwNsxTFederationGMToLMSynchronizationErrorClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFlowIdentifier"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationGMToLMSynchronizationErrorClear.setStatus(
        "current"
    )

vmwNsxTFederationGMToLMSynchronizationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 25)
)
vmwNsxTFederationGMToLMSynchronizationWarning.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFlowIdentifier"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSyncIssueReason"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationGMToLMSynchronizationWarning.setStatus(
        "current"
    )

vmwNsxTFederationGMToLMSynchronizationWarningClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 26)
)
vmwNsxTFederationGMToLMSynchronizationWarningClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFlowIdentifier"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationGMToLMSynchronizationWarningClear.setStatus(
        "current"
    )

vmwNsxTFederationGMToLMLatencyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 27)
)
vmwNsxTFederationGMToLMLatencyWarning.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLatencyValue"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLatencyThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationGMToLMLatencyWarning.setStatus(
        "current"
    )

vmwNsxTFederationGMToLMLatencyWarningClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 28)
)
vmwNsxTFederationGMToLMLatencyWarningClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLatencyValue"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLatencyThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationGMToLMLatencyWarningClear.setStatus(
        "current"
    )

vmwNsxTFederationQueueOccupancyThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 29)
)
vmwNsxTFederationQueueOccupancyThresholdExceeded.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterQueueName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterQueueSize"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterQueueSizeThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationQueueOccupancyThresholdExceeded.setStatus(
        "current"
    )

vmwNsxTFederationQueueOccupancyThresholdExceededClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 30)
)
vmwNsxTFederationQueueOccupancyThresholdExceededClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterQueueName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteSiteId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterQueueSize"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterQueueSizeThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationQueueOccupancyThresholdExceededClear.setStatus(
        "current"
    )

vmwNsxTFederationLMRestoreWhileConfigImportInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 31)
)
vmwNsxTFederationLMRestoreWhileConfigImportInProgress.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationLMRestoreWhileConfigImportInProgress.setStatus(
        "current"
    )

vmwNsxTFederationLMRestoreWhileConfigImportInProgressClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 32, 0, 32)
)
vmwNsxTFederationLMRestoreWhileConfigImportInProgressClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSiteId"))
)
if mibBuilder.loadTexts:
    vmwNsxTFederationLMRestoreWhileConfigImportInProgressClear.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSMaxEventsReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 3)
)
vmwNsxTDistributedIDSIPSMaxEventsReached.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIDSEventsCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMaxIDSEventsAllowed"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSMaxEventsReached.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSMaxEventsReachedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 4)
)
vmwNsxTDistributedIDSIPSMaxEventsReachedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIDSEventsCount"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterMaxIDSEventsAllowed"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSMaxEventsReachedClear.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 7)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHigh.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 8)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHighClear.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 9)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 10)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 13)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineDown.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 14)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineDownClear.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 15)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHigh.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 16)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHighClear.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 17)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHigh.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 18)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHighClear.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 19)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 20)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 21)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHigh.setStatus(
        "current"
    )

vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 33, 0, 22)
)
vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemResourceUsage"))
)
if mibBuilder.loadTexts:
    vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHighClear.setStatus(
        "current"
    )

vmwNsxTCommunicationManagementChannelToTransportNodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 1)
)
vmwNsxTCommunicationManagementChannelToTransportNodeDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagementChannelToTransportNodeDown.setStatus(
        "current"
    )

vmwNsxTCommunicationManagementChannelToTransportNodeDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 2)
)
vmwNsxTCommunicationManagementChannelToTransportNodeDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagementChannelToTransportNodeDownClear.setStatus(
        "current"
    )

vmwNsxTCommunicationManagerControlChannelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 3)
)
vmwNsxTCommunicationManagerControlChannelDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagerControlChannelDown.setStatus(
        "current"
    )

vmwNsxTCommunicationManagerControlChannelDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 4)
)
vmwNsxTCommunicationManagerControlChannelDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagerControlChannelDownClear.setStatus(
        "current"
    )

vmwNsxTCommunicationManagementChannelToTransportNodeDownLg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 5)
)
vmwNsxTCommunicationManagementChannelToTransportNodeDownLg.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagementChannelToTransportNodeDownLg.setStatus(
        "current"
    )

vmwNsxTCommunicationManagementChannelToTransportNodeDownLgClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 6)
)
vmwNsxTCommunicationManagementChannelToTransportNodeDownLgClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagementChannelToTransportNodeDownLgClear.setStatus(
        "current"
    )

vmwNsxTCommunicationControlChannelToManagerNodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 7)
)
vmwNsxTCommunicationControlChannelToManagerNodeDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimeoutInMinutes"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationControlChannelToManagerNodeDown.setStatus(
        "current"
    )

vmwNsxTCommunicationControlChannelToManagerNodeDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 8)
)
vmwNsxTCommunicationControlChannelToManagerNodeDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationControlChannelToManagerNodeDownClear.setStatus(
        "current"
    )

vmwNsxTCommunicationControlChannelToManagerNodeDownTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 9)
)
vmwNsxTCommunicationControlChannelToManagerNodeDownTooLong.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimeoutInMinutes"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationControlChannelToManagerNodeDownTooLong.setStatus(
        "current"
    )

vmwNsxTCommunicationControlChannelToManagerNodeDownTooLongClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 10)
)
vmwNsxTCommunicationControlChannelToManagerNodeDownTooLongClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationControlChannelToManagerNodeDownTooLongClear.setStatus(
        "current"
    )

vmwNsxTCommunicationControlChannelToTransportNodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 11)
)
vmwNsxTCommunicationControlChannelToTransportNodeDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCentralControlPlaneId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationControlChannelToTransportNodeDown.setStatus(
        "current"
    )

vmwNsxTCommunicationControlChannelToTransportNodeDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 12)
)
vmwNsxTCommunicationControlChannelToTransportNodeDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCentralControlPlaneId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationControlChannelToTransportNodeDownClear.setStatus(
        "current"
    )

vmwNsxTCommunicationManagementChannelToManagerNodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 13)
)
vmwNsxTCommunicationManagementChannelToManagerNodeDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagementChannelToManagerNodeDown.setStatus(
        "current"
    )

vmwNsxTCommunicationManagementChannelToManagerNodeDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 14)
)
vmwNsxTCommunicationManagementChannelToManagerNodeDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagementChannelToManagerNodeDownClear.setStatus(
        "current"
    )

vmwNsxTCommunicationManagerClusterLatencyHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 17)
)
vmwNsxTCommunicationManagerClusterLatencyHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteManagerNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteApplianceAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagerClusterLatencyHigh.setStatus(
        "current"
    )

vmwNsxTCommunicationManagerClusterLatencyHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 18)
)
vmwNsxTCommunicationManagerClusterLatencyHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteManagerNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterRemoteApplianceAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagerClusterLatencyHighClear.setStatus(
        "current"
    )

vmwNsxTCommunicationControlChannelToTransportNodeDownLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 19)
)
vmwNsxTCommunicationControlChannelToTransportNodeDownLong.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCentralControlPlaneId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationControlChannelToTransportNodeDownLong.setStatus(
        "current"
    )

vmwNsxTCommunicationControlChannelToTransportNodeDownLongClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 20)
)
vmwNsxTCommunicationControlChannelToTransportNodeDownLongClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterCentralControlPlaneId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationControlChannelToTransportNodeDownLongClear.setStatus(
        "current"
    )

vmwNsxTCommunicationManagerFQDNLookupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 21)
)
vmwNsxTCommunicationManagerFQDNLookupFailure.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceFQDN"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagerFQDNLookupFailure.setStatus(
        "current"
    )

vmwNsxTCommunicationManagerFQDNLookupFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 22)
)
vmwNsxTCommunicationManagerFQDNLookupFailureClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceFQDN"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagerFQDNLookupFailureClear.setStatus(
        "current"
    )

vmwNsxTCommunicationManagerFQDNReverseLookupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 23)
)
vmwNsxTCommunicationManagerFQDNReverseLookupFailure.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagerFQDNReverseLookupFailure.setStatus(
        "current"
    )

vmwNsxTCommunicationManagerFQDNReverseLookupFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 24)
)
vmwNsxTCommunicationManagerFQDNReverseLookupFailureClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagerFQDNReverseLookupFailureClear.setStatus(
        "current"
    )

vmwNsxTCommunicationManagementChannelToManagerNodeDownLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 25)
)
vmwNsxTCommunicationManagementChannelToManagerNodeDownLong.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterTransportNodeId"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagementChannelToManagerNodeDownLong.setStatus(
        "current"
    )

vmwNsxTCommunicationManagementChannelToManagerNodeDownLongClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 35, 0, 26)
)
vmwNsxTCommunicationManagementChannelToManagerNodeDownLongClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterApplianceAddress"))
)
if mibBuilder.loadTexts:
    vmwNsxTCommunicationManagementChannelToManagerNodeDownLongClear.setStatus(
        "current"
    )

vmwNsxTIdentityFirewallConnectivityToLDAPServerLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 36, 0, 1)
)
vmwNsxTIdentityFirewallConnectivityToLDAPServerLost.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLDAPServer"))
)
if mibBuilder.loadTexts:
    vmwNsxTIdentityFirewallConnectivityToLDAPServerLost.setStatus(
        "current"
    )

vmwNsxTIdentityFirewallConnectivityToLDAPServerLostClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 36, 0, 2)
)
vmwNsxTIdentityFirewallConnectivityToLDAPServerLostClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterLDAPServer"))
)
if mibBuilder.loadTexts:
    vmwNsxTIdentityFirewallConnectivityToLDAPServerLostClear.setStatus(
        "current"
    )

vmwNsxTIdentityFirewallErrorInDeltaSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 36, 0, 3)
)
vmwNsxTIdentityFirewallErrorInDeltaSync.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDirectoryDomain"))
)
if mibBuilder.loadTexts:
    vmwNsxTIdentityFirewallErrorInDeltaSync.setStatus(
        "current"
    )

vmwNsxTIdentityFirewallErrorInDeltaSyncClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 36, 0, 4)
)
vmwNsxTIdentityFirewallErrorInDeltaSyncClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterDirectoryDomain"))
)
if mibBuilder.loadTexts:
    vmwNsxTIdentityFirewallErrorInDeltaSyncClear.setStatus(
        "current"
    )

vmwNsxTIPAMIPBlockUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 38, 0, 1)
)
vmwNsxTIPAMIPBlockUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntentPath"))
)
if mibBuilder.loadTexts:
    vmwNsxTIPAMIPBlockUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTIPAMIPBlockUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 38, 0, 2)
)
vmwNsxTIPAMIPBlockUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntentPath"))
)
if mibBuilder.loadTexts:
    vmwNsxTIPAMIPBlockUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTIPAMIPPoolUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 38, 0, 3)
)
vmwNsxTIPAMIPPoolUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntentPath"))
)
if mibBuilder.loadTexts:
    vmwNsxTIPAMIPPoolUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTIPAMIPPoolUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 38, 0, 4)
)
vmwNsxTIPAMIPPoolUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterIntentPath"))
)
if mibBuilder.loadTexts:
    vmwNsxTIPAMIPPoolUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTGatewayFirewallICMPFlowCountExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 39, 0, 21)
)
vmwNsxTGatewayFirewallICMPFlowCountExceeded.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFirewallICMPFlowUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTGatewayFirewallICMPFlowCountExceeded.setStatus(
        "current"
    )

vmwNsxTGatewayFirewallICMPFlowCountExceededClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 39, 0, 22)
)
vmwNsxTGatewayFirewallICMPFlowCountExceededClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTGatewayFirewallICMPFlowCountExceededClear.setStatus(
        "current"
    )

vmwNsxTGatewayFirewallICMPFlowCountHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 39, 0, 23)
)
vmwNsxTGatewayFirewallICMPFlowCountHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFirewallICMPFlowUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTGatewayFirewallICMPFlowCountHigh.setStatus(
        "current"
    )

vmwNsxTGatewayFirewallICMPFlowCountHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 39, 0, 24)
)
vmwNsxTGatewayFirewallICMPFlowCountHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTGatewayFirewallICMPFlowCountHighClear.setStatus(
        "current"
    )

vmwNsxTGatewayFirewallIPFlowCountExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 39, 0, 25)
)
vmwNsxTGatewayFirewallIPFlowCountExceeded.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFirewallIPFlowUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTGatewayFirewallIPFlowCountExceeded.setStatus(
        "current"
    )

vmwNsxTGatewayFirewallIPFlowCountExceededClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 39, 0, 26)
)
vmwNsxTGatewayFirewallIPFlowCountExceededClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTGatewayFirewallIPFlowCountExceededClear.setStatus(
        "current"
    )

vmwNsxTGatewayFirewallIPFlowCountHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 39, 0, 27)
)
vmwNsxTGatewayFirewallIPFlowCountHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFirewallIPFlowUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTGatewayFirewallIPFlowCountHigh.setStatus(
        "current"
    )

vmwNsxTGatewayFirewallIPFlowCountHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 39, 0, 28)
)
vmwNsxTGatewayFirewallIPFlowCountHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTGatewayFirewallIPFlowCountHighClear.setStatus(
        "current"
    )

vmwNsxTGatewayFirewallTcpHalfOpenFlowCountExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 39, 0, 29)
)
vmwNsxTGatewayFirewallTcpHalfOpenFlowCountExceeded.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFirewallHalfopenFlowUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTGatewayFirewallTcpHalfOpenFlowCountExceeded.setStatus(
        "current"
    )

vmwNsxTGatewayFirewallTcpHalfOpenFlowCountExceededClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 39, 0, 30)
)
vmwNsxTGatewayFirewallTcpHalfOpenFlowCountExceededClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTGatewayFirewallTcpHalfOpenFlowCountExceededClear.setStatus(
        "current"
    )

vmwNsxTGatewayFirewallTcpHalfOpenFlowCountHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 39, 0, 31)
)
vmwNsxTGatewayFirewallTcpHalfOpenFlowCountHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFirewallHalfopenFlowUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTGatewayFirewallTcpHalfOpenFlowCountHigh.setStatus(
        "current"
    )

vmwNsxTGatewayFirewallTcpHalfOpenFlowCountHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 39, 0, 32)
)
vmwNsxTGatewayFirewallTcpHalfOpenFlowCountHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTGatewayFirewallTcpHalfOpenFlowCountHighClear.setStatus(
        "current"
    )

vmwNsxTGatewayFirewallUDPFlowCountExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 39, 0, 33)
)
vmwNsxTGatewayFirewallUDPFlowCountExceeded.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFirewallUDPFlowUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTGatewayFirewallUDPFlowCountExceeded.setStatus(
        "current"
    )

vmwNsxTGatewayFirewallUDPFlowCountExceededClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 39, 0, 34)
)
vmwNsxTGatewayFirewallUDPFlowCountExceededClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTGatewayFirewallUDPFlowCountExceededClear.setStatus(
        "current"
    )

vmwNsxTGatewayFirewallUDPFlowCountHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 39, 0, 35)
)
vmwNsxTGatewayFirewallUDPFlowCountHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFirewallUDPFlowUsage"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTGatewayFirewallUDPFlowCountHigh.setStatus(
        "current"
    )

vmwNsxTGatewayFirewallUDPFlowCountHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 39, 0, 36)
)
vmwNsxTGatewayFirewallUDPFlowCountHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTGatewayFirewallUDPFlowCountHighClear.setStatus(
        "current"
    )

vmwNsxTClusteringClusterDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 40, 0, 1)
)
vmwNsxTClusteringClusterDegraded.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterGroupType"))
)
if mibBuilder.loadTexts:
    vmwNsxTClusteringClusterDegraded.setStatus(
        "current"
    )

vmwNsxTClusteringClusterDegradedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 40, 0, 2)
)
vmwNsxTClusteringClusterDegradedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterGroupType"))
)
if mibBuilder.loadTexts:
    vmwNsxTClusteringClusterDegradedClear.setStatus(
        "current"
    )

vmwNsxTClusteringClusterUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 40, 0, 3)
)
vmwNsxTClusteringClusterUnavailable.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeIDS"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterGroupType"))
)
if mibBuilder.loadTexts:
    vmwNsxTClusteringClusterUnavailable.setStatus(
        "current"
    )

vmwNsxTClusteringClusterUnavailableClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 40, 0, 4)
)
vmwNsxTClusteringClusterUnavailableClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterManagerNodeIDS"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterGroupType"))
)
if mibBuilder.loadTexts:
    vmwNsxTClusteringClusterUnavailableClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformCommunicationMgrDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 41, 0, 1)
)
vmwNsxTNSXApplicationPlatformCommunicationMgrDisconnected.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformCommunicationMgrDisconnected.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformCommunicationMgrDisconnectedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 41, 0, 2)
)
vmwNsxTNSXApplicationPlatformCommunicationMgrDisconnectedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformCommunicationMgrDisconnectedClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformCommunicationDelayInOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 41, 0, 7)
)
vmwNsxTNSXApplicationPlatformCommunicationDelayInOverflow.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappMessagingLAGThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformCommunicationDelayInOverflow.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformCommunicationDelayInOverflowClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 41, 0, 8)
)
vmwNsxTNSXApplicationPlatformCommunicationDelayInOverflowClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappMessagingLAGThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformCommunicationDelayInOverflowClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformCommunicationDelayInRawflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 41, 0, 11)
)
vmwNsxTNSXApplicationPlatformCommunicationDelayInRawflow.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappMessagingLAGThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformCommunicationDelayInRawflow.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformCommunicationDelayInRawflowClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 41, 0, 12)
)
vmwNsxTNSXApplicationPlatformCommunicationDelayInRawflowClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappMessagingLAGThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformCommunicationDelayInRawflowClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformCommunicationExpDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 41, 0, 13)
)
vmwNsxTNSXApplicationPlatformCommunicationExpDisconnected.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformCommunicationExpDisconnected.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformCommunicationExpDisconnectedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 41, 0, 14)
)
vmwNsxTNSXApplicationPlatformCommunicationExpDisconnectedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformCommunicationExpDisconnectedClear.setStatus(
        "current"
    )

vmwNsxTMTUCheckMTUMismatchWithinTransportZone = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 42, 0, 1)
)
vmwNsxTMTUCheckMTUMismatchWithinTransportZone.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTMTUCheckMTUMismatchWithinTransportZone.setStatus(
        "current"
    )

vmwNsxTMTUCheckMTUMismatchWithinTransportZoneClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 42, 0, 2)
)
vmwNsxTMTUCheckMTUMismatchWithinTransportZoneClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTMTUCheckMTUMismatchWithinTransportZoneClear.setStatus(
        "current"
    )

vmwNsxTMTUCheckGlobalRouterMTUTooBig = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 42, 0, 3)
)
vmwNsxTMTUCheckGlobalRouterMTUTooBig.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTMTUCheckGlobalRouterMTUTooBig.setStatus(
        "current"
    )

vmwNsxTMTUCheckGlobalRouterMTUTooBigClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 42, 0, 4)
)
vmwNsxTMTUCheckGlobalRouterMTUTooBigClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTMTUCheckGlobalRouterMTUTooBigClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 1)
)
vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 2)
)
vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageVeryHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 3)
)
vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageVeryHi.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageVeryHi.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageVeryHiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 4)
)
vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageVeryHiClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageVeryHiClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 5)
)
vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 6)
)
vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageVeryHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 7)
)
vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageVeryHi.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageVeryHi.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageVeryHiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 8)
)
vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageVeryHiClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageVeryHiClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthAnalyticsMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 9)
)
vmwNsxTNSXApplicationPlatformHealthAnalyticsMemoryUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthAnalyticsMemoryUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthAnalyticsMemoryUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 10)
)
vmwNsxTNSXApplicationPlatformHealthAnalyticsMemoryUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthAnalyticsMemoryUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthAnalyticsMemUsageVeryHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 11)
)
vmwNsxTNSXApplicationPlatformHealthAnalyticsMemUsageVeryHi.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthAnalyticsMemUsageVeryHi.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthAnalyticsMemUsageVeryHiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 12)
)
vmwNsxTNSXApplicationPlatformHealthAnalyticsMemUsageVeryHiClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthAnalyticsMemUsageVeryHiClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 13)
)
vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 14)
)
vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 15)
)
vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 16)
)
vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 17)
)
vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 18)
)
vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 19)
)
vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 20)
)
vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthClusterMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 21)
)
vmwNsxTNSXApplicationPlatformHealthClusterMemoryUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthClusterMemoryUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthClusterMemoryUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 22)
)
vmwNsxTNSXApplicationPlatformHealthClusterMemoryUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthClusterMemoryUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthClusterMemUsageVeryHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 23)
)
vmwNsxTNSXApplicationPlatformHealthClusterMemUsageVeryHi.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthClusterMemUsageVeryHi.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthClusterMemUsageVeryHiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 24)
)
vmwNsxTNSXApplicationPlatformHealthClusterMemUsageVeryHiClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthClusterMemUsageVeryHiClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 31)
)
vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageHi.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageHi.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageHiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 32)
)
vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageHiClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageHiClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageVeryHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 33)
)
vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageVeryHi.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageVeryHi.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageVeryHiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 34)
)
vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageVeryHiClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageVeryHiClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 35)
)
vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 36)
)
vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageVeryHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 37)
)
vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageVeryHi.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageVeryHi.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageVeryHiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 38)
)
vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageVeryHiClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageVeryHiClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 39)
)
vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 40)
)
vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 41)
)
vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 42)
)
vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageVeryHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 43)
)
vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageVeryHi.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageVeryHi.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageVeryHiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 44)
)
vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageVeryHiClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageVeryHiClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 45)
)
vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 46)
)
vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageVeryHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 47)
)
vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageVeryHi.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageVeryHi.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageVeryHiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 48)
)
vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageVeryHiClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageVeryHiClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthDatastoreMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 49)
)
vmwNsxTNSXApplicationPlatformHealthDatastoreMemoryUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthDatastoreMemoryUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthDatastoreMemoryUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 50)
)
vmwNsxTNSXApplicationPlatformHealthDatastoreMemoryUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthDatastoreMemoryUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthDatastoreMemUsageVeryHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 51)
)
vmwNsxTNSXApplicationPlatformHealthDatastoreMemUsageVeryHi.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthDatastoreMemUsageVeryHi.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthDatastoreMemUsageVeryHiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 52)
)
vmwNsxTNSXApplicationPlatformHealthDatastoreMemUsageVeryHiClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthDatastoreMemUsageVeryHiClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 53)
)
vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 54)
)
vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageVeryHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 55)
)
vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageVeryHi.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageVeryHi.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageVeryHiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 56)
)
vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageVeryHiClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageVeryHiClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 57)
)
vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 58)
)
vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageVeryHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 59)
)
vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageVeryHi.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageVeryHi.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageVeryHiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 60)
)
vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageVeryHiClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageVeryHiClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMessagingMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 61)
)
vmwNsxTNSXApplicationPlatformHealthMessagingMemoryUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMessagingMemoryUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMessagingMemoryUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 62)
)
vmwNsxTNSXApplicationPlatformHealthMessagingMemoryUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMessagingMemoryUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMessagingMemUsageVeryHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 63)
)
vmwNsxTNSXApplicationPlatformHealthMessagingMemUsageVeryHi.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMessagingMemUsageVeryHi.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMessagingMemUsageVeryHiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 64)
)
vmwNsxTNSXApplicationPlatformHealthMessagingMemUsageVeryHiClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMessagingMemUsageVeryHiClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 65)
)
vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 66)
)
vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 67)
)
vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 68)
)
vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 69)
)
vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 70)
)
vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 71)
)
vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 72)
)
vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 73)
)
vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 74)
)
vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 75)
)
vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 76)
)
vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappNodeName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNodeStatusDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 77)
)
vmwNsxTNSXApplicationPlatformHealthNodeStatusDegraded.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappNodeName"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNodeStatusDegraded.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNodeStatusDegradedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 78)
)
vmwNsxTNSXApplicationPlatformHealthNodeStatusDegradedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappNodeName"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNodeStatusDegradedClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNodeStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 79)
)
vmwNsxTNSXApplicationPlatformHealthNodeStatusDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappNodeName"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNodeStatusDown.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNodeStatusDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 80)
)
vmwNsxTNSXApplicationPlatformHealthNodeStatusDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappNodeName"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNodeStatusDownClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 81)
)
vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 82)
)
vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 83)
)
vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 84)
)
vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 85)
)
vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 86)
)
vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageVeryHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 87)
)
vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageVeryHi.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageVeryHi.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageVeryHiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 88)
)
vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageVeryHiClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageVeryHiClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthPlatformMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 89)
)
vmwNsxTNSXApplicationPlatformHealthPlatformMemoryUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthPlatformMemoryUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthPlatformMemoryUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 90)
)
vmwNsxTNSXApplicationPlatformHealthPlatformMemoryUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthPlatformMemoryUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthPlatformMemUsageVeryHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 91)
)
vmwNsxTNSXApplicationPlatformHealthPlatformMemUsageVeryHi.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthPlatformMemUsageVeryHi.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthPlatformMemUsageVeryHiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 92)
)
vmwNsxTNSXApplicationPlatformHealthPlatformMemUsageVeryHiClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthPlatformMemUsageVeryHiClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthServiceStatusDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 93)
)
vmwNsxTNSXApplicationPlatformHealthServiceStatusDegraded.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappServiceName"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthServiceStatusDegraded.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthServiceStatusDegradedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 94)
)
vmwNsxTNSXApplicationPlatformHealthServiceStatusDegradedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappServiceName"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthServiceStatusDegradedClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthServiceStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 95)
)
vmwNsxTNSXApplicationPlatformHealthServiceStatusDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappServiceName"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthServiceStatusDown.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthServiceStatusDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 96)
)
vmwNsxTNSXApplicationPlatformHealthServiceStatusDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappServiceName"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthServiceStatusDownClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 97)
)
vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 98)
)
vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 99)
)
vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 100)
)
vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 101)
)
vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageHi.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageHi.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageHiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 102)
)
vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageHiClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageHiClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 103)
)
vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 104)
)
vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMetricsMemUasgeHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 105)
)
vmwNsxTNSXApplicationPlatformHealthMetricsMemUasgeHi.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMetricsMemUasgeHi.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMetricsMemUasgeHiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 106)
)
vmwNsxTNSXApplicationPlatformHealthMetricsMemUasgeHiClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMetricsMemUasgeHiClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMetricsMemUsageVeryHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 107)
)
vmwNsxTNSXApplicationPlatformHealthMetricsMemUsageVeryHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMetricsMemUsageVeryHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthMetricsMemUsageVeryHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 108)
)
vmwNsxTNSXApplicationPlatformHealthMetricsMemUsageVeryHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthMetricsMemUsageVeryHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 109)
)
vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageHigh.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 110)
)
vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageHighClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNappStatusDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 117)
)
vmwNsxTNSXApplicationPlatformHealthNappStatusDegraded.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNappStatusDegraded.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNappStatusDegradedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 118)
)
vmwNsxTNSXApplicationPlatformHealthNappStatusDegradedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNappStatusDegradedClear.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNappStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 119)
)
vmwNsxTNSXApplicationPlatformHealthNappStatusDown.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNappStatusDown.setStatus(
        "current"
    )

vmwNsxTNSXApplicationPlatformHealthNappStatusDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 43, 0, 120)
)
vmwNsxTNSXApplicationPlatformHealthNappStatusDownClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNappClusterId"))
)
if mibBuilder.loadTexts:
    vmwNsxTNSXApplicationPlatformHealthNappStatusDownClear.setStatus(
        "current"
    )

vmwNsxTEdgeEdgeNodeSettingsAndvSphereSettingsAreChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 45, 0, 1)
)
vmwNsxTEdgeEdgeNodeSettingsAndvSphereSettingsAreChanged.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNodeAndvSphereSettingsMismatchReason"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeEdgeNodeSettingsAndvSphereSettingsAreChanged.setStatus(
        "current"
    )

vmwNsxTEdgeEdgeNodeSettingsAndvSphereSettingsAreChangedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 45, 0, 2)
)
vmwNsxTEdgeEdgeNodeSettingsAndvSphereSettingsAreChangedClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeEdgeNodeSettingsAndvSphereSettingsAreChangedClear.setStatus(
        "current"
    )

vmwNsxTEdgeEdgeNodeSettingsMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 45, 0, 3)
)
vmwNsxTEdgeEdgeNodeSettingsMismatch.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeNodeSettingMismatchReason"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeEdgeNodeSettingsMismatch.setStatus(
        "current"
    )

vmwNsxTEdgeEdgeNodeSettingsMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 45, 0, 4)
)
vmwNsxTEdgeEdgeNodeSettingsMismatchClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeEdgeNodeSettingsMismatchClear.setStatus(
        "current"
    )

vmwNsxTEdgeEdgeVmvSphereSettingsMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 45, 0, 5)
)
vmwNsxTEdgeEdgeVmvSphereSettingsMismatch.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgeVMvSphereSettingsMismatchReason"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeEdgeVmvSphereSettingsMismatch.setStatus(
        "current"
    )

vmwNsxTEdgeEdgeVmvSphereSettingsMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 45, 0, 6)
)
vmwNsxTEdgeEdgeVmvSphereSettingsMismatchClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeEdgeVmvSphereSettingsMismatchClear.setStatus(
        "current"
    )

vmwNsxTEdgeEdgevSphereLocationMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 45, 0, 7)
)
vmwNsxTEdgeEdgevSphereLocationMismatch.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEdgevSphereLocationMismatchReason"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeEdgevSphereLocationMismatch.setStatus(
        "current"
    )

vmwNsxTEdgeEdgevSphereLocationMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 45, 0, 8)
)
vmwNsxTEdgeEdgevSphereLocationMismatchClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"))
)
if mibBuilder.loadTexts:
    vmwNsxTEdgeEdgevSphereLocationMismatchClear.setStatus(
        "current"
    )

vmwNsxTNATSNATPortUsageOnGatewayIsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 46, 0, 1)
)
vmwNsxTNATSNATPortUsageOnGatewayIsHigh.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSNATIPAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNATSNATPortUsageOnGatewayIsHigh.setStatus(
        "current"
    )

vmwNsxTNATSNATPortUsageOnGatewayIsHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 0, 46, 0, 2)
)
vmwNsxTNATSNATPortUsageOnGatewayIsHighClear.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterTimestamp"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterFeatureName"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEventSeverity"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNodeType"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterEntityId"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSNATIPAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterSystemUsageThreshold"))
)
if mibBuilder.loadTexts:
    vmwNsxTNATSNATPortUsageOnGatewayIsHighClear.setStatus(
        "current"
    )


# Notifications groups

vmwNsxTDataCenterNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 2)
)
vmwNsxTDataCenterNotificationGroup.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTAlarmManagementAlarmServiceOverloaded"),
        ("VMWARE-NSX-MIB", "vmwNsxTAlarmManagementAlarmServiceOverloadedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTAlarmManagementHeavyVolumeOfAlarms"),
        ("VMWARE-NSX-MIB", "vmwNsxTAlarmManagementHeavyVolumeOfAlarmsClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCertificatesCertificateExpirationApproaching"),
        ("VMWARE-NSX-MIB", "vmwNsxTCertificatesCertificateExpirationApproachingClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCertificatesCertificateExpired"),
        ("VMWARE-NSX-MIB", "vmwNsxTCertificatesCertificateExpiredClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCertificatesCertificateIsAboutToExpire"),
        ("VMWARE-NSX-MIB", "vmwNsxTCertificatesCertificateIsAboutToExpireClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCniHealthHyperbusManagerConnectionDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTCniHealthHyperbusManagerConnectionDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDHCPPoolLeaseAllocationFailed"),
        ("VMWARE-NSX-MIB", "vmwNsxTDHCPPoolLeaseAllocationFailedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDHCPPoolOverloaded"),
        ("VMWARE-NSX-MIB", "vmwNsxTDHCPPoolOverloadedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedFirewallDFWCPUUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedFirewallDFWCPUUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedFirewallDFWMemoryUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedFirewallDFWMemoryUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDNSForwarderDisabled"),
        ("VMWARE-NSX-MIB", "vmwNsxTDNSForwarderDisabledClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDNSForwarderDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTDNSForwarderDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeCPUUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeCPUUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeCPUUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeCPUUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathConfigurationFailure"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathConfigurationFailureClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathCPUHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathCPUHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathCPUVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathCPUVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathCryptodrvDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathCryptodrvDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathMempoolHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathMempoolHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDiskUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDiskUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDiskUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDiskUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeMemoryUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeMemoryUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeMemoryUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeMemoryUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeNICLinkStatusDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeNICLinkStatusDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeNICOutOfReceiveBuffer"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeNICOutOfReceiveBufferClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeNICOutOfTransmitBuffer"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeNICOutOfTransmitBufferClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEndpointProtectionEAMStatusDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTEndpointProtectionEAMStatusDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEndpointProtectionPartnerChannelDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTEndpointProtectionPartnerChannelDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTHighAvailabilityTier0GatewayFailover"),
        ("VMWARE-NSX-MIB", "vmwNsxTHighAvailabilityTier0GatewayFailoverClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTHighAvailabilityTier1GatewayFailover"),
        ("VMWARE-NSX-MIB", "vmwNsxTHighAvailabilityTier1GatewayFailoverClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTInfrastructureCommunicationEdgeTunnelsDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTInfrastructureCommunicationEdgeTunnelsDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTInfrastructureServiceEdgeServiceStatusChanged"),
        ("VMWARE-NSX-MIB", "vmwNsxTInfrastructureServiceEdgeServiceStatusChangedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTInfrastructureServiceEdgeServiceStatusDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTInfrastructureServiceEdgeServiceStatusDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnected"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnectedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthCPUUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthCPUUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthCPUUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthCPUUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthDataDiskPartitionUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthDataDiskPartitionUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthDiskUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthDiskUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthDiskUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthDiskUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthMemoryUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthMemoryUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthMemoryUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthMemoryUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthNodeStatusDegraded"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthNodeStatusDegradedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLicensesLicenseExpired"),
        ("VMWARE-NSX-MIB", "vmwNsxTLicensesLicenseExpiredClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLicensesLicenseIsAboutToExpire"),
        ("VMWARE-NSX-MIB", "vmwNsxTLicensesLicenseIsAboutToExpireClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBCPUVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBCPUVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBStatusDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBStatusDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerPoolStatusDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerPoolStatusDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerVirtualServerStatusDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerVirtualServerStatusDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthDuplicateIPAddress"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthDuplicateIPAddressClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerConfigDiskUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerConfigDiskUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerConfigDiskUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerConfigDiskUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerCPUUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerCPUUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerCPUUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerCPUUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerDiskUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerDiskUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerDiskUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerDiskUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerMemoryUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerMemoryUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerMemoryUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthManagerMemoryUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNCPHealthNCPPluginDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTNCPHealthNCPPluginDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNodeAgentsHealthNodeAgentsDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTNodeAgentsHealthNodeAgentsDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTPasswordManagementPasswordExpirationApproaching"),
        ("VMWARE-NSX-MIB", "vmwNsxTPasswordManagementPasswordExpirationApproachingClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTPasswordManagementPasswordExpired"),
        ("VMWARE-NSX-MIB", "vmwNsxTPasswordManagementPasswordExpiredClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTPasswordManagementPasswordIsAboutToExpire"),
        ("VMWARE-NSX-MIB", "vmwNsxTPasswordManagementPasswordIsAboutToExpireClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingBFDDownOnExternalInterface"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingBFDDownOnExternalInterfaceClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingBGPDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingBGPDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingRoutingDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingRoutingDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingStaticRoutingRemoved"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingStaticRoutingRemovedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTTransportNodeHealthLAGMemberDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTTransportNodeHealthLAGMemberDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTTransportNodeHealthNVDSUplinkDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTTransportNodeHealthNVDSUplinkDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNIPsecPolicyBasedSessionDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNIPsecPolicyBasedSessionDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNIPsecPolicyBasedTunnelDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNIPsecPolicyBasedTunnelDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNIPsecRouteBasedSessionDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNIPsecRouteBasedSessionDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNIPsecRouteBasedTunnelDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNIPsecRouteBasedTunnelDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNL2VpnSessionDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNL2VpnSessionDownClear"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationGroup.setStatus(
        "current"
    )

vmwNsxTDataCenterNotificationGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 4)
)
vmwNsxTDataCenterNotificationGroup2.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthStorageError"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthStorageErrorClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationLmToLmSynchronizationError"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationLmToLmSynchronizationErrorClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationLmToLmSynchronizationWarning"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationLmToLmSynchronizationWarningClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationRtepBGPDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationRtepBGPDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthOperationsDbDiskUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthOperationsDbDiskUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthOperationsDbDiskUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthOperationsDbDiskUsageVeryHighClear"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationGroup2.setStatus(
        "current"
    )

vmwNsxTDataCenterNotificationGroup3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 6)
)
vmwNsxTDataCenterNotificationGroup3.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagementChannelToTransportNodeDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagementChannelToTransportNodeDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagementChannelToTransportNodeDownLg"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagementChannelToTransportNodeDownLgClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagerControlChannelDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagerControlChannelDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationRtepConnectivityLost"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationRtepConnectivityLostClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthStorageError"),
        ("VMWARE-NSX-MIB", "vmwNsxTManagerHealthStorageErrorClear"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationGroup3.setStatus(
        "current"
    )

vmwNsxTDataCenterNotificationGroup4 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 8)
)
vmwNsxTDataCenterNotificationGroup4.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTAuditLogHealthAuditLogFileUpdateError"),
        ("VMWARE-NSX-MIB", "vmwNsxTAuditLogHealthAuditLogFileUpdateErrorClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTAuditLogHealthRemoteLoggingServerError"),
        ("VMWARE-NSX-MIB", "vmwNsxTAuditLogHealthRemoteLoggingServerErrorClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCapacityMaximumCapacity"),
        ("VMWARE-NSX-MIB", "vmwNsxTCapacityMaximumCapacityClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCapacityMaximumCapacityThreshold"),
        ("VMWARE-NSX-MIB", "vmwNsxTCapacityMaximumCapacityThresholdClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCapacityMinimumCapacityThreshold"),
        ("VMWARE-NSX-MIB", "vmwNsxTCapacityMinimumCapacityThresholdClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationControlChannelToManagerNodeDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationControlChannelToManagerNodeDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationControlChannelToManagerNodeDownTooLong"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationControlChannelToManagerNodeDownTooLongClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationControlChannelToTransportNodeDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationControlChannelToTransportNodeDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationControlChannelToTransportNodeDownLong"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationControlChannelToTransportNodeDownLongClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagerClusterLatencyHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagerClusterLatencyHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagerFQDNLookupFailure"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagerFQDNLookupFailureClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagerFQDNReverseLookupFailure"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagerFQDNReverseLookupFailureClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSMaxEventsReached"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSMaxEventsReachedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthDatapathThreadDeadlocked"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthDatapathThreadDeadlockedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationGMToGMSplitBrain"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationGMToGMSplitBrainClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIdentityFirewallConnectivityToLDAPServerLost"),
        ("VMWARE-NSX-MIB", "vmwNsxTIdentityFirewallConnectivityToLDAPServerLostClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIdentityFirewallErrorInDeltaSync"),
        ("VMWARE-NSX-MIB", "vmwNsxTIdentityFirewallErrorInDeltaSyncClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTInfrastructureServiceServiceStatusUnknown"),
        ("VMWARE-NSX-MIB", "vmwNsxTInfrastructureServiceServiceStatusUnknownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthStorageLatencyHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIntelligenceHealthStorageLatencyHighClear"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationGroup4.setStatus(
        "current"
    )

vmwNsxTDataCenterNotificationGroup5 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 10)
)
vmwNsxTDataCenterNotificationGroup5.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTRoutingOSPFNeighborWentDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingOSPFNeighborWentDownClear"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationGroup5.setStatus(
        "current"
    )

vmwNsxTDataCenterNotificationGroup6 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 12)
)
vmwNsxTDataCenterNotificationGroup6.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTRoutingProxyARPNotConfiguredForServiceIP"),
        ("VMWARE-NSX-MIB", "vmwNsxTRoutingProxyARPNotConfiguredForServiceIPClear"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationGroup6.setStatus(
        "current"
    )

vmwNsxTDataCenterNotificationGroup7 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 14)
)
vmwNsxTDataCenterNotificationGroup7.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTIPAMIPBlockUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIPAMIPBlockUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTIPAMIPPoolUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTIPAMIPPoolUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerDLBStatusDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerDLBStatusDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBEdgeCapacityInUseHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBEdgeCapacityInUseHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBStatusDegraded"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerLBStatusDegradedClear"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationGroup7.setStatus(
        "current"
    )

vmwNsxTDataCenterNotificationGroup8 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 16)
)
vmwNsxTDataCenterNotificationGroup8.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDNSForwarderUpstreamServerTimeout"),
        ("VMWARE-NSX-MIB", "vmwNsxTDNSForwarderUpstreamServerTimeoutClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTGatewayFirewallICMPFlowCountExceeded"),
        ("VMWARE-NSX-MIB", "vmwNsxTGatewayFirewallICMPFlowCountExceededClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTGatewayFirewallICMPFlowCountHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTGatewayFirewallICMPFlowCountHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTGatewayFirewallIPFlowCountExceeded"),
        ("VMWARE-NSX-MIB", "vmwNsxTGatewayFirewallIPFlowCountExceededClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTGatewayFirewallIPFlowCountHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTGatewayFirewallIPFlowCountHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTGatewayFirewallTcpHalfOpenFlowCountExceeded"),
        ("VMWARE-NSX-MIB", "vmwNsxTGatewayFirewallTcpHalfOpenFlowCountExceededClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTGatewayFirewallTcpHalfOpenFlowCountHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTGatewayFirewallTcpHalfOpenFlowCountHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTGatewayFirewallUDPFlowCountExceeded"),
        ("VMWARE-NSX-MIB", "vmwNsxTGatewayFirewallUDPFlowCountExceededClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTGatewayFirewallUDPFlowCountHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTGatewayFirewallUDPFlowCountHighClear"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationGroup8.setStatus(
        "current"
    )

vmwNsxTDataCenterNotificationGroup9 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 2, 18)
)
vmwNsxTDataCenterNotificationGroup9.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTCertificatesCABundleUpdateRecommended"),
        ("VMWARE-NSX-MIB", "vmwNsxTCertificatesCABundleUpdateRecommendedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCertificatesCABundleUpdateSuggested"),
        ("VMWARE-NSX-MIB", "vmwNsxTCertificatesCABundleUpdateSuggestedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTClusteringClusterDegraded"),
        ("VMWARE-NSX-MIB", "vmwNsxTClusteringClusterDegradedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTClusteringClusterUnavailable"),
        ("VMWARE-NSX-MIB", "vmwNsxTClusteringClusterUnavailableClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagementChannelToManagerNodeDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagementChannelToManagerNodeDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagementChannelToManagerNodeDownLong"),
        ("VMWARE-NSX-MIB", "vmwNsxTCommunicationManagementChannelToManagerNodeDownLongClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedFirewallDFWSessionCountHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedFirewallDFWSessionCountHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedFirewallDFWVmotionFailure"),
        ("VMWARE-NSX-MIB", "vmwNsxTDistributedFirewallDFWVmotionFailureClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeEdgeNodeSettingsAndvSphereSettingsAreChanged"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeEdgeNodeSettingsAndvSphereSettingsAreChangedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeEdgeNodeSettingsMismatch"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeEdgeNodeSettingsMismatchClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeEdgeVmvSphereSettingsMismatch"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeEdgeVmvSphereSettingsMismatchClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeEdgevSphereLocationMismatch"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeEdgevSphereLocationMismatchClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathNICThroughputHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathNICThroughputHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathNICThroughputVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthEdgeDatapathNICThroughputVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthFailureDomainDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTEdgeHealthFailureDomainDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationGMToGMLatencyWarning"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationGMToGMLatencyWarningClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationGMToGMSynchronizationError"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationGMToGMSynchronizationErrorClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationGMToGMSynchronizationWarning"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationGMToGMSynchronizationWarningClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationGMToLMLatencyWarning"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationGMToLMLatencyWarningClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationGMToLMSynchronizationError"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationGMToLMSynchronizationErrorClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationGMToLMSynchronizationWarning"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationGMToLMSynchronizationWarningClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationLMRestoreWhileConfigImportInProgress"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationLMRestoreWhileConfigImportInProgressClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationQueueOccupancyThresholdExceeded"),
        ("VMWARE-NSX-MIB", "vmwNsxTFederationQueueOccupancyThresholdExceededClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerConfigurationNotRealizedDueToLowMemory"),
        ("VMWARE-NSX-MIB", "vmwNsxTLoadBalancerConfigurationNotRealizedDueToLowMemoryClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTMTUCheckGlobalRouterMTUTooBig"),
        ("VMWARE-NSX-MIB", "vmwNsxTMTUCheckGlobalRouterMTUTooBigClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTMTUCheckMTUMismatchWithinTransportZone"),
        ("VMWARE-NSX-MIB", "vmwNsxTMTUCheckMTUMismatchWithinTransportZoneClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNATSNATPortUsageOnGatewayIsHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNATSNATPortUsageOnGatewayIsHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformCommunicationDelayInOverflow"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformCommunicationDelayInOverflowClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformCommunicationDelayInRawflow"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformCommunicationDelayInRawflowClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformCommunicationMgrDisconnected"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformCommunicationMgrDisconnectedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformCommunicationExpDisconnected"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformCommunicationExpDisconnectedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageVeryHi"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageVeryHiClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageVeryHi"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageVeryHiClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthAnalyticsMemoryUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthAnalyticsMemoryUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthAnalyticsMemUsageVeryHi"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthAnalyticsMemUsageVeryHiClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthClusterMemoryUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthClusterMemoryUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthClusterMemUsageVeryHi"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthClusterMemUsageVeryHiClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageHi"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageHiClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageVeryHi"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageVeryHiClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageVeryHi"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageVeryHiClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageVeryHi"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageVeryHiClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageVeryHi"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageVeryHiClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthDatastoreMemoryUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthDatastoreMemoryUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthDatastoreMemUsageVeryHi"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthDatastoreMemUsageVeryHiClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageVeryHi"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageVeryHiClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageVeryHi"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageVeryHiClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMessagingMemoryUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMessagingMemoryUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMessagingMemUsageVeryHi"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMessagingMemUsageVeryHiClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageHi"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageHiClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMetricsMemUasgeHi"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMetricsMemUasgeHiClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMetricsMemUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthMetricsMemUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNappStatusDegraded"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNappStatusDegradedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNappStatusDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNappStatusDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNodeStatusDegraded"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNodeStatusDegradedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNodeStatusDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthNodeStatusDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageVeryHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageVeryHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageVeryHi"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageVeryHiClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthPlatformMemoryUsageHigh"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthPlatformMemoryUsageHighClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthPlatformMemUsageVeryHi"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthPlatformMemUsageVeryHiClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthServiceStatusDegraded"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthServiceStatusDegradedClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthServiceStatusDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTNSXApplicationPlatformHealthServiceStatusDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTTransportNodeHealthTransportNodeUplinkDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTTransportNodeHealthTransportNodeUplinkDownClear"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNIPsecServiceDown"),
        ("VMWARE-NSX-MIB", "vmwNsxTVPNIPsecServiceDownClear"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterNotificationGroup9.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmwNsxTDataCenterBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 1, 1)
)
vmwNsxTDataCenterBasicCompliance.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBasicCompliance.setStatus(
        "deprecated"
    )

vmwNsxTDataCenterBasicCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 1, 2)
)
vmwNsxTDataCenterBasicCompliance2.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup2"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBasicCompliance2.setStatus(
        "deprecated"
    )

vmwNsxTDataCenterBasicCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 1, 3)
)
vmwNsxTDataCenterBasicCompliance3.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup3"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBasicCompliance3.setStatus(
        "deprecated"
    )

vmwNsxTDataCenterBasicCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 1, 4)
)
vmwNsxTDataCenterBasicCompliance4.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup4"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup4"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBasicCompliance4.setStatus(
        "deprecated"
    )

vmwNsxTDataCenterBasicCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 1, 5)
)
vmwNsxTDataCenterBasicCompliance5.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup4"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup4"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup5"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBasicCompliance5.setStatus(
        "deprecated"
    )

vmwNsxTDataCenterBasicCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 1, 6)
)
vmwNsxTDataCenterBasicCompliance6.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup4"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup6"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup4"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup5"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup6"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBasicCompliance6.setStatus(
        "deprecated"
    )

vmwNsxTDataCenterBasicCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 1, 7)
)
vmwNsxTDataCenterBasicCompliance7.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup4"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup6"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup7"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup4"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup5"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup6"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup7"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBasicCompliance7.setStatus(
        "deprecated"
    )

vmwNsxTDataCenterBasicCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 1, 8)
)
vmwNsxTDataCenterBasicCompliance8.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup4"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup7"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup8"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup4"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup5"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup6"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup7"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup8"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBasicCompliance8.setStatus(
        "deprecated"
    )

vmwNsxTDataCenterBasicCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 120, 1, 2, 1, 9)
)
vmwNsxTDataCenterBasicCompliance9.setObjects(
      *(("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup4"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup7"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup8"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationInfoGroup9"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup2"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup3"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup4"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup5"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup6"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup7"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup8"),
        ("VMWARE-NSX-MIB", "vmwNsxTDataCenterNotificationGroup9"))
)
if mibBuilder.loadTexts:
    vmwNsxTDataCenterBasicCompliance9.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-NSX-MIB",
    **{"VmwNsxTDataCenterFeatureIdType": VmwNsxTDataCenterFeatureIdType,
       "VmwNsxTDataCenterEventTypeType": VmwNsxTDataCenterEventTypeType,
       "VmwNsxTDataCenterSeverityType": VmwNsxTDataCenterSeverityType,
       "VmwNsxTDataCenterNodeIdType": VmwNsxTDataCenterNodeIdType,
       "VmwNsxTDataCenterNodeTypeType": VmwNsxTDataCenterNodeTypeType,
       "VmwNsxTDataCenterEntityIdType": VmwNsxTDataCenterEntityIdType,
       "VmwNsxTDataCenterSystemResourceUsageType": VmwNsxTDataCenterSystemResourceUsageType,
       "VmwNsxTDataCenterDiskPartitionNameType": VmwNsxTDataCenterDiskPartitionNameType,
       "VmwNsxTDataCenterLicenseEditionTypeType": VmwNsxTDataCenterLicenseEditionTypeType,
       "VmwNsxTDataCenterApplianceAddressType": VmwNsxTDataCenterApplianceAddressType,
       "VmwNsxTDataCenterCurrentGatewayStateType": VmwNsxTDataCenterCurrentGatewayStateType,
       "VmwNsxTDataCenterCurrentServiceStateType": VmwNsxTDataCenterCurrentServiceStateType,
       "VmwNsxTDataCenterDatapathResourceUsageType": VmwNsxTDataCenterDatapathResourceUsageType,
       "VmwNsxTDataCenterDHCPPoolUsageType": VmwNsxTDataCenterDHCPPoolUsageType,
       "VmwNsxTDataCenterEdgeServiceNameType": VmwNsxTDataCenterEdgeServiceNameType,
       "VmwNsxTDataCenterFailureReasonType": VmwNsxTDataCenterFailureReasonType,
       "VmwNsxTDataCenterPreviousGatewayStateType": VmwNsxTDataCenterPreviousGatewayStateType,
       "VmwNsxTDataCenterPreviousServiceStateType": VmwNsxTDataCenterPreviousServiceStateType,
       "VmwNsxTDataCenterSystemUsageThresholdType": VmwNsxTDataCenterSystemUsageThresholdType,
       "VmwNsxTDataCenterUsernameType": VmwNsxTDataCenterUsernameType,
       "VmwNsxTDataCenterDHCPServerIdType": VmwNsxTDataCenterDHCPServerIdType,
       "VmwNsxTDataCenterServiceNameType": VmwNsxTDataCenterServiceNameType,
       "VmwNsxTDataCenterIntelligenceNodeIdType": VmwNsxTDataCenterIntelligenceNodeIdType,
       "VmwNsxTDataCenterHostnameOrIPAddressWithPortType": VmwNsxTDataCenterHostnameOrIPAddressWithPortType,
       "VmwNsxTDataCenterEventIdType": VmwNsxTDataCenterEventIdType,
       "VmwNsxTDataCenterActiveGlobalManagerType": VmwNsxTDataCenterActiveGlobalManagerType,
       "VmwNsxTDataCenterActiveGlobalManagersType": VmwNsxTDataCenterActiveGlobalManagersType,
       "VmwNsxTDataCenterSessionDownReasonType": VmwNsxTDataCenterSessionDownReasonType,
       "VmwNsxTDataCenterManagerNodeNameType": VmwNsxTDataCenterManagerNodeNameType,
       "VmwNsxTDataCenterTransportNodeAddressType": VmwNsxTDataCenterTransportNodeAddressType,
       "VmwNsxTDataCenterTransportNodeNameType": VmwNsxTDataCenterTransportNodeNameType,
       "VmwNsxTDataCenterCentralControlPlaneIdType": VmwNsxTDataCenterCentralControlPlaneIdType,
       "VmwNsxTDataCenterTunnelDownReasonType": VmwNsxTDataCenterTunnelDownReasonType,
       "VmwNsxTDataCenterHeapTypeType": VmwNsxTDataCenterHeapTypeType,
       "VmwNsxTDataCenterMempoolNameType": VmwNsxTDataCenterMempoolNameType,
       "VmwNsxTDataCenterPasswordExpirationDaysType": VmwNsxTDataCenterPasswordExpirationDaysType,
       "VmwNsxTDataCenterBGPNeighborIPType": VmwNsxTDataCenterBGPNeighborIPType,
       "VmwNsxTDataCenterLDAPServerType": VmwNsxTDataCenterLDAPServerType,
       "VmwNsxTDataCenterPeerAddressType": VmwNsxTDataCenterPeerAddressType,
       "VmwNsxTDataCenterMaxIDSEventsAllowedType": VmwNsxTDataCenterMaxIDSEventsAllowedType,
       "VmwNsxTDataCenterStaticAddressType": VmwNsxTDataCenterStaticAddressType,
       "VmwNsxTDataCenterDuplicateIPAddressType": VmwNsxTDataCenterDuplicateIPAddressType,
       "VmwNsxTDataCenterCapacityDisplayNameType": VmwNsxTDataCenterCapacityDisplayNameType,
       "VmwNsxTDataCenterCapacityUsageCountType": VmwNsxTDataCenterCapacityUsageCountType,
       "VmwNsxTDataCenterEdgeNICNameType": VmwNsxTDataCenterEdgeNICNameType,
       "VmwNsxTDataCenterRxRingBufferOverflowPercentageType": VmwNsxTDataCenterRxRingBufferOverflowPercentageType,
       "VmwNsxTDataCenterTxRingBufferOverflowPercentageType": VmwNsxTDataCenterTxRingBufferOverflowPercentageType,
       "VmwNsxTDataCenterSrIdType": VmwNsxTDataCenterSrIdType,
       "VmwNsxTDataCenterIDSEventsCountType": VmwNsxTDataCenterIDSEventsCountType,
       "VmwNsxTDataCenterRemoteSiteNameType": VmwNsxTDataCenterRemoteSiteNameType,
       "VmwNsxTDataCenterBGPSourceIPType": VmwNsxTDataCenterBGPSourceIPType,
       "VmwNsxTDataCenterRemoteSiteIdType": VmwNsxTDataCenterRemoteSiteIdType,
       "VmwNsxTDataCenterSiteIdType": VmwNsxTDataCenterSiteIdType,
       "VmwNsxTDataCenterSiteNameType": VmwNsxTDataCenterSiteNameType,
       "VmwNsxTDataCenterLrIdType": VmwNsxTDataCenterLrIdType,
       "VmwNsxTDataCenterRxMissesType": VmwNsxTDataCenterRxMissesType,
       "VmwNsxTDataCenterRxProcessedType": VmwNsxTDataCenterRxProcessedType,
       "VmwNsxTDataCenterTxMissesType": VmwNsxTDataCenterTxMissesType,
       "VmwNsxTDataCenterTxProcessedType": VmwNsxTDataCenterTxProcessedType,
       "VmwNsxTDataCenterLrportIdType": VmwNsxTDataCenterLrportIdType,
       "VmwNsxTDataCenterServiceIPType": VmwNsxTDataCenterServiceIPType,
       "VmwNsxTDataCenterRemoteManagerNodeIdType": VmwNsxTDataCenterRemoteManagerNodeIdType,
       "VmwNsxTDataCenterDirectoryDomainType": VmwNsxTDataCenterDirectoryDomainType,
       "VmwNsxTDataCenterTimeoutInMinutesType": VmwNsxTDataCenterTimeoutInMinutesType,
       "VmwNsxTDataCenterMaxCapacityThresholdType": VmwNsxTDataCenterMaxCapacityThresholdType,
       "VmwNsxTDataCenterMinCapacityThresholdType": VmwNsxTDataCenterMinCapacityThresholdType,
       "VmwNsxTDataCenterMaxSupportedCapacityCountType": VmwNsxTDataCenterMaxSupportedCapacityCountType,
       "VmwNsxTDataCenterLatencySourceType": VmwNsxTDataCenterLatencySourceType,
       "VmwNsxTDataCenterLatencyThresholdType": VmwNsxTDataCenterLatencyThresholdType,
       "VmwNsxTDataCenterLatencyValueType": VmwNsxTDataCenterLatencyValueType,
       "VmwNsxTDataCenterApplianceFQDNType": VmwNsxTDataCenterApplianceFQDNType,
       "VmwNsxTDataCenterRemoteApplianceAddressType": VmwNsxTDataCenterRemoteApplianceAddressType,
       "VmwNsxTDataCenterManagerNodeIdType": VmwNsxTDataCenterManagerNodeIdType,
       "VmwNsxTDataCenterDisplayedLicenseKeyType": VmwNsxTDataCenterDisplayedLicenseKeyType,
       "VmwNsxTDataCenterEdgeThreadNameType": VmwNsxTDataCenterEdgeThreadNameType,
       "VmwNsxTDataCenterIntentPathType": VmwNsxTDataCenterIntentPathType,
       "VmwNsxTDataCenterFirewallHalfopenFlowUsageType": VmwNsxTDataCenterFirewallHalfopenFlowUsageType,
       "VmwNsxTDataCenterFirewallICMPFlowUsageType": VmwNsxTDataCenterFirewallICMPFlowUsageType,
       "VmwNsxTDataCenterServiceDownReasonType": VmwNsxTDataCenterServiceDownReasonType,
       "VmwNsxTDataCenterFirewallUDPFlowUsageType": VmwNsxTDataCenterFirewallUDPFlowUsageType,
       "VmwNsxTDataCenterFirewallIPFlowUsageType": VmwNsxTDataCenterFirewallIPFlowUsageType,
       "VmwNsxTDataCenterDNSIdType": VmwNsxTDataCenterDNSIdType,
       "VmwNsxTDataCenterDNSUpstreamIPType": VmwNsxTDataCenterDNSUpstreamIPType,
       "VmwNsxTDataCenterCABundleAgeThresholdType": VmwNsxTDataCenterCABundleAgeThresholdType,
       "VmwNsxTDataCenterAPICollectionPathType": VmwNsxTDataCenterAPICollectionPathType,
       "VmwNsxTDataCenterEdgeNodeSettingMismatchReasonType": VmwNsxTDataCenterEdgeNodeSettingMismatchReasonType,
       "VmwNsxTDataCenterEdgeVMvSphereSettingsMismatchReasonType": VmwNsxTDataCenterEdgeVMvSphereSettingsMismatchReasonType,
       "VmwNsxTDataCenterFirewallSNATPortsUsageType": VmwNsxTDataCenterFirewallSNATPortsUsageType,
       "VmwNsxTDataCenterEdgevSphereLocationMismatchReasonType": VmwNsxTDataCenterEdgevSphereLocationMismatchReasonType,
       "VmwNsxTDataCenterEdgeNodeAndvSphereSettingsMismatchReasonType": VmwNsxTDataCenterEdgeNodeAndvSphereSettingsMismatchReasonType,
       "VmwNsxTDataCenterSNATIPAddressType": VmwNsxTDataCenterSNATIPAddressType,
       "VmwNsxTDataCenterNappClusterIdType": VmwNsxTDataCenterNappClusterIdType,
       "VmwNsxTDataCenterNappMessagingLAGThresholdType": VmwNsxTDataCenterNappMessagingLAGThresholdType,
       "VmwNsxTDataCenterNappNodeIdType": VmwNsxTDataCenterNappNodeIdType,
       "VmwNsxTDataCenterNappServiceNameType": VmwNsxTDataCenterNappServiceNameType,
       "VmwNsxTDataCenterFlowIdentifierType": VmwNsxTDataCenterFlowIdentifierType,
       "VmwNsxTDataCenterSyncIssueReasonType": VmwNsxTDataCenterSyncIssueReasonType,
       "VmwNsxTDataCenterQueueNameType": VmwNsxTDataCenterQueueNameType,
       "VmwNsxTDataCenterQueueSizeType": VmwNsxTDataCenterQueueSizeType,
       "VmwNsxTDataCenterQueueSizeThresholdType": VmwNsxTDataCenterQueueSizeThresholdType,
       "VmwNsxTDataCenterGroupTypeType": VmwNsxTDataCenterGroupTypeType,
       "VmwNsxTDataCenterManagerNodeIDSType": VmwNsxTDataCenterManagerNodeIDSType,
       "VmwNsxTDataCenterServiceRouterIdType": VmwNsxTDataCenterServiceRouterIdType,
       "VmwNsxTDataCenterTransportNodeIdType": VmwNsxTDataCenterTransportNodeIdType,
       "VmwNsxTDataCenterFromGMPathType": VmwNsxTDataCenterFromGMPathType,
       "VmwNsxTDataCenterToGMPathType": VmwNsxTDataCenterToGMPathType,
       "VmwNsxTDataCenterNICThroughputType": VmwNsxTDataCenterNICThroughputType,
       "VmwNsxTDataCenterNICThroughputThresholdType": VmwNsxTDataCenterNICThroughputThresholdType,
       "VmwNsxTDataCenterEdgeCryptoDrvNameType": VmwNsxTDataCenterEdgeCryptoDrvNameType,
       "VmwNsxTDataCenterNappNodeNameType": VmwNsxTDataCenterNappNodeNameType,
       "vmwNSXsysMIB": vmwNSXsysMIB,
       "vmwNsxTDataCenterNotifications": vmwNsxTDataCenterNotifications,
       "vmwNsxTManagerHealthFeaturePrefix": vmwNsxTManagerHealthFeaturePrefix,
       "vmwNsxTManagerHealthFeature": vmwNsxTManagerHealthFeature,
       "vmwNsxTManagerHealthManagerCPUUsageHigh": vmwNsxTManagerHealthManagerCPUUsageHigh,
       "vmwNsxTManagerHealthManagerCPUUsageHighClear": vmwNsxTManagerHealthManagerCPUUsageHighClear,
       "vmwNsxTManagerHealthManagerCPUUsageVeryHigh": vmwNsxTManagerHealthManagerCPUUsageVeryHigh,
       "vmwNsxTManagerHealthManagerCPUUsageVeryHighClear": vmwNsxTManagerHealthManagerCPUUsageVeryHighClear,
       "vmwNsxTManagerHealthManagerMemoryUsageHigh": vmwNsxTManagerHealthManagerMemoryUsageHigh,
       "vmwNsxTManagerHealthManagerMemoryUsageHighClear": vmwNsxTManagerHealthManagerMemoryUsageHighClear,
       "vmwNsxTManagerHealthManagerMemoryUsageVeryHigh": vmwNsxTManagerHealthManagerMemoryUsageVeryHigh,
       "vmwNsxTManagerHealthManagerMemoryUsageVeryHighClear": vmwNsxTManagerHealthManagerMemoryUsageVeryHighClear,
       "vmwNsxTManagerHealthManagerDiskUsageHigh": vmwNsxTManagerHealthManagerDiskUsageHigh,
       "vmwNsxTManagerHealthManagerDiskUsageHighClear": vmwNsxTManagerHealthManagerDiskUsageHighClear,
       "vmwNsxTManagerHealthManagerDiskUsageVeryHigh": vmwNsxTManagerHealthManagerDiskUsageVeryHigh,
       "vmwNsxTManagerHealthManagerDiskUsageVeryHighClear": vmwNsxTManagerHealthManagerDiskUsageVeryHighClear,
       "vmwNsxTManagerHealthManagerConfigDiskUsageHigh": vmwNsxTManagerHealthManagerConfigDiskUsageHigh,
       "vmwNsxTManagerHealthManagerConfigDiskUsageHighClear": vmwNsxTManagerHealthManagerConfigDiskUsageHighClear,
       "vmwNsxTManagerHealthManagerConfigDiskUsageVeryHigh": vmwNsxTManagerHealthManagerConfigDiskUsageVeryHigh,
       "vmwNsxTManagerHealthManagerConfigDiskUsageVeryHighClear": vmwNsxTManagerHealthManagerConfigDiskUsageVeryHighClear,
       "vmwNsxTManagerHealthDuplicateIPAddress": vmwNsxTManagerHealthDuplicateIPAddress,
       "vmwNsxTManagerHealthDuplicateIPAddressClear": vmwNsxTManagerHealthDuplicateIPAddressClear,
       "vmwNsxTManagerHealthOperationsDbDiskUsageHigh": vmwNsxTManagerHealthOperationsDbDiskUsageHigh,
       "vmwNsxTManagerHealthOperationsDbDiskUsageHighClear": vmwNsxTManagerHealthOperationsDbDiskUsageHighClear,
       "vmwNsxTManagerHealthOperationsDbDiskUsageVeryHigh": vmwNsxTManagerHealthOperationsDbDiskUsageVeryHigh,
       "vmwNsxTManagerHealthOperationsDbDiskUsageVeryHighClear": vmwNsxTManagerHealthOperationsDbDiskUsageVeryHighClear,
       "vmwNsxTManagerHealthStorageError": vmwNsxTManagerHealthStorageError,
       "vmwNsxTManagerHealthStorageErrorClear": vmwNsxTManagerHealthStorageErrorClear,
       "vmwNsxTEdgeHealthFeaturePrefix": vmwNsxTEdgeHealthFeaturePrefix,
       "vmwNsxTEdgeHealthFeature": vmwNsxTEdgeHealthFeature,
       "vmwNsxTEdgeHealthEdgeCPUUsageHigh": vmwNsxTEdgeHealthEdgeCPUUsageHigh,
       "vmwNsxTEdgeHealthEdgeCPUUsageHighClear": vmwNsxTEdgeHealthEdgeCPUUsageHighClear,
       "vmwNsxTEdgeHealthEdgeCPUUsageVeryHigh": vmwNsxTEdgeHealthEdgeCPUUsageVeryHigh,
       "vmwNsxTEdgeHealthEdgeCPUUsageVeryHighClear": vmwNsxTEdgeHealthEdgeCPUUsageVeryHighClear,
       "vmwNsxTEdgeHealthEdgeMemoryUsageHigh": vmwNsxTEdgeHealthEdgeMemoryUsageHigh,
       "vmwNsxTEdgeHealthEdgeMemoryUsageHighClear": vmwNsxTEdgeHealthEdgeMemoryUsageHighClear,
       "vmwNsxTEdgeHealthEdgeMemoryUsageVeryHigh": vmwNsxTEdgeHealthEdgeMemoryUsageVeryHigh,
       "vmwNsxTEdgeHealthEdgeMemoryUsageVeryHighClear": vmwNsxTEdgeHealthEdgeMemoryUsageVeryHighClear,
       "vmwNsxTEdgeHealthEdgeDiskUsageHigh": vmwNsxTEdgeHealthEdgeDiskUsageHigh,
       "vmwNsxTEdgeHealthEdgeDiskUsageHighClear": vmwNsxTEdgeHealthEdgeDiskUsageHighClear,
       "vmwNsxTEdgeHealthEdgeDiskUsageVeryHigh": vmwNsxTEdgeHealthEdgeDiskUsageVeryHigh,
       "vmwNsxTEdgeHealthEdgeDiskUsageVeryHighClear": vmwNsxTEdgeHealthEdgeDiskUsageVeryHighClear,
       "vmwNsxTEdgeHealthEdgeDatapathCPUHigh": vmwNsxTEdgeHealthEdgeDatapathCPUHigh,
       "vmwNsxTEdgeHealthEdgeDatapathCPUHighClear": vmwNsxTEdgeHealthEdgeDatapathCPUHighClear,
       "vmwNsxTEdgeHealthEdgeDatapathCPUVeryHigh": vmwNsxTEdgeHealthEdgeDatapathCPUVeryHigh,
       "vmwNsxTEdgeHealthEdgeDatapathCPUVeryHighClear": vmwNsxTEdgeHealthEdgeDatapathCPUVeryHighClear,
       "vmwNsxTEdgeHealthEdgeDatapathConfigurationFailure": vmwNsxTEdgeHealthEdgeDatapathConfigurationFailure,
       "vmwNsxTEdgeHealthEdgeDatapathConfigurationFailureClear": vmwNsxTEdgeHealthEdgeDatapathConfigurationFailureClear,
       "vmwNsxTEdgeHealthEdgeDatapathCryptodrvDown": vmwNsxTEdgeHealthEdgeDatapathCryptodrvDown,
       "vmwNsxTEdgeHealthEdgeDatapathCryptodrvDownClear": vmwNsxTEdgeHealthEdgeDatapathCryptodrvDownClear,
       "vmwNsxTEdgeHealthEdgeDatapathMempoolHigh": vmwNsxTEdgeHealthEdgeDatapathMempoolHigh,
       "vmwNsxTEdgeHealthEdgeDatapathMempoolHighClear": vmwNsxTEdgeHealthEdgeDatapathMempoolHighClear,
       "vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHigh": vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHigh,
       "vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHighClear": vmwNsxTEdgeHealthEdgeGlobalARPTableUsageHighClear,
       "vmwNsxTEdgeHealthEdgeNICLinkStatusDown": vmwNsxTEdgeHealthEdgeNICLinkStatusDown,
       "vmwNsxTEdgeHealthEdgeNICLinkStatusDownClear": vmwNsxTEdgeHealthEdgeNICLinkStatusDownClear,
       "vmwNsxTEdgeHealthEdgeNICOutOfReceiveBuffer": vmwNsxTEdgeHealthEdgeNICOutOfReceiveBuffer,
       "vmwNsxTEdgeHealthEdgeNICOutOfReceiveBufferClear": vmwNsxTEdgeHealthEdgeNICOutOfReceiveBufferClear,
       "vmwNsxTEdgeHealthEdgeNICOutOfTransmitBuffer": vmwNsxTEdgeHealthEdgeNICOutOfTransmitBuffer,
       "vmwNsxTEdgeHealthEdgeNICOutOfTransmitBufferClear": vmwNsxTEdgeHealthEdgeNICOutOfTransmitBufferClear,
       "vmwNsxTEdgeHealthStorageError": vmwNsxTEdgeHealthStorageError,
       "vmwNsxTEdgeHealthStorageErrorClear": vmwNsxTEdgeHealthStorageErrorClear,
       "vmwNsxTEdgeHealthDatapathThreadDeadlocked": vmwNsxTEdgeHealthDatapathThreadDeadlocked,
       "vmwNsxTEdgeHealthDatapathThreadDeadlockedClear": vmwNsxTEdgeHealthDatapathThreadDeadlockedClear,
       "vmwNsxTEdgeHealthEdgeDatapathNICThroughputHigh": vmwNsxTEdgeHealthEdgeDatapathNICThroughputHigh,
       "vmwNsxTEdgeHealthEdgeDatapathNICThroughputHighClear": vmwNsxTEdgeHealthEdgeDatapathNICThroughputHighClear,
       "vmwNsxTEdgeHealthEdgeDatapathNICThroughputVeryHigh": vmwNsxTEdgeHealthEdgeDatapathNICThroughputVeryHigh,
       "vmwNsxTEdgeHealthEdgeDatapathNICThroughputVeryHighClear": vmwNsxTEdgeHealthEdgeDatapathNICThroughputVeryHighClear,
       "vmwNsxTEdgeHealthFailureDomainDown": vmwNsxTEdgeHealthFailureDomainDown,
       "vmwNsxTEdgeHealthFailureDomainDownClear": vmwNsxTEdgeHealthFailureDomainDownClear,
       "vmwNsxTCertificatesFeaturePrefix": vmwNsxTCertificatesFeaturePrefix,
       "vmwNsxTCertificatesFeature": vmwNsxTCertificatesFeature,
       "vmwNsxTCertificatesCertificateExpirationApproaching": vmwNsxTCertificatesCertificateExpirationApproaching,
       "vmwNsxTCertificatesCertificateExpirationApproachingClear": vmwNsxTCertificatesCertificateExpirationApproachingClear,
       "vmwNsxTCertificatesCertificateExpired": vmwNsxTCertificatesCertificateExpired,
       "vmwNsxTCertificatesCertificateExpiredClear": vmwNsxTCertificatesCertificateExpiredClear,
       "vmwNsxTCertificatesCertificateIsAboutToExpire": vmwNsxTCertificatesCertificateIsAboutToExpire,
       "vmwNsxTCertificatesCertificateIsAboutToExpireClear": vmwNsxTCertificatesCertificateIsAboutToExpireClear,
       "vmwNsxTCertificatesCABundleUpdateRecommended": vmwNsxTCertificatesCABundleUpdateRecommended,
       "vmwNsxTCertificatesCABundleUpdateRecommendedClear": vmwNsxTCertificatesCABundleUpdateRecommendedClear,
       "vmwNsxTCertificatesCABundleUpdateSuggested": vmwNsxTCertificatesCABundleUpdateSuggested,
       "vmwNsxTCertificatesCABundleUpdateSuggestedClear": vmwNsxTCertificatesCABundleUpdateSuggestedClear,
       "vmwNsxTPasswordManagementFeaturePrefix": vmwNsxTPasswordManagementFeaturePrefix,
       "vmwNsxTPasswordManagementFeature": vmwNsxTPasswordManagementFeature,
       "vmwNsxTPasswordManagementPasswordExpirationApproaching": vmwNsxTPasswordManagementPasswordExpirationApproaching,
       "vmwNsxTPasswordManagementPasswordExpirationApproachingClear": vmwNsxTPasswordManagementPasswordExpirationApproachingClear,
       "vmwNsxTPasswordManagementPasswordExpired": vmwNsxTPasswordManagementPasswordExpired,
       "vmwNsxTPasswordManagementPasswordExpiredClear": vmwNsxTPasswordManagementPasswordExpiredClear,
       "vmwNsxTPasswordManagementPasswordIsAboutToExpire": vmwNsxTPasswordManagementPasswordIsAboutToExpire,
       "vmwNsxTPasswordManagementPasswordIsAboutToExpireClear": vmwNsxTPasswordManagementPasswordIsAboutToExpireClear,
       "vmwNsxTLicensesFeaturePrefix": vmwNsxTLicensesFeaturePrefix,
       "vmwNsxTLicensesFeature": vmwNsxTLicensesFeature,
       "vmwNsxTLicensesLicenseExpired": vmwNsxTLicensesLicenseExpired,
       "vmwNsxTLicensesLicenseExpiredClear": vmwNsxTLicensesLicenseExpiredClear,
       "vmwNsxTLicensesLicenseIsAboutToExpire": vmwNsxTLicensesLicenseIsAboutToExpire,
       "vmwNsxTLicensesLicenseIsAboutToExpireClear": vmwNsxTLicensesLicenseIsAboutToExpireClear,
       "vmwNsxTIntelligenceHealthFeaturePrefix": vmwNsxTIntelligenceHealthFeaturePrefix,
       "vmwNsxTIntelligenceHealthFeature": vmwNsxTIntelligenceHealthFeature,
       "vmwNsxTIntelligenceHealthCPUUsageHigh": vmwNsxTIntelligenceHealthCPUUsageHigh,
       "vmwNsxTIntelligenceHealthCPUUsageHighClear": vmwNsxTIntelligenceHealthCPUUsageHighClear,
       "vmwNsxTIntelligenceHealthCPUUsageVeryHigh": vmwNsxTIntelligenceHealthCPUUsageVeryHigh,
       "vmwNsxTIntelligenceHealthCPUUsageVeryHighClear": vmwNsxTIntelligenceHealthCPUUsageVeryHighClear,
       "vmwNsxTIntelligenceHealthDataDiskPartitionUsageHigh": vmwNsxTIntelligenceHealthDataDiskPartitionUsageHigh,
       "vmwNsxTIntelligenceHealthDataDiskPartitionUsageHighClear": vmwNsxTIntelligenceHealthDataDiskPartitionUsageHighClear,
       "vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHigh": vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHigh,
       "vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHighClear": vmwNsxTIntelligenceHealthDataDiskPartitionUsageVeryHighClear,
       "vmwNsxTIntelligenceHealthDiskUsageHigh": vmwNsxTIntelligenceHealthDiskUsageHigh,
       "vmwNsxTIntelligenceHealthDiskUsageHighClear": vmwNsxTIntelligenceHealthDiskUsageHighClear,
       "vmwNsxTIntelligenceHealthDiskUsageVeryHigh": vmwNsxTIntelligenceHealthDiskUsageVeryHigh,
       "vmwNsxTIntelligenceHealthDiskUsageVeryHighClear": vmwNsxTIntelligenceHealthDiskUsageVeryHighClear,
       "vmwNsxTIntelligenceHealthMemoryUsageHigh": vmwNsxTIntelligenceHealthMemoryUsageHigh,
       "vmwNsxTIntelligenceHealthMemoryUsageHighClear": vmwNsxTIntelligenceHealthMemoryUsageHighClear,
       "vmwNsxTIntelligenceHealthMemoryUsageVeryHigh": vmwNsxTIntelligenceHealthMemoryUsageVeryHigh,
       "vmwNsxTIntelligenceHealthMemoryUsageVeryHighClear": vmwNsxTIntelligenceHealthMemoryUsageVeryHighClear,
       "vmwNsxTIntelligenceHealthNodeStatusDegraded": vmwNsxTIntelligenceHealthNodeStatusDegraded,
       "vmwNsxTIntelligenceHealthNodeStatusDegradedClear": vmwNsxTIntelligenceHealthNodeStatusDegradedClear,
       "vmwNsxTIntelligenceHealthStorageLatencyHigh": vmwNsxTIntelligenceHealthStorageLatencyHigh,
       "vmwNsxTIntelligenceHealthStorageLatencyHighClear": vmwNsxTIntelligenceHealthStorageLatencyHighClear,
       "vmwNsxTInfrastructureCommunicationFeaturePrefix": vmwNsxTInfrastructureCommunicationFeaturePrefix,
       "vmwNsxTInfrastructureCommunicationFeature": vmwNsxTInfrastructureCommunicationFeature,
       "vmwNsxTInfrastructureCommunicationEdgeTunnelsDown": vmwNsxTInfrastructureCommunicationEdgeTunnelsDown,
       "vmwNsxTInfrastructureCommunicationEdgeTunnelsDownClear": vmwNsxTInfrastructureCommunicationEdgeTunnelsDownClear,
       "vmwNsxTIntelligenceCommunicationFeaturePrefix": vmwNsxTIntelligenceCommunicationFeaturePrefix,
       "vmwNsxTIntelligenceCommunicationFeature": vmwNsxTIntelligenceCommunicationFeature,
       "vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnected": vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnected,
       "vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnectedClear": vmwNsxTIntelligenceCommunicationTNFlowExporterDisconnectedClear,
       "vmwNsxTCniHealthFeaturePrefix": vmwNsxTCniHealthFeaturePrefix,
       "vmwNsxTCniHealthFeature": vmwNsxTCniHealthFeature,
       "vmwNsxTCniHealthHyperbusManagerConnectionDown": vmwNsxTCniHealthHyperbusManagerConnectionDown,
       "vmwNsxTCniHealthHyperbusManagerConnectionDownClear": vmwNsxTCniHealthHyperbusManagerConnectionDownClear,
       "vmwNsxTNCPHealthFeaturePrefix": vmwNsxTNCPHealthFeaturePrefix,
       "vmwNsxTNCPHealthFeature": vmwNsxTNCPHealthFeature,
       "vmwNsxTNCPHealthNCPPluginDown": vmwNsxTNCPHealthNCPPluginDown,
       "vmwNsxTNCPHealthNCPPluginDownClear": vmwNsxTNCPHealthNCPPluginDownClear,
       "vmwNsxTNodeAgentsHealthFeaturePrefix": vmwNsxTNodeAgentsHealthFeaturePrefix,
       "vmwNsxTNodeAgentsHealthFeature": vmwNsxTNodeAgentsHealthFeature,
       "vmwNsxTNodeAgentsHealthNodeAgentsDown": vmwNsxTNodeAgentsHealthNodeAgentsDown,
       "vmwNsxTNodeAgentsHealthNodeAgentsDownClear": vmwNsxTNodeAgentsHealthNodeAgentsDownClear,
       "vmwNsxTEndpointProtectionFeaturePrefix": vmwNsxTEndpointProtectionFeaturePrefix,
       "vmwNsxTEndpointProtectionFeature": vmwNsxTEndpointProtectionFeature,
       "vmwNsxTEndpointProtectionEAMStatusDown": vmwNsxTEndpointProtectionEAMStatusDown,
       "vmwNsxTEndpointProtectionEAMStatusDownClear": vmwNsxTEndpointProtectionEAMStatusDownClear,
       "vmwNsxTEndpointProtectionPartnerChannelDown": vmwNsxTEndpointProtectionPartnerChannelDown,
       "vmwNsxTEndpointProtectionPartnerChannelDownClear": vmwNsxTEndpointProtectionPartnerChannelDownClear,
       "vmwNsxTVPNFeaturePrefix": vmwNsxTVPNFeaturePrefix,
       "vmwNsxTVPNFeature": vmwNsxTVPNFeature,
       "vmwNsxTVPNIPsecPolicyBasedSessionDown": vmwNsxTVPNIPsecPolicyBasedSessionDown,
       "vmwNsxTVPNIPsecPolicyBasedSessionDownClear": vmwNsxTVPNIPsecPolicyBasedSessionDownClear,
       "vmwNsxTVPNIPsecPolicyBasedTunnelDown": vmwNsxTVPNIPsecPolicyBasedTunnelDown,
       "vmwNsxTVPNIPsecPolicyBasedTunnelDownClear": vmwNsxTVPNIPsecPolicyBasedTunnelDownClear,
       "vmwNsxTVPNIPsecRouteBasedSessionDown": vmwNsxTVPNIPsecRouteBasedSessionDown,
       "vmwNsxTVPNIPsecRouteBasedSessionDownClear": vmwNsxTVPNIPsecRouteBasedSessionDownClear,
       "vmwNsxTVPNIPsecRouteBasedTunnelDown": vmwNsxTVPNIPsecRouteBasedTunnelDown,
       "vmwNsxTVPNIPsecRouteBasedTunnelDownClear": vmwNsxTVPNIPsecRouteBasedTunnelDownClear,
       "vmwNsxTVPNL2VpnSessionDown": vmwNsxTVPNL2VpnSessionDown,
       "vmwNsxTVPNL2VpnSessionDownClear": vmwNsxTVPNL2VpnSessionDownClear,
       "vmwNsxTVPNIPsecServiceDown": vmwNsxTVPNIPsecServiceDown,
       "vmwNsxTVPNIPsecServiceDownClear": vmwNsxTVPNIPsecServiceDownClear,
       "vmwNsxTAlarmManagementFeaturePrefix": vmwNsxTAlarmManagementFeaturePrefix,
       "vmwNsxTAlarmManagementFeature": vmwNsxTAlarmManagementFeature,
       "vmwNsxTAlarmManagementAlarmServiceOverloaded": vmwNsxTAlarmManagementAlarmServiceOverloaded,
       "vmwNsxTAlarmManagementAlarmServiceOverloadedClear": vmwNsxTAlarmManagementAlarmServiceOverloadedClear,
       "vmwNsxTAlarmManagementHeavyVolumeOfAlarms": vmwNsxTAlarmManagementHeavyVolumeOfAlarms,
       "vmwNsxTAlarmManagementHeavyVolumeOfAlarmsClear": vmwNsxTAlarmManagementHeavyVolumeOfAlarmsClear,
       "vmwNsxTLoadBalancerFeaturePrefix": vmwNsxTLoadBalancerFeaturePrefix,
       "vmwNsxTLoadBalancerFeature": vmwNsxTLoadBalancerFeature,
       "vmwNsxTLoadBalancerLBCPUVeryHigh": vmwNsxTLoadBalancerLBCPUVeryHigh,
       "vmwNsxTLoadBalancerLBCPUVeryHighClear": vmwNsxTLoadBalancerLBCPUVeryHighClear,
       "vmwNsxTLoadBalancerLBEdgeCapacityInUseHigh": vmwNsxTLoadBalancerLBEdgeCapacityInUseHigh,
       "vmwNsxTLoadBalancerLBEdgeCapacityInUseHighClear": vmwNsxTLoadBalancerLBEdgeCapacityInUseHighClear,
       "vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHigh": vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHigh,
       "vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHighClear": vmwNsxTLoadBalancerLBPoolMemberCapacityInUseVeryHighClear,
       "vmwNsxTLoadBalancerLBStatusDown": vmwNsxTLoadBalancerLBStatusDown,
       "vmwNsxTLoadBalancerLBStatusDownClear": vmwNsxTLoadBalancerLBStatusDownClear,
       "vmwNsxTLoadBalancerPoolStatusDown": vmwNsxTLoadBalancerPoolStatusDown,
       "vmwNsxTLoadBalancerPoolStatusDownClear": vmwNsxTLoadBalancerPoolStatusDownClear,
       "vmwNsxTLoadBalancerVirtualServerStatusDown": vmwNsxTLoadBalancerVirtualServerStatusDown,
       "vmwNsxTLoadBalancerVirtualServerStatusDownClear": vmwNsxTLoadBalancerVirtualServerStatusDownClear,
       "vmwNsxTLoadBalancerLBStatusDegraded": vmwNsxTLoadBalancerLBStatusDegraded,
       "vmwNsxTLoadBalancerLBStatusDegradedClear": vmwNsxTLoadBalancerLBStatusDegradedClear,
       "vmwNsxTLoadBalancerDLBStatusDown": vmwNsxTLoadBalancerDLBStatusDown,
       "vmwNsxTLoadBalancerDLBStatusDownClear": vmwNsxTLoadBalancerDLBStatusDownClear,
       "vmwNsxTLoadBalancerConfigurationNotRealizedDueToLowMemory": vmwNsxTLoadBalancerConfigurationNotRealizedDueToLowMemory,
       "vmwNsxTLoadBalancerConfigurationNotRealizedDueToLowMemoryClear": vmwNsxTLoadBalancerConfigurationNotRealizedDueToLowMemoryClear,
       "vmwNsxTTransportNodeHealthFeaturePrefix": vmwNsxTTransportNodeHealthFeaturePrefix,
       "vmwNsxTTransportNodeHealthFeature": vmwNsxTTransportNodeHealthFeature,
       "vmwNsxTTransportNodeHealthNVDSUplinkDown": vmwNsxTTransportNodeHealthNVDSUplinkDown,
       "vmwNsxTTransportNodeHealthNVDSUplinkDownClear": vmwNsxTTransportNodeHealthNVDSUplinkDownClear,
       "vmwNsxTTransportNodeHealthLAGMemberDown": vmwNsxTTransportNodeHealthLAGMemberDown,
       "vmwNsxTTransportNodeHealthLAGMemberDownClear": vmwNsxTTransportNodeHealthLAGMemberDownClear,
       "vmwNsxTTransportNodeHealthTransportNodeUplinkDown": vmwNsxTTransportNodeHealthTransportNodeUplinkDown,
       "vmwNsxTTransportNodeHealthTransportNodeUplinkDownClear": vmwNsxTTransportNodeHealthTransportNodeUplinkDownClear,
       "vmwNsxTInfrastructureServiceFeaturePrefix": vmwNsxTInfrastructureServiceFeaturePrefix,
       "vmwNsxTInfrastructureServiceFeature": vmwNsxTInfrastructureServiceFeature,
       "vmwNsxTInfrastructureServiceEdgeServiceStatusChanged": vmwNsxTInfrastructureServiceEdgeServiceStatusChanged,
       "vmwNsxTInfrastructureServiceEdgeServiceStatusChangedClear": vmwNsxTInfrastructureServiceEdgeServiceStatusChangedClear,
       "vmwNsxTInfrastructureServiceEdgeServiceStatusDown": vmwNsxTInfrastructureServiceEdgeServiceStatusDown,
       "vmwNsxTInfrastructureServiceEdgeServiceStatusDownClear": vmwNsxTInfrastructureServiceEdgeServiceStatusDownClear,
       "vmwNsxTInfrastructureServiceServiceStatusUnknown": vmwNsxTInfrastructureServiceServiceStatusUnknown,
       "vmwNsxTInfrastructureServiceServiceStatusUnknownClear": vmwNsxTInfrastructureServiceServiceStatusUnknownClear,
       "vmwNsxTDHCPFeaturePrefix": vmwNsxTDHCPFeaturePrefix,
       "vmwNsxTDHCPFeature": vmwNsxTDHCPFeature,
       "vmwNsxTDHCPPoolLeaseAllocationFailed": vmwNsxTDHCPPoolLeaseAllocationFailed,
       "vmwNsxTDHCPPoolLeaseAllocationFailedClear": vmwNsxTDHCPPoolLeaseAllocationFailedClear,
       "vmwNsxTDHCPPoolOverloaded": vmwNsxTDHCPPoolOverloaded,
       "vmwNsxTDHCPPoolOverloadedClear": vmwNsxTDHCPPoolOverloadedClear,
       "vmwNsxTHighAvailabilityFeaturePrefix": vmwNsxTHighAvailabilityFeaturePrefix,
       "vmwNsxTHighAvailabilityFeature": vmwNsxTHighAvailabilityFeature,
       "vmwNsxTHighAvailabilityTier0GatewayFailover": vmwNsxTHighAvailabilityTier0GatewayFailover,
       "vmwNsxTHighAvailabilityTier0GatewayFailoverClear": vmwNsxTHighAvailabilityTier0GatewayFailoverClear,
       "vmwNsxTHighAvailabilityTier1GatewayFailover": vmwNsxTHighAvailabilityTier1GatewayFailover,
       "vmwNsxTHighAvailabilityTier1GatewayFailoverClear": vmwNsxTHighAvailabilityTier1GatewayFailoverClear,
       "vmwNsxTCapacityFeaturePrefix": vmwNsxTCapacityFeaturePrefix,
       "vmwNsxTCapacityFeature": vmwNsxTCapacityFeature,
       "vmwNsxTCapacityMaximumCapacity": vmwNsxTCapacityMaximumCapacity,
       "vmwNsxTCapacityMaximumCapacityClear": vmwNsxTCapacityMaximumCapacityClear,
       "vmwNsxTCapacityMaximumCapacityThreshold": vmwNsxTCapacityMaximumCapacityThreshold,
       "vmwNsxTCapacityMaximumCapacityThresholdClear": vmwNsxTCapacityMaximumCapacityThresholdClear,
       "vmwNsxTCapacityMinimumCapacityThreshold": vmwNsxTCapacityMinimumCapacityThreshold,
       "vmwNsxTCapacityMinimumCapacityThresholdClear": vmwNsxTCapacityMinimumCapacityThresholdClear,
       "vmwNsxTAuditLogHealthFeaturePrefix": vmwNsxTAuditLogHealthFeaturePrefix,
       "vmwNsxTAuditLogHealthFeature": vmwNsxTAuditLogHealthFeature,
       "vmwNsxTAuditLogHealthAuditLogFileUpdateError": vmwNsxTAuditLogHealthAuditLogFileUpdateError,
       "vmwNsxTAuditLogHealthAuditLogFileUpdateErrorClear": vmwNsxTAuditLogHealthAuditLogFileUpdateErrorClear,
       "vmwNsxTAuditLogHealthRemoteLoggingServerError": vmwNsxTAuditLogHealthRemoteLoggingServerError,
       "vmwNsxTAuditLogHealthRemoteLoggingServerErrorClear": vmwNsxTAuditLogHealthRemoteLoggingServerErrorClear,
       "vmwNsxTRoutingFeaturePrefix": vmwNsxTRoutingFeaturePrefix,
       "vmwNsxTRoutingFeature": vmwNsxTRoutingFeature,
       "vmwNsxTRoutingBGPDown": vmwNsxTRoutingBGPDown,
       "vmwNsxTRoutingBGPDownClear": vmwNsxTRoutingBGPDownClear,
       "vmwNsxTRoutingStaticRoutingRemoved": vmwNsxTRoutingStaticRoutingRemoved,
       "vmwNsxTRoutingStaticRoutingRemovedClear": vmwNsxTRoutingStaticRoutingRemovedClear,
       "vmwNsxTRoutingBFDDownOnExternalInterface": vmwNsxTRoutingBFDDownOnExternalInterface,
       "vmwNsxTRoutingBFDDownOnExternalInterfaceClear": vmwNsxTRoutingBFDDownOnExternalInterfaceClear,
       "vmwNsxTRoutingRoutingDown": vmwNsxTRoutingRoutingDown,
       "vmwNsxTRoutingRoutingDownClear": vmwNsxTRoutingRoutingDownClear,
       "vmwNsxTRoutingOSPFNeighborWentDown": vmwNsxTRoutingOSPFNeighborWentDown,
       "vmwNsxTRoutingOSPFNeighborWentDownClear": vmwNsxTRoutingOSPFNeighborWentDownClear,
       "vmwNsxTRoutingProxyARPNotConfiguredForServiceIP": vmwNsxTRoutingProxyARPNotConfiguredForServiceIP,
       "vmwNsxTRoutingProxyARPNotConfiguredForServiceIPClear": vmwNsxTRoutingProxyARPNotConfiguredForServiceIPClear,
       "vmwNsxTDNSFeaturePrefix": vmwNsxTDNSFeaturePrefix,
       "vmwNsxTDNSFeature": vmwNsxTDNSFeature,
       "vmwNsxTDNSForwarderDisabled": vmwNsxTDNSForwarderDisabled,
       "vmwNsxTDNSForwarderDisabledClear": vmwNsxTDNSForwarderDisabledClear,
       "vmwNsxTDNSForwarderDown": vmwNsxTDNSForwarderDown,
       "vmwNsxTDNSForwarderDownClear": vmwNsxTDNSForwarderDownClear,
       "vmwNsxTDNSForwarderUpstreamServerTimeout": vmwNsxTDNSForwarderUpstreamServerTimeout,
       "vmwNsxTDNSForwarderUpstreamServerTimeoutClear": vmwNsxTDNSForwarderUpstreamServerTimeoutClear,
       "vmwNsxTDistributedFirewallFeaturePrefix": vmwNsxTDistributedFirewallFeaturePrefix,
       "vmwNsxTDistributedFirewallFeature": vmwNsxTDistributedFirewallFeature,
       "vmwNsxTDistributedFirewallDFWCPUUsageVeryHigh": vmwNsxTDistributedFirewallDFWCPUUsageVeryHigh,
       "vmwNsxTDistributedFirewallDFWCPUUsageVeryHighClear": vmwNsxTDistributedFirewallDFWCPUUsageVeryHighClear,
       "vmwNsxTDistributedFirewallDFWMemoryUsageVeryHigh": vmwNsxTDistributedFirewallDFWMemoryUsageVeryHigh,
       "vmwNsxTDistributedFirewallDFWMemoryUsageVeryHighClear": vmwNsxTDistributedFirewallDFWMemoryUsageVeryHighClear,
       "vmwNsxTDistributedFirewallDFWSessionCountHigh": vmwNsxTDistributedFirewallDFWSessionCountHigh,
       "vmwNsxTDistributedFirewallDFWSessionCountHighClear": vmwNsxTDistributedFirewallDFWSessionCountHighClear,
       "vmwNsxTDistributedFirewallDFWVmotionFailure": vmwNsxTDistributedFirewallDFWVmotionFailure,
       "vmwNsxTDistributedFirewallDFWVmotionFailureClear": vmwNsxTDistributedFirewallDFWVmotionFailureClear,
       "vmwNsxTFederationFeaturePrefix": vmwNsxTFederationFeaturePrefix,
       "vmwNsxTFederationFeature": vmwNsxTFederationFeature,
       "vmwNsxTFederationRtepBGPDown": vmwNsxTFederationRtepBGPDown,
       "vmwNsxTFederationRtepBGPDownClear": vmwNsxTFederationRtepBGPDownClear,
       "vmwNsxTFederationLmToLmSynchronizationError": vmwNsxTFederationLmToLmSynchronizationError,
       "vmwNsxTFederationLmToLmSynchronizationErrorClear": vmwNsxTFederationLmToLmSynchronizationErrorClear,
       "vmwNsxTFederationLmToLmSynchronizationWarning": vmwNsxTFederationLmToLmSynchronizationWarning,
       "vmwNsxTFederationLmToLmSynchronizationWarningClear": vmwNsxTFederationLmToLmSynchronizationWarningClear,
       "vmwNsxTFederationRtepConnectivityLost": vmwNsxTFederationRtepConnectivityLost,
       "vmwNsxTFederationRtepConnectivityLostClear": vmwNsxTFederationRtepConnectivityLostClear,
       "vmwNsxTFederationGMToGMSplitBrain": vmwNsxTFederationGMToGMSplitBrain,
       "vmwNsxTFederationGMToGMSplitBrainClear": vmwNsxTFederationGMToGMSplitBrainClear,
       "vmwNsxTFederationGMToGMLatencyWarning": vmwNsxTFederationGMToGMLatencyWarning,
       "vmwNsxTFederationGMToGMLatencyWarningClear": vmwNsxTFederationGMToGMLatencyWarningClear,
       "vmwNsxTFederationGMToGMSynchronizationError": vmwNsxTFederationGMToGMSynchronizationError,
       "vmwNsxTFederationGMToGMSynchronizationErrorClear": vmwNsxTFederationGMToGMSynchronizationErrorClear,
       "vmwNsxTFederationGMToGMSynchronizationWarning": vmwNsxTFederationGMToGMSynchronizationWarning,
       "vmwNsxTFederationGMToGMSynchronizationWarningClear": vmwNsxTFederationGMToGMSynchronizationWarningClear,
       "vmwNsxTFederationGMToLMSynchronizationError": vmwNsxTFederationGMToLMSynchronizationError,
       "vmwNsxTFederationGMToLMSynchronizationErrorClear": vmwNsxTFederationGMToLMSynchronizationErrorClear,
       "vmwNsxTFederationGMToLMSynchronizationWarning": vmwNsxTFederationGMToLMSynchronizationWarning,
       "vmwNsxTFederationGMToLMSynchronizationWarningClear": vmwNsxTFederationGMToLMSynchronizationWarningClear,
       "vmwNsxTFederationGMToLMLatencyWarning": vmwNsxTFederationGMToLMLatencyWarning,
       "vmwNsxTFederationGMToLMLatencyWarningClear": vmwNsxTFederationGMToLMLatencyWarningClear,
       "vmwNsxTFederationQueueOccupancyThresholdExceeded": vmwNsxTFederationQueueOccupancyThresholdExceeded,
       "vmwNsxTFederationQueueOccupancyThresholdExceededClear": vmwNsxTFederationQueueOccupancyThresholdExceededClear,
       "vmwNsxTFederationLMRestoreWhileConfigImportInProgress": vmwNsxTFederationLMRestoreWhileConfigImportInProgress,
       "vmwNsxTFederationLMRestoreWhileConfigImportInProgressClear": vmwNsxTFederationLMRestoreWhileConfigImportInProgressClear,
       "vmwNsxTDistributedIDSIPSFeaturePrefix": vmwNsxTDistributedIDSIPSFeaturePrefix,
       "vmwNsxTDistributedIDSIPSFeature": vmwNsxTDistributedIDSIPSFeature,
       "vmwNsxTDistributedIDSIPSMaxEventsReached": vmwNsxTDistributedIDSIPSMaxEventsReached,
       "vmwNsxTDistributedIDSIPSMaxEventsReachedClear": vmwNsxTDistributedIDSIPSMaxEventsReachedClear,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHigh": vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHigh,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHighClear": vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageHighClear,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHigh": vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHigh,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHighClear": vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageVeryHighClear,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineDown": vmwNsxTDistributedIDSIPSNSXIDPSEngineDown,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineDownClear": vmwNsxTDistributedIDSIPSNSXIDPSEngineDownClear,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHigh": vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHigh,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHighClear": vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageHighClear,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHigh": vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHigh,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHighClear": vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageMediumHighClear,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHigh": vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHigh,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHighClear": vmwNsxTDistributedIDSIPSNSXIDPSEngineMemoryUsageVeryHighClear,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHigh": vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHigh,
       "vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHighClear": vmwNsxTDistributedIDSIPSNSXIDPSEngineCPUUsageMediumHighClear,
       "vmwNsxTCommunicationFeaturePrefix": vmwNsxTCommunicationFeaturePrefix,
       "vmwNsxTCommunicationFeature": vmwNsxTCommunicationFeature,
       "vmwNsxTCommunicationManagementChannelToTransportNodeDown": vmwNsxTCommunicationManagementChannelToTransportNodeDown,
       "vmwNsxTCommunicationManagementChannelToTransportNodeDownClear": vmwNsxTCommunicationManagementChannelToTransportNodeDownClear,
       "vmwNsxTCommunicationManagerControlChannelDown": vmwNsxTCommunicationManagerControlChannelDown,
       "vmwNsxTCommunicationManagerControlChannelDownClear": vmwNsxTCommunicationManagerControlChannelDownClear,
       "vmwNsxTCommunicationManagementChannelToTransportNodeDownLg": vmwNsxTCommunicationManagementChannelToTransportNodeDownLg,
       "vmwNsxTCommunicationManagementChannelToTransportNodeDownLgClear": vmwNsxTCommunicationManagementChannelToTransportNodeDownLgClear,
       "vmwNsxTCommunicationControlChannelToManagerNodeDown": vmwNsxTCommunicationControlChannelToManagerNodeDown,
       "vmwNsxTCommunicationControlChannelToManagerNodeDownClear": vmwNsxTCommunicationControlChannelToManagerNodeDownClear,
       "vmwNsxTCommunicationControlChannelToManagerNodeDownTooLong": vmwNsxTCommunicationControlChannelToManagerNodeDownTooLong,
       "vmwNsxTCommunicationControlChannelToManagerNodeDownTooLongClear": vmwNsxTCommunicationControlChannelToManagerNodeDownTooLongClear,
       "vmwNsxTCommunicationControlChannelToTransportNodeDown": vmwNsxTCommunicationControlChannelToTransportNodeDown,
       "vmwNsxTCommunicationControlChannelToTransportNodeDownClear": vmwNsxTCommunicationControlChannelToTransportNodeDownClear,
       "vmwNsxTCommunicationManagementChannelToManagerNodeDown": vmwNsxTCommunicationManagementChannelToManagerNodeDown,
       "vmwNsxTCommunicationManagementChannelToManagerNodeDownClear": vmwNsxTCommunicationManagementChannelToManagerNodeDownClear,
       "vmwNsxTCommunicationManagerClusterLatencyHigh": vmwNsxTCommunicationManagerClusterLatencyHigh,
       "vmwNsxTCommunicationManagerClusterLatencyHighClear": vmwNsxTCommunicationManagerClusterLatencyHighClear,
       "vmwNsxTCommunicationControlChannelToTransportNodeDownLong": vmwNsxTCommunicationControlChannelToTransportNodeDownLong,
       "vmwNsxTCommunicationControlChannelToTransportNodeDownLongClear": vmwNsxTCommunicationControlChannelToTransportNodeDownLongClear,
       "vmwNsxTCommunicationManagerFQDNLookupFailure": vmwNsxTCommunicationManagerFQDNLookupFailure,
       "vmwNsxTCommunicationManagerFQDNLookupFailureClear": vmwNsxTCommunicationManagerFQDNLookupFailureClear,
       "vmwNsxTCommunicationManagerFQDNReverseLookupFailure": vmwNsxTCommunicationManagerFQDNReverseLookupFailure,
       "vmwNsxTCommunicationManagerFQDNReverseLookupFailureClear": vmwNsxTCommunicationManagerFQDNReverseLookupFailureClear,
       "vmwNsxTCommunicationManagementChannelToManagerNodeDownLong": vmwNsxTCommunicationManagementChannelToManagerNodeDownLong,
       "vmwNsxTCommunicationManagementChannelToManagerNodeDownLongClear": vmwNsxTCommunicationManagementChannelToManagerNodeDownLongClear,
       "vmwNsxTIdentityFirewallFeaturePrefix": vmwNsxTIdentityFirewallFeaturePrefix,
       "vmwNsxTIdentityFirewallFeature": vmwNsxTIdentityFirewallFeature,
       "vmwNsxTIdentityFirewallConnectivityToLDAPServerLost": vmwNsxTIdentityFirewallConnectivityToLDAPServerLost,
       "vmwNsxTIdentityFirewallConnectivityToLDAPServerLostClear": vmwNsxTIdentityFirewallConnectivityToLDAPServerLostClear,
       "vmwNsxTIdentityFirewallErrorInDeltaSync": vmwNsxTIdentityFirewallErrorInDeltaSync,
       "vmwNsxTIdentityFirewallErrorInDeltaSyncClear": vmwNsxTIdentityFirewallErrorInDeltaSyncClear,
       "vmwNsxTIPAMFeaturePrefix": vmwNsxTIPAMFeaturePrefix,
       "vmwNsxTIPAMFeature": vmwNsxTIPAMFeature,
       "vmwNsxTIPAMIPBlockUsageVeryHigh": vmwNsxTIPAMIPBlockUsageVeryHigh,
       "vmwNsxTIPAMIPBlockUsageVeryHighClear": vmwNsxTIPAMIPBlockUsageVeryHighClear,
       "vmwNsxTIPAMIPPoolUsageVeryHigh": vmwNsxTIPAMIPPoolUsageVeryHigh,
       "vmwNsxTIPAMIPPoolUsageVeryHighClear": vmwNsxTIPAMIPPoolUsageVeryHighClear,
       "vmwNsxTGatewayFirewallFeaturePrefix": vmwNsxTGatewayFirewallFeaturePrefix,
       "vmwNsxTGatewayFirewallFeature": vmwNsxTGatewayFirewallFeature,
       "vmwNsxTGatewayFirewallICMPFlowCountExceeded": vmwNsxTGatewayFirewallICMPFlowCountExceeded,
       "vmwNsxTGatewayFirewallICMPFlowCountExceededClear": vmwNsxTGatewayFirewallICMPFlowCountExceededClear,
       "vmwNsxTGatewayFirewallICMPFlowCountHigh": vmwNsxTGatewayFirewallICMPFlowCountHigh,
       "vmwNsxTGatewayFirewallICMPFlowCountHighClear": vmwNsxTGatewayFirewallICMPFlowCountHighClear,
       "vmwNsxTGatewayFirewallIPFlowCountExceeded": vmwNsxTGatewayFirewallIPFlowCountExceeded,
       "vmwNsxTGatewayFirewallIPFlowCountExceededClear": vmwNsxTGatewayFirewallIPFlowCountExceededClear,
       "vmwNsxTGatewayFirewallIPFlowCountHigh": vmwNsxTGatewayFirewallIPFlowCountHigh,
       "vmwNsxTGatewayFirewallIPFlowCountHighClear": vmwNsxTGatewayFirewallIPFlowCountHighClear,
       "vmwNsxTGatewayFirewallTcpHalfOpenFlowCountExceeded": vmwNsxTGatewayFirewallTcpHalfOpenFlowCountExceeded,
       "vmwNsxTGatewayFirewallTcpHalfOpenFlowCountExceededClear": vmwNsxTGatewayFirewallTcpHalfOpenFlowCountExceededClear,
       "vmwNsxTGatewayFirewallTcpHalfOpenFlowCountHigh": vmwNsxTGatewayFirewallTcpHalfOpenFlowCountHigh,
       "vmwNsxTGatewayFirewallTcpHalfOpenFlowCountHighClear": vmwNsxTGatewayFirewallTcpHalfOpenFlowCountHighClear,
       "vmwNsxTGatewayFirewallUDPFlowCountExceeded": vmwNsxTGatewayFirewallUDPFlowCountExceeded,
       "vmwNsxTGatewayFirewallUDPFlowCountExceededClear": vmwNsxTGatewayFirewallUDPFlowCountExceededClear,
       "vmwNsxTGatewayFirewallUDPFlowCountHigh": vmwNsxTGatewayFirewallUDPFlowCountHigh,
       "vmwNsxTGatewayFirewallUDPFlowCountHighClear": vmwNsxTGatewayFirewallUDPFlowCountHighClear,
       "vmwNsxTClusteringFeaturePrefix": vmwNsxTClusteringFeaturePrefix,
       "vmwNsxTClusteringFeature": vmwNsxTClusteringFeature,
       "vmwNsxTClusteringClusterDegraded": vmwNsxTClusteringClusterDegraded,
       "vmwNsxTClusteringClusterDegradedClear": vmwNsxTClusteringClusterDegradedClear,
       "vmwNsxTClusteringClusterUnavailable": vmwNsxTClusteringClusterUnavailable,
       "vmwNsxTClusteringClusterUnavailableClear": vmwNsxTClusteringClusterUnavailableClear,
       "vmwNsxTNSXApplicationPlatformCommunicationFeaturePrefix": vmwNsxTNSXApplicationPlatformCommunicationFeaturePrefix,
       "vmwNsxTNSXApplicationPlatformCommunicationFeature": vmwNsxTNSXApplicationPlatformCommunicationFeature,
       "vmwNsxTNSXApplicationPlatformCommunicationMgrDisconnected": vmwNsxTNSXApplicationPlatformCommunicationMgrDisconnected,
       "vmwNsxTNSXApplicationPlatformCommunicationMgrDisconnectedClear": vmwNsxTNSXApplicationPlatformCommunicationMgrDisconnectedClear,
       "vmwNsxTNSXApplicationPlatformCommunicationDelayInOverflow": vmwNsxTNSXApplicationPlatformCommunicationDelayInOverflow,
       "vmwNsxTNSXApplicationPlatformCommunicationDelayInOverflowClear": vmwNsxTNSXApplicationPlatformCommunicationDelayInOverflowClear,
       "vmwNsxTNSXApplicationPlatformCommunicationDelayInRawflow": vmwNsxTNSXApplicationPlatformCommunicationDelayInRawflow,
       "vmwNsxTNSXApplicationPlatformCommunicationDelayInRawflowClear": vmwNsxTNSXApplicationPlatformCommunicationDelayInRawflowClear,
       "vmwNsxTNSXApplicationPlatformCommunicationExpDisconnected": vmwNsxTNSXApplicationPlatformCommunicationExpDisconnected,
       "vmwNsxTNSXApplicationPlatformCommunicationExpDisconnectedClear": vmwNsxTNSXApplicationPlatformCommunicationExpDisconnectedClear,
       "vmwNsxTMTUCheckFeaturePrefix": vmwNsxTMTUCheckFeaturePrefix,
       "vmwNsxTMTUCheckFeature": vmwNsxTMTUCheckFeature,
       "vmwNsxTMTUCheckMTUMismatchWithinTransportZone": vmwNsxTMTUCheckMTUMismatchWithinTransportZone,
       "vmwNsxTMTUCheckMTUMismatchWithinTransportZoneClear": vmwNsxTMTUCheckMTUMismatchWithinTransportZoneClear,
       "vmwNsxTMTUCheckGlobalRouterMTUTooBig": vmwNsxTMTUCheckGlobalRouterMTUTooBig,
       "vmwNsxTMTUCheckGlobalRouterMTUTooBigClear": vmwNsxTMTUCheckGlobalRouterMTUTooBigClear,
       "vmwNsxTNSXApplicationPlatformHealthFeaturePrefix": vmwNsxTNSXApplicationPlatformHealthFeaturePrefix,
       "vmwNsxTNSXApplicationPlatformHealthFeature": vmwNsxTNSXApplicationPlatformHealthFeature,
       "vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageHigh": vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageHighClear": vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageVeryHi": vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageVeryHi,
       "vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageVeryHiClear": vmwNsxTNSXApplicationPlatformHealthAnalyticsCPUUsageVeryHiClear,
       "vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageHigh": vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageHighClear": vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageVeryHi": vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageVeryHi,
       "vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageVeryHiClear": vmwNsxTNSXApplicationPlatformHealthAnalyticsDiskUsageVeryHiClear,
       "vmwNsxTNSXApplicationPlatformHealthAnalyticsMemoryUsageHigh": vmwNsxTNSXApplicationPlatformHealthAnalyticsMemoryUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthAnalyticsMemoryUsageHighClear": vmwNsxTNSXApplicationPlatformHealthAnalyticsMemoryUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthAnalyticsMemUsageVeryHi": vmwNsxTNSXApplicationPlatformHealthAnalyticsMemUsageVeryHi,
       "vmwNsxTNSXApplicationPlatformHealthAnalyticsMemUsageVeryHiClear": vmwNsxTNSXApplicationPlatformHealthAnalyticsMemUsageVeryHiClear,
       "vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageHigh": vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageHighClear": vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageVeryHigh": vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageVeryHigh,
       "vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageVeryHighClear": vmwNsxTNSXApplicationPlatformHealthClusterCPUUsageVeryHighClear,
       "vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageHigh": vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageHighClear": vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageVeryHigh": vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageVeryHigh,
       "vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageVeryHighClear": vmwNsxTNSXApplicationPlatformHealthClusterDiskUsageVeryHighClear,
       "vmwNsxTNSXApplicationPlatformHealthClusterMemoryUsageHigh": vmwNsxTNSXApplicationPlatformHealthClusterMemoryUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthClusterMemoryUsageHighClear": vmwNsxTNSXApplicationPlatformHealthClusterMemoryUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthClusterMemUsageVeryHi": vmwNsxTNSXApplicationPlatformHealthClusterMemUsageVeryHi,
       "vmwNsxTNSXApplicationPlatformHealthClusterMemUsageVeryHiClear": vmwNsxTNSXApplicationPlatformHealthClusterMemUsageVeryHiClear,
       "vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageHi": vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageHi,
       "vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageHiClear": vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageHiClear,
       "vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageVeryHi": vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageVeryHi,
       "vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageVeryHiClear": vmwNsxTNSXApplicationPlatformHealthConfigDbCPUUsageVeryHiClear,
       "vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageHigh": vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageHighClear": vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageVeryHi": vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageVeryHi,
       "vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageVeryHiClear": vmwNsxTNSXApplicationPlatformHealthConfigDbDiskUsageVeryHiClear,
       "vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageVeryHigh": vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageVeryHigh,
       "vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageVeryHighClear": vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageVeryHighClear,
       "vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageHigh": vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageHighClear": vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageVeryHi": vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageVeryHi,
       "vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageVeryHiClear": vmwNsxTNSXApplicationPlatformHealthDatastoreCPUUsageVeryHiClear,
       "vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageHigh": vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageHighClear": vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageVeryHi": vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageVeryHi,
       "vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageVeryHiClear": vmwNsxTNSXApplicationPlatformHealthDatastoreDiskUsageVeryHiClear,
       "vmwNsxTNSXApplicationPlatformHealthDatastoreMemoryUsageHigh": vmwNsxTNSXApplicationPlatformHealthDatastoreMemoryUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthDatastoreMemoryUsageHighClear": vmwNsxTNSXApplicationPlatformHealthDatastoreMemoryUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthDatastoreMemUsageVeryHi": vmwNsxTNSXApplicationPlatformHealthDatastoreMemUsageVeryHi,
       "vmwNsxTNSXApplicationPlatformHealthDatastoreMemUsageVeryHiClear": vmwNsxTNSXApplicationPlatformHealthDatastoreMemUsageVeryHiClear,
       "vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageHigh": vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageHighClear": vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageVeryHi": vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageVeryHi,
       "vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageVeryHiClear": vmwNsxTNSXApplicationPlatformHealthMessagingCPUUsageVeryHiClear,
       "vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageHigh": vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageHighClear": vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageVeryHi": vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageVeryHi,
       "vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageVeryHiClear": vmwNsxTNSXApplicationPlatformHealthMessagingDiskUsageVeryHiClear,
       "vmwNsxTNSXApplicationPlatformHealthMessagingMemoryUsageHigh": vmwNsxTNSXApplicationPlatformHealthMessagingMemoryUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthMessagingMemoryUsageHighClear": vmwNsxTNSXApplicationPlatformHealthMessagingMemoryUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthMessagingMemUsageVeryHi": vmwNsxTNSXApplicationPlatformHealthMessagingMemUsageVeryHi,
       "vmwNsxTNSXApplicationPlatformHealthMessagingMemUsageVeryHiClear": vmwNsxTNSXApplicationPlatformHealthMessagingMemUsageVeryHiClear,
       "vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageHigh": vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageHighClear": vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageVeryHigh": vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageVeryHigh,
       "vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageVeryHighClear": vmwNsxTNSXApplicationPlatformHealthNodeCPUUsageVeryHighClear,
       "vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageHigh": vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageHighClear": vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageVeryHigh": vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageVeryHigh,
       "vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageVeryHighClear": vmwNsxTNSXApplicationPlatformHealthNodeDiskUsageVeryHighClear,
       "vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageHigh": vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageHighClear": vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageVeryHigh": vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageVeryHigh,
       "vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageVeryHighClear": vmwNsxTNSXApplicationPlatformHealthNodeMemoryUsageVeryHighClear,
       "vmwNsxTNSXApplicationPlatformHealthNodeStatusDegraded": vmwNsxTNSXApplicationPlatformHealthNodeStatusDegraded,
       "vmwNsxTNSXApplicationPlatformHealthNodeStatusDegradedClear": vmwNsxTNSXApplicationPlatformHealthNodeStatusDegradedClear,
       "vmwNsxTNSXApplicationPlatformHealthNodeStatusDown": vmwNsxTNSXApplicationPlatformHealthNodeStatusDown,
       "vmwNsxTNSXApplicationPlatformHealthNodeStatusDownClear": vmwNsxTNSXApplicationPlatformHealthNodeStatusDownClear,
       "vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageHigh": vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageHighClear": vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageVeryHigh": vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageVeryHigh,
       "vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageVeryHighClear": vmwNsxTNSXApplicationPlatformHealthPlatformCPUUsageVeryHighClear,
       "vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageHigh": vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageHighClear": vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageVeryHi": vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageVeryHi,
       "vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageVeryHiClear": vmwNsxTNSXApplicationPlatformHealthPlatformDiskUsageVeryHiClear,
       "vmwNsxTNSXApplicationPlatformHealthPlatformMemoryUsageHigh": vmwNsxTNSXApplicationPlatformHealthPlatformMemoryUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthPlatformMemoryUsageHighClear": vmwNsxTNSXApplicationPlatformHealthPlatformMemoryUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthPlatformMemUsageVeryHi": vmwNsxTNSXApplicationPlatformHealthPlatformMemUsageVeryHi,
       "vmwNsxTNSXApplicationPlatformHealthPlatformMemUsageVeryHiClear": vmwNsxTNSXApplicationPlatformHealthPlatformMemUsageVeryHiClear,
       "vmwNsxTNSXApplicationPlatformHealthServiceStatusDegraded": vmwNsxTNSXApplicationPlatformHealthServiceStatusDegraded,
       "vmwNsxTNSXApplicationPlatformHealthServiceStatusDegradedClear": vmwNsxTNSXApplicationPlatformHealthServiceStatusDegradedClear,
       "vmwNsxTNSXApplicationPlatformHealthServiceStatusDown": vmwNsxTNSXApplicationPlatformHealthServiceStatusDown,
       "vmwNsxTNSXApplicationPlatformHealthServiceStatusDownClear": vmwNsxTNSXApplicationPlatformHealthServiceStatusDownClear,
       "vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageHigh": vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageHighClear": vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageVeryHigh": vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageVeryHigh,
       "vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageVeryHighClear": vmwNsxTNSXApplicationPlatformHealthMetricsCPUUsageVeryHighClear,
       "vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageHi": vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageHi,
       "vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageHiClear": vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageHiClear,
       "vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageVeryHigh": vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageVeryHigh,
       "vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageVeryHighClear": vmwNsxTNSXApplicationPlatformHealthMetricsDiskUsageVeryHighClear,
       "vmwNsxTNSXApplicationPlatformHealthMetricsMemUasgeHi": vmwNsxTNSXApplicationPlatformHealthMetricsMemUasgeHi,
       "vmwNsxTNSXApplicationPlatformHealthMetricsMemUasgeHiClear": vmwNsxTNSXApplicationPlatformHealthMetricsMemUasgeHiClear,
       "vmwNsxTNSXApplicationPlatformHealthMetricsMemUsageVeryHigh": vmwNsxTNSXApplicationPlatformHealthMetricsMemUsageVeryHigh,
       "vmwNsxTNSXApplicationPlatformHealthMetricsMemUsageVeryHighClear": vmwNsxTNSXApplicationPlatformHealthMetricsMemUsageVeryHighClear,
       "vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageHigh": vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageHigh,
       "vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageHighClear": vmwNsxTNSXApplicationPlatformHealthConfigDbMemUsageHighClear,
       "vmwNsxTNSXApplicationPlatformHealthNappStatusDegraded": vmwNsxTNSXApplicationPlatformHealthNappStatusDegraded,
       "vmwNsxTNSXApplicationPlatformHealthNappStatusDegradedClear": vmwNsxTNSXApplicationPlatformHealthNappStatusDegradedClear,
       "vmwNsxTNSXApplicationPlatformHealthNappStatusDown": vmwNsxTNSXApplicationPlatformHealthNappStatusDown,
       "vmwNsxTNSXApplicationPlatformHealthNappStatusDownClear": vmwNsxTNSXApplicationPlatformHealthNappStatusDownClear,
       "vmwNsxTEdgeFeaturePrefix": vmwNsxTEdgeFeaturePrefix,
       "vmwNsxTEdgeFeature": vmwNsxTEdgeFeature,
       "vmwNsxTEdgeEdgeNodeSettingsAndvSphereSettingsAreChanged": vmwNsxTEdgeEdgeNodeSettingsAndvSphereSettingsAreChanged,
       "vmwNsxTEdgeEdgeNodeSettingsAndvSphereSettingsAreChangedClear": vmwNsxTEdgeEdgeNodeSettingsAndvSphereSettingsAreChangedClear,
       "vmwNsxTEdgeEdgeNodeSettingsMismatch": vmwNsxTEdgeEdgeNodeSettingsMismatch,
       "vmwNsxTEdgeEdgeNodeSettingsMismatchClear": vmwNsxTEdgeEdgeNodeSettingsMismatchClear,
       "vmwNsxTEdgeEdgeVmvSphereSettingsMismatch": vmwNsxTEdgeEdgeVmvSphereSettingsMismatch,
       "vmwNsxTEdgeEdgeVmvSphereSettingsMismatchClear": vmwNsxTEdgeEdgeVmvSphereSettingsMismatchClear,
       "vmwNsxTEdgeEdgevSphereLocationMismatch": vmwNsxTEdgeEdgevSphereLocationMismatch,
       "vmwNsxTEdgeEdgevSphereLocationMismatchClear": vmwNsxTEdgeEdgevSphereLocationMismatchClear,
       "vmwNsxTNATFeaturePrefix": vmwNsxTNATFeaturePrefix,
       "vmwNsxTNATFeature": vmwNsxTNATFeature,
       "vmwNsxTNATSNATPortUsageOnGatewayIsHigh": vmwNsxTNATSNATPortUsageOnGatewayIsHigh,
       "vmwNsxTNATSNATPortUsageOnGatewayIsHighClear": vmwNsxTNATSNATPortUsageOnGatewayIsHighClear,
       "vmwNsxTDataCenterData": vmwNsxTDataCenterData,
       "vmwNsxTDataCenterTimestamp": vmwNsxTDataCenterTimestamp,
       "vmwNsxTDataCenterFeatureName": vmwNsxTDataCenterFeatureName,
       "vmwNsxTDataCenterEventType": vmwNsxTDataCenterEventType,
       "vmwNsxTDataCenterEventSeverity": vmwNsxTDataCenterEventSeverity,
       "vmwNsxTDataCenterNodeId": vmwNsxTDataCenterNodeId,
       "vmwNsxTDataCenterNodeType": vmwNsxTDataCenterNodeType,
       "vmwNsxTDataCenterEntityId": vmwNsxTDataCenterEntityId,
       "vmwNsxTDataCenterSystemResourceUsage": vmwNsxTDataCenterSystemResourceUsage,
       "vmwNsxTDataCenterDiskPartitionName": vmwNsxTDataCenterDiskPartitionName,
       "vmwNsxTDataCenterLicenseEditionType": vmwNsxTDataCenterLicenseEditionType,
       "vmwNsxTDataCenterApplianceAddress": vmwNsxTDataCenterApplianceAddress,
       "vmwNsxTDataCenterCurrentGatewayState": vmwNsxTDataCenterCurrentGatewayState,
       "vmwNsxTDataCenterCurrentServiceState": vmwNsxTDataCenterCurrentServiceState,
       "vmwNsxTDataCenterDatapathResourceUsage": vmwNsxTDataCenterDatapathResourceUsage,
       "vmwNsxTDataCenterDHCPPoolUsage": vmwNsxTDataCenterDHCPPoolUsage,
       "vmwNsxTDataCenterEdgeServiceName": vmwNsxTDataCenterEdgeServiceName,
       "vmwNsxTDataCenterFailureReason": vmwNsxTDataCenterFailureReason,
       "vmwNsxTDataCenterPreviousGatewayState": vmwNsxTDataCenterPreviousGatewayState,
       "vmwNsxTDataCenterPreviousServiceState": vmwNsxTDataCenterPreviousServiceState,
       "vmwNsxTDataCenterSystemUsageThreshold": vmwNsxTDataCenterSystemUsageThreshold,
       "vmwNsxTDataCenterUsername": vmwNsxTDataCenterUsername,
       "vmwNsxTDataCenterDHCPServerId": vmwNsxTDataCenterDHCPServerId,
       "vmwNsxTDataCenterServiceName": vmwNsxTDataCenterServiceName,
       "vmwNsxTDataCenterIntelligenceNodeId": vmwNsxTDataCenterIntelligenceNodeId,
       "vmwNsxTDataCenterHostnameOrIPAddressWithPort": vmwNsxTDataCenterHostnameOrIPAddressWithPort,
       "vmwNsxTDataCenterEventId": vmwNsxTDataCenterEventId,
       "vmwNsxTDataCenterActiveGlobalManager": vmwNsxTDataCenterActiveGlobalManager,
       "vmwNsxTDataCenterActiveGlobalManagers": vmwNsxTDataCenterActiveGlobalManagers,
       "vmwNsxTDataCenterSessionDownReason": vmwNsxTDataCenterSessionDownReason,
       "vmwNsxTDataCenterManagerNodeName": vmwNsxTDataCenterManagerNodeName,
       "vmwNsxTDataCenterTransportNodeAddress": vmwNsxTDataCenterTransportNodeAddress,
       "vmwNsxTDataCenterTransportNodeName": vmwNsxTDataCenterTransportNodeName,
       "vmwNsxTDataCenterCentralControlPlaneId": vmwNsxTDataCenterCentralControlPlaneId,
       "vmwNsxTDataCenterTunnelDownReason": vmwNsxTDataCenterTunnelDownReason,
       "vmwNsxTDataCenterHeapType": vmwNsxTDataCenterHeapType,
       "vmwNsxTDataCenterMempoolName": vmwNsxTDataCenterMempoolName,
       "vmwNsxTDataCenterPasswordExpirationDays": vmwNsxTDataCenterPasswordExpirationDays,
       "vmwNsxTDataCenterBGPNeighborIP": vmwNsxTDataCenterBGPNeighborIP,
       "vmwNsxTDataCenterLDAPServer": vmwNsxTDataCenterLDAPServer,
       "vmwNsxTDataCenterPeerAddress": vmwNsxTDataCenterPeerAddress,
       "vmwNsxTDataCenterMaxIDSEventsAllowed": vmwNsxTDataCenterMaxIDSEventsAllowed,
       "vmwNsxTDataCenterStaticAddress": vmwNsxTDataCenterStaticAddress,
       "vmwNsxTDataCenterDuplicateIPAddress": vmwNsxTDataCenterDuplicateIPAddress,
       "vmwNsxTDataCenterCapacityDisplayName": vmwNsxTDataCenterCapacityDisplayName,
       "vmwNsxTDataCenterCapacityUsageCount": vmwNsxTDataCenterCapacityUsageCount,
       "vmwNsxTDataCenterEdgeNICName": vmwNsxTDataCenterEdgeNICName,
       "vmwNsxTDataCenterRxRingBufferOverflowPercentage": vmwNsxTDataCenterRxRingBufferOverflowPercentage,
       "vmwNsxTDataCenterTxRingBufferOverflowPercentage": vmwNsxTDataCenterTxRingBufferOverflowPercentage,
       "vmwNsxTDataCenterSrId": vmwNsxTDataCenterSrId,
       "vmwNsxTDataCenterIDSEventsCount": vmwNsxTDataCenterIDSEventsCount,
       "vmwNsxTDataCenterRemoteSiteName": vmwNsxTDataCenterRemoteSiteName,
       "vmwNsxTDataCenterBGPSourceIP": vmwNsxTDataCenterBGPSourceIP,
       "vmwNsxTDataCenterRemoteSiteId": vmwNsxTDataCenterRemoteSiteId,
       "vmwNsxTDataCenterSiteId": vmwNsxTDataCenterSiteId,
       "vmwNsxTDataCenterSiteName": vmwNsxTDataCenterSiteName,
       "vmwNsxTDataCenterLrId": vmwNsxTDataCenterLrId,
       "vmwNsxTDataCenterRxMisses": vmwNsxTDataCenterRxMisses,
       "vmwNsxTDataCenterRxProcessed": vmwNsxTDataCenterRxProcessed,
       "vmwNsxTDataCenterTxMisses": vmwNsxTDataCenterTxMisses,
       "vmwNsxTDataCenterTxProcessed": vmwNsxTDataCenterTxProcessed,
       "vmwNsxTDataCenterLrportId": vmwNsxTDataCenterLrportId,
       "vmwNsxTDataCenterServiceIP": vmwNsxTDataCenterServiceIP,
       "vmwNsxTDataCenterRemoteManagerNodeId": vmwNsxTDataCenterRemoteManagerNodeId,
       "vmwNsxTDataCenterDirectoryDomain": vmwNsxTDataCenterDirectoryDomain,
       "vmwNsxTDataCenterTimeoutInMinutes": vmwNsxTDataCenterTimeoutInMinutes,
       "vmwNsxTDataCenterMaxCapacityThreshold": vmwNsxTDataCenterMaxCapacityThreshold,
       "vmwNsxTDataCenterMinCapacityThreshold": vmwNsxTDataCenterMinCapacityThreshold,
       "vmwNsxTDataCenterMaxSupportedCapacityCount": vmwNsxTDataCenterMaxSupportedCapacityCount,
       "vmwNsxTDataCenterLatencySource": vmwNsxTDataCenterLatencySource,
       "vmwNsxTDataCenterLatencyThreshold": vmwNsxTDataCenterLatencyThreshold,
       "vmwNsxTDataCenterLatencyValue": vmwNsxTDataCenterLatencyValue,
       "vmwNsxTDataCenterApplianceFQDN": vmwNsxTDataCenterApplianceFQDN,
       "vmwNsxTDataCenterRemoteApplianceAddress": vmwNsxTDataCenterRemoteApplianceAddress,
       "vmwNsxTDataCenterManagerNodeId": vmwNsxTDataCenterManagerNodeId,
       "vmwNsxTDataCenterDisplayedLicenseKey": vmwNsxTDataCenterDisplayedLicenseKey,
       "vmwNsxTDataCenterEdgeThreadName": vmwNsxTDataCenterEdgeThreadName,
       "vmwNsxTDataCenterIntentPath": vmwNsxTDataCenterIntentPath,
       "vmwNsxTDataCenterFirewallHalfopenFlowUsage": vmwNsxTDataCenterFirewallHalfopenFlowUsage,
       "vmwNsxTDataCenterFirewallICMPFlowUsage": vmwNsxTDataCenterFirewallICMPFlowUsage,
       "vmwNsxTDataCenterServiceDownReason": vmwNsxTDataCenterServiceDownReason,
       "vmwNsxTDataCenterFirewallUDPFlowUsage": vmwNsxTDataCenterFirewallUDPFlowUsage,
       "vmwNsxTDataCenterFirewallIPFlowUsage": vmwNsxTDataCenterFirewallIPFlowUsage,
       "vmwNsxTDataCenterDNSId": vmwNsxTDataCenterDNSId,
       "vmwNsxTDataCenterDNSUpstreamIP": vmwNsxTDataCenterDNSUpstreamIP,
       "vmwNsxTDataCenterCABundleAgeThreshold": vmwNsxTDataCenterCABundleAgeThreshold,
       "vmwNsxTDataCenterAPICollectionPath": vmwNsxTDataCenterAPICollectionPath,
       "vmwNsxTDataCenterEdgeNodeSettingMismatchReason": vmwNsxTDataCenterEdgeNodeSettingMismatchReason,
       "vmwNsxTDataCenterEdgeVMvSphereSettingsMismatchReason": vmwNsxTDataCenterEdgeVMvSphereSettingsMismatchReason,
       "vmwNsxTDataCenterFirewallSNATPortsUsage": vmwNsxTDataCenterFirewallSNATPortsUsage,
       "vmwNsxTDataCenterEdgevSphereLocationMismatchReason": vmwNsxTDataCenterEdgevSphereLocationMismatchReason,
       "vmwNsxTDataCenterEdgeNodeAndvSphereSettingsMismatchReason": vmwNsxTDataCenterEdgeNodeAndvSphereSettingsMismatchReason,
       "vmwNsxTDataCenterSNATIPAddress": vmwNsxTDataCenterSNATIPAddress,
       "vmwNsxTDataCenterNappClusterId": vmwNsxTDataCenterNappClusterId,
       "vmwNsxTDataCenterNappMessagingLAGThreshold": vmwNsxTDataCenterNappMessagingLAGThreshold,
       "vmwNsxTDataCenterNappNodeId": vmwNsxTDataCenterNappNodeId,
       "vmwNsxTDataCenterNappServiceName": vmwNsxTDataCenterNappServiceName,
       "vmwNsxTDataCenterFlowIdentifier": vmwNsxTDataCenterFlowIdentifier,
       "vmwNsxTDataCenterSyncIssueReason": vmwNsxTDataCenterSyncIssueReason,
       "vmwNsxTDataCenterQueueName": vmwNsxTDataCenterQueueName,
       "vmwNsxTDataCenterQueueSize": vmwNsxTDataCenterQueueSize,
       "vmwNsxTDataCenterQueueSizeThreshold": vmwNsxTDataCenterQueueSizeThreshold,
       "vmwNsxTDataCenterGroupType": vmwNsxTDataCenterGroupType,
       "vmwNsxTDataCenterManagerNodeIDS": vmwNsxTDataCenterManagerNodeIDS,
       "vmwNsxTDataCenterServiceRouterId": vmwNsxTDataCenterServiceRouterId,
       "vmwNsxTDataCenterTransportNodeId": vmwNsxTDataCenterTransportNodeId,
       "vmwNsxTDataCenterFromGMPath": vmwNsxTDataCenterFromGMPath,
       "vmwNsxTDataCenterToGMPath": vmwNsxTDataCenterToGMPath,
       "vmwNsxTDataCenterNICThroughput": vmwNsxTDataCenterNICThroughput,
       "vmwNsxTDataCenterNICThroughputThreshold": vmwNsxTDataCenterNICThroughputThreshold,
       "vmwNsxTDataCenterEdgeCryptoDrvName": vmwNsxTDataCenterEdgeCryptoDrvName,
       "vmwNsxTDataCenterNappNodeName": vmwNsxTDataCenterNappNodeName,
       "vmwNsxTDataCenterConformance": vmwNsxTDataCenterConformance,
       "vmwNsxTDataCenterCompliances": vmwNsxTDataCenterCompliances,
       "vmwNsxTDataCenterBasicCompliance": vmwNsxTDataCenterBasicCompliance,
       "vmwNsxTDataCenterBasicCompliance2": vmwNsxTDataCenterBasicCompliance2,
       "vmwNsxTDataCenterBasicCompliance3": vmwNsxTDataCenterBasicCompliance3,
       "vmwNsxTDataCenterBasicCompliance4": vmwNsxTDataCenterBasicCompliance4,
       "vmwNsxTDataCenterBasicCompliance5": vmwNsxTDataCenterBasicCompliance5,
       "vmwNsxTDataCenterBasicCompliance6": vmwNsxTDataCenterBasicCompliance6,
       "vmwNsxTDataCenterBasicCompliance7": vmwNsxTDataCenterBasicCompliance7,
       "vmwNsxTDataCenterBasicCompliance8": vmwNsxTDataCenterBasicCompliance8,
       "vmwNsxTDataCenterBasicCompliance9": vmwNsxTDataCenterBasicCompliance9,
       "vmwNsxTDataCenterSMIBGroups": vmwNsxTDataCenterSMIBGroups,
       "vmwNsxTDataCenterNotificationInfoGroup": vmwNsxTDataCenterNotificationInfoGroup,
       "vmwNsxTDataCenterNotificationGroup": vmwNsxTDataCenterNotificationGroup,
       "vmwNsxTDataCenterNotificationInfoGroup2": vmwNsxTDataCenterNotificationInfoGroup2,
       "vmwNsxTDataCenterNotificationGroup2": vmwNsxTDataCenterNotificationGroup2,
       "vmwNsxTDataCenterNotificationInfoGroup3": vmwNsxTDataCenterNotificationInfoGroup3,
       "vmwNsxTDataCenterNotificationGroup3": vmwNsxTDataCenterNotificationGroup3,
       "vmwNsxTDataCenterNotificationInfoGroup4": vmwNsxTDataCenterNotificationInfoGroup4,
       "vmwNsxTDataCenterNotificationGroup4": vmwNsxTDataCenterNotificationGroup4,
       "vmwNsxTDataCenterNotificationGroup5": vmwNsxTDataCenterNotificationGroup5,
       "vmwNsxTDataCenterNotificationInfoGroup6": vmwNsxTDataCenterNotificationInfoGroup6,
       "vmwNsxTDataCenterNotificationGroup6": vmwNsxTDataCenterNotificationGroup6,
       "vmwNsxTDataCenterNotificationInfoGroup7": vmwNsxTDataCenterNotificationInfoGroup7,
       "vmwNsxTDataCenterNotificationGroup7": vmwNsxTDataCenterNotificationGroup7,
       "vmwNsxTDataCenterNotificationInfoGroup8": vmwNsxTDataCenterNotificationInfoGroup8,
       "vmwNsxTDataCenterNotificationGroup8": vmwNsxTDataCenterNotificationGroup8,
       "vmwNsxTDataCenterNotificationInfoGroup9": vmwNsxTDataCenterNotificationInfoGroup9,
       "vmwNsxTDataCenterNotificationGroup9": vmwNsxTDataCenterNotificationGroup9}
)
