# SNMP MIB module (ATM-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ATM-TC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:41:20 2025
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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

atmTCMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 37, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AtmAddr(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )



class AtmConnCastType(TextualConvention, Integer32):
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
        *(("p2p", 1),
          ("p2mpRoot", 2),
          ("p2mpLeaf", 3))
    )



class AtmConnKind(TextualConvention, Integer32):
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
        *(("pvc", 1),
          ("svcIncoming", 2),
          ("svcOutgoing", 3),
          ("spvcInitiator", 4),
          ("spvcTarget", 5))
    )



class AtmIlmiNetworkPrefix(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(13, 13),
    )



class AtmInterfaceType(TextualConvention, Integer32):
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
        *(("other", 1),
          ("autoConfig", 2),
          ("ituDss2", 3),
          ("atmfUni3Dot0", 4),
          ("atmfUni3Dot1", 5),
          ("atmfUni4Dot0", 6),
          ("atmfIispUni3Dot0", 7),
          ("atmfIispUni3Dot1", 8),
          ("atmfIispUni4Dot0", 9),
          ("atmfPnni1Dot0", 10),
          ("atmfBici2Dot0", 11),
          ("atmfUniPvcOnly", 12),
          ("atmfNniPvcOnly", 13))
    )



class AtmServiceCategory(TextualConvention, Integer32):
    status = "current"
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
        *(("other", 1),
          ("cbr", 2),
          ("rtVbr", 3),
          ("nrtVbr", 4),
          ("abr", 5),
          ("ubr", 6))
    )



class AtmSigDescrParamIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class AtmTrafficDescrParamIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class AtmVcIdentifier(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class AtmVpIdentifier(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class AtmVorXAdminStatus(TextualConvention, Integer32):
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



class AtmVorXLastChange(TextualConvention, TimeTicks):
    status = "current"


class AtmVorXOperStatus(TextualConvention, Integer32):
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
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AtmTrafficDescriptorTypes_ObjectIdentity = ObjectIdentity
atmTrafficDescriptorTypes = _AtmTrafficDescriptorTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1)
)
_AtmNoTrafficDescriptor_ObjectIdentity = ObjectIdentity
atmNoTrafficDescriptor = _AtmNoTrafficDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 1)
)
if mibBuilder.loadTexts:
    atmNoTrafficDescriptor.setStatus("deprecated")
_AtmNoClpNoScr_ObjectIdentity = ObjectIdentity
atmNoClpNoScr = _AtmNoClpNoScr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 2)
)
if mibBuilder.loadTexts:
    atmNoClpNoScr.setStatus("current")
_AtmClpNoTaggingNoScr_ObjectIdentity = ObjectIdentity
atmClpNoTaggingNoScr = _AtmClpNoTaggingNoScr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 3)
)
if mibBuilder.loadTexts:
    atmClpNoTaggingNoScr.setStatus("deprecated")
_AtmClpTaggingNoScr_ObjectIdentity = ObjectIdentity
atmClpTaggingNoScr = _AtmClpTaggingNoScr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 4)
)
if mibBuilder.loadTexts:
    atmClpTaggingNoScr.setStatus("deprecated")
_AtmNoClpScr_ObjectIdentity = ObjectIdentity
atmNoClpScr = _AtmNoClpScr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 5)
)
if mibBuilder.loadTexts:
    atmNoClpScr.setStatus("current")
_AtmClpNoTaggingScr_ObjectIdentity = ObjectIdentity
atmClpNoTaggingScr = _AtmClpNoTaggingScr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 6)
)
if mibBuilder.loadTexts:
    atmClpNoTaggingScr.setStatus("current")
_AtmClpTaggingScr_ObjectIdentity = ObjectIdentity
atmClpTaggingScr = _AtmClpTaggingScr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 7)
)
if mibBuilder.loadTexts:
    atmClpTaggingScr.setStatus("current")
_AtmClpNoTaggingMcr_ObjectIdentity = ObjectIdentity
atmClpNoTaggingMcr = _AtmClpNoTaggingMcr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 8)
)
if mibBuilder.loadTexts:
    atmClpNoTaggingMcr.setStatus("current")
