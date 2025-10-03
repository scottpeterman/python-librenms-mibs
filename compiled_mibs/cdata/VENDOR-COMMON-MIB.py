# SNMP MIB module (VENDOR-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cdata\VENDOR-COMMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:07 2025
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

vendor = ModuleIdentity(
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
            *(16842752,
              16843009,
              16843265,
              16843521,
              16909057,
              16974081,
              16974082,
              16974083,
              16974084,
              16974085,
              16974086,
              16974087,
              16974088,
              16974089,
              16974090,
              16974091,
              16974092,
              16974094,
              16974095,
              16974337,
              16974338,
              16974593,
              16974594,
              16974849,
              16974850,
              17039617,
              17040129,
              17105153,
              17105409,
              17105665)
        )
    )
    namedValues = NamedValues(
        *(("epon", 16842752),
          ("chassis", 16843009),
          ("olt", 16843265),
          ("pon", 16843521),
          ("pon1", 16909057),
          ("onu4db", 16974081),
          ("onu4db1", 16974082),
          ("onu4db2", 16974083),
          ("onu8db", 16974084),
          ("onu4d", 16974085),
          ("onu1d", 16974086),
          ("onu1dg", 16974087),
          ("onu2dg", 16974088),
          ("onu4dp", 16974089),
          ("onu3dm", 16974090),
          ("onu4d1", 16974091),
          ("onu2dm", 16974092),
          ("onu4dgm", 16974094),
          ("onu2dgm", 16974095),
          ("onu4d2p", 16974337),
          ("onu4d2pp", 16974338),
          ("onu4d1r", 16974593),
          ("onu4d1rp", 16974594),
          ("onu4d2p1r", 16974849),
          ("onu4d2p1rp", 16974850),
          ("onu24d", 17039617),
          ("onu4d2p1r1", 17040129),
          ("epon1u", 17105153),
          ("olt1", 17105409),
          ("pon2", 17105665))
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
_Pon_ObjectIdentity = ObjectIdentity
pon = _Pon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3)
)
if mibBuilder.loadTexts:
    pon.setStatus("current")
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
    "VENDOR-COMMON-MIB",
    **{"OperSwitch": OperSwitch,
       "DeviceStatus": DeviceStatus,
       "DataDirection": DataDirection,
       "DeviceOperation": DeviceOperation,
       "LedStatus": LedStatus,
       "DeviceType": DeviceType,
       "vendor": vendor,
       "ipProduct": ipProduct,
       "mediaConverter": mediaConverter,
       "switch": switch,
       "pon": pon,
       "eoc": eoc}
)
