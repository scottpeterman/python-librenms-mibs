# SNMP MIB module (ERICSSON-ROUTER-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ericsson\ERICSSON-ROUTER-TC
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:27 2025
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

(eriRouterModules,) = mibBuilder.importSymbols(
    "ERICSSON-ROUTER-SMI",
    "eriRouterModules")

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

eriRouterTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 5, 2)
)
if mibBuilder.loadTexts:
    eriRouterTC.setRevisions(
        ("2017-07-28 18:00",
         "2015-01-14 18:00",
         "2014-07-19 17:00",
         "2011-01-19 18:00",
         "2009-10-20 17:00",
         "2004-06-19 17:00",
         "2003-03-17 17:00",
         "2002-11-11 00:00",
         "2002-06-26 00:00",
         "2000-07-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EriRouterCircuitHandle(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d:1d:2x-2x-2x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class EriRouterKBytes(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class EriRouterPercentage(TextualConvention, Integer32):
    status = "current"
    displayHint = "d%"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class EriRouterSlot(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class EriRouterPort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class EriRouterVidOrUntagged(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )



class EriRouterPortMediumType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("dsl", 11),
          ("cable", 12),
          ("wireless", 13),
          ("satellite", 14))
    )



class EriRouterUnsigned64(TextualConvention, OctetString):
    status = "current"
    displayHint = "8d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class EriRouterSubscriberState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9,
              13)
        )
    )
    namedValues = NamedValues(
        *(("up", 9),
          ("standby-up", 13))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERICSSON-ROUTER-TC",
    **{"EriRouterCircuitHandle": EriRouterCircuitHandle,
       "EriRouterKBytes": EriRouterKBytes,
       "EriRouterPercentage": EriRouterPercentage,
       "EriRouterSlot": EriRouterSlot,
       "EriRouterPort": EriRouterPort,
       "EriRouterVidOrUntagged": EriRouterVidOrUntagged,
       "EriRouterPortMediumType": EriRouterPortMediumType,
       "EriRouterUnsigned64": EriRouterUnsigned64,
       "EriRouterSubscriberState": EriRouterSubscriberState,
       "eriRouterTC": eriRouterTC}
)
