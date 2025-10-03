# SNMP MIB module (LLDP-V2-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\LLDP-V2-TC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 09:49:06 2025
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

lldpV2TcMIB = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 12)
)
if mibBuilder.loadTexts:
    lldpV2TcMIB.setRevisions(
        ("2009-06-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LldpV2ChassisIdSubtype(TextualConvention, Integer32):
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
        *(("chassisComponent", 1),
          ("interfaceAlias", 2),
          ("portComponent", 3),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("interfaceName", 6),
          ("local", 7))
    )



class LldpV2ChassisId(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class LldpV2PortIdSubtype(TextualConvention, Integer32):
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
        *(("interfaceAlias", 1),
          ("portComponent", 2),
          ("macAddress", 3),
          ("networkAddress", 4),
          ("interfaceName", 5),
          ("agentCircuitId", 6),
          ("local", 7))
    )



class LldpV2PortId(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class LldpV2ManAddrIfSubtype(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("ifIndex", 2),
          ("systemPortNumber", 3))
    )



class LldpV2ManAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class LldpV2SystemCapabilitiesMap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("other", 0),
          ("repeater", 1),
          ("bridge", 2),
          ("wlanAccessPoint", 3),
          ("router", 4),
          ("telephone", 5),
          ("docsisCableDevice", 6),
          ("stationOnly", 7),
          ("cVLANComponent", 8),
          ("sVLANComponent", 9),
          ("twoPortMACRelay", 10))
    )


class LldpV2DestAddressTableIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )



class LldpV2LinkAggStatusMap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("aggCapable", 0),
          ("aggEnabled", 1))
    )


class LldpV2PowerPortClass(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pClassPSE", 1),
          ("pClassPD", 2))
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
    "LLDP-V2-TC-MIB",
    **{"LldpV2ChassisIdSubtype": LldpV2ChassisIdSubtype,
       "LldpV2ChassisId": LldpV2ChassisId,
       "LldpV2PortIdSubtype": LldpV2PortIdSubtype,
       "LldpV2PortId": LldpV2PortId,
       "LldpV2ManAddrIfSubtype": LldpV2ManAddrIfSubtype,
       "LldpV2ManAddress": LldpV2ManAddress,
       "LldpV2SystemCapabilitiesMap": LldpV2SystemCapabilitiesMap,
       "LldpV2DestAddressTableIndex": LldpV2DestAddressTableIndex,
       "LldpV2LinkAggStatusMap": LldpV2LinkAggStatusMap,
       "LldpV2PowerPortClass": LldpV2PowerPortClass,
       "ieee802dot1mibs": ieee802dot1mibs,
       "lldpV2TcMIB": lldpV2TcMIB}
)