_AtmClpTransparentNoScr_ObjectIdentity = ObjectIdentity
atmClpTransparentNoScr = _AtmClpTransparentNoScr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 9)
)
if mibBuilder.loadTexts:
    atmClpTransparentNoScr.setStatus("current")
_AtmClpTransparentScr_ObjectIdentity = ObjectIdentity
atmClpTransparentScr = _AtmClpTransparentScr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 10)
)
if mibBuilder.loadTexts:
    atmClpTransparentScr.setStatus("current")
_AtmNoClpTaggingNoScr_ObjectIdentity = ObjectIdentity
atmNoClpTaggingNoScr = _AtmNoClpTaggingNoScr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 11)
)
if mibBuilder.loadTexts:
    atmNoClpTaggingNoScr.setStatus("current")
_AtmNoClpNoScrCdvt_ObjectIdentity = ObjectIdentity
atmNoClpNoScrCdvt = _AtmNoClpNoScrCdvt_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 12)
)
if mibBuilder.loadTexts:
    atmNoClpNoScrCdvt.setStatus("current")
_AtmNoClpScrCdvt_ObjectIdentity = ObjectIdentity
atmNoClpScrCdvt = _AtmNoClpScrCdvt_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 13)
)
if mibBuilder.loadTexts:
    atmNoClpScrCdvt.setStatus("current")
_AtmClpNoTaggingScrCdvt_ObjectIdentity = ObjectIdentity
atmClpNoTaggingScrCdvt = _AtmClpNoTaggingScrCdvt_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 14)
)
if mibBuilder.loadTexts:
    atmClpNoTaggingScrCdvt.setStatus("current")
_AtmClpTaggingScrCdvt_ObjectIdentity = ObjectIdentity
atmClpTaggingScrCdvt = _AtmClpTaggingScrCdvt_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 15)
)
if mibBuilder.loadTexts:
    atmClpTaggingScrCdvt.setStatus("current")
_AtmObjectIdentities_ObjectIdentity = ObjectIdentity
atmObjectIdentities = _AtmObjectIdentities_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 3, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-TC-MIB",
    **{"AtmAddr": AtmAddr,
       "AtmConnCastType": AtmConnCastType,
       "AtmConnKind": AtmConnKind,
       "AtmIlmiNetworkPrefix": AtmIlmiNetworkPrefix,
       "AtmInterfaceType": AtmInterfaceType,
       "AtmServiceCategory": AtmServiceCategory,
       "AtmSigDescrParamIndex": AtmSigDescrParamIndex,
       "AtmTrafficDescrParamIndex": AtmTrafficDescrParamIndex,
       "AtmVcIdentifier": AtmVcIdentifier,
       "AtmVpIdentifier": AtmVpIdentifier,
       "AtmVorXAdminStatus": AtmVorXAdminStatus,
       "AtmVorXLastChange": AtmVorXLastChange,
       "AtmVorXOperStatus": AtmVorXOperStatus,
       "atmTrafficDescriptorTypes": atmTrafficDescriptorTypes,
       "atmNoTrafficDescriptor": atmNoTrafficDescriptor,
       "atmNoClpNoScr": atmNoClpNoScr,
       "atmClpNoTaggingNoScr": atmClpNoTaggingNoScr,
       "atmClpTaggingNoScr": atmClpTaggingNoScr,
       "atmNoClpScr": atmNoClpScr,
       "atmClpNoTaggingScr": atmClpNoTaggingScr,
       "atmClpTaggingScr": atmClpTaggingScr,
       "atmClpNoTaggingMcr": atmClpNoTaggingMcr,
       "atmClpTransparentNoScr": atmClpTransparentNoScr,
       "atmClpTransparentScr": atmClpTransparentScr,
       "atmNoClpTaggingNoScr": atmNoClpTaggingNoScr,
       "atmNoClpNoScrCdvt": atmNoClpNoScrCdvt,
       "atmNoClpScrCdvt": atmNoClpScrCdvt,
       "atmClpNoTaggingScrCdvt": atmClpNoTaggingScrCdvt,
       "atmClpTaggingScrCdvt": atmClpTaggingScrCdvt,
       "atmTCMIB": atmTCMIB,
       "atmObjectIdentities": atmObjectIdentities}
)
