# SNMP MIB module (EPON-EOC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cdata\EPON-EOC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:49 2025
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

eponeoc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34592)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OperSwitch(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )



class DeviceStatus(TextualConvention, Integer32):
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
        *(("notPresent", 1),
          ("offline", 2),
          ("online", 3),
          ("normal", 4),
          ("abnormal", 5))
    )



class DataDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upstream", 1),
          ("downstream", 2))
    )



class DeviceOperation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("reset", 2),
          ("default", 3),
          ("saveConfig", 4),
          ("restore", 5),
          ("delete", 6))
    )



class LedStatus(TextualConvention, Integer32):
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
        *(("on", 1),
          ("off", 2),
          ("blink", 3))
    )



class DeviceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              16842752,
              16843009,
              16974083,
              16974084,
              16974086,
              16974087,
              16974088,
              16974089,
              16974090,
              16974091,
              16974092,
              16974094,
              16974095,
              16974097,
              16974337,
              16974337,
              16974338,
              16974593,
              16974594,
              16974850,
              17039617,
              17040129,
              17105153,
              17170689,
              17170945,
              17171202,
              17236225,
              825241671,
              825241674,
              825241683,
              825241960,
              825242728,
              825307464,
              825307496,
              825307496,
              825307757,
              842018893,
              858797160,
              875573314,
              875573325,
              875573331,
              875573335,
              875643987,
              875643991,
              875647827,
              875647831)
        )
    )
    namedValues = NamedValues(
        *(("ONU4FE2P", 1),
          ("ONU4FE2P1TV", 2),
          ("ONU24FEB", 3),
          ("ONU4FE2PW", 4),
          ("ONU2FE1P", 5),
          ("ONU16FEB", 8),
          ("SYSTEM", 16842752),
          ("EPON-2U8P", 16843009),
          ("ONU4D-B", 16974083),
          ("ONU8FEB", 16974084),
          ("ONU1FE", 16974086),
          ("ONU1D-G", 16974087),
          ("ONU1FE1GE", 16974088),
          ("ONU4D-P", 16974089),
          ("ONU3D-M", 16974090),
          ("ONU4FE", 16974091),
          ("ONU2D-M", 16974092),
          ("ONU4D-GM", 16974094),
          ("ONU2D-GM", 16974095),
          ("ONU4GE", 16974097),
          ("ONU4D2P", 16974337),
          ("ONU4FE2PA", 16974337),
          ("ONU4D2P-P", 16974338),
          ("ONU4FE1TV-WDM", 16974593),
          ("ONU4D1R-P", 16974594),
          ("ONU4D2P1R-P", 16974850),
          ("ONU24D", 17039617),
          ("ONU4D2P1R", 17040129),
          ("EPON-1U2P", 17105153),
          ("EPON-1U8P", 17170689),
          ("OLT", 17170945),
          ("PON", 17171202),
          ("EPON-1U4P", 17236225),
          ("ONU1GEC", 825241671),
          ("ONU1GEM", 825241674),
          ("ONU1FEC", 825241683),
          ("ONU1FECA", 825241960),
          ("ONU4FECA", 825242728),
          ("ONU1GE1FE1P", 825307464),
          ("ONU1GE", 825307496),
          ("ONU1GECA", 825307496),
          ("ONU2GE", 825307757),
          ("ONU2GEM", 842018893),
          ("ONU4FE1RF", 858797160),
          ("ONU4GEB", 875573314),
          ("ONU4GEM", 875573325),
          ("ONU4FEC", 875573331),
          ("ONU4FEW", 875573335),
          ("ONU4FE1TVCA", 875643987),
          ("ONU4FE1TVW", 875643991),
          ("ONU4FE1TVC-WDM", 875647827),
          ("ONU4FE1TVW-WDM", 875647831))
    )



# MIB Managed Objects in the order of their OIDs

_IpProduct_ObjectIdentity = ObjectIdentity
ipProduct = _IpProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1)
)
if mibBuilder.loadTexts:
    ipProduct.setStatus("current")
_MediaConverter_ObjectIdentity = ObjectIdentity
mediaConverter = _MediaConverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1)
)
if mibBuilder.loadTexts:
    mediaConverter.setStatus("current")
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 2)
)
if mibBuilder.loadTexts:
    switch.setStatus("current")
_Epon_ObjectIdentity = ObjectIdentity
epon = _Epon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3)
)
if mibBuilder.loadTexts:
    epon.setStatus("current")
_Eoc_ObjectIdentity = ObjectIdentity
eoc = _Eoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 4)
)
if mibBuilder.loadTexts:
    eoc.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EPON-EOC-MIB",
    **{"OperSwitch": OperSwitch,
       "DeviceStatus": DeviceStatus,
       "DataDirection": DataDirection,
       "DeviceOperation": DeviceOperation,
       "LedStatus": LedStatus,
       "DeviceType": DeviceType,
       "eponeoc": eponeoc,
       "ipProduct": ipProduct,
       "mediaConverter": mediaConverter,
       "switch": switch,
       "epon": epon,
       "eoc": eoc}
)
