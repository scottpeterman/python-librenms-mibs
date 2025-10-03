# SNMP MIB module (TPDIN3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tycon\TPDIN3-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:51 2025
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

tpdin3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45621, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Tenths(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



# MIB Managed Objects in the order of their OIDs

_Tycon_ObjectIdentity = ObjectIdentity
tycon = _Tycon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45621)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45621, 3, 1)
)
_Model_Type = DisplayString
_Model_Object = MibScalar
model = _Model_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 1, 1),
    _Model_Type()
)
model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model.setStatus("current")
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 1, 2),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_BuildDate_Type = DisplayString
_BuildDate_Object = MibScalar
buildDate = _BuildDate_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 1, 3),
    _BuildDate_Type()
)
buildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buildDate.setStatus("current")
_Monitor_ObjectIdentity = ObjectIdentity
monitor = _Monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3)
)
_Relay1_Type = Integer32
_Relay1_Object = MibScalar
relay1 = _Relay1_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 1),
    _Relay1_Type()
)
relay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1.setStatus("current")
_Relay2_Type = Integer32
_Relay2_Object = MibScalar
relay2 = _Relay2_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 2),
    _Relay2_Type()
)
relay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2.setStatus("current")
_Relay3_Type = Integer32
_Relay3_Object = MibScalar
relay3 = _Relay3_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 3),
    _Relay3_Type()
)
relay3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3.setStatus("current")
_Relay4_Type = Integer32
_Relay4_Object = MibScalar
relay4 = _Relay4_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 4),
    _Relay4_Type()
)
relay4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4.setStatus("current")


class _V1_Type(DisplayString):
    """Custom type v1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_V1_Type.__name__ = "DisplayString"
_V1_Object = MibScalar
v1 = _V1_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 5),
    _V1_Type()
)
v1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1.setStatus("current")


class _V2_Type(DisplayString):
    """Custom type v2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_V2_Type.__name__ = "DisplayString"
_V2_Object = MibScalar
v2 = _V2_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 6),
    _V2_Type()
)
v2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2.setStatus("current")


class _V3_Type(DisplayString):
    """Custom type v3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_V3_Type.__name__ = "DisplayString"
_V3_Object = MibScalar
v3 = _V3_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 7),
    _V3_Type()
)
v3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3.setStatus("current")


class _V4_Type(DisplayString):
    """Custom type v4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_V4_Type.__name__ = "DisplayString"
_V4_Object = MibScalar
v4 = _V4_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 8),
    _V4_Type()
)
v4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4.setStatus("current")


class _I1_Type(DisplayString):
    """Custom type i1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_I1_Type.__name__ = "DisplayString"
_I1_Object = MibScalar
i1 = _I1_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 9),
    _I1_Type()
)
i1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    i1.setStatus("current")


class _I2_Type(DisplayString):
    """Custom type i2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_I2_Type.__name__ = "DisplayString"
_I2_Object = MibScalar
i2 = _I2_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 10),
    _I2_Type()
)
i2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    i2.setStatus("current")


class _I3_Type(DisplayString):
    """Custom type i3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_I3_Type.__name__ = "DisplayString"
_I3_Object = MibScalar
i3 = _I3_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 11),
    _I3_Type()
)
i3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    i3.setStatus("current")


class _I4_Type(DisplayString):
    """Custom type i4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_I4_Type.__name__ = "DisplayString"
_I4_Object = MibScalar
i4 = _I4_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 12),
    _I4_Type()
)
i4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    i4.setStatus("current")


class _T1_Type(DisplayString):
    """Custom type t1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_T1_Type.__name__ = "DisplayString"
_T1_Object = MibScalar
t1 = _T1_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 13),
    _T1_Type()
)
t1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1.setStatus("current")


class _T2_Type(DisplayString):
    """Custom type t2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_T2_Type.__name__ = "DisplayString"
