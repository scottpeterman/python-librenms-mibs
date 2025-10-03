# SNMP MIB module (WRI-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fiberhome\WRI-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:11 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

wri = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3807)
)

fhn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11408)
)


# Types definitions



class WriNetworkProtocol(Integer32):
    """Custom type WriNetworkProtocol based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("decnet", 2),
          ("pup", 3),
          ("chaos", 4),
          ("xns", 5),
          ("x121", 6),
          ("appletalk", 7),
          ("clns", 8),
          ("lat", 9),
          ("vines", 10),
          ("cons", 11),
          ("apollo", 12),
          ("stun", 13),
          ("novell", 14),
          ("qllc", 15),
          ("snapshot", 16),
          ("atmIlmi", 17),
          ("bstun", 18),
          ("x25pvc", 19),
          ("unknown", 65535))
    )





class WriNetworkAddress(OctetString):
    """Custom type WriNetworkAddress based on OctetString"""




class InterfaceIndexOrZero(Integer32):
    """Custom type InterfaceIndexOrZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class SAPType(Integer32):
    """Custom type SAPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )





class CountryCode(OctetString):
    """Custom type CountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
    )





class EntPhysicalIndexOrZero(Integer32):
    """Custom type EntPhysicalIndexOrZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class WriRowOperStatus(Integer32):
    """Custom type WriRowOperStatus based on Integer32"""
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
        *(("active", 1),
          ("activeDependencies", 2),
          ("inactiveDependency", 3),
          ("missingDependency", 4))
    )





class WriPort(Integer32):
    """Custom type WriPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class WriIpProtocol(Integer32):
    """Custom type WriIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class WriLocationClass(Integer32):
    """Custom type WriLocationClass based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("chassis", 1),
          ("shelf", 2),
          ("slot", 3),
          ("subSlot", 4),
          ("port", 5),
          ("subPort", 6),
          ("channel", 7),
          ("subChannel", 8))
    )





class WriLocationSpecifier(OctetString):
    """Custom type WriLocationSpecifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )





class WriInetAddressMask(Unsigned32):
    """Custom type WriInetAddressMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )





class WriAbsZeroBasedCounter32(Gauge32):
    """Custom type WriAbsZeroBasedCounter32 based on Gauge32"""




class WriSnapShotAbsCounter32(Unsigned32):
    """Custom type WriSnapShotAbsCounter32 based on Unsigned32"""




class WriAlarmSeverity(Integer32):
    """Custom type WriAlarmSeverity based on Integer32"""
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
        *(("cleared", 1),
          ("indeterminate", 2),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6),
          ("info", 7))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WriProducts_ObjectIdentity = ObjectIdentity
wriProducts = _WriProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1)
)
_WriProtocol_ObjectIdentity = ObjectIdentity
wriProtocol = _WriProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 2)
)
_WriMgmt_ObjectIdentity = ObjectIdentity
wriMgmt = _WriMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 3)
)
_FhnProducts_ObjectIdentity = ObjectIdentity
fhnProducts = _FhnProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11408, 1)
)
_FhnProtocol_ObjectIdentity = ObjectIdentity
fhnProtocol = _FhnProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11408, 2)
)
_FhnMgmt_ObjectIdentity = ObjectIdentity
fhnMgmt = _FhnMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11408, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WRI-SMI",
    **{"WriNetworkProtocol": WriNetworkProtocol,
       "WriNetworkAddress": WriNetworkAddress,
       "InterfaceIndexOrZero": InterfaceIndexOrZero,
       "SAPType": SAPType,
       "CountryCode": CountryCode,
       "EntPhysicalIndexOrZero": EntPhysicalIndexOrZero,
       "WriRowOperStatus": WriRowOperStatus,
       "WriPort": WriPort,
       "WriIpProtocol": WriIpProtocol,
       "WriLocationClass": WriLocationClass,
       "WriLocationSpecifier": WriLocationSpecifier,
       "WriInetAddressMask": WriInetAddressMask,
       "WriAbsZeroBasedCounter32": WriAbsZeroBasedCounter32,
       "WriSnapShotAbsCounter32": WriSnapShotAbsCounter32,
       "WriAlarmSeverity": WriAlarmSeverity,
       "wri": wri,
       "wriProducts": wriProducts,
       "wriProtocol": wriProtocol,
       "wriMgmt": wriMgmt,
       "fhn": fhn,
       "fhnProducts": fhnProducts,
       "fhnProtocol": fhnProtocol,
       "fhnMgmt": fhnMgmt}
)
