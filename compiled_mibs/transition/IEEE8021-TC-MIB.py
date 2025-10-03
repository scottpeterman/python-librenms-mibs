# SNMP MIB module (IEEE8021-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\IEEE8021-TC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:27 2025
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 iso,
 org) = mibBuilder.importSymbols(
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
    "iso",
    "org")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ieee8021TcMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021TcMib.setRevisions(
        ("2012-02-15 00:00",
         "2011-08-23 00:00",
         "2011-04-06 00:00",
         "2011-02-27 00:00",
         "2008-11-18 00:00",
         "2008-10-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IEEE8021PbbComponentIdentifier(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class IEEE8021PbbComponentIdentifierOrZero(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



class IEEE8021PbbServiceIdentifier(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 16777214),
    )



class IEEE8021PbbServiceIdentifierOrUnassigned(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(256, 16777214),
    )



class IEEE8021PbbIngressEgress(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ingress", 0),
          ("egress", 1))
    )


class IEEE8021PriorityCodePoint(TextualConvention, Integer32):
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
        *(("codePoint8p0d", 1),
          ("codePoint7p1d", 2),
          ("codePoint6p2d", 3),
          ("codePoint5p3d", 4))
    )



class IEEE8021BridgePortNumber(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class IEEE8021BridgePortNumberOrZero(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class IEEE8021BridgePortType(TextualConvention, Integer32):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("customerVlanPort", 2),
          ("providerNetworkPort", 3),
          ("customerNetworkPort", 4),
          ("customerEdgePort", 5),
          ("customerBackbonePort", 6),
          ("virtualInstancePort", 7),
          ("dBridgePort", 8),
          ("remoteCustomerAccessPort", 9),
          ("stationFacingBridgePort", 10),
          ("uplinkAccessPort", 11),
          ("uplinkRelayPort", 12))
    )



class IEEE8021VlanIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4096, 4294967295),
    )



class IEEE8021VlanIndexOrWildcard(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class IEEE8021MstIdentifier(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class IEEE8021ServiceSelectorType(TextualConvention, Integer32):
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
        *(("vlanId", 1),
          ("isid", 2),
          ("tesid", 3),
          ("segid", 4))
    )



class IEEE8021ServiceSelectorValueOrNone(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



class IEEE8021ServiceSelectorValue(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class IEEE8021PortAcceptableFrameTypes(TextualConvention, Integer32):
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
        *(("admitAll", 1),
          ("admitUntaggedAndPriority", 2),
          ("admitTagged", 3))
    )



class IEEE8021PriorityValue(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class IEEE8021PbbTeProtectionGroupId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429467295),
    )



class IEEE8021PbbTeEsp(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )
    fixed_length = 14



class IEEE8021PbbTeTSidId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 42947295),
    )



class IEEE8021PbbTeProtectionGroupConfigAdmin(TextualConvention, Integer32):
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
        *(("clear", 1),
          ("lockOutProtection", 2),
          ("forceSwitch", 3),
          ("manualSwitchToProtection", 4),
          ("manualSwitchToWorking", 5))
    )



class IEEE8021PbbTeProtectionGroupActiveRequests(TextualConvention, Integer32):
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
        *(("noRequest", 1),
          ("loP", 2),
          ("fs", 3),
          ("pSFH", 4),
          ("wSFH", 5),
          ("manualSwitchToProtection", 6),
          ("manualSwitchToWorking", 7))
    )



class IEEE8021TeipsIpgid(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429467295),
    )



class IEEE8021TeipsSegid(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 42947295),
    )



class IEEE8021TeipsSmpid(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )
    fixed_length = 14



class IEEE8021TeipsIpgConfigAdmin(TextualConvention, Integer32):
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
        *(("clear", 1),
          ("lockOutProtection", 2),
          ("forceSwitch", 3),
          ("manualSwitchToProtection", 4),
          ("manualSwitchToWorking", 5))
    )



class IEEE8021TeipsIpgConfigActiveRequests(TextualConvention, Integer32):
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
        *(("noRequest", 1),
          ("loP", 2),
          ("fs", 3),
          ("pSFH", 4),
          ("wSFH", 5),
          ("manualSwitchToProtection", 6),
          ("manualSwitchToWorking", 7))
    )



# MIB Managed Objects in the order of their OIDs

_Ieee802dot1mibs_ObjectIdentity = ObjectIdentity
ieee802dot1mibs = _Ieee802dot1mibs_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-TC-MIB",
    **{"IEEE8021PbbComponentIdentifier": IEEE8021PbbComponentIdentifier,
       "IEEE8021PbbComponentIdentifierOrZero": IEEE8021PbbComponentIdentifierOrZero,
       "IEEE8021PbbServiceIdentifier": IEEE8021PbbServiceIdentifier,
       "IEEE8021PbbServiceIdentifierOrUnassigned": IEEE8021PbbServiceIdentifierOrUnassigned,
       "IEEE8021PbbIngressEgress": IEEE8021PbbIngressEgress,
       "IEEE8021PriorityCodePoint": IEEE8021PriorityCodePoint,
       "IEEE8021BridgePortNumber": IEEE8021BridgePortNumber,
       "IEEE8021BridgePortNumberOrZero": IEEE8021BridgePortNumberOrZero,
       "IEEE8021BridgePortType": IEEE8021BridgePortType,
       "IEEE8021VlanIndex": IEEE8021VlanIndex,
       "IEEE8021VlanIndexOrWildcard": IEEE8021VlanIndexOrWildcard,
       "IEEE8021MstIdentifier": IEEE8021MstIdentifier,
       "IEEE8021ServiceSelectorType": IEEE8021ServiceSelectorType,
       "IEEE8021ServiceSelectorValueOrNone": IEEE8021ServiceSelectorValueOrNone,
       "IEEE8021ServiceSelectorValue": IEEE8021ServiceSelectorValue,
       "IEEE8021PortAcceptableFrameTypes": IEEE8021PortAcceptableFrameTypes,
       "IEEE8021PriorityValue": IEEE8021PriorityValue,
       "IEEE8021PbbTeProtectionGroupId": IEEE8021PbbTeProtectionGroupId,
       "IEEE8021PbbTeEsp": IEEE8021PbbTeEsp,
       "IEEE8021PbbTeTSidId": IEEE8021PbbTeTSidId,
       "IEEE8021PbbTeProtectionGroupConfigAdmin": IEEE8021PbbTeProtectionGroupConfigAdmin,
       "IEEE8021PbbTeProtectionGroupActiveRequests": IEEE8021PbbTeProtectionGroupActiveRequests,
       "IEEE8021TeipsIpgid": IEEE8021TeipsIpgid,
       "IEEE8021TeipsSegid": IEEE8021TeipsSegid,
       "IEEE8021TeipsSmpid": IEEE8021TeipsSmpid,
       "IEEE8021TeipsIpgConfigAdmin": IEEE8021TeipsIpgConfigAdmin,
       "IEEE8021TeipsIpgConfigActiveRequests": IEEE8021TeipsIpgConfigActiveRequests,
       "ieee802dot1mibs": ieee802dot1mibs,
       "ieee8021TcMib": ieee8021TcMib}
)
