# SNMP MIB module (CISCO-CEF-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCO-CEF-TC
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:51 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoCefTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 493)
)
if mibBuilder.loadTexts:
    ciscoCefTextualConventions.setRevisions(
        ("2005-09-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CefIpVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )



class CefAdjLinkType(TextualConvention, Integer32):
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("mpls", 3),
          ("raw", 4),
          ("unknown", 5))
    )



class CefAdjacencySource(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("atom", 0),
          ("linkRawAdj", 1),
          ("ipPseudowireAdj", 2),
          ("arp", 3),
          ("p2pAdj", 4),
          ("frMap", 5),
          ("atmPVC", 6),
          ("atmSVC", 7),
          ("atmTVC", 8),
          ("nbma", 9),
          ("mpoa", 10),
          ("atmBundle", 11),
          ("lec", 12),
          ("nhrp", 13),
          ("ipv6ND", 14),
          ("cmcc", 15),
          ("ipv6SixtoFourTunnel", 16),
          ("ipv6IsaTapTunnel", 17),
          ("ipv6AutoTunnel", 18),
          ("fibLc", 19),
          ("virtual", 20),
          ("multicast", 21),
          ("unknown", 22))
    )


class CefPathType(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("receive", 1),
          ("connectedPrefix", 2),
          ("attachedPrefix", 3),
          ("attachedHost", 4),
          ("attachedNexthop", 5),
          ("recursiveNexthop", 6),
          ("adjacencyPrefix", 7),
          ("specialPrefix", 8),
          ("unknown", 9))
    )



class CefPrefixSearchState(TextualConvention, Integer32):
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
        *(("running", 1),
          ("matchFound", 2),
          ("noMatchFound", 3))
    )



class CefForwardingElementSpecialType(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("illegal", 1),
          ("punt", 2),
          ("drop", 3),
          ("discard", 4),
          ("null", 5),
          ("glean", 6),
          ("unresolved", 7),
          ("noRoute", 8),
          ("none", 9))
    )



class CefMplsLabelList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class CefAdminStatus(TextualConvention, Integer32):
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



class CefOperStatus(TextualConvention, Integer32):
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



class CefFailureReason(TextualConvention, Integer32):
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
        *(("none", 1),
          ("mallocFailure", 2),
          ("hwFailure", 3),
          ("keepaliveFailure", 4),
          ("noMsgBuffer", 5),
          ("invalidMsgSize", 6),
          ("internalError", 7))
    )



class CefCCType(TextualConvention, Integer32):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("lcDetect", 1),
          ("scanFibLcRp", 2),
          ("scanFibRpLc", 3),
          ("scanRibFib", 4),
          ("scanFibRib", 5),
          ("scanFibHwSw", 6),
          ("scanFibSwHw", 7),
          ("fullScanRibFib", 8),
          ("fullScanFibRib", 9),
          ("fullScanFibRpLc", 10),
          ("fullScanFibLcRp", 11),
          ("fullScanFibHwSw", 12),
          ("fullScanFibSwHw", 13))
    )



class CefCCAction(TextualConvention, Integer32):
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
        *(("ccActionStart", 1),
          ("ccActionAbort", 2),
          ("ccActionNone", 3))
    )



class CefCCStatus(TextualConvention, Integer32):
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
        *(("ccStatusIdle", 1),
          ("ccStatusRunning", 2),
          ("ccStatusDone", 3))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CEF-TC",
    **{"CefIpVersion": CefIpVersion,
       "CefAdjLinkType": CefAdjLinkType,
       "CefAdjacencySource": CefAdjacencySource,
       "CefPathType": CefPathType,
       "CefPrefixSearchState": CefPrefixSearchState,
       "CefForwardingElementSpecialType": CefForwardingElementSpecialType,
       "CefMplsLabelList": CefMplsLabelList,
       "CefAdminStatus": CefAdminStatus,
       "CefOperStatus": CefOperStatus,
       "CefFailureReason": CefFailureReason,
       "CefCCType": CefCCType,
       "CefCCAction": CefCCAction,
       "CefCCStatus": CefCCStatus,
       "ciscoCefTextualConventions": ciscoCefTextualConventions}
)