_T2_Object = MibScalar
t2 = _T2_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 14),
    _T2_Type()
)
t2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2.setStatus("current")
_V1int_Type = Tenths
_V1int_Object = MibScalar
v1int = _V1int_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 15),
    _V1int_Type()
)
v1int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v1int.setStatus("current")
_V2int_Type = Tenths
_V2int_Object = MibScalar
v2int = _V2int_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 16),
    _V2int_Type()
)
v2int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2int.setStatus("current")
_V3int_Type = Tenths
_V3int_Object = MibScalar
v3int = _V3int_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 17),
    _V3int_Type()
)
v3int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3int.setStatus("current")
_V4int_Type = Tenths
_V4int_Object = MibScalar
v4int = _V4int_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 18),
    _V4int_Type()
)
v4int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4int.setStatus("current")
_I1int_Type = Tenths
_I1int_Object = MibScalar
i1int = _I1int_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 19),
    _I1int_Type()
)
i1int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    i1int.setStatus("current")
_I2int_Type = Tenths
_I2int_Object = MibScalar
i2int = _I2int_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 20),
    _I2int_Type()
)
i2int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    i2int.setStatus("current")
_I3int_Type = Tenths
_I3int_Object = MibScalar
i3int = _I3int_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 21),
    _I3int_Type()
)
i3int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    i3int.setStatus("current")
_I4int_Type = Tenths
_I4int_Object = MibScalar
i4int = _I4int_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 22),
    _I4int_Type()
)
i4int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    i4int.setStatus("current")
_T1int_Type = Tenths
_T1int_Object = MibScalar
t1int = _T1int_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 23),
    _T1int_Type()
)
t1int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1int.setStatus("current")
_T2int_Type = Tenths
_T2int_Object = MibScalar
t2int = _T2int_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 3, 24),
    _T2int_Type()
)
t2int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t2int.setStatus("current")
_Mppt_ObjectIdentity = ObjectIdentity
mppt = _Mppt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10)
)
_Mpptmodel_Type = DisplayString
_Mpptmodel_Object = MibScalar
mpptmodel = _Mpptmodel_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 1),
    _Mpptmodel_Type()
)
mpptmodel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpptmodel.setStatus("current")


class _Batv_Type(DisplayString):
    """Custom type batv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Batv_Type.__name__ = "DisplayString"
_Batv_Object = MibScalar
batv = _Batv_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 2),
    _Batv_Type()
)
batv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batv.setStatus("current")


class _Bati_Type(DisplayString):
    """Custom type bati based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Bati_Type.__name__ = "DisplayString"
_Bati_Object = MibScalar
bati = _Bati_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 3),
    _Bati_Type()
)
bati.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bati.setStatus("current")


class _Btemp_Type(DisplayString):
    """Custom type btemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Btemp_Type.__name__ = "DisplayString"
_Btemp_Object = MibScalar
btemp = _Btemp_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 4),
    _Btemp_Type()
)
btemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btemp.setStatus("current")


class _Itemp_Type(DisplayString):
    """Custom type itemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Itemp_Type.__name__ = "DisplayString"
_Itemp_Object = MibScalar
itemp = _Itemp_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 5),
    _Itemp_Type()
)
itemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itemp.setStatus("current")


class _Loadv_Type(DisplayString):
    """Custom type loadv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Loadv_Type.__name__ = "DisplayString"
_Loadv_Object = MibScalar
loadv = _Loadv_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 6),
    _Loadv_Type()
)
loadv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadv.setStatus("current")


class _Loadi_Type(DisplayString):
    """Custom type loadi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Loadi_Type.__name__ = "DisplayString"
_Loadi_Object = MibScalar
loadi = _Loadi_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 7),
    _Loadi_Type()
)
loadi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadi.setStatus("current")


