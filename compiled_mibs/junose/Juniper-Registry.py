# SNMP MIB module (Juniper-Registry) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\Juniper-Registry
# Produced by pysmi-1.6.2 at Thu Oct  2 12:06:22 2025
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

(juniperUniAdmin,) = mibBuilder.importSymbols(
    "Juniper-UNI-SMI",
    "juniperUniAdmin")

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

juniAdmin = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2)
)
if mibBuilder.loadTexts:
    juniAdmin.setRevisions(
        ("2004-12-23 11:58",
         "2003-12-17 19:25",
         "2003-12-17 17:22",
         "2002-11-13 20:38",
         "2001-06-01 21:18")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniRegistry_ObjectIdentity = ObjectIdentity
juniRegistry = _JuniRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 1)
)
_JuniEntPhysicalType_ObjectIdentity = ObjectIdentity
juniEntPhysicalType = _JuniEntPhysicalType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 1)
)
_JuniPcmciaFlashCard_ObjectIdentity = ObjectIdentity
juniPcmciaFlashCard = _JuniPcmciaFlashCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniPcmciaFlashCard.setStatus("current")
_Juni85MegT2FlashCard_ObjectIdentity = ObjectIdentity
juni85MegT2FlashCard = _Juni85MegT2FlashCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juni85MegT2FlashCard.setStatus("current")
_Juni220MegT2FlashCard_ObjectIdentity = ObjectIdentity
juni220MegT2FlashCard = _Juni220MegT2FlashCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juni220MegT2FlashCard.setStatus("current")
_Juni512MegT2FlashCard_ObjectIdentity = ObjectIdentity
juni512MegT2FlashCard = _Juni512MegT2FlashCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    juni512MegT2FlashCard.setStatus("current")
_Juni1GigT2FlashCard_ObjectIdentity = ObjectIdentity
juni1GigT2FlashCard = _Juni1GigT2FlashCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    juni1GigT2FlashCard.setStatus("current")
_JuniTraceRouteImplementationTypes_ObjectIdentity = ObjectIdentity
juniTraceRouteImplementationTypes = _JuniTraceRouteImplementationTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniTraceRouteImplementationTypes.setStatus("current")
_JuniTraceRouteUsingIcmpProbe_ObjectIdentity = ObjectIdentity
juniTraceRouteUsingIcmpProbe = _JuniTraceRouteUsingIcmpProbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    juniTraceRouteUsingIcmpProbe.setStatus("current")
_JuniErxRegistry_ObjectIdentity = ObjectIdentity
juniErxRegistry = _JuniErxRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2)
)
_JuniES2Registry_ObjectIdentity = ObjectIdentity
juniES2Registry = _JuniES2Registry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-Registry",
    **{"juniAdmin": juniAdmin,
       "juniRegistry": juniRegistry,
       "juniEntPhysicalType": juniEntPhysicalType,
       "juniPcmciaFlashCard": juniPcmciaFlashCard,
       "juni85MegT2FlashCard": juni85MegT2FlashCard,
       "juni220MegT2FlashCard": juni220MegT2FlashCard,
       "juni512MegT2FlashCard": juni512MegT2FlashCard,
       "juni1GigT2FlashCard": juni1GigT2FlashCard,
       "juniTraceRouteImplementationTypes": juniTraceRouteImplementationTypes,
       "juniTraceRouteUsingIcmpProbe": juniTraceRouteUsingIcmpProbe,
       "juniErxRegistry": juniErxRegistry,
       "juniES2Registry": juniES2Registry}
)
