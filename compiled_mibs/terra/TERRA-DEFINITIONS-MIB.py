# SNMP MIB module (TERRA-DEFINITIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\terra\TERRA-DEFINITIONS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:12 2025
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

(terraRoot,) = mibBuilder.importSymbols(
    "TERRA-SMI",
    "terraRoot")


# MODULE-IDENTITY

terraDefIdentMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 3)
)
if mibBuilder.loadTexts:
    terraDefIdentMib.setRevisions(
        ("1970-01-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DefTenthdBm(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )



class DefTenthVolt(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d-1"


class DefOnOffStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )



class DefHundredthNanoMeter(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-2"


class DefFaultStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("fault", 2))
    )



class DefMilliAmp(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d-3"


class DefTenthAmp(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d-1"


class DefOnOffControl(TextualConvention, Integer32):
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
        *(("off", 1),
          ("on", 2),
          ("meaningless", 3))
    )



class DefTenthCentigrade(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d-1"


class DefTenthdBuV(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )



class DefTenthdB(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )



class DefStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )



class DefRelayState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERRA-DEFINITIONS-MIB",
    **{"DefTenthdBm": DefTenthdBm,
       "DefTenthVolt": DefTenthVolt,
       "DefOnOffStatus": DefOnOffStatus,
       "DefHundredthNanoMeter": DefHundredthNanoMeter,
       "DefFaultStatus": DefFaultStatus,
       "DefMilliAmp": DefMilliAmp,
       "DefTenthAmp": DefTenthAmp,
       "DefOnOffControl": DefOnOffControl,
       "DefTenthCentigrade": DefTenthCentigrade,
       "DefTenthdBuV": DefTenthdBuV,
       "DefTenthdB": DefTenthdB,
       "DefStatus": DefStatus,
       "DefRelayState": DefRelayState,
       "terraDefIdentMib": terraDefIdentMib}
)