class _Pvv_Type(DisplayString):
    """Custom type pvv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Pvv_Type.__name__ = "DisplayString"
_Pvv_Object = MibScalar
pvv = _Pvv_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 8),
    _Pvv_Type()
)
pvv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvv.setStatus("current")


class _Pvi_Type(DisplayString):
    """Custom type pvi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Pvi_Type.__name__ = "DisplayString"
_Pvi_Object = MibScalar
pvi = _Pvi_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 9),
    _Pvi_Type()
)
pvi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvi.setStatus("current")


class _Loadstate_Type(DisplayString):
    """Custom type loadstate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Loadstate_Type.__name__ = "DisplayString"
_Loadstate_Object = MibScalar
loadstate = _Loadstate_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 10),
    _Loadstate_Type()
)
loadstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadstate.setStatus("current")
_Batvint_Type = Tenths
_Batvint_Object = MibScalar
batvint = _Batvint_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 11),
    _Batvint_Type()
)
batvint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batvint.setStatus("current")
_Batiint_Type = Tenths
_Batiint_Object = MibScalar
batiint = _Batiint_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 12),
    _Batiint_Type()
)
batiint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batiint.setStatus("current")
_Btempint_Type = Tenths
_Btempint_Object = MibScalar
btempint = _Btempint_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 13),
    _Btempint_Type()
)
btempint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btempint.setStatus("current")
_Itempint_Type = Tenths
_Itempint_Object = MibScalar
itempint = _Itempint_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 14),
    _Itempint_Type()
)
itempint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itempint.setStatus("current")
_Loadvint_Type = Tenths
_Loadvint_Object = MibScalar
loadvint = _Loadvint_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 15),
    _Loadvint_Type()
)
loadvint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadvint.setStatus("current")
_Loadiint_Type = Tenths
_Loadiint_Object = MibScalar
loadiint = _Loadiint_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 16),
    _Loadiint_Type()
)
loadiint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadiint.setStatus("current")
_Pvvint_Type = Tenths
_Pvvint_Object = MibScalar
pvvint = _Pvvint_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 17),
    _Pvvint_Type()
)
pvvint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvvint.setStatus("current")
_Pviint_Type = Tenths
_Pviint_Object = MibScalar
pviint = _Pviint_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 18),
    _Pviint_Type()
)
pviint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pviint.setStatus("current")
_Load_Type = Integer32
_Load_Object = MibScalar
load = _Load_Object(
    (1, 3, 6, 1, 4, 1, 45621, 3, 10, 19),
    _Load_Type()
)
load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    load.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPDIN3-MIB",
    **{"Tenths": Tenths,
       "tycon": tycon,
       "tpdin3": tpdin3,
       "product": product,
       "model": model,
       "firmwareVersion": firmwareVersion,
       "buildDate": buildDate,
       "monitor": monitor,
       "relay1": relay1,
       "relay2": relay2,
       "relay3": relay3,
       "relay4": relay4,
       "v1": v1,
       "v2": v2,
       "v3": v3,
       "v4": v4,
       "i1": i1,
       "i2": i2,
       "i3": i3,
       "i4": i4,
       "t1": t1,
       "t2": t2,
       "v1int": v1int,
       "v2int": v2int,
       "v3int": v3int,
       "v4int": v4int,
       "i1int": i1int,
       "i2int": i2int,
       "i3int": i3int,
       "i4int": i4int,
       "t1int": t1int,
       "t2int": t2int,
       "mppt": mppt,
       "mpptmodel": mpptmodel,
       "batv": batv,
       "bati": bati,
       "btemp": btemp,
       "itemp": itemp,
       "loadv": loadv,
       "loadi": loadi,
       "pvv": pvv,
       "pvi": pvi,
       "loadstate": loadstate,
       "batvint": batvint,
       "batiint": batiint,
       "btempint": btempint,
       "itempint": itempint,
       "loadvint": loadvint,
       "loadiint": loadiint,
       "pvvint": pvvint,
       "pviint": pviint,
       "load": load}
)
