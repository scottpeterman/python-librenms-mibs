# SNMP MIB module (SO-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\smartoptics\SO-TC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:28:19 2025
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

(smartoptics,) = mibBuilder.importSymbols(
    "SO-MIB",
    "smartoptics")


# MODULE-IDENTITY

soTcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 3)
)
if mibBuilder.loadTexts:
    soTcMIB.setRevisions(
        ("2022-09-05 14:10",
         "2022-03-18 13:49",
         "2021-04-12 10:49",
         "2018-10-08 14:44")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OpticalPower1Decimal(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class DcpTenths(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class DcpHundreds(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"


class InterfaceStatus(TextualConvention, Integer32):
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
        *(("idle", 1),
          ("down", 2),
          ("up", 3))
    )



class ItuPerceivedSeverity(TextualConvention, Integer32):
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
        *(("cleared", 1),
          ("indeterminate", 2),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )



class OchPortMode(TextualConvention, Integer32):
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
        *(("on", 1),
          ("off", 2),
          ("edfa", 3),
          ("express", 4))
    )



class InterfacePortMode(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("na", 1),
          ("localAD", 2),
          ("xc1", 3),
          ("xc2", 4),
          ("xc3", 5),
          ("xc4Wss1", 6),
          ("xc4Wss2", 7),
          ("xc4Wss3", 8),
          ("xc4Wss4", 9),
          ("xc4Wss5", 10))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SO-TC-MIB",
    **{"OpticalPower1Decimal": OpticalPower1Decimal,
       "DcpTenths": DcpTenths,
       "DcpHundreds": DcpHundreds,
       "InterfaceStatus": InterfaceStatus,
       "ItuPerceivedSeverity": ItuPerceivedSeverity,
       "OchPortMode": OchPortMode,
       "InterfacePortMode": InterfacePortMode,
       "soTcMIB": soTcMIB}
)
